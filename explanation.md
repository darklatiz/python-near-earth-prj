# Explanation

- I decided to return a dictionary for neos and approaches, in both cases the field 'des' is the key.
	- In the case of every NearEarthObject a collection of approaches is set.
    - And for every Approach a NearEarthObject is set
    - The searches based on des are faster
    - A dictionary based on the NearEarthObject's name also is created
- Based on this I has to modify the test cases because a list was expected instead of a dictionary

## URLS
- https://docs.python.org/3/library/itertools.html#itertools.islice
- https://realpython.com/