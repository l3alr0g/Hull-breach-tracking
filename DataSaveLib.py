from panda3d.core import *

class DataSet:
    def __init__(self):
        self.time = float(0.0)
        self.RawData = [] # stores the geomNodes for each frame
        self.RawPos = [] # stores Raw positional data
        self.LoadedData = []
        return None
    
    def store(self, Node, PosList):
        self.RawData.append(Node)
        self.RawPos.append(PosList)
        return None
    
    def insert(self,Node,index):
        return None
    
    def unwrap(self, wireframe: bool = True):
        '''
        transfers the stored GeomNodes to the scene and hides them immediately
        '''
        for x in self.RawData:
            foo = render.attachNewNode(x)
            if wireframe:
                foo.setRenderModeWireframe()
            foo.hide()
            self.LoadedData.append(foo)
        return None
    
    def getFrameData(self, index): 
        try:
            return self.LoadedData[index - 1]
        except IndexError:
            print("Index Error encountered in DataSaveLib") # will be displayed in the console when I'll add it 
            pass
    
    def getFramePosData(self, index):
        try:
            return self.RawPos[index - 1]
        except IndexError:
            print("Index Error encountered in DataSaveLib")
