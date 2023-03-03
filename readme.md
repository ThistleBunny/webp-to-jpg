# WEBP to JPG Batch Converter
This is a simple script that bulk-converts WEBP files in a specified set of directories to JPG files. 

This script was created because I save a ton of pictures from Reddit (mostly of bunnies and cats) and a lot of them end up being WEBP files, which not all programs support.

## Setup
This script requires Python to run.
1) Run `pip -r requirements.txt`
2) Rename `config.json.example` to `config.json`
3) Edit `config.json`

    A) Set `delete_orignal` to `true` if you want it to delete the original WEBP file. **WARNING: SETTING THIS VALUE TO TRUE MAY CAUSE DATA LOSS IF THE CONVERSION FAILS.**

    B) Enter a list of directories you want the script to scan for under `directory_list`. Do not including a trailing `/`. On Windows, replace the backslash (`\`) with a forward slash (`/`)

4) Run the script