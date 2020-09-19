
# ----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# siteConfig
# ----------------------------------------------------------------------------

# Include this line to override gfeConfig (BASE configuration).
#   If you want to override a SITE configuration, you will want
#   to replace "gfeConfig" with the SITE configuration file name.
from gfeConfig import *

#------------------------------------------------------------------------
# Initial GFE Startup Weather Elements, Samples, and Edit Action List
# Configurations
#------------------------------------------------------------------------

# Include override statements here. For example, to override the
# the DefaultGroup name ("Public") with "MyDefault", you would include:
#DefaultGroup = "MyDefault"

# Define keyboard shortcuts.
# You are allowed up to 200 shortcuts.
# IMPORTANT:  You should test your shortcuts on your system as many
#  keys are already bound by the system.  For example, F10 is bound by some Tk
#  widgets to bring up menus.
# See gfeConfig.GFECONFIG for more information.

#SmartTools:

ShortCut1 = ["KP_Subtract", "None", "SmartTool","AdjustValue_Down"]
ShortCut2 = ["KP_Add", "None", "SmartTool","AdjustValue_Up"]
ShortCut3 = ["4", "Ctl", "SmartTool","Assign_Value"]
ShortCut4 = ["F7", "None", "SmartTool","Smooth"]
ShortCut5 = ["t", "Ctl", "SmartTool","AmecFW_TBlend_Tool"]
ShortCut6 = ["t", "Alt", "SmartTool","Wood_UMOS_Copy_Tool"]
ShortCut7 = ["d", "Ctl", "SmartTool","AmecFW_TdBlend_Tool"]
ShortCut8 = ["f", "Ctl", "SmartTool","Wood_Td_Check_Tool"]
ShortCut9 = ["d", "Alt", "SmartTool","Wood_UMOS_Td_Copy_Tool"]
ShortCut10 = ["h", "Ctl", "SmartTool","AmecFW_RHTool"]
ShortCut11 = ["w", "Ctl", "SmartTool","AmecFW_Wind_DDFF_Blend_Tool"]
ShortCut12 = ["q", "Alt", "SmartTool","Wood_UMOS_Wind_Copy_Tool"]
ShortCut13 = ["g", "Ctl", "SmartTool","AmecFW_WindGustTool"]
ShortCut14 = ["q", "Ctl", "SmartTool","AmecFW_FreeWindGustTool"]
ShortCut15 = ["s", "Alt", "SmartTool","AmecFW_Copy_WindGust_Tool"]
ShortCut16 = ["a", "Ctl", "SmartTool","AmecFW_SkyBlend_Tool"]
ShortCut17 = ["z", "Alt", "SmartTool","AmecFW_Sky_Interpolation_Tool"]
ShortCut18 = ["z", "Ctl", "SmartTool","AmecFW_Sky_QPF_Rounder_Tool"]
ShortCut19 = ["x", "Ctl", "SmartTool","Wood_CMC_CloudAdjust"]
ShortCut20 = ["n", "Ctl", "SmartTool","AmecFW_Wx_FirstGuess_Tool"]
ShortCut21 = ["b", "Ctl", "SmartTool","Wood_Wx_Thickness_Guess_Tool"]
ShortCut22 = ["x", "Alt", "SmartTool","AmecFW_Interpolation_Wx_Tool"]
ShortCut23 = ["n", "Alt", "SmartTool","AmecFW_Wx_Copy_Tool"]
ShortCut24 = ["y", "Ctl", "SmartTool","AmecFW_PoP_From_Sky_QPF_Tool"]
ShortCut25 = ["a", "Alt", "SmartTool","AmecFW_PoP_Interpolation_Tool"]
ShortCut26 = ["b", "Alt", "SmartTool","AmecFW_Copy_PoP_Tool"]
ShortCut27 = ["3", "Ctl", "SmartTool","AmecFW_QPFBlend_Tool"]
ShortCut28 = ["5", "Ctl", "SmartTool","AmecFW_Storm_Total_SNIPAmt_Tool"]
ShortCut29 = ["6", "Ctl", "SmartTool","AmecFW_Storm_Total_RNZRAmt_Tool"]
ShortCut30 = ["r", "Ctl", "SmartTool","AmecFW_RNZRAmt_Tool"]
ShortCut31 = ["s", "Ctl", "SmartTool","AmecFW_SNIPAmtTool"]
ShortCut32 = ["v", "Ctl", "SmartTool","Wood_3HrlyVis_Tool"]

#Procedures
ShortCut33 = ["F1", "None", "Procedure","Wood_Outlook_Blend_Procedure"]
ShortCut34 = ["F2", "None", "Procedure","Wood_BulkInterpolation_Procedure"]

#Edit Tools
ShortCut35 = ["F3", "None", "EditTool", "Sample"]
ShortCut36 = ["F4", "None", "EditTool", "Pencil"]
ShortCut37 = ["F5", "None", "EditTool", "DrawEditArea"]

#Toggle Actions
ShortCut39 = ["F6", "None", "Toggle", "TEGM"]


#------------------------------------------------------------------------
# Misc. Configuration
#------------------------------------------------------------------------
# This list of Weather element names will be used to sort the GridManager.
# Elements in this list will occur first.  All others will be sorted
# by name.
GridManagerSortOrder = ['T', 'Td', 'RH', 'MaxT', 'MinT', 'MaxRH', 'MinRH',
  'WindChill', 'HeatIndex', 'Wind', 'WindGust',  'FreeWind',
  'TransWind', 'Sky', 'Wx', 'LAL', 'PoP', 'CWR', 'QPF',
  'StormTotalSNIPAmt', 'StormTotalRNZRAmt', 'SnowLevel', 'MaxTAloft', 'WetBulb', 'Hazards',
  'FzLevel', 'Haines', 'MixHgt', 'RNZRAmt', 'SNIPAmt', 'Pmsl', 'Lum', 'VisKm', 'Insol']

# The network timeout for connecting to the ifpServer and for waiting for
# requests is specified in seconds.
networkTimeout = 300

#------------------------------------------------------------------------
# Map Background Configuration
#------------------------------------------------------------------------
# Defines the initial loaded set of map backgrounds.  The name of the
# background should match the list of available maps defined in Maps.py
# in the server configuration files.
MapBackgrounds_default = ['Canada', 'States']

# Defines the available colors for the map backgrounds that appears
# in the color list popup button 3 over a map legend.

# Specific Colors for a map background
# The user may specify a specific color to be used for a map background,
# rather # than getting a random color assigned.
# Format is mapName_graphicColor = color.  The color does
# not need to be in the MapBackgrounds_availColors list.
# States_graphicColor = 'green'

# Specific Graphic Line Widths for a map
# Default line widths can be set for each map background based on
# map name. Zero is the default value, which represents thin lines.
# The larger the number, the wider the line.  The format is mapName_lineWidth.
# Do not include a decimal point after these entries.
States_lineWidth = 2
Canada_lineWidth=2

# Specific Line Pattern definitions for a map
# Default line patterns can be set up for each map background.  The
# possible strings are "SOLID", "DASHED", "DOTTED", "DASHED_DOTTED".  The
# values must be enclosed within quotes.   The format is mapName_linePattern.
# States_linePattern = "SOLID"

# MapLabelXOffset and MapLabelYOffset are the number of pixels you
# wish to move map city labels relative to their "normal" position.
# MapLabelXOffset = 0
# MapLabelYOffset = 0

# Labels for each map.  These are the names of the shapefile attributes
# to be used for labels.  Format is mapName_labelAttribute = name.
Ontario_Rwis_labelAttribute = "NAME"
Ontario_Laf_labelAttribute = "NAME"
Maritime_Sites_labelAttribute = "NAME"
Maritime_RWIS_Sites_labelAttribute = "NAME"
Maritime_LAF_Sites_labelAttribute = "NAME"
Newfoundland_Sites_labelAttribute = "NAME"
Newfoundland_RWIS_Sites_labelAttribute = "NAME"
Newfoundland_LAF_Sites_labelAttribute = "NAME"
North_RWIS_Sites_labelAttribute = "NAME"
Alberta_All_Sites_labelAttribute = "NAME"
Alberta_LAF_Sites_labelAttribute = "NAME"
Alberta_RWIS_Sites_labelAttribute = "NAME"
NLDOT_LAF_Sites_labelAttribute = "NAME"
NLDOT_RWIS_Sites_labelAttribute = "NAME"
NLDOT_ALL_Sites_labelAttribute = "NAME"
NBDOT_LAF_Sites_labelAttribute = "NAME"
NBDOT_RWIS_Sites_labelAttribute = "NAME"
NBDOT_ALL_Sites_labelAttribute = "NAME"
NSDOT_LAF_Sites_labelAttribute = "NAME"
NSDOT_RWIS_Sites_labelAttribute = "NAME"
NSDOT_ALL_Sites_labelAttribute = "NAME"
PEI_LAF_Sites_labelAttribute = "NAME"
PEI_RWIS_Sites_labelAttribute = "NAME"
PEI_ALL_Sites_labelAttribute = "NAME"
NBDOE_LAF_Sites_labelAttribute = "NAME"
DayRoss_LAF_Sites_labelAttribute = "NAME"
H1_LAF_Sites_labelAttribute = "NAME"
H1_Fo_Sites_labelAttribute = "NAME"
IESO_LAF_Sites_labelAttribute = "NAME"
IESO_SW_Sites_labelAttribute = "NAME"
MTO_LAF_Sites_labelAttribute = "NAME"
MTO_RWIS_Sites_labelAttribute = "NAME"
MTO_ALL_Sites_labelAttribute = "NAME"
NBDOE_LAF_Sites_labelAttribute = "NAME"
OnMuni_RWIS_Sites_labelAttribute = "NAME"
OnMuni_LAF_Sites_labelAttribute = "NAME"
OnMuni_ALL_Sites_labelAttribute = "NAME"
STJ_ALL_Sites_labelAttribute = "NAME"
STJ_LAF_Sites_labelAttribute = "NAME"
STJ_RWIS_Sites_labelAttribute = "NAME"

# Specific Font Offsets for a map background.
# The font offset (called magnification on the GFE menus) allows the
# default font size to be increased or decreased on a per map basis.
# Numbers can range from -2 through +2.  Format is mapName_fontOffset.
# Do not include a decimal point after these entries.
# States_fontOffset = 0

#------------------------------------------------------------------------
# System Time Range Configuration
#------------------------------------------------------------------------
# These parameters indicate the span of the Grid Manager and Temporal
# Editor in relation to the current time.  Units are in hours.  If grids
# are present, the displayable time range may be expanded by the software.
SystemTimeRange_afterCurrentTime =  384

#------------------------------------------------------------------------
# UI Configuration
#------------------------------------------------------------------------
# Defines the color used by the Grid Manager to indicate the
#current system time
CurrentSystemTime_color = 'Green'

# Defines the initial horizontial size of the grid manager when first
# starting the GFE in pixels.  Do not place a decimal point after the number.
TimeScale_horizSize = 450

# Defines the number of Edit Area Quick Set Buttons. Do not place a
# decimal point after the buttons
QuickSetButtons = 7

# Initial layout up of Grid Manager/Temporal Editor:
# Values:  "OnTop" (default)
#          "OnLeft"
GM_TE_Layout = "OnLeft"

#------------------------------------------------------------------------
# Algorithm Configuration
#------------------------------------------------------------------------
# Smart tools can access time-weighted averages of multiple grids.  Since
# weather is discrete, time weighted average for weather is based on
# all values of weather at that grid point as long as they occupy at least
# the given percentage of all grids.  Do not place a decimal point after
# the number.

# Smooth algorithm default value
SmoothSize = 7

# Smooth Size Choices
SmoothSizeList = [3, 5, 7, 9, 11]

# User can control the interpolation algorithm for each weather element.
# The format of the string is parmName_interpolateAlgorithm.  The available
# options, which must be quoted, are "CUBIC_ADVECT", "LINEAR_ADVECT",
# "CUBIC_NOADVECT", and "LINEAR_NOADVECT".  By default, most elements use
# CUBIC_NOADVECT, except for Wx, PoP, Sky, and QPF which use CUBIC_ADVECT.
# Wind and Wx cannot be changed.
# T_interpolateAlgorithm = "CUBIC_NOADVECT"
# QPF_interpolateAlgorithm = "LINEAR_NOADVECT"
T_interpolateAlgorithm = "CUBIC_NOADVECT"
Td_interpolateAlgorithm = "CUBIC_NOADVECT"
RH_interpolateAlgorithm = "CUBIC_NOADVECT"
Wind_interpolateAlgorithm = "CUBIC_NOADVECT"
WindGust_interpolateAlgorithm = "CUBIC_NOADVECT"
Sky_interpolateAlgorithm = "LINEAR_NOADVECT"
PoP_interpolateAlgorithm = "LINEAR_NOADVECT"
Vis_interpolateAlgorithm = "LINEAR_NOADVECT"
Lum_interpolateAlgorithm = "LINEAR_NOADVECT"


#------------------------------------------
Wind_density=-3

#------------------------------------------------------------------------
# Weather/Discrete Common Value Definitions
#------------------------------------------------------------------------
# the following describes common types that appear on the temporal
# editor popup menu and the spatial editor color bar popup menu.
# For WEATHER, the format is the "ugly" string of the Weather Key. For
# DISCRETE, the format is the key string of the Discrete Key.
# Prefixing an string with other strings that end with a vertical
# bar (|) will make these strings in a cascade,
# such as "Winter|Wide:S:--:<NoVis>:<NoAttr>",
# which will put the widespread snow under a Winter cascade.  The format
# of this entry is parmName_commonValues, and applies to Weather and
# Discrete only.

Wx_commonValues = [ \
  "<NoCov>:<NoWx>:<NoInten>:<NoVis>:<NoAttr>",
   "Patchy:F:<NoInten>:<NoVis>:<NoAttr>",
   "Summer--------------------------------|",
   "SChc:L:-:<NoVis>:<NoAttr>",
   "SChc:RW:-:<NoVis>:<NoAttr>",
   "SChc:R:-:<NoVis>:<NoAttr>",
   "SChc:RW:-:<NoVis>:<NoAttr>^SChc:T:<NoInten>:<NoVis>:<NoAttr>",
   #"SChc:R:-:<NoVis>:<NoAttr>^SChc:T:<NoInten>:<NoVis>:<NoAttr>",
   "Winter----------------------------------|",
   "SChc:ZL:-:<NoVis>:<NoAttr>",
   "SChc:ZR:-:<NoVis>:<NoAttr>",
   "SChc:IP:-:<NoVis>:<NoAttr>",
   "SChc:SW:-:<NoVis>:<NoAttr>",
   "SChc:S:-:<NoVis>:<NoAttr>",
   "Mix---------------------------------------|",
   "Brf:ZL:-:<NoVis>:<NoAttr>^Brf:L:-:<NoVis>:<NoAttr>",
   "Brf:ZL:-:<NoVis>:<NoAttr>^Brf:IP:-:<NoVis>:<NoAttr>",
   #"Brf:ZL:-:<NoVis>:<NoAttr>^Brf:RW:-:<NoVis>:<NoAttr>",
   "Brf:SW:-:<NoVis>:<NoAttr>^Brf:ZL:-:<NoVis>:<NoAttr>",
   #"Brf:S:-:<NoVis>:<NoAttr>^Brf:ZL:-:<NoVis>:<NoAttr>",
   
   "Brf:ZR:-:<NoVis>:<NoAttr>^Brf:RW:-:<NoVis>:<NoAttr>",
   "Brf:ZR:-:<NoVis>:<NoAttr>^Brf:R:-:<NoVis>:<NoAttr>",
   "Brf:ZR:-:<NoVis>:<NoAttr>^Brf:IP:-:<NoVis>:<NoAttr>",
   "Brf:ZR:-:<NoVis>:<NoAttr>^Brf:SW:-:<NoVis>:<NoAttr>",
   #"Brf:ZR:-:<NoVis>:<NoAttr>^Brf:S:-:<NoVis>:<NoAttr>",
    
   #"Brf:L:-:<NoVis>:<NoAttr>^Brf:IP:-:<NoVis>:<NoAttr>",
   #"Brf:L:-:<NoVis>:<NoAttr>^Brf:SW:-:<NoVis>:<NoAttr>",
   
   "Brf:RW:-:<NoVis>:<NoAttr>^Brf:SW:-:<NoVis>:<NoAttr>",
   "Brf:RW:-:<NoVis>:<NoAttr>^Brf:IP:-:<NoVis>:<NoAttr>",
   
   "Brf:R:-:<NoVis>:<NoAttr>^Brf:IP:-:<NoVis>:<NoAttr>",
   #"Brf:R:-:<NoVis>:<NoAttr>^Brf:SW:-:<NoVis>:<NoAttr>",
   #"Brf:R:-:<NoVis>:<NoAttr>^Brf:S:-:<NoVis>:<NoAttr>",
   
   "Brf:SW:-:<NoVis>:<NoAttr>^Brf:IP:-:<NoVis>:<NoAttr>",
   
   #"Brf:S:-:<NoVis>:<NoAttr>^Brf:IP:-:<NoVis>:<NoAttr>",
  ]

#------------------------------------------------------------------------
# Weather Dialog Default Values
#------------------------------------------------------------------------
# the following describes the intensity and coverage/probability defaults
# that appear in the Set Value dialog for Weather data.  The format is
# the weather type (e.g., RW), followed by the keyword.  The actual value
# is a string surrounded in quotes.

# Define the weather dialog default coverage/probabilities
#R_defaultCoverage = "Wide"
#RW_defaultCoverage = "Wide"
#S_defaultCoverage = "Wide"
#SW_defaultCoverage = "Wide"
#L_defaultCoverage = "Wide"
#ZR_defaultCoverage = "Wide"
#ZL_defaultCoverage = "Wide"
#IP_defaultCoverage = "Wide"
#T_defaultCoverage = "Wide"

IP_defaultCoverage = "SChc"
ZR_defaultCoverage = "SChc"
ZL_defaultCoverage = "SChc"
L_defaultCoverage = "SChc"
T_defaultCoverage = "SChc"
SW_defaultCoverage = "SChc"
RW_defaultCoverage = "SChc"
R_defaultCoverage = "SChc"
S_defaultCoverage = "SChc"

#R_defaultCoverage= "Chc"
#RW_defaultCoverage= "Chc"
#S_defaultCoverage= "Chc"
#SW_defaultCoverage= "Chc"
#T_defaultCoverage= "Chc"
#ZR_defaultCoverage= "Chc"
#IP_defaultCoverage= "Chc"
#ZL_defaultCoverage= "Chc"
#L_defaultCoverage= "Chc"

#R_defaultCoverage = "Pds"
#RW_defaultCoverage = "Pds"
#T_defaultCoverage= "Pds"
#S_defaultCoverage = "Pds"
#SW_defaultCoverage = "Pds"
#L_defaultCoverage = "Pds"
#ZR_defaultCoverage = "Pds"
#ZL_defaultCoverage = "Pds"
#IP_defaultCoverage = "Pds"

#R_defaultCoverage = "SChc"
#RW_defaultCoverage = "SChc"
#T_defaultCoverage= "SChc"
#S_defaultCoverage = "SChc"
#SW_defaultCoverage = "SChc"
#L_defaultCoverage = "SChc"
#ZR_defaultCoverage = "SChc"
#ZL_defaultCoverage = "SChc"
#IP_defaultCoverage = "SChc"

R_defaultCoverage = "Brf"
RW_defaultCoverage = "Brf"
T_defaultCoverage= "Brf"
S_defaultCoverage = "Brf"
SW_defaultCoverage = "Brf"
L_defaultCoverage = "Brf"
ZR_defaultCoverage = "Brf"
ZL_defaultCoverage = "Brf"
IP_defaultCoverage = "Brf"

#R_defaultCoverage = "Inter"
#RW_defaultCoverage = "Inter"
#T_defaultCoverage= "Inter"
#S_defaultCoverage = "Inter"
#SW_defaultCoverage = "Inter"
#L_defaultCoverage = "Inter"
#ZR_defaultCoverage = "Inter"
#ZL_defaultCoverage = "Inter"
#IP_defaultCoverage = "Inter"

#------------------------------------------------------------------------
# Default (non-weather) Color Table Algorithm Configuration
#------------------------------------------------------------------------
# The default color table is used for all parameters unless overridden in
# this configuration file.  The left wavelength defines the left side
# value for the color in nanometers. 380 is roughly purple.  The right
# wavelength defines the right side value for the color in nanometers.
# 650 is red.  The number of colors indicate the number of color bins
# that will be used when the default color table is displayed.
# Use decimal points after the wavelengths, but not the numColors.

# Default Max/Min Ranges for Color Tables
# By default, all colors tables (except for WEATHER) are spread out over
# the range of the minimum to maximum weather element possible value, as
# defined by serverConfig.py.  The initial range of the color table can
# be specified through these entries.  The form of the two entries are:
# parmName_maxColorTableValue and parmName_minColorTableValue.  These
# values are floats and MUST have a decimal point in them.
#T_maxColorTableValue = 120.0
#T_minColorTableValue = -30.0

########## Limits of the color bar over the spatial editor per weather element.
RNZRAmt_maxColorTableValue=20.0
RNZRAmt_minColorTableValue=0.0
SNIPAmt_maxColorTableValue=20.0
SNIPAmt_minColorTableValue=0.0
QPF_maxColorTableValue=30.0
QPF_minColorTableValue=0.0
T_maxColorTableValue=40.0
T_minColorTableValue=-40.0
Td_maxColorTableValue=40.0
Td_minColorTableValue=-40.0
Vis_maxColorTableValue=15.0
Vis_minColorTableValue=0.0
StormTotalSNIPAmt_maxColorTableValue= 70.0
StormTotalSNIPAmt_minColorTableValue=0.0
StormTotalRNZRAmt_maxColorTableValue=70.0
StormTotalRNZRAmt_minColorTableValue=0.0
Pmsl_maxColorTableValue=1050.0
Pmsl_minColorTableValue=915.0
Insol_maxColorTableValue=1300.0
Insol_minColorTableValue=0.0

#----------------------------------------------------

##Generic_colors=  ["blue", "maroon", "green", "red", "PaleGreen", "MistyRose", "chartreuse3", "PapayaWhip" "DeepPink", "paleTurquoise", "Coral",
##                        "CadetBlue2", "Aquamarine", "DarkKhaki", "DodgerBlue", "IndianRed1",
##                        ]


#------------------------------------------------------------------------
# Weather Color Algorithm Configuration
#------------------------------------------------------------------------
# Color Tables for Weather are handled differently than scalar and
# vector data.  Coverages are denoted by fill patterns.  Composite
# types by colors.  Complex weather of more than two coverages will
# result in a solid fill pattern and can't be configured.

WeatherCoverage_fillPatterns = ["SOLID", "SOLID", "SOLID", "SOLID",
                                 "SOLID", "SOLID", "SOLID", "SOLID",
                                "SOLID", "SOLID", "SOLID", "SOLID",
                                 "SOLID", "SOLID", "SOLID", "SOLID"]

# The weather type entries are generic entries without intensities.
# Combinations are permitted.  The WeatherType_names and WeatherType_colors
# are parallel lists of names and colors.  The default weather color table
# algorithm looks at the weather type or combination of types, as listed
# in the _names, and matches the list with the specified color.  For
# example, if T appears in the names as the first entry and brown2 appears
# in the colors for the first entry, then for weather type T, the color
# shown will be brown2.

WeatherType_names = ["<NoWx>", "T", "R", "RW", "L", "ZR", "ZL",
                     "S", "SW", "IP", "TRW", "SIP", "RZR", "ZRIP", "RIP", "ZRS", "RS", "RWSW", "F", "TR",
                     "RWIP", "RWZL", "ZLIP", "SWZL", "SWIP", "FR", "AT"]

##WeatherType_colors = ["Gray40", "Orange", "ForestGreen", "Green",
##                      "PaleGreen", "red", "Magenta", "Blue3", "lightBlue", "purple",
##                      "Coral", "DodgerBlue", "Pink", "Brown", "Khaki", "DeepPink",
##                      "Aquamarine", "Aquamarine3", "Yellow", "Gray75", "MistyRose", "grey30", "Brown",
##                      "blue1", "coral1", "paleturquoise", "DeepPink"]

WeatherType_colors = ["Gray40", "Orange", "ForestGreen", "Green",
                      "PaleGreen", "red", "Magenta", "Blue3", "lightBlue", "purple",
                      "Coral", "DodgerBlue", "Pink", "Brown", "Khaki", "DeepPink",
                      "Aquamarine", "Aquamarine3", "Yellow", "Gray75", "MistyRose", "grey30", "Brown",
                      "cyan", "coral1", "paleturquoise", "DeepPink"]

# Colors to use for weather which was not defined using any of the methods
# found above. The colors in this list will be used before a "random" color
# is chosen.
WeatherGeneric_colors = [ "red6", "Brown", "DeepPink", "paleTruquoise", "Coral",
                        "CadetBlue2", "Aquamarine", "DarkKhaki", "DodgerBlue", "IndianRed1",
                         "PaleGreen", "MistyRose", "chartreuse3", "PapayaWhip"]


#------------------------------------------------------------------------
# delta values
# Delta values define the default delta (adjust up, adjust down) value
# for the adjust operations.  The user can redefine this at any time
# through the GUI.  If not specified, the delta value defaults to
# the precision value.  For example, a precision of 0 indicates a delta of 1.
# and a precision of 1 indicates a delta of 0.1.
# Format is parmName_deltaValue = value.
# Be sure to include a decimal point.
#parmName_deltaValue = 10.0
#FzLevel_deltaValue = 100.0
#SnowLevel_deltaValue = 100.0
PoP_deltaValue = 10.0
Sky_deltaValue = 10.0
T_deltaValue = 1.0
Td_deltaValue = 1.0

#------------------------------------------------------------------------
# Preference Defaults
#------------------------------------------------------------------------
# Default Time Scale Periods that are shown on the time scale.  These
# are names of the selection time ranges (SELECTTR).
TimeScalePeriods = ['Today', 'Tonight', 'Tomorrow', 'Tomorrow Night',
  'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8']



#------------------------------------------------------------------------
# PRODUCT GENERATION SCRIPTS
#------------------------------------------------------------------------
# Product Generation Scripts appear under the product generation menu
# on the GFE.
Scripts = [
        "Send Forecast to Skynet:" +
        "/usr/src/scripts/sendForecastToSkynet.sh {productDB} {site}"
    ]

