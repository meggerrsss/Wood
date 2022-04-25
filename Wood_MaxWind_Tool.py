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

VariableList = [
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
        THRDPS = None
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

        # importing RDPS wind  
        try:
            WRDPS = self.getGrids(modelWRDPS, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        if (WRDPS == None and modelrunRDPS == "Latest"):
            try:
                WRDPS = self.getGrids(modelWRDPSprev, "Wind", "SFC", GridTimeRange)[0]
            except:
                pass

        # importing HRDPS wind  
        try:
            WHRDPS = self.getGrids(modelWHRDPS, "Wind", "SFC", GridTimeRange)[0]
            THRDPS = self.getGrids(modelWHRDPS, "T", "SFC", GridTimeRange)
        except:
            pass
        if (WHRDPS == None and modelrunHRDPS == "Latest"):
            try:
                WHRDPS = self.getGrids(modelWHRDPSprev, "Wind", "SFC", GridTimeRange)[0]
                THRDPS = self.getGrids(modelWHRDPSprev, "T", "SFC", GridTimeRange)
            except:
                pass


        # importing GDPS wind  
        try:
            WGDPS = self.getGrids(modelWGDPS, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        if (WGDPS == None and modelrunGDPS == "Latest"):
            try:
                WGDPS = self.getGrids(modelWGDPSprev, "Wind", "SFC", GridTimeRange)[0]
            except:
                pass

        # importing GFS wind  
        try:
            WGFS25 = self.getGrids(modelWGFS25, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        if (WGFS25 == None and modelrunGFS25 == "Latest"):
            try:
                WGFS25 = self.getGrids(modelWGFS25prev, "Wind", "SFC", GridTimeRange)[0]
            except:
                pass

        # importing NAM12 wind  
        try:
            WNAM12 = self.getGrids(modelWNAM12, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        if (WNAM12 == None and modelrunNAM == "Latest"):
            try:
                WNAM12 = self.getGrids(modelWNAM12prev, "Wind", "SFC", GridTimeRange)[0]
            except:
                pass
              
        # importing NAM32 wind  - 
        try:
            WNAM32 = self.getGrids(modelWNAM32, "Wind", "SFC", GridTimeRange)[0]
        except:
            pass
        if (WNAM32 == None and modelrunNAM == "Latest"):
            try:
                WNAM32 = self.getGrids(modelWNAM32prev, "Wind", "SFC", GridTimeRange)[0]
            except:
                pass
              
        try:          
            # where NAM12 is empty, replace with NAM32
            WNAM = np.where(np.logical_and.reduce([np.equal(WNAM12, 0)]), WNAM32, WNAM12)
          
            #WNAM = WNAM32 # for when NAM12 is acting up, enable this and ignore NAM12 entirely
            #LogStream.logProblem(WNAM32, WNAM12, WNAM)
        except:
            pass

        # separating Fcst into speed and direction
        Temp=WFcst[0]
        dir=WFcst[1]
        #LogStream.logProblem(Temp)

        #Find model max wind speed. For HRDPS, using THRDPS to determine where that model cuts off so we can discard those null/suspiciously high band of wind speeds. Model cutoff values for temperature are -62 which is easiest to query.
        if MaxorMin == "Max":
            if WRDPS != None:
                Temp = np.where(np.logical_and.reduce([np.greater(WRDPS, Temp)]), WRDPS, Temp)
                #LogStream.logProblem(Temp)
            if WHRDPS != None:
                Temp = np.where(np.logical_and.reduce([np.greater(WHRDPS, Temp), np.greater(THRDPS, -60)]), WHRDPS, Temp)
                #LogStream.logProblem(Temp)
            if WGDPS != None:
                Temp = np.where(np.logical_and.reduce([np.greater(WGDPS, Temp)]), WGDPS, Temp)
                #LogStream.logProblem(Temp)
            if WGFS25 != None:
                Temp = np.where(np.logical_and.reduce([np.greater(WGFS25, Temp)]), WGFS25, Temp)
                #LogStream.logProblem(Temp)
            if WNAM != None:
                Temp = np.where(np.logical_and.reduce([np.greater(WNAM, Temp)]), WNAM, Temp)
                #LogStream.logProblem(Temp)

        #Find model min wind speed. For HRDPS, using THRDPS to determine where that model cuts off so we can discard those null wind speeds.      
        elif MaxorMin == "Min":
            if WRDPS != None:
                Temp = np.where(np.logical_and.reduce([np.less(WRDPS, Temp)]), WRDPS, Temp)
                #LogStream.logProblem(Temp)
            if WHRDPS != None:
                Temp = np.where(np.logical_and.reduce([np.less(WHRDPS, Temp), np.greater(THRDPS, -60)]), WHRDPS, Temp)
                #LogStream.logProblem(Temp)
            if WGDPS != None:
                Temp = np.where(np.logical_and.reduce([np.less(WGDPS, Temp)]), WGDPS, Temp)
                #LogStream.logProblem(Temp)
            if WGFS25 != None:
                Temp = np.where(np.logical_and.reduce([np.less(WGFS25, Temp)]), WGFS25, Temp)
                #LogStream.logProblem(Temp)
            if WNAM != None:
                Temp = np.where(np.logical_and.reduce([np.less(WNAM, Temp)]), WNAM, Temp)
                #LogStream.logProblem(Temp)

        return (Temp, dir)
