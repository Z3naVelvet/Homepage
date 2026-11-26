# Welcome to my Github!


## My info:

### My name is: 
## ![Asmara](https://img.shields.io/badge/Asmara-purple)
#### I'm a beginner coder and often share my stuff here!
#### I only have 2 big projects rn

## My socials:

[Discord]()

[Youtube]()

![Alt text](https://avatars.githubusercontent.com/u/189638603?v=4)

## My projects:

[Big Lyrics](https://github.com/Z3naVelvet/Big-Lyrics)

[OCDex](https://github.com/Z3naVelvet/OCDex)

## My code:

### Personal:

Random password:
```python
import random

def generate_random_password() -> str:
    """Generate a random password with ASCII characters 33–126."""
    passwordlist = []
    countmax = random.randint(7, 20)  # Password length between 7 and 10
    for _ in range(countmax):
        character = random.randint(33, 126)  # Printable ASCII range
        passwordlist.append(chr(character))
    return "".join(passwordlist)

if __name__ == "__main__":
    password = generate_random_password()  # Store password in a variable
    print(password)

    forwhat = input("For what is the password: ")

    # Use raw string to avoid Windows path escape issues
    file_path = r"C:\\Users\\aidan\\Downloads\\Code\\password generator\\passwords.txt"

    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            # Use f-string to insert variables and add newline
            file.write(f"{forwhat}: {password}\n")
        print(f"Password saved to {file_path}")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: No permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

### Jokes and tests:

functest:

```python
import os

import random

import subprocess

import time

from colorama import Fore, Back, Style

import sys

from letters import letters

def text_to_big(name):
    result = [''] * 5
    for char in name.upper():
        if char == ' ':
            for i in range(5):
                result[i] += '    '
        elif char in letters:
            letter = letters[char].splitlines()
            for i in range(5):
                result[i] += letter[i] + ' '
        else:
            print(f"Can't convert char [{char}]")
            return None
    return '\n'.join(result)

def printart(txtfile):
    with open(os.path.join(sys.path[0],f'Ascii art for Quest of the Elixer\\{txtfile}.txt')) as file:
        print(file.read())

def battletest(enemy):
    enemyhealth = 100
    health = 100
    while health > 0:
        if 90 < health <= 100:
            print('Player health:')
            print('(█|█|█|█|█|█|█|█|█|█)')
        elif 80 < health <= 90:
            print('Player health:')
            print('(█|█|█|█|█|█|█|█|█  )')
        elif 70 < health <= 80:
            print('Player health:')
            print('(█|█|█|█|█|█|█|█    )')
        elif 60 < health <= 70:
            print('Player health:')
            print('(█|█|█|█|█|█|█      )')
        elif 50 < health <= 60:
            print('Player health:')
            print('(█|█|█|█|█|█        )')
        elif 40 < health <= 50:
            print('Player health:')
            print('(█|█|█|█|█          )')
        elif 30 < health <= 40:
            print('Player health:')
            print('(█|█|█|█            )')
        elif 20 < health <= 30:
            print('Player health:')
            print('(█|█|█              )')
        elif 10 < health <= 20:
            print('Player health:')
            print('(█|█                )')
        elif 0 < health <= 10:
            print('Player health:')
            print('(█                  )')
        if 90 < enemyhealth <= 100:
            print('Enemy health:')
            print('(█|█|█|█|█|█|█|█|█|█)')
        elif 80 < enemyhealth <= 90:
            print('Enemy health:')
            print('(█|█|█|█|█|█|█|█|█  )')
        elif 70 < enemyhealth <= 80:
            print('Enemy health:')
            print('(█|█|█|█|█|█|█|█    )')
        elif 60 < enemyhealth <= 70:
            print('Enemy health:')
            print('(█|█|█|█|█|█|█      )')
        elif 50 < enemyhealth <= 60:
            print('Enemy health:')
            print('(█|█|█|█|█|█        )')
        elif 40 < enemyhealth <= 50:
            print('Enemy health:')
            print('(█|█|█|█|█          )')
        elif 30 < enemyhealth <= 40:
            print('Enemy health:')
            print('(█|█|█|█            )')
        elif 20 < enemyhealth <= 30:
            print('Enemy health:')
            print('(█|█|█              )')
        elif 10 < enemyhealth <= 20:
            print('Enemy health:')
            print('(█|█                )')
        elif 0 < enemyhealth <= 10:
            print('Enemy health:')
            print('(█                  )')
        damage = int(input("Damage: "))
        enemyhealth -= damage
        enemydamage = random.randint(1, 20)
        print(f'Enemy does {enemydamage} in damage!')
        health -= enemydamage
        if health <= 0:
            print('Player health:')
            print('(                   )')
            print('Game over')
            break
        if enemyhealth <= 0:
            print('Enemy health:')
            print('(                   )')
            print('You win')
            break
for letter in letters.keys():
    print(text_to_big(letter))
    time.sleep(0.5)
    os.system('cls')
print(name_to_big('>>>//|0|\\\\<<<'))
```

Corresponding python file called letters:

```python
letters = {
    'A': ''' ███ 
█   █
█████
█   █
█   █''',

    'B': '''████ 
█   █
████ 
█   █
████ ''',

    'C': ''' ████
█    
█    
█    
 ████''',

    'D': '''████ 
█   █
█   █
█   █
████ ''',

    'E': '''█████
█    
████ 
█    
█████''',

    'F': '''█████
█    
████ 
█    
█    ''',

    'G': ''' ████
█    
█ ███
█   █
 ████''',

    'H': '''█   █
█   █
█████
█   █
█   █''',

    'I': '''█████
  █  
  █  
  █  
█████''',

    'J': '''█████
    █
    █
█   █
 ███ ''',

    'K': '''█   █
█  █ 
███  
█  █ 
█   █''',

    'L': '''█    
█    
█    
█    
█████''',

    'M': '''█   █
██ ██
█ █ █
█   █
█   █''',

    'N': '''█   █
██  █
█ █ █
█  ██
█   █''',

    'O': ''' ███ 
█   █
█   █
█   █
 ███ ''',

    'P': '''████ 
█   █
████ 
█    
█    ''',

    'Q': ''' ███ 
█   █
█   █
█  ██
 ████''',

    'R': '''████ 
█   █
████ 
█  █ 
█   █''',

    'S': ''' ████
█    
 ███ 
    █
████ ''',

    'T': '''█████
  █  
  █  
  █  
  █  ''',

    'U': '''█   █
█   █
█   █
█   █
 ███ ''',

    'V': '''█   █
█   █
█   █
 █ █ 
  █  ''',

    'W': '''█   █
█   █
█ █ █
██ ██
█   █''',

    'X': '''█   █
 █ █ 
  █  
 █ █ 
█   █''',

    'Y': '''█   █
 █ █ 
  █  
  █  
  █  ''',

    'Z': '''█████
   █ 
  █  
 █   
█████''',

    '?': ''' ███ 
█   █
   █ 
     
  █  ''',

    '!': '''  █  
  █  
  █  
     
  █  ''',

    '.': '''     
     
     
     
  █  ''',

    ',': '''     
     
     
  █  
 █   ''',
    
    '0': ''' ███ 
█   █
█   █
█   █
 ███ ''',

    '1': '''  █  
 ██  
  █  
  █  
█████''',

    '2': ''' ███ 
█   █
   █ 
  █  
█████''',

    '3': '''████ 
    █
 ███ 
    █
████ ''',

    '4': '''█   █
█   █
█████
    █
    █''',

    '5': '''█████
█    
████ 
    █
████ ''',

    '6': ''' ███ 
█    
████ 
█   █
 ███ ''',

    '7': '''█████
    █
   █ 
  █  
  █  ''',

    '8': ''' ███ 
█   █
 ███ 
█   █
 ███ ''',

    '9': ''' ███ 
█   █
 ████
    █
 ███ ''',
 
        '*': '''█ █ █
 █ █ 
  █  
 █ █ 
█ █ █''',

    '-': '''     
     
█████
     
     ''',

    '+': '''     
  █  
█████
  █  
     ''',

    '=': '''     
█████
     
█████
     ''',

    '`': '''█    
 █   
     
     
     ''',

    '~': '''     
 ██  █
█  ██ 
     
     ''',
     
    '>': '''██   
  ██ 
    █
  ██ 
██   ''',

    '<': '''   ██
 ██  
█    
 ██  
   ██''',
   
    '/': '''    █
   █ 
  █  
 █   
█    ''',

    '\\': '''█    
 █   
  █  
   █ 
    █''',
    
    '|': '''  █  
  █  
  █  
  █  
  █  '''}
```
