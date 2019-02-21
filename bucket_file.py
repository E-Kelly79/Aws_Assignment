#!/usr/bin/env python3
import sys
import  boto3

s3 = boto3.resource("s3")
bucket_name = sys.argv[1]
file = sys.argv[2]

try:
    response = s3.Object(bucket_name, file).put(ACL='public-read', Body=open(file, 'rb'))
    print(response)
except Exception as error:
    print(error)