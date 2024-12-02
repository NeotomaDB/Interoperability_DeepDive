import re

def process_hits(input: dict) -> dict:
    response = []
    for i in input:
        for j in i.get('highlight'):
            doi = i.get('doi', '') or ''
            snippet = j or ''
            title = i.get('title', '') or ''
            response.append({'doi': doi,
                             'snippet': re.sub('\n', '', snippet),
                             'title': re.sub('\n', '', title)})
    return response
