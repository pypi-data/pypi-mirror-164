#!/bin/python3
import SPARQLWrapper

type_frequency_query_template = '''
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?type ?p (COUNT( ?p ) AS ?cnt) WHERE
{ 
    ?s a ?type .
    ?s ?p ?text .
    VALUES(?text)
    {
$(VALUES)
    }
}
GROUP BY ?type ?p
ORDER BY DESC(?cnt)
'''

other_properties_query_template = '''
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?additional_property (COUNT(DISTINCT ?match_value) AS ?cnt) WHERE
{ 
    ?s a <$(TYPE)> .
    ?s <$(MATCH_PROPERTY)> ?match_value .
    ?s ?additional_property ?some_value .
    FILTER (isLiteral(?some_value)) 
    VALUES(?match_value)
    {
        $(VALUES)
    }
}
GROUP BY ?additional_property
ORDER BY DESC(?cnt)
'''

enrich_query_template = '''
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?match_value ?target_value WHERE
{ 
    ?s a <$(TYPE)> .
    ?s <$(MATCH_PROPERTY)> ?match_value .
    ?s <$(ADDITIONAL_PROPERTY)> ?target_value .
    FILTER (isLiteral(?target_value))
    VALUES(?match_value)
    {
        $(VALUES)
    }
}
'''


def hello():
    print('Hello')


def execute_query(endpoint, query):
    sparql = SPARQLWrapper.SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(SPARQLWrapper.JSON)
    sparql.setMethod('POST')
    sparql.setMethod('POSTDIRECTLY')
    results = sparql.query().convert()
    return results


def find_types(endpoint, l_values, language=None):
    values_str = ''
    indent = '        '
    language_tag = ''
    if language is not None:
        language_tag = '@' + language
    for value in set(l_values):
        values_str += indent + '("' + str(value) + '"' + language_tag + ')\n'
    query = type_frequency_query_template.replace('$(VALUES)', values_str)

    print(query)
    results = execute_query(endpoint, query)
    print(results)
    l_candidate_types = []
    if len(results) == 0:
        return []
    else:
        for row in results["results"]["bindings"]:
            l_candidate_types.append([str(row['type']['value']), str(row['p']['value']), int(row['cnt']['value'])])

    frequency_index = 2
    l_candidate_types.sort(key=lambda x: x[frequency_index], reverse=True)
    return l_candidate_types


def find_properties(endpoint, target_type, identifying_property, l_values, language=None):
    indent = '        '
    language_tag = ''
    if language is not None:
        language_tag = '@' + language
    values_str = ''
    for value in set(l_values):
        values_str += indent + '("' + str(value) + '"' + language_tag + ')\n'

    query = other_properties_query_template.replace('$(TYPE)', target_type)
    query = query.replace('$(MATCH_PROPERTY)', identifying_property)
    query = query.replace('$(VALUES)', values_str)
    print(query)
    results = execute_query(endpoint, query)
    l_candidate_preds = []
    if len(results) == 0:
        return []
    else:
        for row in results["results"]["bindings"]:
            l_candidate_preds.append([str(row['additional_property']['value']), int(row['cnt']['value'])])
    return l_candidate_preds


def enrich(endpoint, target_type, identifying_property, requested_property, l_values, missing_value, language=None):
    indent = '        '
    language_tag = ''
    if language is not None:
        language_tag = '@' + language

    values_str = ''
    for value in set(l_values):
        values_str += indent + '("' + str(value) + '"' + language_tag + ')\n'

    query = enrich_query_template.replace('$(TYPE)', target_type)
    query = query.replace('$(MATCH_PROPERTY)', identifying_property)
    query = query.replace('$(ADDITIONAL_PROPERTY)', requested_property)
    query = query.replace('$(VALUES)', values_str)
    print(query)
    results = execute_query(endpoint, query)
    d = {}
    if len(results) == 0:
        return []
    else:
        for row in results["results"]["bindings"]:
            d[str(row['match_value']['value'])] = str(row['target_value']['value'])
    l_target_values = []
    for value in l_values:
        if value in d:
            l_target_values.append(d[value])
        else:
            l_target_values.append(missing_value)
    return l_target_values, d
