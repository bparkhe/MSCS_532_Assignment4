class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # Compare tasks based on priority (adjust based on heap type)
        return self.priority < other.priority  # for min-heap; use `>` for max-heap

    def __str__(self):
        return f"Task(id={self.task_id}, priority={self.priority}, arrival={self.arrival_time}, deadline={self.deadline})"


class PriorityQueue:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap  # True for max-heap, False for min-heap

    def _compare(self, a, b):
        # Helper to compare tasks based on max-heap or min-heap configuration
        return a > b if self.max_heap else a < b

    def insert(self, task):
        """Insert a new task and maintain the heap property."""
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        """Bubble up to maintain heap property."""
        parent_index = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index].priority, self.heap[parent_index].priority):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def extract_top(self):
        """Remove and return the task with the highest/lowest priority."""
        if self.is_empty():
            raise IndexError("Extract from an empty heap")
        
        top_task = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root and pop
        if not self.is_empty():
            self._bubble_down(0)
        
        return top_task

    def _bubble_down(self, index):
        """Bubble down to maintain heap property."""
        length = len(self.heap)
        while index < length:
            left = 2 * index + 1
            right = 2 * index + 2
            extremum = index  # Largest for max-heap, smallest for min-heap

            if left < length and self._compare(self.heap[left].priority, self.heap[extremum].priority):
                extremum = left
            if right < length and self._compare(self.heap[right].priority, self.heap[extremum].priority):
                extremum = right

            if extremum == index:
                break

            self.heap[index], self.heap[extremum] = self.heap[extremum], self.heap[index]
            index = extremum

    def increase_key(self, index, new_priority):
        """Increase priority of a task and adjust its position."""
        if new_priority < self.heap[index].priority:
            raise ValueError("New priority is lower than current priority")
        self.heap[index].priority = new_priority
        self._bubble_up(index)

    def decrease_key(self, index, new_priority):
        """Decrease priority of a task and adjust its position."""
        if new_priority > self.heap[index].priority:
            raise ValueError("New priority is higher than current priority")
        self.heap[index].priority = new_priority
        self._bubble_down(index)

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0

    def __str__(self):
        """String representation of the heap."""
        return "[" + ", ".join(str(task) for task in self.heap) + "]"


# Example usage:
pq = PriorityQueue(max_heap=True)  # max-heap for highest priority first

# Insert some tasks
pq.insert(Task(1, 10, "09:00", "12:00"))
pq.insert(Task(2, 20, "09:30", "13:00"))
pq.insert(Task(3, 15, "10:00", "11:30"))

# Extract the highest priority task
print("Extracted task:", pq.extract_top())

# Increase the priority of the first task
pq.increase_key(0, 25)

# Check if the priority queue is empty
print("Is the queue empty?", pq.is_empty())

# Print the heap
print("Heap:", pq)
