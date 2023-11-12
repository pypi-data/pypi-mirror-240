from datetime import datetime
from fastapi import Request
from functools import wraps

def custom_logger(ip, port, message, time_taken):
    log_info = f"Sender IP: {ip}, Port: {port}, Message: {message}, Time Taken: {time_taken} seconds"

    # Save logs to a text file
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {log_info}\n")

def log_request(endpoint_function):
    @wraps(endpoint_function)
    async def wrapper(request: Request, *args, **kwargs):
        start_time = datetime.now()
        sender_ip = request.client.host
        sender_port = request.client.port
        log_message = f"Received request at {request.url}"
        result = await endpoint_function(request, *args, **kwargs)
        end_time = datetime.now()
        time_taken = (end_time - start_time).total_seconds()
        custom_logger(sender_ip, sender_port, log_message, time_taken)
        return result
    return wrapper
