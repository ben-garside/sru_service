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

def setup(id, name, desc="", exe="python", arg="", logmode=""):
    with open(xml_template, "r", encoding="utf-8") as f:
        template = f.read()
        new_template = template.format(id, name, desc, exe, arg, logmode)
        with open(xml_file, "w+") as fr:
            fr.write(new_template)

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
    
    
