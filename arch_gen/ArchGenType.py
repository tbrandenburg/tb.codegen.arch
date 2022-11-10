from abc import ABC, abstractmethod

class ArchGenType(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def generate(self,absRootPath,name,content):
        pass

    def isFolder(self) -> bool:
        return True