import requests
import time
from datetime import datetime
import os

# Obtener los secrets desde las variables de entorno
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
USER_GROUP_ID = os.getenv('USER_GROUP_ID')

# Verificar que los secrets están configurados correctamente
if not SLACK_TOKEN or not USER_GROUP_ID:
    raise ValueError("SLACK_TOKEN or USER_GROUP_ID not set in the environment")

print(f"SLACK_TOKEN: {SLACK_TOKEN}")
print(f"USER_GROUP_ID: {USER_GROUP_ID}")

# Definición de los IDs de los usuarios
users = {
    'Andrés': 'U07FFFQRG4D',
    'Lalo': 'U078PC6QU8N',
    'Lucila': 'U054S41LQ8Y',
    'Nancy': 'U0463NZ1LTU',
    'Zai': 'U04681B1JRG',
    'Julio': 'U078YFDTA5A',
    'Susy': 'U04666ZH4TW',
    'Armando': 'U0463LXQHD0'
}

# Horarios de lunes a jueves
horarios_lunes_jueves = {
    '09:00': users['Zai'],
    '10:00': users['Susy'],
    '11:00': users['Julio'],
    '12:00': users['Lalo'],
    '13:00': users['Armando'],
    '15:00': users['Nancy'],
    '16:00': users['Andrés'],
    '17:00': users['Lucila']
}

# Horarios del viernes
horarios_viernes = {
    '09:00': users['Zai'],
    '10:00': users['Susy'],
    '11:00': users['Armando'],
    '12:00': users['Lalo'],
    '13:00': users['Lucila'],
    '15:00': users['Julio'],
    '16:00': users['Nancy'],
    '17:00': users['Andrés']
}

def update_user_group(user_id):
    url = 'https://slack.com/api/usergroups.users.update'
    headers = {
        'Authorization': f'Bearer {SLACK_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'usergroup': USER_GROUP_ID,
        'users': user_id,
    }
    response = requests.post(url, headers=headers, json=data)
    print(f"Request to {url} with data {data}")
    if response.status_code != 200:
        raise Exception(f"Error updating user group: {response.status_code} - {response.text}")
    print(f"Updated user group with user ID {user_id}: {response.json()}")
    return response.json()

def get_current_hour():
    return datetime.now().strftime('%H:%M')

def get_current_day():
    return datetime.now().strftime('%A')

def run_scheduler():
    while True:
        current_hour = get_current_hour()
        current_day = get_current_day()

        print(f"Current time: {current_hour} on {current_day}")

        if current_day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday']:
            if current_hour in horarios_lunes_jueves:
                print(f"Updating user group at {current_hour} on {current_day}")
                update_user_group(horarios_lunes_jueves[current_hour])
        elif current_day == 'Friday':
            if current_hour in horarios_viernes:
                print(f"Updating user group at {current_hour} on {current_day}")
                update_user_group(horarios_viernes[current_hour])

        # Esperar un minuto antes de verificar nuevamente
        time.sleep(60)

if __name__ == '__main__':
    run_scheduler()
