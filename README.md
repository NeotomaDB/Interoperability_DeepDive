# Examining Interoperability Among Databases

This project leverage xDeepDive to understand the intersection between existing paleo-data community resources such as the Neotoma Paleoecology Database, Global Paleofire Database or WorldClim. We use a list of terms compiled from researcher interviews that indicate likely sources of data used by researchers working in Holocene/Quaternary studies across a range of disciplines. Included in this set of terms are various tools associated with these different data resources.

The full list of terms and links used in the xDeepDive snippets search is in the [data folder](./data/merged_records.csv). We have 51 different resources identified from the interviews and 148 unique terms associated with these resources. Terms include URLs (e.g., `neotomadb.org` for the Neotoma Paleoecology Database), programming libraries (e.g., `rgbif` for the Global Biodiversity Information Facility) and alternate names, including initializations (e.g., APD for the African Pollen Database).

Using the xDeepDive snippets API we [search for these terms](./src/interop_dd.py) to build a large table of DOIs, text snippets and database terms. Initial testing shows this table to be quite large (>100k rows), in part because some resources have low specificity in their naming.

## **Contributors**

This project is an open project, and contributions are welcome from any individual. All contributors to this project are bound by a [code of conduct](./CODE_OF_CONDUCT.md). Please review and follow this code of conduct as part of your contribution.

- [![ORCID](https://img.shields.io/badge/orcid-0000--0002--2700--4605-brightgreen.svg)](https://orcid.org/0000-0002-2700-4605) Simon Goring

### Tips for Contributing

Issues and bug reports are always welcome. Code clean-up, and feature additions can be done either through pull requests to [project forks](https://github.com/NeotomaDB/Interoperability_DeepDive/network/members) or [project branches](https://github.com/NeotomaDB/Interoperability_DeepDive/branches).

All products of the Neotoma Paleoecology Database are licensed under an [MIT License](LICENSE) unless otherwise noted.

## Using the Repository

The repository is coded in Python and managed using the [uv Package Manager](https://docs.astral.sh/uv/). To run a script, first clone the repository and then, at the command line enter:

```bash
uv install
```

to install all neccessary dependencies.

To run one of the two main scripts run either:

```bash
uv run src/interop_dd.py
```

or

```bash
uv run src/networkgraph.py
```

### `interop_dd`: Harvesting Snippets

The script to obtain text snippets is within the [src/interoperability_deepdive](./src/interoperability_deepdive) folder. These scripts:

1. Build the API URL -- [gdd_snippets](./src/interoperability_deepdive/gdd_snippets.py)
2. Page through the results list -- [gddURLcall](./src/interoperability_deepdive/gddURLcall.py)
3. Process the JSON response from the API -- [process_hits](./src/interoperability_deepdive/process_hits.py)

The resulting object is a `list` of `dict` items, structured to be submitted to a CSV file with the following structure:

| DOI | highlight | title | resource |
| --- | --------- | ----- | -------- |
| 10.1016/j.epsl.2018.10.016 | "identiﬁed using several publications (see supplementary information), the African Pollen Database, and" | The roles of climate and human land-use in the late Holocene rainforest crisis of Central Africa | African Pollen Database |
| 10.1016/j.crte.2008.12.009 | cm2 pe r year. The determination of 116 pollen taxa was made using the African Pollen Database reference | Climate and environmental change at the end of the Holocene Humid Period: A pollen record off Pakistan | African Pollen Database |

From this table we can manually examine records to assess match quality.

## Processing Results

To effectively build the network model for these resources we look to _co-occurrence_ of resources in publications. For example:

| DOI | highlight | title | resource |
| --- | --------- | ----- | -------- |
| 10.1016/j.tree.2010.10.007 | databases, most notably those of North American Pollen Database (NAPD), European Pollen Database (EPD) | Exploring vegetation in the fourth dimension | European Pollen Database |
| 10.1016/j.tree.2010.10.007 | reviewed data from 36 beetle assemblages from Britain that are held in the BugsCEP database (http://www.bugscep.com) and exploited the specific | Exploring vegetation in the fourth dimension | BugsCEP |

Would indicate co-citation of the European Pollen Database and BugsCEP. A significant challenge in this analysis is knowing whether or not co-citation explicitly includes co-analysis of data (which may involve cross-walking and data translation). This work is challenging because of the structure of the xDeepDive API (which only returns individual "snippets", or sentences) and because of citation and data use patterns in publication.

Ultimately, the scripts first search for text strings, and then process the returned results (in the `data/xdd_results` folder) into a single csv file containing only DOIs that report more than one data resource.

The output data -- [`data/doi_centric.json`](./data/doi_centric.json) -- is a JSON object with the following structure:

```json
[
  {
    "doi": {
        "type": "string",
        "pattern": "/^10.\d{4,9}/[-._;()/:A-Z0-9]+$/i"
    },
    "resources": {
        "type": "array",
        "minLength": 2,
        "items": {
            "type": "string"
        }
    }
  }
]
```

## Statistical Analysis

We care about several key measures: