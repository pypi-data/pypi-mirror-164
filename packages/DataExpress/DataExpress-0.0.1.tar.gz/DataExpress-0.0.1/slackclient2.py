
import os
from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(token="xoxb-3965339375411-3951626502663-PPjuIsDc7W72wmijpKhiHDUz")

try:
    filepath="C:\SERVER_DASA\BI\PRD\Log\MULTIMED_LOG_LOTE0000124_20220819193434.json"
    response = client.files_upload(
        channels='#dasabi-notification',
        file=filepath)
    assert response["file"]  # the uploaded file
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")