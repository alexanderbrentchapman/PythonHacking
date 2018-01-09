#usr/bin/env python3

# created 1/6/2018
# updated 1/6/2018

"""
TODO: @alexander_chapman work on local net tools and stats
"""


#imports
import socket
import sys
import urllib.request
from html.parser import HTMLParser

print("Created 1/6/2018")
print("Updated 1/6/2018")   # remember to update this with each file change
print("Version 1")

#############
# FUNCTIONS #
#############
def check_int(var):     # check if var is int; returns true if int, false if not
    if var is int:
        return True
    else:
        return False

def add_strings(str1, str2):
    return str1 + str2

# website tools
def download_webpage(url, save_name):
        urllib.request.urlretrieve(url=url, filename=save_name)


# parse html
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered start tag: ", tag)

    def handle_endtag(self, tag):
        print("Encountered end tag: ", tag)

    def handle_data(self, data):
        print("Encountered data: ", data)


#########
# MENUS #
#########

# main
mainMenu = """
Select Option
1) Local Networking
2) Website Tools
3) Statistics
4) Connection Tools
"""
locNet = "1"
webTools = '2'
stats = '3'
connTools = '4'

# web tools
webMenu = """
Select Option
1) Download a Webpage
2) Crawl a Webpage
3) Parse a Webpage
"""
dlPage = '1'
crawlPage = '2'

###################
# SETUP VARIABLES #
###################

toolPath = ""   # this is to keep track of the users current position in the menus and as a quick ref for tool locations


#################
# PROGRAM START #
#################

# MAIN MENU
print(mainMenu) # displaying main menu
option = input(">>> ")  # getting option from user
# updating tool location
if option == locNet:
    toolPath = "1"
elif option == webTools:
    toolPath = "2"
elif option == stats:
    toolPath = "3"
elif option == connTools:
    toolPath = '4'
else:
    print("Invalid option. Exiting...")
    exit()


# LOCAL NETWORK TOOLS
if toolPath == "1":
    pass

# WEBSITE TOOLS
elif toolPath == "2":
    print(webMenu)
    option = input(">>> ")

    # DOWNLOAD A WEBPAGE
    if option == '1':
        toolPath = "2.1"

        webAddr = input("Website Address: ")    # website address
        saveAs = input("Save file as: ")    # save as
        download_webpage(webAddr, saveAs)
        print("Webpage saved to {0}".format(saveAs))

    # CRAWL A WEBPAGE
    if option == '2':
        toolPath = "2.2"

    # PARSE A WEBPAGE
    if option == '3':
        toolPath = '2.3'

        # getting the contents of file and storing to variable contents
        filename = input("HTML File: ")
        file = open(filename)
        contents = file.read()
        file.close()

        parser = MyHTMLParser()
        parser.feed(contents)


# STATISTICS
elif toolPath == "3":
    pass

# CONNECTION TOOLS
elif toolPath == '4':
    pass
