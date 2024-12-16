from modelos.usuarios import User

class Task(User):
    def __init__(self, id=0, user_id=0, title="", completed=False, name="", username="", email="", phone="", website=""):
        super().__init__(id=user_id, name=name, username=username, email=email, phone=phone, website=website)
        self.id = id
        self.user_id = user_id
        self.title = title
        self.completed = completed
