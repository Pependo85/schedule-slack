import os
import requests
import datetime
import pytz

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
USER_GROUP_ID = os.getenv("USER_GROUP_ID")

# Función para actualizar el grupo de usuarios en Slack
def update_slack_user_group(usergroup_id, users):
    url = "https://slack.com/api/usergroups.users.update"
    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "usergroup": usergroup_id,
        "users": ",".join(users)
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Response from Slack API: {response.json()}")  # Mensaje de depuración
    return response.json()

# Simulación de la lógica de tu script
def main():
    print("Starting Slack Scheduler...")  # Mensaje de depuración

    # Establecer la zona horaria de la Ciudad de México
    tz = pytz.timezone('America/Mexico_City')
    now = datetime.datetime.now(tz)
    
    current_hour = now.strftime("%H:%M")
    current_day = now.strftime("%A")
    print(f"Current time in Mexico City: {current_hour} on {current_day}")  # Mensaje de depuración
    
    # Aquí puedes añadir la lógica para decidir cuándo actualizar el grupo de usuarios
    if current_hour == "09:00" and current_day == "Monday":
        users = ["U04681B1JRG"]  # Lista de usuarios para el ejemplo
        result = update_slack_user_group(USER_GROUP_ID, users)
        print(f"Update result: {result}")  # Mensaje de depuración

if __name__ == "__main__":
    main()
