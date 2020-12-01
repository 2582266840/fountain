import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
import matplotlib.pyplot as map
max=0
numb=0
y=[0 for _ in  range(1000)]
x=[0 for _ in  range(1000)]
for n in range(1,1000):
        x[n]=n
for a in range(1,1000):
#a=1#比重
    a=a/10
    C=10
    total=0
    for t in range(1,10):
        C1=a/(a+1)*C
        c2=1/(a+1)*C
        sampleNo = 1;
        mu = 1
        sigma = 0.5
        np.random.seed(3)
        s = np.random.normal(mu, sigma, sampleNo )
        C=s*C1-c2
        total+=c2       
    if max<total:
        max=total
        numb=a
    e=(int)(a*10)
    da=0;
    y[e]=total
print(max)
print(numb)
map.plot(x,y,'b')
map.show()  