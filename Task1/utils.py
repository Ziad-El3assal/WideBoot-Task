import heapq
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
        self.content=list(self.content['word'])
        

    def checkIfExist(self,word):
        if word in self.content:
            return True
        else:
            return False


    def find_closest_strings_indices(self, input_string):
        def longest_common_prefix(str1, str2):
            length = min(len(str1), len(str2))
            common_prefix = ""
            for i in range(length):
                if str1[i] != str2[i]:
                    break
                common_prefix += str1[i]
            return common_prefix

        def binary_search_closest( target, heap):
            left, right = 0, len(self.content) - 1

            while left <= right:
                mid = (left + right) // 2
                current_word = self.content[mid]
                common_prefix = longest_common_prefix(current_word, target)

                if len(heap) < 4:
                    heapq.heappush(heap, (len(common_prefix), mid))
                else:
                    heapq.heappushpop(heap, (len(common_prefix), mid))

                if target < current_word:
                    right = mid - 1
                else:
                    left = mid + 1

        # Sort the words list to enable binary search
        self.content.sort()

        # Create a max-heap (min-heap with negated values) to track top 4 similarities
        top_similarities = []

        # Perform binary search to find top 4 similar words
        binary_search_closest( input_string, top_similarities)

        # Retrieve the indices of the top 4 similar words
        top4SimilarWords = [self.content[index] for _, index in top_similarities]

        return top4SimilarWords
    def doWork(self,word):
        if self.checkIfExist(word):
            return "The Word Exist"
        else:
            return self.find_closest_strings_indices(word)
    #The time complexity of this function is O(m) where m is the number of columns of teh Data Frame
    #So for each addWord operation the time complexity is O(1) 
    #The space complexity is O(m) where m is the number of columns of teh Data Frame
    def addWord(self,word):
        if self.checkIfExist(word):
            return False
        else:
            self.content.append(word)
            return True
