# -*- coding: utf-8 -*-
import redis
import json
import pandas as pd
import settings
import time

db = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

def save_feedback(response):
    """
    Guarda las predicciones que tuvieron un feedback como erróneas dentro del container feedback:/data/feedback.csv
    """
    json_response = json.dumps([json.loads(response)])
    pd.read_json(json_response).to_csv('/data/feedback.csv', index=False, mode='a', header=False)
    

def feedback_process():
    """
    Obtiene trabajos encolados por el cliente desde Redis. Los procesa
    y los guarda en un archivo CSV.
    Toda la comunicación se realiza a travez de Redis, por ello esta
    función no posee atributos de entrada ni salida.
    """
    while True:
        queue = db.lrange(settings.REDIS_QUEUE, 0, 9)

        # Iteramos por cada trabajo obtenido
        for q in queue:
            # q = {'id': 0, 'data': json}
            q = json.loads(q.decode("utf-8"))
            save_feedback(q["data"])

        db.ltrim(settings.REDIS_QUEUE, len(queue), -1)
        time.sleep(2)

if __name__ == "__main__":
    print("Launching Feedback service...")
    feedback_process()
