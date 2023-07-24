import utils
    
def main():
    Dict=utils.spellChecker('D:\\UPWork\\WideBot\\Task1\\dictionary.txt')
    while True:
        print("1","Search for a word")
        print("2","Add a word")
        print("3","Exit")
        choice=input("Enter your choice: ")
        if(choice=='1'):
            word=input("Enter the word: ")
            print(Dict.doWork(word))
        elif(choice=='2'):
            word=input("Enter the word: ")
        
            if(Dict.addWord(word)):
                print("The word has been added")
            else:
                print("The word already exist")
        elif(choice=='3'):
            break
        else:
            print("Wrong choice")
main()