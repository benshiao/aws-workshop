import json
from urllib.parse import parse_qs

def lambda_handler(event, context):
    print(type(event))
    print(event)
    body = event['body']
    print(type(body))
    print(body)
    
    body = parse_qs(body)
    
    name = body['name'][0]
    place = body['place'][0]
    verb1 = body['verb1'][0]
    noun = body['noun'][0]
    verb2 = body['verb2'][0]
    sentence = 'One day, there was a person named ' + str(name) + '. ' + str(name) + ' wanted to go to ' + str(place) + \
    ' to ' + str(verb1) + ' as an undercover spy. However, ' + str(name) + ' ran into a ' + str(noun) + \
    ' and woke up with the ability to ' + str(verb2) + '.'
    return {
        'statusCode': 200,
        'body': json.dumps(sentence)
    }


