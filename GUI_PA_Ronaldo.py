import speech_recognition as sr
import pyaudio,os
import time
from time import asctime
import os
from gtts import gTTS
import pyglet
from termcolor import colored
import webbrowser as wb
import tkinter
from pyowm import OWM
import subprocess
import threading
import rumps
from PyDictionary import PyDictionary
import re
import urllib.request
import urllib.parse
dictionary=PyDictionary()
owm = OWM('eb2d837c4d8015c5dc0762433171679d')
###########################################################################
class Ronaldo(rumps.App):
    @rumps.clicked("Quit Ronaldo")
    def quit(self, _):
        rumps.quit_application(sender=None)

def speak(data):
  tts = gTTS(text=data, lang='en')
  tts.save('NewAudio.mp3')

gah = tkinter.Tk()

class Monitor(object):
  @classmethod
  def write(cls, s):
      cls.text.insert(tkinter.END, str(s) + "\n")
      cls.text.see(tkinter.END)
      cls.text.update()
  text = tkinter.Text(gah, width = 100, height = 10)
  text.pack()

Monitor.write('Ronaldo is online')
speak('Ronaldo is online') 
InitMusic = pyglet.media.load('NewAudio.mp3', streaming=False)
InitMusic.play()
time.sleep(InitMusic.duration)

os.remove('NewAudio.mp3')#remove temperory file
         



class App():
  gah.title("Ronaldo")
  def __init__(self, master):
      self.isrecording = False
      self.button = tkinter.Button(gah, text='Push to Talk')
      self.button.bind("<Button-1>",self.startrecording)
      self.button.bind("<ButtonRelease-1>", self.stoprecording)
      self.button.pack()

  def startrecording(self, event):
      self.isrecording = True
      t = threading.Thread(target=self._record)
      t.start()


  def stoprecording(self, event):
      self.isrecording = False        
      

      
  def _record(self):
      while self.isrecording:
        data = ""
        r=sr.Recognizer()
        def speak(data):
            tts = gTTS(text=data, lang='en')
            tts.save('audio.mp3') 

        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            data = r.recognize_google(audio)
            Monitor.write(data)
            speak(data)

        except sr.UnknownValueError:
            raise SystemExit

        except sr.RequestError as e:
            Monitor.write('Please check your connection and restart Ronaldo')
            speak('Please check your connection and restart Ronaldo')         
                  

        if "how are you" in data:
            speak("I am fine")
            Monitor.write("I am fine")

     
        elif "what" and "time" in data:
            speak(asctime())
            Monitor.write(asctime())
            
        elif "what" and "your" and "name" in data:
            speak("my name is Cristiano Ronaldo, and I am better than Messi")
            Monitor.write("my name is Cristiano Ronaldo, and I am better than Messi")

        elif "hello" in data:
            speak("Hello there.")
            Monitor.write("Hello there")

        elif "madarchod" in data:
            speak("Gaali mut they maaderchod")
            Monitor.write("Gaali mat day madarchod")    

        elif "where is" in data:
            where = data.split('is',1)
            location = where[1]
            speak("Hold on. Opening "+location+" on Google Maps")
            Monitor.write("Hold on. Opening "+location+" on Google Maps")
            time.sleep(1)
            wb.open("https://www.google.com/maps/place/" + location + "/&amp")

        elif "Facebook" in data:
            speak('Opening Facebook')
            Monitor.write('Opening Facebook')
            wb.open("https://www.facebook.com")

        elif "quit " in data:
            os.system("say Okay. Bye!")
            Monitor.write('Okay. Bye!')
            os.remove('audio.mp3') #remove temperory file
            time.sleep(2)
            raise gah.destroy()

        elif "call me" in data:
            username = data.split('me',1)
            uname = username[1]
            speak("okay "+uname+", but I don't care what your name is")
            Monitor.write("okay "+uname+", but I don't care what your name is")


        elif "off Wi-Fi" in data:
            os.system("say Turning Wi-Fi off. Remember, I cannot work without an internet connection. Bye.")
            Monitor.write('Turning Wi-Fi off. Remember, I cannot work without an internet connection. Bye.')
            os.system("networksetup -setairportpower airport off")
            WiFiNotif = """
            osascript -e 'display notification "WiFi turned off" with title "Ronaldo"'
            """
            os.sytem(WifiNotif)
            raise SystemExit

        elif "off WiFi" in data:
            os.system("say Turning Wi-Fi off. Remember, I cannot work without an internet connection. Bye.")
            Monitor.write('Turning Wi-Fi off. Remember, I cannot work without an internet connection. Bye.')
            os.system("networksetup -setairportpower airport off")
            WiFiNotif = """
            osascript -e 'display notification "WiFi turned off" with title "Ronaldo"'
            """
            os.sytem(WifiNotif)
            raise SystemExit

        elif "temperature in" in data:
            WeatherPlace = data.split('in',1)
            Place = WeatherPlace[1]
            observation = owm.weather_at_place(Place)
            w = observation.get_weather()
            temperature = w.get_temperature('kelvin')
            CurrentTemp = str(round(temperature['temp']-273,1))
            Monitor.write("It is currently "+CurrentTemp+" degress celcius in"+Place)
            speak("It is currently "+CurrentTemp+" degrees celcius in "+Place)

        elif "sleep" in data:
            os.system('say goodnight homie')
            Monitor.write("Goodnight homie")
            os.system('pmset sleepnow') 

        elif "soja" in data:
            os.system('say goodnight homie')
            Monitor.write("Goodnight homie")
            os.system('pmset sleepnow')

        elif "so ja" in data:
            os.system('say goodnight homie')
            Monitor.write("Goodnight homie")
            os.system('pmset sleepnow')    

        elif "meaning of" in data:
            DicWord = data.split('of',1)
            Word = DicWord[1]
            WordDef = str(dictionary.meaning(Word))
            Def = (WordDef)[:-1]
            Monitor.write(Word+" is a: "+Def)
            speak(Word+" is a: "+Def)

        elif "open" in data:
            App = data.split('open',1)
            AppName = App[1]
            os.system('open -a '+AppName)
            speak('opening '+AppName)
            Monitor.write('opening '+AppName)

        elif "close" in data:
            Monitor.write('Quitting application')
            speak('Quitting application')
            quitCmd = """
            osascript -e 'tell application "System Events" to keystroke "q" using {command down}' 
            """
            os.system(quitCmd)

        elif " mute " in data:
            Monitor.write('Muting')
            speak('Muting')
            MuteCmd = """
            osascript -e 'set volume with output muted'
            """
            os.system(MuteCmd)
            MuteNotif = """
            osascript -e 'display notification "Computer Muted" with title "Ronaldo"'
            """
            os.system(MuteNotif)
            
        elif "unmute" in data:
            Monitor.write('Unmuting')
            speak('Unmuting')
            UnmuteCmd = """
            osascript -e 'set volume without output muted'
            """
            os.system(UnmuteCmd)
            UnmuteNotif = """
            osascript -e 'display notification "Computer Unmuted" with title "Ronaldo"'
            """
            os.system(UnmuteNotif)

        elif "first" and "YouTube" in data:
            cwap = data.split('for',1)
            KeyWord = cwap[1]
            Monitor.write('Here is the first youtube result for '+KeyWord)
            speak('Here is the first youtube result for '+KeyWord)
            query_string = urllib.parse.urlencode({"search_query" : KeyWord})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            wb.open("http://www.youtube.com/watch?v=" + search_results[0])

        elif "pollution in" in data:
            Loc = data.split('in',1)
            AirLoc = Loc[1]
            ##############
        
        else:
            speak('sorry, I have not been programmed to answer this yet.')

        
        
        music = pyglet.media.load('audio.mp3', streaming=False)
        music.play()

        #prevent from killing
        time.sleep(music.duration)
        os.remove('audio.mp3') #remove temperory file
      

              
 
app = App(gah)
gah.mainloop()
if __name__ == "ronaldo":
    Ronaldo("Ronaldo").run()
  ##############################################################################################################################




##################################################################################################################################


     # Record Audio
 


