def row_insert(T,x,i=0):#x ist ein integer
    n=len(T)            #T ist als matrix eingegeben wobei die eintraege strings sind
    if i==n:
        T.append([x])
        return T
    if echt_grosser(T[i],x)==False:
        T[i].append(x)
        return T
    else:
        y=echt_grosser(T[i],x)
        T[i][y[0]]=x
        return row_insert(T,y[1],i+1)
        
        

def echt_grosser(l,x):#auch hier
    found=0
    for index in range(len(l)):
        if l[index]>x:
            return (index,l[index])
    return False

def word_list(youngtableau):#[1,2,5] als outputformat
    wordlist=[]
    for i in range(len(youngtableau)-1,-1,-1):
        wordlist+=youngtableau[i]
    return wordlist
        
    
def multi(S,T):#kommentar schreiben
    wordlist=word_list(T)
    result=S
    for i in wordlist:
        result=row_insert(result,i)
    return result




def K1(liste,index):

    n=len(liste)
    if n<3 or index>n-3:
        raise ValueError('K-operation impossible')
    else:
        if liste[index+2]<liste[index]<=liste[index+1]:
            liste[index+2],liste[index+1]=liste[index+1], liste[index+2]
            wort=[str(i) for i in liste]
            wort=' '.join(wort)
            return wort
        else:
            raise ValueError('K-operation impossible')

def K1_inv(liste,index):

    n=len(liste)
    if n<3 or index>n-3:
        raise ValueError('K-operation impossible')
    else:
        if liste[index+1]<liste[index]<=liste[index+2]:
            liste[index+2],liste[index+1]=liste[index+1],liste[index+2]
            wort=[str(i) for i in liste]
            wort=' '.join(wort)
            return wort
        else:
            raise ValueError('K-operation impossible')
            
def K2(liste,index):

    n=len(liste)
    if n<3 or index>n-3:
        raise ValueError('K-operation impossible')
    else:
        if liste[index]<liste[index+2]<=liste[index+1]:
            liste[index],liste[index+1]=liste[index+1],liste[index]
            wort=[str(i) for i in liste]
            wort=' '.join(wort)
            return wort
        else:
            raise ValueError('K-operation impossible')
            
def K2_inv(liste,index):

    n=len(liste)
    if n<3 or index>n-3:
        raise ValueError('K-operation impossible')
    else:
        if liste[index+1]<liste[index+2]<=liste[index]:
            liste[index],liste[index+1]=liste[index+1],liste[index]
            wort=[str(i) for i in liste]
            wort=' '.join(wort)
            return wort
        else:
            raise ValueError('K-operation impossible')



def multiply_words(word1,word2):
    if word1=='' or word2=='':
        return word1+''+word2
    else:    
        return word1+' '+word2



















