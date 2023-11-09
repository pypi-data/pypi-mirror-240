try:
    from .NebulaCore import json
except ModuleNotFoundError:
    print("~| _autoCFG SCRIPT IMPORT ERROR...")
    os.sys.exit()

ncfg = False

def Main(abyss, projectName:str, projectPath:str) -> bool:
    try:
        open(f"{projectPath}\\.ncfg", "r")
        ncfg = True
    except FileNotFoundError:
        abyss.custom_print('ncfg not found')
    
    if ncfg:
        with open(f"{projectPath}\\.ncfg", "r") as cfgReader:
            cfgData = json.load(cfgReader)
            cfgReader.close()

        if cfgData['env']['configured'] == 'False':
            with open(f"{projectPath}\\.ncfg", "w") as cfgWriter:
                finalCFG = ncfgTemplate = {
                    "env": {
                        "debug": "False",
                        "configured": "True"
                    },
                    "project": {
                        "cfg":"auto",
                        "Nebula ver": "v0.1.6",
                        "project name": f"{projectName}",
                        "project path": f"{projectPath}",
                        "tilesize": 8,
                        "tilemap size": [5000,5000],
                        "screen size": [1400, 800],
                        "canvas size": [700, 400],
                        "target FPS": 60
                    }
                }

                cfgWriter.write("")
                json.dump(finalCFG, cfgWriter, indent=4)
                cfgWriter.close()
            abyss.custom_print('Nebula project configured!')

        elif cfgData['env']['configured'] == 'True':
            abyss.custom_print('Nebula Project Configured.')
    else:
        abyss.custom_print('ncfg not found!')