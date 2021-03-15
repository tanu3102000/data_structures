def anagram(A):#A is array in which we are searching for anagrams
    if(A==None):
        return
    else:
        dict1={}
        for i in range(len(A)):
            word=''.join(sorted(A[i]))#After sorting the letters of word,convert it into string
            if(word not in dict1):
                dict[word]=[i+1]
            else:
                dict[word].append(i + 1)
        return dict

A=['cat','dog','tca','god','act']
print(anagram(A))