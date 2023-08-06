#!/bin/python3

#################################################################
# This file is part of the ScienceLinker module.
# The module provides functionality relevant to ScienceLinker.
#################################################################

import requests
import urllib.parse
import json

GEONAMES_ENDPOINT = 'https://secure.geonames.org/search'
MAX_ROWS = '30'
RETURN_TYPE = 'json'
USER_NAME = 'sltest'

REGION_TYPE_CITY_VILLAGE = 0
REGION_TYPE_PARK_AREA = 1
REGION_TYPE_COUNTRY_STATE_REGION = 2


def _retrieve_geodata(l_search_term, l_country_codes):
    query_terms = urllib.parse.quote(','.join(set(l_search_term)))

    url = GEONAMES_ENDPOINT + '?name=' + query_terms
    url += '&operator=OR'
    url += '&isNameRequired=true'
    for cc in l_country_codes:
        url += '&country=' + cc
    url += '&orderby=population'
    url += '&maxRows=' + MAX_ROWS
    url += '&type=' + RETURN_TYPE
    url += '&username=' + USER_NAME

    r = requests.get(url)

    if r.status_code == 200:
        d = json.loads(r.text)
        return d
    else:
        print('Status Code:')
        print(r.status_code)
        print(r.text)
        return None


def _select_geodata(d, l_search_term, min_population, region_type):
    d_res = {}
    for term in l_search_term:
        d_res[term] = 'missing'
    for entry in d['geonames']:
        if (entry['fclName'] == 'city, village,...' and region_type == REGION_TYPE_CITY_VILLAGE) or (
                entry['fclName'] == 'parks,area, ...' and region_type == REGION_TYPE_PARK_AREA) or (
                entry['fclName'] == 'country, state, region,...' and region_type == REGION_TYPE_COUNTRY_STATE_REGION):
            if entry['population'] >= min_population:
                for key in d_res:
                    if key in entry['name']:  # Find relevant key
                        if d_res[key] == 'missing':  # Existing entry was empty
                            d_res[key] = entry
                        elif d_res[key]['name'] == entry['name']:  # New entry is perfect match
                            d_res[key] = entry
                        else:
                            if len(d_res[key]['name']) > len(entry['name']):
                                d_res[key] = entry
    return d_res


def _prepare_geodata(l_query_terms, d):
    l_longitude = []
    l_latitude = []
    for t in l_query_terms:
        if d[t] == 'missing':
            l_longitude.append('missing')
            l_latitude.append('missing')
        else:
            l_longitude.append(d[t]['lng'])
            l_latitude.append(d[t]['lat'])
    return l_longitude, l_latitude, d


def geonames_lookup(l_search_term, l_country_codes, region_type, min_population):
    d_geo = _retrieve_geodata(l_search_term, l_country_codes)
    d_selected_data = _select_geodata(d_geo, l_search_term, min_population, region_type)
    l_long, l_lat, d = _prepare_geodata(l_search_term, d_selected_data)
    return l_long, l_lat
