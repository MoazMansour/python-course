import urllib

def read_text():
    file = open("/Users/moazmansour/OneDrive/Education/Udacity/Full Stack Development/text.txt")
    content = file.read()
    file.close()
    print(content)
    check_profanity(content)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
    output = connection.read()
    connection.close()
    if "true" in output:
        print ("Alert")
    else:
        print ("You are good to go")

read_text()
