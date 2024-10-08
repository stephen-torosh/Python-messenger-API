from flask import Flask

app = Flask(__name__)

code = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <h1>Hello World!</h1>
    <h3>Welcome to my site!!</h3>

</body>
</html>

<style>

</style>

'''

@app.route("/")
def hello_world():
    return code