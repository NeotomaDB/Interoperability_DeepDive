import re

def process_hits(input: dict) -> dict:
    response = []
    for i in input:
        for j in i.get('highlight'):
            doi = i.get('doi', '') or ''
            snippet = j or ''
            title = i.get('title', '') or ''
            journal = i.get('pubname', '') or ''
            response.append({'doi': doi,
                             'snippet': re.sub('\n', '', snippet),
                             'pubname': re.sub('\n', '', journal),
                             'title': re.sub('\n', '', title)})
    return response
