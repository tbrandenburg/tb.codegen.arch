import os
import json

import logging

import sys
sys.path.insert(0,'./arch_gen')

from FileVisitor import *

from ArchGen import *

class FileVisitorArchJSON(FileVisitor):

    _fileName = "arch.json"
    _archGen  = None
    
    def __init__(self, fileName, types):
        self._fileName = fileName
        self._archGen  = ArchGen(types)

    def visit(self,isDir,relFilePath,absFilePath,fileName) -> dict:
        if fileName == self._fileName:
            with open(absFilePath, 'r') as f:
                data = json.load(f)
            logging.info("Loaded architectural model of " + absFilePath)
            self._archGen.load_arch(data)
            logging.info("Generating into " + os.path.dirname(absFilePath) + "...")
            self._archGen.generate(os.path.dirname(absFilePath))
        return dict()