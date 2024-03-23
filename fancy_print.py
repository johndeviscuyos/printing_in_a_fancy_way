#pseudocode
import colorama
from colorama import Fore,Back, Style
import pyfiglet
colorama.init()

#Import Text
import pyttsx3
text_speech = pyttsx3.init()

#ask user their name
name = input("What is your name? ")
#ask user their dream job
dream_job= input("What is your dream job? ")
#print a goodluck msg
goodluck_message = (name + " your dream job is " + dream_job + ". Goodluck on achieving your dreams and keep striving")

#print dream job and name in a fancy way