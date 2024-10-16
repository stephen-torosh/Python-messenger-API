from flask import Flask
from markupsafe import escape

app = Flask(__name__)

info = [[], [], []]

def AddUser(username):
    info[0].append(username)

def SendMessage(sender, getter, message):
    if (sender in info[0]) and (getter in info[0]):
        info[1].append(sender + ' ' + getter)   
        info[2].append(message)    

def GetIndexDirectFromUsername(username) -> list:
    i = info[1]
    k = []
    for j in range(len(i)):
        if (username in i[j]):
            k.append(j)
    return k


AddUser("Stephen")
AddUser("Damyr")
AddUser("Nikita")

SendMessage("Stephen", "Damyr", "Hey let`s go outside")
SendMessage("Damyr", "Stephen", "okay, i will invite Nikita too")
SendMessage("Damyr", "Nikita", "Hello, me and Stephen are going outside, do you want to go with us?")
SendMessage("Nikita", "Damyr", "Yes, let`s go!")

def getMessagesFromUsername(username):
    direct = GetIndexDirectFromUsername(username)
    answer = ""
    for j in direct:
        answer += f"<h3>{info[1][j]}</h3><p>{info[2][j]}</p>"
    return answer

@app.route('/')
def main():
    return "<h1>Hello! This is my messenger</h1>"


@app.route('/<username>')
def UserMessages(username):
    return f"<h1>Hello! Here are all of {username}`s messages:</h1>{getMessagesFromUsername(username)}"
