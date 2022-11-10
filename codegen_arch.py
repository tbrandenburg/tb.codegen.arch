import os
import sys
import argparse
import pprint

import logging

import sys
sys.path.insert(0,'./visitor')
sys.path.insert(0,'./external/file/')
sys.path.insert(0,'./external/file/visitor')
sys.path.insert(0,'./external/file/filter')
sys.path.insert(0,'./types')

from FileTree import *
from FileFilterDir import *
from FileFilterFile import *
from FileVisitorPrintFilepaths import *
from FileVisitorPrintFileCount import *
from FileVisitorArchJSON import *

from SWComponent import *

def main():
    
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] [%(module)s] %(message)s',
                        datefmt='%y-%m-%d %H:%M:%S')

    parser = argparse.ArgumentParser(description='Architecture Code Generator')
    parser.add_argument("--path", "-p", help="Root path (relative)", type=str, default=".")
  
    args = parser.parse_args()

    archGenTypes = {
        "SWComponent":SWComponent()
    }

    files = FileTree(args.path,[FileFilterDir([".*"]),
                                FileFilterFile(["arch.json"])],
                               [FileVisitorArchJSON("arch.json",archGenTypes)])

    logging.info("Finished!")

    return 0

if __name__ == '__main__':
    sys.exit(main())

