"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = dict()
    with open(neo_csv_path, 'r') as file_csv:
        reader = csv.DictReader(file_csv)
        for row in reader:
            neos[row['pdes']] = NearEarthObject(row['pdes'], row['name'], row['diameter'], row['pha'])
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path) as jsonfile:
        j_data = json.load(jsonfile)
    print(f"Fields = {j_data['fields']}")
    approaches = dict()
    fields_indices = create_indices(j_data['fields'])
    for row in j_data['data']:
        close_approach = CloseApproach(row[fields_indices['des']], row[fields_indices['cd']],
                                       row[fields_indices['dist']], row[fields_indices['v_rel']])
        if approaches.get(row[fields_indices['des']], None) is None:
            approaches[row[fields_indices['des']]] = [close_approach]
        else:
            curlst = approaches[row[fields_indices['des']]]
            curlst.append(close_approach)
    return approaches


def create_indices(fields_list):
    """Create a dictionary based on a list of strings.

    :param fields_list: A list of strings
    :return: A dictionary which key will be a token and the value will be a counter
    eg. {
        "token1" : 0,
        "token2" : 1
    }
    """
    index = 0
    indices = dict()
    for field_index in fields_list:
        indices[field_index] = index
        index += 1
    return indices


if __name__ == "__main__":
    neo = load_neos("data/neos.csv")
    print(neo)

    apps = load_approaches("data/cad.json")
    print(apps)
