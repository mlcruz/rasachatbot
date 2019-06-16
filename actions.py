from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, BotUttered
from rasa_sdk.forms import FormAction
import requests
import json

class ActionReceberNome(Action):

    def name(self) -> Text:
        return "action_receber_user_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = tracker.get_slot("user_id")
        r = requests.get(f'http://localhost:10000/api/actions/{user_id}/simple')
        data = r.json()
        return [SlotSet("first_name", data['firstName']), SlotSet("last_name", data['lastName']), SlotSet("is_actived", data['isActivated']) ,SlotSet("user_name", data['userName'])]

class ActionMostrarDados(Action):

    def name(self) -> Text:
        return "action_mostrar_dados"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = tracker.get_slot("user_id")
        trackers = requests.get(f'http://localhost:10000/api/actions/{user_id}/trackers')
        data = trackers.json()

        dispatcher.utter_custom_json(data)
        return [SlotSet("rastreadores", data['data'])]
