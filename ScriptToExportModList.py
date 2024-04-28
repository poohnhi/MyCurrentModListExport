import os, json, glob, re
import pandas as pd
from pathlib import Path
import json5
b = open("G:\Steam\steamapps\common\Stardew Valley\Mods\modlist.md", "w")
path_to_json = 'G:\Steam\steamapps\common\Stardew Valley\Mods'
string_pattern = path_to_json + '\**\*' + "*manifest.json*"
data2 = {}

for item in glob.iglob('G:\Steam\steamapps\common\Stardew Valley\Mods/**/*manifest.json', recursive=True):
    #print("Item:", item)
    folder_type = ""
    if 'Core1.6' in item:
        folder_type = 'Framework: '
    elif 'Mods Portraits And Animated Sprites' in item:
        folder_type = "Portraits And Animated Sprites: "
    elif 'Mods Tilesheets Recolor And UI' in item:
        folder_type = "Tilesheets Recolor And UI: "
    elif 'Expansions' in item:
        folder_type = "Expansion: "
    elif '[ATCP] Furniture Content Packs' in item:
        folder_type = "AT or CP Furniture: "
    elif '[FS] Fashion Sense Content Packs' in item:
        folder_type = "Fashion Sense: "
    elif '/.' in item:
        continue
    elif 'PoohMods' in item:
        continue
    f = open(item, encoding='utf-8-sig')
    jsondata = ''.join(line for line in f if not line.startswith('//'))
    #data = json.loads(jsondata)
    data = None
    try:
        data = json.loads(jsondata)
    except:
        try: 
            data = json.load(f)
        except:
            try:
                data = json5.loads(jsondata)
            except:
                print("Problem loading: ", item)                
        #print("Problem loading: ", item)
    temp = ""
    if data != None:
        try:
            for i in data['UpdateKeys']:
                temp = ""
                temp2 = i.lower()
                #print(i)
                #print(i)
                if ("nexus" in temp2):
                    NexusId = re.sub("[^0-9]", "", temp2)
                    temp = "(https://www.nexusmods.com/stardewvalley/mods/" + NexusId + ")"
                    break
                elif ("github" in temp2):
                    #NexusId = re.sub("[^0-9]", "", temp2)
                    temp = "(https://github.com/" + temp2[7:] + "/releases)"
                    break
                elif ("moddrop" in temp2):
                    ModdropId = re.sub("[^0-9]", "", temp2)
                    temp = "(https://www.moddrop.com/stardew-valley/mod/" + ModdropId + ")"
                    break
            fullname = folder_type + data['Name']
            data2[fullname] = temp
        except:
            #print(filename, " is error")
            pass
    f.close()
    

for i in data2:
#print(data2)
    try:
        temp = '[' + i + ']' + data2[i]
        b.write(temp)
        b.write("\n\n")
    except:
        print(temp, 'is error')
b.close()

