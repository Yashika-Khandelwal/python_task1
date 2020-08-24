import pyttsx3
import os

pyttsx3.speak("Welcome to my menu!")
print()
print("Welcome! Hope you are doing well.")
print()
print("         ------------------------------------------------------------------------------         ")
print()
print()


while True:
	
	print("What can I do for you : " , end=" ")
	p = input()
	
	if (("run" in p) or  ("execute" in p ) or ("start" in p)) and (("Visual" in p) or ("visual" in p)) and (("Studio" in p) or ("studio" in p)):
	  pyttsx3.speak('Starting Visual Studio Code')
	  os.system("code")

	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")
	
	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  ("putty" in p):
	  os.system("putty")

	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and  (("jupyter" in p) or ("notebook" in p)):
	  os.system("jupyter notebook")

	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and (("chrome" in p) or ("browser" in p)):
	  os.system("start chrome")
	
	elif (("run" in p) or  ("execute" in p ) or ("start" in p)) and (("vlc" in p) or ("video player" in p)):
	  os.system("start vlc") 
	
	elif ("send" in p) and (("mail" in p) or ("email" in p)):
	  os.system("python mail.py")

	elif  ("exit" in p)  or ("quit" in p) or ("abort" in p) or ("stop" in p):
	  pyttsx3.speak('Bye! Hope you enjoyed')
	  break

	else:
	  print("dont support")
	print("\n")
	print("                      ----------------------------------------------------------------------                 ")
	print("\n")
