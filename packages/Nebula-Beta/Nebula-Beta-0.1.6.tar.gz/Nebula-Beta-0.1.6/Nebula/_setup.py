try:
    from .NebulaObject import *
    from .NebulaCore import *
except ModuleNotFoundError:
    print("~| _setup SCRIPT IMPORT ERROR...")
    os.sys.exit()

ABYSS = None

class Main:
    def __init__(self, abyss, projectName:str="MyNebulaProject", projectPath:str=os.path.join(os.getcwd(), "MyNebulaProject"), autoNCFG:bool=True, manNCFG:bool=False):
        self.abyss = abyss
        ABYSS = abyss
        if autoNCFG and not manNCFG:
            self.autoNCFG(abyss=abyss, projectName=projectName, projectPath=projectPath)
        if manNCFG and not autoNCFG:
            return 'manual config specified\n\n'

    def genCFG(self, abyss, projectName:str="MyNebulaProject", projectPath:str=os.path.join(os.getcwd(), "MyNebulaProject")):
        ncfgTemplate = {
            "env": {
                "debug": "False",
                "update": "False",
                "configured": "False"
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
        try:
            with open(f"{projectPath}\\.ncfg", "r") as check:
                c = check.read()
                check.close()
            
            if "env" not in c:
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "r") as f:
                    cache = json.load(f)
                    f.close()
                cache['Nebula'][projectName] = {}
                cache['current project'] = projectName
                cache['Nebula'][projectName]['path'] = projectPath
                cache['Nebula'][projectName]['project name'] = projectName
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "w") as f:
                    json.dump(cache, f, indent=4)
                    f.close()
                
                with open(f"{projectPath}\\.ncfg", "w") as f:
                    json.dump(
                        ncfgTemplate,
                        f,
                        indent=4
                    )
                    f.close()
            
            if "env" in c:
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "r") as f:
                    cache = json.load(f)
                    f.close()
                cache['Nebula'][projectName] = {}
                cache['current project'] = projectName
                cache['Nebula'][projectName]['path'] = projectPath
                cache['Nebula'][projectName]['project name'] = projectName
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "w") as f:
                    json.dump(cache, f, indent=4)
                    f.close()

                with open(f"{projectPath}\\.ncfg", "r") as f:
                    data = json.load(f)
                    f.close()

                if data['env']['configured'] == 'True':
                    abyss.custom_print('Nebula Project Configured.')
        
        
        except (FileNotFoundError):
            if not os.path.exists(f"{projectPath}"):
                os.mkdir(f"{projectPath}")
                abyss.custom_print('Project directory not found! Generating it now!')
            
            abyss.custom_print('Project .ncfg not found! Generating one now!')
            with open(f"{projectPath}\\.ncfg", "w") as check:
                json.dump(
                    ncfgTemplate,
                    check,
                    indent=4
                )
                check.close()
            
            with open(f"{projectPath}\\.ncfg", "r") as check:
                c = check.read()
                check.close()
            
            if "env" not in c:
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "r") as f:
                    cache = json.load(f)
                    f.close()
                cache['Nebula'][projectName] = {}
                cache['current project'] = projectName
                cache['Nebula'][projectName]['path'] = projectPath
                cache['Nebula'][projectName]['project name'] = projectName
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "w") as f:
                    json.dump(cache, f, indent=4)
                    f.close()
                
                with open(f"{projectPath}\\.ncfg", "w") as f:
                    json.dump(
                        ncfgTemplate,
                        f,
                        indent=4
                    )
                    f.close()
            
            if "env" in c:
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "r") as f:
                    cache = json.load(f)
                    f.close()
                cache['Nebula'][projectName] = {}
                cache['current project'] = projectName
                cache['Nebula'][projectName]['path'] = projectPath
                cache['Nebula'][projectName]['project name'] = projectName
                with open(f"C:\\.NebulaCache\\nebula-cache.json", "w") as f:
                    json.dump(cache, f, indent=4)
                    f.close()

                with open(f"{projectPath}\\.ncfg", "r") as f:
                    data = json.load(f)
                    f.close()

                if data['env']['configured'] == 'True':
                    abyss.custom_print('Nebula Project Configured.')
        

    def autoNCFG(self, abyss, projectName:str="MyNebulaProject", projectPath:str=os.path.join(os.getcwd(), "MyNebulaProject")):
        self.genCFG(abyss, projectName=projectName, projectPath=projectPath)

        from ._autoCFG import Main as autoMain
        autoMain(abyss, projectName=projectName, projectPath=projectPath)

if not os.path.exists('C:\\.NebulaCache'):
    os.mkdir('C:\\.NebulaCache')

if not os.path.exists('C:\\.NebulaCache\\nebula-cache.json'):
    with open('C:\\.NebulaCache\\nebula-cache.json', 'w') as f:
        f.write("")
        json.dump({"Nebula":{}, "current project":""}, f, indent=4)
        f.close()


def loadCache() -> dict:
    with open(f"C:\\.NebulaCache\\nebula-cache.json", "r") as f:
        cache = json.load(f)
        f.close()
    return cache

def renameProject(abyss, projectName:str, newProjectName:str):
    cache = loadCache()
    fullCache = cache
    cache = cache['Nebula']
    if projectName in list(cache.keys()):
        newProject = cache[projectName]
        newProject['project name'] = newProjectName
        
        copy = fullCache.copy()
        copy['Nebula'].pop(projectName) 
        newCache = copy
        newCache['Nebula'][newProjectName] = newProject
    else:
        abyss.custom_print(f"{projectName} does not exist in cache!")
        return
    try:
        with open("C:\\.NebulaCache\\nebula-cache.json", 'w') as f:
            json.dump(newCache, f, indent=4)
            f.close()

        with open(cache[newProjectName]['path']+"\\.ncfg", 'r') as f:
            ncfg = json.load(f)
            f.close()

        newNcfg = ncfg.copy()
        newNcfg['project']['project name'] = newProjectName
        
        with open(cache[newProjectName]['path']+"\\.ncfg", 'w') as f:
            ncfg = json.dump(newNcfg, f, indent=4)
            f.close()

    except (FileNotFoundError):
        abyss.custom_print(f'{newProjectName} .ncfg missing!')
        pass

    abyss.custom_print(f'Project Name changed, and cache updated!')

def listCache(abyss):
    cache = loadCache()
    for project in list(cache["Nebula"].keys()):
        abyss.custom_print(f'{project}')
        for data in cache["Nebula"][project]:
            abyss.custom_print(f'{data} | {cache["Nebula"][project][data]}')

def clearCache(abyss):
    cache = loadCache()
    cache.clear()
    with open("C:\\.NebulaCache\\nebula-cache.json", 'w') as f:
        cache = {'Nebula':{},"current project":""}
        json.dump(cache, f, indent=4)
        f.close()

def removeProject(abyss, projectName:str):
    cache = loadCache()
    try:
        cache['Nebula'].pop(projectName)
    except (KeyError):
        abyss.custom_print(f'Nebula Project "{projectName}" not found!')

def configRecentProject(abyss):
    cache = loadCache()
    recentProject = list(cache['Nebula'].keys())[len(cache['Nebula'])-1]
    projectPath= cache['Nebula'][recentProject]['path']
    abyss.custom_print(f'Configuring {recentProject}...')
    Main(
        abyss=abyss,
        projectName=recentProject,
        projectPath=projectPath,
        autoNCFG=True,
        manNCFG=False
    )

def configLoadProjectPath(abyss, choice:str):
    cache = loadCache()
    if os.path.exists(choice):
        with open(choice+"\\.ncfg", "r") as f:
            ncfg = json.load(f)
            f.close()

        projectName = ncfg['project']['project name']
        abyss.custom_print(f'Configuring {choice}!')
        Main(
            abyss=abyss,
            projectName=projectName,
            projectPath=choice,
            autoNCFG=True,
            manNCFG=False
        )
    else:
        abyss.custom_print(f'Unable to locate {choice}!')
        abyss.custom_print(f'You can navigate to your project\'s .ncfg and take a look at the name if need be!')

def configLoadProject(abyss, choice:str):
    cache = loadCache()
    if choice in list(cache['Nebula'].keys()):
        projectPath=cache['Nebula'][choice]['path']
        abyss.custom_print(f'Configuring {choice}!')
        Main(
            abyss=abyss,
            projectName=choice,
            projectPath=projectPath,
            autoNCFG=True,
            manNCFG=False
        )
    else:
        abyss.custom_print(f'Unable to locate {choice}!')
        abyss.custom_print(f'You can navigate to your project\'s .ncfg and take a look at the name if need be!')

def configNewProject(abyss, projectName:str="", projectPath:str=os.getcwd()):
    abyss.custom_print('New project!')
    abyss.custom_print('Lets get it set up!')
    if projectPath in {".", " ", "", "~", "here"}:
        projectPath = os.getcwd()
    Main(
        abyss=abyss,
        projectName=projectName,
        projectPath=projectPath,
        autoNCFG=True,
        manNCFG=False
    )