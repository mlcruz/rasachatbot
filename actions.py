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

        # Preenche informações
        user_id = tracker.get_slot("user_id")
        r = requests.get(
            f'http://localhost:10000/api/actions/{user_id}/simple')
        data = r.json()
        return [SlotSet("first_name", data['firstName']), SlotSet("last_name", data['lastName']), SlotSet("is_actived", data['isActivated']), SlotSet("user_name", data['userName'])]


class ActionMostrarDados(Action):

    def name(self) -> Text:
        return "action_mostrar_dados"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = tracker.get_slot("user_id")

        # Recebe rastreadores da aapi
        trackers = requests.get(
            f'http://localhost:10000/api/actions/{user_id}/trackers')
        data = trackers.json()
        tks = []

        # Imprime sequencia de msg informando os dados da conta do usuario

        is_activated = "Sua conta está ativa"
        if (tracker.slots["is_actived"] == False):
            is_activated = "Sua conta está inativa"

        dispatcher.utter_template("utter_mostrar_dados", tracker)
        dispatcher.utter_message(f"sua conta está {is_activated} \n")

        dispatcher.utter_message("Seus rastreadores: \n")
        for tk in data:
            tks.append(tk['name'])
            dispatcher.utter_message(
                f"{tk['name']} - {tk['phone']} - imei- {tk['imei']}" + "\n")

        return [SlotSet("rastreadores", {"tk": tks})]


class ActionVerificarErros(Action):

    def name(self) -> Text:
        return "action_verificar_erros"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_id = tracker.get_slot("user_id")

        # Chamado de api com logica de verificação de saude da conta
        errorData = requests.get(
            f'http://localhost:10000/api/actions/{user_id}/sanity')
        data = errorData.json()

        # recebe resultado da chamada de api e popula listas com informações de erro
        tracker_errors_data = data["trackerError"]
        subscription_errors_data = data["subscriptionError"]

        # Formato esperado dos erros: [{"error" : string, "trackerId" : int}]
        tracker_errors = []
        subscription_errors = []

        for index, error in enumerate(tracker_errors_data):
            tracker_errors.append({
                "error": error[0]["error"],
                "trackerId": error[0]["trackerId"]
            })

        for index, error in enumerate(subscription_errors_data):
            subscription_errors.append({
                "error": error["error"],
                "trackerId": error["trackerId"]
            })

        all_errors = tracker_errors + subscription_errors

        if (len(all_errors) > 0 ) :
            dispatcher.utter_message("Foram identificados os seguintes problemas:\n ")
            for error in all_errors:
                dispatcher.utter_message(sprintError(error, user_id) + "\n")
        else:
            dispatcher.utter_message("Não foi idenficado nenhum problema\n")
        return []


# returns a string with the correct error message for that error object
def sprintError(error, user_id):
    error_type = error["error"]
    tracker_id = error["trackerId"]

    # Tracker error msg logic
    # Python has no switches :(

    if(tracker_id != 0):
        tracker_name = requests.get(
            f'http://localhost:10000/api/actions/{user_id}/trackerName/{tracker_id}')
        if (error_type == "apn_error"):
            return f"Erro de apn no rastreador {tracker_id} - {tracker_name.text}"
    else:
        if (error_type == "inactive"):
            return "Sua assinatura está inativa."
        if (error_type == "expired"):
            return "Sua assinatura está expirada."
        if (error_type == "too_many_trackers"):
            return "Você tem mais rastreadores cadastrados em sua conta o que o permitido"