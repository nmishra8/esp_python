#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 17:12:45 2016

@author: nmishra
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from sklearn.metrics import r2_score
from sklearn.linear_model import ElasticNet

###############################################################################
alpha = 0.1
k = 2;
mat_contents = sio.loadmat('../tmp/dat-multi-'+str(k)+'.mat');
oct_struct = mat_contents['dat']
X ,Y = oct_struct['xx'], oct_struct['yy']; X, Y = X[0,0], Y[0,0];

n = len(Y)
###############################################################################
# remove NaN
remove_ind = np.where(np.sum(Y,1) <= 10**(-3));
Y = np.delete(Y,remove_ind,0);
X = np.delete(X,list(remove_ind)+[x + len(Y) for x in remove_ind],0);

indices = np.random.permutation(len(Y))
n_samples = len(Y)/2

train_idx_y, test_idx_y = indices[:n_samples] , indices[n_samples:]
train_idx_x = list(train_idx_y)+[x + len(Y) for x in train_idx_y];
test_idx_x     = list(test_idx_y)+[x + len(Y) for x in test_idx_y];

y_train, y_test = Y[train_idx_y,:], Y[test_idx_y,:]
X_train, X_test = X[train_idx_x,:], X[test_idx_x,:]

enet = ElasticNet(alpha=alpha, l1_ratio=0.7)

y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)