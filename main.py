import random
from termcolor import colored
import numpy as np
from collections import Counter
import datetime
import warnings
import sys

def isogram(word):
  word = list(word)
  return len(set(word)) == len(word)

def play_dordle(solution):
  guesses = 0
  solved = [False] * len(solution)
  while guesses < (6 + len(solution) - 5):
    guess = input(f'Guess #{guesses + 1}?\n')
    if len(guess) != 5 or str(guess) not in words:
      print('not in word list, try again')
      continue
    else:
      guesses += 1
    guess = list(zip(list(guess), [None] * len(guess)))
    evaluation = [[]] * len(solution)
    for i, soln in enumerate(solution):
      if solved[i]:
        for letter in list(soln):
          print(c(letter, "cyan"))
        continue
      for index, letter in enumerate([i[0] for i in guess]):
        count = Counter(soln)
        if count[letter] > 0 and (index == soln.index(letter) or index == soln.rindex(letter)):
          evaluation[i].append([letter, "green"])
        elif count[letter] > 0:
          if count[letter] == 1 and letter in [j[0] for j in evaluation[i]]:
            evaluation[i].append([letter, "red"])
          else:
            evaluation[i].append([letter, "yellow"])
        else:
          evaluation[i].append([letter, "red"])
    
    c = colored
    for i, soln in enumerate(evaluation):
      for letter in soln:
        print(c(*letter))
      print()

    guess = [i[0] for i in guess]
    print(guess, [list(i) for i in solution])
    solved = [guess == solution[i] for i in range(len(solution))]

    print(solved)
    if sum(solved) == len(solved):
      print(c(f'Solved! {solution}', "blue"))
      return

  print(c(f'The solution was {solution[0]} & {solution[1]}. Better luck next time!', "magenta"))

if __name__=='__main__':
  warnings.filterwarnings("ignore")
  with open('words.txt', 'r') as f:
    global words
    words = f.readlines()

  words = [word[:-1] for word in words]
  # print(words[:100], len(words))
  day = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days

  n = int(input("How many simultaneous words? 1 for wordle, 2 for dordle, 4 for quordle, etc. \n"))

  solution = []
  for i in range(n):
    solution.append(words[round(day + np.exp(i) * 10 + np.random.random() * len(words)) % len(words)])
  
  solution = random.choices(words)[0], random.choices(words)[0]
  play_dordle(solution)