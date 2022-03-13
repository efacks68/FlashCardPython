#Flash Card app code.
#Imports spreadsheet into Dictionary and maps the words for each language
import numpy as np

#readcsv(filename,columns,datatype)
filename = "languages.csv"
data = np.genfromtxt(filename,delimiter=',',dtype="U30")
print(np.shape(data))

question1 = 'What is the word in ' + data[0,1] +'? '
question2 = 'What is the word in ' + data[0,2] +'? '
guess = 0
#While input is not a quit variable, print random index
while guess !='q':
  index = np.random.randint(0,len(data))
  print('The word in English is: ',data[index,0])
  guess = input(question1)
  if guess == 'q':
    break
  elif guess == data[index,1]:
    print('Great job! You are correct!')
  else:
    guess = input('Sorry, try again: ')
    if guess == 'q':
      break
    elif guess == data[index,1]:
      print('Great job! You are correct!')
      #continue
    else:
      print('Sorry, the correct word is: ',data[index,1],'. Next language!')
      #continue
    #continue
  #Now try Norwegian
  guess = input(question2)
  if guess == 'q':
    break
  elif guess == data[index,2]:
    print('Great job! You are correct!')
  else:
    guess = input('Sorry, try again: ')
    if guess == 'q':
      break
    elif guess == data[index,2]:
      print('Great job! You are correct!')
      #continue
    else:
      print('Sorry, the correct word is: ',data[index,2],'. Next word!')
      #continue

#Displays first language of word at random and creates buttons to display others

#loops back
