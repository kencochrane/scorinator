#!/usr/bin/env python

from queue import enqueue
import json

def go():
    project = {
        'repo_url': 'https://github.com/kencochrane/scorinator.git'
    }
    
    value = enqueue(json.dumps(project))
    print(value)


if __name__ == '__main__':
    print('Start test')
    go()