"""
Este pequeño programa tiene el objetivo de probar el servicio de voz que permite usar python, en concreto este pequeño
programa te permite realizar dos funciones, la primera es la de apagar tu equipo si le dices 'Apagar' y la otra funcion
es la de buscar en internet, para activar esta funcion le tienes que decir 'servicio' y se activara el buscador, este
buscador se divide en dos partes, la primera parte le dices el objeto que buscar y la segunda parte lo que quieres hacer
con dicho objeto (Ejemplo: Pingu - bailando).
"""

import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
 print('speak now:')
 audio = r3.listen(source)
 text = str(r2.recognize_google(audio, language = 'es-Es'))



 if text == 'servicio':
  def services(text):
   with sr.Microphone() as source:
    print('¿Que deseas hacer?')
    audio = r2.listen(source)
    text = str(r2.recognize_google(audio, language='es-Es'))
   if text == 'apagar':
    import os
    os.system("shutdown /s /t 1")

  services(text)
 if text in r2.recognize_google(audio, language = 'es-Es') :
  r2 = sr.Recognizer()
  url = 'https://www.google.com/search?q='+text
  with sr.Microphone() as source:
   print ('¿Que hace'+ text+'?')
   audio = r2.listen(source)

   try:
    get = r2.recognize_google(audio, language = 'es-Es')
    print(get)
    wb.get().open_new(url+get)
   except sr.UnknownValueError:
    print('error')
   except sr.RequestError as e:
     print('failed'.format(e))

"""
#Asi son los comentarios.
a1 = b1 = c1 = "multiple Variables"
fruits = ["kiwi",1,"papaya"]
a2,b2,c2 = fruits
test= 10 #int
age = 20 #int
union = age + test
texto = "Texto" #Texto
print(a1)
print(b1)
print(c1)
print(a2)
print(b2)
print(c2)
print(union)
if age == 20:
 print(age + test
if cebolla == 10:
 print("Esto es un " + a2)
if texto == "Texto":
 print(texto)

#Global variables

x= "engerenge"

def functiontesting():
 x = test
 print("Python is" + x)
functiontesting()
print(x)
print(type(x))
print(type(fruits))
"""