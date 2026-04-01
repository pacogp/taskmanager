import json 


class Task:

    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else " "
        return f"Task ID: {self.id}, Description: {self.description}"
    
class TaskManager:

    FILENAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print (f"Task added: {task}")
        self.save_tasks()


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
                self.save_tasks()
                return
        print(f"Task with ID {id} not found.")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task deleted: {task}")
                self.save_tasks()
                return
        print(f"Task with ID {id} not found.")    

    def load_tasks(self):
        
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1                
                
        except FileNotFoundError:
                self._tasks = []
            
    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)

