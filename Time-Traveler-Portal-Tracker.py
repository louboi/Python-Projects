'''
| need | Add
| need | Remove
| need | Capacity
| need | Manage the line
| need | 
'''

class TimeTravelerQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, traveler):
        """Add the traveller to the queue"""
        if self.rear == self.capacity - 1:
            print("overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = traveler
        print(f"{traveler} has joined the queue")

    def dequeue(self):
        """Remove the traveller from the queue"""
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow: No travelers left in the queue.")
            return None
        traveler = self.queue[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = -1
            self.rear = -1
        print(f"{traveler} has left the queue")
        return traveler

    def display(self):
        """Display the current state of the queue."""
        if self.front == -1:
            print("The portal queue is empty.")
        else:
            print("Current queue:", self.queue[self.front:self.rear + 1])

queue = TimeTravelerQueue(500)

Done = "f"

while Done == "f":
    Done = str(input("Are you done? "))
    traveler = str(input("What is your name? "))
    queue.enqueue(traveler)

queue.display()