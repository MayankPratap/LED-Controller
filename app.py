from flask import Flask,render_template,request
from gpiozero import LED
from time import sleep

led=LED(17)

app=Flask(__name__)

@app.route('/')
           
def index():
    return render_template('index.html')

@app.route('/',methods=["POST"])

def getData():
    print("Hello")
    if request.method=="POST":
        print("Method is post, Hello")
        if request.headers['Content-Type']=='text/plain':
        
            data=request.data
            print(data)    
            if data==b'on':
                led.on()
            elif data==b'off':
                led.off()

    return render_template('index.html')    
                 

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')


