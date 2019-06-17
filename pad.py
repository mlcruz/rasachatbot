import requests
import json

user_id = "B95153C1-8CD0-41A4-A3E2-B3394EFB9020"
errorData = requests.get(f'http://localhost:10000/api/actions/{user_id}/sanity')
data = errorData.json()

# recebe resultado da chamada de api e popula listas com informações de erro

tracker_errors_data = data["trackerError"]
subscription_errors_data = data["subscriptionError"]


# Formato esperado dos erros: [{"error" : string, "trackerId" : int}]
tracker_errors = []
subscription_errors = []

for index, error in enumerate(tracker_errors_data):
    tracker_errors.append({
        "error" : error[0]["error"],
       "trackerId": error[0]["trackerId"]
    })
    
for index, error in enumerate(subscription_errors_data):
    subscription_errors.append({
        "error" : error["error"],
       "trackerId": error["trackerId"]
    })

all_errors = tracker_errors + subscription_errors

# returns a string with the correct error message for that error object
def sprintError(error):
    return_string = ""
    error_type = error["error"]
    tracker_id = error["trackerId"]
    
    # Tracker error msg logic
    # Python has no switches :(

    if(tracker_id != 0):
        tracker_name = requests.get(f'http://localhost:10000/api/actions/{user_id}/trackerName/{tracker_id}')
        if (error_type == "apn_error") : return f"Erro de apn no rastreador {tracker_id} - {tracker_name.text}"
    else:
        if (error_type == "inactive") : return "Sua assinatura está inativa."
        if (error_type == "expired") : return "Sua assinatura está expirada."
        if (error_type == "too_many_trackers") : return "Você tem mais rastreadores cadastrados em sua conta o que o permitido"
            

for error in all_errors:
    print(sprintError(error))
