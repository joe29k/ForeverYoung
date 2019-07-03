from ytmath import *
from words import *
from visual import *
import os
class youngtableau:
     pass
     def __init__(self,wort):
          self.wort=wort
          self.matrix=parse_word(wort)

     def __str__(self):
          return self.wort
     def row_insert(self,x):
         self.matrix=row_insert(self.matrix,x)
         wordlist=word_list(self.matrix)
         wordlist=[str(i) for i in wordlist]
         self.wort=' '.join(wordlist)
         return self
          
     def word(self): 
         return word(self.wort)

     def visual(self,boxlength,file):
         print_tex(self.matrix,boxlength)
         prevname='visual.tex'
         newname=file
         os.rename(prevname,newname)
         os.system("pdflatex {}".format(file)) 
     
        
def multiply(S,T):# die funktion bekommt als parameter 2 Youngtableau objekte und gibt das produkt als objekt der selben klasse zurueck.
    Produkt=multi(S.matrix,T.matrix)
    wordlist=[]
    for i in range(len(Produkt)-1,-1,-1):
        wordlist+=Produkt[i]
    wordlist=[str(i) for i in wordlist]    
    wort=' '.join(wordlist)
    Produkt=youngtableau(wort)
    return Produkt

def create_from(row,file):#es stellt ein youngtableau objekt aus der roe-ten Zeile in der Datei file.
    matrix=parse(row,file)
    wordlist=word_list(matrix)
    wordlist=[str(i) for i in wordlist]
    wort=' '.join(wordlist)
    T=youngtableau(wort)# T ist die resultierende Youngtableau
    return T

class word:
    pass 
    def __init__(self,wort):
        self.wort=wort
        liste=wort.split()
        liste=[int(i) for i in liste]
        self.liste=liste

    def K1(self,index):
        return K1(self.liste, index)

    def K1_inv(self,index):
        return K1_inv(self.liste, index)
        
    def K2(self,index):
        return K2(self.liste, index)
        
    def K2_inv(self,index):
        return K2_inv(self.liste, index)
        
    def multiply(self,other):
         result=word(self.wort+' '+other.wort)
         return result

    def youngtableau(self):
          try:
               matrix=parse_word(self.wort)
               T=youngtableau(self.wort)
               return T
          except ValueError:
              representer=youngtableau('')
              for i in self.liste:
                   representer.row_insert(i)
              return representer

          
def mult_classes(word1,word2):
     new_word=word(multiply_words(word1.wort,word2.wort))
     return word(new_word.youngtableau().wort)


def are_equiv(word1,word2):
     T1=word1.youngtableau()
     T2=word2.youngtableau()
     if T1.word==T2.word:
          return True
     return False
     
          
             
               




            
    
    
















          
     


