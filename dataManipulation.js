
function filterByKey(dataset, key, value, doLog) { // filter the data for a specific key-value pair
    if (Object.hasOwn(dataset[0], key)) {
        if (doLog) {
            console.log(`filterByKey - filtering for plays that match the key-value pair {"${key}":"${value}"}`)
        }

        return dataset.filter(play => play[key] == value);
    } else {
        console.log(`filterByKey - Error: ${key} is not a valid key.`)
        
        return 0;
    }
}

function filterBySong(dataset, songName, artist, doLog) { // filter the data for a specific song
    if (doLog) {
        console.log(`filterBySong - filtering by song name (${songName}) and artist name (${artist})...`)
    };

    return dataset.filter(song => (song["master_metadata_track_name"] == songName && song["master_metadata_album_artist_name"] == artist));
};

function filterByRegex(dataset, key, regex, doLog) { // filter data using a regex
    let result = dataset.filter(song => 
        (regex.test(song[key]))
    )

    if (doLog) {
        console.log(`filterByRegex - filtered for ${key} matching ${toString(regex)}; ${result.length} matches.`)
    }

    return result;
}

function filterByYear(dataset, year, doLog) { // filter the data for a specific year
    if (doLog) {
        console.log(`filterByYear - filtering for songs played in ${year}...`)
    }

    return dataset.filter(song => song.ts.split("-")[0] == year)
};

function sortByDate(dataset, direction, doLog) { // sort the data by date given a direction
    let result;
    
    if (direction == undefined) {
        direction = "on";
    }

    if (direction.toLowerCase() == "on") {
        if (doLog) {
            console.log("sortByDate - Sorting by oldest to newest...")
        };

        result = dataset.sort(
            function(a,b) {return new Date(a.ts) - new Date(b.ts)}); 
        
    } else if (direction.toLowerCase() == "no") {
        if (doLog) {
            console.log("sortByDate - Sorting by newest to oldest...")
        };

        result = dataset.sort(
            function(a,b) {return new Date(b.ts) - new Date(a.ts)}); 
    }

    if (doLog) {
        console.log("sortByDate - Sorted.")
    };

    return result;
};

function sortByName(dataset, doLog) { // sort the data by song name in alphabetical order
    let result = dataset.sort((a, b) => {
        if (b.master_metadata_track_name > a.master_metadata_track_name) {
            return -1;
        } else if (b.master_metadata_track_name == a.master_metadata_track_name) {
            return 0;
        } else if (b.master_metadata_track_name < a.master_metadata_track_name) {
            return 1;
        }
    })

    if (doLog) {
        console.log("sortByName - Sorted.")
    };

    return result;
}

function artistRatio(dataset, artist, precision, doLog) { // find the percentage of your songs that are from a certain artist
    if (doLog) {
        console.log(`artistRatio - finding the ratio for songs made by ${artist}...`);
    }

    precision = 10**precision || 100; // convert to a power of 10 so that it can be used in Math.round
    let artistPlays = dataset.filter(play => play["master_metadata_album_artist_name"] == artist)

    let result = `${Math.round((artistPlays.length / dataset.length) * 100 * (precision)) / precision}%` // calculate and convert to percentage
    if (doLog) {
        console.log(`artistRatio - ${artist} comprises ${result} of your total plays.`)
    }

    return result 
}

function timespan(dataset, doLog) { // given a sorted list of plays from one artist, return the first timestamp as a date, the last timestamp as a date and the total time between the two
    let ts1 = new Date(dataset[0].ts);
    let ts2 = new Date(dataset[dataset.length-1].ts);
    
    let ms = Math.abs(ts2 - ts1);
    let days = Math.round(ms / (1000 * 60 * 60 * 24) * 100) / 100;

    if (doLog) {
        console.log(`timespan - First day: ${ts1[Symbol.toPrimitive]("string")}`); 
        console.log(`timespan - Last day: ${ts2[Symbol.toPrimitive]("string")}`);
        console.log(`timespan - ${days} days.`);

        // idk wtf Symbol.toPrimitive is; i got it from mdn web docs
        // console.log(`artistTimespan - ${ms} milliseconds.`); nobody wants to know this probably
    }

    return {
        "ts1": ts1,
        "ts2": ts2,
        "ms": ms,
        "days": days
    };
}

function totalPlaytime(dataset, key, value, doLog) { // find the total playtime for an artist, a song, or all of your music
    let filteredData;
    
    if (key.toLowerCase() != "none") {
        filteredData = filterByKey(dataset, key, value, false);
        if (filteredData == 0) {
            return "totalPlaytime - Invalid key.";
        }
    } else {
        filteredData = dataset;
    }

    let playtimeMs = filteredData.reduce((sum, play) => sum += play["ms_played"], 0);
    let playtimeDays = Math.round(playtimeMs / (1000 * 60 * 60 * 24) * 100) / 100;
    
    if (doLog) {
        console.log(`totalPlaytime - You have spent ${playtimeDays} days of your life listening to songs matching {"${key}":"${value}"}.`)
    }

    return {
        "ms": playtimeMs,
        "days": playtimeDays
    };
}   

function msToTime(ms, doLog) {
    const hours = Math.floor(ms / 1000 / 60 / 60);
    const minutes = Math.floor((ms-(hours*1000*60*60)) / 1000 / 60);
    const seconds = Math.floor((ms-(hours*1000*60*60)-(minutes*1000*60)) / 1000 / 60);

    if (doLog) {
        console.log(`msToTime - converted ${ms} milliseconds to ${hours} hours, ${minutes} minutes and ${seconds} seconds.`)
    }

    return {
        "time": `${hours} hours and ${minutes} minutes`,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    };
}

function footer(dataset, doLog) { // a little footer for every run; returns nothing
    const plays = dataset.length; // total plays
    const latestPlay = sortByDate(dataset, 'no')[0].ts; // last play in the data
    const totalDays = totalPlaytime(dataset, "none")["days"]; // total days spent listening to music
    const percentTime = Math.round(totalDays / timespan(dataset, false).days * 10000) / 100; // total days spent listening to music over the total days since you started listening to music
    const avgHours = msToTime(((percentTime/100)*(1000*24*60*60)))["time"];

    if (doLog) {
        console.log(`\nYou have ${plays} plays as of ${latestPlay}, the end of the data range.`);
        console.log(`You have spent ${totalDays} days listening to music on Spotify.`);
        console.log(`On average, that's ${avgHours} a day.`);
        console.log(`It's also ${percentTime}% of the time between your oldest and most recent play.`)
    }
};

console.log("\n--------------------------------------------------"); // create a blank space between the console.log outputs and the command 

// import data

console.log("\ndata reading started...");

let data = [
    ...require("./data_8_2023/Streaming_History_Audio_2021_0.json"),
    ...require("./data_8_2023/Streaming_History_Audio_2021-2022_1.json"),
    ...require("./data_8_2023/Streaming_History_Audio_2022-2023_2.json")
]

console.log("\ndata reading complete...\n\n");

