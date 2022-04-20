import json

import requests


def get_data(base_url, params):
    r = requests.get(base_url, params=params)
    return r.json()['data']


def write_to_json(data):
    with open('reddit_comments_2.json', 'w') as f:
        json.dump(data, f, indent=4)


def main():
    url = 'https://api.pushshift.io/reddit/comment/search/'
    params = {"subreddit": "TheSimsBuilding", "sort": "desc", "sort_type": "created_utc"}
    data = get_data(base_url=url, params=params)

    dict_of_comments = {comment['created_utc']: comment['body'] for comment in data}

    print(dict_of_comments)
    write_to_json(data=dict_of_comments)


if __name__ == "__main__":
    main()
