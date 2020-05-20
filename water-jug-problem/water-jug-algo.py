"""
Created on Wed May 20 19:47:24 2020
@author: dunu008
"""

def fill_v1(v1, v2, v1_max):
    while v1 < v1_max:
        if v2 == 0:
            break
        v2 -= 1
        v1 += 1
    return (v1, v2)

def fill_three_litre_jug():
    v1, v1_max = 0, 4
    v2, v2_max = 0, 3
    print("Maximum volume of v1: {}L, v2: {}L".format(v1_max, v2_max))
    print("Volume at different stages : \n(v1, v2) ")
    while v1 != 2:
        #Fill 3 liter jug fully.
        v2 = v2_max
        print((v1, v2))
        #Fill 3 liter jug using 4 liter jug.
        v1, v2 = fill_v1(v1, v2, v1_max)
        if v1 == 2 or v2 == 2:
            break
        print((v1, v2))
    print((v1, v2))

def fill_four_litre_jug():
    v1, v1_max = 0, 3
    v2, v2_max = 0, 4   
    print("Maximum volume of v1: {}L, v2: {}L".format(v1_max, v2_max))
    print("Volume at different stages : \n(v1, v2) ")
    while v2 != 2:
        #Fill 4 liter jug fully.
        v2 = v2_max
        print((v1, v2))
        #Fill 3 liter jug using 4 liter jug.
        v1, v2 = fill_v1(v1, v2, v1_max)
        if v1 == 2 or v2 == 2:
            break
        print((v1, v2))
        #Empty 3 liter jug
        v1 = 0
        print((v1, v2))
        #Fill 3 liter jug using 4 liter jug.
        v1, v2 = fill_v1(v1, v2, v1_max)
        print((v1, v2))
    print((v1, v2))
    
if __name__ == "__main__":
    print("Fill 3L jug with 2L")
    fill_three_litre_jug()
    print("-------------------------")
    print("Fill 4L jug with 2L")
    fill_four_litre_jug()
