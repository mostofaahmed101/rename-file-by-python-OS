                            # this programme will rename all the specific extension file in numerically

import os

# note 
print("\n\n\t\t\t\t <--* HIGH RISK *-->\nNote : Use this file in the specific location where you want to Execute it.\n\n")

# take user input for file extinsion
ex = input("*which type of extension file you want to change --> ")

# start the rename function
def rename(ex):
    # get all file list in the specific directory
    allList = os.listdir()
    
    # filter the allList for extension and append in a new list 
    newList = []
    for i in allList:
        if i[-(len(ex)):]==ex:
            newList.append(i)

    # rename all the file that present in newList 
    for i in range(len(newList)):
        newName = str(i+1)
        newName = newName + '.' + ex
        os.rename(newList[i],newName)
    
    if __name__ == "__main__":
        print("Thanks for using it")

# call the rename function
if __name__ == "__main__":
    rename(ex)


