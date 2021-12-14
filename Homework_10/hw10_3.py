print('Task 3', end='\n\n')
# TV controller

# Create a simple prototype of a TV controller in Python. 
# It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. 
# Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. 
# If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. 
# If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or 
# the string 'name' and returns "Yes", 
# if the channel N or 'name' exists in the list, 
# or "No" - in the other case.
 

# The default channel turned on before all commands is №1.

# Your task is to create the TVController class and 
# methods described above.

CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.current = 0

    def first_channel(self):
        self.current = 0
        return self.current_channel()

    def last_channel(self):
        self.current = len(self.channels)-1
        return self.current_channel()

    def turn_channel(self, number):
        if 0 < number <= len(self.channels):
            self.current = number - 1
        else: 
            self.current = 0
        return self.current_channel()

    def next_channel(self):
        if self.current == len(self.channels)-1:
            self.current = 0
        else:
            self.current+=1
        return self.current_channel()

    def previous_channel(self):
        if self.current == 0:
            self.current = len(self.channels)-1
        else:
            self.current-=1
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current]

    def is_exist(self, search):
        if type(search) == int:
            if 0 < search <= len(self.channels):
                return 'Yes'
            else:
                return 'No'
        try:
            if 0 <= self.channels.index(search) < len(self.channels):
                return 'Yes'   
        except ValueError:
            return 'No'

controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.is_exist(4) == "No"

assert controller.is_exist("BBC") == "Yes"