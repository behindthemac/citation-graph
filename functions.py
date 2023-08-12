import requests
import json


def get_references(doi):
    """Returns the list of DOIs of a given paper's references.

    Args:
        doi: DOI of a paper

    Returns:
        dois: List of DOIs of the given paper's references
    """
    base_url = 'https://api.crossref.org/works/' 
    query_url = base_url + doi
    response = requests.get(query_url)

    data = response.json()
    if ('message' in data) and ('reference' in data['message']):
        references = data['message']['reference']
        
        # Extracting DOIs from the references
        dois = [reference['DOI'] for reference in references if 'DOI' in reference]
        return dois
    else:
        print(f"No references found for DOI {doi}")
        return []
