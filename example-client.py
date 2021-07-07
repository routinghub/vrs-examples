#!/usr/bin/env python3
import requests
import json
import time
import sys
import os
import logging


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


def main():
    BRANCH = '-devel'
    HOST = 'https://routinghub.com'
    ENDPOINT = '{}/api/routing/v1{}'.format(HOST, BRANCH)
    APIKEY = os.environ.get("APIKEY")
    if APIKEY is None:
        logging.error("APIKEY environment variable is required")
        sys.exit(1)
    AUTH_HEADERS = {'Authorization': 'Bearer {}'.format(APIKEY)}

    logging.info('submitting task from stdin to {}'.format(ENDPOINT))

    request = sys.stdin.read()
    response = requests.post('{}/add'.format(ENDPOINT), data=request, headers=AUTH_HEADERS)

    logging.info('submitted task, response: {}'.format(response.text))

    task_id = response.json()["id"]
    result_url = '{}/result/{}'.format(ENDPOINT, task_id)

    logging.info('polling task result at url: {}'.format(result_url))

    response = requests.get(result_url, headers=AUTH_HEADERS)
    while response.status_code not in (200, 500):
        response = requests.get(result_url, headers=AUTH_HEADERS)
        time.sleep(0.5)

    logging.info('printing solution to stdout')

    print(json.dumps(response.json(), indent=2))

    logging.info('solution map url: https://routinghub.com/static/tools/route.html?task_id={}&apikey={}'.format(task_id, APIKEY))


if __name__ == '__main__':
    setup_logging()
    main()
