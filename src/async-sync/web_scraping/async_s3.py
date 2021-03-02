import aiohttp
import asyncio
import time
import boto3
import aioboto3


async def download_file(url):
    print(f'Strated downloading {url}')
    # session encapsulates connector instances in a connection pool
    # session supports async context managers i.e implemented __enter__, __exit__
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            print(f'Fininshed downloading {url}')
            return content


async def write_file(n, content):
    filename = f'scraped_files/async_{n}.html'
    with open(filename, 'wb') as f:
        print(f'Started writing {filename}')
        f.write(content)
        print(f'Finished writing {filename}')


async def upload_file(n, content, bucket):
    filename = f'scraped_files/async/file_{n}.html'
    print(f"started uploading scraped_files/async/file_{n}.html")
    await bucket.Object(filename).put(Body=content)
    print(f"finished uploading scraped_files/async/file_{n}.html")


async def scrape_task(n, url, bucket):
    content = await download_file(url)
    await upload_file(n, content, bucket)


async def main():
    tasks = []
    for n, url in enumerate(open('urls.txt').readlines()):
        tasks.append(scrape_task(n, url))
    await asyncio.wait(tasks)


async def main():
    async with aioboto3.resource('s3') as s3:
        bucket = await s3.Bucket('siddarthareddy')
        print(f'bucket: type: {type(bucket)}, obj:{bucket}')
        # for obj in bucket.objects.all():
        #     print(obj.key, obj.last_modified)

        t = time.perf_counter()
        asyncio.run(main())
        t = time.perf_counter() - t
        print(f'Total time taken: {t:0.2f} seconds')

