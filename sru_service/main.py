# get path to template
# get content and apply variables
# write it to sru.xml
# execure the run command to the exe file with install param
# ...\sru.exe install
import os

from .settings import ROOT
from .helper import ask, run

xml_template = os.path.join(ROOT, "service", "template.xml")
xml_file = os.path.join(ROOT, "service", "sru.xml")
service_file = os.path.join(ROOT, "service", "sru.exe")
args_file = os.path.join(ROOT, "service", "args.txt")

def setup():
    HOST = ask("enter Hostname", default="localhost")
    PORT = ask("enter Port", default="30080")
    SSL = ask("would you like to use ssl? (y/n)", required=True)

    SSL_CERT = None
    SSL_KEY = None

    if SSL == "y":
        SSL_CERT = ask("enter certificate absolute path", required=True)
        SSL_KEY = ask("enter key absolute path", required=True)
    
    ID = ask("enter service ID", default="sru")
    NAME = ask("enter service NAME", default="SRU")
    DESC = ask("enter service Description", default="SRU Automator")
    EXE = ask("enter python path", default="python")
    LOGMODE = ask("enter service Logmode", default="rotate")

    setArgs(host=HOST, port=PORT, ssl_cert=SSL_CERT, ssl_key=SSL_KEY)
    args = getArgs()

    setupService(id=ID, name=NAME, desc=DESC, exe=EXE, logmode=LOGMODE)
    _install = install()
    if _install:
        print(_install)


def setupService(id, name, desc="", exe="python", logmode=""):
    with open(xml_template, "r", encoding="utf-8") as f:
        template = f.read()
        arg = getArgs()
        new_template = template.format(id, name, desc, exe, arg, logmode)
        with open(xml_file, "w+") as fr:
            fr.write(new_template)

def setArgs(host="localhost", port="30080", ssl_cert=None, ssl_key=None):
    with open(args_file, "w+", encoding="utf-8") as f:
        args = "-m sru.cli --host {} --port {} --cert {} --key {}".format(host, port, ssl_cert, ssl_key)
        f.write(args)

def getArgs():
    with open(args_file, "r", encoding="utf-8") as f:
        args = f.read()
        return args

def install():
    cmd = "{} install".format(service_file)
    result = run(cmd)
    return result

def uninstall():
    cmd = "{} uninstall".format(service_file)
    result = run(cmd)
    return result

def start():
    cmd = "{} start".format(service_file)
    result = run(cmd)
    return result

def stop():
    cmd = "{} stop".format(service_file)
    result = run(cmd)
    return result
    
    
