# get path to template
# get content and apply variables
# write it to sru.xml
# execure the run command to the exe file with install param
# ...\sru.exe install
import os
from sru_utils.helper import run
from .settings import ROOT

xml_template = os.path.join(ROOT, "service", "template.xml")
xml_file = os.path.join(ROOT, "service", "sru.xml")
service_file = os.path.join(ROOT, "service", "sru.exe")
args_file = os.path.join(ROOT, "service", "args.txt")

def setup(id, name, desc="", exe="python", logmode=""):
    with open(xml_template, "r", encoding="utf-8") as f:
        template = f.read()
        arg = getArgs()
        new_template = template.format(id, name, desc, exe, arg, logmode)
        with open(xml_file, "w+") as fr:
            fr.write(new_template)

def setArgs(host="localhost", port="30080", ssl_cert=None, ssl_key=None, modules=None):
    with open(args_file, "w+", encoding="utf-8") as f:
        args = "-m sru.cli --host {} --port {} --cert {} --key {} --modules {}".format(host, port, ssl_cert, ssl_key, modules)
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
    
    
