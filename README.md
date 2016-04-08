# TranscRater: Transcription Rating Toolkit
An open-source tool for  automatic speech recognition (ASR) quality estimation (QE)

#### Description
This package contains two main modules: feature extraction and QE purpose machine learning. 

#### Requirements
The requirments for machine learning module:
- Linux OS
- "Python" > v2.7
- "SciPy" 
- "sklearn" python library
- java > v1.8
- "RankLib" > v2.6

The requirments for feature extraction:
- "OpenSmile" signal processing toolkit
- "RNNLM" recurrent neural network language model toolkit
- "SRILM" n-gram language model toolkit
- "TreeTagger" part-of-speech tagging toolkit

#### Installation:
The toolkit by itself does not need any installation nor complie. The user needs to download and compile the requirments and Modify the following environment variables at the top of the configuration file:
-OPENSMILEDIR= the directory of OpenSmile lib
-RNNLMDIR= the directory of RNNLM
-SRILMDIR= the directory of SRILM
-TREETAGDIR= the directory of TreeTagger
-RANKLIBDIR= the directory of RankLib

#### Usage:
To see the first output of the system with regression models, in the root directory of the package, run the following command:
. fast_run_RR.sh

This script will:
1) use the data "./data/RR_train_LEX_LM_POS.data" to train a regression (RR) model,
2) save it into "./RR_Models/"
3) show mean absolute error (MAE) and normalized discounted cumulative gain (NDCG) on the training data
4) use the trained model to predict the WER of the "./data/RR_test_LEX_LM_POS.data"
5) save the predicted WER on "./data/RR_output.pwer" and the predicted ranks on "data/RR_output.pwer.rank"
6) show MAE and NDCG on the test data

To see the first output of the system with machine-learned ranking (MLR) models, in the root directory of the package, run the following command:
. fast_run_MLR.sh

This script will:
1) use the data "./data/MLR_train_LEX_LM_POS.data" to train a regression model,
2) save it into "./MLR_Models/"
3) show NDCG on the training data
4) use the trained model to predict the ranks on "./data/MLR_test_LEX_LM_POS.data"
5) save the predicted ranks on "data/MLR_output.prank.rank"
6) show NDCG on the test data

For a complete process on a real data set, starting from transcripts and feature extraction please go to "./egs/CHiME3/" directory where we use the data this corpora to train and test the ASR QE models. 





