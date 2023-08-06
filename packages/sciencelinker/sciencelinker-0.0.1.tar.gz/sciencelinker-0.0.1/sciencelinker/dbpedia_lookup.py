#!/bin/python3

#################################################################
# This file is part of the ScienceLinker module.
# The module provides functionality relevant to ScienceLinker.
#################################################################

import sciencelinker._lookup

DBPEDIA_ENDPOINT = 'https://dbpedia.org/sparql'


def dbpedia_lookup_types(list_like, language=None):
    return sciencelinker._lookup.find_types(DBPEDIA_ENDPOINT, list_like, language=language)


def dbpedia_lookup_properties(target_type, identifying_property, values, language=None):
    return sciencelinker._lookup.find_properties(DBPEDIA_ENDPOINT, target_type, identifying_property, values,
                                                 language=language)


def dbpedia_enrich(target_type, identifying_property, requested_property, l_values, missing_value='missing',
                   language=None):
    return sciencelinker._lookup.enrich(DBPEDIA_ENDPOINT, target_type, identifying_property, requested_property,
                                        l_values, missing_value, language=language)
