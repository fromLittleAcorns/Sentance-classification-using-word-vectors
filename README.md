# Sentance-classification-using-word-vectors
Sentance classification using Glove word vectors and Pytorch.  Relatively simple neural network at present

Notebook to look at a how to use a word vector approach to catagorise sentances.

This is to help with analysing and assessing transaction data from a company based upon the 
description of the transaction.

The approach is to use a pre-trained set of word vectors - in this case the GloVe set 6.B with each vector being of 
length 300.

In this analysis the approach is to define a fixed sentance length and pad sentances where they are less than this.

I have tried lengths of 5 to 10, and 6 or 7 seems to work best. At present I am padding the sentances in my routine, 
I intend to see how well the padding in the pytorch embedding layer works and whether this is any better since
I am not sure if the padding is having a detrimental effect upon the analysis.

After the embedding layer I am using a simple 3 level neural network, the first two layers with rectified linear and 
then finally a softmax output

The previous bag of words analysis achieved accuracy of 88.9% on training data but 66.2% on the test data using a simple 
bag of words approach.

The present analysis gives me 97% on the training data and 90% on the test data

An improvement I would like to try at some point is to use the natural language tool kit and 
stemmer from the nltk library, however, I think this model is fundamentally limited and so won't 
do so with this version

I also need to look at whether a CNN system works better but before that I think looking at the data more 
thoroughly is needed
