#/bin/bash run the QE process on multiple microphones


export BINDIR=`pwd`
export BASEDIR=`pwd`
export RANKLIBDIR=/home/jalalvand/Downloads in order to use MLR models you need to have RankLib library 

if [ ! -e $RANKLIBDIR/RankLib-2.6.jar ];then
  printf "ERROR!!! RankLib library not found in \"$RANKLIBDIR\"\n"
  return
fi

export CHANNELS=5  # Since there are 5 transcription channels in the data files


mkdir -p $BASEDIR/temp
mkdir -p $BASEDIR/temp/MLR


export MLR_Tune=No  # Set it to "Yes" if you want to optimize the parameters on Training set

# ./MLR_train.sh train_data  k-fold  models
. $BINDIR/MLR-QE/MLR_train.sh  $BASEDIR/data/MLR_train_LEX_LM_POS.data 5 MLR_models

# ./MLR_test.sh  test_data  models  output
. $BINDIR/MLR-QE/MLR_test.sh   $BASEDIR/data/MLR_test_LEX_LM_POS.data MLR_models $BASEDIR/data/MLR_output.prank



