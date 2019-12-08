import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
	print("Hallo")
	audio = r.listen(source)
	print("Terima kasih")

try:
	print("TEXT :"+r.recognize_google(audio))
except:
	pass
