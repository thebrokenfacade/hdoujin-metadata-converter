# hdoujin-metadata-converter

# What the heck?
These python scripts should convert info.txt files from HDoujinDownloader to info.json files. 

# Why the heck?
The use case I have is migrating from HappyPanda, which uses info.txt files for metadata, to Lanraragi, which uses info.json files for metadeta. I do not want to re-download all the metadata for my collection, so I wrote these scripts to convert existing info.txt files to info.json files without needing to re-download anything.

# How the heck?
**You need to have python3 installed for these scripts to work.**

- How to use conv.py:
  - save conv.py to the directory containing the info.txt file you wish to convert.
  - open the cmd or powershell to the directory that now contains the inf.txt file and the conv.py file
  - type python conv.py
  - press enter
  - profit
  
  For this to work your collection needs to have the following layout:
     - /some_path
       - /doujin_name01
         - /image01
         - /info.txt
         - /conv.py
  
- How to use batchconv.py
  - save batchconv.py to the directory containing your doujins
  - open the cmd or powershell to the directory that now contains your doujins and the batchconv.py file
  - type python batchconv.py
  - press enter
  - profit
  
  For this to work your collection needs to have the following layout:
    - /some_path
      - /doujin_name01
        - /image01
        - /info.txt
      - /doujin_name02
        - /image01
        - /info.txt
      - /batchconv.py
    
I hope these instructions are clear.

# Why is it so heckin' bad?
 
I am not a developer. I looked at the python docs and examples I found online to piece these scripts together. This is certainly not the only nor the best way to go about this. It feels good to have gotten it working though!
