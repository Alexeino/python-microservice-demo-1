from flask import Flask, render_template
import json
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello user</p>"

def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return hostname, host_ip

@app.route("/health")
def health():
    
    response = json.dumps({
        "status":"OK"
    })
    print("Response type - ", type(response))

    return response

@app.route("/details")
def details():
    hostname,host_ip = fetchDetails()
    return render_template('index.html',hostname = hostname,host_ip = host_ip )

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)