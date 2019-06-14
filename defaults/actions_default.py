from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests


class ActionReceberNome(Action):

    def name(self) -> Text:
        return "action_receber_nome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print(tracker.latest_message['text'])
        return [SlotSet("name", tracker.latest_message['text'])]
