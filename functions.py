import requests
import json
import csv


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


def import_dois_from_csv(filename):
    """Imports the list of DOIs from a CSV file.

    Args:
        filename: Filename of the CSV file that contains the list of DOIs

    Returns:
        dois: List of DOIs in the CSV file
    """
    with open(filename, mode ='r') as file:
        csv_file = csv.reader(file)
        dois = [row[0] for row in csv_file]
    return dois

