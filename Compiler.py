from flask import Flask, render_template, jsonify, request

import os
import subprocess
from subprocess import Popen, PIPE, STDOUT, check_call
import random  
import string  

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('ide.html')

@application.route('/Compiler', methods=['GET', 'POST'])
def Compiler():
    code = ''
    language = ''

    if request.method :
        language = request.form.get("languages")
        code = request.form['content']
    # data=[{'name':'c'}, {'name':'cpp'}, {'name':'py'}, {'name':'php'}, {'name':'js'}]
    # code = request.form['code']
    # language = request.form["language"]

    filename = ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6)) 
    filepath = 'temp\\'+filename + '.' + language
    writefile(filepath, code)

    if language == 'c' :
        return render_template('ide.html', result = execute_c(filepath))
    
    if language == 'py':
        return render_template('ide.html', result = execute_py(filepath))

    if language == 'js':
        return render_template('ide.html', result = execute_js(filepath))
    # subprocess.call(["C:\\MinGW\\bin\\gcc", filepath])
    # output = subprocess.call("temp\\./a.out")
    # output = subprocess.check_call("C:\\MinGW\\bin\\gcc HelloWorld.c -o out1;./out1", shell = True)
    

    # if code and language:
    #     code = language + '  ' + code
    #     return render_template('ide.html', result = code)
    #     # return render_template('outpot.html')

    # return error

def writefile(filepath, code):
    file = open(filepath, 'w')
    file.write(code)
    file.close()

def execute_c(filepath):
    # subprocess.call(["C:\\MinGW\\bin\\gcc", filepath])
    # output = subprocess.call("temp\\./a.out")
    cmd = "gcc " +filepath +" -o out1;temp\\./out1"
    output = subprocess.run(cmd, shell=True, capture_output=True, text= True)
    return output

def execute_py(filepath):
    cmd = "python " + filepath
    output = subprocess.run(cmd, shell=True, capture_output=True, text= True)
    return output.stdout

def execute_js(filepath):
    cmd = "node " + filepath
    output = subprocess.run(cmd, shell=True, capture_output=True, text= True)
    return output.stdout


if __name__ == '__main__':
    application.run(debug=True)