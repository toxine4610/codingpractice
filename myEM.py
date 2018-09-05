'''
script to fit a gaussian mixtures model using the EM algo
'''


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal as mvn		

def createMixtures(N = 100, m = 0.3, sig1 = 2, sig2 = 1, mu1 = 2, mu2 = 8):
	X = []
	for _ in range(N):
		x1 = sig1*np.random.randn()+mu1
		x2 = sig2*np.random.randn()+mu2
		if np.random.rand() < m:
			X.append(x1)
		else:
			X.append(x2)
	return X

def GaussLikeli(x, mu, sig):
	p = np.sqrt(1/(2*np.pi*(sig**2)))*np.exp(-0.5*(((x-mu)/sig)**2))
	return p

def e_step(X, mu1, mu2, sig1, sig2, pa, pb):
	bn ,bd, bx = 0,0,0
	an, ad, ax = 0,0,0
	for i in X:
		pxb  = GaussLikeli(i, mu1, sig1)
		pxa  = GaussLikeli(i, mu2, sig2)
		bn   +=  ( (pxb*pb)/((pxa*pa)+(pxb*pb)) )*i
		bx   +=  ( (pxb*pb)/((pxa*pa)+(pxb*pb)) )*(i-mu1)**2
		bd	 +=  ( (pxb*pb)/((pxa*pa)+(pxb*pb)) )
		an   +=  ( (pxa*pa)/((pxa*pa)+(pxb*pb)) )*i
		ax   +=  ( (pxa*pa)/((pxa*pa)+(pxb*pb)) )*(i-mu2)**2
		ad	 +=  ( (pxa*pa)/((pxa*pa)+(pxb*pb)) )
	return bn, bd, an, ad, bx, ax

def m_step(bn, bd, an, ad, bx, ax):
	mu1 = bn/bd
	mu2 = an/ad
	sig1 = np.sqrt( bx/bd )
	sig2 = np.sqrt( ax/ad )
	return mu1, mu2, sig1, sig2

def runEM(maxIter):

	m = 0.4
	sig1 = 2
	sig2 = 2
	mu1 = -4
	mu2 = 4


	X = createMixtures(m = m, sig1 = sig1, sig2 = sig2, mu1 = mu1, mu2 = mu2)
	llactual = 0
	for i in X:
		llactual += np.log( m*GaussLikeli(i,mu1,mu2)  + (1-m)*GaussLikeli(i,mu2,sig2) )

	# initial guess
	pa = 0.5
	pb = 0.5
	mu1 = 2
	mu2 = 1
	sig1 = 1
	sig2 = 1

	print("Initial Guess = {}".format((mu1,mu2)))
	
	maxIter = 1000
	llold = 0
	L  = []
	# run iteration
	for e in range(maxIter):
		bn,bd,an,ad,bx,ax = e_step(X,mu1, mu2, sig1, sig2, pa, pb)
		mu1,mu2,sig1,sig2 = m_step(bn,bd,an,ad,bx,ax)
		
		pa = bd/len(X)
		pb = ad/len(X)

		ll = 0
		for i in X:
			ll += np.log( pb*GaussLikeli(i, mu1,sig1)  + pa*GaussLikeli(i, mu2,sig2) )
		if np.abs( -ll+llactual ) < 0.01:
			break
		llold = ll
		L.append( (-llold) + (llactual) )

		
	return mu1, mu2, sig1, sig2, pb, pa, L

mu1, mu2,sig1,sig2, pb, pa, L = runEM(100)
print( "Component 1: MU = {:.3f}, Sig = {:.3f}, W = {:.3f}".format(mu1, sig1, pb) )
print( "Component 2: MU = {:.3f}, Sig = {:.3f}, W = {:.3f}".format(mu2, sig2, pa) )
plt.plot(L)
plt.show()

 