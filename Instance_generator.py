import numpy as np

def polinomio(x,parameters):
  power=len(parameters-1)
  while power>0:
    
  


def instance(n,power):
  x1=np.random.randint(-1000,1000,n)
  parameters=np.random.randint(-1000,1000,power+1)
  y1=polinomio(x1,parameters)
  r=[x1,y1,parameters]
  return r
