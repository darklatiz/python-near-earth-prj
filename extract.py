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

NEOS_HEADERS = {'id': 0, 'spkid': 1, 'full_name': 2, 'pdes': 3, 'name': 4, 'prefix': 5, 'neo': 6, 'pha': 7, 'H': 8,
                'G': 9, 'M1': 10, 'M2': 11, 'K1': 12, 'K2': 13, 'PC': 14, 'diameter': 15, 'extent': 16, 'albedo': 17,
                'rot_per': 18, 'GM': 19, 'BV': 20, 'UB': 21, 'IR': 22, 'spec_B': 23, 'spec_T': 24, 'H_sigma': 25,
                'diameter_sigma': 26, 'orbit_id': 27, 'epoch': 28, 'epoch_mjd': 29, 'epoch_cal': 30, 'equinox': 31,
                'e': 32, 'a': 33, 'q': 34, 'i': 35, 'om': 36, 'w': 37, 'ma': 38, 'ad': 39, 'n': 40, 'tp': 41,
                'tp_cal': 42, 'per': 43, 'per_y': 44, 'moid': 45, 'moid_ld': 46, 'moid_jup': 47, 't_jup': 48,
                'sigma_e': 49, 'sigma_a': 50, 'sigma_q': 51, 'sigma_i': 52, 'sigma_om': 53, 'sigma_w': 54,
                'sigma_ma': 55, 'sigma_ad': 56, 'sigma_n': 57, 'sigma_tp': 58, 'sigma_per': 59, 'class': 60,
                'producer': 61, 'data_arc': 62, 'first_obs': 63, 'last_obs': 64, 'n_obs_used': 65, 'n_del_obs_used': 66,
                'n_dop_obs_used': 67, 'condition_code': 68, 'rms': 69, 'two_body': 70, 'A1': 71, 'A2': 72, 'A3': 73,
                'DT': 74}


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = dict()
    with open(neo_csv_path, 'r') as file_csv:
        headers = file_csv.readline()
        print(f"These are the headers = {headers}")
        for line in file_csv:
            line = line.replace('\n', '')
            line = line.split(',')
            # print(f"size={len(line)}, values={line}")
            neos[line[NEOS_HEADERS['pdes']]] = NearEarthObject(line[NEOS_HEADERS['pdes']], line[NEOS_HEADERS['name']],
                                                               line[NEOS_HEADERS['diameter']],
                                                               line[NEOS_HEADERS['pha']])
    return neos


def create_map_headers(headers_description):
    counter = 0
    h_map = dict()
    for key in headers_description.split(","):
        h_map[key.replace('\n', '')] = counter
        counter += 1
    return h_map


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
        close_approach = CloseApproach(row[fields_indices['des']], row[fields_indices['cd']], row[fields_indices['dist']], row[fields_indices['v_rel']])
        if approaches.get(row[fields_indices['des']], None) is None:
            approaches[row[fields_indices['des']]] = [close_approach]
        else:
            curlst = approaches[row[fields_indices['des']]]
            curlst.append(close_approach)
    return approaches


def create_indices(fields_list):
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
