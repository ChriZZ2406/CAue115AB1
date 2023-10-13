import boto3
import uuid
from urllib.parse import urlencode

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # S3-Bucket-Name
    bucket_name = 'ue114-lambda-0815'
    
    try:
        message = event['body']  # Vorausgesetzt, der POST-Anfragekörper enthält die Nachricht
        # Generieren Sie einen zufälligen Dateinamen mithilfe von UUID
        random_file_name = str(uuid.uuid4())
        s3.put_object(Bucket=bucket_name, Key=random_file_name, Body=message)
        
        # Erstellen Sie die genaue URL, die die GET-Funktion triggert
        api_gateway_endpoint = "7bum3axlfe.execute-api.eu-central-1.amazonaws.com"  # Ändern Sie dies entsprechend Ihrer API Gateway Konfiguration
        get_url = f"https://{api_gateway_endpoint}/lambdauue114get/{random_file_name}"
        
        return {
            'statusCode': 200,
            'body': f'Nachricht erfolgreich in S3 mit zufälligem Dateinamen gespeichert. Die GET-URL ist: {get_url}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }