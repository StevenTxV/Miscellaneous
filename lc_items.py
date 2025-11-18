# This file is mainly for LC to allow carrying all items in the extra 
# This will list all the items with no repetition to be pasted into the necessary document
import string

filename = "lc_itemlist.txt"

def main():
    lc_store_list = ['Shovel', 'Stun grenade','Boombox', 'Extension ladder', 'Flashlight', 'Jetpack', 'Lockpicker', 'Pro-flashlight', 'Radar-booster', 'Spray paint', 'TZP-Inhalant', 'Walkie-talkie', 'Zap gun', 'Weed Killer', 'Belt bag', 'Survival kit', 'MedicalKit', 'Medkit', 'SuperFlashlight', 'Medic Bag', 'Night Vision Goggles', 'Pokeball', 'Great Ball', 'Ultra Ball', 'Master Ball']
    lc_item_list = ['Key', 'Shotgun Shells', 'Kitchen Knife', 'Shotgun', 'Ammo', 'Harp', 'Bagpipe', 'Snare Flea Sample', 'Spore Lizard Sample', 'Hoarding Bug Sample', 'Baboon Hawk Sample', 'Eyeless Dog Sample', 'Forest Giant Sample', 'Bracken Sample', 'Maneater Sample', 'Bunker Spider Sample', 'Tulip Snake Sample', 'Thumper Sample', 'Manticoil Sample', 'Shotgun shell', 'Fire Axe', 'Page', 'Big nut', 'Mysterious Page', 'Rubber tire', 'Flamingo floatie', 'Copper gear', 'Limit sign', 'Makeshift lamp', 'Screwdriver', 'Poop bucket', 'Gas tank', 'Big screw', 'Zapper', 'Improvised Timebomb', 'Small battery', 'Big battery', 'Undelivered Letter 3', 'Missing Poster', 'PolarMilk™', 'Dead ice crystal', 'Silver key', 'Leviathan tooth', 'Jewel box', 'Picture frame', 'Strange Page', 'Pig painting', 'Bronze bar', 'Ice cube', 'Coin', 'Dirty page', 'Post', 'Cog', 'Large plant', 'Copper plate', 'Metal duct', 'Undelivered letter 1', 'Silver bug', 'Silver coin', 'Undelivered letter 2', 'Barbed wire', 'Jar of growth', 'Square vial', 'Petri Dish', 'Grown Petri Dish', 'Round vial', 'Dying grown petri dish', 'Evil cosmo', 'Cosmic Growth', 'Circuit board', 'Blood petri dish', 'Harrington log 4', 'Harrington log 1', 'Harrington log 2', 'Harrington log 3', 'Dying cosmic flashlight', 'Oval vial', 'Toolbox', 'Watching petri dish']
    lc_string = ""
    listed_item = False
    listed_item_cap = False
    listed_item_cap_next = False
    
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
            
        # Combines both lc_store_list with lc_item_list
        for store_item in lc_store_list:
            lc_item_list.append(store_item)
        
        # Splits each item into their own category
        for i in lines:
            i = i.split(',')
            
            # Splits it again removing the number creating varying versions of the item
            for x in i:
                x = x.split(':', 1)
                xCap = x[0].capitalize()
                xCapNext = string.capwords(x[0].lower())
                
                # Checks normal input
                for item in lc_item_list:
                    if item == x[0]:
                        listed_item = True
                        break
                    
                # if already exists, do not add to list (for normal entry)
                if listed_item:
                    listed_item = False
                else:
                    lc_item_list.append(x[0])
                
                # Checks first letter cap only
                for item in lc_item_list:
                    if item == xCap:
                        listed_item_cap = True
                        break
                    
                # If already exists, do not add to list (for first letter)
                if listed_item_cap:
                    listed_item_cap = False
                else:
                    lc_item_list.append(xCap)
                
                # Checks first word caps only
                for item in lc_item_list:
                    if item == xCapNext:
                        listed_item_cap_next = True
                        break
                    
                # If already exists, do not add to list (first word caps)
                if listed_item_cap_next:
                    listed_item_cap_next = False
                else:
                    lc_item_list.append(xCapNext)
        
    # Sorts and prints out the items as string
    lc_item_list = sorted(lc_item_list)

    for item in lc_item_list:
        lc_string += item + ','
    print(lc_string)

if __name__=="__main__":
    main()