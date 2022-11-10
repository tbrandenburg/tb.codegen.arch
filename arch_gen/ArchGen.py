import os

class ArchGen():

    _arch = dict()
    _types = dict()
    
    def __init__(self, types):
        self._types = types
        pass

    def set_types(self,types):
        self._types = types

    def load_arch(self,arch):
        self._arch = arch

    def _generate(self,path,arch):
        for item,values in arch.items():
            type = values.get("type")
            if type:
                genClassInstance = self._types.get(type)
                if genClassInstance:
                    genClassInstance.generate(path,item,values)
                    pass
            children = values.get("children")
            if children:
                self._generate(os.path.join(path,item), children)

    def generate(self,path):
        self._generate(path, self._arch)
        pass