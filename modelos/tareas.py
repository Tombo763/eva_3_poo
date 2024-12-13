class Task:
    def __init__(self, id, user_id, title, completed=False):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.completed = completed
