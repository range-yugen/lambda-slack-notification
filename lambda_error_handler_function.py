import json
import base64
import gzip
from urllib.request import Request, urlopen

import os

SLACK_WEBHOOK = <YOUR SLACK WEBHOOK URL>

def lambda_handler(event, context):
  
  payload = decode_logpayload(event)
  attachments = [{'text': f"{e['message']}"} for e in payload['logEvents']]
  slack_msg = {
    'text': f"{payload['logGroup']}",
    'attachments': attachments
  }
  
  # post the message
  req = Request(SLACK_WEBHOOK, json.dumps(slack_msg).encode('utf-8'))
  urlopen(req)

def decode_logpayload(event):

    compressed_payload = base64.b64decode(event['awslogs']['data'])
    uncompressed_payload = gzip.decompress(compressed_payload)
    return json.loads(uncompressed_payload)