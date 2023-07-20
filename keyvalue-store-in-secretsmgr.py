import boto3

def lambda_handler(event, context):
    # Replace 'YOUR_SECRET_NAME' with the actual name of your secret in AWS Secrets Manager
    secret_name = 'YOUR_SECRET_NAME'
    
    # Replace 'YOUR_KEY' and 'YOUR_VALUE' with the actual key-value pair you want to store
    key = 'YOUR_KEY'
    value = 'YOUR_VALUE'
    
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager')
    
    # Create or update the secret with the key-value pair
    response = client.put_secret_value(SecretId=secret_name, SecretString={key: value})
    
    # Return the response
    return response
