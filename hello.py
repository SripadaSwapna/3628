from flask import Flask
app=Flask(__name__)
@app.route('/')
def firstapp():
    return "Hello World! Welcome"
if __name__=='__main__':
    app.run(debug=True)