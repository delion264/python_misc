import os
import sys
from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS

# images to be analysed will be taken from a user-specified directory
path = input("Enter image directory: ")
os.chdir(path)
files = os.listdir()
losers = 5
print(f"Hello {losers} losers")

if len(files) == 0:
    print("Empty directory")
    exit()

for file in files:
    try:
        # read image data
        img = Image.open(file)
        print()
        print()
        print(f"========================= {file} =========================")
        print()
        #gps_info = {}

        # extract EXIF data - getexif() returns an instance of <class PIL.Image.Exif> or None if image has no EXIF data
        img_exif = img._getexif()
        
        if img_exif == None:
            print(f"{file} contains no exif data.")

        else:
            # iterate over all EXIF data fields and convert tag_id to human-readable form
            for tag, data in img_exif.items():
                tag_name = TAGS[tag]
                
                # print GPS data
                if tag_name == "GPSInfo":
                    for key, val in data.items():
                        print(f"{GPSTAGS[key]}: {val}")
                    
                # print data not related to GPSInfo
                else:
                    print(f"{tag_name}: {data}")
                    # try changing "value" to "data"

    except IOError:
        print("File format not supported!")
