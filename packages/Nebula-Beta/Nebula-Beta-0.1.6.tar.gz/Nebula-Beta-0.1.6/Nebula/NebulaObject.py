try:
    from .NebulaCore import *
except ModuleNotFoundError:
    mnf = str(input("~| BASE IMPORT ERROR...\nThere was an error while gathering nebula.core\nPlease check that your installation directory contains the 'core' sub-directory.\nIf so, type 'fix' to open the Nebula Console.\nWhen the command line appears, type 'neb -fix ~core' to run the appropriate repair script.\nIf the problem persists, contact setoichi.\n~| ")) #cmd, flg, mod
    if mnf in {"fix",}:
        print("open Abyss Console\n")
    import os
    os.sys.exit()

"""
NEBULA CORE OBJECTS
"""
class Camera:
    
    def __init__(self, env, levelSize, screenSize, cameraSpeed, scrollInterpolation):
        self.env = env
        self.levelSize = VECTOR2(levelSize)
        self.screenSize = VECTOR2(screenSize)
        self.scroll = VECTOR2(0, 0)
        self.scrollInterpolation = scrollInterpolation
        self.scrollSpeed = cameraSpeed
        self.DEADZONERADIUS = 10
        self.inDeadzone = False
        self.panSpeed = cameraSpeed/2
        self.panning = False
        self.panTarget = None

    def scrollCamera(self, target):
        desiredScroll = VECTOR2(
            target.rect().x - self.screenSize.x // 2,
            target.rect().y - self.screenSize.y // 2.8
        )

        distanceToTarget = (self.scroll - desiredScroll).length()
        if distanceToTarget >= self.DEADZONERADIUS:
            self.scroll += (desiredScroll - self.scroll) * self.scrollSpeed / self.scrollInterpolation * self.env.DT

    def panCamera(self, target):
        if type(target) == VECTOR2:
            desiredScroll = VECTOR2(
                target.x - self.screenSize.x / 2,
                target.y - self.screenSize.y / 2
            )
            # Use regular division for smoother interpolation
            self.scroll += (desiredScroll - self.scroll) * self.panSpeed / self.scrollInterpolation * self.env.DT
    
    def setTarget(self, target, screenSize, levelBound=False):
        self.screenSize = screenSize
        if not self.panning:
            self.scrollCamera(target)
        else:
            self.panTarget = target
            self.panCamera(self.panTarget)

        if levelBound:
            # Constrain camera within the level bounds
            self.scroll.x = max(0, min(self.scroll.x, self.levelSize.x - self.screenSize.x))
            self.scroll.y = max(0, min(self.scroll.y, self.levelSize.y - self.screenSize.y))

    def getOffset(self):
        # return VECTOR2(self.scroll.x, self.scroll.y)
        return VECTOR2(int(self.scroll.x), int(self.scroll.y))


class Physics:
    def __init__(self, entity):
        self.entity = entity
        self.velocity = VECTOR2(0, 0)
        self.gravity = True
        self.friction = 0.7

    def horizontalMovementCollision(self, entity, tilemap, movement, dt):
        movement = movement
        entity.position.x += movement.x * dt
        entityRect = entity.rect()
        for rect in tilemap.physicsRectsAround(entity.position):
            if entityRect.colliderect(rect):
                if movement.x > 0:
                    entityRect.right = rect.left
                    entity.collisions['right'] = True
                if movement.x < 0:
                    entityRect.left = rect.right
                    entity.collisions['left'] = True
                entity.position.x = entityRect.x

    def verticalMovementCollision(self, entity, tilemap, movement, gravity, dt):
        movement = movement
        if entity.physics.gravity:
            entity.velocity.y = min(280, entity.velocity.y + gravity)
        movement.y = entity.velocity.y
        entity.position.y += movement.y * dt
        entityRect = entity.rect()
        for rect in tilemap.physicsRectsAround(entity.position):
            if entityRect.colliderect(rect):
                if movement.y > 0:
                    entity.velocity.y = 0
                    entityRect.bottom = rect.top
                    entity.collisions['down'] = True
                if movement.y < 0:
                    entity.velocity.y = 0
                    entityRect.top = rect.bottom
                    entity.collisions['up'] = True
                entity.position.y = entityRect.y


class Entity(pygame.sprite.Sprite):
    def __init__(self, _id:int=random.randint(999,9999), position:pygame.math.Vector2()=pygame.math.Vector2(), size:int=32, rectSize=pygame.math.Vector2(32, 32), spriteGroups:list=[], color:list=[10, 30, 20]):
        super().__init__(spriteGroups)
        self._id = _id
        self.Renderer = None
        self.rectSize = rectSize
        self.size = pygame.math.Vector2(size, size)
        self.spriteGroups = spriteGroups
        self.position = pygame.math.Vector2(position)
        self.image = pygame.Surface((size, size))
        self.imageOffset = (0,0)
        self.image.fill(color)
        self.physics = Physics(self)
        self.velocity = VECTOR2()

    def rect(self):
        return pygame.Rect((self.position.x, self.position.y), (self.rectSize[0], self.rectSize[1]))

    def setRenderer(self, renderer):
        self.Renderer = renderer

    def updatePhysics(self, tilemap, gravity, dt):
        # movement = self.velocity
        movement = VECTOR2(self.velocity.x, self.velocity.y)
        # movement = VECTOR2(self.physics.velocity.x, self.physics.velocity.y)
        self.physics.horizontalMovementCollision(self, tilemap, movement, dt)
        self.physics.verticalMovementCollision(self, tilemap, movement, gravity, dt)

    def updateCollisions(self):
        self.collisions = {"up": False, "down": False, "left": False, "right": False}


class NebulaCache:
    def __init__(self, maxSize=100):
        self.cache = {"base": {"cache": {}, "frequency": {}}}
        self.usage = []
        self.maxSize = maxSize

    @outDebugReturn
    def addSubCache(self, name:str=""):
        if name not in self.cache:
            self.cache[name] = {"cache":{}, "frequency":{}}
            return True
        return 'Subcache already present'

    @outDebugReturn
    def get(self, key, subCache=None):
        subCache = subCache if subCache in self.cache else "base"
        cache = self.cache[subCache]["cache"]
        frequency = self.cache[subCache]["frequency"]

        if key in cache:
            frequency[key] += 1
            self.updateUsage(key, subCache)
            return cache[key]
        else:
            return 'Key Not Present'

    def put(self, key, value, subCache=None):
        if self.maxSize <= 0:
            return 'Cache is disabled'

        if subCache in self.cache:
            cache = self.cache[subCache]["cache"]
            frequency = self.cache[subCache]["frequency"]
        elif subCache not in self.cache:
            self.cache[subCache] = {"cache":{}, "frequency":{}}
            cache = self.cache[subCache]["cache"]
            frequency = self.cache[subCache]["frequency"]

        if self.checkSize(subCache) >= self.maxSize:
            minFrequencyKey = min(frequency, key=lambda k: (frequency[k], self.usage.index(k)))
            del cache[minFrequencyKey]
            del frequency[minFrequencyKey]

        try:
            cache[key] = value
            frequency[key] = 1
            self.updateUsage(key, subCache)
        except (KeyError, ValueError):
            return 'Key or Value was not given'

    def checkSize(self, subCache="base"):
        return len(self.cache[subCache]["cache"])

    def updateUsage(self, key, subCache="base"):
        if key in self.usage:
            self.usage.remove(key)
        self.usage.append(key)


class Animation:
    def __init__(self, images, frameCount=5, loop=True):
        self.images = images
        self.imageMasks = [pygame.mask.from_surface(image) for image in images]
        self.loop = loop
        self.frameCount = frameCount
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.frameCount, self.loop)

    def update(self):
        if not self.done:
            self.frame = (self.frame + 1) % (self.frameCount * len(self.images)) if self.loop else min(self.frame + 1, self.frameCount * len(self.images) - 1)

    def img(self):
        frameIndex = int(self.frame / self.frameCount)
        return [self.images[frameIndex], self.imageMasks]


class AssetManager:
    def __init__(self, env, maxCacheSize=100):
        self._env = env
        self.cache = NebulaCache(maxSize=maxCacheSize)

    def loadLiveAssets(self, assetsPath: str, animationLib: dict, frameCount: int, willLoop: bool, subCache=None):
        loadedAssets = {}
        for key, folderPath in animationLib.items():
            self.cache.put(key=key, value=Animation(loadAssetDir(assetsPath + f"{folderPath}"), frameCount=frameCount, loop=willLoop), subCache=subCache)
        return True

    def loadCutStaticAsset(self, assetName: str, assetPath: str, tileSize:int=16, subCache=None):
        self.cache.put(key=assetName, value=cLoadAssets(path=assetPath, tileSize=tileSize), subCache=subCache)
        return True

    def loadStaticAsset(self, assetName: str, assetPath: str, subCache=None):
        self.cache.put(key=assetName, value=loadAsset(assetPath), subCache=subCache)
        return True

    def putAsset(self, assetID, asset, subCache=None):
        self.cache.put(assetID, asset, subCache=subCache)

    def getAssetByID(self, assetID, subCache=None):
        return self.cache.get(assetID, subCache=subCache)

    def reloadAssetPosition(self, assetID, position, subCache=None):
        # Update the rendering position of an asset
        asset = self.getAssetByID(assetID)
        if asset:
            self._env.Renderer.addStaticRenderData(assetID, position)
        else:
            print(f"Asset not found: {assetID}")


class Renderer:
    def __init__(self, env, layerCount: int, assetManager: AssetManager):
        self.env = env
        self.layerCount = layerCount
        self.renderLayers = [[] for _ in range(layerCount)]
        self.dirtyRects = []
        self.tileGroup = pygame.sprite.Group()
        self.assetManager = assetManager
        self.renderData = []  # Store rendering data for static images

    def addLayer(self):
        self.layerCount += 1
        self.renderLayers.append([])

    def addAsset(self, assetID: str|int, asset: pygame.Surface, layerNumber: int=0):
        self.renderLayers[layerNumber].append(asset)
        self.dirtyRects.append(asset.get_rect())

    def addEntity(self, obj: Entity, layerNumber: int=0):
        if obj not in self.renderLayers[layerNumber]:
            self.renderLayers[layerNumber].append(obj)
        self.assetManager.putAsset(obj._id, obj, subCache="Entities")
        if obj.rect() not in self.dirtyRects:
            self.dirtyRects.append(obj.rect())

    def render(self, display: pygame.Surface, canvas:pygame.Surface=None, zoomFactor:int|float=1.0, offset:VECTOR2=VECTOR2(), autoClear:list|tuple|bool=False):
        self.clearDirtyRects()
        # Render the layers and assets on them in order
        if canvas != None:
            if isinstance(autoClear, bool) and autoClear == True:
                canvas.fill([0, 0, 0])  # Clear the surface
            elif isinstance(autoClear, tuple|list):
                canvas.fill(list(autoClear))  # Clear the surface
            self.tileGroup.draw(canvas)
            self.tileGroup.empty()
        else:
            if isinstance(autoClear, bool) and autoClear == True:
                display.fill([0, 0, 0])  # Clear the surface
            elif isinstance(autoClear, tuple|list):
                display.fill(list(autoClear))  # Clear the surface
            self.tileGroup.draw(display)
            self.tileGroup.empty()
        for layer in self.renderLayers:
            for item in layer:
                if isinstance(item, Entity):
                    if canvas != None:
                        canvas.blit(item.image, (item.position.x - offset[0] + item.imageOffset[0], item.position.y - offset[1] + item.imageOffset[1]))
                        self.env.Canvas = SCALE(
                            canvas, (
                                display.get_size()[0]/zoomFactor, 
                                display.get_size()[1]/zoomFactor
                                )
                        )
                        display.blit(SCALE(canvas, display.get_size()), (0,0))
                    else:
                        display.blit(item.image, (item.rect().topleft + VECTOR2(item.imageOffset[0], item.imageOffset[1])) - offset)
                    self.dirtyRects.append(item.rect())
                elif isinstance(item, pygame.Surface):
                    if canvas != None:
                        canvas.blit(item, item.get_rect().topleft - offset)
                    else:
                        display.blit(item, item.get_rect().topleft - offset)
                    self.dirtyRects.append(item.get_rect())
                else:
                    print(f"Unsupported item in render layer: {item}")

    def clearDirtyRects(self):
        self.dirtyRects.clear()


class Tilemap:
    def __init__(self, mapDataPath, env, renderer, tileSize=32, physicsTilesIds=None):
        self.env = env
        self.Renderer = renderer
        self.AssetManager = self.Renderer.assetManager
        self.cache = self.AssetManager.cache
        self.tileSize = tileSize
        self.tilemap = {}
        self.physicsTileIDs = set(physicsTilesIds) if physicsTilesIds else set()
        self.load(mapDataPath)

    @outDebugReturn
    def load(self, path):
        with open(path, "r") as savefile:
            map_data = json.load(savefile)

        self.mapName = map_data["name"]
        self.tilemap = map_data["tileGrid"]
        self.tileSize = map_data["tileSize"]
        self.offgridTiles = map_data["offGrid"]
        self.mapSize = pygame.math.Vector2(map_data['map width']*self.tileSize, map_data['map height']*self.tileSize)

        try:
            [self.AssetManager.putAsset(_id, tile, subCache="tileset") for _id, tile in enumerate(cLoadAssets(map_data["tilesetPath"], self.tileSize))]
            return 'Tileset Cached'
        except (KeyError, ValueError):
            return 'unable to cache tileset'

    def getMapSize(self, in_tiles=True):
        return self.mapSize.x, self.mapSize.y

    def solidTileCheck(self, position, layer):
        tileLocation = f"{int(position[0] // self.tileSize)};{int(position[1] // self.tileSize)}"
        if layer in self.tilemap and tileLocation in self.tilemap[layer]:
            tile = self.tilemap[layer][tileLocation]
            if tile['id'] in self.physicsTileIDs:
                return tile

    def extractTileInfo(self, tileId, keep=False):
        matches = []
        for layer in self.tilemap.values():
            for location, tile in list(layer.items()):
                if tile['id'] in tileId:
                    matches.append(tile.copy())
                    if not keep:
                        del layer[location]
        
        return matches

    def tilesAround(self, position):
        tiles = []
        tileLocation = (int(position[0] // self.tileSize), int(position[1] // self.tileSize))
        for offset in [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]:
            checkLocation = f"{tileLocation[0] + offset[0]};{tileLocation[1] + offset[1]}"
            for layer in self.tilemap:
                if layer in self.tilemap and checkLocation in self.tilemap[layer]:
                    tiles.append(self.tilemap[layer][checkLocation])
        
        return tiles

    def physicsRectsAround(self, position):
        rects = []
        for tile in self.tilesAround(position):
            if tile['id'] in self.physicsTileIDs:
                tileX, tileY = tile['position']
                rect = pygame.Rect(tileX * self.tileSize, tileY * self.tileSize, self.tileSize, self.tileSize)
                rects.append(rect)
        
        return rects

    def render(self, surface, offset=pygame.math.Vector2(), zoomFactor=1):
        visibleArea = pygame.Rect(zoomFactor - (self.tileSize - 1), zoomFactor - (self.tileSize - 1), surface.get_width(), surface.get_height())
        for layer in self.tilemap.values():
            for location, tile in list(layer.items()):
                tileRect = pygame.Rect(
                    tile['position'][0] * self.tileSize - offset[0],
                    tile['position'][1] * self.tileSize - offset[1],
                    self.tileSize, self.tileSize
                )

                if tileRect.colliderect(visibleArea):
                    assetId = tile['id']
                    asset = self.cache.cache['tileset']['cache'][assetId]
                    position = pygame.math.Vector2(tileRect.topleft)
                    tile = Entity(_id=assetId, position=position, size=self.tileSize, rectSize=VECTOR2(self.tileSize,self.tileSize))
                    tile.image = asset
                    tile.rect = tile.rect()
                    self.Renderer.tileGroup.add(tile)
                    self.Renderer.dirtyRects.append(tile)


class TileGrid:
    def __init__(self, mapName, game, tileset, tileSize=32):
        self.game = game
        self.tileSize = tileSize
        self.tileGrid = {}
        self.mapName = mapName
        self.offgrid_tiles = []
    
    def getMapSize(self, inTiles=True):
        if inTiles:
            max_x = 0
            max_y = 0
            for location in self.tileGrid:
                x, y = map(int, location.split(';'))
                max_x = max(max_x, x)
                max_y = max(max_y, y)
            return VECTOR2(max_x + 1, max_y + 1)
        else:
            max_x = 0
            max_y = 0
            for layer in self.tileGrid:
                for location in self.tileGrid[layer]:
                    tile = self.tileGrid[layer][location]
                    max_x = max(max_x, tile['position'][0] * self.tileSize)
                    max_y = max(max_y, tile['position'][1] * self.tileSize)
            return VECTOR2(int(max_x + self.tileSize), int(max_y + self.tileSize))

    def export_as_png(self, save_path):
        # Get the map size in pixels
        map_size = self.get_map_size(in_tiles=False)

        # Create a surface to render the map
        export_surface = pygame.Surface(map_size)

        # Fill the surface with a background color (e.g., white)
        export_surface.fill((255, 255, 255))

        # Render each tile onto the surface
        for layer in self.tileGrid:
            for location in self.tileGrid[layer]:
                tile = self.tileGrid[layer][location]
                tile_image = self.game.assets[f'tileset'][tile['id']]
                position = (tile['position'][0] * self.tileSize, tile['position'][1] * self.tileSize)
                export_surface.blit(tile_image, position)

        # Create the full path for saving the image
        export_filename = f'{self.map_name}.png'
        full_export_path = os.path.join(save_path, export_filename)

        # Save the surface as a PNG image
        pygame.image.save(export_surface, full_export_path)
        print(f"Map exported as {full_export_path}")

    def exportAsPng(self, savePath):
        mapSize = self.getMapSize(inTiles=False)
        exportSurface = pygame.Surface(mapSize)
        exportSurface.fill((255, 255, 255))

        for layer in self.tileGrid:
            for tile in self.tileGrid[layer]:
                t = self.tileGrid[layer][tile]
                tileImage = self.game.assets[f'tileset'][int(t['id'])]
                x, y = t['position']
                position = (x * self.tileSize, y * self.tileSize)
                exportSurface.blit(tileImage, position)

        exportFilename = f'{self.mapName}.png'
        fullExportPath = os.path.join(savePath, exportFilename)
        pygame.image.save(exportSurface, fullExportPath)
        return f"Map exported as {fullExportPath}"

    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[f'tileset'][tile['id']], (
                tile['position'][0] - offset[0], tile['position'][1] - offset[1]))

        for x in range(int(offset[0]) // self.tileSize, (int(offset[0]) + surf.get_width()) // self.tileSize + 1):
            for y in range(int(offset[1]) // self.tileSize, (int(offset[1]) + surf.get_height()) // self.tileSize + 1):
                location = str(x) + ';' + str(y)
                for layer in self.tileGrid:
                    if location in self.tileGrid[layer]:
                        tile = self.tileGrid[layer][location]
                        surf.blit(self.game.assets[f'tileset'][tile['id']], (tile['position'][0] * self.tileSize - int(offset[0]), tile['position'][1] * self.tileSize - int(offset[1])))


class Cloud:
    def __init__(self, pos, img, speed, depth, fog=False, fog_density=0.6):
        self.pos = list(pos)
        if not fog:
            self.img = img
        else:
            self.img = img
            self.img.set_alpha(255*fog_density)
        self.speed = speed
        self.depth = depth
    
    def update(self, dt):
        self.pos[0] += self.speed * dt
        
    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        surf.blit(self.img, (render_pos[0] % (1400 + self.img.get_width()) - self.img.get_width(), render_pos[1] % (960 + self.img.get_height()) - self.img.get_height()))


class Clouds:
    def __init__(self, cloud_images:list|tuple, count:int=16, fog:bool=False, fog_density:int|float=0.6):
        self.clouds = []
        
        for i in range(count):
            self.clouds.append(Cloud((random.random() * 99999, random.random() * 99999), random.choice(cloud_images), random.random() * 8 + 8, random.random() * 0.6 + 0.2, fog=fog, fog_density=fog_density))
        
        self.clouds.sort(key=lambda x: x.depth)
    
    def update(self, dt):
        for cloud in self.clouds:
            cloud.update(dt)
    
    def render(self, surf, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset=offset)