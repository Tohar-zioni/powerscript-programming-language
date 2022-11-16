import keyboard
import web
import appcreator
def Lang(Syntax):
    State = 0
    key = ""
    name = ""
    Token = ""
    String = ""
    inp = ""
    for Char in Syntax:
        Token += Char
        if Token == " ":
            if State == 0:
                Token = ""
 
        elif Token == "\n":
            Token = ""
 
        elif Token == "std::trace":
            Token = ""
 
        elif Token == "\"":
            if State == 0:
                State = 1
                Token = ""
 
            elif State == 1:
                State = 0
 
        elif State == 1:
            String += Token
            Token = ""
        elif Token == "if" + name + "{ }":
            name = ""
            if name == "ps.usekey" + key:
                keyboard.is_pressed(key)
        elif Token == "class" + name + "{ }":
            pass
        elif Token == "function." + name + "{ }":
            name = ""
            if name == "web":
                web()
            elif name == "app":
                appcreator()
            elif name == "normal":
                pass
        elif Token == "std::input ":
            inp = ""
            input(str())
    print(String)
    

Content = open("main.psk", "r").readlines()
for Line in Content:
    Lang(Line)