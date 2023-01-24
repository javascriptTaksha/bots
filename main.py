import webbot
import os
import sys
import time
import random
os.system('pip3 install pyautogui')
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
driver = webbot.Browser()

driver.go_to('https://quizizz.com/join')
code = input("The game id: ")
bots = int(input("Enter the amount of bots you want (Only 1 to 15): "))
while True:
  if bots >= 16:
    print ("Please only 1 to 15 bots!")
    time.sleep(1)
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    bots = int(input("Enter the amount of bot you want (Only 1 to 15): "))
  else:
    if bots <= 15:
      break
bot = bots - 1
tab = 1
botall = bots
botconect = 0
for i in range(0,bot):
  time.sleep(2)
  input_elements = driver.find_elements(xpath='//input')
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(code)
  driver.type(driver.Key.ENTER,into=input_elements[0].text)
  time.sleep(2)
  discname1 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spooky', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'bro', 'droopy', 'why', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy', ]
  noun = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous']
  discname2 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spoopy', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy',]
  noun2 = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous',]
  rand1 = random.choice(discname1)
  rand2 = random.choice(noun)
  username = (random.choice(discname2) + ' ' + random.choice(discname1) + ' ' + random.choice(noun) + ' ' + random.choice(noun2))
  time.sleep(5)
  input_elements = driver.find_elements(xpath='//input')
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(driver.Key.TAB,into=input_elements[0].text)
  driver.type(username)
  driver.type(driver.Key.ENTER,into=input_elements[0].text)
  time.sleep(1)
  botconect = botconect + 1
  time.sleep(1)
  driver.execute_script("window.open(' joinmyquiz.com');")


  tab = tab + 1
  driver.switch_to_tab(tab)
  time.sleep(2)
time.sleep(5)
input_elements = driver.find_elements(xpath='//input')
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(code)
driver.type(driver.Key.ENTER,into=input_elements[0].text)
time.sleep(2)
discname1 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spooky', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy', ]
noun = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous']
discname2 = ['saucy', 'momma', 'mecha', 'earth', 'barbed', 'prehistoric', 'old','cosmic', 'metallic', 'neat', 'supa', 'haunted', 'ruthless', 'clueless', 'rough', 'killer', 'spoopy', 'retro', 'ancient', 'strange', 'astro', 'baren', 'burned', 'chared', 'crap', 'cranky', 'crummy', 'croaked', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'drowned', 'enraged', 'angry', 'good', 'garnished', 'groaning', 'happy', 'hopeful', 'graceful', 'gentle', 'hairy', 'inteligent', 'intergallactic', 'jelly filled', 'jumping', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'nocternal', 'artifcial', 'perfect', 'quirky', 'petty', 'rocky', 'sad', 'sorrowful', 'useless', 'sickly', 'unbeatable', 'zesty', 'acrobatic', 'buttered', 'burpy',]
noun2 = ['chair', 'tortoise', 'fruit', 'paper', 'gecko', 'giraffe', 'mountain', 'boy', 'urinal', 'pencil','toenail', 'pug', 'wrangler', 'garbage', 'tugboat', 'bladder', 'viper', 'chicken', 'gnome', 'slayer', 'apple', 'artichoke', 'butter', 'bladder', 'cat', 'coop', 'carp', 'dome', 'door', 'horse', 'dart', 'fart', 'farie', 'garlic', 'goop', 'gunk', 'guild', 'hoop', 'harp', 'handle', 'house', 'cow', 'cake', 'cookie', 'largo', 'armor', 'bow', 'map', 'mayonaise', 'egg', 'napkin', 'octopus', 'park', 'pancake', 'punk', 'queen', 'rock', 'salmon', 'sock', 'syrup', 'tophat', 'viking', 'hipopotomous',]
rand1 = random.choice(discname1)
rand2 = random.choice(noun)
username = (random.choice(discname2) + ' ' + random.choice(discname1) + ' ' + random.choice(noun) + ' ' + random.choice(noun2))
time.sleep(1)
input_elements = driver.find_elements(xpath='//input')
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(driver.Key.TAB,into=input_elements[0].text)
driver.type(username)
driver.type(driver.Key.ENTER,into=input_elements[0].text)
time.sleep(1)
botconect = botconect + 1
print (botconect ,"out of", bots ,"bots connected successfully")
tab = 0
timerun = 0
