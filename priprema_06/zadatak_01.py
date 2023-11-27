import logging
from datetime import datetime
import os.path
import time

logging.basicConfig(filename=f'logs/log_{datetime.today().strftime('%Y-%m-%d')}.txt',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

if os.stat(f"logs/log_{datetime.today().strftime('%Y-%m-%d')}.txt").st_size == 0:
    with open(f'logs/log_{datetime.today().strftime('%Y-%m-%d')}.txt',
              'a',
              encoding='utf-8') as f:
        f.write(f"Log file created {
            datetime.today().strftime('%Y-%m-%d %H:%M:%S')}\n\n")


def perform_action(action):
    try:
        if "error" in action.lower():
            raise Exception(f"Error during action '{
                            action}': Simulated error for action: {action}")
        log_action(action)
    except Exception as err:
        log_error(str(err))


# logging.info(f"{
#     datetime.today().strftime('%Y-%m-%d %H:%M:%S')} - Otvori datoteku: Akcija 'Otvori datoteku' uspješno dovršena")
# logging.info(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#                 } - Pročitaj podatke: Akcija 'Pročitaj podatke' uspješno dovršena")
# logging.info(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#                 } - Zatvori vezu: Akcija 'Zatvori vezu' uspješno dovršena")
def log_action(action):
    logging.info(f"{action}: Action '{action}' successfully completed")


# def log_error(): ...


# logging.error(f"{datetime.today().strftime('%Y-%m-%d')
#                  } - GREŠKA: Pogreška u akciji 'Izvrši operaciju s pogreškom': Simulirana pogreška za akciju: Izvrši operaciju s pogreškom")
def log_error(error_message):
    logging.error(f"ERROR: {error_message}")


def read_log(log_filename):
    with open(log_filename,
              'r',
              encoding='utf-8',
              errors='replace') as f:
        log_content = f.read()

    print(log_content)


def main():
    actions = [
        "Open file",
        "Read data",
        "Close connection",
        "Complete task with error",
    ]

    for action in actions:
        perform_action(action)
        time.sleep(5)
    read_log(f'logs/log_{datetime.today().strftime('%Y-%m-%d')}.txt')


main()
