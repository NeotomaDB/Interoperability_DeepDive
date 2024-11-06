def process_hits(input: dict) -> dict:
    response = []
    for i in input:
        for j in i.get('highlight'):
            response.append({'doi': i.get('doi'), 'snippet': j})
    return response

