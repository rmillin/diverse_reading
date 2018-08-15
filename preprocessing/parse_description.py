def standardize_description(data):

    """
    This function will remove repeated sentences from the description, remove
    punctuation, parse into words, remove stopwords, and lemmatize the remaining
    words.

    input: a dataframe with a "description" column"
    ouptut: the same dataframe with the cleaned descriptions

    """

    import pandas as pd
    from clean_description import clean_description

    # clean the summaries
    data['description'] = data['description'].apply(clean_description)
    
    # flatten summary lists into strings
    data['description'] = data['description'].apply(lambda x: "".join(x) if isinstance(x,list) else str(x))

    return data
    

def lemmatize_description(data)

    import nltk
    import re
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer

    def tokenize_text(word_tokens):
        return [w for w in word_tokens if not w in stop_words]    

    def lemmatize_text(word_tokens):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(w) for w in word_tokens]

    stop_words = set(stopwords.words('english'))

    # convert to lower case
    data['description'] = data['description'].apply(lambda x:x.lower())
    print(data.loc[0,'description'])

    # eliminate numbers
    data['description'] = data['description'].apply(lambda x:re.sub("[\d]", " ",  x))
    print(data.loc[0,'description'])

    # tokenize
    data['description'] = data['description'].apply(lambda x:re.sub("[^\w]", " ",  x).split())
    print(data.loc[0,'description'])

    # remove stopwords
    data['description'] = data['description'].apply(lambda x:tokenize_text(x))
    print(data.loc[0,'description'])

    # lemmatize
    data['description'] = data['description'].apply(lambda x:lemmatize_text(x))

    return data

