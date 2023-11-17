import subprocess
import pdb #debugger

#simple call to run bash script created through get_create_script()
#first list arg: file extension
#2nd list arg: path and file name to run script


def run(run_path):
    subprocess.call(['sh',f'./{run_path}'])
    #any error catching??