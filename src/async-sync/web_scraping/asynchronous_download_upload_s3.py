import aiohttp
import asyncio
import time


async def download_file(url):
    print(f'Started downloading {url}')
    # session encapsulates connector instances in a connection pool
    # session supports async context managers i.e implemented __enter__, __exit__
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.read()
            print(f'Finished downloading {url}')
            return content


async def write_file(n, content):
    filename = f'scraped_files/async_{n}.html'
    with open(filename, 'wb') as f:
        print(f'Started writing {filename}')
        f.write(content)
        print(f'Finished writing {filename}')


async def scrape_task(n, url):
    content = await download_file(url)
    await write_file(n, content)


async def main():
    tasks = []
    for n, url in enumerate(open('urls.txt').readlines()):
        tasks.append(scrape_task(n, url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t = time.perf_counter()
    asyncio.run(main())
    t = time.perf_counter() - t
    print(f'Total time taken: {t:0.2f} seconds')
