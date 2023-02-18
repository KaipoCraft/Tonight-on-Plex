import api_request # <- our file that handles the api request
import json
####################################################################################################
## This file handles how to read a "channel" json file
####################################################################################################

# Hey, this is just for the hackathon. I'm just going to make this a static file for now.
file = 'example_channel.json'



# define the function that reads in a json file and returns a list media items with their times
def read_json(filename):
    # open the file
    with open(filename, 'r') as f:
        # read the file
        data = json.load(f)
        # return the data
        return data

# now make the dictionary containing the channel content.
channel_content = read_json(file)

print (channel_content)

