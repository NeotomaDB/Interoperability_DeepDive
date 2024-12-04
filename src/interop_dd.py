import csv
import interoperability_deepdive as iod
from interop_agg import interop_agg

# This will generate a large-ish number of papers and grants.

dbs = []

with open('./data/merged_records.csv', 'r', encoding='UTF-8') as terms:
    reader = csv.reader(terms)
    for i in reader:
        dbs.append([j.strip() for j in i])

for i in dbs:
    full_list = []
    print(i)
    try:
        full_list = full_list + iod.gdd_snippets(i[0])
        if len(full_list) > 0:
            with open(f'./data/resources/{i[1]}.csv', 'a', encoding='utf-8', newline="") as file:
                dictwriter = csv.DictWriter(file, full_list[0].keys())
                dictwriter.writerows(full_list)
    except Exception as e:
        print(e)

aggregate = interop_agg('data/resources')