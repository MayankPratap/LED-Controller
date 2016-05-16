from flask import Flask,render_template,request
from gpiozero import LED
from time import sleep

led=LED(17)

app=Flask(__name__)

@app.route('/')
           
def index():
    return render_template('index.html')

@app.route('/',methods=["GET","POST"])

def getData():
    if request.method=="POST":
        if request.headers['Content-Type']=='text/plain':
            data=request.data
            if data=="on":
                led.on()
            elif data=="off":
                led.off()

    return render_template('index.html')    
                 

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')


