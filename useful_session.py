# coding: utf-8
import run_gravity as g 
import importlib
gravity = g.Gravity(10)
gravity 
g.system
gravity.system
gravity.metric
gravity.nodes
gravity.distance_matrix
gravity.nodes
gravity.A
gravity.B
import point_generator as pg
gravity.nodes
gravity.distance_matrix()
gravity.distance_matrix
gravity.system.distance_matrix
np.linspace(0, 100, node_number)
import numpy as np 
np.linspace(0, 100, node_number)
np.linspace(0, 100, 5)
np.linspace(0, 100, 6)
gravity.system.nodes
d = gravity.system.nodes
d 
freq, bins = np.histogram(d, np.arange(0,100))
freq
freq, bins = np.histogram(d, np.arange(0,5))
freq 
np.arange(0,5)
np.arange(0,100,3)
freq, bins = np.histogram(d, np.arange(0,100, 20))
freq
freq, bins = np.histogram(d, np.arange(0,120, 20))
freq
bins 
freq[0]
d 
bins = np.linspace(0,100, 6 )
bins 
a = np.digitize(d,bins)
a
a = np.digitize(d,bins, True)
a 
new_distances = []
a = np.digitize(d,bins, right = True)
a 
d
bins = np.linspace(0,101, 6)
bins 
a = np.digitize(d, bins, True)
a 
a = np.digitize(d, bins,False,  True)
a = np.digitize(d, bins, left = True)
a = np.digitize(d, bins, True)
a
a = np.digitize(d, bins, False)
a 
a[0]
range(len(d))
chl  = np.array([0.4,0.1,0.04,0.05,0.4,0.2,0.6,0.09,0.23,0.43,0.65,0.22,0.12,0.2,0.33])
depth = np.array([0.1,0.3,0.31,0.44,0.49,1.1,1.145,1.33,1.49,1.53,1.67,1.79,1.87,2.1,2.3])
bins = np.array([0,0.5,1.0,1.5,2.0,2.5])
A = np.vstack((np.digitize(depth, bins), chl)).T
a
A
bins = np.linspace(0,101, 6) 
a 
A = np.vstack((np.digitize(d, bins), d)).T
A
res_lst = [np.mean(A[A[:, 0] == i, 1]) for i in range(len(bins))]
res_lst = [np.average(A[A[:, 0] == i, 1]) for i in range(len(bins))]
res = {bins[int(i)]: np.mean(A[A[:, 0] == i, 1]) for i in np.unique(A[:, 0])}
res 
res = {np.mean(A[A[:, 0] == i, 1]) for i in np.unique(A[:, 0])}
res
res = np.array([np.mean(A[A[:, 0] == i, 1]) for i in np.unique(A[:, 0])])
res
A = np.vstack((np.digitize(depth, bins), chl))
A
A = np.vstack((np.digitize(d, bins), d))
A
A = np.vstack((np.digitize(d, bins), d)).T
A
res
