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

The present analysis gives me 88% on the test data, with 98.6% correct within the first three choices of the 13 catagories

The results on the validation data give me 92%, which is slightly better than the training data hence I feel I have not suffered from a variance problem

One of the issues I have seen with the data is that there is not an even spread across catagories, some have very few examples and hence tend to get poor prediction.  Across the major catagories the prediction is pretty good at 98% for the largets catagory and 93% for the next largest.

I have used a simplified version of the Pytorch dataset and dataiterator since I could not get the ones provided to work in this case.
