import requests
import time

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


if __name__ == '__main__':
    t = time.perf_counter()
    for n, url in enumerate(open('urls.txt').readlines()):
        content = download_file(url)
        write_file(n, content)
    t = time.perf_counter() - t
    print(f'Total time taken: {t:0.2f} seconds')


