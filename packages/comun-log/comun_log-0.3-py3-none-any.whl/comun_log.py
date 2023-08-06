import os

import requests


def insert_log_ok(id_project, fecha_inicio, fecha_fin, observations=''):
    try:
        obj = {
            "project_id": id_project,
            "start_date": str(fecha_inicio),
            "end_date": str(fecha_fin),
            "successful": True,
            "observations": observations
        }
        r = requests.post(f'{os.getenv("PARAMS_API_URL")}/execution_log', json=obj, headers={'token': os.getenv('API_TOKEN')})
        r.raise_for_status()
    except Exception as e:
        print(str(e))


def insert_log_ko(id_project, fecha_inicio, fecha_fin, observations=''):
    try:
        obj = {
            "project_id": id_project,
            "start_date": str(fecha_inicio),
            "end_date": str(fecha_fin),
            "successful": False,
            "observations": observations
        }
        r = requests.post(f'{os.getenv("PARAMS_API_URL")}/execution_log', json=obj, headers={'token': os.getenv('API_TOKEN')})
        r.raise_for_status()
    except Exception as e:
        print(str(e))
