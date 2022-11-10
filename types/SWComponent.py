import os
import logging

import sys
sys.path.insert(0,'./arch_gen')

from ArchGenType import *

class SWComponent(ArchGenType):

    def generate(self,absRootPath,name,content):
        logging.info("Generating " + name + "...")
        os.makedirs(os.path.join(absRootPath,name), exist_ok=True)
        os.makedirs(os.path.join(absRootPath,name,"src"), exist_ok=True)
        os.makedirs(os.path.join(absRootPath,name,"api"), exist_ok=True)
        pass