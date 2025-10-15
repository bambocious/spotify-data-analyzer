# First I need to convert all the old JS functions into Python.
# Only after that is done can I consider adding more.

# Return a list only containing dictionaries that match the key-value pair. This is sort of a master-function that all the other filters can use.
def filterByKey(dataset: list, key, value):
    filteredSet = [s for s in dataset if s[key] == value]

    return filteredSet

# Return a list only containing dictionaries matching the provided song title. 
def filterByTitle(dataset: list, title):
    break
