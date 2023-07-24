import Levenshtein
import pandas as pd
from itertools import product

class spellChecker:
    
    def __init__(self,path):
        self.content=pd.DataFrame()
        self.read_content(path)
        

    def read_content(self,path):
        with open(path,'r', encoding='latin-1') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        self.content=pd.DataFrame(content,columns=['word'])
        

    def checkIfExist(self,word):
        if word in self.content['word'].values:
            return True
        else:
            return False
    def generate_combinations(self,combination_length):
        """
        This function takes a number and generate all possible combinations of the alphabet with this length
        Time complexity is O(m!) where m is the number of the combinations
        """
        characters = 'abcdefghijklmnopqrstuvwxyz'
        combinations = [''.join(combo) for combo in product(characters, repeat=combination_length)]
        return combinations
    #Suppose length of the dictionary is m and the lenght of the input word is n
    # the time complexity of this function is O(n*m+m+ m log m) which is O(n*m)
    # The space complexity is O(m)     
    def getNearst4Words(self,input_word):
        """
        This function takes a word and return the 4 nearest words to it
        by looking for the most similar words to it in the dictionary
        
        """
        # hello
        # hella
        # hellb
        #  

        self.highPriority = pd.DataFrame()
        self.lookFor=self.content
        for (i,char) in enumerate(input_word):
            self.prob=self.lookFor[self.lookFor['word'].str[0:i]==input_word[0:i]]
            self.nxt=len(self.prob)
            if(self.nxt==0):
                subset=input_word[0:i-1]
                cur=i
                while (len(self.highPriority)<4)and i>0:
                    i-=1
                    #here we are looking for the words that have the same prefix as the input word and go backward
                    self.highPriority=self.content[self.content['word'].str[0:i]==input_word[0:i]]
                break
            else:
                self.highPriority=self.prob
                self.lookFor=self.prob
        return self.highPriority.sort_values(by=['word'])[0:4].values[:,0]
    def doWork(self,word):
        if self.checkIfExist(word):
            return "The Word Exist"
        else:
            return self.getNearst4Words(word)
    #The time complexity of this function is O(m) where m is the number of columns of teh Data Frame
    #So for each addWord operation the time complexity is O(1) 
    #The space complexity is O(m) where m is the number of columns of teh Data Frame
    def addWord(self,word):
        if self.checkIfExist(word):
            return False
        else:
            self.content[word].append(word)
            return True
