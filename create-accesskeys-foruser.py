import boto3

def lambda_handler(event, context):
    # Replace 'YOUR_USER_NAME' with the actual IAM user name
    user_name = 'YOUR_USER_NAME'
    
    # Create an IAM client
    iam = boto3.client('iam')
    
    # Create a new access key for the user
    response = iam.create_access_key(UserName=user_name)
    
    # Extract the new access key and secret access key
    access_key_id = response['AccessKey']['AccessKeyId']
    secret_access_key = response['AccessKey']['SecretAccessKey']
    
    # Return the new access key details
    return {
        'AccessKeyId': access_key_id,
        'SecretAccessKey': secret_access_key
    }

#Make sure to replace 'YOUR_USER_NAME' with the actual IAM user 
