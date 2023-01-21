import requests
from loguru import logger

import configs



try:
    url = configs.CONFIGS.get("URL")
    r = requests.get(url, timeout=10)
    
    if r.status_code == 200:
         logger.add("logs/client_request.log", filter=lambda record: "special" in record["extra"])
         logger.bind(special=True).success(f"Client has successfully sent request to Server. status: {r.status_code}.")
except Exception as e:
    logger.add("logs/server_error.log", filter=lambda record: "special" in record["extra"])
    logger.bind(special=True).error(f"{e}")