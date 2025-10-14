import json # Spotify history is exported in JSON
import os # for working with files provided by the user

if __name__ == "__main__":
    # Currently the debug toggle is hardcoded. 
    # I will likely keep it that way, or make it a flag that can be set when executing this application through a terminal.
    debug = True

    # TODO: Reimplement this differently when we move to a GUI application. As a script this works fine.
    dataDir = input("Please enter the absolute location of Spotify history files (\".\" is also accepted): ")
    
    # Collect the files containing Spotify history within the directory provided by the user.
    # Currently pulls all JSON files with the correct prefix in their filename into the following array.
    histFiles = []
    for dirpath, _, filenames in os.walk(dataDir):
        for name in filenames:
            # Since we will be checking the filename and extension more than once, let's make it a variable.
            nameAndExt = os.path.splitext(name)
            
            # If the file does not match the filename and extension, then move on.
            if nameAndExt[0].find("Streaming_History_Audio") == -1: break
            if nameAndExt[1].lower() != ".json": break

            # Otherwise, add it to the list.
            histFiles.append(os.path.join(dirpath,name))
                
    # Check what files were collected to see if the filter worked or if the right files were passed in.
    if debug: print(histFiles) 

    # Now, we begin extracting the JSON files into one big list of dictionaries.
    data = []
    for file in histFiles:
        with open(file) as json_data:
            data.extend(json.load(json_data))