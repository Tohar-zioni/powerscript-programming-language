import forpsk
from flask import Flask
app = Flask(__name__)
import keyboard
@app.route("/")
def home():
    return xhtml
xhtml = ""
def Lang(Syntax):
    State = 0
    key = ""
    name = ""
    Token = ""
    var = ""
    varname = ""
    String = ""
    inp = ""
    optype = "Number", "String" ,"Class" , "Char"
    something = ""
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
        elif Token == "if(" + name + "){ }":
            name = ""
            if name == "ps.usekey" + key:
                keyboard.is_pressed(key)
        elif Token == "class" + name + "{ }":
            pass
        elif Token == "function." + name + "{ }":
            name = ""
            if name == "all":
                pass
        elif Token == "std::input " + inp:
            inp = ""
            input(str(inp)) 
        elif Token == "web.run":
            if __name__ == "__main__":
                app.run()
        elif Token == "web.channel " + xhtml:
            pass
            inp = ""
            input(str())
        elif Token == "loop[" + forpsk.name + " in" + forpsk.func + "] ==>{ }":
            forpsk.xfor() 
        elif Token == "||" + something:
            something = ""
            pass
    print(String)
Content = open("main.psk", "r").readlines()
for Line in Content:
    Lang(Line)
