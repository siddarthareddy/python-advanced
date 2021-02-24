import boto3
from pprint import pprint
from datetime import datetime

from dateutil.tz import tzutc
from botocore.client import BaseClient

def func():
    # is this how we should do type hinting here?
    # using base class of dynamically generated classes?
    # evnet that doesn't help in the functions which are dynamic class specific
    s3: BaseClient = boto3.client('s3')
    # <class 'botocore.client.S3'>
    print(type(s3))
    # how do we get the function suggestions for such dynamically created class?
    # how would we know the functions available through IDE
    # type hinting doesn't seem to help here, as these are dynamically created types
    l = s3.list_objects(Bucket='siddarthareddy')
    print(type(l))
    # pprint(l)
    s3 = boto3.resource('s3')
    # <class 'boto3.resources.factory.s3.ServiceResource'>
    print(type(s3))
    bucket = s3.Bucket('siddarthareddy')
    print(bucket)
    print(type(bucket))
    buckets = s3.buckets
    # <class 'boto3.resources.collection.s3.bucketsCollectionManager'>
    print(type(buckets))
    # gets credentials for the account from
    # .aws/credentials, .aws/config
    print(buckets)
    # why is this returning a function call without evaluation
    # s3.bucketsCollectionManager(s3.ServiceResource(), s3.Bucket)
    for bucket in s3.buckets.all():
        print(bucket.name)

    s3 = boto3.client('s3')
    # <class 'botocore.client.S3'>
    print(type(s3))
    response = s3.list_buckets()
    print(type(response))
    # pprint(response)

    # upload new file
    # data = open('a.png', 'rb')
    # s3.Bucket('siddarthareddy').put_object(Key='first_image.png', Body=data)
    #
    # any examples of code generation?
    # taking json files and generating code from them


func()
