#----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# Wood_WindMaxMin_Tool
#
# Author: Meghan Green
# Feb 2, 2022
# with inspiration from the MaxT tool
#
# This tool will output the max or min wind speeds from all models available in the domain
# ----------------------------------------------------------------------------


HideTool=0

ToolType = "numeric"
WeatherElementEdited = "Wind"
ScreenList=["VECTOR"]

import numpy as np
import SmartScript
import LogStream
import time

VariableList = [
    #("Yes", "Yes", "radio", ["Yes", "Yes", "Yes"]),
    ("Max or Min Model Wind:", "Max", "radio", ["Max", "Min"]),
    ("RDPS Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("HRDPS Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("GDPS Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("NAM Run:", "Latest", "radio", ["Latest", "Previous"]),
    ("GFS25 Run:", "Latest", "radio", ["Latest", "Previous"]),
    ]

class Tool (SmartScript.SmartScript):
    def __init__(self, dbss):
        SmartScript.SmartScript.__init__(self, dbss)

    def execute(self, Wind, GridTimeRange, varDict):
        SITE=self.getSiteID()
        tic = time.perf_counter()

        # input variables from forecaster running tool
        MaxorMin=varDict["Max or Min Model Wind:"]
        modelrunRDPS = varDict["RDPS Run:"]
        modelrunHRDPS = varDict["HRDPS Run:"]
        modelrunGDPS = varDict["GDPS Run:"]
        modelrunNAM = varDict["NAM Run:"]
        modelrunGFS25 = varDict["GFS25 Run:"]

        # initializing imports of database from each model
        modelWRDPS = None
        modelWHRDPS = None
        modelWGDPS = None
        modelWNAM12 = None
        modelWGFS25 = None
        modelWNAM32 = None
        
        # Assigning previous or latest model runs, prev to have the previous model on hand anyways for any gaps
        if modelrunRDPS == "Latest":
            modelWRDPS = self.findDatabase("RDPS", 0)
        elif modelrunRDPS == "Previous":
            modelWRDPS = self.findDatabase("RDPS", -1)
        modelWRDPSprev = self.findDatabase("RDPS", -1)
          
        if modelrunHRDPS == "Latest":
            modelWHRDPS = self.findDatabase("HRDPS", 0)
        elif modelrunHRDPS == "Previous":
            modelWHRDPS = self.findDatabase("HRDPS", -1)
        modelWHRDPSprev = self.findDatabase("HRDPS", -1)
        
        if modelrunGDPS=="Latest":
            modelWGDPS=self.findDatabase("GDPS", 0)
        elif modelrunGDPS=="Previous":
            modelWGDPS=self.findDatabase("GDPS", -1)
        modelWGDPSprev = self.findDatabase("GDPS", -1)
 
        if modelrunNAM=="Latest":
            modelWNAM32=self.findDatabase("NAM32", 0)
            modelWNAM12=self.findDatabase("NAM12", 0)
        elif modelrunNAM=="Previous":
            modelWNAM32=self.findDatabase("NAM32", -1)
            modelWNAM12=self.findDatabase("NAM12", -1)
        modelWNAM32prev=self.findDatabase("NAM32", -1)
        modelWNAM12prev=self.findDatabase("NAM12", -1)
       
        if modelrunGFS25=="Latest":
            modelWGFS25=self.findDatabase("GFS25", 0)
        elif modelrunGFS25=="Previous":
            modelWGFS25=self.findDatabase("GFS25", -1)
        modelWGFS25prev=self.findDatabase("GFS25", -1)

        # initializing imports of direct wind data from each model and forecast
        #WOfficial = None
        WFcst = None
        WRDPS = None
        WHRDPS = None
        WGDPS = None
        WNAM12 = None
        WGFS25 = None
        WNAM32 = None
        WNAM = None
        Temp = None
        
        # obtaining Model Data
        # model imports are using [0] in these lines to just take speed, 
        # Fcst is importing the full vector to hold onto direction
        try:
            WFcst=self.getGrids("Fcst", "Wind", "SFC",  GridTimeRange)
            #LogStream.logProblem("Fcst Wind",WFcst)
        except:
            pass
        try:
            WRDPS = self.getGrids(modelWRDPS, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        try:
            WHRDPS = self.getGrids(modelWHRDPS, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        try:
            WGDPS = self.getGrids(modelWGDPS, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        try:
            WNAM12 = self.getGrids(modelWNAM12, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        try:
            WGFS25 = self.getGrids(modelWGFS25, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        try:
            WNAM32 = self.getGrids(modelWNAM32, "Wind", "SFC", GridTimeRange)[0]
          
            # where NAM12 is empty, replace with NAM32
            WNAM = np.where(np.logical_and.reduce([np.equal(WNAM12, 0)]), WNAM32, WNAM12)
          
            #WNAM = WNAM32 # for when NAM12 is acting up, enable this and ignore NAM12
            #LogStream.logProblem(WNAM32, WNAM12, WNAM)
        except:
            pass

        # separating Fcst into speed and direction
        Temp=WFcst[0]
        dir=WFcst[1]
        #LogStream.logProblem(Temp)
        
        if MaxorMin == "Max":
            Temp = WGDPS
            if (WHRDPS == None and WRDPS != None and WGFS25 != None):
                Temp = np.where(np.logical_and.reduce([np.greater(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WGFS25, Temp)]), WGFS25, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WRDPS, Temp)]), WRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS != None and WRDPS != None and WGFS25 != None):
                Temp = np.where(np.logical_and.reduce([np.greater(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WGFS25, Temp)]), WGFS25, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WRDPS, Temp)]), WRDPS, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WHRDPS, Temp)]), WHRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WRDPS == None and WHRDPS == None and WGFS25 != None):
                Temp = np.where(np.logical_and.reduce([np.greater(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WGFS25, Temp)]), WGFS25, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS != None and WRDPS != None and WGFS25 == None):
                Temp = np.where(np.logical_and.reduce([np.greater(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WRDPS, Temp)]), WRDPS, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WHRDPS, Temp)]), WHRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS == None and WRDPS != None and WGFS25 == None):
                Temp = np.where(np.logical_and.reduce([np.greater(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WGFS25, Temp)]), WGFS25, Temp)
                Temp = np.where(np.logical_and.reduce([np.greater(WRDPS, Temp)]), WRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS == None and WRDPS == None and WGFS25 == None):
                Temp = np.where(np.logical_and.reduce([np.greater(WNAM, Temp)]), WNAM, Temp)
                #LogStream.logProblem(Temp)

        elif MaxorMin == "Min":
            Temp = WGDPS
            if (WHRDPS == None and WRDPS != None and WGFS25 != None):
                Temp = np.where(np.logical_and.reduce([np.less(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WGFS25, Temp)]), WGFS25, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WRDPS, Temp)]), WRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS != None and WRDPS != None and WGFS25 != None):
                Temp = np.where(np.logical_and.reduce([np.less(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WGFS25, Temp)]), WGFS25, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WRDPS, Temp)]), WRDPS, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WHRDPS, Temp)]), WHRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WRDPS == None and WHRDPS == None and WGFS25 != None):
                Temp = np.where(np.logical_and.reduce([np.less(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WGFS25, Temp)]), WGFS25, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS != None and WRDPS != None and WGFS25 == None):
                Temp = np.where(np.logical_and.reduce([np.less(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WRDPS, Temp)]), WRDPS, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WHRDPS, Temp)]), WHRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS == None and WRDPS != None and WGFS25 == None):
                Temp = np.where(np.logical_and.reduce([np.less(WNAM, Temp)]), WNAM, Temp)
                Temp = np.where(np.logical_and.reduce([np.less(WRDPS, Temp)]), WRDPS, Temp)
                #LogStream.logProblem(Temp)
            if (WHRDPS == None and WRDPS == None and WGFS25 == None):
                Temp = np.where(np.logical_and.reduce([np.less(WNAM, Temp)]), WNAM, Temp)
                #LogStream.logProblem(Temp)

        toc = time.perf_counter()
        LogStream.logProblem(toc-tic)
        return (Temp, dir)

