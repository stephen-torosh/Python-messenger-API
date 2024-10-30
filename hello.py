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
        return True
    else:
        return False

def GetIndexDirectFromUsername(username) -> list:
    i = info[1]
    k = []
    for j in range(len(i)):
        if (username in i[j]):
            k.append(j)
    return k

def GetIndexDirectFromContact(sender,getter) -> list:
    i = info[1]
    k = []
    for j in range(len(i)):
        if (sender in i[j]) and (getter in i[j]):
            k.append(j)
    return k


# AddUser("Stephen")
# AddUser("Damyr")
# AddUser("Nikita")

# SendMessage("Stephen", "Damyr", "Hey let`s go outside")
# SendMessage("Damyr", "Stephen", "okay, i will invite Nikita too")
# SendMessage("Damyr", "Nikita", "Hello, me and Stephen are going outside, do you want to go with us?")
# SendMessage("Nikita", "Damyr", "Yes, let`s go!")

def getMessagesFromUsername(username):
    direct = GetIndexDirectFromUsername(username)
    answer = ""
    for j in direct:
        answer += f"<h3>{info[1][j]}</h3><p>{info[2][j]}</p>"
    return answer

def getMessagesFromContact(sender, getter):
    direct = GetIndexDirectFromContact(sender,getter)
    answer = ""
    for j in direct:
        answer += f"<h3>{info[1][j]}</h3><p>{info[2][j]}</p>"
    return answer

def getAllUsers():
    answer = ""
    for i in info[0]:
        answer += f"<p>{i}</p>"
    return answer

print(GetIndexDirectFromUsername("Damyr"))
print(GetIndexDirectFromContact("Damyr", "Nikita"))

@app.route('/')
def main():
    return "<h1>Hello! This is my Flask messenger API, made using Python!</h1><a href='https://github.com/stephen-torosh/Python-messenger-API'>Github project</a>"


@app.route('/u/<username>')
def UserMessages(username):
    if (getMessagesFromUsername(username) != ""):
        return f"<h1>Hello! Here are all of {username}`s messages:</h1>{getMessagesFromUsername(username)}"
    else:
        return f"Sorry, but user {username} doesn`t have any contacts or messages, or the user possibly doesn`t even exist"

@app.route('/s/<sender>/<getter>/<message>')
def SendMessageRoute(sender, getter, message):
    if SendMessage(sender,getter,message):
        return f'Message "{message}" successfully sent with "{sender}" as sender, and "{getter}" as getter'
    else:
        return 'Sorry, there was an error in sending a message'
    
@app.route('/c/<username>')
def createUser(username):
    AddUser(username)
    return f'User successfully created with the username - {username}!'

@app.route('/a')
def AllUsers():
    if (getAllUsers() != ""):
        return "<h1>Here all of users:</h1>" + getAllUsers()
    else:
        return "Sorry, there aren`t any users on this server!"

@app.route('/m/<sender>/<getter>')
def ContactMessages(sender,getter):
    if (getMessagesFromContact(str(sender), str(getter)) != ""):
        return f'<h1>Hello! Here are all of {sender} & {getter} contact messages:</h1>{getMessagesFromContact(str(sender), str(getter))}'
    else:
        return f"Sorry, but the contact between {sender} & {getter} doesn`t exist, or one or both of these users doesn`t exist"