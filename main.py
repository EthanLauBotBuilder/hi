import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
''''
class menu(GridLayout):
    def __init__(self, **kwargs):
        super(menu,self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text = "JAPEN TRAVELING APP"))
        self.rows = 2
        
        self.jpymopconvert = Button(text="JPY MOP CHANGER")
        self.jpymopconvert.bind(on_press=self.run1)
        self.add_widget(self.jpymopconvert)
    def run1(self,instance):
        return jpymopchanger()
'''
    
class jpymopchanger(GridLayout):
    def __init__(self, **kwargs):
        super(jpymopchanger,self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text = "JPY MOP CHANGER"))
        self.rows = 5
        self.n1 = TextInput(multiline=False)
        self.add_widget(self.n1)
        self.answer = Label(text="")
        self.add_widget(self.answer)
        self.jpytomop = Button(text="JPY to MOP")
        self.jpytomop.bind(on_press=self.jtomfunc)
        self.add_widget(self.jpytomop)
        self.mtoj = Button(text="MOP TO JPY")
        self.mtoj.bind(on_press=self.moptojpy)
        self.add_widget(self.mtoj)
    
    
        

    #jpytomop

    def jtomfunc(self,instance):
        def jtomexchangerate():
            import requests
            from bs4 import BeautifulSoup

            url = "https://wise.com/zh-hk/currency-converter/jpy-to-mop-rate"
            res = requests.get(url, headers={'referer': url})

            soup = BeautifulSoup(res.content, 'html.parser')

            text = soup.select_one("span.d-inline-block span").text
            return text
        try:
            n1value = int(self.n1.text)
            exchangerate = jtomexchangerate()
            self.answer.text = str(n1value*float(exchangerate))
            
        except Exception as error:
            print(error)
            
            
    #moptojpy
            

    def moptojpy(self,instance):
        def mtojexchangerate():
            import requests
            from bs4 import BeautifulSoup

            url = "https://wise.com/zh-cn/currency-converter/mop-to-jpy-rate"
            res = requests.get(url, headers={'referer': url})

            soup = BeautifulSoup(res.content, 'html.parser')

            text = soup.select_one("span.d-inline-block span").text
            return text
        try:
            n1value = int(self.n1.text)
            exchangerate = mtojexchangerate()
            self.answer.text = str(n1value*float(exchangerate))
            
        except Exception as error:
            print(error)
            
    
class Myapp(App):
    def build(self):
        return jpymopchanger()
if __name__ == '__main__':
    app = Myapp()
    app.run()
     
