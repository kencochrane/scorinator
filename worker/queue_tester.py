#!/usr/bin/env python

import json
from queue import enqueue_analytics


def go():
    project = {
        'repo_url': 'https://github.com/kencochrane/scorinator.git'
    }

    value = enqueue_analytics(json.dumps(project))
    print(value)


if __name__ == '__main__':
    print('Start test')
    go()