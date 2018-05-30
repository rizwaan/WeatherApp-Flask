from flask import Flask, render_template
import os
import time
import json
import urllib3 as ul

app=Flask(__name__)

def getweather():
    url='http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=9cfbfabd348d2fc63c3073e92a178160&cnt=7'
    http = ul.PoolManager()
    response=http.request("GET",url)
    r=json.loads(response.data.decode('utf-8'))

    return  r


@app.route("/")
def index():
    data=getweather()
    temp=data['coord']["lon"]
    return render_template("index.html",temp=temp)


if __name__=='__main__':

    app.run(debug=True)