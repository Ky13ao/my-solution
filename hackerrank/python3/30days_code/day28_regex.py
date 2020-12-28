#!/bin/python3

import math
import os
import random
import re
import sys

def email_validator(email):
  patern = r'[a-z]+@gmail\.com$'
  return re.search(patern,email)

if __name__ == '__main__':
  N = int(input())
  contact_ls = []
  for N_itr in range(N):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]
    if email_validator(emailID):
      contact_ls.append(firstName)
  print(*sorted(contact_ls), sep='\n')