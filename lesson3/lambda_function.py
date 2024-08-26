from HelloBlazePreprocessLambda import preprocess
import json
def lambda_handler(event, context):
    preprocess(event['s3-dataset-uri'])
    return {
        'statusCode': 200,
        'body': "Good to go!"
    }