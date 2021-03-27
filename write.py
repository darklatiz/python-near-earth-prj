"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w') as out_csv:
        out_csv.write(",".join(fieldnames))
        out_csv.write('\n')
        for result in results:
            out_csv.write(f"{result.time_str},{result.distance},{result.velocity},{result.neo.designation},{result.neo.nombre or ''},{result.neo.diameter},{result.neo.hazardous}")
            out_csv.write('\n')


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # Write the results to a JSON file, following the specification in the instructions.
    with open(filename, 'w') as json_out_file:
        if results is None or len(results) <= 0:
            json.dump([], json_out_file)
        else:
            data_objs = []
            for close_approach in results:
                data = close_approach.serialize()
                data['neo'] = close_approach.neo.serialize()
                data_objs.append(data)
                print(data)
            json.dump(data_objs, json_out_file)
