import re

bot_template = "SPOS : {0}"
user_template = "USER : {0}"

name = "SPOS"


def getResponse(msg):
    send_message(msg)


def check_special_command(message):
    match = re.match("^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", message)
    if not match:
        return False
    quad = []
    for number in match.groups():
        quad.append(int(number))
    if quad[0] < 1:
        return False
    for number in quad:
        if number > 255 or number < 0:
            return False
    return True


def respond(message):
    if message in responses:
        bot_message = responses[message]
    elif message in commands:

        if check_special_command(message) is True:
            bot_message = commands[message]
        else:
            bot_message = commands['invalid IP']
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

commands = {
    "Run Scan": "Please specify the Scan Type /n Nmap Scan or Metasploit Scan",
    "run scan": "Please specify the Scan Type",
    "Run Scans": "Please specify the Scan Type",
    "run scans": "Please specify the Scan Type",
    "Nmap Scan": "Please Specify the Host Address",
    "Metasploit Scan": "Please Specify the Host Address",
    "Invalid IP": "Please provide a correct IP.",
    "default": "Please say it again!"

}
