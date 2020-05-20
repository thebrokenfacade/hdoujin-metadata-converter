# This script should convert an info.txt file in the same dir to an info.json file in the same dir
# This script requires python3 to be installed in order to run properly.
# To run the script place conv.py in the directory containing the info.txt you want to convert
# Open a cmd to the directory (hold shift and right click > open powershell here)
# Type python conv.py
# Watch for the new info.json to be created.

import os

try:
    # Read in info.txt to a string delineated by commas, using utf8 for non english characters
    with open("info.txt", "rt", encoding='utf8') as in_file:
        infotxt = in_file.read()
except FileNotFoundError:
    print("\nAn info.txt file was not found in the directory.")
    print("    There is nothing to do!")
    input("\nPress enter to exit...")
    exit()

# Convert the infotxt string to a list with each item determined by the commas
infolist = infotxt.split("\n")

# Create string variables for each category in the info.txt v2 format
# For some reason some categories use "" while others use [] to denote an empty category
# the if statement is only needed for empty categories that use []
# the rest of the empty categories use "" and thus do not need modified
tit = "\"%s\"" % (infolist[0].replace('TITLE: ', ''))
ori = "\"%s\"" % (infolist[1].replace('ORIGINAL TITLE: ', ''))
aut = "\"%s\"" % (infolist[2].replace('AUTHOR: ', ''))
if aut == "\"\"":
    aut = "[]"
art = "\"%s\"" % (infolist[3].replace('ARTIST: ', ''))
if art == "\"\"":
    art = "[]"
cir = "\"%s\"" % (infolist[4].replace('CIRCLE: ', ''))
if cir == "\"\"":
    cir = "[]"
sca = "\"%s\"" % (infolist[5].replace('SCANLATOR: ', ''))
if sca == "\"\"":
    sca = "[]"
tra = "\"%s\"" % (infolist[6].replace('TRANSLATOR: ', ''))
if tra == "\"\"":
    tra = "[]"
pub = "\"%s\"" % (infolist[7].replace('PUBLISHER: ', ''))
des = "\"%s\"" % (infolist[8].replace('DESCRIPTION: ', ''))
sta = "\"%s\"" % (infolist[9].replace('STATUS: ', ''))
cha = "\"%s\"" % (infolist[10].replace('CHAPTERS: ', ''))
# This seems to be the only category that does not use "" or [] around the item
pag = "%s" % (infolist[11].replace('PAGES: ', ''))
tag = "\"%s\"" % (infolist[12].replace('TAGS: ', ''))
if tag == "\'\'":
    tag = "[]"
typ = "\"%s\"" % (infolist[13].replace('TYPE: ', ''))
lan = "\"%s\"" % (infolist[14].replace('LANGUAGE: ', ''))
if lan == "\'\'":
    lan = "[]"
rel = "\"%s\"" % (infolist[15].replace('RELEASED: ', ''))
rea = "\"%s\"" % (infolist[16].replace('READING DIRECTION: ', ''))
chara = "\"%s\"" % (infolist[17].replace('CHARACTERS: ', ''))
if chara == "\"\"":
    chara = "[]"
ser = "\"%s\"" % (infolist[18].replace('SERIES: ', ''))
par = "\"%s\"" % (infolist[19].replace('PARODY: ', ''))
if par == "\"\"":
    par = "[]"
url = "\"%s\"" % (infolist[20].replace('URL: ', ''))

# Open a new json file to write into and create the json line by line because I can not figure out a better way to do it
with open("info.json", "w", encoding = 'utf8') as out_file:
    out_file.write("{\n")
    out_file.write("  \"manga_info\": {\n")
    out_file.write("    \"title\": %s,\n" % tit)
    out_file.write("    \"original_title\": %s,\n" % ori)

    # If the category is empty just use [] on a single line
    # If the category has one or more items it needs to be in the format:
    #    "category": [
    #      "item1",
    #      "item2",
    #      "item3"
    #    ],
    if aut == "[]":
        out_file.write("    \"author\": %s,\n" % aut)
    else:
        out_file.write("    \"author\": [\n      %s\n    ],\n" % aut.replace(", ", "\",\n      \""))

    if art == "[]":
        out_file.write("    \"artist\": %s,\n" % art)
    else:
        out_file.write("    \"artist\": [\n      %s\n    ],\n" % art.replace(", ", "\",\n      \""))

    if cir == "[]":
        out_file.write("    \"circle\": %s,\n" % cir)
    else:
        out_file.write("    \"circle\": [\n      %s\n    ],\n" % cir.replace(", ", "\",\n      \""))

    if sca == "[]":
        out_file.write("    \"scanlator\": %s,\n" % sca)
    else:
        out_file.write("    \"scanlator\": [\n      %s\n    ],\n" % sca.replace(", ", "\",\n      \""))

    if tra == "[]":
        out_file.write("    \"translator\": %s,\n" % tra)
    else:
        out_file.write("    \"translator\": [\n      %s\n    ],\n" % tra.replace(", ", "\",\n      \""))

    out_file.write("    \"publisher\": %s,\n" % pub)
    out_file.write("    \"description\": %s,\n" % des)
    out_file.write("    \"status\": %s,\n" % sta)
    out_file.write("    \"chapters\": %s,\n" % cha)
    # Note no "" or [] for pages
    out_file.write("    \"pages\": %s,\n" % pag)

    if tag == "[]":
        out_file.write("    \"tags\": %s,\n" % tag)
    else:
        out_file.write("    \"tags\": [\n      %s\n    ],\n" % tag.replace(", ", "\",\n      \""))

    out_file.write("    \"type\": %s,\n" % typ)

    if lan == "[]":
        out_file.write("    \"language\": %s,\n" % lan)
    else:
        out_file.write("    \"language\": [\n      %s\n    ],\n" % lan.replace(", ", "\",\n      \""))

    out_file.write("    \"released\": %s,\n" % rel)
    out_file.write("    \"reading_direction\": %s,\n" % rea)

    if chara == "[]":
        out_file.write("    \"characters\": %s,\n" % chara)
    else:
        out_file.write("    \"characters\": [\n      %s\n    ],\n" % chara.replace(", ", "\",\n      \""))

    out_file.write("    \"series\": %s,\n" % ser)

    if par == "[]":
        out_file.write("    \"parody\": %s,\n" % par)
    else:
        out_file.write("    \"parody\": [\n      %s\n    ],\n" % par.replace(", ", "\",\n      \""))

    out_file.write("    \"url\": %s\n" % url)
    out_file.write("  }\n")
    out_file.write("}\n")

root = os.getcwd()
gal_path = os.path.join(root)

print("\nA info.txt file was found in \"%s\"." % gal_path)
print("    The info.txt was successfully converted.")
print("    The info.json was saved to \"%s\"." % gal_path)
print("    The info.txt was not deleted.")
input("\nPress enter to exit...")
exit()




