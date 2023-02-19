import json
import time
##########################################################################
## This file handles how to read a "calendar" of content in a json file ##
##########################################################################

# Hey, this is just for the hackathon. I'm just going to make this a static file for now.
file = 'example_calendar.json'


# a class that manages the calendar of media items
class Schedule:
    # constructor
    def __init__(self, file):
        self.file = file
        self.library = self.parse_file_to_library()
        self.sorted_times_list = self.sort_by_time(self.library)
    
    #read json file and return a list of media items
    def parse_file_to_library(self):
        with open(self.file) as f:
            data = json.load(f)
        return data
    
    # method that sorts the library of media items by time
    def sort_by_time(self, library):
        return sorted(library)

    # method that returns the current media ID that should be playing
    def get_current_media(self):
        #Instantiate the media server and grab the ID #NKS
        pass

    # method that returns the time in milliseconds since a given time (time is ms since 1970)
    def get_time_since(self, time):
        current_time = time.time_ns() // 1_000_000
        calculated_timestamp_ms = current_time - time
        print(calculated_timestamp_ms)
        return calculated_timestamp_ms

# #make a new instance of the schedule class for degugging
# schedule = Schedule(file)
# print(schedule.sorted_times_list)
# print(schedule.get_time_since(1676682000000))