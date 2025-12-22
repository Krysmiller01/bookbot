# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

Project description: Bookbot was a minimally guided project that takes most of the fundamentals of learning python and creates a program that: grabs a *.txt file, reads the word count, turns all the characters into lowercase, creates a dictionary of key: character : number of instances used (e.g. e : 223 - in plain english: the letter e was used 223 times), converts the dictionary into a list of dictionaries, sorts them from highest instance to lowest, prints a report of the word count and the character count in highest to lowest instance - while keeping non-alpha characters out.

how to run it: python3 main.py books/frankenstein.txt 

Example output:
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1

Installation steps: 
1. Make sure you have python3 installed: 
  check with: python3 --version
  if not installed, use this to install: 
  sudo apt update
  sudo apt install -y python3
2. Clone the repository:
   git clone git@github.com:Krysmiller01/bookbot.git
3. Navigate into the directory:
   cd bookbot/bookbot
4. Run it:
   python3 main.py books/<your-book-here>

Dependencies:
I recommend utilizing bash with a linux OS, having python 3.10 or newer
