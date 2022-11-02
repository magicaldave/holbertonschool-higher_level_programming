#!/usr/bin/python3
"""gets the last 10 commits from repo"""

if __name__ == "__main__":
    from sys import argv
    import requests

    payload = {'per_page': 2, 'page': 1}

    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        argv[1], argv[2]),
                     params=payload,
                     timeout=10)

    for commit in r.json():
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
    # commit_list = []
    # for commit in r.json():
    #    sha = commit.get("sha")
    #    author = commit.get("commit", {}).get("author", {}).get("name")
    #    commit_list.append("{}: {}".format(sha, author))

    # for i in commit_list:
    #    print(i)
