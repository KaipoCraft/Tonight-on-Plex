import api_request # <- our file that handles the api request
import json
####################################################################################################
## This file handles how to read a "calendar" of content in a json file
####################################################################################################

# Hey, this is just for the hackathon. I'm just going to make this a static file for now.
file = 'example_channel.json'


# a class that manages the calendar of media items
class Schedule:
    # constructor
    def __init__(self, file):
        self.file = file
        self.list = self.parse_file()
    
    #read json file and return a list of media items
    def parse_file_to_WHAT(self):
        with open(self.file) as f:
            data = json.load(f)
        return data
    
#make a new instance of the schedule class
schedule = Schedule(file)
print(schedule.list)