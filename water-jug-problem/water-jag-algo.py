#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:32:31 2020

@author: dunu008
"""
SMALL_JUG_CAPACITY = 3
LARGE_JUG_CAPACITY = 4

three_litre_jug = 0
four_litre_jug = 0

print("1. Fill 3L jug fully")

while(1):
    three_litre_jug += 1
    if three_litre_jug == SMALL_JUG_CAPACITY:
        break
    
print("3L jug has {}Litres of water".format(three_litre_jug))

print("------------------------------------------------------")

print("2. Pour water in 3L jug to 4L jug")

for i in range(three_litre_jug):
    three_litre_jug -= 1
    four_litre_jug += 1
    
print("3L jug has {}Litres of water".format(three_litre_jug))
print("4L jug has {}Litres of water".format(four_litre_jug))

print("------------------------------------------------------")

print("3. Fill 3L jug fully again")

while(1):
    three_litre_jug += 1
    if three_litre_jug == SMALL_JUG_CAPACITY:
        break
    
print("3L jug has {}Litres of water".format(three_litre_jug))
print("4L jug has {}Litres of water".format(four_litre_jug))

print("------------------------------------------------------")

print("4. Pour water in 3L jug into 4L jug until 4L jug fills completely")

while(1):
    three_litre_jug -= 1
    four_litre_jug += 1
    if four_litre_jug == LARGE_JUG_CAPACITY:
        break
    
print("3L jug has {}Litres of water".format(three_litre_jug))
print("4L jug has {}Litres of water".format(four_litre_jug))