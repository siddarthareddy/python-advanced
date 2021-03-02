import requests
import time
import boto3
from botocore.exceptions import ClientError


def download_file(url):
    print(f'Started downloading {url}')
    response = requests.get(url)
    print(f'Finished downloading {url}')
    return response.content


def write_file(n, content):
    filename = f'scraped_files/sync_{n}.html'
    with open(filename, 'wb') as f:
        print(f'Started writing {filename}')
        f.write(content)
        print(f'Finished writing {filename}')


def upload_file(n, content):
    filename = f'scraped_files/sync/file_{n}.html'
    print(f"started uploading scraped_files/sync/file_{n}.html")
    bucket.Object(filename).put(Body=content)
    print(f"finished uploading scraped_files/sync/file_{n}.html")


if __name__ == '__main__':
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('siddarthareddy')
    print(f'bucket: type: {type(bucket)}, obj:{bucket}')
    # for obj in bucket.objects.all():
    #     print(obj.key, obj.last_modified)

    t = time.perf_counter()
    for n, url in enumerate(open('urls.txt').readlines()):
        content = download_file(url)
        upload_file(n, content)
    t = time.perf_counter() - t
    print(f'Total time taken: {t:0.2f} seconds')
