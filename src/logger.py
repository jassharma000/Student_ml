import logging
import os
from datetime import datetime
from src.exception import CustomException
import sys
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s %(lineno)s %(name)s - %(levelname)s - %(message)s',
     
)


if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("division by zero")
        raise CustomException(e, sys)
    