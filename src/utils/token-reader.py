from os import path


def getClientToken():
    if not path.exists("resources/client-token"):
        raise Exception("No client token file found! Make sure you have a token for the discord bot and it is located in a file 'resources/client-token'.")

    f = open("resources/client-token", "r")
    return f.readline().strip()