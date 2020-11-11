# import NL FIRE data into library 
import shlex
sitelist = [i for i in open('NLFIREobssites.txt', 'r').read().strip().split("\n")]
sites = {}
for i in range(len(sitelist)):
  id,sitename,lat,long,umos = shlex.split(sitelist[i])
  sites

 


def dist(lat1,long1,lat2,long2):
  