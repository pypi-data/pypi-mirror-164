import colorama
from colorama import Fore
import subprocess
colorama.init()

hwid = hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())

def find():
    print(Fore.RED+"Your HWID is: "+hwid)