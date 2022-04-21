import concurrent
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import requests


def get_data(base_url, params):
    r = requests.get(base_url, params=params)
    return {params['subreddit']: r.json()['data']}


def write_to_json(file_name, data):
    with open(f'{file_name}.json', 'w') as f:
        json.dump(data, f, indent=4)


def main():
    url = 'https://api.pushshift.io/reddit/comment/search/'
    params = [{"subreddit": "TheSimsBuilding", "sort": "desc", "sort_type": "created_utc"},
              {"subreddit": "books", "sort": "desc", "sort_type": "created_utc"},
              {"subreddit": "funny", "sort": "desc", "sort_type": "created_utc"},
              {"subreddit": "AskReddit", "sort": "desc", "sort_type": "created_utc"}]

    # data = get_data(base_url=url, params=params)

    # dict_of_comments = {comment['created_utc']: comment['body'] for comment in data}
    t1 = datetime.now()

    # with concurrent.futures.ThreadPoolExecutor(2) as executor:
    #     threads = []
    #     elements = []
    #     for parameter in params:
    #         threads.append(executor.submit(get_data, url, parameter))
    #
    #     for thread in concurrent.futures.as_completed(threads):
    #         try:
    #             elements.append(thread.result())
    #         except StopIteration:
    #             break

    with concurrent.futures.ProcessPoolExecutor(2) as executor:
        processes = []
        elements = []
        for parameter in params:
            processes.append(executor.submit(get_data, url, parameter))

        for process in concurrent.futures.as_completed(processes):
            try:
                elements.append(process.result())
            except StopIteration:
                break

    for element in elements:
        for key, value in element.items():
            file_name = key
            data = value
            write_to_json(file_name=file_name, data=data)

    t2 = datetime.now() - t1
    print(t2)

if __name__ == "__main__":
    main()
