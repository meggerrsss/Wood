# ----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# Wood_WxOutlook_Tool
#
# Author: Matt Baker
# July 22, 2019
#
# This tool will provide you with the first guess precipitation type basede on
# your sfc T and sfc QPF
# ----------------------------------------------------------------------------
ToolType = "numeric"
WeatherElementEdited = "Wx"
import numpy as np
import math
import SmartScript

class Tool (SmartScript.SmartScript):
    def __init__(self, dbss):
        SmartScript.SmartScript.__init__(self, dbss)

    def execute(self, T, Wx, QPF, GridTimeRange, varDict):
        SITE=self.getSiteID()

        TFcst=self.getGrids("Fcst", "T", "SFC", GridTimeRange)
        QPFFcst=self.getGrids("Fcst", "QPF", "SFC", GridTimeRange)
   
        wxValues = Wx[0]
        keys = Wx[1]

        #Rain
        #wxValues=np.where(np.logical_and.reduce([np.greater(TFcst, 1.4), np.greater(QPFFcst, 0), np.less(QPFFcst, 0.5)]), self.getIndex("SChc:L:-:<NoVis>:", keys), wxValues)
        wxValues=np.where(np.logical_and.reduce([np.greater(TFcst, 1.4), np.greater(QPFFcst, 0), np.less(QPFFcst, 1.5)]), self.getIndex("SChc:RW:-:<NoVis>:", keys), wxValues)
        wxValues=np.where(np.logical_and.reduce([np.greater(TFcst, 1.4), np.greater_equal(QPFFcst, 1.5)]), self.getIndex("SChc:R:-:<NoVis>:", keys), wxValues)
        #Rain/Snow Mix
        wxValues=np.where(np.logical_and.reduce([np.less_equal(TFcst, 1.4), np.greater(TFcst, 0.4), np.greater(QPFFcst, 0)]), self.getIndex("Brf:RW:-:<NoVis>:^Brf:SW:-:<NoVis>:", keys), wxValues)
        #Snow
        wxValues=np.where(np.logical_and.reduce([np.less_equal(TFcst, 0.4), np.greater(QPFFcst, 0)]), self.getIndex("SChc:SW:-:<NoVis>:", keys), wxValues)
        wxValues=np.where(np.logical_and.reduce([np.less_equal(TFcst, 0.4), np.greater_equal(QPFFcst, 1.5)]), self.getIndex("SChc:S:-:<NoVis>:", keys), wxValues)
        #Clean Up
        wxValues=np.where(np.logical_and.reduce([np.equal(QPFFcst, 0)]), self.getIndex("<NoCov>:<NoWx>:<NoInten>:<NoVis>:", keys), wxValues)

                          
        return (wxValues, keys)
