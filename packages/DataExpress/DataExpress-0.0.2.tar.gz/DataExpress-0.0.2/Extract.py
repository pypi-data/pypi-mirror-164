import DE_LibUtil as U
import DE_DataBase as D
import DE_LogEventos as L
import DE_Parametros as P
import DE_Gera_Arquivos as G
import inspect
import os
import socket as sk
import datetime as dt
import json
import pandas as pd
import requests

lib = U.LIB()
db = D.DATABASE()
par = P.PARAMETROS()


class EXTRACAO:

    class_name = inspect.stack()[0].function
    log, logger = None, None

    def __init__(self, **kwargs):
        msglog, loginfo = None, None
        self._PID = lib.getPID()
        self._dthr_inicio_processo = dt.datetime.now()

        try:
            method_name = inspect.stack()[0].function
            # Analizando parametros recebidos
            if "nom_processo" in kwargs.keys():
                if "des_processo" not in kwargs.keys():
                    kwargs["des_processo"] = f"""Descritivo do processo não definido na inicialização da classe {self._class_name}, PID={self.PID}"""
                self._PROCESSO = []
                self._PROCESSO.append(kwargs["nom_processo"])
                self._PROCESSO.append(kwargs["des_processo"])

                # Obtendo parametros para processamento
                result = self._get_parametros()
                if result is not None:
                    raise result

                # criando um LOG para os eventos
                self._set_LogEventos()
                msglog = f"""Iniciando execucao do processo... [pid: {self._PID}]-{self._PROCESSO[0]}-{self._PROCESSO[1]}\n{log.Sublinhado}Lista de parametros utilizados para o processamento...\n{log.Italico}{json.dumps(self._PAR, indent=2)}"""
                log.Popula(logger=logger, level=log.INFO, content=msglog, function_name=method_name, cor=log.Verde_Claro_Fore)
            else:
                raise Exception(f"""Falha ao instanciar a classe {self._class_name}, para o processo {self._PROCESSO[0]}-{self._PROCESSO[1]}""")
            msglog = "Classe de extração instanciada, pronta para uso!"
            loginfo = log.INFO
        except Exception as error:
            msglog = error
            loginfo = log.ERROR
        finally:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name, cor=log.Verde_Claro_Fore)

    def Execute(self):
        global log, logger
        msglog, loginfo, method_name, result = "Iniciando execução do processo...", log.INFO, inspect.stack()[0].function, True
        try:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name, cor=log.Amarelo_Claro_Fore)
            self._arq = G.ARQUIVOS(**{"log":log, "logger":logger})
            # Iniciando a extração
            if self._PAR["ESTRATEGIA"]["origem_extracao"].upper() == "DATABASE":
                self._cnnORIGEM = None
                result = self._inicia_extracao_database()
                if not isinstance(result, bool):
                    raise Exception(result)
            elif self._PAR["ESTRATEGIA"]["origem_extracao"].upper() == "FILESYSTEM":
                pass
            elif self._PAR["ESTRATEGIA"]["origem_extracao"].upper() == "CLOUD":
                pass
            elif self._PAR["ESTRATEGIA"]["origem_extracao"].upper() == "URL":
                pass

            if result == False:
                raise Exception()
            #--------------------------------------------------------------------------
            # Os tipos possiveis ate o momento para extração de dados são os seguintes:
            # 1. Database
            # 2. fileSystem
            # 3. Cloud (GPC, AZURE, AWS)
            # 4. HTML
            # --------------------------------------------
            msglog = f"""Processo: [{self._PID}-{self._PROCESSO[0]}] concluido com exito!"""
            loginfo = log.INFO
            cor = log.Amarelo_Claro_Fore
        except Exception as error:
            loginfo = log.ERROR
            msglog = f"""ERRO==> [pid: {self._PID}]-{self._PROCESSO[0]}-{self._PROCESSO[1]} - {error}"""
            result = False
            cor = log.Vermelho_Claro_Fore
        finally:
            #dfPAR = pd.DataFrame.from_dict(data=self._PAR)
            msg = ''
            msgslack = self._onboarding_template_slack()
            self.post_message_to_slack(text=msg, token=self._PAR["SLACK"]["token"], channel=self._PAR["SLACK"]["channel"], icon_emoji=self._PAR["SLACK"]["icon_emoji"], blocks=msgslack, username=self._PAR["SLACK"]["user_name"])
            self._set_parametros()
            self._close_connections()
            msglog = f"""...Finalizando a execução do processo... {msglog}"""
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name, cor=cor)
            log.Finaliza(logger)
            return result

    def _inicia_extracao_database(self):
        where, delta, delta_segundos = None, None, None
        msglog, loginfo, method_name, result, cor = None, None, inspect.stack()[0].function, True, log.Cyan_Fore
        try:

            log.Popula(logger=logger, level=log.INFO, content="Iniciando extracao...", function_name=method_name, cor=cor)

            # 1. efetuar conexao com a origem
            self._cnnORIGEM = self._conecta_origem(sgbd=self._PAR["CONEXAO"]["database"].upper(), str_conexao=self._PAR["CONEXAO"])
            if isinstance(self._cnnORIGEM, str):
                raise Exception(self._cnnORIGEM)

            # 2. montar resumo do processamento para analise
            # monta um resumo do processamento para posterior utilizacao
            self._candidatas = self._set_resumo_processo()
            if isinstance(self._candidatas, str):
                raise Exception(self._candidatas)

            # 3. Montar as queries (metadados ou sql) para extração com seus respectivos filtros
            # Montas as querys para todos os objetos e popyla o dataframe com o conteudo a query
            self._monta_querys(df=self._candidatas, conexao=self._cnnORIGEM)

            # 4. Gerar arquivos (efetuar quebra por numero de linhas)
            self._extracao_dados(df=self._candidatas)

            msglog = f"""{cor}... Finalizando extracao!"""
            loginfo = log.INFO
            cor = log.Cyan_Fore
        except Exception as error:
            msglog = error
            loginfo = log.ERROR
            result = msglog
            cor = log.Vermelho_Claro_Fore
        finally:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name, cor=cor)
            return result

    # 1. Conexão com a base de dados de ORIGEM
    def _conecta_origem(self, sgbd: str, str_conexao: str):
        msglog, loginfo, method_name, result = None, log.INFO, inspect.stack()[0].function, None
        try:
            msglog = f"""Conectando com a base de ORIGEM: {self._PAR["CONEXAO"]["database"].upper()} - {self._PROCESSO[0]}!"""
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name, lf=False, cor=log.Azul_Fore)

            # 1. efetuar conexao com a origem
            if sgbd.upper() == "ORACLE":
                #self._cnnORIGEM = db.ORACLE(self._PAR["CONEXAO"])
                conexao = db.ORACLE(str_conexao)
            elif sgbd.upper() == "MYSQL":
                pass
            elif sgbd.upper() == "EXADATA":
                pass
            elif sgbd.upper() == "POSTGRES":
                pass
            elif sgbd.upper() == "AZURE":
                pass
            elif sgbd.upper() == "REDSHIFT":
                pass
            elif sgbd.upper() == "MSSQL":
                pass
            elif sgbd.upper() == "SQLITE":
                pass

            if isinstance(conexao, str):
                msglog = f"""Falha ao tentar conexão com a origem dos dados!"""
                raise Exception(msglog)

            msglog = f"""Conexao com a base de ORIGEM estabelecida!"""
            loginfo = log.INFO
            result = conexao
        except Exception as error:
            msglog = error
            loginfo = log.ERROR
            result = msglog
        finally:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name)
            return result

    # 2. montar resumo do processamento para analise
    # monta um resumo do processamento para posterior utilizacao
    def _set_resumo_processo(self):
        result, method_name, msglog, loginfo, cor = None, inspect.stack()[0].function, None, log.INFO, log.Azul_Fore
        try:
            log.Popula(logger=logger, level=log.INFO, content="Montando dataframe com os objetos candidatos e resumo do processo...", function_name=method_name, lf=False, cor=cor)
            df = pd.DataFrame(self._PAR["OBJETOS"])
            df["ext_dh_inicio"] = None
            df["ext_dh_fim"] = None
            df["ext_tempo"] = None
            df["ext_linhas_lidas"] = 0
            df["ext_stmt"] = None
            df["ext_file_size"] = None
            df["ext_file_qtd"] = None
            result = df
            loginfo = log.INFO
            msglog = f"""Resumo do processo montado!"""
        except Exception as error:
            loginfo = log.ERROR
            msglog = error
            result = msglog
        finally:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name)
            return result

    # 3. Montar as queries (metadados ou sql) para extração com seus respectivos filtros
    # Monta as querys para todos os objetos e popyla o dataframe com o conteudo a query
    def _monta_querys(self, df, conexao):
        msglog, loginfo, method_name, cor = None, None, inspect.stack()[0].function, log.Branco_Fore
        try:
            msglog = f"""Montando query´s para execução..."""
            log.Popula(logger=logger, level=log.INFO, content=msglog, function_name=method_name, cor=cor)
            for key in self._PAR["OBJETOS"]:
                if key["flg_processa"] == "S":
                    if key["estrategia"]["flg_tipo_carga"].upper() == 'INCREMENTAL':
                        if key["estrategia"]["data_type"].upper() in ["DATE", "DATETIME"]:
                            if key["estrategia"]["delta_range_type"] == 'segundos':
                                delta_segundos = 1
                            if key["estrategia"]["delta_range_type"] == 'minutos':
                                delta_segundos = 60
                            if key["estrategia"]["delta_range_type"] == 'horas':
                                delta_segundos = (60 * 60)
                            if key["estrategia"]["delta_range_type"] == 'dias':  # dias, semana, dezena, quinzena, mes, ano
                                delta_segundos = (60 * 60 * 24)
                            delta_inicial = dt.datetime.strptime(key["estrategia"]["ultimo_delta"], key["estrategia"]["formato"]) + dt.timedelta(
                                seconds=1)
                            delta_final = delta_inicial + (dt.timedelta(seconds=key["estrategia"]["delta_range"]) * delta_segundos) - dt.timedelta(
                                seconds=1)
                            where = f"""where {key["estrategia"]["nom_coluna"]} between TO_DATE('{delta_inicial}', 'YYYY-MM-DD HH24:MI:SS') and TO_DATE('{delta_final}', 'YYYY-MM-DD HH24:MI:SS')"""
                        elif key["estrategia"]["data_type"].upper() == "NUMBER":
                            delta_inicial = key["estrategia"]["ultimo_delta"] + 1
                            x = key["estrategia"]["delta_range"]
                            if x is None:
                                delta_final = 99999999999999
                            else:
                                delta_final = delta_inicial + key["estrategia"]["delta_range"]
                            where = f"""where {key["estrategia"]["nom_coluna"]} between {delta_inicial} and {delta_final}"""
                        else:
                            pass
                    elif key["flg_tipo_carga"].upper() == 'HISTORICA':
                        pass
                    msglog = f"""\t\t{key["nome_tabela"]}"""
                    log.Popula(logger=logger, level=log.INFO, content=msglog, function_name=method_name, lf=False, cor=log.Cinza_Claro_Fore)
                    md = db.METADATA(conexao=conexao,
                                     database=self._PAR["CONEXAO"]["database"].upper(),
                                     nome_tabela=key["nome_tabela"],
                                     owner=key["owner"].upper(),
                                     where=where
                                     )
                    msglog = f"""\n{md}\n Query montada!"""
                    log.Popula(logger=logger, level=log.INFO, content=msglog, function_name=method_name, cor=log.Cinza_Escuro_Fore)
                    df.loc[df["nome_tabela"] == key["nome_tabela"], "ext_stmt"] = md
            msglog = f"""Query´s montadas com sucesso!"""
            loginfo = log.INFO
            cor = log.Branco_Fore
        except Exception as error:
            msglog = error
            loginfo = log.ERROR
            cor = log.Vermelho_Claro_Fore
        finally:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name, cor=cor)

    # 4. gerar arquivos (efetuar quebra por numero de linhas)
    def _extracao_dados(self, df):
        msglog, loginfo, method_name, cor = None, None, inspect.stack()[0].function, log.Magenta_Claro_Fore
        try:
            log.Popula(logger=logger, level=log.INFO, content="Extraindo dados e gerando arquivos...", function_name=method_name, cor=cor)
            for index, value in df.iterrows():
                msglog = f"""\t{index} - {df.loc[index,"nome_tabela"]}"""
                log.Popula(logger=logger, level=log.INFO, content=msglog, function_name=method_name, cor=log.Branco_Fore)
                now = dt.datetime.now()
                df.loc[index, "ext_dh_inicio"] = str(now)
                stmt = df.loc[index]["ext_stmt"]
                cur = self._cnnORIGEM.cursor()
                cur.execute(stmt)
                header = lib.colunas_cursor(cur)
                filenumber = 0
                lines_read = 0
                while (True):
                    rows = cur.fetchmany(self._PAR["ESTRATEGIA"]["lines_fetch"])
                    if len(rows) == 0:
                        break
                    dfExtracao = pd.DataFrame(data=rows, columns=header)
                    filenumber = filenumber + 1
                    lines_read = lines_read + len(dfExtracao)
                    if len(dfExtracao) > 0:
                        df.loc[index, "ext_linhas_lidas"] = df.loc[index, "ext_linhas_lidas"] + len(dfExtracao)
                        # 5.1 - gera os arquivos baseado na extração (1 arquivo para cada paginação: self._PAR["ESTRATEGIA"]["lote"]["lines_page"]
                        file = df.loc[index, "export_file"]
                        status = []
                        for filetype in file["extencao"]:
                            # geracao dos arquivos retorna um dict:
                            # status = {"filename": full_filename, "size": size, "ext_inicio": str(ext_inicio), "ext_termino": str(ext_termino),
                            #                       "ext_tempo": str(ext_tempo), "msg": msg}
                            nome_tabela = df.loc[index, "nome_tabela"]
                            file_name = f"""{self._PROCESSO[0]}_LOTE{self._numero_proximo_lote:07}_{nome_tabela}_{filenumber:04}_{dt.datetime.now().strftime("%Y%m%d%H%M%S")}"""
                            file_path = os.path.join(self._PAR["root"], self._PAR["PATH"]["tgt_files"])
                            if "CSV" in filetype.upper():
                                file = self._arq.CSV(df=dfExtracao, file_path=file_path, file_name=file_name, file_sufix='', decimal=file["separador_decimal"], sep=file["delimitador_campos"], quotechar=file["quotedchar"], index=False)
                                status.append(file)
                            if "TXT" in filetype.upper():
                                file_path = file_path + "." + filetype
                            if  "JSON" in filetype.upper():
                                file_path = file_path + "." + filetype
                            if  "XLSX" in filetype.upper():
                                file_path = file_path + "." + filetype
                            if  "PARQUET" in filetype.upper():
                                file_path = file_path + "." + filetype
                cur.close()
                msglog = f"""{log.Cinza_Escuro_Fore}Arquivos gerados: {filenumber}, Linhas lidas: {lines_read}"""
                log.Popula(logger=logger, level=log.INFO, content=msglog, function_name=method_name)
                df.loc[index, "ext_file_qtd"] = str(filenumber)
                df.loc[index, "ext_dh_fim"] = str(dt.datetime.now())
                df.loc[index, "ext_tempo"] = str(dt.datetime.now() - now)
            msglog = f"""Fim da extração e geração dos arquivos"""
            loginfo = log.INFO
        except Exception as error:
            msglog = error
            loginfo = log.ERROR
        finally:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name, cor=cor)

    def _get_parametros(self):
        result = None
        method_name = inspect.stack()[0].function
        try:
            self._cnnPAR = db.SQLITE(database="c:\Projetos\db\DATAx.db")
            if not db.CONNECTION_VALID:
                msg = "Parametros para DATAx inexistentes!"
                raise Exception(msg)
            par = P.PARAMETROS(**{"conexao": self._cnnPAR, "table": "SYS_PAR"})
            parDICT = par.APLICACAO_get(['GERAL', self._PROCESSO[0].upper()])
            if isinstance(parDICT, str):
                raise Exception(parDICT)
            self._PAR = {}
            for key in parDICT:
                self._PAR[key["nom_variavel"]] = key["val_parametro"]
            # Definindo o numero do proximo lote
            self._numero_proximo_lote = int(self._PAR["ESTRATEGIA"]["lote"]["numero_ultimo_lote"]) + self._PAR["ESTRATEGIA"]["lote"]["incremento_lote"]
            # Definindo o ROOT_DIR
            if sk.gethostname() == self._PAR["HOST_APP"]:
                self._PAR["root"] = self._PAR["PATH"]["root_server"]
            else:
                self._PAR["root"] = self._PAR["PATH"]["root_local"]
        except Exception as error:
            result = error
        finally:
            return result

    def _set_parametros(self, status: str=None):
        msglog, loginfo, method_name, cor = None, None, inspect.stack()[0].function, log.DESTAQUE
        try:
            log.Popula(logger=logger, level=log.INFO, content="Salvando parametros", function_name=method_name, cor=cor)
            par = P.PARAMETROS(**{"conexao": self._cnnPAR, "table": "SYS_PAR"})
            # Atualizando parametro de resumo do processo
            inicio = self._dthr_inicio_processo
            termino = dt.datetime.now()
            resumo = self._PAR["RESUMO"]
            resumo["ultimo_processamento"]["pid"] = self._PID
            resumo["ultimo_processamento"]["dthr_inicio"] = str(inicio)
            resumo["ultimo_processamento"]["dthr_fim"] = str(termino)
            resumo["ultimo_processamento"]["tempo_ultima_execucao"] = str(termino - inicio)
            resumo["ultimo_processamento"]["tempo_medio"] = dt.datetime.strftime((termino - inicio) + dt.datetime.strptime(resumo["ultimo_processamento"]["tempo_ultima_execucao"], "%H:%M:%S.%f"), "%H:%M:%S.%f")
            resumo["ultimo_processamento"]["status"] = status
            xdf = self._candidatas.loc[self._candidatas["flg_processa"] == "S", ["nome_tabela", "export_file", "ext_dh_inicio", "ext_dh_fim", "ext_tempo", "ext_linhas_lidas"]]
            xdf.set_index("nome_tabela", inplace=True)
            resumo["extracao"] = xdf.to_dict(orient="index")
            par.PARAMETRO_set(nome_parametro=f"""{self._PROCESSO[0]}_RESUMO""", value=json.dumps(resumo, indent=4))
            # Atualizando parametro de LOTE de processamento
            lote = self._PAR["ESTRATEGIA"]["lote"]
            lote["numero_ultimo_lote"] = str(self._numero_proximo_lote)
            #lote["incremento_lote"] = lote["incremento_lote"]
            par.PARAMETRO_set(nome_parametro=f"""{self._PROCESSO[0]}_LOTE""", value=json.dumps(lote, indent=2))
            #lote["extracao"] = self._CANDIDATAS[""]
            msglog = f"""Parametros salvos!"""
            loginfo = log.INFO
        except Exception as error:
            msglog = error
            loginfo = log.ERROR
        finally:
            log.Popula(logger=logger, level=loginfo, content=msglog, function_name=method_name)

    def _set_LogEventos(self, **parametros):
        global log, logger
        result = None
        method_name = inspect.stack()[0].function
        try:
            self._cnnLOG = db.SQLITE("c:\Projetos\db\LOG.db")
            if isinstance(self._cnnLOG, object):
                log_file = os.path.join(self._PAR['root'], self._PAR["PATH"]["log_files"], f"""{self._PROCESSO[0]}_LOG_LOTE{self._numero_proximo_lote:07}_{dt.datetime.now().strftime("%Y%m%d%H%M%S")}.json""")
                self._PAR["LOG"]["nom_rotina"] = self._PROCESSO[0]
                self._PAR["LOG"]["nom_subrotina"] = self.class_name
                self._PAR["LOG"]["descricao"] = self._PROCESSO[1]
                processo = {"nom_rotina": self._PROCESSO[0],  # nome da rotina (obrigatorio)
                            "nom_subrotina": f"""{self.class_name}""",  # nome da subrotina (opcional)
                            "descricao": self._PROCESSO[1],  # descrição da rotina (HEADER do log)
                            "file": log_file,
                            "conexao_log": self._cnnLOG,  # conexão com o banco de dados
                            "nome_tabela_log": "LOG",  # nome da tabela de LOG (Header)
                            "nome_tabela_log_evento": "LOG_EVENT",
                            # nome da tabela onde serao gravados os eventos do log (a estrutura nao se pode mexer)
                            # "dataframe": pd, # objeto PANDAS
                            "device_out": ["screen", "file", "database"]
                            # ["screen", "database"|"memory", "file"]. Não permite utilizar "database" e "memory" simultaneamente
                            }
                log = L.LOG(**processo)
                logger = log.Inicializa()
            else:
                raise Exception("Problemas na conexão com o BD LOG")
        except Exception as error:
            result = error
        finally:
            return result

    def _close_connections(self):
        method_name = inspect.stack()[0].function
        log.Popula(logger=logger, level=log.INFO, content="Fechando conexões", function_name=method_name)
        self._cnnPAR.close()
        self._cnnORIGEM.close()


    # def modelo(self):
    #     result = None
    #     method_name = inspect.stack()[0].function
    #     try:
    #         pass
    #     except Exception as error:
    #         result = error
    #     finally:
    #         return result

    def _onboarding_template_slack(self):
        blocks = '''{
	"type": "modal",
	"title": {
		"type": "plain_text",
		"text": "My App",
		"emoji": true
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": true
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": true
	},
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Processo: ETL - CDPI/MULTIMAGEM\n• Inicio: 2022-08-19 23:45:55\n• Término: 2022-08-20 01:05:43"
			}
		},
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "😍 This is a header block 333",
				"emoji": true
			}
		}
	]
}'''
        # blocks = '''[{"type":"section",
        #      "text":{"type":"mrkdwn",
        #              "text": ":sorriso_olhos_arregalados: Processo: ETL - CDPI/MULTIMAGEM"
        #              }
        #      }
        #     ]'''
        return blocks

    def post_message_to_slack(self, token, channel, text, icon_emoji, username, blocks=None, url="https://slack.com/api/chat.postMessage" ):
        result = None
        x = blocks
        try:
            result =  requests.post(url,
                                 {'token': token,
                                  'channel': channel,
                                  'text': text,
                                  'icon_emoji': icon_emoji,
                                  'username': username,
                                  'blocks': blocks
                                  }
                                 ).json()
        except Exception as error:
            print(error)
        finally:
            return result

# 'blocks': '''[{"type":"section",
#             "text":{"type":"mrkdwn",
#                     "text": "teste 123456"
#                     }
#             }
#            ]

if __name__ == "__main__"    :
    processo = {"nom_processo": "MULTIMED",
                "des_processo": "Extração MULTIMED/CDPI"
                }
    x = EXTRACAO(**processo)
    x.Execute()