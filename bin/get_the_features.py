#!/usr/bin/env python Extracts the features
# egs:
# python get_the_features ( "train" )
# python get_the_features ( "test" )

import sys
import numpy as np

from __main__ import *


def main ( setname ):

  # set data size
  if setname == "train":
    global data_size 
    data_size = sum(1 for line in open(trainREF))
  else:
    global data_size 
    data_size = sum(1 for line in open(testREF))
    

  # Compute WER scores and Ranks  
  import get_WER_scores
  get_WER_scores.main( setname , data_size )


  # Extract Signal features
  if "SIG" in FEAT:
    import get_SIG_features
    get_SIG_features.main( setname )
      
  # Extract Lexical features
  if "LEX" in  FEAT:
    import get_LEX_features
    get_LEX_features.main( setname )

  # Extract Language Model features
  if "LM" in FEAT:
    import get_LM_features
    get_LM_features.main( setname )

  # Extract Part-of-Speech tag features
  if "POS" in FEAT:
    import get_POS_features
    get_POS_features.main( setname )

  # Use the User Defined features
  if "UDF" in FEAT:
    import get_UDF_features
    get_UDF_features.main( setname )
  #    ....

  
  # Accumulate the Extracted features for each Channel of transcription
  if '_' in FEAT:  # if different types of features are asked
  
    for ch in range(CHANNELS):
    
      feat_array = np.array([])
      for feat in FEAT.split('_'):
        tmparr = np.nan_to_num(np.genfromtxt("data/features/"+setname+"_CH_"+str(ch+1)+"_"+feat+".feat",delimiter=' '))
        if (feat_array.size == 0):
          feat_array = tmparr
        else:
          feat_array = np.column_stack ( [ feat_array , tmparr ] )
     
      np.savetxt( BASEDIR+"/data/features/"+setname+"_CH_"+str(ch+1)+"_"+FEAT+".feat", feat_array , fmt='%.4f') 
    

if __name__=='__main__':
  sys.exit(main(sys.argv[1]))
      
  
    
    
  
  

