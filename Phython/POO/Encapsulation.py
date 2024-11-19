class password:
    def __init__(self):
        self._password = "qwerty1234"
        self.__password = "qwerty12345"

n = password()

print(n.__password)