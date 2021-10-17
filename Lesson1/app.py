from flask import Flask, jsonify

app = Flask(__name__)

# Once the server is up and running,
# waiting for request for / --> 127.0.0.1:5000/

@app.route('/') 
def hello_world():
    return "Hello World!"

@app.route('/hithere') # basically prepares a response 
def hi_there_everyone():
    return "I just hit /hithere"

@app.route('/bye')
def bye():
    c=2*534
    s=str(c)
    retJson={
        "Name": "Ahmet",
        "Age": 25,
        "phones":[
            {
                "phoneName":"Iphone13",
                "phoneNumber":"11111"
            },
            {
                "phoneName":"SamsungS21",
                "phoneNumber":"22222"
            }
        ]
    }
    return jsonify(retJson)

if __name__ == "__main__":
    app.run(debug=True)

# For web services we usually return JSON
# For web applications we return a page