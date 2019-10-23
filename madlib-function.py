def lambda_handler(event, context):
    body = event['body']
    name = body['name']
    place = body['place']
    verb1 = body['verb1']
    noun = body['noun']
    verb2 = body['verb2']
    sentence = 'One day, there was a person named ' + str(name) + '. ' + str(name) + ' wanted to go to a ' + str(place) + \
    ' to ' + str(verb1) + ' as an undercover spy. However, ' + str(name) + ' ran into a ' + str(noun) + \
    ' and woke up with the ability to ' + str(verb2) + '.'
    return {
        'statusCode': 200,
        'body': json.dumps(sentence)
    }