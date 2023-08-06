#!/bin/python3

#################################################################
# This file is part of the ScienceLinker module.
# The module provides functionality relevant to ScienceLinker.
#################################################################

import requests
import urllib.parse
import json

SPOTLIGHT_ENDPOINT = 'https://api.dbpedia-spotlight.org'


def ner_spotlight_text(l_text, language):
    l_annotations = []
    r = None

    for text in l_text:
        params = urllib.parse.urlencode({'text': text})
        url = SPOTLIGHT_ENDPOINT + '/' + language + '/annotate'
        r = requests.get(url, params=params, headers={'Accept': 'application/json'})
        r.encoding = 'utf-8'

        if r.status_code == 200:
            d_results = json.loads(r.text)
            l_uris = []
            if 'Resources' in d_results:
                for resource in d_results['Resources']:
                    l_uris.append(resource['@URI'])
            l_annotations.append(l_uris)
        else:
            raise ('Spotlight returned status: ' + str(r.status_code)+'\n'+r.text)
    return l_annotations


def ner_spotlight_url(l_url, language):
    l_annotations = []
    r = None

    for query_url in l_url:
        params = urllib.parse.urlencode({'url': query_url})
        endpoint_url = SPOTLIGHT_ENDPOINT + '/' + language + '/annotate'
        r = requests.get(endpoint_url, params=params, headers={'Accept': 'application/json'})
        r.encoding = 'utf-8'

        if r.status_code == 200:
            d_results = json.loads(r.text)
            l_uris = []
            if 'Resources' in d_results:
                for resource in d_results['Resources']:
                    l_uris.append(resource['@URI'])
            l_annotations.append(l_uris)
        else:
            raise Exception('Spotlight returned status: ' + str(r.status_code)+'\n'+r.text)
    return l_annotations
