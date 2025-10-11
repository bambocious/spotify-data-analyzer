import json
import os

if __name__ == "__main__":
    dataDir = input("Absolute location of Spotify history files: ")
    
    histFiles = []

    for dirpath, _, filenames in os.walk(dataDir):
        for name in filenames:
            if os.path.splitext(name)[1].lower() == ".json":
                histFiles.append(os.path.join(dirpath,name))
    

