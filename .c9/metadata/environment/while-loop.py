{"filter":false,"title":"while-loop.py","tooltip":"/while-loop.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":86},"action":"insert","lines":["print(\"Welcome to Guess the Number!\")","print(\"The rules are simple. I will think of a number, and you will try to guess it.\")"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":13},"action":"insert","lines":["import random"],"id":3}],[{"start":{"row":3,"column":86},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":29},"action":"insert","lines":["number = random.randint(1,10)"],"id":5}],[{"start":{"row":4,"column":29},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":20},"action":"insert","lines":["isGuessRight = False"],"id":7}],[{"start":{"row":5,"column":20},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":13,"column":79},"action":"insert","lines":["while isGuessRight != True:","    guess = input(\"Guess a number between 1 and 10: \")","    if int(guess) == number:","        print(\"You guessed {}. That is correct! You win!\".format(guess))","        isGuessRight = True","    else:","        print(\"You guessed {}. Sorry, that isn’t it. Try again.\".format(guess))"],"id":9}],[{"start":{"row":9,"column":12},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":79},"end":{"row":13,"column":79},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1688654168466,"hash":"f5a7369e65563c5e5d27e305392bae0891560bc8"}