#!/usr/bin/env python3
import boto3

s3 = boto3.resource("s3")


#so this is looking for a prarm which is coming from the main file not in here but i could be wrong
def putfile(bucket_name):
    file = "embed2.jpg"
    try:
        response = s3.Object(bucket_name, file).put(ACL='public-read', ContentType='image/jpeg', Body=open(file, 'rb'))
        print(response)
    except Exception as error:
        print(error)