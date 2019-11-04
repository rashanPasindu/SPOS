bot_template = "SPOS : {0}"
user_template = "USER : {0}"

name = "SPOS"


def getResponse(msg):
    send_message(msg)


def respond(message):
    if message in responses:
        bot_message = responses[message]
    else:
        bot_message = responses["default"]

    return bot_message


def send_message(message):
    print(user_template.format(message))

    response = respond(message)
    print(bot_template.format(response))

    response = bot_template.format(response)
    return response


responses = {
    "Hello": "Hi :)",
    "hello": "hi :)",
    "Hi": "Hi :)",
    "hi": "Hi :)",
    "What is your name?": "My Name is {0}".format(name),
    "What's your name?": "My Name is {0}".format(name),
    "what is your name?": "My Name is {0}".format(name),
    "what's your name?": "My Name is {0}".format(name),
    "default": "Sorry I didn't understand, Please say it again"
}
