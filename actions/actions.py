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
import sys
import time
from bs4 import BeautifulSoup
import requests
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher


class ActionFetchWebsiteData(Action):

    def name(self) -> str:
        return "action_fetch_website_data"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        try:
            page = requests.get('https://foc.kdu.ac.lk/')
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            dispatcher.utter_message(text=f"Error for link: https://foc.kdu.ac.lk/")
            dispatcher.utter_message(text=f"{error_type} at Line: {error_info.tb_lineno}")
            return []

        time.sleep(2)  # Simulate any loading delay if needed
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.find_all('p')

        # Collect and display the data
        scraped_data = ""
        for i in links:
            scraped_data += i.text + "\n\n"  # Collect scraped paragraphs

        # Send the scraped data as a message to the chatbot
        if scraped_data:
            dispatcher.utter_message(text=scraped_data)
        else:
            dispatcher.utter_message(text="Couldn't find any data to scrape.")

        return []


