#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 13:43:42 2018

@author: rvrikhye
"""
import numpy as np
import matplotlib.pyplot as plt
import sklearn.mixture as mix
np.random.seed(10)

def simpleaxis(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

from matplotlib.patches import Ellipse 

def draw_ellipse(position, covariance, ax=None, **kwargs):
    """Draw an ellipse with a given position and covariance"""
    
    # Convert covariance to principal axes
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
        width, height = 2 * np.sqrt(s)
    else:
        angle = 0
        width, height = 2 * np.sqrt(covariance)
        
    # Draw the Ellipse
    for nsig in range(1, 4):
        ax.add_patch(Ellipse(position, nsig * width, nsig * height, 
                            angle, **kwargs))
    
def plot_gmm(gmm, X, label=True, ax=None):
    
    fig, ax = plt.subplots(figsize=(9,7))      
    ax = ax or plt.gca()
    labels = gmm.fit(X).predict(X)
    
    if label:
        ax.scatter(X[:, 0], X[:, 1], c=labels, s=dot_size, cmap=cmap, zorder=2)
    else:
        ax.scatter(X[:, 0], X[:, 1], s=dot_size, zorder=2)
    simpleaxis(ax)
    
    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covariances_, gmm.weights_):
        print(pos)
        draw_ellipse(pos, covar, ax=ax, alpha=w * w_factor)

k = 2
n_draws = 600
sigma = .7
random_state = 0
dot_size = 50
cmap = 'viridis'
save = 1

from sklearn.datasets.samples_generator import make_blobs

X, y_true = make_blobs(n_samples = n_draws,
                       centers = k,
                       cluster_std = sigma,
                       random_state = random_state)

stretch = [[13,0], [0,1]]
X = X[:, ::-1]
X_stretched = np.dot(X, np.random.randn(2,2))

gmm = mix.GaussianMixture(n_components=k, random_state=random_state)
plot_gmm(gmm, X_stretched)
if save == 1:
    plt.savefig('fig2', format='eps', dpi=1000)


fig, ax = plt.subplots(figsize=(9,7))
ax.scatter(X_stretched[:, 0], X_stretched[:, 1], s=dot_size)
simpleaxis(ax)
if save == 1:
    plt.savefig('fig1', format='eps', dpi=1000)



