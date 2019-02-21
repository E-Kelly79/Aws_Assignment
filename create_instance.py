#!/usr/bin/python
import boto3
import os
from filter_instance import filter_instance

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
file_exisits = os.path.isfile('keys.pem')


user_script = """#!/bin/bash
    echo "Beginning to install apache" >> /tmp/log.txt
    sudo yum install httpd -y
    sudo systemctl enable httpd
    sudo service httpd start
    sudo yum install python3
    echo "<h2>Test page</h2>Instance ID: " > /var/www/html/index.html
    curl --silent http://169.254.169.254/latest/meta-data/instance-id/ >> /var/www/html/index.html
    echo "<br>Availability zone: " >> /var/www/html/index.html
    curl --silent http://169.254.169.254/latest/meta-data/placement/availability-zone/ >> /var/www/html/index.html
    echo "<br>IP address: " >> /var/www/html/index.html
    curl --silent http://169.254.169.254/latest/meta-data/public-ipv4 >> /var/www/html/index.html
    echo "<hr>Here is an image that I have stored on S3: <br>" >> /var/www/html/index.html
    echo "<img src=https://s3-eu-west-1.amazonaws.com/t1mm0/embed2.jpg>" >> /var/www/html/index.html
    echo "Apache was installed" >> /tmp/log.txt"""

# Create a key-pair for the created instance if the file does not exist
if not file_exisits:
    file = open('keys.pem', 'w')
    key = ec2.create_key_pair(KeyName='assigment')
    key_pair = str(key.key_material)
    file.write(key_pair)

# Create an instance under the assigment security group
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
print(instance[0].id)

running_instance = instance[0].id

filter_instance(running_instance)
