from requests import get
from json import loads
from .process_hits import process_hits

def gddURLcall(url: str, verbose = False) -> list:
    """_Pass a formatted call to GDD and evaluate output._

    Args:
        url (str): _A fully constructed URL for a GeoDeepDive API call._

    Returns:
        list: _A list of the full set of results from a single GDD call._
    """
    call = get(url, timeout=10)
    outcome = []
    if call.status_code == 200:
        output = loads(call.content)
        maxhits = output.get('success').get('hits')
        if verbose:
            print(f"Returning a total of {maxhits}:")
        gddurl = output.get('success').get('next_page')
        outcome = process_hits(output.get('success').get('data'))
    if gddurl != '':
        if verbose:
            print("Fetching next page.")
        outcome = outcome + gddURLcall(gddurl)
    return outcome
