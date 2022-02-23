import json

import requests


def get_data(base_url, params):
    r = requests.get(base_url, params=params)
    return r.json()


def write_to_json(data):
    with open('reddit_comments.json', 'w') as f:
        json.dump(data["data"], f, indent=4)


def main():
    url = 'https://api.pushshift.io/reddit/comment/search/'
    params = {"subreddit": "TheSimsBuilding", "sort": "desc", "sort_type": "created_utc"}
    data = get_data(base_url=url, params=params)
    write_to_json(data=data)


if __name__ == "__main__":
    main()
