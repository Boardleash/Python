#!/usr/bin/env python3

###########################################
### TITLE: github-repo-lister.py        ###
### AUTHOR: Boardleash (Derek)          ###
### DATE: Sunday, February 23 2025      ###
###########################################
#
###################
### DESCRIPTION ###
###################
#
# Credit to user 'kenorb' who posted an answer/response to a similar question on Stack Overflow
# on October 15th, 2025 at 22:56.
# I wanted to build a script around their contribution to make it user interactive, particularly
# to edit the user variable.
# Link to Stack Overflow question and answer:
# https://stackoverflow.com/questions/8713596/how-to-retrieve-the-list-of-all-github-repositories-of-a-person
# This script has been tested on Python version 3.9.12, 3.12.10 and 3.13.5

################################
### FORMATTING AND VARIABLES ###
################################

# Import the 're' module for regex and 'requests' module for API request.

import re
import requests

# Colors

class clrs:
    '''Class to hold color variables'''
    cyn = '\033[1;36m'
    noc = '\033[0m'

#####################
### INTRODUCTIONS ###
#####################

# Set up an introduction to let user know what this script will do.

def intro():
    '''Introduction function that provides information and instruction'''
    print()
    print(clrs.cyn+"Hello!  I can retrieve a list of public Github repositories for a particular user.")
    print("This does NOT clone, checkout or pull files or repositories from the user's GitHub!")
    print("This only provides a list of available repositores that the GitHub user has created.")
    print("I'll have to ask for the user, and, at the end, I'll ask if you wish to save the list.")
    print("If you want to quit out of the script, type 'quit' or 'q' at the second question."+clrs.noc)
    print()

#####################################
### ASK FOR USER and TO SAVE LIST ###
#####################################

def meatnpotatoes():
    '''Ask for the GitHub username and establish a variable for requesting from the GitHub API.'''
    GITUSER = input("What is the GitHub username for the repositores you want to get a list of?: ")
    DATA = requests.get("https://api.github.com/users/"+GITUSER+"/repos?")

    # Set up a pattern to use for parsing the DATA variable.
    PATTERN = 'git@[^"]*'
    SEARCH = re.findall(PATTERN, DATA.text)
    ANSWER = input("Do you want to save this list for future reference? (Yes/No): ")
    if ANSWER == 'Y' or ANSWER == 'Yes' or ANSWER == 'y' or ANSWER == 'yes':
        print()
        for x in SEARCH:
            print(x)
            FILE = open(GITUSER+"_GitHub_Repos", 'a+')
            FILE.write(x+"\n")
            FILE.close()
        print()
        print("The list of GitHub repositories for "+GITUSER+" has been saved in the current directory.")
        print()
    elif ANSWER == 'N' or ANSWER == 'No' or ANSWER == 'n' or ANSWER == 'no':
        print()
        for x in SEARCH:
            print(x)
        print()
        print("The list of GitHub repositores for "+GITUSER+" will NOT be saved for future reference.")
        print()
    elif ANSWER == 'Q' or ANSWER == 'Quit' or ANSWER == 'q' or ANSWER == 'quit':
        exit
    else:
        print("That is not an appropriate response.  Let's start over.")
        meatnpotatoes()

#####################
### MAIN FUNCTION ###
#####################

# Consolidate the two functions above into a main function.

def main():
    '''Main function that will execute the intro() and meatnpotatoes() functions'''
    intro()
    meatnpotatoes()

#############################
### EXECUTE MAIN FUNCTION ###
#############################

# Execute the main function/script.

main()

# EOF

