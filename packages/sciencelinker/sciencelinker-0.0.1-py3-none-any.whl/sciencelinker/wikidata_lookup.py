#!/bin/python3

#################################################################
# This file is part of the ScienceLinker module.
# The module provides functionality relevant to ScienceLinker.
#################################################################

import sciencelinker._lookup

WIKIDATA_ENDPOINT = 'https://query.wikidata.org/sparql'


def wikidata_lookup_types(list_like, language=None):
    return sciencelinker._lookup.find_types(WIKIDATA_ENDPOINT, list_like, language=language)


def wikidata_lookup_properties(target_type, identifying_property, values, language=None):
    return sciencelinker._lookup.find_properties(WIKIDATA_ENDPOINT, target_type, identifying_property, values,
                                                 language=language)


def wikidata_enrich(target_type, identifying_property, requested_property, l_values, missing_value='missing',
                    language=None):
    return sciencelinker._lookup.enrich(WIKIDATA_ENDPOINT, target_type, identifying_property, requested_property,
                                        l_values, missing_value, language=language)
