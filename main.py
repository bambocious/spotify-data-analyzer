"""
Main program to collect the JSON files and create the large list,
and then run various processes on it.
"""

import json  # Spotify history is exported in JSON
import os  # for working with files provided by the user

import processing  # Local file with the important functions

if __name__ == "__main__":
    # Currently the debug toggle is hardcoded. I will likely keep it that way,
    # or make it a flag that can be set when executing this application through
    # a terminal.
    debug = True

    dataDir = input(
        'Please enter the absolute location of Spotify history files ("." is also accepted): '
    )

    # Collect the files containing Spotify history within the directory provided
    # by the user. Currently pulls all JSON files with the correct prefix in
    # their filename into the following array.
    histFiles = []
    for dirpath, _, filenames in os.walk(dataDir):
        for name in filenames:
            # Since we will be checking the filename and extension more than
            # once, let's make it a variable.
            nameAndExt = os.path.splitext(name)

            # If the file does not match the filename and extension, then move on.
            if nameAndExt[0].find("Streaming_History_Audio") == -1:
                break
            if nameAndExt[1].lower() != ".json":
                break

            # Otherwise, add it to the list.
            histFiles.append(os.path.join(dirpath, name))

    # Check what files were collected to see if the filter worked or if the
    # right files were passed in.
    if debug:
        print(histFiles)

    # Now, we extract the JSON files into one big list of dictionaries.
    data = []
    for file in histFiles:
        with open(file) as json_data:
            data.extend(json.load(json_data))

    # Now that the list is complete, we can process it in various ways.
    # Eventually the GUI application will show either a bunch of things or you
    # can choose what it will show. For now, I could just ask the user for how
    # they want their data processed. Either way, I need to write the data
    # processing functions in Python before I can continue further, which will
    # exist in a separate file.

    # Testing below.
    listA = processing.filterByKey(
        data, "master_metadata_album_artist_name", "Palaye Royale", False, False
    )
    listB = processing.sortBykey(listA, "master_metadata_track_name", False)

    for song in listB:
        print(song["master_metadata_track_name"])
"""
For reference, the different options for keys (in songs) are:
    ts
    username
    platform
    ms_played
    conn_country
    ip_addr (ip_addr_decrypted)
    master_metadata_track_name
    master_metadata_album_artist_name
    master_metadta_album_album_name
    spotify_track_uri
    episode_name
    episode_show_name
    spotify_episode_uri
    audiobook_title
    audiobook_uri
    audiobook_chapter_uri
    audiobook_chapter_title
    reason_start
    reason_end
    shuffle
    skipped
    offline
    offline_timestamp
    incognito_mode
"""
