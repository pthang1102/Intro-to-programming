# This program moves photos (which have locations within their names) from Folder 'Photos' 
# into newly created folders based on locations. 
import os

# Create directories based on places
def make_place_directories(places):
    for place in places:
        os.mkdir(place)

# Extract place from fileName
def extract_place(filename):
    return filename.split('_')[1]

def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places: # This is the key change
            places.append(place) # Add new place into list Places

    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename)) # Move file into its new folder

organize_photos("Photos")
