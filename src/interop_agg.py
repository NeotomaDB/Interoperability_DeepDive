import json
import os
import csv
import re
from collections import defaultdict

def interop_agg(path: str) -> list:
    """_Aggregate Resource List by DOI_

    Args:
        path (str): _A relative or complete path as a string._

    Returns:
        list: _A list of dict objects structured with kets `doi` and `resources`:
            {"doi":"XXX", "resources":["XXX","YYY"]}_
    """
    files = os.listdir(path)
    resources = []
    for i in files:
        filename = f"{os.getcwd()}/{path}/{i}"
        with open(filename, "r", encoding = "utf-8") as file:
            reader = csv.reader(file)
            for k in reader:
                j = [j for j in k]
                resources.append((j[0].strip(), re.sub(r'\.csv', '', i)))
    clean_res = list(set(resources))
    res = defaultdict(list)
    for key, val in sorted(clean_res, key=lambda tup: tup[0]):
        res[key].append(val)
    cleaned = [{"doi": i, "resources": list(set(res[i]))} for i in res if len(list(set(res[i]))) > 1]
    with open('data/doi_joined.json', 'w', encoding='utf-8') as file:
        json.dump(cleaned, file)
    return cleaned