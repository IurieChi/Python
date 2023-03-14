
# class "SaveMessages" that extends the Messenger class that does the following things:
# Add any messages it receives to a list, along with the time the message was received
# Use the "getCurrentTime" function so that the received message time is a string
# method "printMessages" that prints all collected messages when it's called.
# clearing the message list when "printMessages" is called.
# Exteption are added if message is to long
# The SaveMessages class now has limited memory and should only be able to hold a maximum of 10 messages at once.

from datetime import datetime
#get time function
def getCurrentTime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class Messenger:
    #constructor
    def __init__(self,listeners=[]):
        self.listeners = listeners
    #send function
    def send(self,message):
        for listener in self.listeners:
            listener.receive(message)
    def receive(self, message):
        #will be finished on save calss 
        pass
#exception class
class TooManyMessagesException(Exception):
    def __init__(self,message):
        super().__init__(f'Message "{message}"To many record tried to add on Messages. Please clean existing messages')

class SaveMessages(Messenger):
    #constructor
    def __init__(self, listeners=[]):
        super().__init__(listeners)
        self.messages = []
        self.max_messages = 10
    #send receive
    def receive(self,message):
        if len(self.messages) >= self.max_messages:
            raise TooManyMessagesException(message)  
        self.messages.append({'message':message, 'time':getCurrentTime()})
    #print
    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time: {m["time"]}')
        #empty list 
        self.messages =[]


#create clas instance 
listener = SaveMessages()
sender = Messenger([listener])


 #with try we send 20 messages  
for i in range(0, 20):
    try:
        sender.send(f'This is message {i}')
    except TooManyMessagesException:
        listener.printMessages()
        sender.send(f'This is message {i}')
        
listener.printMessages()
#print messages
listener.printMessages()









