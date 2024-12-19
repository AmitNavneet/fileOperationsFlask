from flask import Flask,render_template
from flask import request
import os
app=Flask(__name__)


def getFormData():
    return request.args['nameFile']


def createFile(nameFile):
    
    LocalpathFile=f"extraFileProg/{nameFile}.txt"
       
    try:
        myFile=open(LocalpathFile,"x")
    except Exception as e:
        return str(e)
    
    return "File created successfully"

def writeFile():    
    myFile=open(pathFile,"w")
    data=request.args['dataFile']
    myFile.write(data)
    return f"Text Data:{data}<br>File written successfully"

def readFile():
    try:
        myFile=open(pathFile,"r")
    except Exception as e:
        return str(e)
    dataTextArea=myFile.read()
    print(dataTextArea)
    return render_template('index.html',dataTextArea=dataTextArea)
    
#readFile

def deleteFile():
    if os.path.exists(pathFile):
        os.remove(pathFile)
        return f"<h1>{pathFile} deleted</h1>"
    else:
        return f"<h1>{pathFile} does not exist</h1>"

def appendFile():
    if not os.path.exists(pathFile):
        return f"{pathFile} does not exist"
    try:
        myFile=open(pathFile,'a')
    except Exception as e:
        return str(e)
    data=request.args['dataFile']
    print(myFile.write(data))
    data=f"{data}<br> Append operation done, file:{pathFile}"
    return data

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fileOperation')
def fileOperation():
    global pathFile #must
    
    pathFile=f"extraFileProg/{getFormData()}.txt"
    fileOp=request.args['fileOp']
    if fileOp=='createFile':
        return createFile(getFormData())
    elif fileOp=='writeFile':
        return writeFile()
    elif fileOp=='readFile':
        return readFile()
    elif fileOp=='deleteFile':
        return deleteFile()
    elif fileOp=='appendFile':
        return appendFile()
    return fileOp

if __name__=='__main__':
    app.run(debug=True)