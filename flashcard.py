#Flash Card app code.
#Imports spreadsheet into Dictionary and maps the words for each language
import numpy as np

#readcsv(filename,columns,datatype)
filename = "languages.csv"
data = np.genfromtxt(filename,delimiter=',',dtype="U20")
print(data)


#Randomly selects line and stores the words into output variables

#Displays first language of word at random and creates buttons to display others

#loops back
