import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # S3-Bucket-Name
    bucket_name = 'ue114-lambda-0815'
    
    # Dateinamen aus der URL extrahieren
    file_name = event.get('pathParameters', {}).get('filename')  
    
    if not file_name:
        return {
            'statusCode': 400,
            'body': 'No filename provided'
        }

    try:
        # Dateiinhalt holen
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        content = response['Body'].read().decode('utf-8')
        
        # Datei nach dem Lesen löschen
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        
        return {
            'statusCode': 200,
            'body': content
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
