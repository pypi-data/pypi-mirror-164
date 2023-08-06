import datetime
import os

import requests
from datetime import datetime


def insert_log_ok(id_project, observations='', fecha_inicio=None):
    try:
        fecha_fin = str(datetime.now())
        if fecha_inicio is not None:
            fecha_inicio = str(fecha_inicio)

        obj = {
            "project_id": id_project,
            "start_date": fecha_inicio,
            "end_date": fecha_fin,
            "successful": True,
            "observations": observations
        }
        r = requests.post(f'{os.getenv("PARAMS_API_URL")}/execution_log', json=obj, headers={'token': os.getenv('API_TOKEN')})
        r.raise_for_status()
    except Exception as e:
        print(str(e))


def insert_log_ko(id_project, observations='', fecha_inicio=None):
    try:
        fecha_fin = str(datetime.now())
        if fecha_inicio is not None:
            fecha_inicio = str(fecha_inicio)

        obj = {
            "project_id": id_project,
            "start_date": fecha_inicio,
            "end_date": fecha_fin,
            "successful": False,
            "observations": observations
        }
        r = requests.post(f'{os.getenv("PARAMS_API_URL")}/execution_log', json=obj, headers={'token': os.getenv('API_TOKEN')})
        r.raise_for_status()
    except Exception as e:
        print(str(e))
