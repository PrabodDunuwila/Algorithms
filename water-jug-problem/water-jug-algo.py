"""
Created on Wed May 20 19:47:24 2020
@author: dunu008
"""

def fill_v1(v1, v2, v1_max):
    while v1 < v1_max and v2 != 0:
        v2 -= 1
        v1 += 1
    return v1, v2

def fill_jug_algo(v1_max, v2_max, value):
    v1, v1_max = 0, v1_max
    v2, v2_max = 0, v2_max
    print("\nVolume at different stages : \n{}L jar  |  {}L jar ".format(v1_max, v2_max))
    print("------------------")
    print("    {}   |   {}".format(v1, v2))
    while v1 != value and v2 != value:
        v2 = v2_max
        print("    {}   |   {}".format(v1, v2))
        while v2 != 0 and v1 != value and v2 != value:
            if v1 == v1_max and v2 != 0:
                v1 = 0
                print("    {}   |   {}".format(v1, v2))
            v1, v2 = fill_v1(v1, v2, v1_max)
            print("    {}   |   {}".format(v1, v2))
    
if __name__ == "__main__":
    fill_jug_algo(v1_max = 3, v2_max = 4, value = 2)
    fill_jug_algo(v1_max = 4, v2_max = 3, value = 2)
