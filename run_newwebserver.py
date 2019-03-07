import datetime
import time

from create_bucket import createBucket
from create_instance import createinstance
from bucket_file import addFileToBucket


def main():
    print("We are about to create a bucket you will be asked to give that bucket a name")
    time.sleep(2)

    # Name a bucket and add the micro second to the end of the bucket name for a unique name
    bucket = input("Please name your bucket: ")
    bucket = bucket.lower()
    micro_sec = datetime.datetime.now()
    now = str(micro_sec.microsecond)
    bucket_name = bucket + now

    # call the functions to create buckets and instances
    createBucket(bucket_name)
    addFileToBucket(bucket_name)
    createinstance(bucket_name)

# Run the main function when this file is called
if __name__ == '__main__':
    main()


