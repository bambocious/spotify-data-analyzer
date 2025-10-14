import json # Spotify history is exported in JSON
import os # for working with files provided by the user

debug = True

if __name__ == "__main__":
    dataDir = input("Absolute location of Spotify history files: ")
    
    # Collect the files containing Spotify history within the directory provided by the user.
    # Currently just pulls all JSON files and adds their absolute paths to the following array.
    histFiles = []
    for dirpath, _, filenames in os.walk(dataDir):
        for name in filenames:
            if os.path.splitext(name)[1].lower() == ".json": # Matching all JSON files, for now.
                histFiles.append(os.path.join(dirpath,name)) 
    
    if debug: print(histFiles) 

    data = {}
    for file in histFiles:
        if debug: print("file: " + file)
        with open(file) as json_data:
            # .update should "append" additional json files to make one big dictionary
            data.update(json.load(json_data))

    print(data)
