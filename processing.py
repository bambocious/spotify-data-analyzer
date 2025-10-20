"""
First I need to convert all the old JS functions into Python.
Only after that is done can I consider adding more.
"""

import re  # To filter against regex


# Return a list only containing dictionaries that match the key-value pair (case sensitivity and exactness can be chosen). This is sort of a master-function that all the other filters can use.
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


# ... matching provided key-regex pair.
def filterByRegex(dataset: list, key, regex):
    pattern = re.compile(regex)
    # I have to check for None types because the regex-matching will through an error if it tries to match for one.
    filteredSet = [s for s in dataset if s[key] != None and pattern.search(s[key])]

    return filteredSet


# ... matching provided year.
def filterByYear(dataset: list, year):
    filteredSet = [s for s in dataset if s["ts"].split("-")[0] == str(year)]

    return filteredSet
