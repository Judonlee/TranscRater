#!Python NDCG for rankings

from __future__ import division

import sys
from sys import exit
import argparse
import math
import numpy as np

if sys.argv[1]:
  true_rank = sys.argv[1]
else:
  print "Error!!! Not defined inputs for ./bin/compute_NDCG.py ..."
  
if sys.argv[2]:
  pred_rank = sys.argv[2]
else:
  print "Error!!! Not defined inputs for ./bin/compute_NDCG.py ..."


true_rank_mat = np.nan_to_num(np.genfromtxt(true_rank, delimiter=' '))
pred_rank_mat = np.nan_to_num(np.genfromtxt(pred_rank, delimiter=' '))

if ( true_rank_mat.shape != pred_rank_mat.shape ):
  print "Error!!! Mismatch between True and Predicted ranking files shape"
  exit()



ndcg=[]

for k in range(true_rank_mat.shape[0]):
  trtmp = true_rank_mat.shape[1] - true_rank_mat[k][true_rank_mat[k].ravel().argsort()] + 1
  prtmp = true_rank_mat.shape[1] - pred_rank_mat[k][true_rank_mat[k].ravel().argsort()] + 1

  idcg = 0
  i=1
  for elem in trtmp:
    idcg += (math.pow(2,elem) - 1 ) / math.log(i+1,2)
    i+=1
    
  dcg = 0
  i=1
  for elem in prtmp:
    dcg += (math.pow(2,elem) - 1 ) / math.log(i+1,2)
    i+=1
  
#  print  (dcg / idcg)
  ndcg.append( dcg / idcg )
  
print "NDCG: %.3f" % np.mean(ndcg*100)




