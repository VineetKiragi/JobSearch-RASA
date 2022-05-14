# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#from sre_parse import State

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#import sys
#sys.path.append('C:\Omkar\SJSU_Notes\AI&DataEngineering\ChatBot\actions')
#from fake_abc_api import demograph

from rasa_sdk.events import SlotSet
import requests


class ActionName(Action):

    def name(self) -> Text:
        return "action_Name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_ask_Email",tracker)

        return [SlotSet('Name',tracker.latest_message['text'])]


class ActionEmail(Action):

    def name(self) -> Text:
        return "action_Email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_ask_Age",tracker)
        #print(tracker.get_slot('pushpull'))

        return [SlotSet('Email',tracker.latest_message['text'])]


class ActionAge(Action):

    def name(self) -> Text:
        return "action_Age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_ask_Gender",tracker)
        #print(tracker.get_slot('pushpull'))

        return [SlotSet('Age',tracker.latest_message['text'])]

class ActionGender(Action):

    def name(self) -> Text:
        return "action_Gender"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_ask_University",tracker)
        #print(tracker.get_slot('pushpull'))

        return [SlotSet('Gender',tracker.latest_message['text'])]

class ActionUniversity(Action):

    def name(self) -> Text:
        return "action_University"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_ask_Experience",tracker)
        #print(tracker.get_slot('pushpull'))

        return [SlotSet('University',tracker.latest_message['text'])]

class ActionExperience(Action):

    def name(self) -> Text:
        return "action_Experience"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_ask_store",tracker)
        #print(tracker.get_slot('pushpull'))

        return [SlotSet('Experience',tracker.latest_message['text'])]

class ActionTitle(Action):

    def name(self) -> Text:
        return "action_Title"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_ask_Jobs",tracker)
        print(tracker.get_slot('Title'))

        return [SlotSet('Title',tracker.latest_message['text'])]

    

