import re
import NmapScans
bot_template = "SPOS : {0}"
user_template = "USER : {0}"

name = "SPOS"


def getResponse(msg):
    reply = send_message(msg)

    return reply


def initiate_nmapScan(ip):
    NmapScans.initiate_scan(ip)


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

    elif message not in commands:

        if check_special_command(message) is True:
            initiate_nmapScan(message)
            bot_message = commands["Valid"]
        else:
            bot_message = commands["Invalid IP"]
    else:
        bot_message = responses["default"]

    return bot_message


def send_message(message):
    # print(user_template.format(message))
    response = respond(message)
    # print(bot_template.format(response))

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
    "Run Scan": "Please specify the Scan Type \n Nmap Scan or Vulnerability Scan",
    "run scan": "Please specify the Scan Type \n Nmap Scan or Vulnerability Scan",
    "Run Scans": "Please specify the Scan Type \n Nmap Scan or Vulnerability Scan",
    "run scans": "Please specify the Scan Type \n Nmap Scan or Vulnerability Scan",
    "Nmap Scan": "Please Specify the Host Address",
    "Metasploit Scan": "Please Specify the Host Address",
    "default": "Sorry I didn't understand, Please say it again"
}

commands = {

    "Invalid IP": "Please provide a correct IP.",
    "Valid": "Scanning is Done",
    "default": "Please say it again!"

}
