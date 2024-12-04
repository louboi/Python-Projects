# Make the class
class queue:
    def __init__(self, c):
        self.queue = [None] * c      # Fixed-size array
        self.capacity = c            # Maximum size of the queue
        self.front = 0               # Index of the first item
        self.rear = -1               # Index of the last item
        self.size = 0                # Number of items in the queue

    # Display the queue
    def display_queue(queue_data):
        print("Current Queue:", queue_data["queue"])

    # Add an item to the rear of the queue
    def enqueue(queue_data, item):
        if queue_data["size"] == queue_data["capacity"]:
            print("Queue is full! Cannot add more time travelers.")
            return None
        queue_data["rear"] = (queue_data["rear"] + 1) % queue_data["capacity"]  # Wrap around
        queue_data["queue"][queue_data["rear"]] = item  # Add the item
        queue_data["size"] += 1  # Increment the size
        print(f"Added {item} to the queue.")

    # Remove an item from the front of the queue
    def dequeue(queue_data):
        if queue_data["size"] == 0:
            print("Queue is empty! No time travelers to remove.")
            return None

        item = queue_data["queue"][queue_data["front"]]  # Get the front item
        queue_data["queue"][queue_data["front"]] = None  # Clear the spot (optional)
        queue_data["front"] = (queue_data["front"] + 1) % queue_data["capacity"]  # Wrap around
        queue_data["size"] -= 1  # Decrement the size
        print(f"Removed {item} from the queue.")
        return item

capacity = 5
line = queue(capacity)

line.enqueue("Traveler 1")
line.enqueue(queue, "Traveler 2")
line.enqueue(queue, "Traveler 3")
line.display_queue(queue)

line.dequeue(queue)
line.dequeue(queue)
line.display_queue(queue)

line.enqueue(queue, "Traveler 4")
line.enqueue(queue, "Traveler 5")
line.enqueue(queue, "Traveler 6")  # This should wrap around
line.display_queue(queue)
