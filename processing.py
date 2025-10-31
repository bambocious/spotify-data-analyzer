"""
All functions used to process data in some way.
"""

import re  # To filter against regex


# Return a list only containing dictionaries that match the key-value pair (case
# sensitivity and exactness can be chosen). This is sort of a master-function
# that all the other filters can use.
def filterByKey(dataset: list, key, value, isExact, isCaseSensitive):
    filteredSet = []

    for s in dataset:
        if s[key] == None:
            continue

        if type(s[key]) != str:
            if s[key] == value:
                filteredSet.append(s)

        if isCaseSensitive and isExact:
            if s[key] == value:
                filteredSet.append(s)
        elif isCaseSensitive:
            if s[key].find(value) >= 0:
                filteredSet.append(s)
        elif isExact:
            if s[key].lower() == value.lower():
                filteredSet.append(s)
        else:
            if s[key].lower().find(value.lower()) >= 0:
                filteredSet.append(s)

    return filteredSet


# ... not matching key-value pair. (Inversion of the above)
def filterOutByKey(dataset: list, key, value, isExact, isCaseSensitive):
    filteredSet = []

    for s in dataset:
        if s[key] == None:
            filteredSet.append(s)
            continue

        if type(s[key]) != str:
            if s[key] != value:
                filteredSet.append(s)
            continue

        if isCaseSensitive and isExact:
            if s[key] != value:
                filteredSet.append(s)
        elif isCaseSensitive:
            if s[key].find(value) < 0:
                filteredSet.append(s)
        elif isExact:
            if s[key].lower() != value.lower():
                filteredSet.append(s)
        else:
            if s[key].lower().find(value.lower()) < 0:
                filteredSet.append(s)

    return filteredSet


# ... matching provided key-regex pair.
def filterByRegex(dataset: list, key, regex):
    pattern = re.compile(regex)
    # I have to check for None types because the regex-matching will through an
    # error if it tries to match for one.
    filteredSet = [s for s in dataset if s[key] != None and pattern.search(s[key])]

    return filteredSet


# ... matching provided year.
def filterByYear(dataset: list, year):
    filteredSet = [s for s in dataset if s["ts"].split("-")[0] == str(year)]

    return filteredSet


# ... sorted by value of a key. Numerically or alphabetically is automatically
# handled, direction is provided or default to ascending.
def sortBykey(dataset: list, key, isDescending):
    # Check type of values for a key.
    valueType = findValueType(dataset, key)

    # Then, use the value to decide if we need to lowercase or not.
    # Case-sensitivity of sorting produces undesirable results.
    if valueType == str:
        sortedSet = sorted(
            dataset, key=lambda song: song[key].lower(), reverse=isDescending
        )
    else:
        sortedSet = sorted(dataset, key=lambda song: song[key], reverse=isDescending)

    return sortedSet


# Finds the intended type of a value (i.e. will determine that track names
# should be strings.) This ignores None values to find the true value. Other
# exceptions will be added if found.
def findValueType(dataset: list, key):
    for song in dataset:
        t = type(song[key])

        if t == None:
            continue

        return t
