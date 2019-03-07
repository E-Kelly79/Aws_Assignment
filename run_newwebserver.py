import datetime

from create_bucket import createBucket
from create_instance import createinstance
from bucket_file import putfile


def main():
    bucket = input("Name your bucket: ")
    bucket = bucket.lower()
    micro_sec = datetime.datetime.now()
    now = str(micro_sec.microsecond)
    bucket_name = bucket + now
    createBucket(bucket_name)
    putfile(bucket_name)
    createinstance(bucket_name)


if __name__ == '__main__':
    main()
