

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#from sre_parse import State
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#import sys
#sys.path.append('C:\Omkar\SJSU_Notes\AI&DataEngineering\ChatBot\actions')
#from fake_abc_api import demograph
from rasa_sdk.events import SlotSet
import requests
import json 

import sqlite3

def datastore(Name, Email, Age, Gender, University, Experience):
    conn=sqlite3.connect('JobSearch2.db')
    mycursor = conn.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS Job (Name TEXT, Email TEXT, Age TEXT, Gender TEXT, University TEXT, Experience TEXT);""")
    mycursor.execute("INSERT INTO Job VALUES (?,?,?,?,?,?)",(Name, Email, Age, Gender, University, Experience))
    conn.commit()
    print(mycursor.rowcount,"record inserted vineet")



# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_store"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         print('hello')    
#         x=tracker.get_slot('pushpull')
#         print(x)
#         y=tracker.get_slot('description')
#         print(y)
#         DataUpdate(tracker.get_slot('muscles'), tracker.get_slot('height'))
#         dispatcher.utter_message("Database Updated")
#         return []


#y=datastore('Vineet','vineet.kiragi.n8@gmail.com')
#print(y)

class Actiondatabase(Action):

    def name(self) -> Text:
        return "action_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        x=tracker.get_slot('Name')
        y=tracker.get_slot('Email')
        z=tracker.get_slot('Age')
        a=tracker.get_slot('Gender')
        b=tracker.get_slot('University')
        c=tracker.get_slot('Experience')
        #d=tracker.get_slot('Email')
        datastore(x,y,z,a,b,c)
        print(x,y,z,a,b,c)
        dispatcher.utter_message("I will pass on the contact info you have provided to the companies above which match your profile.")

        return []

#print("hello")