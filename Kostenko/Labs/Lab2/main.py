class Player:
    def __init__(self, **data):
        for key, value in data.items():
            self[key] = value

idk = Player(5, 1, 3, True, "funny")
print(idk)