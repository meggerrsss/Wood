# functions from http://paulbourke.net/miscellaneous/interpolation/
# determining if running a gust tool on hourly grids is necessary or if interpolating 3 hourly grids with the tool already run is fine
# question what you've been told kids


def CubicInterpolate(y0,y1,y2,y3,mu):
   mu2 = mu*mu;
   a0 = y3 - y2 - y0 + y1;
   a1 = y0 - y1 - a0;
   a2 = y2 - y0;
   a3 = y1;
   return(a0*mu*mu2+a1*mu2+a2*mu+a3)


def CatmullRom(y0,y1,y2,y3,mu):
   mu2 = mu*mu;
   a0 = -0.5*y0 + 1.5*y1 - 1.5*y2 + 0.5*y3;
   a1 = y0 - 2.5*y1 + 2*y2 - 0.5*y3;
   a2 = -0.5*y0 + 0.5*y2;
   a3 = y1;
   return(a0*mu*mu2+a1*mu2+a2*mu+a3)


def avg(l):
  if len(l) == 0: return "all values were the same"
  return sum(l)/len(l)

errcub = []
errcat = []
for i in range(0,100,5):
  for j in range(0,100,5):
    for k in range(0,100,5):
      for l in range(0,100,5):
        muu = 0.66
        v1 = 1.5*CubicInterpolate(i,j,k,l,muu)
        v2 = CubicInterpolate(1.5*i,1.5*j,1.5*k,1.5*l,muu)
        if not v1 == v2:
          #print((i,j,k,l), v1-v2)
          errcub.append(v1-v2)
        u1 = 1.5*CatmullRom(i,j,k,l,muu)
        u2 = CatmullRom(1.5*i,1.5*j,1.5*k,1.5*l,muu)
        if not u1 == u2:
          #print((i,j,k,l), u1-u2)
          errcat.append(u1-u2)
print(avg(errcub))
print(avg(errcat))


