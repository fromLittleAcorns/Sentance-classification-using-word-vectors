import re

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        #print s
        return False

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    #string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"[^A-Za-z0-9?\'\`]", " ", string)
    # matches any single character not in the above list and replaces with a white space
    string = re.sub(r"\'s", " \'s", string)
    # adds a space prior to '\apostrophy with an s
    string = re.sub(r"\'ve", " \'ve", string)
    # adds a space before apostrphy with ve
    string = re.sub(r"n\'t", " n\'t", string)
    # as above but for a 't
    string = re.sub(r"\'re", " \'re", string)
    # as above but with 're
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    # not sure why this is necessary since I have not seen this option before
    string = re.sub(r",", " , ", string)
    # adds space before and after commas
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " ( ", string)
    # adds spaces before and after the brackets
    string = re.sub(r"\)", " ) ", string)
    string = re.sub(r"\?", " ? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    # replaces multiple white space sections with single whitespace
    return string.strip().lower()

def rem_numbers(string):
    string=re.sub(r"[0123456789]","",string)
    string = re.sub(r"\s{2,}", " ", string)
    string=string.strip()
    return string

def remove_stop_words(sentance, stop_list):
    filtered = [word for word in sentance if word not in stop_list] 
    return filtered

def replace_similar_words(sentance, replace_list):
    new_sentance=[]
    for word in sentance:
        if word in replace_list:
            word=replace_list[word]
        new_sentance.append(word)
    return new_sentance

def build_vocab(sentences):
    """
    Builds a vocabulary mapping from word to index based on the sentences.
    Returns vocabulary mapping and inverse vocabulary mapping.
    """
    # Build vocabulary
    word_counts = Counter(itertools.chain(*sentences))
    # Mapping from index to word
    vocabulary_inv = [x[0] for x in word_counts.most_common()]
    # Mapping from word to index
    vocabulary = {x: i for i, x in enumerate(vocabulary_inv)}
    return [vocabulary, vocabulary_inv]