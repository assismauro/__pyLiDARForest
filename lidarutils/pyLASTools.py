import os
import shutil
import subprocess
from sys import platform as _platform

class pyLASTools(object):
    """Implements a Python interface to LASTools command line tools"""

    def __init__(self,lastoolspath):
        self.lastoolspath = lastoolspath + ("" if lastoolspath.endswith(os.sep) else os.sep)

    def runcommand(self,command,commandonly,verbose):
        cmd="{0}{1}".format(self.lastoolspath,command)
        isamac = _platform == "darwin"
        if isamac:
            command="wine "+cmd
        else:
            command=cmd
        print command
        if commandonly:
            print(command)
            return None, 
        if verbose > 0:
            print command
        if isamac:
            p = subprocess.Popen(command,shell=True)
        else:
            p = subprocess.Popen(command,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        out, err = p.communicate()
        if ((out != None) and ("ERROR" in out)) or ((err != None) and ("ERROR" in err)):
            print "Error in command: {0} Message: {1}{2}".format(command,out,err)
            raise 
        if verbose > 0:
            print(out)
        return out, err

    def lasground(self,inputfname,outputfname,options="",commandonly=False,verbose=False):
        self.runcommand(r"lasground -i {0} -o {1} {2}".format(inputfname,outputfname,options),commandonly,verbose)
       
    def lasheight(self,inputfname,outputfname,options="",commandonly=False,verbose=False):
        self.runcommand(r"lasheight -i {0} -o {1} {2}".format(inputfname,outputfname,options),commandonly,verbose)
    
    def las2las(self,inputfname,outputfname,options="",commandonly=False,verbose=False):
        self.runcommand(r"las2las -i {0} -o {1} {2}".format(inputfname,outputfname,options),commandonly,verbose)

    def blast2dem(self,inputfname,outputfname,step=0.5,options="",commandonly=False,verbose=False):
        self.runcommand(r"blast2dem -i {0} -o {1} -step {2} {3}".format(inputfname,outputfname,step,options),commandonly,verbose)

    def lastile(self,inputfname,outputfname,options="",commandonly=False,verbose=False):
        self.runcommand(r"lastile -i {0} {1} {2}".format(\
            inputfname,"-o "+outputfname if outputfname != "" else "",options),commandonly,verbose)

    def lasthin(self,inputfname,outputfname,options,commandonly=False,verbose=False):
        self.runcommand(r"lasthin -i {0} {1} {2}".format(\
            inputfname,"-o "+outputfname if outputfname != "" else "",options),commandonly,verbose)

    def lasmerge(self,inputfname,outputfname,options,commandonly=False,verbose=False):
        self.runcommand(r"lasmerge -i {0} -o {1} {2}".format(\
            inputfname,outputfname,options),commandonly,verbose)

    def lasgrid(self,inputfname,outputfname,step=0.5,options="",commandonly=False,verbose=False):
        self.runcommand(r"lasgrid -i {0} -step {1} -average -o {2} -mem 1900".format(inputfname,step,outputfname),commandonly,verbose)

    def lascanopy(self,inputfname,outputfname,step=0.5,options="",
                  commandonly=False,verbose=False):
        self.runcommand(r"lascanopy -i {0} -o {1} -step {2} {3}".format(inputfname,outputfname,step,options),commandonly,verbose)

    
