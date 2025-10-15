"""
First I need to convert all the old JS functions into Python.
Only after that is done can I consider adding more.
"""

import re  # To filter against regex


# Return a list only containing dictionaries that match the key-value pair (case sensitivity and exactness can be chosen). This is sort of a master-function that all the other filters can use.
# TODO: Something needs to process out NoneTypes, as they are affecting more than just regex. They either need to be ignored or need to be turned into empty strings.
def filterByKey(dataset: list, key, value, isExact, isCaseSensitive):
    if isCaseSensitive:
        if isExact:
            # Case-sensitive and exact:
            filteredSet = [s for s in dataset if s[key] == value]
            return filteredSet
        # Otherwise (case-sensitive but not exact):
        filteredSet = [s for s in dataset if s[key].find(value) >= 0]
        return filteredSet
    if isExact:
        # Case-insensitive and exact:
        filteredSet = [s for s in dataset if s[key].lower() == value.lower()]
    # Case-insensitive and not exact:
    filteredSet = [s for s in dataset if s[key].lower().find(value.lower()) >= 0]


# ... matching provided key-regex pair.
def filterByRegex(dataset: list, key, regex):
    pattern = re.compile(regex)
    # I have to check for None types because the regex-matching will through an error if it tries to match for one.
    filteredSet = [s for s in dataset if s[key] != None and pattern.search(s[key])]

    return filteredSet
