#!/usr/bin/python
import subprocess

import boto3
import os
from filter_instance import filter_instance

def get_user_data(filename = 'user_data.sh'):
    template = open(filename).read()
    return template

def createinstance(bucket_name):
    ec2 = boto3.resource('ec2')
    file_exists = os.path.isfile('keys.pem')

    # Create a key-pair for the created instance if the file does not exist
    if not file_exists:
        file = open('keys.pem', 'w')
        key = ec2.create_key_pair(KeyName='assigment')
        key_pair = str(key.key_material)
        file.write(key_pair)

    # subprocess.run("sudo chmod 400 keys.pem", shell=True)

    # Run some scripts to install the apache web server on the created instance
    user_script =  get_user_data() % bucket_name

    # Create an instance under the assignment security group
    instance = ec2.create_instances(
        ImageId='ami-0bdb1d6c15a40392c',
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName='assigment',
        SecurityGroups=[
            'Assignment'
        ],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Cloud Assignment'
                    },
                ]
            }
        ],
        UserData=user_script
    )
    print("We are starting your EC2 instance please wait\n")
    instance[0].wait_until_running()
    instance[0].reload()
    print("An instance has been created wit the id " + instance[0].id)
    print("Instance has now started\nBeginning to install apache web server")
    running_instance = instance[0].id
    filter_instance(running_instance)
