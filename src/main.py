from role import harvester, upgrader, builder

# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.
from defs import *

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

MAIN_SPAWN_NAME = 'Spawn1'

def main():
    """
    Main game logic loop.
    """

    # Clean up dead creep memory
    for name in Object.keys(Memory.creeps):
        if not Game.creeps[name]:
            del Memory.creeps[name]
            console.log('Clearing non-existing creep memory:', name)

    harvesters = _.filter(
        Game.creeps, lambda creep: creep.memory.role == 'harvester')
    console.log('Harvesters: ' + len(harvesters))

    if len(harvesters) < 2:
        newName = 'Harvester' + Game.time
        console.log('Spawning new harvester: ' + newName)
        Game.spawns[MAIN_SPAWN_NAME].spawnCreep(
            [WORK, CARRY, MOVE],
            newName,
            {'memory': {'role': 'harvester'}}
        )

    if Game.spawns[MAIN_SPAWN_NAME].spawning:
        spawningCreep = Game.creeps[Game.spawns[MAIN_SPAWN_NAME].spawning.name]
        Game.spawns[MAIN_SPAWN_NAME].room.visual.text(
            '🛠️' + spawningCreep.memory.role,
            Game.spawns[MAIN_SPAWN_NAME].pos.x + 1,
            Game.spawns[MAIN_SPAWN_NAME].pos.y,
            {'align': 'left', 'opacity': 0.8}
        )

    # replace this with the id of your tower
    tower = Game.getObjectById('TOWER_ID')

    if tower:
        closest_damaged_structure = tower.pos.findClosestByRange(FIND_STRUCTURES, {
            "filter": lambda structure: structure.hits < structure.hitsMax
        })
        if closest_damaged_structure:
            tower.repair(closest_damaged_structure)

        closest_hostile = tower.pos.findClosestByRange(FIND_HOSTILE_CREEPS)
        if closest_hostile:
            tower.attack(closest_hostile)

    # Run each creep
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]

        if creep.memory.role == 'harvester':
            harvester.run(creep)
        if creep.memory.role == 'upgrader':
            upgrader.run(creep)
        if creep.memory.role == 'builder':
            builder.run(creep)


module.exports.loop = main
