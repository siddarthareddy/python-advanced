import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from datetime import datetime

from dateutil.tz import tzutc

s3 = boto3.resource('s3')
try:
    bucket = s3.Bucket('my-bucket')
    print(f'bucket: type: {type(bucket)}, obj:{bucket}')
    for obj in bucket.objects.all():
        print(obj.key, obj.last_modified)
except ClientError as e:
    print(e.response)

bucket = s3.Bucket('siddarthareddy')
print(f'bucket: type: {type(bucket)}, obj:{bucket}')


# upload a object
# with open('a.png', 'rb') as data:
#     bucket.Object('new.png').put(Body=data)

# download an object
for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)


# to print all objects in all buckets
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    for obj in bucket.objects.all():
        print(bucket.name, obj.key)

print(f"obj: {obj}")
# to download a particular object
# create bucket and object objects,
# these are local objects, no remote calls are made
# remote calls are performed lazily

try:
    bucket = s3.Bucket('siddarthareddy')
    obj = bucket.Object('a.txt')
    data = obj.get()['Body'].read().decode('ascii')
    print(data)
except Exception as e:
    print(f"exception occured: {e.response}")


try:
    s3_client = boto3.client('s3')
    resp = s3_client.get_object(Bucket='siddarthareddy',
                                Key='a.txt')['Body'].read().decode('ascii')
    print(resp)
except:
    print("exception occured")


def topic_queue():
    sns = boto3.resource('sns')
    # Create SNS topic - idempotent
    topic = sns.crate_topic(Name='boto3')

    # Get an SNS topic
    topic = sns.Topic('<TOPIC ARN>')

    sqs = boto3.resource('sqs')
    # Create SQS queue - idempotent
    queue = sqs.crate_queue(Name='boto3')

    # Get an existing queue
    queue = sqs.get_queue_by_name(QueueName='boto3')

    # to get messages into the queue from a topic
    # Subscribe an SQS queue to the topic

    topic.subscribe(
        Protocol='sqs',
        Endpoint=queue.attributes['QueueArn']
    )


def func():
    # is this how we should do type hinting here?
    # using base class of dynamically generated classes?
    # evnet that doesn't help in the functions which are dynamic class specific
    s3 = boto3.client('s3')
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
    # this is a test commit to test branch