from .gddURLcall import gddURLcall

def gdd_snippets(terms: str) -> list:
    """_Get snippets from xDD using a term or terms_

    Args:
        terms (str): _A single term or set of terms to be passed into the xDD API_

    Returns:
        _list_: _A list of dict elements returned from xDD._
    """
    gddurl = (f"https://geodeepdive.org/api/v1/snippets?term={terms}&clean&full_results")
    responses = gddURLcall(gddurl)
    with_repo = [dict(item, **{'repository': terms}) for item in responses]
    return with_repo
