# This file is used to select the ideal modules currently in your possession for BPSR

import itertools
import numpy

filename = "bp_modlist.txt"
module_list = []

stat_selection = ""
stat_1 = "0"
stat_2 = "0"

def main():
    stat_selection = input("Do you want to select your two stats? (y/n) ")

    with open(filename) as file:
        header_line = next(file)
        
        # List stat selection and enter stat
        if stat_selection == "y":
            print("Enter the number for the following stat that you want:")
            n = 0
            
            for x in header_line.split(','):
                print(f"{x}: {n}")
                n = n + 1
            
            stat_1 = input("First stat number: ")
            stat_2 = input("Second stat number: ")
            print("Listing modules to create selected stats over 20...")
        else:
            print("Listing at least 2 stats over 20 and a 3rd stat over 8...")
        
        lines = [line.rstrip() for line in file]
        
        # Update the lines into arrays stored in module_list
        for modules in lines:
            #print(modules)
            module_list.append(modules.split(','))
            
        # Iterate through the module list with a combination of 4
        for combo in itertools.combinations(module_list,4):
            #print(combo)
            array = [0,0,0,0,0]
            
            # Adds the numbers in the combo array together
            for x in combo:
                #print(x)
                array += numpy.array(x).astype(int)
            
            # Determines best modules for selections
            if stat_selection == "y":
                specific_values(stat_1, stat_2, combo, array, header_line)
            else:
                two_values(combo, array, header_line)
        

# Lists modules used to generate over 2 main stats along with a 3rd decent stat
def two_values(combo, array, header_line):
    greater_main = [v for v in array if v > 20]
    greater_second = [v for v in array if v > 8]
    if len(greater_main) >= 2:
        if len(greater_second) >=3:
            print(combo)
            print(array)
            print(header_line)

# Lists modules used to generate 2 specific stats
def specific_values(stat_1, stat_2, combo, array, header_line):
    if array[int(stat_1)] >= 20 and array[int(stat_2)] >= 20:
        print(combo)
        print(array)
        print(header_line)
            
            
if __name__=="__main__":
    main()