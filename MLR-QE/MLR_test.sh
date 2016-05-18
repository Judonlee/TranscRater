#!/bin/bash Test RR for CHiME3

testFile=$1
modelsdir=$2
outfile=$3

printf "\nTest \"$modelsdir\" on \"$testFile\"...\n"


# ----------------- Predict ranks
cat $testFile | cut -d' ' -f 1 > $BASEDIR/temp/MLR/test.label

java -jar  $RANKLIBDIR/RankLib-2.6.jar -load  $modelsdir/MLR.model -rank $testFile -norm zscore \
                                   -metric2T NDCG@${CHANNELS} -score  $BASEDIR/temp/MLR/Scores 2>&1 | grep WriteNothing

cat $BASEDIR/temp/MLR/Scores | awk '{printf("%.3f\n", $NF)}' > $outfile


# ----------------- Compute NDCG
python $BINDIR/bin/rank_array.py $BASEDIR/temp/MLR/test.label $CHANNELS $BASEDIR/temp/MLR/test.label.rank
python $BINDIR/bin/rank_array.py $outfile $CHANNELS ${outfile}.rank


python $BINDIR/bin/compute_NDCG.py  $BASEDIR/temp/MLR/test.label.rank ${outfile}.rank


