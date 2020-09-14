In [1]: #comment

In [2]: '''
   ...: this is a multi line comment
   ...: this is another line
   ...: and yet another
   ...: '''
Out[2]: '\nthis is a multi line comment\nthis is another line\nand yet another \n'

In [3]: rome_bell = "Rome Bell"

In [4]: print(rome_bell)
Rome Bell

In [5]: age =7

In [6]: print(age)
7

In [7]: isCool = True

In [8]: notCool = False

In [9]: print(isCool)
True

In [10]: this_is_none = None

In [11]: print(this_is_none
    ...: )
None

In [12]: True and False
Out[12]: False

In [13]: True or False
Out[13]: True

In [14]: True and "0"
Out[14]: '0'

In [15]: 2 ** 3
Out[15]: 8

In [16]: 2 8 2
  File "<ipython-input-16-9e12a9e618ec>", line 1
    2 8 2
      ^
SyntaxError: invalid syntax


In [17]: 2 * 2
Out[17]: 4

In [18]: rome_bell.split(" ")
Out[18]: ['Rome', 'Bell']

In [19]: rome_bell.index("m")
Out[19]: 2

In [20]: rome_bell.upper()
Out[20]: 'ROME BELL'

In [21]: rome_bell.replace("Rome", "Rob")
Out[21]: 'Rob Bell'

In [22]: rome_bell
Out[22]: 'Rome Bell'

In [23]: rob_bell = rome_bell.replace("Rome", "Rob")

In [24]: rob_bell
Out[24]: 'Rob Bell'

In [25]: rome_bell
Out[25]: 'Rome Bell'

In [26]: ace_of_spades = "Ace of Spades"

In [27]: "of" in ace_of_spades
Out[27]: True

In [28]: "out" in ace_of_spades
Out[28]: False

In [29]: "spades" in ace_of_spades
Out[29]: False

In [30]: len(ace_of_spades)
Out[30]: 13

In [31]: ace_of_spades[2]
Out[31]: 'e'

In [32]: ace_of_spades[2].upper()
Out[32]: 'E'

In [33]: ace_of_spades[-1]
Out[33]: 's'

In [34]: ace_of_spades[:2]
Out[34]: 'Ac'

In [35]: ace_of_spades[3:7]
Out[35]: ' of '

In [36]: ace_of_spades[::-1]
Out[36]: 'sedapS fo ecA'

In [37]: 19 % 5
Out[37]: 4

In [38]: not True
Out[38]: False

In [39]: not False
Out[39]: True

In [40]: not True and not 1
Out[40]: False

In [41]: not 1 or True
Out[41]: True

In [42]: 1 == 1
Out[42]: True

In [43]: 1 !== 1
  File "<ipython-input-43-276d466a9273>", line 1
    1 !== 1
        ^
SyntaxError: invalid syntax


In [44]: 1 != 1
Out[44]: False

In [45]: 1 === 1
  File "<ipython-input-45-284449d4984d>", line 1
    1 === 1
        ^
SyntaxError: invalid syntax


In [46]: nba_teams = ['Lakers', "Nuggets", "Celtics"]

In [47]: len(nba_teams)
Out[47]: 3

In [48]: nba_teams.append("Clippers")

In [49]: nba_teams
Out[49]: ['Lakers', 'Nuggets', 'Celtics', 'Clippers']

In [50]: len(nba_teams)
Out[50]: 4

In [51]: arr_of_numbers = [1] * 3

In [52]: arr_of_numbers
Out[52]: [1, 1, 1]

In [53]: nba_teams[3]
Out[53]: 'Clippers'

In [54]: one_through_ten = list(range(10))

In [55]: one_through_ten = list(range(10))

In [56]: one_through_ten
Out[56]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [57]: random-numbers = [9, 6, 8, 4, 6, 3, 2]
  File "<ipython-input-57-37a65576c0e3>", line 1
    random-numbers = [9, 6, 8, 4, 6, 3, 2]
    ^
SyntaxError: cannot assign to operator


In [58]: random_numbers = [9, 6, 8, 4, 6, 3, 2]

In [59]: random_numbers.sort()

In [60]: random_numbers
Out[60]: [2, 3, 4, 6, 6, 8, 9]

In [61]: random_numbers[::-1]
Out[61]: [9, 8, 6, 6, 4, 3, 2]

In [62]: random_numbers[::-1]
Out[62]: [9, 8, 6, 6, 4, 3, 2]

In [63]: random_numbers
Out[63]: [2, 3, 4, 6, 6, 8, 9]

In [64]: random_numbers.pop()
Out[64]: 9

In [65]: random_numbers
Out[65]: [2, 3, 4, 6, 6, 8]

In [66]: random_numbers.pop(2)
Out[66]: 4

In [67]: random_numbers
Out[67]: [2, 3, 6, 6, 8]

In [68]: print(random_numbers)
[2, 3, 6, 6, 8]

In [69]: list
Out[69]: list

In [70]: help
Out[70]: Type help() for interactive help, or help(object) for help about object.

In [71]: help(nba_teams)


In [72]:

In [72]: dog ={
    ...: "name": "Rocco",
    ...: "age" : "7",
    ...: "location" : "Los Angeles"
    ...: }

In [73]: dog["name"]
Out[73]: 'Rocco'

In [74]: dog["sleep_alot"] = True

In [75]: dog
Out[75]: {'name': 'Rocco', 'age': '7', 'location': 'Los Angeles', 'sleep_alot': True}

In [76]: int("5")
Out[76]: 5

In [77]: str(5)
Out[77]: '5'

In [78]: float(99)
Out[78]: 99.0

In [79]: bool("Rome")
Out[79]: True

In [80]: bool(0)
Out[80]: False

In [81]: my_message = f"{dog["name"]} lives in {dog["location"].}"
  File "<ipython-input-81-44d01305717f>", line 1
    my_message = f"{dog["name"]} lives in {dog["location"].}"
                         ^
SyntaxError: invalid syntax


In [82]: my_message = f"{dog['name']} lives in {dog['location'].}"
  File "<fstring>", line 1
    (dog['location'].)
                     ^
SyntaxError: unexpected EOF while parsing


In [83]: my_message = f"{dog['name']} lives in {dog['location']}"

In [84]: my_message
Out[84]: 'Rocco lives in Los Angeles'

In [85]: another_message = f" I predict the {nba_teams[0]} to win it all."

In [86]: another_message
Out[86]: ' I predict the Lakers to win it all.'

In [87]: "I predict the {} to win it all".format(nba_teams[0])
Out[87]: 'I predict the Lakers to win it all'

In [88]: "I predict the {} to win it all".format(nba_teams[0])
Out[88]: 'I predict the Lakers to win it all'

In [89]: def add_numbers(num1, num2):
    ...:     result = num1 + num2
    ...:     return result
    ...:

In [90]: 1, 2
Out[90]: (1, 2)

In [91]: add_numbers(1, 3)
Out[91]: 4

In [92]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

In [93]: def legal_age(age):
    ...:     if (age < 21):
    ...:         return "Sorry youre too young."
    ...:

In [94]: def legal_age(age):
    ...:     if (age < 21):
    ...:         return "Sorry youre too young."
    ...:     elif(age == 21);
  File "<ipython-input-94-a250a1066ecb>", line 4
    elif(age == 21);
                   ^
SyntaxError: invalid syntax


In [95]: def legal_age(age):
    ...:     if (age < 21):
    ...:         return "Sorry youre too young."
    ...:     elif(age == 21):
    ...:         return "youre an adult"
    ...:     else:
    ...:         return "youre free to pass, enjoy"
    ...:

In [96]: legal_age(19)
Out[96]: 'Sorry youre too young.'

In [97]: legal_age(27)
Out[97]: 'youre free to pass, enjoy'

In [98]: legal_age(21)
Out[98]: 'youre an adult'

In [99]: def the_spot(vip, food_place, location="Bay Area")
  File "<ipython-input-99-05c7a33a489c>", line 1
    def the_spot(vip, food_place, location="Bay Area")
                                                      ^
SyntaxError: invalid syntax


In [100]: def the_spot(vip, food_place, location="Bay Area"):
     ...:     if(food_place == "full" and not vip)
  File "<ipython-input-100-e4c3e5c79b29>", line 2
    if(food_place == "full" and not vip)
                                        ^
SyntaxError: invalid syntax


In [101]: vip = True

In [102]: food_place = "busy"

In [103]: number = 0

In [104]: while number < 10:
     ...:     number++
  File "<ipython-input-104-56723548440e>", line 2
    number++
            ^
SyntaxError: invalid syntax


In [105]: while number < 10:
     ...:     number+
  File "<ipython-input-105-8bbfc25e12aa>", line 2
    number+
           ^
SyntaxError: invalid syntax


In [106]: while number < 10:
     ...:     number ++
  File "<ipython-input-106-ef99a883f77f>", line 2
    number ++
             ^
SyntaxError: invalid syntax


In [107]: while number < 10:
     ...:     (number++)
  File "<ipython-input-107-8312f5709bdf>", line 2
    (number++)
             ^
SyntaxError: invalid syntax


In [108]: while number < 10:
     ...:     number +=
  File "<ipython-input-108-1270339dcb30>", line 2
    number +=
             ^
SyntaxError: invalid syntax


In [109]: while number < 10:
     ...:     print(number)
     ...:     number += 1
     ...:
     ...:
0
1
2
3
4
5
6
7
8
9

In [110]: for i in range(0,15):
     ...:     print(i)
     ...:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14

In [111]: nba_teams
Out[111]: ['Lakers', 'Nuggets', 'Celtics', 'Clippers']

In [112]: for team in range(len(nba_teams))
  File "<ipython-input-112-b3fe659ea4f1>", line 1
    for team in range(len(nba_teams))
                                     ^
SyntaxError: invalid syntax


In [113]: for i in range(len(nba_teams)):
     ...:     each_team = nba_teams[i]
     ...:     print(each_team)
     ...:
Lakers
Nuggets
Celtics
Clippers

In [114]: teams  = ("Patriots", "Dolphins", "Bears", "Falcons")

In [115]: teams
Out[115]: ('Patriots', 'Dolphins', 'Bears', 'Falcons')

In [116]: teams[0] = "Bananas"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-116-87baf2ed0a36> in <module>
----> 1 teams[0] = "Bananas"

TypeError: 'tuple' object does not support item assignment

In [117]: new_englas, miami, atlanta = teams
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-117-fcbe7c2f42a6> in <module>
----> 1 new_englas, miami, atlanta = teams

ValueError: too many values to unpack (expected 3)

In [118]: new_england, miami, atlanta = teams
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-118-faed21902d7a> in <module>
----> 1 new_england, miami, atlanta = teams

ValueError: too many values to unpack (expected 3)

In [119]: new_england, miami, atlanta, aruba  = teams

In [120]:  teams
Out[120]: ('Patriots', 'Dolphins', 'Bears', 'Falcons')

In [121]: new_england
Out[121]: 'Patriots'

In [122]: aruba
Out[122]: 'Falcons'

In [123]: sales_tax = (0.13, 0.11, 0.08)

In [124]: california, illinois, alabama = sales_tax

In [125]: california
Out[125]: 0.13

In [126]: