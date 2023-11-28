from fastapi import BackgroundTasks, FastAPI
import logging

app = FastAPI()

logging.basicConfig(filename=f'logs/email_log.txt',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def write_to_log(email: str, message: str):
    logging.info(f"The message '{message}' was sent to '{email}'.")

# def send_email(): ...


@app.post("/send-mail/{email}")
async def send_email(email, data: dict, background_tasks: BackgroundTasks):
    message = data["message"]
    background_tasks.add_task(write_to_log, email, message)
    return {"status": "message sent"}
