from flask import Flask,request,render_template

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
        result = a+b
    elif(operation=="sub"):
        result = a-b
    elif(operation=="mul"):
        result = a*b
    else:
        result = a/b
    return result 
    






if __name__ == '__main__':
    app.run(debug=True)







