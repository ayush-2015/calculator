from flask import Flask,request,render_template,jsonify

import json

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to the home page"
@app.route('/calculator',methods=["get"])
def math_operation():
    operation=request.json["operation"]
    a=request.json["a"]
    b=request.json["b"]
    if(operation=="add"):
        result = int(a)+int(b)
    elif(operation=="sub"):
        result = int(a)-int(b)
    elif(operation=="mul"):
        result = int(a)*int(b)
    else:
        result = int(a)-int(b)
    return jsonify(result)
    






if __name__ == '__main__':
    app.run(debug=True)







