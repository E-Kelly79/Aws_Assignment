#!/usr/bin/env python3
import boto3

s3 = boto3.resource("s3")

#Take a chosen file and add it to the create bucket
def addFileToBucket(bucket_name):
    file = "embed2.jpg"
    try:
        response = s3.Object(bucket_name, file).put(ACL='public-read', ContentType='image/jpeg', Body=open(file, 'rb'))
        print(response)
    except Exception as error:
        print(error)