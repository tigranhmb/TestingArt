# A Sample class with init method
class videogame:

    # init method or constructor
    def __init__(self, name, genre, multiplayer, publisher):
        self.name = name
        self.genre = genre
        self.multiplayer = multiplayer
        self.publisher = publisher

first_game = videogame("CS:GO", "Shooter", "Yes", "Valve")
print("Game name: " + first_game.name)
print("Genre: " + first_game.genre)
print("Multiplayer: " + first_game.multiplayer)
print("Publisher: " + first_game.publisher)

print("**************")

second_game = videogame("PUBG", "Shooter", "Yes", "Tencent Games")
print("Game name: " + second_game.name)
print("Genre: " + second_game.genre)
print("Multiplayer: " + second_game.multiplayer)
print("Publisher: " + second_game.publisher)


