import queue
import time
import random

def generate_request(request_queue):
    request_id = random.randint(1000, 9999)
    request_queue.put(request_id)
    print(f"Request {request_id} has been added to the queue.")

def process_request(request_queue):
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Request {request_id} has been processed.")
    else:
        print("The queue is empty.")

def main():
    request_queue = queue.Queue()

    try:
        while True:
            generate_request(request_queue)
            process_request(request_queue)
            time.sleep(1)  # Пауза для імітації часу на обробку
    except KeyboardInterrupt:
        print("System has been stopped by the user.")

if __name__ == "__main__":
    main()
