import requests

base_url = "https://api.pushshift.io/reddit/comment/search/"


def main():
    resp = requests.get(base_url)
    data = resp.text
    with open('robots.txt', 'w') as f:
        f.write(data)
        print('Added successfully')


if __name__ == '__main__':
    main()
