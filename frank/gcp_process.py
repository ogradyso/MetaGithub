import requests
import gzip
import json
import datetime

from io import BytesIO
from concurrent.futures import ProcessPoolExecutor
from collections import Counter

HOST = 'data.gharchive.org'
BASE_URL = 'http://' + HOST + '/{}.json.gz'
START_DATE = datetime.datetime(2018, 7, 2, 0)
END_DATE = datetime.datetime(2018, 7, 2, 1)
DELTA = datetime.timedelta(hours=1)


def date_to_filename(date):
    filename = '{}-{:02d}-{:02d}-{}'.format(date.year, date.month, date.day, date.hour)
    return BASE_URL.format(filename)


urls = []
current_date = START_DATE
while current_date <= END_DATE:
    urls.append(date_to_filename(current_date))
    current_date = current_date + DELTA


def process_events(events):
    counts = Counter((event['type'] for event in events))
    print(counts)


def main():
    executor = ProcessPoolExecutor()
    for url in urls:
       executor.submit(process_url, url)
    executor.shutdown()


def process_url(url):
    print(url)
    with gzip.open(BytesIO(requests.get(url).content)) as f:
        process_events(json.loads(line.decode().strip()) for line in f)


if __name__ == '__main__':
    main()
