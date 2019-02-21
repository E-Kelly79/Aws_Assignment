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

    for instance in running_instances:
        dns = instance.public_dns_name
        try:
            run("ssh -i keys.pem ec2-user@" + dns + " touch testing.txt", shell=True)
            run("scp -i keys.pem main.py ec2-user@" + dns + ":/tmp", shell=True)
            # run("ssh -i keys.pem ec2-user@" + dns + " python3 /tmp/main.py", shell=True)

        except Exception as error:
            print(error)

