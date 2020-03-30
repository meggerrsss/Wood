#----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# AmecFW__SkyBlend_Tool
#
# Author: Dr. Diar Hassan
# May 9, 2017
# Modified: Jason Burks Aug 19, 2017 Made it fault tolerant.
# Modified: Dr. Diar Hassan Feb 20, 2018 Added NAM32.
# Modified: Dr. Diar Hassan Feb 27, 2018 Re-scalled RDPS& GDPS for lower and higher
# cloud ranges.
# Modified: Dr. Diar Hassan Apr 03, 2018 More cloud tweeks (Re-scalled RDPS& GDPS for lower and higher cloud ranges.)
# 
# This tool will blend differnt % of the available models, including your
# current Forecast and Official, that are set by the forecaster (% adds up to 100%).
# ----------------------------------------------------------------------------

ToolType = "numeric"
WeatherElementEdited = "Sky"

import numpy as np
import SmartScript



VariableList = [
    ("Official Sky %", 0, "scale",[0,100],5),
    ("Fcst Sky %", 0, "scale",[0,100],5),
    ("RDPS Sky %", 0, "scale",[0,100],5),
    ("RDPS Run:", "Latest", "radio", ["Latest", "Previous"]),
   # ("HRDPS Sky %", 0, "scale",[0,100],5),
    #("HRDPS Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("GDPS Sky %", 0,"scale",[0,100],5),
    ("GDPS Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("NAM12 Sky %", 0,"scale",[0,100],5),
    ("NAM12 Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("NAM32 Sky %", 0,"scale",[0,100],5),
    ("NAM32 Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("GFS25 Sky %", 0,"scale",[0,100],5),
    ("GFS25 Run:", "Latest", "radio", ["Latest", "Previous"]),
##    ("NAM32 Sky %", 0,"scale",[0,100],5),
##    ("NAM32 Run:", "Latest", "radio", ["Latest", "Previous", "2 Runs ago"]),
   # ("",800,"scrollbar"),
    ]


class Tool (SmartScript.SmartScript):
    def __init__(self, dbss):
        SmartScript.SmartScript.__init__(self, dbss)


    def execute(self, Sky, GridTimeRange, varDict):
        
        SITE=self.getSiteID()

        percentOfficial=varDict["Official Sky %"]
        percentFcst=varDict["Fcst Sky %"]
        percentRDPS=varDict["RDPS Sky %"]
        #percentHRDPS=varDict["HRDPS Sky %"]
        percentHRDPS=0
        percentGDPS=varDict["GDPS Sky %"]
        percentNAM12=varDict["NAM12 Sky %"]
        percentNAM32=varDict["NAM32 Sky %"]
        percentGFS25=varDict["GFS25 Sky %"]
        
        modelrunRDPS=varDict["RDPS Run:"]
        #modelrunHRDPS=varDict["RDPS Run:"]
        modelrunHRDPS = None
        modelrunGDPS=varDict["GDPS Run:"]
        modelrunNAM12=varDict["NAM12 Run:"]
        modelrunGFS25=varDict["GFS25 Run:"]
        modelrunNAM32=varDict["NAM32 Run:"]
        
        modelSkyRDPS = None
        modelSkyHRDPS = None
        modelSkyGDPS = None
        modelSkyNAM12 = None
        modelSkyGFS25 = None
        modelSkyNAM32 = None
        # for the model runs
        if modelrunRDPS=="Latest":
            modelSkyRDPS=self.findDatabase("RDPS", 0)
        elif modelrunRDPS=="Previous":
            modelSkyRDPS=self.findDatabase("RDPS", -1)
        else:
            modelSkyRDPS=self.findDatabase("RDPS", -2)

        if modelrunHRDPS=="Latest":
            modelSkyHRDPS=self.findDatabase("HRDPS-WEST", 0)
        elif modelrunHRDPS=="Previous":
            modelSkyHRDPS=self.findDatabase("HRDPS-WEST", -1)
        else:
            modelSkyHRDPS=self.findDatabase("HRDPS-WEST", -2)

        if modelrunGDPS=="Latest":
            modelSkyGDPS=self.findDatabase("GDPS", 0)
        elif modelrunGDPS=="Previous":
            modelSkyGDPS=self.findDatabase("GDPS", -1)
        else:
            modelSkyGDPS=self.findDatabase("GDPS", -2)

        if modelrunNAM12=="Latest":
            modelSkyNAM12=self.findDatabase("NAM12", 0)
        elif modelrunNAM12=="Previous":
            modelSkyNAM12=self.findDatabase("NAM12", -1)
        else:
            modelSkyNAM12=self.findDatabase("NAM12", -2)

        if modelrunNAM32=="Latest":
            modelSkyNAM32=self.findDatabase("NAM32", 0)
        elif modelrunNAM32=="Previous":
            modelSkyNAM32=self.findDatabase("NAM32", -1)
        else:
            modelSkyNAM32=self.findDatabase("NAM32", -2)

        if modelrunGFS25=="Latest":
            modelSkyGFS25=self.findDatabase("GFS25", 0)
        elif modelrunGFS25=="Previous":
            modelSkyGFS25=self.findDatabase("GFS25", -1)
        else:
            modelSkyGFS25=self.findDatabase("GFS25", -2)

        SkyOfficial = None
        SkyFcst = None
        SkyRDPS = None
        SkyHRDPS = None
        QPFRDPS = None
        SkyGDPS = None
        QPFGDPS = None
        SkyNAM12 = None
        SkyGFS25 = None
        SkyNAM32 = None
            
        #Grab Sky from the models....add models as you go
        if (percentOfficial >0):
            try:
                SkyOfficial=self.getGrids("Official", "Sky", "SFC",  GridTimeRange)
            except:
                pass
        if (percentFcst > 0):
            try:
                SkyFcst=self.getGrids("Fcst", "Sky", "SFC",  GridTimeRange)
            except:
                pass
        if (percentRDPS >0):
            try:
                SkyRDPS=self.getGrids(modelSkyRDPS, "Sky", "SFC", GridTimeRange)
                QPFRDPS=self.getGrids(modelSkyRDPS, "QPF", "SFC", GridTimeRange)
            except:
                pass
        if (percentHRDPS >0):
            try:
                SkyHRDPS=self.getGrids(modelSkyHRDPS, "Sky", "SFC", GridTimeRange)
                QPFHRDPS=self.getGrids(modelSkyHRDPS, "QPF", "SFC", GridTimeRange)
            except:
                pass
        if (percentGDPS >0):
            try:
                SkyGDPS=self.getGrids(modelSkyGDPS, "Sky", "SFC", GridTimeRange)
                QPFGDPS=self.getGrids(modelSkyGDPS, "QPF", "SFC", GridTimeRange)
            except:
                pass
        if (percentNAM12 >0):
            try:
                SkyNAM12=self.getGrids(modelSkyNAM12, "Sky", "SFC", GridTimeRange)
            except:
                pass
        if (percentNAM32 >0):
            try:
                SkyNAM32=self.getGrids(modelSkyNAM32, "Sky", "SFC", GridTimeRange)
            except:
                pass
        if (percentGFS25 >0):
            try:
                SkyGFS25=self.getGrids(modelSkyGFS25, "Sky", "SFC", GridTimeRange)
            except:
                pass
                
        totalPercent = 0   
        scale = np.zeros(np.shape(Sky))
        
        if (SkyOfficial != None):
            totalPercent = totalPercent+percentOfficial
        if (SkyFcst != None):
            totalPercent = totalPercent+percentFcst
        if (SkyRDPS != None):
            totalPercent = totalPercent+percentRDPS
        if (SkyHRDPS != None):
            totalPercent = totalPercent+percentHRDPS
        if (SkyGDPS != None):
            totalPercent = totalPercent+percentGDPS
        if (SkyNAM12 != None):
            totalPercent = totalPercent+percentNAM12
        if (SkyGFS25 != None):
            totalPercent = totalPercent+percentGFS25
        if (SkyNAM32 != None):
            totalPercent = totalPercent+percentNAM32

        print("Total Precent: "+str(totalPercent))
        if (SkyOfficial != None):
            scale = scale + (percentOfficial/totalPercent)*SkyOfficial
        if (SkyFcst != None):
            scale = scale + (percentFcst/totalPercent)*SkyFcst
        if (SkyRDPS != None):
            scale = scale + (percentRDPS/totalPercent)*SkyRDPS
        if (SkyHRDPS != None):
            scale = scale + (percentHRDPS/totalPercent)*SkyHRDPS
        if (SkyGDPS != None):
            scale = scale + (percentGDPS/totalPercent)*SkyGDPS
        if (SkyNAM12 != None):
            scale = scale + (percentNAM12/totalPercent)*SkyNAM12
        if (SkyGFS25 != None):
            scale= scale +(percentGFS25/totalPercent)*SkyGFS25
        if (SkyNAM32 != None):
            scale = scale + (percentNAM32/totalPercent)*SkyNAM32
            
    
        return scale
