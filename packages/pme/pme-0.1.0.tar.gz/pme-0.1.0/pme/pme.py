import numpy as np
import scipy as sp


def pme(est,pvar):
    d=est.shape[1]
    E,Q=sp.linalg.schur(est)
    EI=np.diag(E)
    jstd=np.sqrt(pvar/d**2)
    if np.any(jstd==0):
        return est
    prob=((1-sp.stats.norm.cdf(-EI/jstd))*jstd*np.sqrt(np.pi*2))
    flag=~np.isclose(prob,0)
    res=np.zeros(d)
    res[flag]=((EI*(1-sp.stats.norm.cdf(-EI/jstd))*jstd*np.sqrt(np.pi*2)
                      + jstd**2*np.exp(-EI**2/2/jstd**2))[flag]/
                        prob[flag] )
    res=Q@np.diag(res)@Q.T

    return res/np.trace(res)*np.trace(est)
 
def samplecov(X,zeromean=False):
    if zeromean:
        Xm=X
    else:
        Xm=X-X.mean(axis=0)
    return np.dot(Xm.T,Xm)/X.shape[0]

def sigma(x,zeromean=False):
    n=x.shape[0]
    if zeromean:
        xm=x
    else:
        xm=x-x.mean(axis=0)
    S=np.dot(xm.T,xm)/n
    tot=0
    for i in range(n):
        tot+=(((np.outer(xm[i],xm[i]))-S)**2).sum()
    return tot/n**2

