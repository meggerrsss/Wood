# import NL FIRE data into library 
import shlex
import pandas
import numpy
from sklearn.neighbors import DistanceMetric

sitelist = [i for i in open('NLFIREforecastsites.txt', 'r').read().strip().split("\n")]
sites = {}
for i in range(len(sitelist)):
  id,sitename,lat,long,umos = shlex.split(sitelist[i])
  sites

forecast_sites = pandas.read_csv('NLFIREforecastsites.txt', sep=" ", names=["site_id", "name", "lat", "long", "umos"])
print(forecast_sites)

obs = pandas.read_csv("NLFIREobsemail.txt", sep="\t")
print(obs)
"""so, for each obs point, find the nearest model point
Then, for each collection of obs, return max(precip) for that point"""


def dist(lat1,long1,lat2,long2):
  pass