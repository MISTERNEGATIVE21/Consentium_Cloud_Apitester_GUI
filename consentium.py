from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from ConsentiumThingsPy import ThingsUpdate
import time
import requests
class InsertWindow(Screen):
    api_key = ObjectProperty(None)
    sensor1 = ObjectProperty(None)
    sensor2 = ObjectProperty(None)
    sensor3 = ObjectProperty(None)
    sensor4 = ObjectProperty(None)
    sensor5 = ObjectProperty(None)
    sensor6 = ObjectProperty(None)
    sensor7 = ObjectProperty(None)

    def insert(self):
  
          sensor_val1 = self.sensor1.text
          sensor_val2 = self.sensor2.text
          sensor_val3 = self.sensor3.text
          sensor_val4 = self.sensor4.text
          sensor_val5 = self.sensor5.text
          sensor_val6 = self.sensor6.text
          sensor_val7 = self.sensor7.text

          api_key_val=str(self.api_key.text)
          board = ThingsUpdate(key=api_key_val)

          sensor_val = [sensor_val1, sensor_val2, sensor_val3, sensor_val4, sensor_val5, sensor_val6, sensor_val7]
          info_buff = ["a", "b", "c", "d", "e", "f", "g"]
          r = board.sendREST(sensor_val=sensor_val, info_buff=info_buff)
          print(r)
          time.sleep(5)
    def clearbtn(self):
        sm.current = "clearentries"


class ClearWindow(Screen):
    
    api_key = ObjectProperty(None)  

    def Cleardata(self):                                # for clearing data
      URL = "http://consentiuminc.online:80/clear?send_key="
  
      api_key_val=self.api_key.txt
# defining a params dict for the parameters to be sent to the API
      PARAMS = {'address':api_key_val}
      
# sending get request and saving the response as response object
      r = requests.get(url = URL, params = PARAMS)
      print (r)
  
# extracting data in json format
      data = r.json()  
      pop = Popup(title='success inside',
                  content=Label(text=r),
                  size_hint=(None, None), size=(400, 400))

      pop.open() 
    
    def InsertBtn(self):
        sm.current = "insert"

    def Clearbtn(self):
        sm.current = "clearentries"

class MainWindow(Screen):
    api_key = ObjectProperty(None)  



    def on_enter(self, *args):
       pop = Popup(title='success inside',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

       pop.open() 


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("Consentium.kv")

sm = WindowManager()

screens = [ClearWindow(name="clearentries"), InsertWindow(name="insert"),MainWindow(name="main")]  #check this 
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class ConsentiumApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    ConsentiumApp().run()
