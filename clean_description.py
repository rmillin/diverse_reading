def clean_description(description):
    
    """
    This function will remove repeated sentences from a description.

    input: a description from "goodreads", consisting of a list of strings
    ouptut: the same description with repeated cells eliminated
    """
    if isinstance(description,list):
        ind2 = 0
        ind1=len(description)-1
        while ind1>=0 and ind2<len(description):
            while ind2<ind1:
                if description[ind2] in description[ind1]:
                    description.remove(description[ind2])
                    ind1-=1
                else:
                    ind2+=1
            ind1-=1
            ind2=0
    return description
