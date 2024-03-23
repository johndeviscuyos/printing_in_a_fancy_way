#pseudocode
import colorama
from colorama import Fore,Back, Style
import pyfiglet
colorama.init()

#Import Text
import pyttsx3
text_speech = pyttsx3.init()

name_speech = ("What is your name?")
text_speech.say(name_speech)
text_speech.runAndWait()
#ask user their name
name = input("What is your name? ")

speak_name = ("Hello " + name + ", May I know what is your dream job?")
text_speech.say(speak_name)
text_speech.runAndWait()
#ask user their dream job
dream_job= input("What is your dream job? ")

#print a goodluck msg
goodluck_message = (name + " your dream job is " + dream_job + ". Goodluck on achieving your dreams and keep striving")
print (goodluck_message)
text_speech.say(goodluck_message)
text_speech.runAndWait()

#print dream job and name in a fancy way
art_text=pyfiglet.figlet_format(text= name+ " the "+ dream_job,
                            font="slant")
print (art_text)

print('Additional Info')
print("Some of the most in-demand tech-related jobs in today's market include Data Scientists, who leverage statistical analysis and machine learning techniques to extract insights from large datasets and inform business decisions.\nCybersecurity Analysts are also highly sought after, responsible for protecting an organization's computer systems and networks from cyber threats by implementing security measures and monitoring for breaches.\nAdditionally, Cloud Architects play a pivotal role in designing and implementing cloud-based solutions, ensuring scalability, reliability, and optimal performance for businesses migrating to the cloud.\nLastly, AI/Machine Learning Engineers are increasingly in demand, focusing on developing and deploying algorithms and models that enable machines to perform tasks that typically require human intelligence, driving advancements in automation and personalization across various industries.")
