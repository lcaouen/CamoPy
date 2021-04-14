import threading
import sys
import os
import json
import glob
from bottle import route, run, template, static_file

class TaskWeb(threading.Thread):
    def __init__(self, config):
        threading.Thread.__init__(self)
        self.port = config["webService"]["port"]
        self.config = config

    def run(self):
        @route('/api/config/<pwd>', method="GET")
        def getConfig(pwd):
            if pwd==self.config["webService"]["pwd"]:
                return self.config
            return ""

        @route('/api/restart/<pwd>', method="GET")
        def restart(pwd):
            if pwd==self.config["webService"]["pwd"]:
                python = sys.executable
                os.execl(python, python, * sys.argv)
                return "done"
            return "no authorization"
        
        @route('/api/currentImage/<pwd>', method="GET")
        def currentImage(pwd):
            if pwd==self.config["webService"]["pwd"]:
                fileList = glob.glob(self.config["images"]["path"] + '*-img.jpg')
                fileName = max(fileList, key=os.path.getctime)
                return static_file(fileName.replace(self.config["images"]["path"], ""), root=self.config["images"]["path"])
            return "no authorization"
        
        @route('/', method="GET")
        def index():
            return template('index')

        @route('/static/<filepath:path>')
        def server_static(filepath):
            return static_file(filepath, root='views/static')

        run(host='0.0.0.0', port=self.port)
