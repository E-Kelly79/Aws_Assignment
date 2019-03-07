#!/usr/bin/env python3
import boto3
s3 = boto3.resource("s3")

""" 
    A simple python program to create a bucket
    with the give argument passed into the function
 """


def createBucket(bucket_name):
    try:
        response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
        print("A bucket was created with the name " + bucket_name)
    except Exception as error:
        print("Your bucket was not created because of the following reason " + error)
