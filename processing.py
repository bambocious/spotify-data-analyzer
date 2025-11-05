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
            continue

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


# Finds all unique entries and counts how often they occur. Returns a list of
# lists where the first value is the name and the second is the number of
# occurences. This is best for artists and albums. for songs, use countSongs.
def countUniqueValues(dataset: list, key, sort: bool):
    counts = []
    for song in dataset:
        name = song[key]
        for pair in counts:
            if pair[0] == name:
                pair[1] += 1
                break
        else:
            counts.append([name, 1])

    if sort:
        counts = sorted(counts, key=lambda entry: entry[1], reverse=True)

    return counts


# Same as above, but finds unique songs and also stores artist and album data
# for reference.
def countUniqueSongs(dataset: list, sort: bool):
    # We use a dict first as it is faster to work with. Convert to list later.
    # I have to thank generative AI for this idea.
    countsDict = {}
    for song in dataset:
        # Use a tuple as the dict key, and the value will be the count.
        key = (
            song["master_metadata_track_name"],
            song["master_metadata_album_artist_name"],
            song["master_metadata_album_album_name"],
        )

        if key in countsDict:
            countsDict[key] += 1
        else:
            countsDict[key] = 1

    # Now we can convert back to a list. Much faster than working wiht a list
    # directly.
    counts = [
        [
            {
                "track_name": key[0],
                "artist_name": key[1],
                "album_name": key[2],
            },
            value,
        ]
        for key, value in countsDict.items()  # List comprehension.
    ]

    if sort:
        counts = sorted(counts, key=lambda entry: entry[1], reverse=True)

    return counts


# Finds the intended type of a value (i.e. will determine that track names
# should be strings.) This ignores None values to find the true value. Other
# exceptions will be added if found.
def findValueType(dataset: list, key):
    for song in dataset:
        t = type(song[key])

        if t == None:
            continue

        return t
