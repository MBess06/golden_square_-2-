class todo_tasks:
    def __init__(self):
        self.task_list = []
        
    def add_task(self, task):
        if isinstance(task, str) == False:
            raise Exception("Please add a task.")
        return self.task_list.append(task)

    def present_tasks(self):
        if self.task_list == []:
            raise Exception("Todo list is empty. Please add tasks")
        return self.task_list