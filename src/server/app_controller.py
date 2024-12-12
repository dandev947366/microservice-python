

class AppController:
    def __init__(self):
        pass
    def get_resource(self, name):
        return f"You gave me {name}"

app_controller = AppController()