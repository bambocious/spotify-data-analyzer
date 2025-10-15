"""
First I need to convert all the old JS functions into Python.
Only after that is done can I consider adding more.
"""
import re # To filter against regex


# Return a list only containing dictionaries that match the key-value pair. This is sort of a master-function that all the other filters can use.
def filterByKey(dataset: list, key, value):
    filteredSet = [
        s for s in dataset if s[key] == value
    ]

    return filteredSet

# These next few functions will be mostly implementations of filterByKey. Technically, they are all unnecessary, however I believe it will simplify things in the future.

# ... matching the provided song title. 
def filterByTitle(dataset: list, title):
    filteredSet = [
        # Case insensitive matching + can just contain the song title.
        s for s in dataset if s["master_metadata_track_name"].lower().find(title.lower())
    ]

    return filteredSet

# ... matching provided key-regex pair.
def filterByRegex(dataset: list, key, regex):
    pattern = re.compile(regex)
    filteredSet = [
        s for s in dataset if s[key] != None and pattern.search(s[key])
    ]
    
    return filteredSet

