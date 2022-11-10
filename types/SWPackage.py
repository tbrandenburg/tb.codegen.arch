import os
import logging

import sys
sys.path.insert(0,'./arch_gen')

from ArchGenType import *

class SWPackage(ArchGenType):

    def generate(self,absRootPath,name,content):
        logging.info("Generating package " + name + "...")
        os.makedirs(os.path.join(absRootPath,name), exist_ok=True)
        pass