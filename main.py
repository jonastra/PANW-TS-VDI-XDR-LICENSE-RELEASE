#!/usr/bin/env python3

# Author: Jonas trand (jstrand@paloaltonetworks.com)
# Version 0.1

import requests
import json

ROOT_URL = ''   # FILL IN
API_ID = ''     # FILL IN
API_KEY = ''    # FILL IN

ENDPOINTS_TO_DELETE = []


def get_all_endpoints():
    url = "%s/public_api/v1/endpoints/get_endpoints/" % (ROOT_URL)

    payload = "{}"
    headers = {
        'x-xdr-auth-id': '%s' % (API_ID),
        'Authorization': '%s' % (API_KEY),
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        newResponse = json.loads(response.text)
    except Exception as e:
        return 'Error'

    for result in newResponse['reply']:
        if result['agent_status'] == 'DISCONNECTED' or result['agent_status'] == 'LOST':
            endpoint = result['agent_id']
            ENDPOINTS_TO_DELETE.append(endpoint)
    if not ENDPOINTS_TO_DELETE:
        exit()


def get_detailed_endpoints():
    url = "%s/public_api/v1/endpoints/get_endpoint/" % (ROOT_URL)
    data = {}
    data['request_data'] = {'filters': [{'field': 'endpoint_id_list',
                                         'operator': 'in', 'value': ENDPOINTS_TO_DELETE}]}
    json_data = json.dumps(data)
    payload = json_data
    headers = {
        'x-xdr-auth-id': '%s' % (API_ID),
        'Authorization': '%s' % (API_KEY),
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        newResponse = json.loads(response.text)
        print(newResponse)
    except Exception as e:
        return 'Error'


def delete_all_inactive_endpoints():
    url = "%s/public_api/v1/endpoints/delete/" % (ROOT_URL)
    data = {}
    data['request_data'] = {'filters': [{'field': 'endpoint_id_list',
                                         'operator': 'in', 'value': ENDPOINTS_TO_DELETE}]}
    json_data = json.dumps(data)
    payload = json_data
    headers = {
        'x-xdr-auth-id': '%s' % (API_ID),
        'Authorization': '%s' % (API_KEY),
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        newResponse = json.loads(response.text)
        print(newResponse)
    except Exception as e:
        return 'Error'


def main():
    get_all_endpoints()
    get_detailed_endpoints()
    # delete_all_inactive_endpoints()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('[INFO] User aborted.')
