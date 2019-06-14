from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import requests


class ActionReceberNome(Action):

    def name(self) -> Text:
        return "action_receber_nome"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(tracker.latest_message['text'])
        return [SlotSet("name", tracker.latest_message['text'])]


class CadastrarRastreadorForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "cadastrar_rastreador_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["n_telefone_form", "imei_form", "tk_type_form", "apn_form"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "n_telefone_form": self.from_entity(entity="n_telefone"),
            "imei_form": [
                self.from_entity(entity="imei")
            ],
            "tk_type_form": [
                self.from_entity(entity="rastreador"),
            ],
            "apn_form": [
                self.from_intent(intent="apn"),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        dispatcher.utter_template("utter_slots_values", tracker)
        return []
