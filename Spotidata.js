/** 
 * Spotidata Remastered. I wrote a little javascript program when I first learned the language. It's purpose was to
 * take your Spotify full listening history (from text files, no API available for full history) and manipulate it
 * in ways that weren't available to me online. It also allows me to do Spotify Wrapped-type analysis at any time 
 * of year.
 * Now I've forgotten most of the slightly more advanced methods I used do filter data in that program, I will be 
 * re-writing it on this computer. So far I plan to stick to JS but I could try Java simply because it is what I'm
 * currently learning and hopefully it has the same functionalities I'm looking for.
*/

/*
 * TODO: 
 * functionalities to be implemented are as follows:
 * - read json
 * - total listens by given parameter (artist, album, title, publication year, duration, etc.)
 *    - hopefully under one method where you can tell it what parameter to search by, shouldn't need
 *      multiple methods
 * - 
 */


console.log("\ndata reading starting...\n\n");

let data = [ // waiting for next spotify data request to arrive, currently reading most recent one 
             // which is like a year old
    ...require(".original/Spotidata/data_8_2023/Streaming_History_Audio_2021_0.json"),
    ...require(".original/Spotidata/data_8_2023/Streaming_History_Audio_2021-2022_1.json"),
    ...require(".original/Spotidata/data_8_2023/Streaming_History_Audio_2022-2023_2.json")
]

console.log("\ndata reading complete...\n\n");


console.log();
