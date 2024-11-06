import csv
import interoperability_deepdive as iod

# This will generate a large-ish number of papers and grants.

with open('../data/term_records.csv', 'r') as terms:
    repositories = terms.read().splitlines()

for i in repositories:
    full_list = []
    print(i)
    full_list = full_list + iod.gdd_snippets(i)
    if len(full_list) > 0:
        with open('../data/repohits.csv', 'a', encoding='utf-8', newline="") as file:
            dictwriter = csv.DictWriter(file, full_list[0].keys())
            dictwriter.writerows(full_list)
