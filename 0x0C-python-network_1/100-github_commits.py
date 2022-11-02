#!/usr/bin/python3
"""
Lists the last ten commits from a given repository
"""

if __name__ == "__main__":
    from sys import argv
    from requests import get

    commit_list = get('https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1]),
                      params={
                          'per_page': 10
                      },
                      timeout=10).json()

    for commit in commit_list:
        print(commit['sha'] + ': ' + commit['commit']['author']['name'])
