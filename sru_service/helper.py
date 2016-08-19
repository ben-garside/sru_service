import subprocess
import json
import logging

log = logging.getLogger(__name__)

def run(cmd, errMsg=None):
    """ run given commands in a subprocess
    """
    try:
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()
        if type(output) == bytes:
            output = output.decode(encoding='UTF-8')
        log.debug("Output: {}".format(output))
        log.debug("Return Code: {}".format(proc.returncode))
        if "[Error]" in output or proc.returncode != 0:
            log.debug("errMsg: {}".format(errMsg))
            log.debug("err: {}".format(err))
            if errMsg:
                return errMsg
            else:
                return "%s\r\n%s" % (output, err.decode("utf-8"))
        return output
    except Exception as e:
        log.error("Exception running 'run': {}".format(e))
        return None

def ask(message=None, default=None, required=True):
    if message:
        if default:
            var = input("{}: (default:{}) ".format(message, default))
            if not var:
                var = default
        else:
            var = input("{}: ".format(message))
            if required:
                if not var:
                    print("This value is required, please try again.")
                    ask(message, required)
    return var
