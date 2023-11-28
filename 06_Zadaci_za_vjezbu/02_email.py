from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_to_log(message: str):
    with open("email_log.txt", mode="a") as log:
        log.write(message)

@app.post("/send-email/{email}")
async def send_email(email: str, message: str, background_tasks: BackgroundTasks):
    email_message = f"Message to {email}: {message}\n"
    background_tasks.add_task(write_to_log, email_message)
    return {"message": "Email sent successfully"}
