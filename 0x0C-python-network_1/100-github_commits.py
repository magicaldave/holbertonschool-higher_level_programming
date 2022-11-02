#!/usr/bin/python3
"""gets the last 10 commits from repo"""

if __name__ == "__main__":
    from sys import argv
    import requests

    commit_list = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1]),
        params={
            'per_page': 10,
            'page': 1
        },
        timeout=10).json()

    for commit in commit_list:
        print(
            commit.get('sha') + ': ' +
            commit.get('commit').get('author').get('name'))
