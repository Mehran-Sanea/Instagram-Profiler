#!/user/bin/env python3
import requests
from os import system, name
from sys import argv
from colorama import Fore, init
init(autoreset="true")

# Give profile information.
def infoGather(username):
    response = str()
    response = requests.get(f"https://www.instagram.com/{username}/")
    return response

# Clear the screen
def cls():
    if  name == "nt":
        system("cls")
    else:
        system("clear")

# Show full name.
def full_name(text):
    name = ""
    start = (text.find('full_name')) + 12
    end = text.find('"', start)
    for char in range(start, end):
        name += text[char]
    return name

# Show country.
def country(text):
    region = ""
    start = (text.find('country_cod')) + 15
    end = text.find('"', start)
    for char in range(start, end):
        region += text[char]
    return region

# Show ID.
def ID(text):
    id = ""
    start = (text.find(',"id":"')) + 7
    end = text.find('"', start)
    for char in range(start, end):
        id += text[char]
    return id

# Show account type.
def pageStatus(text):
    status = ""
    start = (text.find('is_private')) + 12
    end = text.find(',', start)
    for char in range(start, end):
        status += text[char]
    if status == "false":
        return "Public Account."
    else:
        return "Private Account."

# Show business status.
def business(text):
    busy = ""
    start = (text.find('is_business_account')) + 21
    end = text.find(',', start)
    for char in range(start, end):
        busy += text[char]
    return busy 

# Findout posts number.
def numberOfPosts(text):
    number = ""
    if pageStatus(text) == "Private Account.":
        start = (text.find('has')) + 4
        end = text.find(' posts', start)
    else:
        start = (text.find('has')) + 4
        end = text.find(' photos and videos', start)

    for char in range(start, end):
        number += text[char]
    try:
    	print(f"{Fore.RED}Number of Posts: {number}\n{Fore.LIGHTGREEN_EX}***This user has{postState(int(number))}***\n")
    except:
        try:
            number = ""
            start = (text.find('see all')) + 8
            end = text.find(' of', start)
            for char in range(start, end):
                number += text[char]
            print(f"{Fore.RED}Number of Posts: {number}\n{Fore.LIGHTGREEN_EX}***This user has{postState(int(number))}***\n")
        except:
            try:
                number = ""
                start = (text.find('Following')) + 11
                end = text.find(' Posts', start)
                for char in range(start, end):
                    number += text[char]
                print(f"{Fore.RED}Number of Posts: {number}\n{Fore.LIGHTGREEN_EX}***This user has{postState(int(number))}***\n")
            except:
                print(f"{Fore.RED}Number of Posts: {0}\n{Fore.LIGHTGREEN_EX}***This user has{postState(0)}***\n")

# Calculate post status.
def postState(number_of_posts):
    if number_of_posts == 0:
        return " Not any post"
    elif number_of_posts >= 1 and number_of_posts <= 5:
        return " A few posts"
    elif number_of_posts >= 6 and number_of_posts <= 10:
        return " Some posts"
    elif number_of_posts >= 11 and number_of_posts <= 20:
        return " Many posts"
    elif number_of_posts >= 21 and number_of_posts <= 50:
        return " Lots of posts"
    elif number_of_posts > 50:
        return " Large number of posts"
    else:
        return "...hmmm! Something wrong! (We can't figureout status)"

# Find all follows.
def followNumbers(text):
    follower = ""
    following = ""
    start = (text.find('edge_followed_by":{"count":')) + 27
    end = text.find('}', start)
    for char in range(start, end):
        follower += text[char]
    start = (text.find('edge_follow":{"count":')) + 22
    end = text.find('}', start)
    for char in range(start, end):
        following += text[char]
    status = (int(follower) - int(following))
    if status == 0:
        print(f"{Fore.RED}followers: {follower} / followings: {following}\n{Fore.LIGHTGREEN_EX}***status: Balance ({status})***\n")
    elif status < 0:
        print(f"{Fore.RED}followers: {follower} / followings: {following}\n{Fore.LIGHTGREEN_EX}***status: Bad ({status})***\n")
    else:
        print(f"{Fore.RED}followers: {follower} / followings: {following}\n{Fore.LIGHTGREEN_EX}***status: Good ({status})***\n")

# Show banner.
def banner():
    print("""
                     /_\   /_\   /_\                                
                    // \\ // \\ // \\                               
                   |/   \|/   \|/   \|                              
  __                   .-'''-.        .-'''-.                  __   
 /\ \             _   '   _    \     '   _    \ _             / /\  
'  \ \          .' )/   /` '.   \  /   /` '.   ( `.          / /  ' 
 \  \ \        / .'.   |     \  ' .   |     \  ''. \        / /  /  
  \  \ \      / /  |   '      |  '|   '      |  ' \ \      / /  /   
   \  \ \    / /   \    \     / / \    \     / /   \ \    / /  /    
    \  \ \  . '     `.   ` ..' /   `.   ` ..' /     ' .  / /  /     
     \  \ \ | |        '-...-'`       '-...-'`      | | / /  /      
      \  \ \' '                                     ' '/ /  /       
       \  \ \\ \ ________________                  / // /  /        
        \  \_\\ \________________|                / //_/  /         
         \ / / \ '.                             .' / \ \ /          
          '-'   '._)   Lets go                 (_.'   --'           
                _   _   _            _   _   _                      
              .' ).' ).' )          ( `.( `.( `.      :)              
             / .'/ .'/ .'            '. \'. \'. \                   
            / / / / / /                \ \ \ \ \ \                  
           / / / / / /     Instagram    \ \ \ \ \ \                 
          . ' . ' . '       Profiler     ' . ' . ' .                
          | | | | | |                    | | | | | |                
          ' ' ' ' ' '    MehranTheSanea  ' ' ' ' ' '                
           \ \ \ \ \ \                  / / / / / /                 
            \ \ \ \ \ \                / / / / / /                  
             \ '.\ '.\ '.            .' /.' /.' /                   
              '._)'._)'._)          (_.'(_.'(_.'                    
    """)

# Main
if len(argv) <= 1 or len(argv) > 2:
    print(f"{Fore.RED}* Usage:\n{Fore.LIGHTGREEN_EX}    {argv[0]} USER")
else:
    cls()
    banner()
    info = infoGather(argv[1])
    if info.status_code == 200:
        print(Fore.LIGHTGREEN_EX + "Username found!")
    elif info.status_code == 404:
        print(Fore.RED + f"The '{argv[1]}' Username not found in Instagram.\nPlease check username and try again.\nBye bye!\n")
        exit()
    else:
        print(Fore.RED + "Something is wrong!\nCheck your connection and try again.\n")
        exit()

    print(f"{Fore.RED}Full name:{Fore.LIGHTGREEN_EX} {full_name(info.text)}")
    print(f"{Fore.RED}You Connected from:{Fore.LIGHTGREEN_EX} {country(info.text)}")
    print(f"{Fore.RED}User ID:{Fore.LIGHTGREEN_EX} {ID(info.text)}")
    print(f"{Fore.RED}Page status:{Fore.LIGHTGREEN_EX} {pageStatus(info.text)}")
    print(f"{Fore.RED}Business::{Fore.LIGHTGREEN_EX} {business(info.text)}\n")

    numberOfPosts(info.text)
    followNumbers(info.text)
