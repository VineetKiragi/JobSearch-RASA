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

import requests
import json 



def JobsAPI(title):
    url = "https://job-search4.p.rapidapi.com/simplyhired/search"
    querystring = {"query":"Software Engineer","page":"1"}
    headers = {
	"X-RapidAPI-Host": "job-search4.p.rapidapi.com",
	"X-RapidAPI-Key": "e34b2f1793mshc6bfedd1062b653p171d64jsn41e4c56dc357"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    data = response.text
    res = json.loads(data) 
    return res

    

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_job_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        h=tracker.get_slot('Title')
        #p=tracker.latest_message['text']
        temp=JobsAPI(h)
        for job in temp['jobs']:
            dispatcher.utter_message("Job Title:"+job['title']+'\nSource:'+job['source']+'\nCompany name:'+job['company_name']+'\nLocation:'+job['location']+'\n')
            dispatcher.utter_message("---------------------------------------------------------------------------------------------------------------------------")
            #print("Job Title:"+job['title']+'\nSource:'+job['source']+'\nCompany name:'+job['company_name']+'\nLocation:'+job['location']+'\n')
    
        dispatcher.utter_template("utter_ask_Apply",tracker,temp=temp)

        return []
#JobsAPI("Software Engineer")