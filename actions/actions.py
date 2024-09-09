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

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
try:
    from bs4 import BeautifulSoup
    import requests
    print("Modules imported successfully!")
except ModuleNotFoundError as e:
    print(f"Error importing modules: {e}")


class ActionFetchWebsiteData(Action):

    def name(self) -> str:
        return "action_fetch_website_data"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        # URL of the website to scrape
        url = "https://kdu.ac.lk/"

        # Send a GET request to the website
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract specific data from the website (modify as needed)
        # For example, finding a specific tag:
        data = soup.find("div", {"class": "info-section"}).get_text()

        # Respond back with the scraped data
        dispatcher.utter_message(text=f"Here is the information from the website: {data}")

        return []
