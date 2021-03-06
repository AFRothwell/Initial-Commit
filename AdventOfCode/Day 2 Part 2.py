# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:31:30 2021

@author: Andrew Rothwell
"""

'''

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be
what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the
password policy rules from his old job at the sled rental place down the
street! The Official Toboggan Corporate Policy actually works a little
differently.

Each policy actually describes two positions in the password, where 1 means
the first character, 2 means the second character, and so on. (Be careful;
Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of
these positions must contain the given letter. Other occurrences of the letter
are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the
policies?

'''

list = [str(x) for x in open("day 2 input.txt", "r").readlines()]
invalid_passwords = []
valid_passwords = []


for i in list:
    policy = (i.split(": ")[0])
    password1 = (i.split(": ")[1])
    password = password1.splitlines()[0]
    policy_positions = policy.split(" ")[0]
    policy_character = policy.split(" ")[1]
    position_lower = (int(policy_positions.split("-")[0]) - 1)
    position_upper = (int(policy_positions.split("-")[1]) - 1)
    
    if (password[position_lower] == policy_character) is not (password[position_upper] == policy_character):
        valid_passwords.append(i)
    else:
        invalid_passwords.append(i)
        
        
'''

Personal Notes:
    
Once I had the first part sorted out, the rest of this was easy! Too bad it's
been so warm recently... IDK I guess I'm the odd one out who PREFERS cold
weather.

'''