import json
import datetime

globaltext ='Hello World from globaltext'

def handler(event, context):
    data = {
        'output': globaltext,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
