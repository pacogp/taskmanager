class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else " "
        return f"Task ID: {self.id}, Description: {self.description}"
    
class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print (f"Task added: {task}")


    def list_task(self):
        if not self._tasks:
            print("No tasks available.")
        else:
            for task in self._tasks:
                print(task)

    def complete_tasks(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Task completed: {task}")
                return
        print(f"Task with ID {id} not found.")

    def delete_task(self):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task deleted: {task}")
                return
        print(f"Task with ID {id} not found.")    


