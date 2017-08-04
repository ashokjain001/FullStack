# This program will check for profanity in your text document if there is it will print "Profanity alert" and "document
# has no profanity" if there is no profanity. It reads the content of the file and checks against the website "http://www.wdylike.appspot.com/?q="

from urllib import urlopen

def profanity():
    texts =  open("/Users/ashokjain/Desktop/Python/movie_quotes.txt","r")
    file_contents = texts.read()
    print file_contents
    check_profanity(file_contents)
    texts.close()
def check_profanity(text_to_check):
    connection = urlopen("http://www.wdylike.appspot.com/?q=" +text_to_check)
    output = connection.read()
    connection.close()
    if(output) == True:
        print "Profanity Alert"
    else:
        print "Document has no profanity"

print profanity()