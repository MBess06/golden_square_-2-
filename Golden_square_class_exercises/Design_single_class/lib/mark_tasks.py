class mark_tasks:
    def __init__(self):
        self._tasks = []
    def add_task(self, task):
        return self._tasks.append(task)

    def incomplete_tasks(self):
        return self._tasks

    def complete_tasks(self, index):
        if index < 0 or index >= len(self._tasks):
            raise Exception("Out of list range")
        return self._tasks.remove(self._tasks[index])
