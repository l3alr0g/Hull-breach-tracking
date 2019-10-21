import sys
try:
    from panda3d.core import *
    from direct.showbase.ShowBase import ShowBase
    from direct.task import Task
    from ParticleField import *
except:
    print('failed to load modules')
    sys.exit()

class mainApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.ParticleSystem = ParticleMesh(50,50,None)
        self.task_mgr.add(self.MainLoop,'ScreenUpdatingTask')
        return None
    def MainLoop(self,task):
        self.ParticleSystem.update()
        return None

Simulation = mainApp()
Simulation.run()