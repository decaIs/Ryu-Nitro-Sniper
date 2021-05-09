from flask import Flask
from threading import Thread

app=Flask("")

@app.route("/")
def index():
    return "<p>Thanks for using my App ily <3 ;w; - <strong>Topia</strong></p>"

Thread(target=app.run,args=("0.0.0.0",8080)).start()
