import boto3
import requests

def lambda_handler(event, context):
    # Replace 'YOUR_USER_NAME' with the actual IAM user name
    user_name = 'YOUR_USER_NAME'
    
    # Replace 'YOUR_MULESOFT_ENDPOINT' with the actual MuleSoft endpoint URL
    mulesoft_endpoint = 'YOUR_MULESOFT_ENDPOINT'
    
    # Create an IAM client
    iam = boto3.client('iam')
    
    # Create a new access key for the user
    response = iam.create_access_key(UserName=user_name)
    
    # Extract the new access key and secret access key
    access_key_id = response['AccessKey']['AccessKeyId']
    secret_access_key = response['AccessKey']['SecretAccessKey']
    
    # Prepare the payload for the MuleSoft request
    payload = {
        'access_key_id': access_key_id,
        'secret_access_key': secret_access_key
    }
    
    # Make a POST request to the MuleSoft endpoint
    response = requests.post(mulesoft_endpoint, json=payload)
    
    # Return the MuleSoft response
    return {
        'statusCode': response.status_code,
        'body': response.text
    }
