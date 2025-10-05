'''
Author: 
Date: 
Class: AP CSP

Assignment: Message Analysis

Complete the problems below dealing reading from files and slicing Strings!

***IMPORTANT: each intercepted message is in the following format:
Sender-Receiver-MessageID-Message

Where...
   Sender is eight characters long
   Receiver is eight characters long
   MessageID is eight characters long
   Message is not a specified length

'''


'''
countByKeyword(filename, keyword)

A file name is passed into this method.
Open it and read it line by line.
For each line, see if the "message" portion contains the keyword passed in.
Keep track of how many messages contain the keyword passed in.
Return that count!
'''
def countByKeyword(filename, keyword):
    return -1   # dummy return statement; remove when you are writing this method

  
'''
countBySender(filename, sender)

A file name is passed into this method.
Open it and read it line by line.
For each line, see if the sender matches the sender passed into this method.
Keep track of how many messages are sent by the sender passed into this method.
Return that count!
'''
def countBySender(filename, sender):
    return -1   # dummy return statement; remove when you are writing this method


'''
countByReceiver(filename, receiver)

A file name is passed into this method.
Open it and read it line by line.
For each line, see if the receiver matches the receiver passed into this method.
Keep track of how many messages are received by the receiver passed into this method.
Return that count!
'''
def countByReceiver(filename, receiver):
    return -1   # dummy return statement; remove when you are writing this method

  
'''
getMessageByID(filename, id)

A file name is passed into this method.
Open it and read it line by line.
Go line by line until you find the message whose messageID matches the id passed into this method.
Return the "message" portion of the intercepted message!
'''
def getMessageByID(filename, id):
    return "dummy"   # dummy return statement; remove when you are writing this method

  
'''
getIDByMessage(filename, message)

A file name is passed into this method.
Open it and read it line by line.
Go line by line until you find the message whose message portion matches the message passed into this method.
Return the messageID of the intercepted message!
'''
def getIDByMessage(filename, message):
    return -1   # dummy return statement; remove when you are writing this method
