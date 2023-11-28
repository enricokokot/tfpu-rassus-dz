import os
from datetime import datetime

def perform_action(action):
    try:
        # Simulate an action that might raise an exception
        # For demonstration purposes, we'll raise an exception for actions containing the word "error"
        if 'error' in action.lower():
            raise Exception(f"Simulated error for action: {action}")
        
        # If no exception, perform the action
        result = f"Action '{action}' completed successfully"

    except Exception as e:
        # Log the error and its details
        log_error(f"Error in action '{action}': {str(e)}")
        result = f"Action '{action}' failed. Check the log for details."

    else:
        # If no exception, log the successful action
        log_action(action, result)

    return result

def log_action(action, result):
    # Get today's date
    today_date = datetime.now().strftime('%d-%m-%Y')

    # Create the log file name with today's date
    log_filename = f"log_{today_date}.txt"

    # Log the action and result
    with open(log_filename, 'a') as log_file:
        log_file.write(f"{datetime.now()} - {action}: {result}\n")

def log_error(error_message):
    # Get today's date
    today_date = datetime.now().strftime('%d-%m-%Y')

    # Create the log file name with today's date
    log_filename = f"log_{today_date}.txt"

    # Log the error message
    with open(log_filename, 'a') as log_file:
        log_file.write(f"{datetime.now()} - ERROR: {error_message}\n")

def read_log(log_filename):
    # Read and print the contents of the log file
    with open(log_filename, 'r') as log_file:
        log_contents = log_file.read()
        print("Log contents:\n", log_contents)

# Get today's date for creating the log file
today_date = datetime.now().strftime('%d-%m-%Y')
log_filename = f"log_{today_date}.txt"

# Create the log file if it doesn't exist
if not os.path.exists(log_filename):
    with open(log_filename, 'w') as log_file:
        log_file.write(f"Log file created on {datetime.now()}\n")

# Example usage with potential error
action1 = "Open file"
action2 = "Read data"
action3 = "Close connection"
action4 = "Perform error operation"

result1 = perform_action(action1)
result2 = perform_action(action2)
result3 = perform_action(action3)
result4 = perform_action(action4)

# Read and print the log
read_log(log_filename)
