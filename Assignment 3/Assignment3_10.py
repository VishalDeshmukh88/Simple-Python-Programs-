def long_words(n ,str):
    output_list=[]
    txt=str.split()
    for x in txt:
        if len(x)>n:
            output_list.append(x)
    return output_list
    
long_words(4,"This is hello world")