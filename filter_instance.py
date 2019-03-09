import time

import boto3
from subprocess import *

ec2 = boto3.resource("ec2")


# Loop trough the running instances and filter them by the giving instance id
def filter_instance(instance_id):
    running_instances = ec2.instances.filter(Filters=[{
        'Name': 'instance-id',
        'Values': [instance_id]}])

    for instance in running_instances:
        instance.wait_until_running()
        instance.reload()
        time.sleep(10)
        dns = instance.public_dns_name
        # install python3 o the running instance and then run the check web server file to see if the server is running
        try:
            run("ssh -t -o StrictHostKeyChecking=no -i keys.pem ec2-user@" + dns + " sudo yum install python3 -y", shell=True)
            run("scp -i keys.pem check_webserver.py ec2-user@" + dns + ":.", shell=True)
            run("ssh -i keys.pem ec2-user@" + dns + " sudo yum install git -y", shell=True)
            run("ssh -i keys.pem ec2-user@" + dns + " git clone https://github.com/E-Kelly79/Aws_Assignment.git", shell=True)
            run("ssh -i keys.pem ec2-user@" + dns + " python3 check_webserver.py", shell=True)



        except Exception as error:
            print(error)

