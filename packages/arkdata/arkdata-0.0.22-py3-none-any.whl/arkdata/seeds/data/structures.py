from arkdata import models


def backup_seed():
    models.Structure.new(id=95, name='Wooden Window', stack_size=100, class_name='PrimalItemStructure_WoodWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWindow.PrimalItemStructure_WoodWindow\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Window',
                         description='Wooden beams on hinges that cover windows to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Wooden_Window.png')
    models.Structure.new(id=94, name='Wooden Windowframe', stack_size=100,
                         class_name='PrimalItemStructure_WoodWallWithWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWallWithWindow.PrimalItemStructure_WoodWallWithWindow\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Windowframe',
                         description='Wooden beams on hinges that cover windows to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Wooden_Window.png')
    models.Structure.new(id=92, name='Wooden Wall', stack_size=100, class_name='PrimalItemStructure_WoodWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWall.PrimalItemStructure_WoodWall\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Wall',
                         description='A sturdy wooden wall that insulates the inside from the outside, separates rooms, and provides structural integrity.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Wooden_Wall.png')
    models.Structure.new(id=260, name='Wooden Wall Sign', stack_size=100,
                         class_name='PrimalItemStructure_WoodSign_Wall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSign_Wall.PrimalItemStructure_WoodSign_Wall\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Wall_Sign',
                         description='A sturdy wooden wall that insulates the inside from the outside, separates rooms, and provides structural integrity.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Wooden_Wall.png')
    models.Structure.new(id=495, name='Wooden Triangle Roof', stack_size=100,
                         class_name='PrimalItemStructure_TriRoof_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Wood/PrimalItemStructure_TriRoof_Wood.PrimalItemStructure_TriRoof_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Triangle_Roof',
                         description='A wood, sloped triangle roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/48/Wooden_Triangle_Roof.png')
    models.Structure.new(id=489, name='Wooden Triangle Foundation', stack_size=100,
                         class_name='PrimalItemStructure_TriFoundation_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Wood/PrimalItemStructure_TriFoundation_Wood.PrimalItemStructure_TriFoundation_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Triangle_Foundation',
                         description='Required to build structures in an area. Triangle shaped.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Wooden_Triangle_Foundation.png')
    models.Structure.new(id=484, name='Wooden Triangle Ceiling', stack_size=100,
                         class_name='PrimalItemStructure_TriCeiling_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Wood/PrimalItemStructure_TriCeiling_Wood.PrimalItemStructure_TriCeiling_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Triangle_Ceiling',
                         description='A stable wooden ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Wooden_Triangle_Ceiling.png')
    models.Structure.new(id=91, name='Wooden Trapdoor', stack_size=100, class_name='PrimalItemStructure_WoodTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodTrapdoor.PrimalItemStructure_WoodTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Trapdoor',
                         description='This small wooden door can be used to secure hatches.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Wooden_Trapdoor.png')
    models.Structure.new(id=478, name='Wooden Stairs', stack_size=100, class_name='PrimalItemStructure_Ramp_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Wood/PrimalItemStructure_Ramp_Wood.PrimalItemStructure_Ramp_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Stairs',
                         description='Wooden stairs for traveling up or down levels. Can be switched to a ramp variant.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5e/Wooden_Stairs.png')
    models.Structure.new(id=303, name='Wooden Spike Wall', stack_size=100,
                         class_name='PrimalItemStructure_WoodSpikeWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSpikeWall.PrimalItemStructure_WoodSpikeWall\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Spike_Wall',
                         description='These incredibly sharp wooden stakes are dangerous to any that touch them. Larger creatures take more damage.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Wooden_Spike_Wall.png')
    models.Structure.new(id=96, name='Wooden Sign', stack_size=100, class_name='PrimalItemStructure_WoodSign_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSign.PrimalItemStructure_WoodSign\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Sign',
                         description='A simple wooden sign for landmark navigation or relaying messages.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Wooden_Sign.png')
    models.Structure.new(id=90, name='Wooden Ramp', stack_size=100, class_name='PrimalItemStructure_WoodRamp_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodRamp.PrimalItemStructure_WoodRamp\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Ramp',
                         description='An inclined wooden floor for travelling up or down. Can also be used to make an angled roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Wooden_Ramp.png')
    models.Structure.new(id=410, name='Wooden Raft', stack_size=1, class_name='PrimalItemRaft_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/Items/Raft/PrimalItemRaft.PrimalItemRaft\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Raft',
                         description='A floating wooden platform that you can pilot across the water. Can support the weight of structures and be built on.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Wooden_Raft.png')
    models.Structure.new(id=89, name='Wooden Pillar', stack_size=100, class_name='PrimalItemStructure_WoodPillar_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodPillar.PrimalItemStructure_WoodPillar\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Pillar',
                         description='Adds structural integrity to the area it is built on. Can also act as stilts for buildings on inclines.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Wooden_Pillar.png')
    models.Structure.new(id=88, name='Wooden Ladder', stack_size=100, class_name='PrimalItemStructure_WoodLadder_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodLadder.PrimalItemStructure_WoodLadder\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Ladder',
                         description='A simple wooden ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Wooden_Ladder.png')
    models.Structure.new(id=85, name='Wooden Hatchframe', stack_size=100,
                         class_name='PrimalItemStructure_WoodCeilingWithTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCeilingWithTrapdoor.PrimalItemStructure_WoodCeilingWithTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Hatchframe',
                         description='A wooden ceiling with a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Wooden_Hatchframe.png')
    models.Structure.new(id=87, name='Wooden Foundation', stack_size=100, class_name='PrimalItemStructure_WoodFloor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodFloor.PrimalItemStructure_WoodFloor\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Foundation',
                         description='A foundation is required to build structures. This one is made from sturdy wood.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Wooden_Foundation.png')
    models.Structure.new(id=466, name='Wooden Fence Support', stack_size=100,
                         class_name='PrimalItemStructure_FenceSupport_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Wood/PrimalItemStructure_FenceSupport_Wood.PrimalItemStructure_FenceSupport_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Fence_Support',
                         description="Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Wooden_Fence_Support.png')
    models.Structure.new(id=135, name='Wooden Fence Foundation', stack_size=100,
                         class_name='PrimalItemStructure_WoodFenceFoundation_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodFenceFoundation.PrimalItemStructure_WoodFenceFoundation\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Fence_Foundation',
                         description='This very cheap, narrow foundation is used to build fences around an area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Wooden_Fence_Foundation.png')
    models.Structure.new(id=455, name='Wooden Double Door', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoor_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Wood/PrimalItemStructure_DoubleDoor_Wood.PrimalItemStructure_DoubleDoor_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Double_Door',
                         description='A stable wooden door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/af/Wooden_Double_Door.png')
    models.Structure.new(id=461, name='Wooden Double Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoorframe_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Wood/PrimalItemStructure_DoubleDoorframe_Wood.PrimalItemStructure_DoubleDoorframe_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Double_Doorframe',
                         description='A stable wooden door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/af/Wooden_Double_Door.png')
    models.Structure.new(id=86, name='Wooden Door', stack_size=100, class_name='PrimalItemStructure_WoodDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodDoor.PrimalItemStructure_WoodDoor\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Door',
                         description='A stable wooden door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Wooden_Door.png')
    models.Structure.new(id=93, name='Wooden Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_WoodWallWithDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWallWithDoor.PrimalItemStructure_WoodWallWithDoor\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Doorframe',
                         description='A stable wooden door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Wooden_Door.png')
    models.Structure.new(id=84, name='Wooden Ceiling', stack_size=100, class_name='PrimalItemStructure_WoodCeiling_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCeiling.PrimalItemStructure_WoodCeiling\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Ceiling',
                         description='A stable wooden ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Wooden_Ceiling.png')
    models.Structure.new(id=83, name='Wooden Catwalk', stack_size=100, class_name='PrimalItemStructure_WoodCatwalk_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCatwalk.PrimalItemStructure_WoodCatwalk\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Catwalk',
                         description='A thin walkway for bridging areas together. Made from sturdy wood.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Wooden_Catwalk.png')
    models.Structure.new(id=217, name='Wooden Billboard', stack_size=100,
                         class_name='PrimalItemStructure_WoodSign_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSign_Large.PrimalItemStructure_WoodSign_Large\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Billboard',
                         description='A large wooden billboard for landmark navigation or relaying messages.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Wooden_Billboard.png')
    models.Structure.new(id=183, name='Water Reservoir', stack_size=100, class_name='PrimalItemStructure_WaterTank_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_WaterTank.PrimalItemStructure_WaterTank\'"',
                         url='https://ark.fandom.com/wiki/Water_Reservoir',
                         description='A standing storage device for holding water. Automatically fills up during rain, can be filled up with the use of a water skin/jar.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Water_Reservoir.png')
    models.Structure.new(id=191, name='Vertical Electrical Cable', stack_size=100,
                         class_name='PrimalItemStructure_PowerCableVertical_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableVertical.PrimalItemStructure_PowerCableVertical\'"',
                         url='https://ark.fandom.com/wiki/Vertical_Electrical_Cable',
                         description='A vertical cable for transmitting electricity up and down cliffs.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Vertical_Electrical_Cable.png')
    models.Structure.new(id=302, name='Vault', stack_size=1, class_name='PrimalItemStructure_StorageBox_Huge_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StorageBox_Huge.PrimalItemStructure_StorageBox_Huge\'"',
                         url='https://ark.fandom.com/wiki/Vault',
                         description='A large metal vault to securely store goods in.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c9/Vault.png')
    models.Structure.new(id=81, name='Thatch Wall', stack_size=100, class_name='PrimalItemStructure_ThatchWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchWall.PrimalItemStructure_ThatchWall\'"',
                         url='https://ark.fandom.com/wiki/Thatch_Wall',
                         description='A simple wall made of bundled sticks, and stabilized by a wooden frame. Fairly fragile, but better than nothing.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Thatch_Wall.png')
    models.Structure.new(id=80, name='Thatch Foundation', stack_size=100,
                         class_name='PrimalItemStructure_ThatchFloor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchFloor.PrimalItemStructure_ThatchFloor\'"',
                         url='https://ark.fandom.com/wiki/Thatch_Foundation',
                         description='A foundation is required to build structures. This one is a wooden frame with some smooth bundles of sticks that act as a floor.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Thatch_Foundation.png')
    models.Structure.new(id=79, name='Thatch Door', stack_size=100, class_name='PrimalItemStructure_ThatchDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchDoor.PrimalItemStructure_ThatchDoor\'"',
                         url='https://ark.fandom.com/wiki/Thatch_Door',
                         description='Enough sticks bundled together works as a simple door. Can be locked for security, but not very strong.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/Thatch_Door.png')
    models.Structure.new(id=82, name='Thatch Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_ThatchWallWithDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchWallWithDoor.PrimalItemStructure_ThatchWallWithDoor\'"',
                         url='https://ark.fandom.com/wiki/Thatch_Doorframe',
                         description='Enough sticks bundled together works as a simple door. Can be locked for security, but not very strong.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/Thatch_Door.png')
    models.Structure.new(id=78, name='Thatch Ceiling', stack_size=100, class_name='PrimalItemStructure_ThatchCeiling_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchCeiling.PrimalItemStructure_ThatchCeiling\'"',
                         url='https://ark.fandom.com/wiki/Thatch_Ceiling',
                         description='A thatched ceiling to protect you from the elements. Not stable enough to build on.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8d/Thatch_Ceiling.png')
    models.Structure.new(id=494, name='Tek Triangle Roof', stack_size=100,
                         class_name='PrimalItemStructure_TriRoof_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Tek/PrimalItemStructure_TriRoof_Tek.PrimalItemStructure_TriRoof_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Triangle_Roof', description='A sloped Tek triangle roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dc/Tek_Triangle_Roof.png')
    models.Structure.new(id=488, name='Tek Triangle Foundation', stack_size=100,
                         class_name='PrimalItemStructure_TriFoundation_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Tek/PrimalItemStructure_TriFoundation_Tek.PrimalItemStructure_TriFoundation_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Triangle_Foundation',
                         description='Required to build structures in an area. Triangle shaped.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Tek_Triangle_Foundation.png')
    models.Structure.new(id=483, name='Tek Triangle Ceiling', stack_size=100,
                         class_name='PrimalItemStructure_TriCeiling_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Tek/PrimalItemStructure_TriCeiling_Tek.PrimalItemStructure_TriCeiling_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Triangle_Ceiling',
                         description='An incredibly durable composite Tek ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Tek_Triangle_Ceiling.png')
    models.Structure.new(id=477, name='Tek Stairs', stack_size=100, class_name='PrimalItemStructure_Ramp_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Tek/PrimalItemStructure_Ramp_Tek.PrimalItemStructure_Ramp_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Stairs',
                         description='Composite Tek stairs for travelling up or down levels. Can be switched to a ramp variant.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Tek_Stairs.png')
    models.Structure.new(id=465, name='Tek Fence Support', stack_size=100,
                         class_name='PrimalItemStructure_FenceSupport_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Tek/PrimalItemStructure_FenceSupport_Tek.PrimalItemStructure_FenceSupport_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Fence_Support',
                         description="Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1a/Tek_Fence_Support.png')
    models.Structure.new(id=454, name='Tek Double Door', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoor_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Tek/PrimalItemStructure_DoubleDoor_Tek.PrimalItemStructure_DoubleDoor_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Double_Door',
                         description='A stable composite door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Tek_Double_Door.png')
    models.Structure.new(id=460, name='Tek Double Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoorframe_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Tek/PrimalItemStructure_DoubleDoorframe_Tek.PrimalItemStructure_DoubleDoorframe_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Double_Doorframe',
                         description='A stable composite door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Tek_Double_Door.png')
    models.Structure.new(id=449, name='Tek Dedicated Storage', stack_size=100,
                         class_name='PrimalItemStructure_DedicatedStorage_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Misc/DedicatedStorage/PrimalItemStructure_DedicatedStorage.PrimalItemStructure_DedicatedStorage\'"',
                         url='https://ark.fandom.com/wiki/Tek_Dedicated_Storage',
                         description='Holds a large amount of a single resource.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/Tek_Dedicated_Storage.png')
    models.Structure.new(id=190, name='Straight Electrical Cable', stack_size=100,
                         class_name='PrimalItemStructure_PowerCableStraight_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableStraight.PrimalItemStructure_PowerCableStraight\'"',
                         url='https://ark.fandom.com/wiki/Straight_Electrical_Cable',
                         description='A straight cable, used for transmitting electricity across land.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1d/Straight_Electrical_Cable.png')
    models.Structure.new(id=104, name='Storage Box', stack_size=100,
                         class_name='PrimalItemStructure_StorageBox_Small_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StorageBox_Small.PrimalItemStructure_StorageBox_Small\'"',
                         url='https://ark.fandom.com/wiki/Storage_Box', description='A small box to store goods in.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Storage_Box.png')
    models.Structure.new(id=319, name='Stone Windowframe', stack_size=100,
                         class_name='PrimalItemStructure_StoneWallWithWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneWallWithWindow.PrimalItemStructure_StoneWallWithWindow\'"',
                         url='https://ark.fandom.com/wiki/Stone_Windowframe',
                         description='A brick-and-mortar wall with a hole for a window.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Stone_Windowframe.png')
    models.Structure.new(id=307, name='Stone Wall', stack_size=100, class_name='PrimalItemStructure_StoneWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneWall.PrimalItemStructure_StoneWall\'"',
                         url='https://ark.fandom.com/wiki/Stone_Wall',
                         description='A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png')
    models.Structure.new(id=493, name='Stone Triangle Roof', stack_size=100,
                         class_name='PrimalItemStructure_TriRoof_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Stone/PrimalItemStructure_TriRoof_Stone.PrimalItemStructure_TriRoof_Stone\'"',
                         url='https://ark.fandom.com/wiki/Stone_Triangle_Roof',
                         description='A sloped stone triangle roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Stone_Triangle_Roof.png')
    models.Structure.new(id=487, name='Stone Triangle Foundation', stack_size=100,
                         class_name='PrimalItemStructure_TriFoundation_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Stone/PrimalItemStructure_TriFoundation_Stone.PrimalItemStructure_TriFoundation_Stone\'"',
                         url='https://ark.fandom.com/wiki/Stone_Triangle_Foundation',
                         description='Required to build structures in an area. Triangle shaped.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3c/Stone_Triangle_Foundation.png')
    models.Structure.new(id=482, name='Stone Triangle Ceiling', stack_size=100,
                         class_name='PrimalItemStructure_TriCeiling_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Stone/PrimalItemStructure_TriCeiling_Stone.PrimalItemStructure_TriCeiling_Stone\'"',
                         url='https://ark.fandom.com/wiki/Stone_Triangle_Ceiling',
                         description='A stable brick-and-mortar ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Stone_Triangle_Ceiling.png')
    models.Structure.new(id=476, name='Stone Stairs', stack_size=100, class_name='PrimalItemStructure_Ramp_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Stone/PrimalItemStructure_Ramp_Stone.PrimalItemStructure_Ramp_Stone\'"',
                         url='https://ark.fandom.com/wiki/Stone_Stairs',
                         description='Stone stairs for traveling up or down levels. Can be switched to a ramp variant.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1d/Stone_Stairs.png')
    models.Structure.new(id=317, name='Stone Pillar', stack_size=100, class_name='PrimalItemStructure_StonePillar_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StonePillar.PrimalItemStructure_StonePillar\'"',
                         url='https://ark.fandom.com/wiki/Stone_Pillar',
                         description='Adds structural integrity to the area it is built on. Can also act as stilts for buildings on inclines.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Stone_Pillar.png')
    models.Structure.new(id=113, name='Stone Irrigation Pipe - Vertical', stack_size=100,
                         class_name='PrimalItemStructure_StonePipeVertical_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeVertical.PrimalItemStructure_StonePipeVertical\'"',
                         url='https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Vertical',
                         description='A vertical stone pipe for an irrigation network, used for transporting water up and down cliffs.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d7/Stone_Irrigation_Pipe_-_Vertical.png')
    models.Structure.new(id=114, name='Stone Irrigation Pipe - Tap', stack_size=100,
                         class_name='PrimalItemStructure_StonePipeTap_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeTap.PrimalItemStructure_StonePipeTap\'"',
                         url='https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Tap',
                         description='This stone tap allows access to the water in an irrigation network. Can refill containers, irrigate crop plots, or provide a refreshing drink.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Stone_Irrigation_Pipe_-_Tap.png')
    models.Structure.new(id=110, name='Stone Irrigation Pipe - Straight', stack_size=100,
                         class_name='PrimalItemStructure_StonePipeStraight_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeStraight.PrimalItemStructure_StonePipeStraight\'"',
                         url='https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Straight',
                         description='A straight stone pipe for an irrigation network, used for transporting water across land.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/Stone_Irrigation_Pipe_-_Straight.png')
    models.Structure.new(id=112, name='Stone Irrigation Pipe - Intersection', stack_size=100,
                         class_name='PrimalItemStructure_StonePipeIntersection_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeIntersection.PrimalItemStructure_StonePipeIntersection\'"',
                         url='https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Intersection',
                         description='A plus-shaped stone intersection for an irrigation network, used for splitting one water source into three.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Stone_Irrigation_Pipe_-_Intersection.png')
    models.Structure.new(id=109, name='Stone Irrigation Pipe - Intake', stack_size=100,
                         class_name='PrimalItemStructure_StonePipeIntake_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeIntake.PrimalItemStructure_StonePipeIntake\'"',
                         url='https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Intake',
                         description='The stone intake for an irrigation network that transports water over land.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/68/Stone_Irrigation_Pipe_-_Intake.png')
    models.Structure.new(id=111, name='Stone Irrigation Pipe - Inclined', stack_size=100,
                         class_name='PrimalItemStructure_StonePipeIncline_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeIncline.PrimalItemStructure_StonePipeIncline\'"',
                         url='https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Inclined',
                         description='An inclined stone pipe for an irrigation network, used for transporting water up and down hills.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Stone_Irrigation_Pipe_-_Inclined.png')
    models.Structure.new(id=473, name='Stone Irrigation Pipe - Flexible', stack_size=100,
                         class_name='PrimalItemStructure_PipeFlex_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Pipes/Flex/Stone/PrimalItemStructure_PipeFlex_Stone.PrimalItemStructure_PipeFlex_Stone\'"',
                         url='https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Flexible',
                         description='Connects nearby pipes dynamically.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/57/Stone_Irrigation_Pipe_-_Flexible.png')
    models.Structure.new(id=312, name='Stone Hatchframe', stack_size=100,
                         class_name='PrimalItemStructure_StoneCeilingWithTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeilingWithTrapdoor.PrimalItemStructure_StoneCeilingWithTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Stone_Hatchframe',
                         description='This brick-and-mortar ceiling has a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Stone_Hatchframe.png')
    models.Structure.new(id=314, name='Stone Foundation', stack_size=100, class_name='PrimalItemStructure_StoneFloor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneFloor.PrimalItemStructure_StoneFloor\'"',
                         url='https://ark.fandom.com/wiki/Stone_Foundation',
                         description='A foundation is required to build structures in an area. This one is made from brick-and-mortar.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f6/Stone_Foundation.png')
    models.Structure.new(id=464, name='Stone Fence Support', stack_size=100,
                         class_name='PrimalItemStructure_FenceSupport_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Stone/PrimalItemStructure_FenceSupport_Stone.PrimalItemStructure_FenceSupport_Stone\'"',
                         url='https://ark.fandom.com/wiki/Stone_Fence_Support',
                         description="Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/69/Stone_Fence_Support.png')
    models.Structure.new(id=306, name='Stone Fence Foundation', stack_size=100,
                         class_name='PrimalItemStructure_StoneFenceFoundation_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneFenceFoundation.PrimalItemStructure_StoneFenceFoundation\'"',
                         url='https://ark.fandom.com/wiki/Stone_Fence_Foundation',
                         description='This strong, narrow foundation is used to build walls around an area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c0/Stone_Fence_Foundation.png')
    models.Structure.new(id=459, name='Stone Double Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoorframe_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Stone/PrimalItemStructure_DoubleDoorframe_Stone.PrimalItemStructure_DoubleDoorframe_Stone\'"',
                         url='https://ark.fandom.com/wiki/Stone_Double_Doorframe',
                         description='A brick-and-mortar wall that provides entrance to a structure.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Stone_Double_Doorframe.png')
    models.Structure.new(id=318, name='Stone Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_StoneWallWithDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneWallWithDoor.PrimalItemStructure_StoneWallWithDoor\'"',
                         url='https://ark.fandom.com/wiki/Stone_Doorframe',
                         description='A stone wall that provides entrance to a structure.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Stone_Doorframe.png')
    models.Structure.new(id=316, name='Stone Dinosaur Gateway', stack_size=100,
                         class_name='PrimalItemStructure_StoneGateframe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGateframe.PrimalItemStructure_StoneGateframe\'"',
                         url='https://ark.fandom.com/wiki/Stone_Dinosaur_Gateway',
                         description='A large brick-and-mortar gateway that can be used with a Gate to keep most dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Stone_Dinosaur_Gateway.png')
    models.Structure.new(id=311, name='Stone Ceiling', stack_size=100, class_name='PrimalItemStructure_StoneCeiling_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeiling.PrimalItemStructure_StoneCeiling\'"',
                         url='https://ark.fandom.com/wiki/Stone_Ceiling',
                         description='A stable brick-and-mortar ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Stone_Ceiling.png')
    models.Structure.new(id=40, name='Standing Torch', stack_size=3, class_name='PrimalItemStructure_StandingTorch_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StandingTorch.PrimalItemStructure_StandingTorch\'"',
                         url='https://ark.fandom.com/wiki/Standing_Torch',
                         description='A torch on a small piece of wood that lights and warms the immediate area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Standing_Torch.png')
    models.Structure.new(id=280, name='Spider Flag', stack_size=100, class_name='PrimalItemStructure_Flag_Spider_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Spider.PrimalItemStructure_Flag_Spider\'"',
                         url='https://ark.fandom.com/wiki/Spider_Flag',
                         description='This flag is proof that you have defeated the Broodmother.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/10/Spider_Flag.png')
    models.Structure.new(id=125, name='Smithy', stack_size=100, class_name='PrimalItemStructure_AnvilBench_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_AnvilBench.PrimalItemStructure_AnvilBench\'"',
                         url='https://ark.fandom.com/wiki/Smithy',
                         description='Place materials along with blueprints in this to create certain advanced forged items.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b9/Smithy.png')
    models.Structure.new(id=129, name='Small Crop Plot', stack_size=100,
                         class_name='PrimalItemStructure_CropPlot_Small_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CropPlot_Small.PrimalItemStructure_CropPlot_Small\'"',
                         url='https://ark.fandom.com/wiki/Small_Crop_Plot',
                         description='A small garden plot, with a fence to keep out vermin.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/59/Small_Crop_Plot.png')
    models.Structure.new(id=393, name='Sloped Wooden Roof', stack_size=100, class_name='PrimalItemStructure_WoodRoof_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Wood/PrimalItemStructure_WoodRoof.PrimalItemStructure_WoodRoof\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Wooden_Roof',
                         description='An inclined wooden roof. Slightly different angle than the ramp.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f6/Sloped_Wooden_Roof.png')
    models.Structure.new(id=395, name='Sloped Wood Wall Right', stack_size=100,
                         class_name='PrimalItemStructure_WoodWall_Sloped_Right_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Wood/PrimalItemStructure_WoodWall_Sloped_Right.PrimalItemStructure_WoodWall_Sloped_Right\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Wood_Wall_Right',
                         description='A sturdy Wooden sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Sloped_Wood_Wall_Right.png')
    models.Structure.new(id=394, name='Sloped Wood Wall Left', stack_size=100,
                         class_name='PrimalItemStructure_WoodWall_Sloped_Left_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Wood/PrimalItemStructure_WoodWall_Sloped_Left.PrimalItemStructure_WoodWall_Sloped_Left\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Wood_Wall_Left',
                         description='A sturdy Wooden sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Sloped_Wood_Wall_Left.png')
    models.Structure.new(id=392, name='Sloped Thatch Wall Right', stack_size=100,
                         class_name='PrimalItemStructure_ThatchWall_Sloped_Right_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Thatch/PrimalItemStructure_ThatchWall_Sloped_Right.PrimalItemStructure_ThatchWall_Sloped_Right\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Thatch_Wall_Right',
                         description='A simple wall made of bundled sticks, and stabilized by a wooden frame. Fairly fragile, but better than nothing.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Thatch_Wall.png')
    models.Structure.new(id=391, name='Sloped Thatch Wall Left', stack_size=100,
                         class_name='PrimalItemStructure_ThatchWall_Sloped_Left_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Thatch/PrimalItemStructure_ThatchWall_Sloped_Left.PrimalItemStructure_ThatchWall_Sloped_Left\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Thatch_Wall_Left',
                         description='A simple wall made of bundled sticks, and stabilized by a wooden frame. Fairly fragile, but better than nothing.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Thatch_Wall.png')
    models.Structure.new(id=390, name='Sloped Thatch Roof', stack_size=100,
                         class_name='PrimalItemStructure_ThatchRoof_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Thatch/PrimalItemStructure_ThatchRoof.PrimalItemStructure_ThatchRoof\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Thatch_Roof',
                         description='An inclined thatched roof. Slightly different angle than the ramp.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9d/Sloped_Thatch_Roof.png')
    models.Structure.new(id=398, name='Sloped Stone Wall Right', stack_size=100,
                         class_name='PrimalItemStructure_StoneWall_Sloped_Right_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Stone/PrimalItemStructure_StoneWall_Sloped_Right.PrimalItemStructure_StoneWall_Sloped_Right\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Stone_Wall_Right',
                         description='A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png')
    models.Structure.new(id=397, name='Sloped Stone Wall Left', stack_size=100,
                         class_name='PrimalItemStructure_StoneWall_Sloped_Left_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Stone/PrimalItemStructure_StoneWall_Sloped_Left.PrimalItemStructure_StoneWall_Sloped_Left\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Stone_Wall_Left',
                         description='A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png')
    models.Structure.new(id=396, name='Sloped Stone Roof', stack_size=100, class_name='PrimalItemStructure_StoneRoof_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Stone/PrimalItemStructure_StoneRoof.PrimalItemStructure_StoneRoof\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Stone_Roof',
                         description='An inclined stone roof. Slightly different angle than the ramp.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b9/Sloped_Stone_Roof.png')
    models.Structure.new(id=401, name='Sloped Metal Wall Right', stack_size=100,
                         class_name='PrimalItemStructure_MetalWall_Sloped_Right_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Metal/PrimalItemStructure_MetalWall_Sloped_Right.PrimalItemStructure_MetalWall_Sloped_Right\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Metal_Wall_Right',
                         description='A sturdy metal sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Sloped_Metal_Wall_Right.png')
    models.Structure.new(id=400, name='Sloped Metal Wall Left', stack_size=100,
                         class_name='PrimalItemStructure_MetalWall_Sloped_Left_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Metal/PrimalItemStructure_MetalWall_Sloped_Left.PrimalItemStructure_MetalWall_Sloped_Left\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Metal_Wall_Left',
                         description='A sturdy metal sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Sloped_Metal_Wall_Left.png')
    models.Structure.new(id=399, name='Sloped Metal Roof', stack_size=100, class_name='PrimalItemStructure_MetalRoof_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Metal/PrimalItemStructure_MetalRoof.PrimalItemStructure_MetalRoof\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Metal_Roof',
                         description='An inclined metal roof. Slightly different angle than the ramp.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3f/Sloped_Metal_Roof.png')
    models.Structure.new(id=438, name='Sloped Greenhouse Wall Right', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseWall_Sloped_Right_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWall_Sloped_Right.PrimalItemStructure_GreenhouseWall_Sloped_Right\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Greenhouse_Wall_Right',
                         description='A metal-frame, glass sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/12/Sloped_Greenhouse_Wall_Right.png')
    models.Structure.new(id=437, name='Sloped Greenhouse Wall Left', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseWall_Sloped_Left_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWall_Sloped_Left.PrimalItemStructure_GreenhouseWall_Sloped_Left\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Greenhouse_Wall_Left',
                         description='A metal-frame, glass sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/95/Sloped_Greenhouse_Wall_Left.png')
    models.Structure.new(id=439, name='Sloped Greenhouse Roof', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseRoof_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseRoof.PrimalItemStructure_GreenhouseRoof\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Greenhouse_Roof',
                         description='An inclined metal-frame, glass roof. Slightly different angle than the ramp. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Greenhouse_Roof.png')
    models.Structure.new(id=370, name='Single Panel Flag', stack_size=100,
                         class_name='PrimalItemStructure_Flag_Single_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Single.PrimalItemStructure_Flag_Single\'"',
                         url='https://ark.fandom.com/wiki/Single_Panel_Flag',
                         description="Mark your tribe's territory by placing this and painting it.",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Single_Panel_Flag.png')
    models.Structure.new(id=128, name='Simple Bed', stack_size=3, class_name='PrimalItemStructure_Bed_Simple_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bed_Simple.PrimalItemStructure_Bed_Simple\'"',
                         url='https://ark.fandom.com/wiki/Simple_Bed',
                         description='Thatch may not make the most comfortable mattress, but this bed acts as a respawn point for you and your Tribe.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Simple_Bed.png')
    models.Structure.new(id=195, name='Remote Keypad', stack_size=100, class_name='PrimalItemStructure_Keypad_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Keypad.PrimalItemStructure_Keypad\'"',
                         url='https://ark.fandom.com/wiki/Remote_Keypad',
                         description='Allows remote access to multiple doors and/or lights.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9b/Remote_Keypad.png')
    models.Structure.new(id=313, name='Reinforced Wooden Door', stack_size=100,
                         class_name='PrimalItemStructure_StoneDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneDoor.PrimalItemStructure_StoneDoor\'"',
                         url='https://ark.fandom.com/wiki/Reinforced_Wooden_Door',
                         description='A stable wooden door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Wooden_Door.png')
    models.Structure.new(id=353, name='Reinforced Window', stack_size=100,
                         class_name='PrimalItemStructure_StoneWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_StoneWindow.PrimalItemStructure_StoneWindow\'"',
                         url='https://ark.fandom.com/wiki/Reinforced_Window',
                         description='Reinforced window covering to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Reinforced_Window.png')
    models.Structure.new(id=354, name='Reinforced Trapdoor', stack_size=100,
                         class_name='PrimalItemStructure_StoneTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_StoneTrapdoor.PrimalItemStructure_StoneTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Reinforced_Trapdoor',
                         description='This small reinforced door can be used to secure hatches.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Reinforced_Trapdoor.png')
    models.Structure.new(id=453, name='Reinforced Double Door', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoor_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Stone/PrimalItemStructure_DoubleDoor_Stone.PrimalItemStructure_DoubleDoor_Stone\'"',
                         url='https://ark.fandom.com/wiki/Reinforced_Double_Door',
                         description='A reinforced wooden door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b0/Reinforced_Double_Door.png')
    models.Structure.new(id=315, name='Reinforced Dinosaur Gate', stack_size=100,
                         class_name='PrimalItemStructure_StoneGate_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGate.PrimalItemStructure_StoneGate\'"',
                         url='https://ark.fandom.com/wiki/Reinforced_Dinosaur_Gate',
                         description='A large, reinforced wooden gate that can be used with a Gateway to keep dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Reinforced_Dinosaur_Gate.png')
    models.Structure.new(id=193, name='Refrigerator', stack_size=1, class_name='PrimalItemStructure_IceBox_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_IceBox.PrimalItemStructure_IceBox\'"',
                         url='https://ark.fandom.com/wiki/Refrigerator',
                         description='Requires electricity to run. Keeps perishables from spoiling for a long time.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Refrigerator.png')
    models.Structure.new(id=124, name='Refining Forge', stack_size=100, class_name='PrimalItemStructure_Forge_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Forge.PrimalItemStructure_Forge\'"',
                         url='https://ark.fandom.com/wiki/Refining_Forge',
                         description='Requires wood, thatch, or sparkpowder to activate. Put unrefined resources in this to refine them.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Refining_Forge.png')
    models.Structure.new(id=291, name='Preserving Bin', stack_size=100,
                         class_name='PrimalItemStructure_PreservingBin_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_PreservingBin.PrimalItemStructure_PreservingBin\'"',
                         url='https://ark.fandom.com/wiki/Preserving_Bin',
                         description='Burns simple fuel at low temperatures to dehydrate food and kill bacteria. Keeps perishables from spoiling for a small time.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/09/Preserving_Bin.png')
    models.Structure.new(id=416, name='Painting Canvas', stack_size=100,
                         class_name='PrimalItemStructure_PaintingCanvas_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_PaintingCanvas.PrimalItemStructure_PaintingCanvas\'"',
                         url='https://ark.fandom.com/wiki/Painting_Canvas',
                         description='A canvas sheet stretched over a wooden frame. Perfect for painting on.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Painting_Canvas.png')
    models.Structure.new(id=355, name='Omnidirectional Lamppost', stack_size=100,
                         class_name='PrimalItemStructure_LamppostOmni_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_LamppostOmni.PrimalItemStructure_LamppostOmni\'"',
                         url='https://ark.fandom.com/wiki/Omnidirectional_Lamppost',
                         description='Requires electricity to activate. Lights an area without adding much heat.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Omnidirectional_Lamppost.png')
    models.Structure.new(id=276, name='Multi-Panel Flag', stack_size=100, class_name='PrimalItemStructure_Flag_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag.PrimalItemStructure_Flag\'"',
                         url='https://ark.fandom.com/wiki/Multi-Panel_Flag',
                         description='Mark your tribes territory and show off its colours by placing this and dying it.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/76/Flag.png')
    models.Structure.new(id=106, name='Mortar and Pestle', stack_size=100,
                         class_name='PrimalItemStructure_MortarAndPestle_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_MortarAndPestle.PrimalItemStructure_MortarAndPestle\'"',
                         url='https://ark.fandom.com/wiki/Mortar_And_Pestle',
                         description='This simple stone contraption can be used to grind resources into new substances.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Mortar_And_Pestle.png')
    models.Structure.new(id=179, name='Metal Window', stack_size=100, class_name='PrimalItemStructure_MetalWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWindow.PrimalItemStructure_MetalWindow\'"',
                         url='https://ark.fandom.com/wiki/Metal_Window',
                         description='Metal plates on hinges that cover windows to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/Metal_Window.png')
    models.Structure.new(id=178, name='Metal Windowframe', stack_size=100,
                         class_name='PrimalItemStructure_MetalWallWithWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWallWithWindow.PrimalItemStructure_MetalWallWithWindow\'"',
                         url='https://ark.fandom.com/wiki/Metal_Windowframe',
                         description='Metal plates on hinges that cover windows to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/Metal_Window.png')
    models.Structure.new(id=308, name='Metal Water Reservoir', stack_size=100,
                         class_name='PrimalItemStructure_WaterTankMetal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_WaterTankMetal.PrimalItemStructure_WaterTankMetal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Water_Reservoir',
                         description='A standing storage device for holding water. Automatically fills up during rain, can be filled up with the use of a water skin/jar.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Water_Reservoir.png')
    models.Structure.new(id=176, name='Metal Wall', stack_size=100, class_name='PrimalItemStructure_MetalWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWall.PrimalItemStructure_MetalWall\'"',
                         url='https://ark.fandom.com/wiki/Metal_Wall',
                         description='A metal-plated concrete wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Metal_Wall.png')
    models.Structure.new(id=265, name='Metal Wall Sign', stack_size=100,
                         class_name='PrimalItemStructure_MetalSign_Wall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSign_Wall.PrimalItemStructure_MetalSign_Wall\'"',
                         url='https://ark.fandom.com/wiki/Metal_Wall_Sign',
                         description='A metal-plated concrete wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Metal_Wall.png')
    models.Structure.new(id=492, name='Metal Triangle Roof', stack_size=100,
                         class_name='PrimalItemStructure_TriRoof_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Metal/PrimalItemStructure_TriRoof_Metal.PrimalItemStructure_TriRoof_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Triangle_Roof',
                         description='A sloped metal triangle roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Metal_Triangle_Roof.png')
    models.Structure.new(id=486, name='Metal Triangle Foundation', stack_size=100,
                         class_name='PrimalItemStructure_TriFoundation_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Metal/PrimalItemStructure_TriFoundation_Metal.PrimalItemStructure_TriFoundation_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Triangle_Foundation',
                         description='Required to build structures in an area. Triangle shaped.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/67/Metal_Triangle_Foundation.png')
    models.Structure.new(id=481, name='Metal Triangle Ceiling', stack_size=100,
                         class_name='PrimalItemStructure_TriCeiling_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Metal/PrimalItemStructure_TriCeiling_Metal.PrimalItemStructure_TriCeiling_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Triangle_Ceiling',
                         description='A stable metal-plated concrete ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Metal_Triangle_Ceiling.png')
    models.Structure.new(id=175, name='Metal Trapdoor', stack_size=100,
                         class_name='PrimalItemStructure_MetalTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalTrapdoor.PrimalItemStructure_MetalTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Metal_Trapdoor',
                         description='This metal-plated concrete slab can be used to secure hatches.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/Metal_Trapdoor.png')
    models.Structure.new(id=475, name='Metal Stairs', stack_size=100, class_name='PrimalItemStructure_Ramp_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Metal/PrimalItemStructure_Ramp_Metal.PrimalItemStructure_Ramp_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Stairs',
                         description='Metal-plated concrete stairs for travelling up or down levels. Can be switched to a ramp variant.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Metal_Stairs.png')
    models.Structure.new(id=292, name='Metal Spike Wall', stack_size=100,
                         class_name='PrimalItemStructure_MetalSpikeWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSpikeWall.PrimalItemStructure_MetalSpikeWall\'"',
                         url='https://ark.fandom.com/wiki/Metal_Spike_Wall',
                         description='These incredibly sharp metal spikes are dangerous to any that touch them. Large creatures take more damage.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Metal_Spike_Wall.png')
    models.Structure.new(id=214, name='Metal Sign', stack_size=100, class_name='PrimalItemStructure_MetalSign_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSign.PrimalItemStructure_MetalSign\'"',
                         url='https://ark.fandom.com/wiki/Metal_Sign',
                         description='A small metal sign for landmark navigation or relaying messages.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Metal_Sign.png')
    models.Structure.new(id=174, name='Metal Ramp', stack_size=100, class_name='PrimalItemStructure_MetalRamp_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalRamp.PrimalItemStructure_MetalRamp\'"',
                         url='https://ark.fandom.com/wiki/Metal_Ramp',
                         description='An inclined metal-plated concrete floor for travelling up or down levels. Can also be used to make an angled roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Metal_Ramp.png')
    models.Structure.new(id=173, name='Metal Pillar', stack_size=100, class_name='PrimalItemStructure_MetalPillar_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalPillar.PrimalItemStructure_MetalPillar\'"',
                         url='https://ark.fandom.com/wiki/Metal_Pillar',
                         description='This metal-plated concrete pillar adds structural integrity to the area it is built under. Can also act as stilts for building on inclines.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Metal_Pillar.png')
    models.Structure.new(id=172, name='Metal Ladder', stack_size=100, class_name='PrimalItemStructure_MetalLadder_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalLadder.PrimalItemStructure_MetalLadder\'"',
                         url='https://ark.fandom.com/wiki/Metal_Ladder',
                         description='A simple metal ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5e/Metal_Ladder.png')
    models.Structure.new(id=201, name='Metal Irrigation Pipe - Vertical', stack_size=100,
                         class_name='PrimalItemStructure_MetalPipeVertical_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeVertical.PrimalItemStructure_MetalPipeVertical\'"',
                         url='https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Vertical',
                         description='A vertical metal pipe for an irrigation network, used for transporting water up and down cliffs.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d9/Metal_Irrigation_Pipe_-_Vertical.png')
    models.Structure.new(id=200, name='Metal Irrigation Pipe - Tap', stack_size=100,
                         class_name='PrimalItemStructure_MetalPipeTap_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeTap.PrimalItemStructure_MetalPipeTap\'"',
                         url='https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Tap',
                         description='This metal tap allows access to the water in an irrigation network. Can refill containers, irrigate crop plots, or provide a refreshing drink.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Metal_Irrigation_Pipe_-_Tap.png')
    models.Structure.new(id=199, name='Metal Irrigation Pipe - Straight', stack_size=100,
                         class_name='PrimalItemStructure_MetalPipeStraight_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeStraight.PrimalItemStructure_MetalPipeStraight\'"',
                         url='https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Straight',
                         description='A straight metal pipe for an irrigation network, used for transporting water across land.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Metal_Irrigation_Pipe_-_Straight.png')
    models.Structure.new(id=198, name='Metal Irrigation Pipe - Intersection', stack_size=100,
                         class_name='PrimalItemStructure_MetalPipeIntersection_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeIntersection.PrimalItemStructure_MetalPipeIntersection\'"',
                         url='https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Intersection',
                         description='A plus-shaped metal intersection for an irrigation network, used for splitting one water source into three.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/77/Metal_Irrigation_Pipe_-_Intersection.png')
    models.Structure.new(id=197, name='Metal Irrigation Pipe - Intake', stack_size=100,
                         class_name='PrimalItemStructure_MetalPipeIntake_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeIntake.PrimalItemStructure_MetalPipeIntake\'"',
                         url='https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Intake',
                         description='The metal intake for an irrigation network that transports water over land.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Metal_Irrigation_Pipe_-_Intake.png')
    models.Structure.new(id=196, name='Metal Irrigation Pipe - Inclined', stack_size=100,
                         class_name='PrimalItemStructure_MetalPipeIncline_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeIncline.PrimalItemStructure_MetalPipeIncline\'"',
                         url='https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Inclined',
                         description='An inclined metal pipe for an irrigation network, used for transporting water up and down hills.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/19/Metal_Irrigation_Pipe_-_Inclined.png')
    models.Structure.new(id=472, name='Metal Irrigation Pipe - Flexible', stack_size=100,
                         class_name='PrimalItemStructure_PipeFlex_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Pipes/Flex/Metal/PrimalItemStructure_PipeFlex_Metal.PrimalItemStructure_PipeFlex_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Flexible',
                         description='Connects nearby pipes dynamically.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/db/Metal_Irrigation_Pipe_-_Flexible.png')
    models.Structure.new(id=166, name='Metal Hatchframe', stack_size=100,
                         class_name='PrimalItemStructure_MetalCeilingWithTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCeilingWithTrapdoor.PrimalItemStructure_MetalCeilingWithTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Metal_Hatchframe',
                         description='This metal-plated concrete ceiling has a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Metal_Hatchframe.png')
    models.Structure.new(id=169, name='Metal Foundation', stack_size=100, class_name='PrimalItemStructure_MetalFloor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalFloor.PrimalItemStructure_MetalFloor\'"',
                         url='https://ark.fandom.com/wiki/Metal_Foundation',
                         description='A foundation is required to build structures in an area. This one is made from sturdy metal-plated concrete.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Metal_Foundation.png')
    models.Structure.new(id=463, name='Metal Fence Support', stack_size=100,
                         class_name='PrimalItemStructure_FenceSupport_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Metal/PrimalItemStructure_FenceSupport_Metal.PrimalItemStructure_FenceSupport_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Fence_Support',
                         description="Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Metal_Fence_Support.png')
    models.Structure.new(id=168, name='Metal Fence Foundation', stack_size=100,
                         class_name='PrimalItemStructure_MetalFenceFoundation_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalFenceFoundation.PrimalItemStructure_MetalFenceFoundation\'"',
                         url='https://ark.fandom.com/wiki/Metal_Fence_Foundation',
                         description='This very strong, narrow foundation is used to build walls around an area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3d/Metal_Fence_Foundation.png')
    models.Structure.new(id=452, name='Metal Double Door', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoor_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Metal/PrimalItemStructure_DoubleDoor_Metal.PrimalItemStructure_DoubleDoor_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Double_Door',
                         description='A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e5/Metal_Double_Door.png')
    models.Structure.new(id=458, name='Metal Double Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoorframe_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Metal/PrimalItemStructure_DoubleDoorframe_Metal.PrimalItemStructure_DoubleDoorframe_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Double_Doorframe',
                         description='A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e5/Metal_Double_Door.png')
    models.Structure.new(id=167, name='Metal Door', stack_size=100, class_name='PrimalItemStructure_MetalDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalDoor.PrimalItemStructure_MetalDoor\'"',
                         url='https://ark.fandom.com/wiki/Metal_Door',
                         description='A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Metal_Door.png')
    models.Structure.new(id=177, name='Metal Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_MetalWallWithDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWallWithDoor.PrimalItemStructure_MetalWallWithDoor\'"',
                         url='https://ark.fandom.com/wiki/Metal_Doorframe',
                         description='A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Metal_Door.png')
    models.Structure.new(id=262, name='Metal Dinosaur Gate', stack_size=100,
                         class_name='PrimalItemStructure_MetalGate_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGate.PrimalItemStructure_MetalGate\'"',
                         url='https://ark.fandom.com/wiki/Metal_Dinosaur_Gate',
                         description='A large metal gate that can be used with a Gateway to keep most dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/26/Metal_Dinosaur_Gate.png')
    models.Structure.new(id=261, name='Metal Dinosaur Gateway', stack_size=100,
                         class_name='PrimalItemStructure_MetalGateframe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGateframe.PrimalItemStructure_MetalGateframe\'"',
                         url='https://ark.fandom.com/wiki/Metal_Dinosaur_Gateway',
                         description='A large metal gate that can be used with a Gateway to keep most dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/26/Metal_Dinosaur_Gate.png')
    models.Structure.new(id=165, name='Metal Ceiling', stack_size=100, class_name='PrimalItemStructure_MetalCeiling_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCeiling.PrimalItemStructure_MetalCeiling\'"',
                         url='https://ark.fandom.com/wiki/Metal_Ceiling',
                         description='A stable metal-plated concrete ceiling that provides insulation, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ac/Metal_Ceiling.png')
    models.Structure.new(id=164, name='Metal Catwalk', stack_size=100, class_name='PrimalItemStructure_MetalCatwalk_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCatwalk.PrimalItemStructure_MetalCatwalk\'"',
                         url='https://ark.fandom.com/wiki/Metal_Catwalk',
                         description='A thin walkway for bridging areas together. Made from metal plates.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Metal_Catwalk.png')
    models.Structure.new(id=239, name='Metal Billboard', stack_size=100,
                         class_name='PrimalItemStructure_MetalSign_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSign_Large.PrimalItemStructure_MetalSign_Large\'"',
                         url='https://ark.fandom.com/wiki/Metal_Billboard',
                         description='A large metal billboard for landmark navigation or relaying messages.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Metal_Billboard.png')
    models.Structure.new(id=244, name='Medium Crop Plot', stack_size=100,
                         class_name='PrimalItemStructure_CropPlot_Medium_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CropPlot_Medium.PrimalItemStructure_CropPlot_Medium\'"',
                         url='https://ark.fandom.com/wiki/Medium_Crop_Plot',
                         description='A medium garden plot, with a fence to keep out vermin.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Medium_Crop_Plot.png')
    models.Structure.new(id=471, name='Large Wooden Wall', stack_size=100,
                         class_name='PrimalItemStructure_LargeWall_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Wood/PrimalItemStructure_LargeWall_Wood.PrimalItemStructure_LargeWall_Wood\'"',
                         url='https://ark.fandom.com/wiki/Large_Wooden_Wall',
                         description='A sturdy wooden wall that insulates the inside from the outside, separates rooms, and provides structural integrity.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Wooden_Wall.png')
    models.Structure.new(id=470, name='Large Tek Wall', stack_size=100,
                         class_name='PrimalItemStructure_LargeWall_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Tek/PrimalItemStructure_LargeWall_Tek.PrimalItemStructure_LargeWall_Tek\'"',
                         url='https://ark.fandom.com/wiki/Large_Tek_Wall',
                         description='A composite Tek wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png')
    models.Structure.new(id=105, name='Large Storage Box', stack_size=100,
                         class_name='PrimalItemStructure_StorageBox_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StorageBox_Large.PrimalItemStructure_StorageBox_Large\'"',
                         url='https://ark.fandom.com/wiki/Large_Storage_Box',
                         description='A small box to store goods in.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Storage_Box.png')
    models.Structure.new(id=469, name='Large Stone Wall', stack_size=100,
                         class_name='PrimalItemStructure_LargeWall_Stone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Stone/PrimalItemStructure_LargeWall_Stone.PrimalItemStructure_LargeWall_Stone\'"',
                         url='https://ark.fandom.com/wiki/Large_Stone_Wall',
                         description='A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png')
    models.Structure.new(id=468, name='Large Metal Wall', stack_size=100,
                         class_name='PrimalItemStructure_LargeWall_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Metal/PrimalItemStructure_LargeWall_Metal.PrimalItemStructure_LargeWall_Metal\'"',
                         url='https://ark.fandom.com/wiki/Large_Metal_Wall',
                         description='A metal-plated concrete wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Metal_Wall.png')
    models.Structure.new(id=245, name='Large Crop Plot', stack_size=100,
                         class_name='PrimalItemStructure_CropPlot_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CropPlot_Large.PrimalItemStructure_CropPlot_Large\'"',
                         url='https://ark.fandom.com/wiki/Large_Crop_Plot',
                         description='A large garden plot, with a fence to keep out vermin.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Large_Crop_Plot.png')
    models.Structure.new(id=467, name='Large Adobe Wall', stack_size=100,
                         class_name='PrimalItemStructure_LargeWall_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Adobe/PrimalItemStructure_LargeWall_Adobe.PrimalItemStructure_LargeWall_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Large_Adobe_Wall_(Scorched_Earth)',
                         description='A wall that is as tall as four normal walls.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/10/Large_Adobe_Wall_%28Scorched_Earth%29.png')
    models.Structure.new(id=192, name='Lamppost', stack_size=100, class_name='PrimalItemStructure_Lamppost_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Lamppost.PrimalItemStructure_Lamppost\'"',
                         url='https://ark.fandom.com/wiki/Lamppost',
                         description='Requires electricity to activate. Lights an area without adding much heat.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Lamppost.png')
    models.Structure.new(id=356, name='Industrial Grill', stack_size=1, class_name='PrimalItemStructure_Grill_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Grill.PrimalItemStructure_Grill\'"',
                         url='https://ark.fandom.com/wiki/Industrial_Grill',
                         description='Perfect for cooking meat in bulk, staying warm, and providing light. Powered by Gasoline.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/90/Industrial_Grill.png')
    models.Structure.new(id=188, name='Inclined Electrical Cable', stack_size=100,
                         class_name='PrimalItemStructure_PowerCableIncline_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableIncline.PrimalItemStructure_PowerCableIncline\'"',
                         url='https://ark.fandom.com/wiki/Inclined_Electrical_Cable',
                         description='An inclined cable for transmitting electricity up and down hills.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Inclined_Electrical_Cable.png')
    models.Structure.new(id=41, name='Hide Sleeping Bag', stack_size=3,
                         class_name='PrimalItemStructure_SleepingBag_Hide_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_SleepingBag_Hide.PrimalItemStructure_SleepingBag_Hide\'"',
                         url='https://ark.fandom.com/wiki/Hide_Sleeping_Bag',
                         description='This hide sleeping bag acts as a single-use respawn point, only usable by you.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Hide_Sleeping_Bag.png')
    models.Structure.new(id=440, name='Greenhouse Window', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWindow.PrimalItemStructure_GreenhouseWindow\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Window',
                         description='Metal-framed, glass plates on hinges that cover windows to provide protection from projectiles and spying. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/35/Greenhouse_Window.png')
    models.Structure.new(id=433, name='Greenhouse Wall', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWall.PrimalItemStructure_GreenhouseWall\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Wall',
                         description='A metal-framed, glass wall that insulates the inside from the outside and separates rooms. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3c/Greenhouse_Wall.png')
    models.Structure.new(id=491, name='Greenhouse Triangle Roof', stack_size=100,
                         class_name='PrimalItemStructure_TriRoof_Greenhouse_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Greenhouse/PrimalItemStructure_TriRoof_Greenhouse.PrimalItemStructure_TriRoof_Greenhouse\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Triangle_Roof',
                         description='A sloped greenhouse triangle roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Greenhouse_Triangle_Roof.png')
    models.Structure.new(id=480, name='Greenhouse Triangle Ceiling', stack_size=100,
                         class_name='PrimalItemStructure_TriCeiling_Greenhouse_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Greenhouse/PrimalItemStructure_TriCeiling_Greenhouse.PrimalItemStructure_TriCeiling_Greenhouse\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Triangle_Ceiling',
                         description='A metal-framed, glass ceiling that insulates the inside from the outside, and doubles as a floor for higher levels. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/28/Greenhouse_Triangle_Ceiling.png')
    models.Structure.new(id=451, name='Greenhouse Double Door', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoor_Greenhouse_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Greenhouse/PrimalItemStructure_DoubleDoor_Greenhouse.PrimalItemStructure_DoubleDoor_Greenhouse\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Double_Door',
                         description='A metal-framed, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Greenhouse_Double_Door.png')
    models.Structure.new(id=457, name='Greenhouse Double Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoorframe_Greenhouse_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Greenhouse/PrimalItemStructure_DoubleDoorframe_Greenhouse.PrimalItemStructure_DoubleDoorframe_Greenhouse\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Double_Doorframe',
                         description='A metal-framed, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Greenhouse_Double_Door.png')
    models.Structure.new(id=436, name='Greenhouse Door', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseDoor.PrimalItemStructure_GreenhouseDoor\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Door',
                         description='A metal-frame, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Greenhouse_Door.png')
    models.Structure.new(id=435, name='Greenhouse Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseWallWithDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWallWithDoor.PrimalItemStructure_GreenhouseWallWithDoor\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Doorframe',
                         description='A metal-frame, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Greenhouse_Door.png')
    models.Structure.new(id=434, name='Greenhouse Ceiling', stack_size=100,
                         class_name='PrimalItemStructure_GreenhouseCeiling_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseCeiling.PrimalItemStructure_GreenhouseCeiling\'"',
                         url='https://ark.fandom.com/wiki/Greenhouse_Ceiling',
                         description='A metal-framed, glass ceiling that provides insulation, and doubles as a floor for higher levels. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Greenhouse_Ceiling.png')
    models.Structure.new(id=496, name='Flexible Electrical Cable', stack_size=100,
                         class_name='PrimalItemStructure_Wire_Flex_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Wires/Flex/PrimalItemStructure_Wire_Flex.PrimalItemStructure_Wire_Flex\'"',
                         url='https://ark.fandom.com/wiki/Flexible_Electrical_Cable',
                         description='Connects nearby cables dynamically',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9f/Flexible_Electrical_Cable.png')
    models.Structure.new(id=371, name='Feeding Trough', stack_size=100,
                         class_name='PrimalItemStructure_FeedingTrough_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_FeedingTrough.PrimalItemStructure_FeedingTrough\'"',
                         url='https://ark.fandom.com/wiki/Feeding_Trough',
                         description="Put food for your nearby pets in this, and they'll automatically eat it when hungry!",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Feeding_Trough.png')
    models.Structure.new(id=182, name='Fabricator', stack_size=1, class_name='PrimalItemStructure_Fabricator_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Fabricator.PrimalItemStructure_Fabricator\'"',
                         url='https://ark.fandom.com/wiki/Fabricator',
                         description='Place materials along with blueprints in this to create certain high-end machined items.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/66/Fabricator.png')
    models.Structure.new(id=187, name='Electrical Outlet', stack_size=100,
                         class_name='PrimalItemStructure_PowerOutlet_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerOutlet.PrimalItemStructure_PowerOutlet\'"',
                         url='https://ark.fandom.com/wiki/Electrical_Outlet',
                         description='An outlet for an electrical grid. When connected to a generator via cables, this provides power to all nearby devices that use electricity.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Electrical_Outlet.png')
    models.Structure.new(id=186, name='Electrical Generator', stack_size=100,
                         class_name='PrimalItemStructure_PowerGenerator_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerGenerator.PrimalItemStructure_PowerGenerator\'"',
                         url='https://ark.fandom.com/wiki/Electrical_Generator',
                         description='A large machine that converts gasoline into electricity.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Electrical_Generator.png')
    models.Structure.new(id=189, name='Electrical Cable Intersection', stack_size=100,
                         class_name='PrimalItemStructure_PowerCableIntersection_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableIntersection.PrimalItemStructure_PowerCableIntersection\'"',
                         url='https://ark.fandom.com/wiki/Electrical_Cable_Intersection',
                         description='A plus-shaped intersection for a power grid, used for splitting one power cable into three.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Electrical_Cable_Intersection.png')
    models.Structure.new(id=145, name='Dinosaur Gate', stack_size=100, class_name='PrimalItemStructure_WoodGate_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodGate.PrimalItemStructure_WoodGate\'"',
                         url='https://ark.fandom.com/wiki/Dinosaur_Gate',
                         description='A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png')
    models.Structure.new(id=142, name='Dinosaur Gateway', stack_size=100,
                         class_name='PrimalItemStructure_WoodGateframe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodGateframe.PrimalItemStructure_WoodGateframe\'"',
                         url='https://ark.fandom.com/wiki/Dinosaur_Gateway',
                         description='A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png')
    models.Structure.new(id=127, name='Cooking Pot', stack_size=100, class_name='PrimalItemStructure_CookingPot_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CookingPot.PrimalItemStructure_CookingPot\'"',
                         url='https://ark.fandom.com/wiki/Cooking_Pot',
                         description='Must contain basic fuel to light the fire. Put various ingredients with water in this to make soups, stews, and dyes.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Cooking_Pot.png')
    models.Structure.new(id=126, name='Compost Bin', stack_size=100, class_name='PrimalItemStructure_CompostBin_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CompostBin.PrimalItemStructure_CompostBin\'"',
                         url='https://ark.fandom.com/wiki/Compost_Bin',
                         description='A large bin for converting thatch and dung into high-quality fertilizer.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Compost_Bin.png')
    models.Structure.new(id=39, name='Campfire', stack_size=3, class_name='PrimalItemStructure_Campfire_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Campfire.PrimalItemStructure_Campfire\'"',
                         url='https://ark.fandom.com/wiki/Campfire',
                         description='Perfect for cooking meat, staying warm, and providing light.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Campfire.png')
    models.Structure.new(id=305, name='Bookshelf', stack_size=100, class_name='PrimalItemStructure_Bookshelf_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bookshelf.PrimalItemStructure_Bookshelf\'"',
                         url='https://ark.fandom.com/wiki/Bookshelf',
                         description='A large bookshelf to store Blueprints, Notes, and other small trinkets in.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Bookshelf.png')
    models.Structure.new(id=377, name='Behemoth Stone Dinosaur Gateway', stack_size=5,
                         class_name='PrimalItemStructure_StoneGateframe_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGateframe_Large.PrimalItemStructure_StoneGateframe_Large\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Stone_Dinosaur_Gateway',
                         description='A large brick-and-mortar gateway that can be used with a Gate to keep most dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Stone_Dinosaur_Gateway.png')
    models.Structure.new(id=378, name='Behemoth Reinforced Dinosaur Gate', stack_size=5,
                         class_name='PrimalItemStructure_StoneGateLarge_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGateLarge.PrimalItemStructure_StoneGateLarge\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Reinforced_Dinosaur_Gate',
                         description='A large, reinforced wooden gate that can be used with a Gateway to keep dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Reinforced_Dinosaur_Gate.png')
    models.Structure.new(id=170, name='Behemoth Gate', stack_size=5, class_name='PrimalItemStructure_MetalGate_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGate_Large.PrimalItemStructure_MetalGate_Large\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Gate',
                         description='A large metal-plated concrete gate that can be used with a Behemoth Gateway to allow even the largest of creatures in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Behemoth_Gate.png')
    models.Structure.new(id=171, name='Behemoth Gateway', stack_size=5,
                         class_name='PrimalItemStructure_MetalGateframe_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGateframe_Large.PrimalItemStructure_MetalGateframe_Large\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Gateway',
                         description='A large metal-plated concrete gate that can be used with a Behemoth Gateway to allow even the largest of creatures in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Behemoth_Gate.png')
    models.Structure.new(id=194, name='Auto Turret', stack_size=1, class_name='PrimalItemStructure_Turret_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Turret.PrimalItemStructure_Turret\'"',
                         url='https://ark.fandom.com/wiki/Auto_Turret',
                         description='Requires electricity to run. Consumes bullets while firing. Can be configured to automatically attack hostiles within range.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Auto_Turret.png')
    models.Structure.new(id=185, name='Air Conditioner', stack_size=1,
                         class_name='PrimalItemStructure_AirConditioner_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_AirConditioner.PrimalItemStructure_AirConditioner\'"',
                         url='https://ark.fandom.com/wiki/Air_Conditioner',
                         description='Requires electricity to run. Provides insulation from both the heat and the cold to an area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Air_Conditioner.png')
    models.Structure.new(id=490, name='Adobe Triangle Roof', stack_size=100,
                         class_name='PrimalItemStructure_TriRoof_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Adobe/PrimalItemStructure_TriRoof_Adobe.PrimalItemStructure_TriRoof_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Triangle_Roof_(Scorched_Earth)',
                         description='A sloped adobe triangle roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5f/Adobe_Triangle_Roof_%28Scorched_Earth%29.png')
    models.Structure.new(id=485, name='Adobe Triangle Foundation', stack_size=100,
                         class_name='PrimalItemStructure_TriFoundation_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Adobe/PrimalItemStructure_TriFoundation_Adobe.PrimalItemStructure_TriFoundation_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Triangle_Foundation_(Scorched_Earth)',
                         description='Required to build structures in an area. Triangle shaped.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/da/Adobe_Triangle_Foundation_%28Scorched_Earth%29.png')
    models.Structure.new(id=479, name='Adobe Triangle Ceiling', stack_size=100,
                         class_name='PrimalItemStructure_TriCeiling_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Adobe/PrimalItemStructure_TriCeiling_Adobe.PrimalItemStructure_TriCeiling_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Triangle_Ceiling_(Scorched_Earth)',
                         description='A stable adobe-plated concrete ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/24/Adobe_Triangle_Ceiling_%28Scorched_Earth%29.png')
    models.Structure.new(id=474, name='Adobe Stairs', stack_size=100, class_name='PrimalItemStructure_Ramp_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Adobe/PrimalItemStructure_Ramp_Adobe.PrimalItemStructure_Ramp_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Stairs_(Scorched_Earth)',
                         description='Adobe-plated concrete stairs for travelling up or down levels. Can be switched to a ramp variant.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/28/Adobe_Stairs_%28Scorched_Earth%29.png')
    models.Structure.new(id=462, name='Adobe Fence Support', stack_size=100,
                         class_name='PrimalItemStructure_FenceSupport_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Adobe/PrimalItemStructure_FenceSupport_Adobe.PrimalItemStructure_FenceSupport_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Fence_Support_(Scorched_Earth)',
                         description="Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Adobe_Fence_Support_%28Scorched_Earth%29.png')
    models.Structure.new(id=450, name='Adobe Double Door', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoor_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Adobe/PrimalItemStructure_DoubleDoor_Adobe.PrimalItemStructure_DoubleDoor_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Double_Door_(Scorched_Earth)',
                         description='A stable adobe door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/77/Adobe_Double_Door_%28Scorched_Earth%29.png')
    models.Structure.new(id=456, name='Adobe Double Doorframe', stack_size=100,
                         class_name='PrimalItemStructure_DoubleDoorframe_Adobe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Adobe/PrimalItemStructure_DoubleDoorframe_Adobe.PrimalItemStructure_DoubleDoorframe_Adobe\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Double_Doorframe_(Scorched_Earth)',
                         description='A stable adobe door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/77/Adobe_Double_Door_%28Scorched_Earth%29.png')
    models.Structure.new(name='Pumpkin', stack_size=100, class_name=None,
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_Pumpkin.PrimalItemStructure_Pumpkin\'"',
                         url='https://ark.fandom.com/wiki/Pumpkin',
                         description='Decorate your base with this pumpkin. Can be "carved" with all manner of paints.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/64/Pumpkin.png')
    models.Structure.new(name='Scarecrow', stack_size=100, class_name=None,
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_Scarecrow.PrimalItemStructure_Scarecrow\'"',
                         url='https://ark.fandom.com/wiki/Scarecrow',
                         description='Decorate your base with this scarecrow. Guaranteed to scare the crows away.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/75/Scarecrow.png')
    models.Structure.new(name='Stolen Headstone', stack_size=100, class_name=None,
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_HW_Grave.PrimalItemStructure_HW_Grave\'"',
                         url='https://ark.fandom.com/wiki/Stolen_Headstone',
                         description='A headstone stolen from a graveyard.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Stolen_Headstone.png')
    models.Structure.new(name='Wreath', stack_size=100, class_name='PrimalItemStructure_Wreath_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_Wreath.PrimalItemStructure_Wreath\'"',
                         url='https://ark.fandom.com/wiki/Wreath',
                         description='A decorative collection of leaves that make any room festive. Requires attaching to a wall.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/de/Wreath.png')
    models.Structure.new(name='Holiday Lights', stack_size=100, class_name='PrimalItemStructure_XmasLights_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_XmasLights.PrimalItemStructure_XmasLights\'"',
                         url='https://ark.fandom.com/wiki/Holiday_Lights',
                         description='A decoration string of lights that make any room festive. Requires attaching to a wall.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Holiday_Lights.png')
    models.Structure.new(name='Holiday Stocking', stack_size=100, class_name='PrimalItemStructure_Stocking_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_Stocking.PrimalItemStructure_Stocking\'"',
                         url='https://ark.fandom.com/wiki/Holiday_Stocking',
                         description='An oversized sock which adds jolliness to any holiday. Requires attaching to a wall.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Holiday_Stocking.png')
    models.Structure.new(name='Holiday Tree', stack_size=100, class_name='PrimalItemStructure_ChristmasTree_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_ChristmasTree.PrimalItemStructure_ChristmasTree\'"',
                         url='https://ark.fandom.com/wiki/Holiday_Tree',
                         description='This is the perfect tree to use when celebrating the winter solstace!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Holiday_Tree.png')
    models.Structure.new(name='Snowman', stack_size=100, class_name='PrimalItemStructure_Snowman_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_Snowman.PrimalItemStructure_Snowman\'"',
                         url='https://ark.fandom.com/wiki/Snowman', description='Put a hat on it for extra fun!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Snowman.png')
    models.Structure.new(name='Gift Box', stack_size=100, class_name='PrimalItemStructure_StorageBox_ChristmasGift_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_StorageBox_ChristmasGift.PrimalItemStructure_StorageBox_ChristmasGift\'"',
                         url='https://ark.fandom.com/wiki/Gift_Box',
                         description="Put items in this and inscribe a Tribemember's name, and only they will be able to open it, with a bang!",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/56/Gift_Box.png')
    models.Structure.new(name='Bunny Egg', stack_size=100, class_name='PrimalItemStructure_EasterEgg_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_EasterEgg.PrimalItemStructure_EasterEgg\'"',
                         url='https://ark.fandom.com/wiki/Bunny_Egg',
                         description='Put it in a Cooking Pot to craft fun costumes or place on the ground as a festive decoration!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4d/Bunny_Egg.png')
    models.Structure.new(name='Birthday Cake', stack_size=100, class_name=None,
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_BirthdayCake.PrimalItemStructure_BirthdayCake\'"',
                         url='https://ark.fandom.com/wiki/Birthday_Cake',
                         description='Place this Cake on a table and blow out its candles to make a wish (then eat it). Or you can put it in a Cooking Pot for...',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Birthday_Cake.png')
    models.Structure.new(name='Adobe Ceiling', stack_size=100, class_name='PrimalItemStructure_AdobeCeiling_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeiling.PrimalItemStructure_AdobeCeiling\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Ceiling_(Scorched_Earth)',
                         description='A stable adobe-plated concrete ceiling that provides insulation, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/64/Adobe_Ceiling_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Dinosaur Gate', stack_size=100, class_name='PrimalItemStructure_AdobeGateDoor_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeGateDoor.PrimalItemStructure_AdobeGateDoor\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Dinosaur_Gate_(Scorched_Earth)',
                         description='A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png')
    models.Structure.new(name='Adobe Dinosaur Gateway', stack_size=100,
                         class_name='PrimalItemStructure_AdobeFrameGate_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeFrameGate.PrimalItemStructure_AdobeFrameGate\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Dinosaur_Gateway_(Scorched_Earth)',
                         description='A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png')
    models.Structure.new(name='Adobe Door', stack_size=100, class_name='PrimalItemStructure_AdobeDoor_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeDoor.PrimalItemStructure_AdobeDoor\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Door_(Scorched_Earth)',
                         description='A stable adobe door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Adobe_Door_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Doorframe', stack_size=100, class_name='PrimalItemStructure_AdobeWallWithDoor_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWallWithDoor.PrimalItemStructure_AdobeWallWithDoor\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Doorframe_(Scorched_Earth)',
                         description='A adobe wall that provides entrance to a structure.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Adobe_Doorframe_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Fence Foundation', stack_size=100,
                         class_name='PrimalItemStructure_AdobeFenceFoundation_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeFenceFoundation.PrimalItemStructure_AdobeFenceFoundation\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Fence_Foundation_(Scorched_Earth)',
                         description='This very strong, narrow foundation is used to build walls around an area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Adobe_Fence_Foundation_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Foundation', stack_size=100, class_name='PrimalItemStructure_AdobeFloor_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeFloor.PrimalItemStructure_AdobeFloor\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Foundation_(Scorched_Earth)',
                         description='Required to build structures in an area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/55/Adobe_Foundation_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Hatchframe', stack_size=100,
                         class_name='PrimalItemStructure_AdobeCeilingWithTrapdoor_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeilingWithTrapdoor.PrimalItemStructure_AdobeCeilingWithTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Hatchframe_(Scorched_Earth)',
                         description='This Adobe concrete ceiling has a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3f/Adobe_Hatchframe_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Ladder', stack_size=100, class_name='PrimalItemStructure_AdobeLader_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeLader.PrimalItemStructure_AdobeLader\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Ladder_(Scorched_Earth)',
                         description='A simple adobe ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Adobe_Ladder_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Pillar', stack_size=100, class_name='PrimalItemStructure_AdobePillar_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobePillar.PrimalItemStructure_AdobePillar\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Pillar_(Scorched_Earth)',
                         description='The adobe pillar adds structural integrity to the area it is built under. Can also act as stilts for buildings on inclines.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Adobe_Pillar_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Railing', stack_size=100, class_name='PrimalItemStructure_AdobeRailing_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeRailing.PrimalItemStructure_AdobeRailing\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Railing_(Scorched_Earth)',
                         description='A adobe railing that acts a a simple barrier to prevent people from falling.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Adobe_Railing_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Ramp', stack_size=100, class_name='PrimalItemStructure_AdobeRamp_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeRamp.PrimalItemStructure_AdobeRamp\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Ramp_(Scorched_Earth)',
                         description='An inclined adobe-plated concrete floor for travelling up or down levels. Can also be used to make an angled roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c0/Adobe_Ramp_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Staircase', stack_size=100, class_name='PrimalItemStructure_AdobeStaircase_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeStaircase.PrimalItemStructure_AdobeStaircase\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Staircase_(Scorched_Earth)',
                         description='An adobe spiral staircase, useful in constructing multi-level buildings.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Adobe_Staircase_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Trapdoor', stack_size=100, class_name='PrimalItemStructure_AdobeTrapdoor_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeTrapdoor.PrimalItemStructure_AdobeTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Trapdoor_(Scorched_Earth)',
                         description='This adobe slab can be used to secure hatches.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/46/Adobe_Trapdoor_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Wall', stack_size=100, class_name='PrimalItemStructure_AdobeWall_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWall.PrimalItemStructure_AdobeWall\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Wall_(Scorched_Earth)',
                         description='An adobe wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Adobe_Wall_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Window', stack_size=100, class_name='PrimalItemStructure_AdobeWindow_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWindow.PrimalItemStructure_AdobeWindow\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Window_(Scorched_Earth)',
                         description='Adobe plates on hinges that cover windows to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Adobe_Window_%28Scorched_Earth%29.png')
    models.Structure.new(name='Adobe Windowframe', stack_size=100,
                         class_name='PrimalItemStructure_AdobeWallWithWindow_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWallWithWindow.PrimalItemStructure_AdobeWallWithWindow\'"',
                         url='https://ark.fandom.com/wiki/Adobe_Windowframe_(Scorched_Earth)',
                         description='An adobe wall, with a hole for a window.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/86/Adobe_Windowframe_%28Scorched_Earth%29.png')
    models.Structure.new(name='Artifact Pedestal', stack_size=100, class_name='PrimalItemStructure_TrophyBase_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TrophyBase.PrimalItemStructure_TrophyBase\'"',
                         url='https://ark.fandom.com/wiki/Artifact_Pedestal',
                         description='Provides the base upon which you can proudly display an Artifact, among other things!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Artifact_Pedestal.png')
    models.Structure.new(name='Ballista Turret', stack_size=1, class_name='PrimalItemStructure_TurretBallista_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretBallista.PrimalItemStructure_TurretBallista\'"',
                         url='https://ark.fandom.com/wiki/Ballista_Turret',
                         description='Mount this to fire large piercing Spear Bolts, useful for bringing down large dinos and structures.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Ballista_Turret.png')
    models.Structure.new(name='Bee Hive', stack_size=1, class_name='PrimalItemStructure_BeeHive_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/Structures/BeeHive/PrimalItemStructure_BeeHive.PrimalItemStructure_BeeHive\'"',
                         url='https://ark.fandom.com/wiki/Bee_Hive',
                         description='Bee hives house a queen bee and produces honey.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Bee_Hive.png')
    models.Structure.new(name='Beer Barrel', stack_size=3, class_name='PrimalItemStructure_BeerBarrel_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_BeerBarrel.PrimalItemStructure_BeerBarrel\'"',
                         url='https://ark.fandom.com/wiki/Beer_Barrel',
                         description='Ferments tasty brew from Thatch, Water, and Berries',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Beer_Barrel.png')
    models.Structure.new(name='Behemoth Adobe Dinosaur Gate', stack_size=5,
                         class_name='PrimalItemStructure_AdobeGateDoor_Large_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeGateDoor_Large.PrimalItemStructure_AdobeGateDoor_Large\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Adobe_Dinosaur_Gate_(Scorched_Earth)',
                         description='A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png')
    models.Structure.new(name='Behemoth Adobe Dinosaur Gateway', stack_size=5,
                         class_name='PrimalItemStructure_AdobeGateframe_Large_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeGateframe_Large.PrimalItemStructure_AdobeGateframe_Large\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Adobe_Dinosaur_Gateway_(Scorched_Earth)',
                         description='A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png')
    models.Structure.new(name='Behemoth Tek Gateway', stack_size=5,
                         class_name='PrimalItemStructure_TekGateframe_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGateframe_Large.PrimalItemStructure_TekGateframe_Large\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Tek_Gateway',
                         description='A large composite Tek gate that can be used with a Behemoth Gateway to allow even the largest creatures in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Behemoth_Tek_Gate.png')
    models.Structure.new(name='Behemoth Tek Gate', stack_size=5, class_name='PrimalItemStructure_TekGate_Large_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGate_Large.PrimalItemStructure_TekGate_Large\'"',
                         url='https://ark.fandom.com/wiki/Behemoth_Tek_Gate',
                         description='A large composite Tek gate that can be used with a Behemoth Gateway to allow even the largest creatures in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Behemoth_Tek_Gate.png')
    models.Structure.new(name='Bunk Bed', stack_size=3, class_name='PrimalItemStructure_Bed_Modern_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bed_Modern.PrimalItemStructure_Bed_Modern\'"',
                         url='https://ark.fandom.com/wiki/Bunk_Bed',
                         description='This modern bunk-style bed has two mattresses, and a high thread count. Acts as a respawn point for you and your tribe with half cooldown time.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Bunk_Bed.png')
    models.Structure.new(name='Cannon', stack_size=1, class_name='PrimalItemStructure_Cannon_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Cannon.PrimalItemStructure_Cannon\'"',
                         url='https://ark.fandom.com/wiki/Cannon',
                         description='A powerful, heavy weapon of war, capable of demolishing heavily reinforced structures.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Cannon.png')
    models.Structure.new(name='Catapult Turret', stack_size=1, class_name='PrimalItemStructure_TurretCatapult_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretCatapult.PrimalItemStructure_TurretCatapult\'"',
                         url='https://ark.fandom.com/wiki/Catapult_Turret',
                         description='Mount this to throw destructive Boulders at your enemies, particularly effective against Structures.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Catapult_Turret.png')
    models.Structure.new(name='Chemistry Bench', stack_size=1, class_name='PrimalItemStructure_ChemBench_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_ChemBench.PrimalItemStructure_ChemBench\'"',
                         url='https://ark.fandom.com/wiki/Chemistry_Bench',
                         description='Place materials in this to transmute chemical substances with extreme efficiency!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9d/Chemistry_Bench.png')
    models.Structure.new(name='Cloning Chamber', stack_size=1, class_name='PrimalItemStructure_TekCloningChamber_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_TekCloningChamber.PrimalItemStructure_TekCloningChamber\'"',
                         url='https://ark.fandom.com/wiki/Cloning_Chamber',
                         description='Enables you to generate clones of your creatures!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Cloning_Chamber.png')
    models.Structure.new(name='Cryofridge', stack_size=1, class_name='PrimalItemStructure_CryoFridge_C',
                         blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_CryoFridge.PrimalItemStructure_CryoFridge\'"',
                         url='https://ark.fandom.com/wiki/Cryofridge_(Extinction)',
                         description='Requires electricity to run. Keeps Cryopods alive forever!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Cryofridge.png')
    models.Structure.new(name='Crystal Wyvern Queen Flag', stack_size=100,
                         class_name='PrimalItemStructure_Flag_CIBoss_C',
                         blueprint='"Blueprint\'/Game/Mods/CrystalIsles/Assets/Dinos/CIBoss/Trophy/PrimalItemStructure_Flag_CIBoss.PrimalItemStructure_Flag_CIBoss\'"',
                         url='https://ark.fandom.com/wiki/Crystal_Wyvern_Queen_Flag_(Crystal_Isles)',
                         description='This flag is proof that you have defeated the Crystal Wyvern Queen.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9c/Crystal_Wyvern_Queen_Flag_%28Crystal_Isles%29.png')
    models.Structure.new(name='Delivery Crate', stack_size=100, class_name='PrimalItemStructure_StorageBox_Balloon_C',
                         blueprint='"Blueprint\'/Game/Extinction/Structures/ItemBalloon/PrimalItemStructure_StorageBox_Balloon.PrimalItemStructure_StorageBox_Balloon\'"',
                         url='https://ark.fandom.com/wiki/Delivery_Crate_(Extinction)',
                         description='A box with a Gasbag attached that can be used to deliver items to another location.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/85/Delivery_Crate_%28Extinction%29.png')
    models.Structure.new(name='Dino Leash', stack_size=100, class_name='PrimalItemStructure_DinoLeash_C',
                         blueprint='"Blueprint\'/Game/Extinction/Structures/DinoLeash/PrimalItemStructure_DinoLeash.PrimalItemStructure_DinoLeash\'"',
                         url='https://ark.fandom.com/wiki/Dino_Leash_(Extinction)',
                         description='Electronic leash to keep your dinos from wandering too far.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Dino_Leash_%28Extinction%29.png')
    models.Structure.new(name='Dragon Flag', stack_size=100, class_name='PrimalItemStructure_Flag_Dragon_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Dragon.PrimalItemStructure_Flag_Dragon\'"',
                         url='https://ark.fandom.com/wiki/Dragon_Flag',
                         description='This flag is proof that you have defeated the Dragon.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/33/Dragon_Flag.png')
    models.Structure.new(name='Elevator Track', stack_size=100, class_name='PrimalItemStructure_ElevatorTrackBase_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorTrackBase.PrimalItemStructure_ElevatorTrackBase\'"',
                         url='https://ark.fandom.com/wiki/Elevator_Track',
                         description='Attach an Elevator Platform to these to complete an elevator!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Elevator_Track.png')
    models.Structure.new(name='Fish Basket', stack_size=5, class_name='PrimalItemStructure_FishBasket_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_FishBasket.PrimalItemStructure_FishBasket\'"',
                         url='https://ark.fandom.com/wiki/Fish_Basket_(Aberration)',
                         description='Trap certain fish in this basket to tame and transport them!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/68/Fish_Basket_%28Aberration%29.png')
    models.Structure.new(name='Gas Collector', stack_size=1, class_name='PrimalItemStructure_GasCollector_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/GasCollector/PrimalItemStructure_GasCollector.PrimalItemStructure_GasCollector\'"',
                         url='https://ark.fandom.com/wiki/Gas_Collector_(Aberration)',
                         description='Place on a Gas Vent to extract Congealed Gas Balls over time.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Gas_Collector_%28Aberration%29.png')
    models.Structure.new(name='Giant Adobe Hatchframe', stack_size=5,
                         class_name='PrimalItemStructure_AdobeCeilingWithDoorWay_Giant_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeilingWithDoorWay_Giant.PrimalItemStructure_AdobeCeilingWithDoorWay_Giant\'"',
                         url='https://ark.fandom.com/wiki/Giant_Adobe_Hatchframe_(Scorched_Earth)',
                         description='This Giant Adobe concrete ceiling has a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Giant_Adobe_Hatchframe_%28Scorched_Earth%29.png')
    models.Structure.new(name='Giant Adobe Trapdoor', stack_size=5,
                         class_name='PrimalItemStructure_AdobeCeilingDoorGiant_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeilingDoorGiant.PrimalItemStructure_AdobeCeilingDoorGiant\'"',
                         url='https://ark.fandom.com/wiki/Giant_Adobe_Trapdoor_(Scorched_Earth)',
                         description='A large adobe gate that can be used with a Gateway to most keep dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Giant_Adobe_Trapdoor_%28Scorched_Earth%29.png')
    models.Structure.new(name='Giant Metal Hatchframe', stack_size=5,
                         class_name='PrimalItemStructure_MetalCeilingWithTrapdoorGiant_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCeilingWithTrapdoorGiant.PrimalItemStructure_MetalCeilingWithTrapdoorGiant\'"',
                         url='https://ark.fandom.com/wiki/Giant_Metal_Hatchframe',
                         description='This metal-plated concrete ceiling has a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Metal_Hatchframe.png')
    models.Structure.new(name='Giant Metal Trapdoor', stack_size=5,
                         class_name='PrimalItemStructure_MetalTrapdoorGiant_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalTrapdoorGiant.PrimalItemStructure_MetalTrapdoorGiant\'"',
                         url='https://ark.fandom.com/wiki/Giant_Metal_Trapdoor',
                         description='This metal-plated concrete slab can be used to secure hatches.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/Metal_Trapdoor.png')
    models.Structure.new(name='Giant Reinforced Trapdoor', stack_size=5,
                         class_name='PrimalItemStructure_StoneCeilingDoorGiant_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeilingDoorGiant.PrimalItemStructure_StoneCeilingDoorGiant\'"',
                         url='https://ark.fandom.com/wiki/Giant_Reinforced_Trapdoor',
                         description='This small reinforced door can be used to secure hatches.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Reinforced_Trapdoor.png')
    models.Structure.new(name='Giant Stone Hatchframe', stack_size=5,
                         class_name='PrimalItemStructure_StoneCeilingWithTrapdoorGiant_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeilingWithTrapdoorGiant.PrimalItemStructure_StoneCeilingWithTrapdoorGiant\'"',
                         url='https://ark.fandom.com/wiki/Giant_Stone_Hatchframe',
                         description='This brick-and-mortar ceiling has a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Stone_Hatchframe.png')
    models.Structure.new(name='Gorilla Flag', stack_size=100, class_name='PrimalItemStructure_Flag_Gorilla_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Gorilla.PrimalItemStructure_Flag_Gorilla\'"',
                         url='https://ark.fandom.com/wiki/Gorilla_Flag',
                         description='This flag is proof that you have defeated the Megapithecus.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9f/Gorilla_Flag.png')
    models.Structure.new(name='Gravestone', stack_size=100, class_name='PrimalItemStructure_Furniture_Gravestone_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_Gravestone.PrimalItemStructure_Furniture_Gravestone\'"',
                         url='https://ark.fandom.com/wiki/Gravestone',
                         description='A simple unadorned stone headstone to mark a grave or commemorate a loved one.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Gravestone.png')
    models.Structure.new(name='Heavy Auto Turret', stack_size=1, class_name='PrimalItemStructure_HeavyTurret_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_HeavyTurret.PrimalItemStructure_HeavyTurret\'"',
                         url='https://ark.fandom.com/wiki/Heavy_Auto_Turret',
                         description='Requires electricity to run. Provides increased firepower, but consumes FOUR bullets while firing. Can be configured to automatically attack hostiles within range.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7f/Heavy_Auto_Turret.png')
    models.Structure.new(name='Homing Underwater Mine', stack_size=10, class_name='PrimalItemStructure_SeaMine_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_SeaMine.PrimalItemStructure_SeaMine\'"',
                         url='https://ark.fandom.com/wiki/Homing_Underwater_Mine',
                         description='Place this underwater to create an explosive trap that floats, homes, explodes when touched.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Homing_Underwater_Mine.png')
    models.Structure.new(name='Industrial Cooker', stack_size=1,
                         class_name='PrimalItemStructure_IndustrialCookingPot_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_IndustrialCookingPot.PrimalItemStructure_IndustrialCookingPot\'"',
                         url='https://ark.fandom.com/wiki/Industrial_Cooker',
                         description='Burns Gasoline to cook large quantities of food quickly. Put various ingredients in this to make soups, stews, and dyes.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/91/Industrial_Cooker.png')
    models.Structure.new(name='Industrial Forge', stack_size=1, class_name='PrimalItemStructure_IndustrialForge_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_IndustrialForge.PrimalItemStructure_IndustrialForge\'"',
                         url='https://ark.fandom.com/wiki/Industrial_Forge', description=None,
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c5/Industrial_Forge.png')
    models.Structure.new(name='Industrial Grinder', stack_size=1, class_name='PrimalItemStructure_Grinder_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Grinder.PrimalItemStructure_Grinder\'"',
                         url='https://ark.fandom.com/wiki/Industrial_Grinder',
                         description='Grind up crafted items and certain resources!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Industrial_Grinder.png')
    models.Structure.new(name='King Titan Flag', stack_size=100, class_name='PrimalItemStructure_Flag_KingKaiju_C',
                         blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Trophies/PrimalItemStructure_Flag_KingKaiju.PrimalItemStructure_Flag_KingKaiju\'"',
                         url='https://ark.fandom.com/wiki/King_Titan_Flag_(Extinction)',
                         description='This flag is proof that you have defeated the King of the Titans.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/King_Titan_Flag_%28Extinction%29.png')
    models.Structure.new(name='King Titan Flag (Mecha)', stack_size=100,
                         class_name='PrimalItemStructure_Flag_KingKaijuMecha_C',
                         blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Trophies/PrimalItemStructure_Flag_KingKaijuMecha.PrimalItemStructure_Flag_KingKaijuMecha\'"',
                         url='https://ark.fandom.com/wiki/King_Titan_Flag_(Mecha)_(Extinction)',
                         description='This flag is proof that you have defeated the King of the Titans.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/79/King_Titan_Flag_%28Mecha%29_%28Extinction%29.png')
    models.Structure.new(name='Large Elevator Platform', stack_size=1,
                         class_name='PrimalItemStructure_ElevatorPlatformLarge_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorPlatformLarge.PrimalItemStructure_ElevatorPlatformLarge\'"',
                         url='https://ark.fandom.com/wiki/Large_Elevator_Platform',
                         description='Attach to an Elevator Track to carry a large amount of weight.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Large_Elevator_Platform.png')
    models.Structure.new(name='Large Taxidermy Base', stack_size=100,
                         class_name='PrimalItemStructure_TaxidermyBase_Large_C',
                         blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_TaxidermyBase_Large.PrimalItemStructure_TaxidermyBase_Large\'"',
                         url='https://ark.fandom.com/wiki/Large_Taxidermy_Base_(Extinction)',
                         description='Place a harvested dermis to show off your prowess!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/ff/Large_Taxidermy_Base_%28Extinction%29.png')
    models.Structure.new(name='Large Wood Elevator Platform', stack_size=100,
                         class_name='PrimalItemStructure_WoodElevatorPlatform_Large_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorPlatform_Large.PrimalItemStructure_WoodElevatorPlatform_Large\'"',
                         url='https://ark.fandom.com/wiki/Large_Wood_Elevator_Platform_(Aberration)',
                         description='Attach to an Elevator Track to lift a large amount of weight.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Large_Wood_Elevator_Platform_%28Aberration%29.png')
    models.Structure.new(name='Manticore Flag', stack_size=100, class_name='PrimalItemStructure_Flag_Manticore_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/ManticoreFlag/PrimalItemStructure_Flag_Manticore.PrimalItemStructure_Flag_Manticore\'"',
                         url='https://ark.fandom.com/wiki/Manticore_Flag_(Scorched_Earth)',
                         description='This flag is proof that you have defeated the Manticore.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e0/Manticore_Flag_%28Scorched_Earth%29.png')
    models.Structure.new(name='Medium Elevator Platform', stack_size=1,
                         class_name='PrimalItemStructure_ElevatorPlatfromMedium_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorPlatfromMedium.PrimalItemStructure_ElevatorPlatfromMedium\'"',
                         url='https://ark.fandom.com/wiki/Medium_Elevator_Platform',
                         description='Attach to an Elevator Track to carry a medium amount of weight.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/80/Medium_Elevator_Platform.png')
    models.Structure.new(name='Medium Taxidermy Base', stack_size=100,
                         class_name='PrimalItemStructure_TaxidermyBase_Medium_C',
                         blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_TaxidermyBase_Medium.PrimalItemStructure_TaxidermyBase_Medium\'"',
                         url='https://ark.fandom.com/wiki/Medium_Taxidermy_Base_(Extinction)',
                         description='Place a harvested dermis to show off your prowess!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Medium_Taxidermy_Base_%28Extinction%29.png')
    models.Structure.new(name='Medium Wood Elevator Platform', stack_size=100,
                         class_name='PrimalItemStructure_WoodElevatorPlatform_Medium_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorPlatform_Medium.PrimalItemStructure_WoodElevatorPlatform_Medium\'"',
                         url='https://ark.fandom.com/wiki/Medium_Wood_Elevator_Platform_(Aberration)',
                         description='Attach to an Elevator Track to lift a medium amount of weight.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5b/Medium_Wood_Elevator_Platform_%28Aberration%29.png')
    models.Structure.new(name='Metal Cliff Platform', stack_size=3,
                         class_name='PrimalItemStructure_Metal_CliffPlatform_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/CliffPlatforms/Metal_CliffPlatform/PrimalItemStructure_Metal_CliffPlatform.PrimalItemStructure_Metal_CliffPlatform\'"',
                         url='https://ark.fandom.com/wiki/Metal_Cliff_Platform_(Aberration)',
                         description='A Cliff Platform is required to build structures extending from a cliff. This one is made from shiny metal.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Metal_Cliff_Platform_%28Aberration%29.png')
    models.Structure.new(name='Metal Ocean Platform', stack_size=3,
                         class_name='PrimalItemStructure_Metal_OceanPlatform_C',
                         blueprint='"Blueprint\'/Game/Genesis/Structures/OceanPlatform/OceanPlatform_Wood/PrimalItemStructure_Metal_OceanPlatform.PrimalItemStructure_Metal_OceanPlatform\'"',
                         url='https://ark.fandom.com/wiki/Metal_Ocean_Platform_(Genesis:_Part_1)',
                         description='Floats on the surface of bodies of water.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Metal_Ocean_Platform_%28Genesis_Part_1%29.png')
    models.Structure.new(name='Metal Railing', stack_size=100, class_name='PrimalItemStructure_MetalRailing_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalRailing.PrimalItemStructure_MetalRailing\'"',
                         url='https://ark.fandom.com/wiki/Metal_Railing',
                         description='A metal-plated concrete railing that acts as a simple barrier to prevent people from falling.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/85/Metal_Railing.png')
    models.Structure.new(name='Metal Staircase', stack_size=100, class_name='PrimalItemStructure_MetalStairs_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalStairs.PrimalItemStructure_MetalStairs\'"',
                         url='https://ark.fandom.com/wiki/Metal_Staircase',
                         description='A metal spiral staircase, useful in constructing multi-level buildings.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Metal_Staircase.png')
    models.Structure.new(name='Metal Tree Platform', stack_size=1,
                         class_name='PrimalItemStructure_TreePlatform_Metal_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_TreePlatform_Metal.PrimalItemStructure_TreePlatform_Metal\'"',
                         url='https://ark.fandom.com/wiki/Metal_Tree_Platform',
                         description='Attaches to a large tree, enabling you to build on it.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cc/Metal_Tree_Platform.png')
    models.Structure.new(name='Minigun Turret', stack_size=1, class_name='PrimalItemStructure_TurretMinigun_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretMinigun.PrimalItemStructure_TurretMinigun\'"',
                         url='https://ark.fandom.com/wiki/Minigun_Turret',
                         description='Mount this to fire a hail of Advanced Rifle Bullets at your enemies. Powered by the rider.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b6/Minigun_Turret.png')
    models.Structure.new(name='Mirror', stack_size=100, class_name='PrimalItemStructure_Mirror_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/DesertFurnitureSet/Mirror/PrimalItemStructure_Mirror.PrimalItemStructure_Mirror\'"',
                         url='https://ark.fandom.com/wiki/Mirror_(Scorched_Earth)',
                         description='Put it on a wall, and look at your beautiful self!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4d/Mirror_%28Scorched_Earth%29.png')
    models.Structure.new(name='Moeder Flag', stack_size=100, class_name='PrimalItemStructure_Flag_EelBoss_C',
                         blueprint='"Blueprint\'/Game/Genesis/CoreBlueprints/Structures/PrimalItemStructure_Flag_EelBoss.PrimalItemStructure_Flag_EelBoss\'"',
                         url='https://ark.fandom.com/wiki/Moeder_Flag_(Genesis:_Part_1)',
                         description='This flag is proof that you have defeated Moeder.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b6/Moeder_Flag_%28Genesis_Part_1%29.png')
    models.Structure.new(name='Motorboat', stack_size=1, class_name='PrimalItemMotorboat_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/Items/Raft/PrimalItemMotorboat.PrimalItemMotorboat\'"',
                         url='https://ark.fandom.com/wiki/Motorboat',
                         description='A floating metal platform that you can pilot across the water, requires gasoline to power its motor. Can support the weight of structures and be built on.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Motorboat.png')
    models.Structure.new(name='Oil Pump', stack_size=1, class_name='PrimalItemStructure_oilPump_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/OilPump/PrimalItemStructure_oilPump.PrimalItemStructure_oilPump\'"',
                         url='https://ark.fandom.com/wiki/Oil_Pump_(Scorched_Earth)',
                         description='Extracts Oil from an Oil zone',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7d/Oil_Pump_%28Scorched_Earth%29.png')
    models.Structure.new(name='Plant Species Y Trap', stack_size=10,
                         class_name='PrimalItemStructure_PlantSpeciesYTrap_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/WeaponPlantSpeciesY/PrimalItemStructure_PlantSpeciesYTrap.PrimalItemStructure_PlantSpeciesYTrap\'"',
                         url='https://ark.fandom.com/wiki/Plant_Species_Y_Trap_(Scorched_Earth)',
                         description='Immobilizes humans and small creatures.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cb/Plant_Species_Y_Trap_%28Scorched_Earth%29.png')
    models.Structure.new(name='Portable Rope Ladder', stack_size=100, class_name='PrimalItemStructure_PortableLadder_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/PortableRopeLadder/PrimalItemStructure_PortableLadder.PrimalItemStructure_PortableLadder\'"',
                         url='https://ark.fandom.com/wiki/Portable_Rope_Ladder_(Aberration)',
                         description='A simple rope ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Rope_Ladder.png')
    models.Structure.new(name='Pressure Plate', stack_size=5, class_name='PrimalItemStructure_PressurePlate_C',
                         blueprint='"Blueprint\'/Game/Genesis/Structures/TekAlarm/PrimalItemStructure_PressurePlate.PrimalItemStructure_PressurePlate\'"',
                         url='https://ark.fandom.com/wiki/Pressure_Plate_(Genesis:_Part_1)',
                         description='A mechanical trigger that activates nearby devices and structures when stepped on.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a2/Pressure_Plate_%28Genesis_Part_1%29.png')
    models.Structure.new(name='Rocket Turret', stack_size=1, class_name='PrimalItemStructure_TurretRocket_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretRocket.PrimalItemStructure_TurretRocket\'"',
                         url='https://ark.fandom.com/wiki/Rocket_Turret',
                         description='Mount this to fire Rockets at your enemies. Powered by the rider.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/56/Rocket_Turret.png')
    models.Structure.new(name='Rockwell Flag', stack_size=100, class_name='PrimalItemStructure_Flag_Rockwell_C',
                         blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Trophies/PrimalItemStructure_Flag_Rockwell.PrimalItemStructure_Flag_Rockwell\'"',
                         url='https://ark.fandom.com/wiki/Rockwell_Flag_(Aberration)',
                         description='This flag is proof that you have defeated Rockwell.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/83/Rockwell_Flag_%28Aberration%29.png')
    models.Structure.new(name='Rope Ladder', stack_size=100, class_name='PrimalItemStructure_RopeLadder_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_RopeLadder.PrimalItemStructure_RopeLadder\'"',
                         url='https://ark.fandom.com/wiki/Rope_Ladder',
                         description='A simple rope ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Rope_Ladder.png')
    models.Structure.new(name='Shag Rug', stack_size=100, class_name='PrimalItemStructure_Furniture_Rug_C',
                         blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Structures/PrimalItemStructure_Furniture_Rug.PrimalItemStructure_Furniture_Rug\'"',
                         url='https://ark.fandom.com/wiki/Shag_Rug_(Aberration)',
                         description='A decorative, paintable rug with a shaggy appearance, which dulls the sound of footsteps.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Shag_Rug_%28Aberration%29.png')
    models.Structure.new(name='Sloped Adobe Roof', stack_size=100, class_name='PrimalItemStructure_AdobeRoof_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeRoof.PrimalItemStructure_AdobeRoof\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Adobe_Roof_(Scorched_Earth)',
                         description='An inclined adobe-framed roof. Slightly different angle than the ramp. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dd/Sloped_Adobe_Roof_%28Scorched_Earth%29.png')
    models.Structure.new(name='Sloped Adobe Wall Left', stack_size=100,
                         class_name='PrimalItemStructure_AdobeWall_Sloped_Left_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWall_Sloped_Left.PrimalItemStructure_AdobeWall_Sloped_Left\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Adobe_Wall_Left_(Scorched_Earth)',
                         description='A sturdy adobe-framed, sloped wall that insulates the inside from the outside, seprarates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/ff/Sloped_Adobe_Wall_Left_%28Scorched_Earth%29.png')
    models.Structure.new(name='Sloped Adobe Wall Right', stack_size=100,
                         class_name='PrimalItemStructure_AdobeWall_Sloped_Right_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWall_Sloped_Right.PrimalItemStructure_AdobeWall_Sloped_Right\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Adobe_Wall_Right_(Scorched_Earth)',
                         description='A sturdy adobe-framed, sloped wall that insulates the inside from the outside, seprarates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2f/Sloped_Adobe_Wall_Right_%28Scorched_Earth%29.png')
    models.Structure.new(name='Sloped Tek Roof', stack_size=100, class_name='PrimalItemStructure_TekRoof_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekRoof.PrimalItemStructure_TekRoof\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Tek_Roof',
                         description='An inclined tek roof. Slightly different angle than the ramp.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6a/Sloped_Tek_Roof.png')
    models.Structure.new(name='Sloped Tek Wall Left', stack_size=100,
                         class_name='PrimalItemStructure_TekWall_Sloped_Left_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWall_Sloped_Left.PrimalItemStructure_TekWall_Sloped_Left\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Tek_Wall_Left',
                         description='A composite Tek wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png')
    models.Structure.new(name='Sloped Tek Wall Right', stack_size=100,
                         class_name='PrimalItemStructure_TekWall_Sloped_Right_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWall_Sloped_Right.PrimalItemStructure_TekWall_Sloped_Right\'"',
                         url='https://ark.fandom.com/wiki/Sloped_Tek_Wall_Right',
                         description='A composite Tek wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png')
    models.Structure.new(name='Small Elevator Platform', stack_size=1,
                         class_name='PrimalItemStructure_ElevatorPlatformSmall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorPlatformSmall.PrimalItemStructure_ElevatorPlatformSmall\'"',
                         url='https://ark.fandom.com/wiki/Small_Elevator_Platform',
                         description='Attach to an Elevator Track to carry a small amount of weight.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Small_Elevator_Platform.png')
    models.Structure.new(name='Small Taxidermy Base', stack_size=100,
                         class_name='PrimalItemStructure_TaxidermyBase_Small_C',
                         blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_TaxidermyBase_Small.PrimalItemStructure_TaxidermyBase_Small\'"',
                         url='https://ark.fandom.com/wiki/Small_Taxidermy_Base_(Extinction)',
                         description='Place a harvested dermis to show off your prowess!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Small_Taxidermy_Base_%28Extinction%29.png')
    models.Structure.new(name='Small Wood Elevator Platform', stack_size=100,
                         class_name='PrimalItemStructure_WoodElevatorPlatform_Small_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorPlatform_Small.PrimalItemStructure_WoodElevatorPlatform_Small\'"',
                         url='https://ark.fandom.com/wiki/Small_Wood_Elevator_Platform_(Aberration)',
                         description='Attach to an Elevator Track to lift a small amount of weight.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Small_Wood_Elevator_Platform_%28Aberration%29.png')
    models.Structure.new(name='Stone Cliff Platform', stack_size=3,
                         class_name='PrimalItemStructure_Stone_CliffPlatform_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/CliffPlatforms/Stone_CliffPlatform/PrimalItemStructure_Stone_CliffPlatform.PrimalItemStructure_Stone_CliffPlatform\'"',
                         url='https://ark.fandom.com/wiki/Stone_Cliff_Platform_(Aberration)',
                         description='A Cliff Platform is required to build structures extending from a cliff. This one is made from heavy stone.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Stone_Cliff_Platform_%28Aberration%29.png')
    models.Structure.new(name='Stone Fireplace', stack_size=3, class_name='PrimalItemStructure_Fireplace_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Fireplace.PrimalItemStructure_Fireplace\'"',
                         url='https://ark.fandom.com/wiki/Stone_Fireplace',
                         description='A nice, relaxing fireplace. Keeps a large area very warm and provides light.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c2/Stone_Fireplace.png')
    models.Structure.new(name='Stone Railing', stack_size=100, class_name='PrimalItemStructure_StoneRailing_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneRailing.PrimalItemStructure_StoneRailing\'"',
                         url='https://ark.fandom.com/wiki/Stone_Railing',
                         description='A brick-and-mortar railing that acts as a simple barrier to prevent people from falling.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1b/Stone_Railing.png')
    models.Structure.new(name='Stone Staircase', stack_size=100, class_name='PrimalItemStructure_StoneStairs_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneStairs.PrimalItemStructure_StoneStairs\'"',
                         url='https://ark.fandom.com/wiki/Stone_Staircase',
                         description='A stone spiral staircase, useful in constructing multi-level buildings.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/09/Stone_Staircase.png')
    models.Structure.new(name='Tek Bridge', stack_size=100, class_name='PrimalItemStructure_TekBridge_C',
                         blueprint='"Blueprint\'/Game/Extinction/Structures/TekBridge/PrimalItemStructure_TekBridge.PrimalItemStructure_TekBridge\'"',
                         url='https://ark.fandom.com/wiki/Tek_Bridge_(Extinction)',
                         description='Extendable force bridge',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3b/Tek_Bridge_%28Extinction%29.png')
    models.Structure.new(name='Tek Catwalk', stack_size=100, class_name='PrimalItemStructure_TekCatwalk_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekCatwalk.PrimalItemStructure_TekCatwalk\'"',
                         url='https://ark.fandom.com/wiki/Tek_Catwalk',
                         description='A thin walkway for bridging areas together. Made from advanced Tek materials.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/Tek_Catwalk.png')
    models.Structure.new(name='Tek Ceiling', stack_size=100, class_name='PrimalItemStructure_TekCeiling_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekCeiling.PrimalItemStructure_TekCeiling\'"',
                         url='https://ark.fandom.com/wiki/Tek_Ceiling',
                         description='An incredibly durable composite Tek ceiling that provides insulation, and doubles as a floor for higher levels.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Tek_Ceiling.png')
    models.Structure.new(name='Tek Dinosaur Gateway', stack_size=100, class_name='PrimalItemStructure_TekGateframe_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGateframe.PrimalItemStructure_TekGateframe\'"',
                         url='https://ark.fandom.com/wiki/Tek_Dinosaur_Gateway',
                         description='A large composite Tek gate that can be used with a Gateway to keep most dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Tek_Dinosaur_Gate.png')
    models.Structure.new(name='Tek Dinosaur Gate', stack_size=100, class_name='PrimalItemStructure_TekGate_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGate.PrimalItemStructure_TekGate\'"',
                         url='https://ark.fandom.com/wiki/Tek_Dinosaur_Gate',
                         description='A large composite Tek gate that can be used with a Gateway to keep most dinosaurs in or out.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Tek_Dinosaur_Gate.png')
    models.Structure.new(name='Tek Doorframe', stack_size=100, class_name='PrimalItemStructure_TekWallWithDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWallWithDoor.PrimalItemStructure_TekWallWithDoor\'"',
                         url='https://ark.fandom.com/wiki/Tek_Doorframe',
                         description='A stable composite Tek door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/36/Tek_Door.png')
    models.Structure.new(name='Tek Door', stack_size=100, class_name='PrimalItemStructure_TekDoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekDoor.PrimalItemStructure_TekDoor\'"',
                         url='https://ark.fandom.com/wiki/Tek_Door',
                         description='A stable composite Tek door that provides entrance to structures. Can be locked for security.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/36/Tek_Door.png')
    models.Structure.new(name='Tek Fence Foundation', stack_size=100,
                         class_name='PrimalItemStructure_TekFenceFoundation_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekFenceFoundation.PrimalItemStructure_TekFenceFoundation\'"',
                         url='https://ark.fandom.com/wiki/Tek_Fence_Foundation',
                         description='This composite Tek foundation is used to build walls around an area.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Tek_Fence_Foundation.png')
    models.Structure.new(name='Tek Forcefield', stack_size=1, class_name='PrimalItemStructure_TekShield_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekShield.PrimalItemStructure_TekShield\'"',
                         url='https://ark.fandom.com/wiki/Tek_Forcefield',
                         description='Generates an impenetrable, expandable spherical shield to keep out enemies. Requires Element to run, and Tek Engram to use.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5a/Tek_Forcefield.png')
    models.Structure.new(name='Tek Foundation', stack_size=100, class_name='PrimalItemStructure_TekFloor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekFloor.PrimalItemStructure_TekFloor\'"',
                         url='https://ark.fandom.com/wiki/Tek_Foundation',
                         description='A foundation is required to build structures in an area. This is made from sturdy composite Tek materials.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8c/Tek_Foundation.png')
    models.Structure.new(name='Tek Generator', stack_size=1, class_name='PrimalItemStructure_TekGenerator_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekGenerator.PrimalItemStructure_TekGenerator\'"',
                         url='https://ark.fandom.com/wiki/Tek_Generator',
                         description='Powers Tek Structures and electrical structures wirelessly! Requires Element to run, and Tek Engram to use.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Tek_Generator.png')
    models.Structure.new(name='Tek Hatchframe', stack_size=100,
                         class_name='PrimalItemStructure_TekCeilingWithTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekCeilingWithTrapdoor.PrimalItemStructure_TekCeilingWithTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Tek_Hatchframe',
                         description='This composite Tek ceiling has a hole in it for trapdoors.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Tek_Hatchframe.png')
    models.Structure.new(name='Tek Jump Pad', stack_size=1, class_name='PrimalItemStructure_TekJumpPad_C',
                         blueprint='"Blueprint\'/Game/Genesis/Structures/TekJumpPad/PrimalItemStructure_TekJumpPad.PrimalItemStructure_TekJumpPad\'"',
                         url='https://ark.fandom.com/wiki/Tek_Jump_Pad_(Genesis:_Part_1)',
                         description='A Tek-powered propulsion device; useful for traversal and mayhem.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Tek_Jump_Pad_%28Genesis_Part_1%29.png')
    models.Structure.new(name='Tek Ladder', stack_size=100, class_name='PrimalItemStructure_TekLadder_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekLadder.PrimalItemStructure_TekLadder\'"',
                         url='https://ark.fandom.com/wiki/Tek_Ladder',
                         description='A composite Tek ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Tek_Ladder.png')
    models.Structure.new(name='Tek Light', stack_size=100, class_name='PrimalItemStructure_TekLight_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekLight.PrimalItemStructure_TekLight\'"',
                         url='https://ark.fandom.com/wiki/Tek_Light',
                         description='Useful for spelunking, they can be attached to any surface, self powered by Element Shards , or linked to generators, and picked-up after placement.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Tek_Light_%28Ragnarok%29.png')
    models.Structure.new(name='Tek Pillar', stack_size=100, class_name='PrimalItemStructure_TekPillar_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekPillar.PrimalItemStructure_TekPillar\'"',
                         url='https://ark.fandom.com/wiki/Tek_Pillar',
                         description='This composite Tek pillar adds structural integrity to the area it is build under. Can also act as stilts for buildings on inclines.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Tek_Pillar.png')
    models.Structure.new(name='Tek Railing', stack_size=100, class_name='PrimalItemStructure_TekRailing_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekRailing.PrimalItemStructure_TekRailing\'"',
                         url='https://ark.fandom.com/wiki/Tek_Railing',
                         description='A composite Tek railing that acts as a simple barrier to prevent people from falling.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0f/Tek_Railing.png')
    models.Structure.new(name='Tek Ramp', stack_size=100, class_name='PrimalItemStructure_TekRamp_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekRamp.PrimalItemStructure_TekRamp\'"',
                         url='https://ark.fandom.com/wiki/Tek_Ramp',
                         description='An inclined composite Tek floor for travelling up or down levels. Can also be used to make an angled roof.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1a/Tek_Ramp.png')
    models.Structure.new(name='Tek Replicator', stack_size=1, class_name='PrimalItemStructure_TekReplicator_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekReplicator.PrimalItemStructure_TekReplicator\'"',
                         url='https://ark.fandom.com/wiki/Tek_Replicator',
                         description='Replicate items here. Requires Element to be activated.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a2/Tek_Replicator.png')
    models.Structure.new(name='Tek Sensor', stack_size=1, class_name='PrimalItemStructure_TekAlarm_C',
                         blueprint='"Blueprint\'/Game/Genesis/Structures/TekAlarm/PrimalItemStructure_TekAlarm.PrimalItemStructure_TekAlarm\'"',
                         url='https://ark.fandom.com/wiki/Tek_Sensor_(Genesis:_Part_1)',
                         description='An advanced detection and activation system used to automate nearby devices and structures. Requires Tek Generator power.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/16/Tek_Sensor_%28Genesis_Part_1%29.png')
    models.Structure.new(name='Tek Sleeping Pod', stack_size=3, class_name='PrimalItemStructure_Bed_Tek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bed_Tek.PrimalItemStructure_Bed_Tek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Sleeping_Pod_(Aberration)',
                         description='This Tek-powered Chamber lets you rapidly recover vitals, and slowly gain XP even when sleeping. You can also sleep soundly within it, protected even while on a moving platform!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Tek_Sleeping_Pod_%28Aberration%29.png')
    models.Structure.new(name='Tek Staircase', stack_size=100, class_name='PrimalItemStructure_TekStairs_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekStairs.PrimalItemStructure_TekStairs\'"',
                         url='https://ark.fandom.com/wiki/Tek_Staircase',
                         description='A composite Tek spiral staircase, useful in constructing multi-level buildings.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Tek_Staircase.png')
    models.Structure.new(name='Tek Teleporter', stack_size=1, class_name='PrimalItemStructure_TekTeleporter_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekTeleporter.PrimalItemStructure_TekTeleporter\'"',
                         url='https://ark.fandom.com/wiki/Tek_Teleporter',
                         description='Allows instantaneous traversal between Teleporters! Requires Tek Generator to power, and Element & Tek Engram to use.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/64/Tek_Teleporter.png')
    models.Structure.new(name='Tek Transmitter', stack_size=1, class_name='PrimalItemStructure_TekTransmitter_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekTransmitter.PrimalItemStructure_TekTransmitter\'"',
                         url='https://ark.fandom.com/wiki/Tek_Transmitter',
                         description='Transmits items, Survivors, and creatures to other ARKs! Requires Tek Engram to use.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Tek_Transmitter.png')
    models.Structure.new(name='Tek Trapdoor', stack_size=100, class_name='PrimalItemStructure_TekTrapdoor_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekTrapdoor.PrimalItemStructure_TekTrapdoor\'"',
                         url='https://ark.fandom.com/wiki/Tek_Trapdoor',
                         description='This composite Tek slab can be used to secure hatches.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Tek_Trapdoor.png')
    models.Structure.new(name='Tek Trough', stack_size=1, class_name='PrimalItemStructure_TekTrough_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekTrough.PrimalItemStructure_TekTrough\'"',
                         url='https://ark.fandom.com/wiki/Tek_Trough',
                         description="Put food for your nearby pets in this, and they'll automatically eat it when hungry! Can refridgerate items, so long as it's powered by a Tek Generator!",
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Tek_Trough.png')
    models.Structure.new(name='Tek Turret', stack_size=1, class_name='PrimalItemStructure_TurretTek_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretTek.PrimalItemStructure_TurretTek\'"',
                         url='https://ark.fandom.com/wiki/Tek_Turret',
                         description='Requires Tek Generator power. Consumes Element Shards while firing. Has a variety of smart-targeting configuration options.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Tek_Turret.png')
    models.Structure.new(name='Tek Wall', stack_size=100, class_name='PrimalItemStructure_TekWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWall.PrimalItemStructure_TekWall\'"',
                         url='https://ark.fandom.com/wiki/Tek_Wall',
                         description='A composite Tek wall that insulates the inside from the outside and separates rooms.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png')
    models.Structure.new(name='Tek Windowframe', stack_size=100, class_name='PrimalItemStructure_TekWallWithWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWallWithWindow.PrimalItemStructure_TekWallWithWindow\'"',
                         url='https://ark.fandom.com/wiki/Tek_Windowframe',
                         description='Tek plates that cover windows to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Tek_Window.png')
    models.Structure.new(name='Tek Window', stack_size=100, class_name='PrimalItemStructure_TekWindow_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWindow.PrimalItemStructure_TekWindow\'"',
                         url='https://ark.fandom.com/wiki/Tek_Window',
                         description='Tek plates that cover windows to provide protection from projectiles and spying.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Tek_Window.png')
    models.Structure.new(name='Tent', stack_size=1, class_name='PrimalItemStructure_Tent_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/Tent/PrimalItemStructure_Tent.PrimalItemStructure_Tent\'"',
                         url='https://ark.fandom.com/wiki/Tent_(Scorched_Earth)',
                         description='A portable Tent where you can take cover in hostile environments',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d6/Tent_%28Scorched_Earth%29.png')
    models.Structure.new(name='Toilet', stack_size=100, class_name='PrimalItemStructure_Toilet_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_Toilet.PrimalItemStructure_Toilet\'"',
                         url='https://ark.fandom.com/wiki/Toilet',
                         description='Attach to water pipes, and sit on it when you hear the call of nature. Do your business, feel refreshed, and then flush for efficient waste disposal!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Toilet.png')
    models.Structure.new(name='Training Dummy', stack_size=100, class_name='PrimalItemStructure_TrainingDummy_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_TrainingDummy.PrimalItemStructure_TrainingDummy\'"',
                         url='https://ark.fandom.com/wiki/Training_Dummy',
                         description='Attack this training dummy to test your DPS!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/49/Training_Dummy.png')
    models.Structure.new(name='Tree Sap Tap', stack_size=100, class_name='PrimalItemStructure_TreeTap_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_TreeTap.PrimalItemStructure_TreeTap\'"',
                         url='https://ark.fandom.com/wiki/Tree_Sap_Tap',
                         description='Attach this to a large tree to tap its sap over time.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Tree_Sap_Tap.png')
    models.Structure.new(name='Trophy Wall-Mount', stack_size=100, class_name='PrimalItemStructure_TrophyWall_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TrophyWall.PrimalItemStructure_TrophyWall\'"',
                         url='https://ark.fandom.com/wiki/Trophy_Wall-Mount',
                         description='Provides the wall-mount upon which you can place a trophy!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Trophy_Wall-Mount.png')
    models.Structure.new(name='Vacuum Compartment Moonpool', stack_size=100,
                         class_name='PrimalItemStructure_UnderwaterBase_Moonpool_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_UnderwaterBase_Moonpool.PrimalItemStructure_UnderwaterBase_Moonpool\'"',
                         url='https://ark.fandom.com/wiki/Vacuum_Compartment_Moonpool',
                         description='Place underwater, power with Tek Generator, and you can live and breath in it!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Vacuum_Compartment.png')
    models.Structure.new(name='Vacuum Compartment', stack_size=100, class_name='PrimalItemStructure_UnderwaterBase_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_UnderwaterBase.PrimalItemStructure_UnderwaterBase\'"',
                         url='https://ark.fandom.com/wiki/Vacuum_Compartment',
                         description='Place underwater, power with Tek Generator, and you can live and breath in it!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Vacuum_Compartment.png')
    models.Structure.new(name='Vessel', stack_size=100, class_name='PrimalItemStructure_Vessel_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/DesertFurnitureSet/Vessel/PrimalItemStructure_Vessel.PrimalItemStructure_Vessel\'"',
                         url='https://ark.fandom.com/wiki/Vessel_(Scorched_Earth)',
                         description='Stores preserving salts and makes them last longer.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/07/Vessel_%28Scorched_Earth%29.png')
    models.Structure.new(name='VR Boss Flag', stack_size=100, class_name='PrimalItemStructure_Flag_VRBoss_C',
                         blueprint='"Blueprint\'/Game/Genesis/CoreBlueprints/Structures/PrimalItemStructure_Flag_VRBoss.PrimalItemStructure_Flag_VRBoss\'"',
                         url='https://ark.fandom.com/wiki/VR_Boss_Flag_(Genesis:_Part_1)',
                         description='This flag is proof that you have defeated the VR Boss.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/23/VR_Boss_Flag_%28Genesis_Part_1%29.png')
    models.Structure.new(name='Wall Torch', stack_size=3, class_name='PrimalItemStructure_WallTorch_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_WallTorch.PrimalItemStructure_WallTorch\'"',
                         url='https://ark.fandom.com/wiki/Wall_Torch',
                         description='A torch on a metal connector that lights and warms the immediate area. Must be placed on a wall.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Wall_Torch.png')
    models.Structure.new(name='War Map', stack_size=100, class_name='PrimalItemStructure_WarMap_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WarMap.PrimalItemStructure_WarMap\'"',
                         url='https://ark.fandom.com/wiki/War_Map',
                         description='A map of the Island upon which you can draw your plans.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7a/War_Map.png')
    models.Structure.new(name='Wardrums', stack_size=100, class_name='PrimalItemStructure_Wardrums_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Wardrums.PrimalItemStructure_Wardrums\'"',
                         url='https://ark.fandom.com/wiki/Wardrums',
                         description='A set of tribal wardrums, to let everyone around hear the power of your tribe.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/db/Wardrums.png')
    models.Structure.new(name='Water Well', stack_size=100, class_name='PrimalItemStructure_WaterWell_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/WaterWell/PrimalItemStructure_WaterWell.PrimalItemStructure_WaterWell\'"',
                         url='https://ark.fandom.com/wiki/Water_Well_(Scorched_Earth)',
                         description='This stone tap allows access to the water in an irrigation network. Can refill containers, irrigate crop plots, or provide a refreshing drink.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Water_Well_%28Scorched_Earth%29.png')
    models.Structure.new(name='Wind Turbine', stack_size=1, class_name='PrimalItemStructure_WindTurbine_C',
                         blueprint='"Blueprint\'/Game/ScorchedEarth/Structures/WindTurbine/PrimalItemStructure_WindTurbine.PrimalItemStructure_WindTurbine\'"',
                         url='https://ark.fandom.com/wiki/Wind_Turbine_(Scorched_Earth)',
                         description='Converts the force of the wind into electricity.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8c/Wind_Turbine_%28Scorched_Earth%29.png')
    models.Structure.new(name='Wood Elevator Top Switch', stack_size=100,
                         class_name='PrimalItemStructure_WoodElevatorTopSwitch_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorTopSwitch.PrimalItemStructure_WoodElevatorTopSwitch\'"',
                         url='https://ark.fandom.com/wiki/Wood_Elevator_Top_Switch_(Aberration)',
                         description='Attach to the top of a Wood Elevator Track to complete an Elevator!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Wood_Elevator_Top_Switch_%28Aberration%29.png')
    models.Structure.new(name='Wood Elevator Track', stack_size=100,
                         class_name='PrimalItemStructure_WoodElevatorTrack_C',
                         blueprint='"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorTrack.PrimalItemStructure_WoodElevatorTrack\'"',
                         url='https://ark.fandom.com/wiki/Wood_Elevator_Track_(Aberration)',
                         description='Attach a Wood Elevator Platform to these to complete an elevator!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Wood_Elevator_Track_%28Aberration%29.png')
    models.Structure.new(name='Wood Ocean Platform', stack_size=3,
                         class_name='PrimalItemStructure_Wood_OceanPlatform_C',
                         blueprint='"Blueprint\'/Game/Genesis/Structures/OceanPlatform/OceanPlatform_Wood/PrimalItemStructure_Wood_OceanPlatform.PrimalItemStructure_Wood_OceanPlatform\'"',
                         url='https://ark.fandom.com/wiki/Wood_Ocean_Platform_(Genesis:_Part_1)',
                         description='Floats on the surface of bodies of water.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Wood_Ocean_Platform_%28Genesis_Part_1%29.png')
    models.Structure.new(name='Wooden Bench', stack_size=100, class_name='PrimalItemStructure_Furniture_WoodBench_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_WoodBench.PrimalItemStructure_Furniture_WoodBench\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Bench',
                         description='A simple wooden bench for group sitting.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Wooden_Bench.png')
    models.Structure.new(name='Wooden Cage', stack_size=1, class_name='PrimalItemStructure_WoodCage_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCage.PrimalItemStructure_WoodCage\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Cage',
                         description='A portable cage in which to imprison victims.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Wooden_Cage.png')
    models.Structure.new(name='Wooden Chair', stack_size=100, class_name='PrimalItemStructure_Furniture_WoodChair_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_WoodChair.PrimalItemStructure_Furniture_WoodChair\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Chair',
                         description='A simple wooden chair for solo sitting.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/87/Wooden_Chair.png')
    models.Structure.new(name='Wooden Railing', stack_size=100, class_name='PrimalItemStructure_WoodRailing_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodRailing.PrimalItemStructure_WoodRailing\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Railing',
                         description='A sturdy wooden railing that acts as a simple barrier to prevent people from falling.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7b/Wooden_Railing.png')
    models.Structure.new(name='Wooden Staircase', stack_size=100, class_name='PrimalItemStructure_WoodStairs_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodStairs.PrimalItemStructure_WoodStairs\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Staircase',
                         description='A wooden spiral staircase, useful in constructing multi-level buildings.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c2/Wooden_Staircase.png')
    models.Structure.new(name='Wooden Table', stack_size=100, class_name='PrimalItemStructure_Furniture_WoodTable_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_WoodTable.PrimalItemStructure_Furniture_WoodTable\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Table',
                         description='A simple wooden table with a variety of uses.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Wooden_Table.png')
    models.Structure.new(name='Wooden Tree Platform', stack_size=1,
                         class_name='PrimalItemStructure_TreePlatform_Wood_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_TreePlatform_Wood.PrimalItemStructure_TreePlatform_Wood\'"',
                         url='https://ark.fandom.com/wiki/Wooden_Tree_Platform',
                         description='Attaches to a large tree, enabling you to build on it.',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Wooden_Tree_Platform.png')
    models.Structure.new(name='Plant Species X', stack_size=1, class_name='PrimalItemStructure_TurretPlant_C',
                         blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretPlant.PrimalItemStructure_TurretPlant\'"',
                         url='https://ark.fandom.com/wiki/Plant_Species_X', description=None,
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Plant_Species_X.png')
    models.Structure.new(name='Tek ATV', stack_size=1, class_name=None,
                         blueprint='"Blueprint\'/Game/PrimalEarth/Vehicles/VH_Buggy/Blueprint/PrimalItemVHBuggy.PrimalItemVHBuggy\'"',
                         url='https://ark.fandom.com/wiki/Tek_ATV',
                         description='Cruise around in this jaunty Element-powered ride. Supports a driver and one passenger, both of whom are able to wield weapons!',
                         image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Tek_ATV.png')
    items = [item.to_json() for item in models.Structure.all()]
    print(items)


def seed():
    items = [
        {
            'name': 'Campfire', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Campfire.PrimalItemStructure_Campfire\'"',
            'description': 'Perfect for cooking meat, staying warm, and providing light.',
            'url': 'https://ark.fandom.com/wiki/Campfire', 'id': 39, 'class_name': 'PrimalItemStructure_Campfire_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Campfire.png'
        },
        {
            'name': 'Standing Torch', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StandingTorch.PrimalItemStructure_StandingTorch\'"',
            'description': 'A torch on a small piece of wood that lights and warms the immediate area.',
            'url': 'https://ark.fandom.com/wiki/Standing_Torch', 'id': 40,
            'class_name': 'PrimalItemStructure_StandingTorch_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Standing_Torch.png'
        },
        {
            'name': 'Hide Sleeping Bag', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_SleepingBag_Hide.PrimalItemStructure_SleepingBag_Hide\'"',
            'description': 'This hide sleeping bag acts as a single-use respawn point, only usable by you.',
            'url': 'https://ark.fandom.com/wiki/Hide_Sleeping_Bag', 'id': 41,
            'class_name': 'PrimalItemStructure_SleepingBag_Hide_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Hide_Sleeping_Bag.png'
        },
        {
            'name': 'Thatch Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchCeiling.PrimalItemStructure_ThatchCeiling\'"',
            'description': 'A thatched ceiling to protect you from the elements. Not stable enough to build on.',
            'url': 'https://ark.fandom.com/wiki/Thatch_Ceiling', 'id': 78,
            'class_name': 'PrimalItemStructure_ThatchCeiling_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8d/Thatch_Ceiling.png'
        },
        {
            'name': 'Thatch Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchDoor.PrimalItemStructure_ThatchDoor\'"',
            'description': 'Enough sticks bundled together works as a simple door. Can be locked for security, but not very strong.',
            'url': 'https://ark.fandom.com/wiki/Thatch_Door', 'id': 79,
            'class_name': 'PrimalItemStructure_ThatchDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/Thatch_Door.png'
        },
        {
            'name': 'Thatch Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchFloor.PrimalItemStructure_ThatchFloor\'"',
            'description': 'A foundation is required to build structures. This one is a wooden frame with some smooth bundles of sticks that act as a floor.',
            'url': 'https://ark.fandom.com/wiki/Thatch_Foundation', 'id': 80,
            'class_name': 'PrimalItemStructure_ThatchFloor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Thatch_Foundation.png'
        },
        {
            'name': 'Thatch Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchWall.PrimalItemStructure_ThatchWall\'"',
            'description': 'A simple wall made of bundled sticks, and stabilized by a wooden frame. Fairly fragile, but better than nothing.',
            'url': 'https://ark.fandom.com/wiki/Thatch_Wall', 'id': 81,
            'class_name': 'PrimalItemStructure_ThatchWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Thatch_Wall.png'
        },
        {
            'name': 'Thatch Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Thatch/PrimalItemStructure_ThatchWallWithDoor.PrimalItemStructure_ThatchWallWithDoor\'"',
            'description': 'Enough sticks bundled together works as a simple door. Can be locked for security, but not very strong.',
            'url': 'https://ark.fandom.com/wiki/Thatch_Doorframe', 'id': 82,
            'class_name': 'PrimalItemStructure_ThatchWallWithDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/Thatch_Door.png'
        },
        {
            'name': 'Wooden Catwalk', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCatwalk.PrimalItemStructure_WoodCatwalk\'"',
            'description': 'A thin walkway for bridging areas together. Made from sturdy wood.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Catwalk', 'id': 83,
            'class_name': 'PrimalItemStructure_WoodCatwalk_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Wooden_Catwalk.png'
        },
        {
            'name': 'Wooden Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCeiling.PrimalItemStructure_WoodCeiling\'"',
            'description': 'A stable wooden ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Ceiling', 'id': 84,
            'class_name': 'PrimalItemStructure_WoodCeiling_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Wooden_Ceiling.png'
        },
        {
            'name': 'Wooden Hatchframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCeilingWithTrapdoor.PrimalItemStructure_WoodCeilingWithTrapdoor\'"',
            'description': 'A wooden ceiling with a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Hatchframe', 'id': 85,
            'class_name': 'PrimalItemStructure_WoodCeilingWithTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Wooden_Hatchframe.png'
        },
        {
            'name': 'Wooden Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodDoor.PrimalItemStructure_WoodDoor\'"',
            'description': 'A stable wooden door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Door', 'id': 86, 'class_name': 'PrimalItemStructure_WoodDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Wooden_Door.png'
        },
        {
            'name': 'Wooden Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodFloor.PrimalItemStructure_WoodFloor\'"',
            'description': 'A foundation is required to build structures. This one is made from sturdy wood.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Foundation', 'id': 87,
            'class_name': 'PrimalItemStructure_WoodFloor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Wooden_Foundation.png'
        },
        {
            'name': 'Wooden Ladder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodLadder.PrimalItemStructure_WoodLadder\'"',
            'description': 'A simple wooden ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Ladder', 'id': 88,
            'class_name': 'PrimalItemStructure_WoodLadder_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Wooden_Ladder.png'
        },
        {
            'name': 'Wooden Pillar', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodPillar.PrimalItemStructure_WoodPillar\'"',
            'description': 'Adds structural integrity to the area it is built on. Can also act as stilts for buildings on inclines.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Pillar', 'id': 89,
            'class_name': 'PrimalItemStructure_WoodPillar_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Wooden_Pillar.png'
        },
        {
            'name': 'Wooden Ramp', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodRamp.PrimalItemStructure_WoodRamp\'"',
            'description': 'An inclined wooden floor for travelling up or down. Can also be used to make an angled roof.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Ramp', 'id': 90, 'class_name': 'PrimalItemStructure_WoodRamp_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Wooden_Ramp.png'
        },
        {
            'name': 'Wooden Trapdoor', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodTrapdoor.PrimalItemStructure_WoodTrapdoor\'"',
            'description': 'This small wooden door can be used to secure hatches.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Trapdoor', 'id': 91,
            'class_name': 'PrimalItemStructure_WoodTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Wooden_Trapdoor.png'
        },
        {
            'name': 'Wooden Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWall.PrimalItemStructure_WoodWall\'"',
            'description': 'A sturdy wooden wall that insulates the inside from the outside, separates rooms, and provides structural integrity.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Wall', 'id': 92, 'class_name': 'PrimalItemStructure_WoodWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Wooden_Wall.png'
        },
        {
            'name': 'Wooden Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWallWithDoor.PrimalItemStructure_WoodWallWithDoor\'"',
            'description': 'A stable wooden door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Doorframe', 'id': 93,
            'class_name': 'PrimalItemStructure_WoodWallWithDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Wooden_Door.png'
        },
        {
            'name': 'Wooden Windowframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWallWithWindow.PrimalItemStructure_WoodWallWithWindow\'"',
            'description': 'Wooden beams on hinges that cover windows to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Windowframe', 'id': 94,
            'class_name': 'PrimalItemStructure_WoodWallWithWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Wooden_Window.png'
        },
        {
            'name': 'Wooden Window', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodWindow.PrimalItemStructure_WoodWindow\'"',
            'description': 'Wooden beams on hinges that cover windows to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Window', 'id': 95,
            'class_name': 'PrimalItemStructure_WoodWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Wooden_Window.png'
        },
        {
            'name': 'Wooden Sign', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSign.PrimalItemStructure_WoodSign\'"',
            'description': 'A simple wooden sign for landmark navigation or relaying messages.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Sign', 'id': 96, 'class_name': 'PrimalItemStructure_WoodSign_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Wooden_Sign.png'
        },
        {
            'name': 'Storage Box', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StorageBox_Small.PrimalItemStructure_StorageBox_Small\'"',
            'description': 'A small box to store goods in.', 'url': 'https://ark.fandom.com/wiki/Storage_Box',
            'id': 104, 'class_name': 'PrimalItemStructure_StorageBox_Small_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Storage_Box.png'
        },
        {
            'name': 'Large Storage Box', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StorageBox_Large.PrimalItemStructure_StorageBox_Large\'"',
            'description': 'A small box to store goods in.', 'url': 'https://ark.fandom.com/wiki/Large_Storage_Box',
            'id': 105, 'class_name': 'PrimalItemStructure_StorageBox_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Storage_Box.png'
        },
        {
            'name': 'Mortar and Pestle', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_MortarAndPestle.PrimalItemStructure_MortarAndPestle\'"',
            'description': 'This simple stone contraption can be used to grind resources into new substances.',
            'url': 'https://ark.fandom.com/wiki/Mortar_And_Pestle', 'id': 106,
            'class_name': 'PrimalItemStructure_MortarAndPestle_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Mortar_And_Pestle.png'
        },
        {
            'name': 'Stone Irrigation Pipe - Intake', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeIntake.PrimalItemStructure_StonePipeIntake\'"',
            'description': 'The stone intake for an irrigation network that transports water over land.',
            'url': 'https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Intake', 'id': 109,
            'class_name': 'PrimalItemStructure_StonePipeIntake_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/68/Stone_Irrigation_Pipe_-_Intake.png'
        },
        {
            'name': 'Stone Irrigation Pipe - Straight', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeStraight.PrimalItemStructure_StonePipeStraight\'"',
            'description': 'A straight stone pipe for an irrigation network, used for transporting water across land.',
            'url': 'https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Straight', 'id': 110,
            'class_name': 'PrimalItemStructure_StonePipeStraight_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/Stone_Irrigation_Pipe_-_Straight.png'
        },
        {
            'name': 'Stone Irrigation Pipe - Inclined', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeIncline.PrimalItemStructure_StonePipeIncline\'"',
            'description': 'An inclined stone pipe for an irrigation network, used for transporting water up and down hills.',
            'url': 'https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Inclined', 'id': 111,
            'class_name': 'PrimalItemStructure_StonePipeIncline_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Stone_Irrigation_Pipe_-_Inclined.png'
        },
        {
            'name': 'Stone Irrigation Pipe - Intersection', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeIntersection.PrimalItemStructure_StonePipeIntersection\'"',
            'description': 'A plus-shaped stone intersection for an irrigation network, used for splitting one water source into three.',
            'url': 'https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Intersection', 'id': 112,
            'class_name': 'PrimalItemStructure_StonePipeIntersection_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Stone_Irrigation_Pipe_-_Intersection.png'
        },
        {
            'name': 'Stone Irrigation Pipe - Vertical', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeVertical.PrimalItemStructure_StonePipeVertical\'"',
            'description': 'A vertical stone pipe for an irrigation network, used for transporting water up and down cliffs.',
            'url': 'https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Vertical', 'id': 113,
            'class_name': 'PrimalItemStructure_StonePipeVertical_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d7/Stone_Irrigation_Pipe_-_Vertical.png'
        },
        {
            'name': 'Stone Irrigation Pipe - Tap', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_StonePipeTap.PrimalItemStructure_StonePipeTap\'"',
            'description': 'This stone tap allows access to the water in an irrigation network. Can refill containers, irrigate crop plots, or provide a refreshing drink.',
            'url': 'https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Tap', 'id': 114,
            'class_name': 'PrimalItemStructure_StonePipeTap_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Stone_Irrigation_Pipe_-_Tap.png'
        },
        {
            'name': 'Refining Forge', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Forge.PrimalItemStructure_Forge\'"',
            'description': 'Requires wood, thatch, or sparkpowder to activate. Put unrefined resources in this to refine them.',
            'url': 'https://ark.fandom.com/wiki/Refining_Forge', 'id': 124, 'class_name': 'PrimalItemStructure_Forge_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Refining_Forge.png'
        },
        {
            'name': 'Smithy', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_AnvilBench.PrimalItemStructure_AnvilBench\'"',
            'description': 'Place materials along with blueprints in this to create certain advanced forged items.',
            'url': 'https://ark.fandom.com/wiki/Smithy', 'id': 125, 'class_name': 'PrimalItemStructure_AnvilBench_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b9/Smithy.png'
        },
        {
            'name': 'Compost Bin', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CompostBin.PrimalItemStructure_CompostBin\'"',
            'description': 'A large bin for converting thatch and dung into high-quality fertilizer.',
            'url': 'https://ark.fandom.com/wiki/Compost_Bin', 'id': 126,
            'class_name': 'PrimalItemStructure_CompostBin_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Compost_Bin.png'
        },
        {
            'name': 'Cooking Pot', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CookingPot.PrimalItemStructure_CookingPot\'"',
            'description': 'Must contain basic fuel to light the fire. Put various ingredients with water in this to make soups, stews, and dyes.',
            'url': 'https://ark.fandom.com/wiki/Cooking_Pot', 'id': 127,
            'class_name': 'PrimalItemStructure_CookingPot_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Cooking_Pot.png'
        },
        {
            'name': 'Simple Bed', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bed_Simple.PrimalItemStructure_Bed_Simple\'"',
            'description': 'Thatch may not make the most comfortable mattress, but this bed acts as a respawn point for you and your Tribe.',
            'url': 'https://ark.fandom.com/wiki/Simple_Bed', 'id': 128,
            'class_name': 'PrimalItemStructure_Bed_Simple_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Simple_Bed.png'
        },
        {
            'name': 'Small Crop Plot', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CropPlot_Small.PrimalItemStructure_CropPlot_Small\'"',
            'description': 'A small garden plot, with a fence to keep out vermin.',
            'url': 'https://ark.fandom.com/wiki/Small_Crop_Plot', 'id': 129,
            'class_name': 'PrimalItemStructure_CropPlot_Small_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/59/Small_Crop_Plot.png'
        },
        {
            'name': 'Wooden Fence Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodFenceFoundation.PrimalItemStructure_WoodFenceFoundation\'"',
            'description': 'This very cheap, narrow foundation is used to build fences around an area.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Fence_Foundation', 'id': 135,
            'class_name': 'PrimalItemStructure_WoodFenceFoundation_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Wooden_Fence_Foundation.png'
        },
        {
            'name': 'Dinosaur Gateway', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodGateframe.PrimalItemStructure_WoodGateframe\'"',
            'description': 'A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
            'url': 'https://ark.fandom.com/wiki/Dinosaur_Gateway', 'id': 142,
            'class_name': 'PrimalItemStructure_WoodGateframe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png'
        },
        {
            'name': 'Dinosaur Gate', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodGate.PrimalItemStructure_WoodGate\'"',
            'description': 'A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
            'url': 'https://ark.fandom.com/wiki/Dinosaur_Gate', 'id': 145,
            'class_name': 'PrimalItemStructure_WoodGate_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png'
        },
        {
            'name': 'Metal Catwalk', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCatwalk.PrimalItemStructure_MetalCatwalk\'"',
            'description': 'A thin walkway for bridging areas together. Made from metal plates.',
            'url': 'https://ark.fandom.com/wiki/Metal_Catwalk', 'id': 164,
            'class_name': 'PrimalItemStructure_MetalCatwalk_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Metal_Catwalk.png'
        },
        {
            'name': 'Metal Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCeiling.PrimalItemStructure_MetalCeiling\'"',
            'description': 'A stable metal-plated concrete ceiling that provides insulation, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Metal_Ceiling', 'id': 165,
            'class_name': 'PrimalItemStructure_MetalCeiling_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ac/Metal_Ceiling.png'
        },
        {
            'name': 'Metal Hatchframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCeilingWithTrapdoor.PrimalItemStructure_MetalCeilingWithTrapdoor\'"',
            'description': 'This metal-plated concrete ceiling has a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Metal_Hatchframe', 'id': 166,
            'class_name': 'PrimalItemStructure_MetalCeilingWithTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Metal_Hatchframe.png'
        },
        {
            'name': 'Metal Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalDoor.PrimalItemStructure_MetalDoor\'"',
            'description': 'A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Metal_Door', 'id': 167, 'class_name': 'PrimalItemStructure_MetalDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Metal_Door.png'
        },
        {
            'name': 'Metal Fence Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalFenceFoundation.PrimalItemStructure_MetalFenceFoundation\'"',
            'description': 'This very strong, narrow foundation is used to build walls around an area.',
            'url': 'https://ark.fandom.com/wiki/Metal_Fence_Foundation', 'id': 168,
            'class_name': 'PrimalItemStructure_MetalFenceFoundation_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3d/Metal_Fence_Foundation.png'
        },
        {
            'name': 'Metal Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalFloor.PrimalItemStructure_MetalFloor\'"',
            'description': 'A foundation is required to build structures in an area. This one is made from sturdy metal-plated concrete.',
            'url': 'https://ark.fandom.com/wiki/Metal_Foundation', 'id': 169,
            'class_name': 'PrimalItemStructure_MetalFloor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Metal_Foundation.png'
        },
        {
            'name': 'Behemoth Gate', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGate_Large.PrimalItemStructure_MetalGate_Large\'"',
            'description': 'A large metal-plated concrete gate that can be used with a Behemoth Gateway to allow even the largest of creatures in or out.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Gate', 'id': 170,
            'class_name': 'PrimalItemStructure_MetalGate_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Behemoth_Gate.png'
        },
        {
            'name': 'Behemoth Gateway', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGateframe_Large.PrimalItemStructure_MetalGateframe_Large\'"',
            'description': 'A large metal-plated concrete gate that can be used with a Behemoth Gateway to allow even the largest of creatures in or out.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Gateway', 'id': 171,
            'class_name': 'PrimalItemStructure_MetalGateframe_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Behemoth_Gate.png'
        },
        {
            'name': 'Metal Ladder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalLadder.PrimalItemStructure_MetalLadder\'"',
            'description': 'A simple metal ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
            'url': 'https://ark.fandom.com/wiki/Metal_Ladder', 'id': 172,
            'class_name': 'PrimalItemStructure_MetalLadder_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5e/Metal_Ladder.png'
        },
        {
            'name': 'Metal Pillar', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalPillar.PrimalItemStructure_MetalPillar\'"',
            'description': 'This metal-plated concrete pillar adds structural integrity to the area it is built under. Can also act as stilts for building on inclines.',
            'url': 'https://ark.fandom.com/wiki/Metal_Pillar', 'id': 173,
            'class_name': 'PrimalItemStructure_MetalPillar_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Metal_Pillar.png'
        },
        {
            'name': 'Metal Ramp', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalRamp.PrimalItemStructure_MetalRamp\'"',
            'description': 'An inclined metal-plated concrete floor for travelling up or down levels. Can also be used to make an angled roof.',
            'url': 'https://ark.fandom.com/wiki/Metal_Ramp', 'id': 174, 'class_name': 'PrimalItemStructure_MetalRamp_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Metal_Ramp.png'
        },
        {
            'name': 'Metal Trapdoor', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalTrapdoor.PrimalItemStructure_MetalTrapdoor\'"',
            'description': 'This metal-plated concrete slab can be used to secure hatches.',
            'url': 'https://ark.fandom.com/wiki/Metal_Trapdoor', 'id': 175,
            'class_name': 'PrimalItemStructure_MetalTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/Metal_Trapdoor.png'
        },
        {
            'name': 'Metal Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWall.PrimalItemStructure_MetalWall\'"',
            'description': 'A metal-plated concrete wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Metal_Wall', 'id': 176, 'class_name': 'PrimalItemStructure_MetalWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Metal_Wall.png'
        },
        {
            'name': 'Metal Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWallWithDoor.PrimalItemStructure_MetalWallWithDoor\'"',
            'description': 'A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Metal_Doorframe', 'id': 177,
            'class_name': 'PrimalItemStructure_MetalWallWithDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Metal_Door.png'
        },
        {
            'name': 'Metal Windowframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWallWithWindow.PrimalItemStructure_MetalWallWithWindow\'"',
            'description': 'Metal plates on hinges that cover windows to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Metal_Windowframe', 'id': 178,
            'class_name': 'PrimalItemStructure_MetalWallWithWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/Metal_Window.png'
        },
        {
            'name': 'Metal Window', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalWindow.PrimalItemStructure_MetalWindow\'"',
            'description': 'Metal plates on hinges that cover windows to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Metal_Window', 'id': 179,
            'class_name': 'PrimalItemStructure_MetalWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/Metal_Window.png'
        },
        {
            'name': 'Fabricator', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Fabricator.PrimalItemStructure_Fabricator\'"',
            'description': 'Place materials along with blueprints in this to create certain high-end machined items.',
            'url': 'https://ark.fandom.com/wiki/Fabricator', 'id': 182,
            'class_name': 'PrimalItemStructure_Fabricator_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/66/Fabricator.png'
        },
        {
            'name': 'Water Reservoir', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_WaterTank.PrimalItemStructure_WaterTank\'"',
            'description': 'A standing storage device for holding water. Automatically fills up during rain, can be filled up with the use of a water skin/jar.',
            'url': 'https://ark.fandom.com/wiki/Water_Reservoir', 'id': 183,
            'class_name': 'PrimalItemStructure_WaterTank_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Water_Reservoir.png'
        },
        {
            'name': 'Air Conditioner', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_AirConditioner.PrimalItemStructure_AirConditioner\'"',
            'description': 'Requires electricity to run. Provides insulation from both the heat and the cold to an area.',
            'url': 'https://ark.fandom.com/wiki/Air_Conditioner', 'id': 185,
            'class_name': 'PrimalItemStructure_AirConditioner_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Air_Conditioner.png'
        },
        {
            'name': 'Electrical Generator', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerGenerator.PrimalItemStructure_PowerGenerator\'"',
            'description': 'A large machine that converts gasoline into electricity.',
            'url': 'https://ark.fandom.com/wiki/Electrical_Generator', 'id': 186,
            'class_name': 'PrimalItemStructure_PowerGenerator_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Electrical_Generator.png'
        },
        {
            'name': 'Electrical Outlet', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerOutlet.PrimalItemStructure_PowerOutlet\'"',
            'description': 'An outlet for an electrical grid. When connected to a generator via cables, this provides power to all nearby devices that use electricity.',
            'url': 'https://ark.fandom.com/wiki/Electrical_Outlet', 'id': 187,
            'class_name': 'PrimalItemStructure_PowerOutlet_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Electrical_Outlet.png'
        },
        {
            'name': 'Inclined Electrical Cable', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableIncline.PrimalItemStructure_PowerCableIncline\'"',
            'description': 'An inclined cable for transmitting electricity up and down hills.',
            'url': 'https://ark.fandom.com/wiki/Inclined_Electrical_Cable', 'id': 188,
            'class_name': 'PrimalItemStructure_PowerCableIncline_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Inclined_Electrical_Cable.png'
        },
        {
            'name': 'Electrical Cable Intersection', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableIntersection.PrimalItemStructure_PowerCableIntersection\'"',
            'description': 'A plus-shaped intersection for a power grid, used for splitting one power cable into three.',
            'url': 'https://ark.fandom.com/wiki/Electrical_Cable_Intersection', 'id': 189,
            'class_name': 'PrimalItemStructure_PowerCableIntersection_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Electrical_Cable_Intersection.png'
        },
        {
            'name': 'Straight Electrical Cable', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableStraight.PrimalItemStructure_PowerCableStraight\'"',
            'description': 'A straight cable, used for transmitting electricity across land.',
            'url': 'https://ark.fandom.com/wiki/Straight_Electrical_Cable', 'id': 190,
            'class_name': 'PrimalItemStructure_PowerCableStraight_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1d/Straight_Electrical_Cable.png'
        },
        {
            'name': 'Vertical Electrical Cable', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_PowerCableVertical.PrimalItemStructure_PowerCableVertical\'"',
            'description': 'A vertical cable for transmitting electricity up and down cliffs.',
            'url': 'https://ark.fandom.com/wiki/Vertical_Electrical_Cable', 'id': 191,
            'class_name': 'PrimalItemStructure_PowerCableVertical_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Vertical_Electrical_Cable.png'
        },
        {
            'name': 'Lamppost', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Lamppost.PrimalItemStructure_Lamppost\'"',
            'description': 'Requires electricity to activate. Lights an area without adding much heat.',
            'url': 'https://ark.fandom.com/wiki/Lamppost', 'id': 192, 'class_name': 'PrimalItemStructure_Lamppost_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Lamppost.png'
        },
        {
            'name': 'Refrigerator', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_IceBox.PrimalItemStructure_IceBox\'"',
            'description': 'Requires electricity to run. Keeps perishables from spoiling for a long time.',
            'url': 'https://ark.fandom.com/wiki/Refrigerator', 'id': 193, 'class_name': 'PrimalItemStructure_IceBox_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Refrigerator.png'
        },
        {
            'name': 'Auto Turret', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Turret.PrimalItemStructure_Turret\'"',
            'description': 'Requires electricity to run. Consumes bullets while firing. Can be configured to automatically attack hostiles within range.',
            'url': 'https://ark.fandom.com/wiki/Auto_Turret', 'id': 194, 'class_name': 'PrimalItemStructure_Turret_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Auto_Turret.png'
        },
        {
            'name': 'Remote Keypad', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Keypad.PrimalItemStructure_Keypad\'"',
            'description': 'Allows remote access to multiple doors and/or lights.',
            'url': 'https://ark.fandom.com/wiki/Remote_Keypad', 'id': 195, 'class_name': 'PrimalItemStructure_Keypad_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9b/Remote_Keypad.png'
        },
        {
            'name': 'Metal Irrigation Pipe - Inclined', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeIncline.PrimalItemStructure_MetalPipeIncline\'"',
            'description': 'An inclined metal pipe for an irrigation network, used for transporting water up and down hills.',
            'url': 'https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Inclined', 'id': 196,
            'class_name': 'PrimalItemStructure_MetalPipeIncline_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/19/Metal_Irrigation_Pipe_-_Inclined.png'
        },
        {
            'name': 'Metal Irrigation Pipe - Intake', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeIntake.PrimalItemStructure_MetalPipeIntake\'"',
            'description': 'The metal intake for an irrigation network that transports water over land.',
            'url': 'https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Intake', 'id': 197,
            'class_name': 'PrimalItemStructure_MetalPipeIntake_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Metal_Irrigation_Pipe_-_Intake.png'
        },
        {
            'name': 'Metal Irrigation Pipe - Intersection', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeIntersection.PrimalItemStructure_MetalPipeIntersection\'"',
            'description': 'A plus-shaped metal intersection for an irrigation network, used for splitting one water source into three.',
            'url': 'https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Intersection', 'id': 198,
            'class_name': 'PrimalItemStructure_MetalPipeIntersection_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/77/Metal_Irrigation_Pipe_-_Intersection.png'
        },
        {
            'name': 'Metal Irrigation Pipe - Straight', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeStraight.PrimalItemStructure_MetalPipeStraight\'"',
            'description': 'A straight metal pipe for an irrigation network, used for transporting water across land.',
            'url': 'https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Straight', 'id': 199,
            'class_name': 'PrimalItemStructure_MetalPipeStraight_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Metal_Irrigation_Pipe_-_Straight.png'
        },
        {
            'name': 'Metal Irrigation Pipe - Tap', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeTap.PrimalItemStructure_MetalPipeTap\'"',
            'description': 'This metal tap allows access to the water in an irrigation network. Can refill containers, irrigate crop plots, or provide a refreshing drink.',
            'url': 'https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Tap', 'id': 200,
            'class_name': 'PrimalItemStructure_MetalPipeTap_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Metal_Irrigation_Pipe_-_Tap.png'
        },
        {
            'name': 'Metal Irrigation Pipe - Vertical', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_MetalPipeVertical.PrimalItemStructure_MetalPipeVertical\'"',
            'description': 'A vertical metal pipe for an irrigation network, used for transporting water up and down cliffs.',
            'url': 'https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Vertical', 'id': 201,
            'class_name': 'PrimalItemStructure_MetalPipeVertical_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d9/Metal_Irrigation_Pipe_-_Vertical.png'
        },
        {
            'name': 'Metal Sign', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSign.PrimalItemStructure_MetalSign\'"',
            'description': 'A small metal sign for landmark navigation or relaying messages.',
            'url': 'https://ark.fandom.com/wiki/Metal_Sign', 'id': 214, 'class_name': 'PrimalItemStructure_MetalSign_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Metal_Sign.png'
        },
        {
            'name': 'Wooden Billboard', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSign_Large.PrimalItemStructure_WoodSign_Large\'"',
            'description': 'A large wooden billboard for landmark navigation or relaying messages.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Billboard', 'id': 217,
            'class_name': 'PrimalItemStructure_WoodSign_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Wooden_Billboard.png'
        },
        {
            'name': 'Metal Billboard', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSign_Large.PrimalItemStructure_MetalSign_Large\'"',
            'description': 'A large metal billboard for landmark navigation or relaying messages.',
            'url': 'https://ark.fandom.com/wiki/Metal_Billboard', 'id': 239,
            'class_name': 'PrimalItemStructure_MetalSign_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Metal_Billboard.png'
        },
        {
            'name': 'Medium Crop Plot', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CropPlot_Medium.PrimalItemStructure_CropPlot_Medium\'"',
            'description': 'A medium garden plot, with a fence to keep out vermin.',
            'url': 'https://ark.fandom.com/wiki/Medium_Crop_Plot', 'id': 244,
            'class_name': 'PrimalItemStructure_CropPlot_Medium_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Medium_Crop_Plot.png'
        },
        {
            'name': 'Large Crop Plot', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_CropPlot_Large.PrimalItemStructure_CropPlot_Large\'"',
            'description': 'A large garden plot, with a fence to keep out vermin.',
            'url': 'https://ark.fandom.com/wiki/Large_Crop_Plot', 'id': 245,
            'class_name': 'PrimalItemStructure_CropPlot_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Large_Crop_Plot.png'
        },
        {
            'name': 'Wooden Wall Sign', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSign_Wall.PrimalItemStructure_WoodSign_Wall\'"',
            'description': 'A sturdy wooden wall that insulates the inside from the outside, separates rooms, and provides structural integrity.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Wall_Sign', 'id': 260,
            'class_name': 'PrimalItemStructure_WoodSign_Wall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Wooden_Wall.png'
        },
        {
            'name': 'Metal Dinosaur Gateway', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGateframe.PrimalItemStructure_MetalGateframe\'"',
            'description': 'A large metal gate that can be used with a Gateway to keep most dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Metal_Dinosaur_Gateway', 'id': 261,
            'class_name': 'PrimalItemStructure_MetalGateframe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/26/Metal_Dinosaur_Gate.png'
        },
        {
            'name': 'Metal Dinosaur Gate', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalGate.PrimalItemStructure_MetalGate\'"',
            'description': 'A large metal gate that can be used with a Gateway to keep most dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Metal_Dinosaur_Gate', 'id': 262,
            'class_name': 'PrimalItemStructure_MetalGate_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/26/Metal_Dinosaur_Gate.png'
        },
        {
            'name': 'Metal Wall Sign', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSign_Wall.PrimalItemStructure_MetalSign_Wall\'"',
            'description': 'A metal-plated concrete wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Metal_Wall_Sign', 'id': 265,
            'class_name': 'PrimalItemStructure_MetalSign_Wall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Metal_Wall.png'
        },
        {
            'name': 'Multi-Panel Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag.PrimalItemStructure_Flag\'"',
            'description': 'Mark your tribes territory and show off its colours by placing this and dying it.',
            'url': 'https://ark.fandom.com/wiki/Multi-Panel_Flag', 'id': 276,
            'class_name': 'PrimalItemStructure_Flag_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/76/Flag.png'
        },
        {
            'name': 'Spider Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Spider.PrimalItemStructure_Flag_Spider\'"',
            'description': 'This flag is proof that you have defeated the Broodmother.',
            'url': 'https://ark.fandom.com/wiki/Spider_Flag', 'id': 280,
            'class_name': 'PrimalItemStructure_Flag_Spider_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/10/Spider_Flag.png'
        },
        {
            'name': 'Preserving Bin', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_PreservingBin.PrimalItemStructure_PreservingBin\'"',
            'description': 'Burns simple fuel at low temperatures to dehydrate food and kill bacteria. Keeps perishables from spoiling for a small time.',
            'url': 'https://ark.fandom.com/wiki/Preserving_Bin', 'id': 291,
            'class_name': 'PrimalItemStructure_PreservingBin_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/09/Preserving_Bin.png'
        },
        {
            'name': 'Metal Spike Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalSpikeWall.PrimalItemStructure_MetalSpikeWall\'"',
            'description': 'These incredibly sharp metal spikes are dangerous to any that touch them. Large creatures take more damage.',
            'url': 'https://ark.fandom.com/wiki/Metal_Spike_Wall', 'id': 292,
            'class_name': 'PrimalItemStructure_MetalSpikeWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Metal_Spike_Wall.png'
        },
        {
            'name': 'Vault', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_StorageBox_Huge.PrimalItemStructure_StorageBox_Huge\'"',
            'description': 'A large metal vault to securely store goods in.',
            'url': 'https://ark.fandom.com/wiki/Vault', 'id': 302,
            'class_name': 'PrimalItemStructure_StorageBox_Huge_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c9/Vault.png'
        },
        {
            'name': 'Wooden Spike Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodSpikeWall.PrimalItemStructure_WoodSpikeWall\'"',
            'description': 'These incredibly sharp wooden stakes are dangerous to any that touch them. Larger creatures take more damage.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Spike_Wall', 'id': 303,
            'class_name': 'PrimalItemStructure_WoodSpikeWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Wooden_Spike_Wall.png'
        },
        {
            'name': 'Bookshelf', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bookshelf.PrimalItemStructure_Bookshelf\'"',
            'description': 'A large bookshelf to store Blueprints, Notes, and other small trinkets in.',
            'url': 'https://ark.fandom.com/wiki/Bookshelf', 'id': 305, 'class_name': 'PrimalItemStructure_Bookshelf_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Bookshelf.png'
        },
        {
            'name': 'Stone Fence Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneFenceFoundation.PrimalItemStructure_StoneFenceFoundation\'"',
            'description': 'This strong, narrow foundation is used to build walls around an area.',
            'url': 'https://ark.fandom.com/wiki/Stone_Fence_Foundation', 'id': 306,
            'class_name': 'PrimalItemStructure_StoneFenceFoundation_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c0/Stone_Fence_Foundation.png'
        },
        {
            'name': 'Stone Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneWall.PrimalItemStructure_StoneWall\'"',
            'description': 'A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Stone_Wall', 'id': 307, 'class_name': 'PrimalItemStructure_StoneWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png'
        },
        {
            'name': 'Metal Water Reservoir', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_WaterTankMetal.PrimalItemStructure_WaterTankMetal\'"',
            'description': 'A standing storage device for holding water. Automatically fills up during rain, can be filled up with the use of a water skin/jar.',
            'url': 'https://ark.fandom.com/wiki/Metal_Water_Reservoir', 'id': 308,
            'class_name': 'PrimalItemStructure_WaterTankMetal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Water_Reservoir.png'
        },
        {
            'name': 'Stone Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeiling.PrimalItemStructure_StoneCeiling\'"',
            'description': 'A stable brick-and-mortar ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Stone_Ceiling', 'id': 311,
            'class_name': 'PrimalItemStructure_StoneCeiling_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Stone_Ceiling.png'
        },
        {
            'name': 'Stone Hatchframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeilingWithTrapdoor.PrimalItemStructure_StoneCeilingWithTrapdoor\'"',
            'description': 'This brick-and-mortar ceiling has a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Stone_Hatchframe', 'id': 312,
            'class_name': 'PrimalItemStructure_StoneCeilingWithTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Stone_Hatchframe.png'
        },
        {
            'name': 'Reinforced Wooden Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneDoor.PrimalItemStructure_StoneDoor\'"',
            'description': 'A stable wooden door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Reinforced_Wooden_Door', 'id': 313,
            'class_name': 'PrimalItemStructure_StoneDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Wooden_Door.png'
        },
        {
            'name': 'Stone Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneFloor.PrimalItemStructure_StoneFloor\'"',
            'description': 'A foundation is required to build structures in an area. This one is made from brick-and-mortar.',
            'url': 'https://ark.fandom.com/wiki/Stone_Foundation', 'id': 314,
            'class_name': 'PrimalItemStructure_StoneFloor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f6/Stone_Foundation.png'
        },
        {
            'name': 'Reinforced Dinosaur Gate', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGate.PrimalItemStructure_StoneGate\'"',
            'description': 'A large, reinforced wooden gate that can be used with a Gateway to keep dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Reinforced_Dinosaur_Gate', 'id': 315,
            'class_name': 'PrimalItemStructure_StoneGate_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Reinforced_Dinosaur_Gate.png'
        },
        {
            'name': 'Stone Dinosaur Gateway', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGateframe.PrimalItemStructure_StoneGateframe\'"',
            'description': 'A large brick-and-mortar gateway that can be used with a Gate to keep most dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Stone_Dinosaur_Gateway', 'id': 316,
            'class_name': 'PrimalItemStructure_StoneGateframe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Stone_Dinosaur_Gateway.png'
        },
        {
            'name': 'Stone Pillar', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StonePillar.PrimalItemStructure_StonePillar\'"',
            'description': 'Adds structural integrity to the area it is built on. Can also act as stilts for buildings on inclines.',
            'url': 'https://ark.fandom.com/wiki/Stone_Pillar', 'id': 317,
            'class_name': 'PrimalItemStructure_StonePillar_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Stone_Pillar.png'
        },
        {
            'name': 'Stone Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneWallWithDoor.PrimalItemStructure_StoneWallWithDoor\'"',
            'description': 'A stone wall that provides entrance to a structure.',
            'url': 'https://ark.fandom.com/wiki/Stone_Doorframe', 'id': 318,
            'class_name': 'PrimalItemStructure_StoneWallWithDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Stone_Doorframe.png'
        },
        {
            'name': 'Stone Windowframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneWallWithWindow.PrimalItemStructure_StoneWallWithWindow\'"',
            'description': 'A brick-and-mortar wall with a hole for a window.',
            'url': 'https://ark.fandom.com/wiki/Stone_Windowframe', 'id': 319,
            'class_name': 'PrimalItemStructure_StoneWallWithWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Stone_Windowframe.png'
        },
        {
            'name': 'Reinforced Window', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_StoneWindow.PrimalItemStructure_StoneWindow\'"',
            'description': 'Reinforced window covering to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Reinforced_Window', 'id': 353,
            'class_name': 'PrimalItemStructure_StoneWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Reinforced_Window.png'
        },
        {
            'name': 'Reinforced Trapdoor', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_StoneTrapdoor.PrimalItemStructure_StoneTrapdoor\'"',
            'description': 'This small reinforced door can be used to secure hatches.',
            'url': 'https://ark.fandom.com/wiki/Reinforced_Trapdoor', 'id': 354,
            'class_name': 'PrimalItemStructure_StoneTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Reinforced_Trapdoor.png'
        },
        {
            'name': 'Omnidirectional Lamppost', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_LamppostOmni.PrimalItemStructure_LamppostOmni\'"',
            'description': 'Requires electricity to activate. Lights an area without adding much heat.',
            'url': 'https://ark.fandom.com/wiki/Omnidirectional_Lamppost', 'id': 355,
            'class_name': 'PrimalItemStructure_LamppostOmni_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Omnidirectional_Lamppost.png'
        },
        {
            'name': 'Industrial Grill', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Grill.PrimalItemStructure_Grill\'"',
            'description': 'Perfect for cooking meat in bulk, staying warm, and providing light. Powered by Gasoline.',
            'url': 'https://ark.fandom.com/wiki/Industrial_Grill', 'id': 356,
            'class_name': 'PrimalItemStructure_Grill_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/90/Industrial_Grill.png'
        },
        {
            'name': 'Single Panel Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Single.PrimalItemStructure_Flag_Single\'"',
            'description': "Mark your tribe's territory by placing this and painting it.",
            'url': 'https://ark.fandom.com/wiki/Single_Panel_Flag', 'id': 370,
            'class_name': 'PrimalItemStructure_Flag_Single_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Single_Panel_Flag.png'
        },
        {
            'name': 'Feeding Trough', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_FeedingTrough.PrimalItemStructure_FeedingTrough\'"',
            'description': "Put food for your nearby pets in this, and they'll automatically eat it when hungry!",
            'url': 'https://ark.fandom.com/wiki/Feeding_Trough', 'id': 371,
            'class_name': 'PrimalItemStructure_FeedingTrough_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Feeding_Trough.png'
        },
        {
            'name': 'Behemoth Stone Dinosaur Gateway', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGateframe_Large.PrimalItemStructure_StoneGateframe_Large\'"',
            'description': 'A large brick-and-mortar gateway that can be used with a Gate to keep most dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Stone_Dinosaur_Gateway', 'id': 377,
            'class_name': 'PrimalItemStructure_StoneGateframe_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Stone_Dinosaur_Gateway.png'
        },
        {
            'name': 'Behemoth Reinforced Dinosaur Gate', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneGateLarge.PrimalItemStructure_StoneGateLarge\'"',
            'description': 'A large, reinforced wooden gate that can be used with a Gateway to keep dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Reinforced_Dinosaur_Gate', 'id': 378,
            'class_name': 'PrimalItemStructure_StoneGateLarge_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Reinforced_Dinosaur_Gate.png'
        },
        {
            'name': 'Sloped Thatch Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Thatch/PrimalItemStructure_ThatchRoof.PrimalItemStructure_ThatchRoof\'"',
            'description': 'An inclined thatched roof. Slightly different angle than the ramp.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Thatch_Roof', 'id': 390,
            'class_name': 'PrimalItemStructure_ThatchRoof_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9d/Sloped_Thatch_Roof.png'
        },
        {
            'name': 'Sloped Thatch Wall Left', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Thatch/PrimalItemStructure_ThatchWall_Sloped_Left.PrimalItemStructure_ThatchWall_Sloped_Left\'"',
            'description': 'A simple wall made of bundled sticks, and stabilized by a wooden frame. Fairly fragile, but better than nothing.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Thatch_Wall_Left', 'id': 391,
            'class_name': 'PrimalItemStructure_ThatchWall_Sloped_Left_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Thatch_Wall.png'
        },
        {
            'name': 'Sloped Thatch Wall Right', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Thatch/PrimalItemStructure_ThatchWall_Sloped_Right.PrimalItemStructure_ThatchWall_Sloped_Right\'"',
            'description': 'A simple wall made of bundled sticks, and stabilized by a wooden frame. Fairly fragile, but better than nothing.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Thatch_Wall_Right', 'id': 392,
            'class_name': 'PrimalItemStructure_ThatchWall_Sloped_Right_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Thatch_Wall.png'
        },
        {
            'name': 'Sloped Wooden Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Wood/PrimalItemStructure_WoodRoof.PrimalItemStructure_WoodRoof\'"',
            'description': 'An inclined wooden roof. Slightly different angle than the ramp.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Wooden_Roof', 'id': 393,
            'class_name': 'PrimalItemStructure_WoodRoof_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f6/Sloped_Wooden_Roof.png'
        },
        {
            'name': 'Sloped Wood Wall Left', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Wood/PrimalItemStructure_WoodWall_Sloped_Left.PrimalItemStructure_WoodWall_Sloped_Left\'"',
            'description': 'A sturdy Wooden sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Wood_Wall_Left', 'id': 394,
            'class_name': 'PrimalItemStructure_WoodWall_Sloped_Left_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Sloped_Wood_Wall_Left.png'
        },
        {
            'name': 'Sloped Wood Wall Right', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Wood/PrimalItemStructure_WoodWall_Sloped_Right.PrimalItemStructure_WoodWall_Sloped_Right\'"',
            'description': 'A sturdy Wooden sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Wood_Wall_Right', 'id': 395,
            'class_name': 'PrimalItemStructure_WoodWall_Sloped_Right_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Sloped_Wood_Wall_Right.png'
        },
        {
            'name': 'Sloped Stone Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Stone/PrimalItemStructure_StoneRoof.PrimalItemStructure_StoneRoof\'"',
            'description': 'An inclined stone roof. Slightly different angle than the ramp.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Stone_Roof', 'id': 396,
            'class_name': 'PrimalItemStructure_StoneRoof_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b9/Sloped_Stone_Roof.png'
        },
        {
            'name': 'Sloped Stone Wall Left', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Stone/PrimalItemStructure_StoneWall_Sloped_Left.PrimalItemStructure_StoneWall_Sloped_Left\'"',
            'description': 'A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Stone_Wall_Left', 'id': 397,
            'class_name': 'PrimalItemStructure_StoneWall_Sloped_Left_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png'
        },
        {
            'name': 'Sloped Stone Wall Right', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Stone/PrimalItemStructure_StoneWall_Sloped_Right.PrimalItemStructure_StoneWall_Sloped_Right\'"',
            'description': 'A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Stone_Wall_Right', 'id': 398,
            'class_name': 'PrimalItemStructure_StoneWall_Sloped_Right_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png'
        },
        {
            'name': 'Sloped Metal Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Metal/PrimalItemStructure_MetalRoof.PrimalItemStructure_MetalRoof\'"',
            'description': 'An inclined metal roof. Slightly different angle than the ramp.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Metal_Roof', 'id': 399,
            'class_name': 'PrimalItemStructure_MetalRoof_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3f/Sloped_Metal_Roof.png'
        },
        {
            'name': 'Sloped Metal Wall Left', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Metal/PrimalItemStructure_MetalWall_Sloped_Left.PrimalItemStructure_MetalWall_Sloped_Left\'"',
            'description': 'A sturdy metal sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Metal_Wall_Left', 'id': 400,
            'class_name': 'PrimalItemStructure_MetalWall_Sloped_Left_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Sloped_Metal_Wall_Left.png'
        },
        {
            'name': 'Sloped Metal Wall Right', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Roofs/Metal/PrimalItemStructure_MetalWall_Sloped_Right.PrimalItemStructure_MetalWall_Sloped_Right\'"',
            'description': 'A sturdy metal sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Metal_Wall_Right', 'id': 401,
            'class_name': 'PrimalItemStructure_MetalWall_Sloped_Right_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Sloped_Metal_Wall_Right.png'
        },
        {
            'name': 'Wooden Raft', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Items/Raft/PrimalItemRaft.PrimalItemRaft\'"',
            'description': 'A floating wooden platform that you can pilot across the water. Can support the weight of structures and be built on.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Raft', 'id': 410, 'class_name': 'PrimalItemRaft_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Wooden_Raft.png'
        },
        {
            'name': 'Painting Canvas', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_PaintingCanvas.PrimalItemStructure_PaintingCanvas\'"',
            'description': 'A canvas sheet stretched over a wooden frame. Perfect for painting on.',
            'url': 'https://ark.fandom.com/wiki/Painting_Canvas', 'id': 416,
            'class_name': 'PrimalItemStructure_PaintingCanvas_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Painting_Canvas.png'
        },
        {
            'name': 'Greenhouse Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWall.PrimalItemStructure_GreenhouseWall\'"',
            'description': 'A metal-framed, glass wall that insulates the inside from the outside and separates rooms. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Wall', 'id': 433,
            'class_name': 'PrimalItemStructure_GreenhouseWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3c/Greenhouse_Wall.png'
        },
        {
            'name': 'Greenhouse Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseCeiling.PrimalItemStructure_GreenhouseCeiling\'"',
            'description': 'A metal-framed, glass ceiling that provides insulation, and doubles as a floor for higher levels. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Ceiling', 'id': 434,
            'class_name': 'PrimalItemStructure_GreenhouseCeiling_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Greenhouse_Ceiling.png'
        },
        {
            'name': 'Greenhouse Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWallWithDoor.PrimalItemStructure_GreenhouseWallWithDoor\'"',
            'description': 'A metal-frame, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Doorframe', 'id': 435,
            'class_name': 'PrimalItemStructure_GreenhouseWallWithDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Greenhouse_Door.png'
        },
        {
            'name': 'Greenhouse Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseDoor.PrimalItemStructure_GreenhouseDoor\'"',
            'description': 'A metal-frame, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Door', 'id': 436,
            'class_name': 'PrimalItemStructure_GreenhouseDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Greenhouse_Door.png'
        },
        {
            'name': 'Sloped Greenhouse Wall Left', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWall_Sloped_Left.PrimalItemStructure_GreenhouseWall_Sloped_Left\'"',
            'description': 'A metal-frame, glass sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Greenhouse_Wall_Left', 'id': 437,
            'class_name': 'PrimalItemStructure_GreenhouseWall_Sloped_Left_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/95/Sloped_Greenhouse_Wall_Left.png'
        },
        {
            'name': 'Sloped Greenhouse Wall Right', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWall_Sloped_Right.PrimalItemStructure_GreenhouseWall_Sloped_Right\'"',
            'description': 'A metal-frame, glass sloped wall that insulates the inside from the outside, separates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Greenhouse_Wall_Right', 'id': 438,
            'class_name': 'PrimalItemStructure_GreenhouseWall_Sloped_Right_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/12/Sloped_Greenhouse_Wall_Right.png'
        },
        {
            'name': 'Sloped Greenhouse Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseRoof.PrimalItemStructure_GreenhouseRoof\'"',
            'description': 'An inclined metal-frame, glass roof. Slightly different angle than the ramp. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Greenhouse_Roof', 'id': 439,
            'class_name': 'PrimalItemStructure_GreenhouseRoof_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Greenhouse_Roof.png'
        },
        {
            'name': 'Greenhouse Window', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Greenhouse/PrimalItemStructure_GreenhouseWindow.PrimalItemStructure_GreenhouseWindow\'"',
            'description': 'Metal-framed, glass plates on hinges that cover windows to provide protection from projectiles and spying. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Window', 'id': 440,
            'class_name': 'PrimalItemStructure_GreenhouseWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/35/Greenhouse_Window.png'
        },
        {
            'name': 'Tek Dedicated Storage', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Misc/DedicatedStorage/PrimalItemStructure_DedicatedStorage.PrimalItemStructure_DedicatedStorage\'"',
            'description': 'Holds a large amount of a single resource.',
            'url': 'https://ark.fandom.com/wiki/Tek_Dedicated_Storage', 'id': 449,
            'class_name': 'PrimalItemStructure_DedicatedStorage_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/Tek_Dedicated_Storage.png'
        },
        {
            'name': 'Adobe Double Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Adobe/PrimalItemStructure_DoubleDoor_Adobe.PrimalItemStructure_DoubleDoor_Adobe\'"',
            'description': 'A stable adobe door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Double_Door_(Scorched_Earth)', 'id': 450,
            'class_name': 'PrimalItemStructure_DoubleDoor_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/77/Adobe_Double_Door_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Greenhouse Double Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Greenhouse/PrimalItemStructure_DoubleDoor_Greenhouse.PrimalItemStructure_DoubleDoor_Greenhouse\'"',
            'description': 'A metal-framed, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Double_Door', 'id': 451,
            'class_name': 'PrimalItemStructure_DoubleDoor_Greenhouse_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Greenhouse_Double_Door.png'
        },
        {
            'name': 'Metal Double Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Metal/PrimalItemStructure_DoubleDoor_Metal.PrimalItemStructure_DoubleDoor_Metal\'"',
            'description': 'A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Metal_Double_Door', 'id': 452,
            'class_name': 'PrimalItemStructure_DoubleDoor_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e5/Metal_Double_Door.png'
        },
        {
            'name': 'Reinforced Double Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Stone/PrimalItemStructure_DoubleDoor_Stone.PrimalItemStructure_DoubleDoor_Stone\'"',
            'description': 'A reinforced wooden door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Reinforced_Double_Door', 'id': 453,
            'class_name': 'PrimalItemStructure_DoubleDoor_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b0/Reinforced_Double_Door.png'
        },
        {
            'name': 'Tek Double Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Tek/PrimalItemStructure_DoubleDoor_Tek.PrimalItemStructure_DoubleDoor_Tek\'"',
            'description': 'A stable composite door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Tek_Double_Door', 'id': 454,
            'class_name': 'PrimalItemStructure_DoubleDoor_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Tek_Double_Door.png'
        },
        {
            'name': 'Wooden Double Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Doors/Doors_Double/Wood/PrimalItemStructure_DoubleDoor_Wood.PrimalItemStructure_DoubleDoor_Wood\'"',
            'description': 'A stable wooden door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Double_Door', 'id': 455,
            'class_name': 'PrimalItemStructure_DoubleDoor_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/af/Wooden_Double_Door.png'
        },
        {
            'name': 'Adobe Double Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Adobe/PrimalItemStructure_DoubleDoorframe_Adobe.PrimalItemStructure_DoubleDoorframe_Adobe\'"',
            'description': 'A stable adobe door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Double_Doorframe_(Scorched_Earth)', 'id': 456,
            'class_name': 'PrimalItemStructure_DoubleDoorframe_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/77/Adobe_Double_Door_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Greenhouse Double Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Greenhouse/PrimalItemStructure_DoubleDoorframe_Greenhouse.PrimalItemStructure_DoubleDoorframe_Greenhouse\'"',
            'description': 'A metal-framed, glass door that provides entrance to structures. Can be locked for security. Excellent for growing crops indoors',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Double_Doorframe', 'id': 457,
            'class_name': 'PrimalItemStructure_DoubleDoorframe_Greenhouse_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Greenhouse_Double_Door.png'
        },
        {
            'name': 'Metal Double Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Metal/PrimalItemStructure_DoubleDoorframe_Metal.PrimalItemStructure_DoubleDoorframe_Metal\'"',
            'description': 'A stable metal-plated concrete door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Metal_Double_Doorframe', 'id': 458,
            'class_name': 'PrimalItemStructure_DoubleDoorframe_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e5/Metal_Double_Door.png'
        },
        {
            'name': 'Stone Double Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Stone/PrimalItemStructure_DoubleDoorframe_Stone.PrimalItemStructure_DoubleDoorframe_Stone\'"',
            'description': 'A brick-and-mortar wall that provides entrance to a structure.',
            'url': 'https://ark.fandom.com/wiki/Stone_Double_Doorframe', 'id': 459,
            'class_name': 'PrimalItemStructure_DoubleDoorframe_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Stone_Double_Doorframe.png'
        },
        {
            'name': 'Tek Double Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Tek/PrimalItemStructure_DoubleDoorframe_Tek.PrimalItemStructure_DoubleDoorframe_Tek\'"',
            'description': 'A stable composite door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Tek_Double_Doorframe', 'id': 460,
            'class_name': 'PrimalItemStructure_DoubleDoorframe_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Tek_Double_Door.png'
        },
        {
            'name': 'Wooden Double Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Doorframes_Double/Wood/PrimalItemStructure_DoubleDoorframe_Wood.PrimalItemStructure_DoubleDoorframe_Wood\'"',
            'description': 'A stable wooden door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Double_Doorframe', 'id': 461,
            'class_name': 'PrimalItemStructure_DoubleDoorframe_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/af/Wooden_Double_Door.png'
        },
        {
            'name': 'Adobe Fence Support', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Adobe/PrimalItemStructure_FenceSupport_Adobe.PrimalItemStructure_FenceSupport_Adobe\'"',
            'description': "Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
            'url': 'https://ark.fandom.com/wiki/Adobe_Fence_Support_(Scorched_Earth)', 'id': 462,
            'class_name': 'PrimalItemStructure_FenceSupport_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Adobe_Fence_Support_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Metal Fence Support', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Metal/PrimalItemStructure_FenceSupport_Metal.PrimalItemStructure_FenceSupport_Metal\'"',
            'description': "Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
            'url': 'https://ark.fandom.com/wiki/Metal_Fence_Support', 'id': 463,
            'class_name': 'PrimalItemStructure_FenceSupport_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Metal_Fence_Support.png'
        },
        {
            'name': 'Stone Fence Support', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Stone/PrimalItemStructure_FenceSupport_Stone.PrimalItemStructure_FenceSupport_Stone\'"',
            'description': "Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
            'url': 'https://ark.fandom.com/wiki/Stone_Fence_Support', 'id': 464,
            'class_name': 'PrimalItemStructure_FenceSupport_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/69/Stone_Fence_Support.png'
        },
        {
            'name': 'Tek Fence Support', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Tek/PrimalItemStructure_FenceSupport_Tek.PrimalItemStructure_FenceSupport_Tek\'"',
            'description': "Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
            'url': 'https://ark.fandom.com/wiki/Tek_Fence_Support', 'id': 465,
            'class_name': 'PrimalItemStructure_FenceSupport_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1a/Tek_Fence_Support.png'
        },
        {
            'name': 'Wooden Fence Support', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/FenceSupports/Wood/PrimalItemStructure_FenceSupport_Wood.PrimalItemStructure_FenceSupport_Wood\'"',
            'description': "Acts as a foundation so you can build on fence walls. Doesn't follow ground so can build level fences.",
            'url': 'https://ark.fandom.com/wiki/Wooden_Fence_Support', 'id': 466,
            'class_name': 'PrimalItemStructure_FenceSupport_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Wooden_Fence_Support.png'
        },
        {
            'name': 'Large Adobe Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Adobe/PrimalItemStructure_LargeWall_Adobe.PrimalItemStructure_LargeWall_Adobe\'"',
            'description': 'A wall that is as tall as four normal walls.',
            'url': 'https://ark.fandom.com/wiki/Large_Adobe_Wall_(Scorched_Earth)', 'id': 467,
            'class_name': 'PrimalItemStructure_LargeWall_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/10/Large_Adobe_Wall_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Large Metal Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Metal/PrimalItemStructure_LargeWall_Metal.PrimalItemStructure_LargeWall_Metal\'"',
            'description': 'A metal-plated concrete wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Large_Metal_Wall', 'id': 468,
            'class_name': 'PrimalItemStructure_LargeWall_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Metal_Wall.png'
        },
        {
            'name': 'Large Stone Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Stone/PrimalItemStructure_LargeWall_Stone.PrimalItemStructure_LargeWall_Stone\'"',
            'description': 'A brick-and-mortar wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Large_Stone_Wall', 'id': 469,
            'class_name': 'PrimalItemStructure_LargeWall_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Stone_Wall.png'
        },
        {
            'name': 'Large Tek Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Tek/PrimalItemStructure_LargeWall_Tek.PrimalItemStructure_LargeWall_Tek\'"',
            'description': 'A composite Tek wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Large_Tek_Wall', 'id': 470,
            'class_name': 'PrimalItemStructure_LargeWall_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png'
        },
        {
            'name': 'Large Wooden Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Walls_L/Wood/PrimalItemStructure_LargeWall_Wood.PrimalItemStructure_LargeWall_Wood\'"',
            'description': 'A sturdy wooden wall that insulates the inside from the outside, separates rooms, and provides structural integrity.',
            'url': 'https://ark.fandom.com/wiki/Large_Wooden_Wall', 'id': 471,
            'class_name': 'PrimalItemStructure_LargeWall_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Wooden_Wall.png'
        },
        {
            'name': 'Metal Irrigation Pipe - Flexible', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Pipes/Flex/Metal/PrimalItemStructure_PipeFlex_Metal.PrimalItemStructure_PipeFlex_Metal\'"',
            'description': 'Connects nearby pipes dynamically.',
            'url': 'https://ark.fandom.com/wiki/Metal_Irrigation_Pipe_-_Flexible', 'id': 472,
            'class_name': 'PrimalItemStructure_PipeFlex_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/db/Metal_Irrigation_Pipe_-_Flexible.png'
        },
        {
            'name': 'Stone Irrigation Pipe - Flexible', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Pipes/Flex/Stone/PrimalItemStructure_PipeFlex_Stone.PrimalItemStructure_PipeFlex_Stone\'"',
            'description': 'Connects nearby pipes dynamically.',
            'url': 'https://ark.fandom.com/wiki/Stone_Irrigation_Pipe_-_Flexible', 'id': 473,
            'class_name': 'PrimalItemStructure_PipeFlex_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/57/Stone_Irrigation_Pipe_-_Flexible.png'
        },
        {
            'name': 'Adobe Stairs', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Adobe/PrimalItemStructure_Ramp_Adobe.PrimalItemStructure_Ramp_Adobe\'"',
            'description': 'Adobe-plated concrete stairs for travelling up or down levels. Can be switched to a ramp variant.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Stairs_(Scorched_Earth)', 'id': 474,
            'class_name': 'PrimalItemStructure_Ramp_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/28/Adobe_Stairs_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Metal Stairs', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Metal/PrimalItemStructure_Ramp_Metal.PrimalItemStructure_Ramp_Metal\'"',
            'description': 'Metal-plated concrete stairs for travelling up or down levels. Can be switched to a ramp variant.',
            'url': 'https://ark.fandom.com/wiki/Metal_Stairs', 'id': 475,
            'class_name': 'PrimalItemStructure_Ramp_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Metal_Stairs.png'
        },
        {
            'name': 'Stone Stairs', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Stone/PrimalItemStructure_Ramp_Stone.PrimalItemStructure_Ramp_Stone\'"',
            'description': 'Stone stairs for traveling up or down levels. Can be switched to a ramp variant.',
            'url': 'https://ark.fandom.com/wiki/Stone_Stairs', 'id': 476,
            'class_name': 'PrimalItemStructure_Ramp_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1d/Stone_Stairs.png'
        },
        {
            'name': 'Tek Stairs', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Tek/PrimalItemStructure_Ramp_Tek.PrimalItemStructure_Ramp_Tek\'"',
            'description': 'Composite Tek stairs for travelling up or down levels. Can be switched to a ramp variant.',
            'url': 'https://ark.fandom.com/wiki/Tek_Stairs', 'id': 477, 'class_name': 'PrimalItemStructure_Ramp_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Tek_Stairs.png'
        },
        {
            'name': 'Wooden Stairs', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ramps/Wood/PrimalItemStructure_Ramp_Wood.PrimalItemStructure_Ramp_Wood\'"',
            'description': 'Wooden stairs for traveling up or down levels. Can be switched to a ramp variant.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Stairs', 'id': 478,
            'class_name': 'PrimalItemStructure_Ramp_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5e/Wooden_Stairs.png'
        },
        {
            'name': 'Adobe Triangle Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Adobe/PrimalItemStructure_TriCeiling_Adobe.PrimalItemStructure_TriCeiling_Adobe\'"',
            'description': 'A stable adobe-plated concrete ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Triangle_Ceiling_(Scorched_Earth)', 'id': 479,
            'class_name': 'PrimalItemStructure_TriCeiling_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/24/Adobe_Triangle_Ceiling_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Greenhouse Triangle Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Greenhouse/PrimalItemStructure_TriCeiling_Greenhouse.PrimalItemStructure_TriCeiling_Greenhouse\'"',
            'description': 'A metal-framed, glass ceiling that insulates the inside from the outside, and doubles as a floor for higher levels. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Triangle_Ceiling', 'id': 480,
            'class_name': 'PrimalItemStructure_TriCeiling_Greenhouse_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/28/Greenhouse_Triangle_Ceiling.png'
        },
        {
            'name': 'Metal Triangle Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Metal/PrimalItemStructure_TriCeiling_Metal.PrimalItemStructure_TriCeiling_Metal\'"',
            'description': 'A stable metal-plated concrete ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Metal_Triangle_Ceiling', 'id': 481,
            'class_name': 'PrimalItemStructure_TriCeiling_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Metal_Triangle_Ceiling.png'
        },
        {
            'name': 'Stone Triangle Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Stone/PrimalItemStructure_TriCeiling_Stone.PrimalItemStructure_TriCeiling_Stone\'"',
            'description': 'A stable brick-and-mortar ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Stone_Triangle_Ceiling', 'id': 482,
            'class_name': 'PrimalItemStructure_TriCeiling_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Stone_Triangle_Ceiling.png'
        },
        {
            'name': 'Tek Triangle Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Tek/PrimalItemStructure_TriCeiling_Tek.PrimalItemStructure_TriCeiling_Tek\'"',
            'description': 'An incredibly durable composite Tek ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Tek_Triangle_Ceiling', 'id': 483,
            'class_name': 'PrimalItemStructure_TriCeiling_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Tek_Triangle_Ceiling.png'
        },
        {
            'name': 'Wooden Triangle Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Ceilings/Triangle/Wood/PrimalItemStructure_TriCeiling_Wood.PrimalItemStructure_TriCeiling_Wood\'"',
            'description': 'A stable wooden ceiling that insulates the inside from the outside, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Triangle_Ceiling', 'id': 484,
            'class_name': 'PrimalItemStructure_TriCeiling_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Wooden_Triangle_Ceiling.png'
        },
        {
            'name': 'Adobe Triangle Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Adobe/PrimalItemStructure_TriFoundation_Adobe.PrimalItemStructure_TriFoundation_Adobe\'"',
            'description': 'Required to build structures in an area. Triangle shaped.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Triangle_Foundation_(Scorched_Earth)', 'id': 485,
            'class_name': 'PrimalItemStructure_TriFoundation_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/da/Adobe_Triangle_Foundation_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Metal Triangle Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Metal/PrimalItemStructure_TriFoundation_Metal.PrimalItemStructure_TriFoundation_Metal\'"',
            'description': 'Required to build structures in an area. Triangle shaped.',
            'url': 'https://ark.fandom.com/wiki/Metal_Triangle_Foundation', 'id': 486,
            'class_name': 'PrimalItemStructure_TriFoundation_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/67/Metal_Triangle_Foundation.png'
        },
        {
            'name': 'Stone Triangle Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Stone/PrimalItemStructure_TriFoundation_Stone.PrimalItemStructure_TriFoundation_Stone\'"',
            'description': 'Required to build structures in an area. Triangle shaped.',
            'url': 'https://ark.fandom.com/wiki/Stone_Triangle_Foundation', 'id': 487,
            'class_name': 'PrimalItemStructure_TriFoundation_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3c/Stone_Triangle_Foundation.png'
        },
        {
            'name': 'Tek Triangle Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Tek/PrimalItemStructure_TriFoundation_Tek.PrimalItemStructure_TriFoundation_Tek\'"',
            'description': 'Required to build structures in an area. Triangle shaped.',
            'url': 'https://ark.fandom.com/wiki/Tek_Triangle_Foundation', 'id': 488,
            'class_name': 'PrimalItemStructure_TriFoundation_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Tek_Triangle_Foundation.png'
        },
        {
            'name': 'Wooden Triangle Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Foundations/Triangle/Wood/PrimalItemStructure_TriFoundation_Wood.PrimalItemStructure_TriFoundation_Wood\'"',
            'description': 'Required to build structures in an area. Triangle shaped.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Triangle_Foundation', 'id': 489,
            'class_name': 'PrimalItemStructure_TriFoundation_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Wooden_Triangle_Foundation.png'
        },
        {
            'name': 'Adobe Triangle Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Adobe/PrimalItemStructure_TriRoof_Adobe.PrimalItemStructure_TriRoof_Adobe\'"',
            'description': 'A sloped adobe triangle roof.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Triangle_Roof_(Scorched_Earth)', 'id': 490,
            'class_name': 'PrimalItemStructure_TriRoof_Adobe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5f/Adobe_Triangle_Roof_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Greenhouse Triangle Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Greenhouse/PrimalItemStructure_TriRoof_Greenhouse.PrimalItemStructure_TriRoof_Greenhouse\'"',
            'description': 'A sloped greenhouse triangle roof.',
            'url': 'https://ark.fandom.com/wiki/Greenhouse_Triangle_Roof', 'id': 491,
            'class_name': 'PrimalItemStructure_TriRoof_Greenhouse_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Greenhouse_Triangle_Roof.png'
        },
        {
            'name': 'Metal Triangle Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Metal/PrimalItemStructure_TriRoof_Metal.PrimalItemStructure_TriRoof_Metal\'"',
            'description': 'A sloped metal triangle roof.', 'url': 'https://ark.fandom.com/wiki/Metal_Triangle_Roof',
            'id': 492, 'class_name': 'PrimalItemStructure_TriRoof_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Metal_Triangle_Roof.png'
        },
        {
            'name': 'Stone Triangle Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Stone/PrimalItemStructure_TriRoof_Stone.PrimalItemStructure_TriRoof_Stone\'"',
            'description': 'A sloped stone triangle roof.', 'url': 'https://ark.fandom.com/wiki/Stone_Triangle_Roof',
            'id': 493, 'class_name': 'PrimalItemStructure_TriRoof_Stone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Stone_Triangle_Roof.png'
        },
        {
            'name': 'Tek Triangle Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Tek/PrimalItemStructure_TriRoof_Tek.PrimalItemStructure_TriRoof_Tek\'"',
            'description': 'A sloped Tek triangle roof.', 'url': 'https://ark.fandom.com/wiki/Tek_Triangle_Roof',
            'id': 494, 'class_name': 'PrimalItemStructure_TriRoof_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dc/Tek_Triangle_Roof.png'
        },
        {
            'name': 'Wooden Triangle Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Structures/Roofs_Tri/Wood/PrimalItemStructure_TriRoof_Wood.PrimalItemStructure_TriRoof_Wood\'"',
            'description': 'A wood, sloped triangle roof.', 'url': 'https://ark.fandom.com/wiki/Wooden_Triangle_Roof',
            'id': 495, 'class_name': 'PrimalItemStructure_TriRoof_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/48/Wooden_Triangle_Roof.png'
        },
        {
            'name': 'Flexible Electrical Cable', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/StructuresPlus/Wires/Flex/PrimalItemStructure_Wire_Flex.PrimalItemStructure_Wire_Flex\'"',
            'description': 'Connects nearby cables dynamically',
            'url': 'https://ark.fandom.com/wiki/Flexible_Electrical_Cable', 'id': 496,
            'class_name': 'PrimalItemStructure_Wire_Flex_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9f/Flexible_Electrical_Cable.png'
        },
        {
            'name': 'Pumpkin', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_Pumpkin.PrimalItemStructure_Pumpkin\'"',
            'description': 'Decorate your base with this pumpkin. Can be "carved" with all manner of paints.',
            'url': 'https://ark.fandom.com/wiki/Pumpkin', 'id': 497, 'class_name': None,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/64/Pumpkin.png'
        },
        {
            'name': 'Scarecrow', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_Scarecrow.PrimalItemStructure_Scarecrow\'"',
            'description': 'Decorate your base with this scarecrow. Guaranteed to scare the crows away.',
            'url': 'https://ark.fandom.com/wiki/Scarecrow', 'id': 498, 'class_name': None,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/75/Scarecrow.png'
        },
        {
            'name': 'Stolen Headstone', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_HW_Grave.PrimalItemStructure_HW_Grave\'"',
            'description': 'A headstone stolen from a graveyard.',
            'url': 'https://ark.fandom.com/wiki/Stolen_Headstone', 'id': 499, 'class_name': None,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Stolen_Headstone.png'
        },
        {
            'name': 'Wreath', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_Wreath.PrimalItemStructure_Wreath\'"',
            'description': 'A decorative collection of leaves that make any room festive. Requires attaching to a wall.',
            'url': 'https://ark.fandom.com/wiki/Wreath', 'id': 500, 'class_name': 'PrimalItemStructure_Wreath_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/de/Wreath.png'
        },
        {
            'name': 'Holiday Lights', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_XmasLights.PrimalItemStructure_XmasLights\'"',
            'description': 'A decoration string of lights that make any room festive. Requires attaching to a wall.',
            'url': 'https://ark.fandom.com/wiki/Holiday_Lights', 'id': 501,
            'class_name': 'PrimalItemStructure_XmasLights_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Holiday_Lights.png'
        },
        {
            'name': 'Holiday Stocking', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_Stocking.PrimalItemStructure_Stocking\'"',
            'description': 'An oversized sock which adds jolliness to any holiday. Requires attaching to a wall.',
            'url': 'https://ark.fandom.com/wiki/Holiday_Stocking', 'id': 502,
            'class_name': 'PrimalItemStructure_Stocking_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Holiday_Stocking.png'
        },
        {
            'name': 'Holiday Tree', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_ChristmasTree.PrimalItemStructure_ChristmasTree\'"',
            'description': 'This is the perfect tree to use when celebrating the winter solstace!',
            'url': 'https://ark.fandom.com/wiki/Holiday_Tree', 'id': 503,
            'class_name': 'PrimalItemStructure_ChristmasTree_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Holiday_Tree.png'
        },
        {
            'name': 'Snowman', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_Snowman.PrimalItemStructure_Snowman\'"',
            'description': 'Put a hat on it for extra fun!', 'url': 'https://ark.fandom.com/wiki/Snowman', 'id': 504,
            'class_name': 'PrimalItemStructure_Snowman_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Snowman.png'
        },
        {
            'name': 'Gift Box', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Christmas/PrimalItemStructure_StorageBox_ChristmasGift.PrimalItemStructure_StorageBox_ChristmasGift\'"',
            'description': "Put items in this and inscribe a Tribemember's name, and only they will be able to open it, with a bang!",
            'url': 'https://ark.fandom.com/wiki/Gift_Box', 'id': 505,
            'class_name': 'PrimalItemStructure_StorageBox_ChristmasGift_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/56/Gift_Box.png'
        },
        {
            'name': 'Bunny Egg', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_EasterEgg.PrimalItemStructure_EasterEgg\'"',
            'description': 'Put it in a Cooking Pot to craft fun costumes or place on the ground as a festive decoration!',
            'url': 'https://ark.fandom.com/wiki/Bunny_Egg', 'id': 506, 'class_name': 'PrimalItemStructure_EasterEgg_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4d/Bunny_Egg.png'
        },
        {
            'name': 'Birthday Cake', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_BirthdayCake.PrimalItemStructure_BirthdayCake\'"',
            'description': 'Place this Cake on a table and blow out its candles to make a wish (then eat it). Or you can put it in a Cooking Pot for...',
            'url': 'https://ark.fandom.com/wiki/Birthday_Cake', 'id': 507, 'class_name': None,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Birthday_Cake.png'
        },
        {
            'name': 'Adobe Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeiling.PrimalItemStructure_AdobeCeiling\'"',
            'description': 'A stable adobe-plated concrete ceiling that provides insulation, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Ceiling_(Scorched_Earth)', 'id': 508,
            'class_name': 'PrimalItemStructure_AdobeCeiling_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/64/Adobe_Ceiling_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Dinosaur Gate', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeGateDoor.PrimalItemStructure_AdobeGateDoor\'"',
            'description': 'A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Dinosaur_Gate_(Scorched_Earth)', 'id': 509,
            'class_name': 'PrimalItemStructure_AdobeGateDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png'
        },
        {
            'name': 'Adobe Dinosaur Gateway', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeFrameGate.PrimalItemStructure_AdobeFrameGate\'"',
            'description': 'A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Dinosaur_Gateway_(Scorched_Earth)', 'id': 510,
            'class_name': 'PrimalItemStructure_AdobeFrameGate_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png'
        },
        {
            'name': 'Adobe Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeDoor.PrimalItemStructure_AdobeDoor\'"',
            'description': 'A stable adobe door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Door_(Scorched_Earth)', 'id': 511,
            'class_name': 'PrimalItemStructure_AdobeDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Adobe_Door_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWallWithDoor.PrimalItemStructure_AdobeWallWithDoor\'"',
            'description': 'A adobe wall that provides entrance to a structure.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Doorframe_(Scorched_Earth)', 'id': 512,
            'class_name': 'PrimalItemStructure_AdobeWallWithDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Adobe_Doorframe_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Fence Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeFenceFoundation.PrimalItemStructure_AdobeFenceFoundation\'"',
            'description': 'This very strong, narrow foundation is used to build walls around an area.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Fence_Foundation_(Scorched_Earth)', 'id': 513,
            'class_name': 'PrimalItemStructure_AdobeFenceFoundation_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Adobe_Fence_Foundation_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeFloor.PrimalItemStructure_AdobeFloor\'"',
            'description': 'Required to build structures in an area.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Foundation_(Scorched_Earth)', 'id': 514,
            'class_name': 'PrimalItemStructure_AdobeFloor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/55/Adobe_Foundation_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Hatchframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeilingWithTrapdoor.PrimalItemStructure_AdobeCeilingWithTrapdoor\'"',
            'description': 'This Adobe concrete ceiling has a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Hatchframe_(Scorched_Earth)', 'id': 515,
            'class_name': 'PrimalItemStructure_AdobeCeilingWithTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3f/Adobe_Hatchframe_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Ladder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeLader.PrimalItemStructure_AdobeLader\'"',
            'description': 'A simple adobe ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Ladder_(Scorched_Earth)', 'id': 516,
            'class_name': 'PrimalItemStructure_AdobeLader_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Adobe_Ladder_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Pillar', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobePillar.PrimalItemStructure_AdobePillar\'"',
            'description': 'The adobe pillar adds structural integrity to the area it is built under. Can also act as stilts for buildings on inclines.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Pillar_(Scorched_Earth)', 'id': 517,
            'class_name': 'PrimalItemStructure_AdobePillar_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Adobe_Pillar_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Railing', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeRailing.PrimalItemStructure_AdobeRailing\'"',
            'description': 'A adobe railing that acts a a simple barrier to prevent people from falling.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Railing_(Scorched_Earth)', 'id': 518,
            'class_name': 'PrimalItemStructure_AdobeRailing_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Adobe_Railing_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Ramp', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeRamp.PrimalItemStructure_AdobeRamp\'"',
            'description': 'An inclined adobe-plated concrete floor for travelling up or down levels. Can also be used to make an angled roof.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Ramp_(Scorched_Earth)', 'id': 519,
            'class_name': 'PrimalItemStructure_AdobeRamp_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c0/Adobe_Ramp_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Staircase', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeStaircase.PrimalItemStructure_AdobeStaircase\'"',
            'description': 'An adobe spiral staircase, useful in constructing multi-level buildings.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Staircase_(Scorched_Earth)', 'id': 520,
            'class_name': 'PrimalItemStructure_AdobeStaircase_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Adobe_Staircase_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Trapdoor', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeTrapdoor.PrimalItemStructure_AdobeTrapdoor\'"',
            'description': 'This adobe slab can be used to secure hatches.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Trapdoor_(Scorched_Earth)', 'id': 521,
            'class_name': 'PrimalItemStructure_AdobeTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/46/Adobe_Trapdoor_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWall.PrimalItemStructure_AdobeWall\'"',
            'description': 'An adobe wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Wall_(Scorched_Earth)', 'id': 522,
            'class_name': 'PrimalItemStructure_AdobeWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Adobe_Wall_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Window', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWindow.PrimalItemStructure_AdobeWindow\'"',
            'description': 'Adobe plates on hinges that cover windows to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Window_(Scorched_Earth)', 'id': 523,
            'class_name': 'PrimalItemStructure_AdobeWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Adobe_Window_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Adobe Windowframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWallWithWindow.PrimalItemStructure_AdobeWallWithWindow\'"',
            'description': 'An adobe wall, with a hole for a window.',
            'url': 'https://ark.fandom.com/wiki/Adobe_Windowframe_(Scorched_Earth)', 'id': 524,
            'class_name': 'PrimalItemStructure_AdobeWallWithWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/86/Adobe_Windowframe_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Artifact Pedestal', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TrophyBase.PrimalItemStructure_TrophyBase\'"',
            'description': 'Provides the base upon which you can proudly display an Artifact, among other things!',
            'url': 'https://ark.fandom.com/wiki/Artifact_Pedestal', 'id': 525,
            'class_name': 'PrimalItemStructure_TrophyBase_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Artifact_Pedestal.png'
        },
        {
            'name': 'Ballista Turret', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretBallista.PrimalItemStructure_TurretBallista\'"',
            'description': 'Mount this to fire large piercing Spear Bolts, useful for bringing down large dinos and structures.',
            'url': 'https://ark.fandom.com/wiki/Ballista_Turret', 'id': 526,
            'class_name': 'PrimalItemStructure_TurretBallista_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Ballista_Turret.png'
        },
        {
            'name': 'Bee Hive', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Structures/BeeHive/PrimalItemStructure_BeeHive.PrimalItemStructure_BeeHive\'"',
            'description': 'Bee hives house a queen bee and produces honey.',
            'url': 'https://ark.fandom.com/wiki/Bee_Hive', 'id': 527, 'class_name': 'PrimalItemStructure_BeeHive_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Bee_Hive.png'
        },
        {
            'name': 'Beer Barrel', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_BeerBarrel.PrimalItemStructure_BeerBarrel\'"',
            'description': 'Ferments tasty brew from Thatch, Water, and Berries',
            'url': 'https://ark.fandom.com/wiki/Beer_Barrel', 'id': 528,
            'class_name': 'PrimalItemStructure_BeerBarrel_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Beer_Barrel.png'
        },
        {
            'name': 'Behemoth Adobe Dinosaur Gate', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeGateDoor_Large.PrimalItemStructure_AdobeGateDoor_Large\'"',
            'description': 'A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Adobe_Dinosaur_Gate_(Scorched_Earth)', 'id': 529,
            'class_name': 'PrimalItemStructure_AdobeGateDoor_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png'
        },
        {
            'name': 'Behemoth Adobe Dinosaur Gateway', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeGateframe_Large.PrimalItemStructure_AdobeGateframe_Large\'"',
            'description': 'A large wooden gate that can be used with a gateway to keep dinosaurs in or out. Cannot be destroyed by any dinosaur.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Adobe_Dinosaur_Gateway_(Scorched_Earth)', 'id': 530,
            'class_name': 'PrimalItemStructure_AdobeGateframe_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Dinosaur_Gate.png'
        },
        {
            'name': 'Behemoth Tek Gateway', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGateframe_Large.PrimalItemStructure_TekGateframe_Large\'"',
            'description': 'A large composite Tek gate that can be used with a Behemoth Gateway to allow even the largest creatures in or out.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Tek_Gateway', 'id': 531,
            'class_name': 'PrimalItemStructure_TekGateframe_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Behemoth_Tek_Gate.png'
        },
        {
            'name': 'Behemoth Tek Gate', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGate_Large.PrimalItemStructure_TekGate_Large\'"',
            'description': 'A large composite Tek gate that can be used with a Behemoth Gateway to allow even the largest creatures in or out.',
            'url': 'https://ark.fandom.com/wiki/Behemoth_Tek_Gate', 'id': 532,
            'class_name': 'PrimalItemStructure_TekGate_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e7/Behemoth_Tek_Gate.png'
        },
        {
            'name': 'Bunk Bed', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bed_Modern.PrimalItemStructure_Bed_Modern\'"',
            'description': 'This modern bunk-style bed has two mattresses, and a high thread count. Acts as a respawn point for you and your tribe with half cooldown time.',
            'url': 'https://ark.fandom.com/wiki/Bunk_Bed', 'id': 533, 'class_name': 'PrimalItemStructure_Bed_Modern_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Bunk_Bed.png'
        },
        {
            'name': 'Cannon', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Cannon.PrimalItemStructure_Cannon\'"',
            'description': 'A powerful, heavy weapon of war, capable of demolishing heavily reinforced structures.',
            'url': 'https://ark.fandom.com/wiki/Cannon', 'id': 534, 'class_name': 'PrimalItemStructure_Cannon_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Cannon.png'
        },
        {
            'name': 'Catapult Turret', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretCatapult.PrimalItemStructure_TurretCatapult\'"',
            'description': 'Mount this to throw destructive Boulders at your enemies, particularly effective against Structures.',
            'url': 'https://ark.fandom.com/wiki/Catapult_Turret', 'id': 535,
            'class_name': 'PrimalItemStructure_TurretCatapult_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Catapult_Turret.png'
        },
        {
            'name': 'Chemistry Bench', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_ChemBench.PrimalItemStructure_ChemBench\'"',
            'description': 'Place materials in this to transmute chemical substances with extreme efficiency!',
            'url': 'https://ark.fandom.com/wiki/Chemistry_Bench', 'id': 536,
            'class_name': 'PrimalItemStructure_ChemBench_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9d/Chemistry_Bench.png'
        },
        {
            'name': 'Cloning Chamber', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_TekCloningChamber.PrimalItemStructure_TekCloningChamber\'"',
            'description': 'Enables you to generate clones of your creatures!',
            'url': 'https://ark.fandom.com/wiki/Cloning_Chamber', 'id': 537,
            'class_name': 'PrimalItemStructure_TekCloningChamber_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Cloning_Chamber.png'
        },
        {
            'name': 'Cryofridge', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_CryoFridge.PrimalItemStructure_CryoFridge\'"',
            'description': 'Requires electricity to run. Keeps Cryopods alive forever!',
            'url': 'https://ark.fandom.com/wiki/Cryofridge_(Extinction)', 'id': 538,
            'class_name': 'PrimalItemStructure_CryoFridge_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Cryofridge.png'
        },
        {
            'name': 'Crystal Wyvern Queen Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Mods/CrystalIsles/Assets/Dinos/CIBoss/Trophy/PrimalItemStructure_Flag_CIBoss.PrimalItemStructure_Flag_CIBoss\'"',
            'description': 'This flag is proof that you have defeated the Crystal Wyvern Queen.',
            'url': 'https://ark.fandom.com/wiki/Crystal_Wyvern_Queen_Flag_(Crystal_Isles)', 'id': 539,
            'class_name': 'PrimalItemStructure_Flag_CIBoss_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9c/Crystal_Wyvern_Queen_Flag_%28Crystal_Isles%29.png'
        },
        {
            'name': 'Delivery Crate', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/Structures/ItemBalloon/PrimalItemStructure_StorageBox_Balloon.PrimalItemStructure_StorageBox_Balloon\'"',
            'description': 'A box with a Gasbag attached that can be used to deliver items to another location.',
            'url': 'https://ark.fandom.com/wiki/Delivery_Crate_(Extinction)', 'id': 540,
            'class_name': 'PrimalItemStructure_StorageBox_Balloon_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/85/Delivery_Crate_%28Extinction%29.png'
        },
        {
            'name': 'Dino Leash', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/Structures/DinoLeash/PrimalItemStructure_DinoLeash.PrimalItemStructure_DinoLeash\'"',
            'description': 'Electronic leash to keep your dinos from wandering too far.',
            'url': 'https://ark.fandom.com/wiki/Dino_Leash_(Extinction)', 'id': 541,
            'class_name': 'PrimalItemStructure_DinoLeash_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Dino_Leash_%28Extinction%29.png'
        },
        {
            'name': 'Dragon Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Dragon.PrimalItemStructure_Flag_Dragon\'"',
            'description': 'This flag is proof that you have defeated the Dragon.',
            'url': 'https://ark.fandom.com/wiki/Dragon_Flag', 'id': 542,
            'class_name': 'PrimalItemStructure_Flag_Dragon_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/33/Dragon_Flag.png'
        },
        {
            'name': 'Elevator Track', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorTrackBase.PrimalItemStructure_ElevatorTrackBase\'"',
            'description': 'Attach an Elevator Platform to these to complete an elevator!',
            'url': 'https://ark.fandom.com/wiki/Elevator_Track', 'id': 543,
            'class_name': 'PrimalItemStructure_ElevatorTrackBase_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Elevator_Track.png'
        },
        {
            'name': 'Fish Basket', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_FishBasket.PrimalItemStructure_FishBasket\'"',
            'description': 'Trap certain fish in this basket to tame and transport them!',
            'url': 'https://ark.fandom.com/wiki/Fish_Basket_(Aberration)', 'id': 544,
            'class_name': 'PrimalItemStructure_FishBasket_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/68/Fish_Basket_%28Aberration%29.png'
        },
        {
            'name': 'Gas Collector', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/GasCollector/PrimalItemStructure_GasCollector.PrimalItemStructure_GasCollector\'"',
            'description': 'Place on a Gas Vent to extract Congealed Gas Balls over time.',
            'url': 'https://ark.fandom.com/wiki/Gas_Collector_(Aberration)', 'id': 545,
            'class_name': 'PrimalItemStructure_GasCollector_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Gas_Collector_%28Aberration%29.png'
        },
        {
            'name': 'Giant Adobe Hatchframe', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeilingWithDoorWay_Giant.PrimalItemStructure_AdobeCeilingWithDoorWay_Giant\'"',
            'description': 'This Giant Adobe concrete ceiling has a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Giant_Adobe_Hatchframe_(Scorched_Earth)', 'id': 546,
            'class_name': 'PrimalItemStructure_AdobeCeilingWithDoorWay_Giant_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Giant_Adobe_Hatchframe_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Giant Adobe Trapdoor', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeCeilingDoorGiant.PrimalItemStructure_AdobeCeilingDoorGiant\'"',
            'description': 'A large adobe gate that can be used with a Gateway to most keep dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Giant_Adobe_Trapdoor_(Scorched_Earth)', 'id': 547,
            'class_name': 'PrimalItemStructure_AdobeCeilingDoorGiant_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Giant_Adobe_Trapdoor_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Giant Metal Hatchframe', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalCeilingWithTrapdoorGiant.PrimalItemStructure_MetalCeilingWithTrapdoorGiant\'"',
            'description': 'This metal-plated concrete ceiling has a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Giant_Metal_Hatchframe', 'id': 548,
            'class_name': 'PrimalItemStructure_MetalCeilingWithTrapdoorGiant_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Metal_Hatchframe.png'
        },
        {
            'name': 'Giant Metal Trapdoor', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalTrapdoorGiant.PrimalItemStructure_MetalTrapdoorGiant\'"',
            'description': 'This metal-plated concrete slab can be used to secure hatches.',
            'url': 'https://ark.fandom.com/wiki/Giant_Metal_Trapdoor', 'id': 549,
            'class_name': 'PrimalItemStructure_MetalTrapdoorGiant_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/Metal_Trapdoor.png'
        },
        {
            'name': 'Giant Reinforced Trapdoor', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeilingDoorGiant.PrimalItemStructure_StoneCeilingDoorGiant\'"',
            'description': 'This small reinforced door can be used to secure hatches.',
            'url': 'https://ark.fandom.com/wiki/Giant_Reinforced_Trapdoor', 'id': 550,
            'class_name': 'PrimalItemStructure_StoneCeilingDoorGiant_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Reinforced_Trapdoor.png'
        },
        {
            'name': 'Giant Stone Hatchframe', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneCeilingWithTrapdoorGiant.PrimalItemStructure_StoneCeilingWithTrapdoorGiant\'"',
            'description': 'This brick-and-mortar ceiling has a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Giant_Stone_Hatchframe', 'id': 551,
            'class_name': 'PrimalItemStructure_StoneCeilingWithTrapdoorGiant_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Stone_Hatchframe.png'
        },
        {
            'name': 'Gorilla Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Flag_Gorilla.PrimalItemStructure_Flag_Gorilla\'"',
            'description': 'This flag is proof that you have defeated the Megapithecus.',
            'url': 'https://ark.fandom.com/wiki/Gorilla_Flag', 'id': 552,
            'class_name': 'PrimalItemStructure_Flag_Gorilla_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9f/Gorilla_Flag.png'
        },
        {
            'name': 'Gravestone', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_Gravestone.PrimalItemStructure_Furniture_Gravestone\'"',
            'description': 'A simple unadorned stone headstone to mark a grave or commemorate a loved one.',
            'url': 'https://ark.fandom.com/wiki/Gravestone', 'id': 553,
            'class_name': 'PrimalItemStructure_Furniture_Gravestone_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Gravestone.png'
        },
        {
            'name': 'Heavy Auto Turret', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_HeavyTurret.PrimalItemStructure_HeavyTurret\'"',
            'description': 'Requires electricity to run. Provides increased firepower, but consumes FOUR bullets while firing. Can be configured to automatically attack hostiles within range.',
            'url': 'https://ark.fandom.com/wiki/Heavy_Auto_Turret', 'id': 554,
            'class_name': 'PrimalItemStructure_HeavyTurret_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7f/Heavy_Auto_Turret.png'
        },
        {
            'name': 'Homing Underwater Mine', 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_SeaMine.PrimalItemStructure_SeaMine\'"',
            'description': 'Place this underwater to create an explosive trap that floats, homes, explodes when touched.',
            'url': 'https://ark.fandom.com/wiki/Homing_Underwater_Mine', 'id': 555,
            'class_name': 'PrimalItemStructure_SeaMine_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Homing_Underwater_Mine.png'
        },
        {
            'name': 'Industrial Cooker', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_IndustrialCookingPot.PrimalItemStructure_IndustrialCookingPot\'"',
            'description': 'Burns Gasoline to cook large quantities of food quickly. Put various ingredients in this to make soups, stews, and dyes.',
            'url': 'https://ark.fandom.com/wiki/Industrial_Cooker', 'id': 556,
            'class_name': 'PrimalItemStructure_IndustrialCookingPot_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/91/Industrial_Cooker.png'
        },
        {
            'name': 'Industrial Forge', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_IndustrialForge.PrimalItemStructure_IndustrialForge\'"',
            'description': None, 'url': 'https://ark.fandom.com/wiki/Industrial_Forge', 'id': 557,
            'class_name': 'PrimalItemStructure_IndustrialForge_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c5/Industrial_Forge.png'
        },
        {
            'name': 'Industrial Grinder', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Grinder.PrimalItemStructure_Grinder\'"',
            'description': 'Grind up crafted items and certain resources!',
            'url': 'https://ark.fandom.com/wiki/Industrial_Grinder', 'id': 558,
            'class_name': 'PrimalItemStructure_Grinder_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Industrial_Grinder.png'
        },
        {
            'name': 'King Titan Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Trophies/PrimalItemStructure_Flag_KingKaiju.PrimalItemStructure_Flag_KingKaiju\'"',
            'description': 'This flag is proof that you have defeated the King of the Titans.',
            'url': 'https://ark.fandom.com/wiki/King_Titan_Flag_(Extinction)', 'id': 559,
            'class_name': 'PrimalItemStructure_Flag_KingKaiju_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/King_Titan_Flag_%28Extinction%29.png'
        },
        {
            'name': 'King Titan Flag (Mecha)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Trophies/PrimalItemStructure_Flag_KingKaijuMecha.PrimalItemStructure_Flag_KingKaijuMecha\'"',
            'description': 'This flag is proof that you have defeated the King of the Titans.',
            'url': 'https://ark.fandom.com/wiki/King_Titan_Flag_(Mecha)_(Extinction)', 'id': 560,
            'class_name': 'PrimalItemStructure_Flag_KingKaijuMecha_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/79/King_Titan_Flag_%28Mecha%29_%28Extinction%29.png'
        },
        {
            'name': 'Large Elevator Platform', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorPlatformLarge.PrimalItemStructure_ElevatorPlatformLarge\'"',
            'description': 'Attach to an Elevator Track to carry a large amount of weight.',
            'url': 'https://ark.fandom.com/wiki/Large_Elevator_Platform', 'id': 561,
            'class_name': 'PrimalItemStructure_ElevatorPlatformLarge_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Large_Elevator_Platform.png'
        },
        {
            'name': 'Large Taxidermy Base', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_TaxidermyBase_Large.PrimalItemStructure_TaxidermyBase_Large\'"',
            'description': 'Place a harvested dermis to show off your prowess!',
            'url': 'https://ark.fandom.com/wiki/Large_Taxidermy_Base_(Extinction)', 'id': 562,
            'class_name': 'PrimalItemStructure_TaxidermyBase_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/ff/Large_Taxidermy_Base_%28Extinction%29.png'
        },
        {
            'name': 'Large Wood Elevator Platform', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorPlatform_Large.PrimalItemStructure_WoodElevatorPlatform_Large\'"',
            'description': 'Attach to an Elevator Track to lift a large amount of weight.',
            'url': 'https://ark.fandom.com/wiki/Large_Wood_Elevator_Platform_(Aberration)', 'id': 563,
            'class_name': 'PrimalItemStructure_WoodElevatorPlatform_Large_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b7/Large_Wood_Elevator_Platform_%28Aberration%29.png'
        },
        {
            'name': 'Manticore Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/ManticoreFlag/PrimalItemStructure_Flag_Manticore.PrimalItemStructure_Flag_Manticore\'"',
            'description': 'This flag is proof that you have defeated the Manticore.',
            'url': 'https://ark.fandom.com/wiki/Manticore_Flag_(Scorched_Earth)', 'id': 564,
            'class_name': 'PrimalItemStructure_Flag_Manticore_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e0/Manticore_Flag_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Medium Elevator Platform', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorPlatfromMedium.PrimalItemStructure_ElevatorPlatfromMedium\'"',
            'description': 'Attach to an Elevator Track to carry a medium amount of weight.',
            'url': 'https://ark.fandom.com/wiki/Medium_Elevator_Platform', 'id': 565,
            'class_name': 'PrimalItemStructure_ElevatorPlatfromMedium_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/80/Medium_Elevator_Platform.png'
        },
        {
            'name': 'Medium Taxidermy Base', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_TaxidermyBase_Medium.PrimalItemStructure_TaxidermyBase_Medium\'"',
            'description': 'Place a harvested dermis to show off your prowess!',
            'url': 'https://ark.fandom.com/wiki/Medium_Taxidermy_Base_(Extinction)', 'id': 566,
            'class_name': 'PrimalItemStructure_TaxidermyBase_Medium_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Medium_Taxidermy_Base_%28Extinction%29.png'
        },
        {
            'name': 'Medium Wood Elevator Platform', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorPlatform_Medium.PrimalItemStructure_WoodElevatorPlatform_Medium\'"',
            'description': 'Attach to an Elevator Track to lift a medium amount of weight.',
            'url': 'https://ark.fandom.com/wiki/Medium_Wood_Elevator_Platform_(Aberration)', 'id': 567,
            'class_name': 'PrimalItemStructure_WoodElevatorPlatform_Medium_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5b/Medium_Wood_Elevator_Platform_%28Aberration%29.png'
        },
        {
            'name': 'Metal Cliff Platform', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/CliffPlatforms/Metal_CliffPlatform/PrimalItemStructure_Metal_CliffPlatform.PrimalItemStructure_Metal_CliffPlatform\'"',
            'description': 'A Cliff Platform is required to build structures extending from a cliff. This one is made from shiny metal.',
            'url': 'https://ark.fandom.com/wiki/Metal_Cliff_Platform_(Aberration)', 'id': 568,
            'class_name': 'PrimalItemStructure_Metal_CliffPlatform_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Metal_Cliff_Platform_%28Aberration%29.png'
        },
        {
            'name': 'Metal Ocean Platform', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/Genesis/Structures/OceanPlatform/OceanPlatform_Wood/PrimalItemStructure_Metal_OceanPlatform.PrimalItemStructure_Metal_OceanPlatform\'"',
            'description': 'Floats on the surface of bodies of water.',
            'url': 'https://ark.fandom.com/wiki/Metal_Ocean_Platform_(Genesis:_Part_1)', 'id': 569,
            'class_name': 'PrimalItemStructure_Metal_OceanPlatform_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Metal_Ocean_Platform_%28Genesis_Part_1%29.png'
        },
        {
            'name': 'Metal Railing', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalRailing.PrimalItemStructure_MetalRailing\'"',
            'description': 'A metal-plated concrete railing that acts as a simple barrier to prevent people from falling.',
            'url': 'https://ark.fandom.com/wiki/Metal_Railing', 'id': 570,
            'class_name': 'PrimalItemStructure_MetalRailing_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/85/Metal_Railing.png'
        },
        {
            'name': 'Metal Staircase', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Metal/PrimalItemStructure_MetalStairs.PrimalItemStructure_MetalStairs\'"',
            'description': 'A metal spiral staircase, useful in constructing multi-level buildings.',
            'url': 'https://ark.fandom.com/wiki/Metal_Staircase', 'id': 571,
            'class_name': 'PrimalItemStructure_MetalStairs_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Metal_Staircase.png'
        },
        {
            'name': 'Metal Tree Platform', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_TreePlatform_Metal.PrimalItemStructure_TreePlatform_Metal\'"',
            'description': 'Attaches to a large tree, enabling you to build on it.',
            'url': 'https://ark.fandom.com/wiki/Metal_Tree_Platform', 'id': 572,
            'class_name': 'PrimalItemStructure_TreePlatform_Metal_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cc/Metal_Tree_Platform.png'
        },
        {
            'name': 'Minigun Turret', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretMinigun.PrimalItemStructure_TurretMinigun\'"',
            'description': 'Mount this to fire a hail of Advanced Rifle Bullets at your enemies. Powered by the rider.',
            'url': 'https://ark.fandom.com/wiki/Minigun_Turret', 'id': 573,
            'class_name': 'PrimalItemStructure_TurretMinigun_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b6/Minigun_Turret.png'
        },
        {
            'name': 'Mirror', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/DesertFurnitureSet/Mirror/PrimalItemStructure_Mirror.PrimalItemStructure_Mirror\'"',
            'description': 'Put it on a wall, and look at your beautiful self!',
            'url': 'https://ark.fandom.com/wiki/Mirror_(Scorched_Earth)', 'id': 574,
            'class_name': 'PrimalItemStructure_Mirror_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4d/Mirror_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Moeder Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Genesis/CoreBlueprints/Structures/PrimalItemStructure_Flag_EelBoss.PrimalItemStructure_Flag_EelBoss\'"',
            'description': 'This flag is proof that you have defeated Moeder.',
            'url': 'https://ark.fandom.com/wiki/Moeder_Flag_(Genesis:_Part_1)', 'id': 575,
            'class_name': 'PrimalItemStructure_Flag_EelBoss_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b6/Moeder_Flag_%28Genesis_Part_1%29.png'
        },
        {
            'name': 'Motorboat', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Items/Raft/PrimalItemMotorboat.PrimalItemMotorboat\'"',
            'description': 'A floating metal platform that you can pilot across the water, requires gasoline to power its motor. Can support the weight of structures and be built on.',
            'url': 'https://ark.fandom.com/wiki/Motorboat', 'id': 576, 'class_name': 'PrimalItemMotorboat_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Motorboat.png'
        },
        {
            'name': 'Oil Pump', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/OilPump/PrimalItemStructure_oilPump.PrimalItemStructure_oilPump\'"',
            'description': 'Extracts Oil from an Oil zone',
            'url': 'https://ark.fandom.com/wiki/Oil_Pump_(Scorched_Earth)', 'id': 577,
            'class_name': 'PrimalItemStructure_oilPump_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7d/Oil_Pump_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Plant Species Y Trap', 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/WeaponPlantSpeciesY/PrimalItemStructure_PlantSpeciesYTrap.PrimalItemStructure_PlantSpeciesYTrap\'"',
            'description': 'Immobilizes humans and small creatures.',
            'url': 'https://ark.fandom.com/wiki/Plant_Species_Y_Trap_(Scorched_Earth)', 'id': 578,
            'class_name': 'PrimalItemStructure_PlantSpeciesYTrap_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cb/Plant_Species_Y_Trap_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Portable Rope Ladder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/PortableRopeLadder/PrimalItemStructure_PortableLadder.PrimalItemStructure_PortableLadder\'"',
            'description': 'A simple rope ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
            'url': 'https://ark.fandom.com/wiki/Portable_Rope_Ladder_(Aberration)', 'id': 579,
            'class_name': 'PrimalItemStructure_PortableLadder_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Rope_Ladder.png'
        },
        {
            'name': 'Pressure Plate', 'stack_size': 5,
            'blueprint': '"Blueprint\'/Game/Genesis/Structures/TekAlarm/PrimalItemStructure_PressurePlate.PrimalItemStructure_PressurePlate\'"',
            'description': 'A mechanical trigger that activates nearby devices and structures when stepped on.',
            'url': 'https://ark.fandom.com/wiki/Pressure_Plate_(Genesis:_Part_1)', 'id': 580,
            'class_name': 'PrimalItemStructure_PressurePlate_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a2/Pressure_Plate_%28Genesis_Part_1%29.png'
        },
        {
            'name': 'Rocket Turret', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretRocket.PrimalItemStructure_TurretRocket\'"',
            'description': 'Mount this to fire Rockets at your enemies. Powered by the rider.',
            'url': 'https://ark.fandom.com/wiki/Rocket_Turret', 'id': 581,
            'class_name': 'PrimalItemStructure_TurretRocket_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/56/Rocket_Turret.png'
        },
        {
            'name': 'Rockwell Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Trophies/PrimalItemStructure_Flag_Rockwell.PrimalItemStructure_Flag_Rockwell\'"',
            'description': 'This flag is proof that you have defeated Rockwell.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Flag_(Aberration)', 'id': 582,
            'class_name': 'PrimalItemStructure_Flag_Rockwell_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/83/Rockwell_Flag_%28Aberration%29.png'
        },
        {
            'name': 'Rope Ladder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_RopeLadder.PrimalItemStructure_RopeLadder\'"',
            'description': 'A simple rope ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
            'url': 'https://ark.fandom.com/wiki/Rope_Ladder', 'id': 583,
            'class_name': 'PrimalItemStructure_RopeLadder_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Rope_Ladder.png'
        },
        {
            'name': 'Shag Rug', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Structures/PrimalItemStructure_Furniture_Rug.PrimalItemStructure_Furniture_Rug\'"',
            'description': 'A decorative, paintable rug with a shaggy appearance, which dulls the sound of footsteps.',
            'url': 'https://ark.fandom.com/wiki/Shag_Rug_(Aberration)', 'id': 584,
            'class_name': 'PrimalItemStructure_Furniture_Rug_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Shag_Rug_%28Aberration%29.png'
        },
        {
            'name': 'Sloped Adobe Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeRoof.PrimalItemStructure_AdobeRoof\'"',
            'description': 'An inclined adobe-framed roof. Slightly different angle than the ramp. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Adobe_Roof_(Scorched_Earth)', 'id': 585,
            'class_name': 'PrimalItemStructure_AdobeRoof_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dd/Sloped_Adobe_Roof_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Sloped Adobe Wall Left', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWall_Sloped_Left.PrimalItemStructure_AdobeWall_Sloped_Left\'"',
            'description': 'A sturdy adobe-framed, sloped wall that insulates the inside from the outside, seprarates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Adobe_Wall_Left_(Scorched_Earth)', 'id': 586,
            'class_name': 'PrimalItemStructure_AdobeWall_Sloped_Left_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/ff/Sloped_Adobe_Wall_Left_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Sloped Adobe Wall Right', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Adobe/Blueprints/PrimalItemStructure_AdobeWall_Sloped_Right.PrimalItemStructure_AdobeWall_Sloped_Right\'"',
            'description': 'A sturdy adobe-framed, sloped wall that insulates the inside from the outside, seprarates rooms, and provides structural integrity. Used in conjunction with the roof. Excellent for growing crops indoors.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Adobe_Wall_Right_(Scorched_Earth)', 'id': 587,
            'class_name': 'PrimalItemStructure_AdobeWall_Sloped_Right_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2f/Sloped_Adobe_Wall_Right_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Sloped Tek Roof', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekRoof.PrimalItemStructure_TekRoof\'"',
            'description': 'An inclined tek roof. Slightly different angle than the ramp.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Tek_Roof', 'id': 588,
            'class_name': 'PrimalItemStructure_TekRoof_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6a/Sloped_Tek_Roof.png'
        },
        {
            'name': 'Sloped Tek Wall Left', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWall_Sloped_Left.PrimalItemStructure_TekWall_Sloped_Left\'"',
            'description': 'A composite Tek wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Tek_Wall_Left', 'id': 589,
            'class_name': 'PrimalItemStructure_TekWall_Sloped_Left_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png'
        },
        {
            'name': 'Sloped Tek Wall Right', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWall_Sloped_Right.PrimalItemStructure_TekWall_Sloped_Right\'"',
            'description': 'A composite Tek wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Sloped_Tek_Wall_Right', 'id': 590,
            'class_name': 'PrimalItemStructure_TekWall_Sloped_Right_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png'
        },
        {
            'name': 'Small Elevator Platform', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_ElevatorPlatformSmall.PrimalItemStructure_ElevatorPlatformSmall\'"',
            'description': 'Attach to an Elevator Track to carry a small amount of weight.',
            'url': 'https://ark.fandom.com/wiki/Small_Elevator_Platform', 'id': 591,
            'class_name': 'PrimalItemStructure_ElevatorPlatformSmall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Small_Elevator_Platform.png'
        },
        {
            'name': 'Small Taxidermy Base', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItemStructure_TaxidermyBase_Small.PrimalItemStructure_TaxidermyBase_Small\'"',
            'description': 'Place a harvested dermis to show off your prowess!',
            'url': 'https://ark.fandom.com/wiki/Small_Taxidermy_Base_(Extinction)', 'id': 592,
            'class_name': 'PrimalItemStructure_TaxidermyBase_Small_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Small_Taxidermy_Base_%28Extinction%29.png'
        },
        {
            'name': 'Small Wood Elevator Platform', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorPlatform_Small.PrimalItemStructure_WoodElevatorPlatform_Small\'"',
            'description': 'Attach to an Elevator Track to lift a small amount of weight.',
            'url': 'https://ark.fandom.com/wiki/Small_Wood_Elevator_Platform_(Aberration)', 'id': 593,
            'class_name': 'PrimalItemStructure_WoodElevatorPlatform_Small_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Small_Wood_Elevator_Platform_%28Aberration%29.png'
        },
        {
            'name': 'Stone Cliff Platform', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/CliffPlatforms/Stone_CliffPlatform/PrimalItemStructure_Stone_CliffPlatform.PrimalItemStructure_Stone_CliffPlatform\'"',
            'description': 'A Cliff Platform is required to build structures extending from a cliff. This one is made from heavy stone.',
            'url': 'https://ark.fandom.com/wiki/Stone_Cliff_Platform_(Aberration)', 'id': 594,
            'class_name': 'PrimalItemStructure_Stone_CliffPlatform_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Stone_Cliff_Platform_%28Aberration%29.png'
        },
        {
            'name': 'Stone Fireplace', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Fireplace.PrimalItemStructure_Fireplace\'"',
            'description': 'A nice, relaxing fireplace. Keeps a large area very warm and provides light.',
            'url': 'https://ark.fandom.com/wiki/Stone_Fireplace', 'id': 595,
            'class_name': 'PrimalItemStructure_Fireplace_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c2/Stone_Fireplace.png'
        },
        {
            'name': 'Stone Railing', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneRailing.PrimalItemStructure_StoneRailing\'"',
            'description': 'A brick-and-mortar railing that acts as a simple barrier to prevent people from falling.',
            'url': 'https://ark.fandom.com/wiki/Stone_Railing', 'id': 596,
            'class_name': 'PrimalItemStructure_StoneRailing_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1b/Stone_Railing.png'
        },
        {
            'name': 'Stone Staircase', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Stone/PrimalItemStructure_StoneStairs.PrimalItemStructure_StoneStairs\'"',
            'description': 'A stone spiral staircase, useful in constructing multi-level buildings.',
            'url': 'https://ark.fandom.com/wiki/Stone_Staircase', 'id': 597,
            'class_name': 'PrimalItemStructure_StoneStairs_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/09/Stone_Staircase.png'
        },
        {
            'name': 'Tek Bridge', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/Structures/TekBridge/PrimalItemStructure_TekBridge.PrimalItemStructure_TekBridge\'"',
            'description': 'Extendable force bridge', 'url': 'https://ark.fandom.com/wiki/Tek_Bridge_(Extinction)',
            'id': 598, 'class_name': 'PrimalItemStructure_TekBridge_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3b/Tek_Bridge_%28Extinction%29.png'
        },
        {
            'name': 'Tek Catwalk', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekCatwalk.PrimalItemStructure_TekCatwalk\'"',
            'description': 'A thin walkway for bridging areas together. Made from advanced Tek materials.',
            'url': 'https://ark.fandom.com/wiki/Tek_Catwalk', 'id': 599,
            'class_name': 'PrimalItemStructure_TekCatwalk_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/Tek_Catwalk.png'
        },
        {
            'name': 'Tek Ceiling', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekCeiling.PrimalItemStructure_TekCeiling\'"',
            'description': 'An incredibly durable composite Tek ceiling that provides insulation, and doubles as a floor for higher levels.',
            'url': 'https://ark.fandom.com/wiki/Tek_Ceiling', 'id': 600,
            'class_name': 'PrimalItemStructure_TekCeiling_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Tek_Ceiling.png'
        },
        {
            'name': 'Tek Dinosaur Gateway', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGateframe.PrimalItemStructure_TekGateframe\'"',
            'description': 'A large composite Tek gate that can be used with a Gateway to keep most dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Tek_Dinosaur_Gateway', 'id': 601,
            'class_name': 'PrimalItemStructure_TekGateframe_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Tek_Dinosaur_Gate.png'
        },
        {
            'name': 'Tek Dinosaur Gate', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekGate.PrimalItemStructure_TekGate\'"',
            'description': 'A large composite Tek gate that can be used with a Gateway to keep most dinosaurs in or out.',
            'url': 'https://ark.fandom.com/wiki/Tek_Dinosaur_Gate', 'id': 602,
            'class_name': 'PrimalItemStructure_TekGate_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Tek_Dinosaur_Gate.png'
        },
        {
            'name': 'Tek Doorframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWallWithDoor.PrimalItemStructure_TekWallWithDoor\'"',
            'description': 'A stable composite Tek door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Tek_Doorframe', 'id': 603,
            'class_name': 'PrimalItemStructure_TekWallWithDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/36/Tek_Door.png'
        },
        {
            'name': 'Tek Door', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekDoor.PrimalItemStructure_TekDoor\'"',
            'description': 'A stable composite Tek door that provides entrance to structures. Can be locked for security.',
            'url': 'https://ark.fandom.com/wiki/Tek_Door', 'id': 604, 'class_name': 'PrimalItemStructure_TekDoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/36/Tek_Door.png'
        },
        {
            'name': 'Tek Fence Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekFenceFoundation.PrimalItemStructure_TekFenceFoundation\'"',
            'description': 'This composite Tek foundation is used to build walls around an area.',
            'url': 'https://ark.fandom.com/wiki/Tek_Fence_Foundation', 'id': 605,
            'class_name': 'PrimalItemStructure_TekFenceFoundation_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Tek_Fence_Foundation.png'
        },
        {
            'name': 'Tek Forcefield', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekShield.PrimalItemStructure_TekShield\'"',
            'description': 'Generates an impenetrable, expandable spherical shield to keep out enemies. Requires Element to run, and Tek Engram to use.',
            'url': 'https://ark.fandom.com/wiki/Tek_Forcefield', 'id': 606,
            'class_name': 'PrimalItemStructure_TekShield_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5a/Tek_Forcefield.png'
        },
        {
            'name': 'Tek Foundation', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekFloor.PrimalItemStructure_TekFloor\'"',
            'description': 'A foundation is required to build structures in an area. This is made from sturdy composite Tek materials.',
            'url': 'https://ark.fandom.com/wiki/Tek_Foundation', 'id': 607,
            'class_name': 'PrimalItemStructure_TekFloor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8c/Tek_Foundation.png'
        },
        {
            'name': 'Tek Generator', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekGenerator.PrimalItemStructure_TekGenerator\'"',
            'description': 'Powers Tek Structures and electrical structures wirelessly! Requires Element to run, and Tek Engram to use.',
            'url': 'https://ark.fandom.com/wiki/Tek_Generator', 'id': 608,
            'class_name': 'PrimalItemStructure_TekGenerator_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Tek_Generator.png'
        },
        {
            'name': 'Tek Hatchframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekCeilingWithTrapdoor.PrimalItemStructure_TekCeilingWithTrapdoor\'"',
            'description': 'This composite Tek ceiling has a hole in it for trapdoors.',
            'url': 'https://ark.fandom.com/wiki/Tek_Hatchframe', 'id': 609,
            'class_name': 'PrimalItemStructure_TekCeilingWithTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Tek_Hatchframe.png'
        },
        {
            'name': 'Tek Jump Pad', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Structures/TekJumpPad/PrimalItemStructure_TekJumpPad.PrimalItemStructure_TekJumpPad\'"',
            'description': 'A Tek-powered propulsion device; useful for traversal and mayhem.',
            'url': 'https://ark.fandom.com/wiki/Tek_Jump_Pad_(Genesis:_Part_1)', 'id': 610,
            'class_name': 'PrimalItemStructure_TekJumpPad_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Tek_Jump_Pad_%28Genesis_Part_1%29.png'
        },
        {
            'name': 'Tek Ladder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekLadder.PrimalItemStructure_TekLadder\'"',
            'description': 'A composite Tek ladder used to climb up or down tall structures. Can also be used to extend existing ladders.',
            'url': 'https://ark.fandom.com/wiki/Tek_Ladder', 'id': 611, 'class_name': 'PrimalItemStructure_TekLadder_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Tek_Ladder.png'
        },
        {
            'name': 'Tek Light', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekLight.PrimalItemStructure_TekLight\'"',
            'description': 'Useful for spelunking, they can be attached to any surface, self powered by Element Shards , or linked to generators, and picked-up after placement.',
            'url': 'https://ark.fandom.com/wiki/Tek_Light', 'id': 612, 'class_name': 'PrimalItemStructure_TekLight_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Tek_Light_%28Ragnarok%29.png'
        },
        {
            'name': 'Tek Pillar', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekPillar.PrimalItemStructure_TekPillar\'"',
            'description': 'This composite Tek pillar adds structural integrity to the area it is build under. Can also act as stilts for buildings on inclines.',
            'url': 'https://ark.fandom.com/wiki/Tek_Pillar', 'id': 613, 'class_name': 'PrimalItemStructure_TekPillar_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/eb/Tek_Pillar.png'
        },
        {
            'name': 'Tek Railing', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekRailing.PrimalItemStructure_TekRailing\'"',
            'description': 'A composite Tek railing that acts as a simple barrier to prevent people from falling.',
            'url': 'https://ark.fandom.com/wiki/Tek_Railing', 'id': 614,
            'class_name': 'PrimalItemStructure_TekRailing_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0f/Tek_Railing.png'
        },
        {
            'name': 'Tek Ramp', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekRamp.PrimalItemStructure_TekRamp\'"',
            'description': 'An inclined composite Tek floor for travelling up or down levels. Can also be used to make an angled roof.',
            'url': 'https://ark.fandom.com/wiki/Tek_Ramp', 'id': 615, 'class_name': 'PrimalItemStructure_TekRamp_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1a/Tek_Ramp.png'
        },
        {
            'name': 'Tek Replicator', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekReplicator.PrimalItemStructure_TekReplicator\'"',
            'description': 'Replicate items here. Requires Element to be activated.',
            'url': 'https://ark.fandom.com/wiki/Tek_Replicator', 'id': 616,
            'class_name': 'PrimalItemStructure_TekReplicator_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a2/Tek_Replicator.png'
        },
        {
            'name': 'Tek Sensor', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Structures/TekAlarm/PrimalItemStructure_TekAlarm.PrimalItemStructure_TekAlarm\'"',
            'description': 'An advanced detection and activation system used to automate nearby devices and structures. Requires Tek Generator power.',
            'url': 'https://ark.fandom.com/wiki/Tek_Sensor_(Genesis:_Part_1)', 'id': 617,
            'class_name': 'PrimalItemStructure_TekAlarm_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/16/Tek_Sensor_%28Genesis_Part_1%29.png'
        },
        {
            'name': 'Tek Sleeping Pod', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Bed_Tek.PrimalItemStructure_Bed_Tek\'"',
            'description': 'This Tek-powered Chamber lets you rapidly recover vitals, and slowly gain XP even when sleeping. You can also sleep soundly within it, protected even while on a moving platform!',
            'url': 'https://ark.fandom.com/wiki/Tek_Sleeping_Pod_(Aberration)', 'id': 618,
            'class_name': 'PrimalItemStructure_Bed_Tek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Tek_Sleeping_Pod_%28Aberration%29.png'
        },
        {
            'name': 'Tek Staircase', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekStairs.PrimalItemStructure_TekStairs\'"',
            'description': 'A composite Tek spiral staircase, useful in constructing multi-level buildings.',
            'url': 'https://ark.fandom.com/wiki/Tek_Staircase', 'id': 619,
            'class_name': 'PrimalItemStructure_TekStairs_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Tek_Staircase.png'
        },
        {
            'name': 'Tek Teleporter', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekTeleporter.PrimalItemStructure_TekTeleporter\'"',
            'description': 'Allows instantaneous traversal between Teleporters! Requires Tek Generator to power, and Element & Tek Engram to use.',
            'url': 'https://ark.fandom.com/wiki/Tek_Teleporter', 'id': 620,
            'class_name': 'PrimalItemStructure_TekTeleporter_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/64/Tek_Teleporter.png'
        },
        {
            'name': 'Tek Transmitter', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekTransmitter.PrimalItemStructure_TekTransmitter\'"',
            'description': 'Transmits items, Survivors, and creatures to other ARKs! Requires Tek Engram to use.',
            'url': 'https://ark.fandom.com/wiki/Tek_Transmitter', 'id': 621,
            'class_name': 'PrimalItemStructure_TekTransmitter_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Tek_Transmitter.png'
        },
        {
            'name': 'Tek Trapdoor', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekTrapdoor.PrimalItemStructure_TekTrapdoor\'"',
            'description': 'This composite Tek slab can be used to secure hatches.',
            'url': 'https://ark.fandom.com/wiki/Tek_Trapdoor', 'id': 622,
            'class_name': 'PrimalItemStructure_TekTrapdoor_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Tek_Trapdoor.png'
        },
        {
            'name': 'Tek Trough', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TekTrough.PrimalItemStructure_TekTrough\'"',
            'description': "Put food for your nearby pets in this, and they'll automatically eat it when hungry! Can refridgerate items, so long as it's powered by a Tek Generator!",
            'url': 'https://ark.fandom.com/wiki/Tek_Trough', 'id': 623, 'class_name': 'PrimalItemStructure_TekTrough_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/Tek_Trough.png'
        },
        {
            'name': 'Tek Turret', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretTek.PrimalItemStructure_TurretTek\'"',
            'description': 'Requires Tek Generator power. Consumes Element Shards while firing. Has a variety of smart-targeting configuration options.',
            'url': 'https://ark.fandom.com/wiki/Tek_Turret', 'id': 624, 'class_name': 'PrimalItemStructure_TurretTek_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Tek_Turret.png'
        },
        {
            'name': 'Tek Wall', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWall.PrimalItemStructure_TekWall\'"',
            'description': 'A composite Tek wall that insulates the inside from the outside and separates rooms.',
            'url': 'https://ark.fandom.com/wiki/Tek_Wall', 'id': 625, 'class_name': 'PrimalItemStructure_TekWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Tek_Wall.png'
        },
        {
            'name': 'Tek Windowframe', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWallWithWindow.PrimalItemStructure_TekWallWithWindow\'"',
            'description': 'Tek plates that cover windows to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Tek_Windowframe', 'id': 626,
            'class_name': 'PrimalItemStructure_TekWallWithWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Tek_Window.png'
        },
        {
            'name': 'Tek Window', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Tek/PrimalItemStructure_TekWindow.PrimalItemStructure_TekWindow\'"',
            'description': 'Tek plates that cover windows to provide protection from projectiles and spying.',
            'url': 'https://ark.fandom.com/wiki/Tek_Window', 'id': 627, 'class_name': 'PrimalItemStructure_TekWindow_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/Tek_Window.png'
        },
        {
            'name': 'Tent', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/Tent/PrimalItemStructure_Tent.PrimalItemStructure_Tent\'"',
            'description': 'A portable Tent where you can take cover in hostile environments',
            'url': 'https://ark.fandom.com/wiki/Tent_(Scorched_Earth)', 'id': 628,
            'class_name': 'PrimalItemStructure_Tent_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d6/Tent_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Toilet', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_Toilet.PrimalItemStructure_Toilet\'"',
            'description': 'Attach to water pipes, and sit on it when you hear the call of nature. Do your business, feel refreshed, and then flush for efficient waste disposal!',
            'url': 'https://ark.fandom.com/wiki/Toilet', 'id': 629, 'class_name': 'PrimalItemStructure_Toilet_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Toilet.png'
        },
        {
            'name': 'Training Dummy', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Halloween/PrimalItemStructure_TrainingDummy.PrimalItemStructure_TrainingDummy\'"',
            'description': 'Attack this training dummy to test your DPS!',
            'url': 'https://ark.fandom.com/wiki/Training_Dummy', 'id': 630,
            'class_name': 'PrimalItemStructure_TrainingDummy_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/49/Training_Dummy.png'
        },
        {
            'name': 'Tree Sap Tap', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Pipes/PrimalItemStructure_TreeTap.PrimalItemStructure_TreeTap\'"',
            'description': 'Attach this to a large tree to tap its sap over time.',
            'url': 'https://ark.fandom.com/wiki/Tree_Sap_Tap', 'id': 631, 'class_name': 'PrimalItemStructure_TreeTap_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Tree_Sap_Tap.png'
        },
        {
            'name': 'Trophy Wall-Mount', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TrophyWall.PrimalItemStructure_TrophyWall\'"',
            'description': 'Provides the wall-mount upon which you can place a trophy!',
            'url': 'https://ark.fandom.com/wiki/Trophy_Wall-Mount', 'id': 632,
            'class_name': 'PrimalItemStructure_TrophyWall_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Trophy_Wall-Mount.png'
        },
        {
            'name': 'Vacuum Compartment Moonpool', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_UnderwaterBase_Moonpool.PrimalItemStructure_UnderwaterBase_Moonpool\'"',
            'description': 'Place underwater, power with Tek Generator, and you can live and breath in it!',
            'url': 'https://ark.fandom.com/wiki/Vacuum_Compartment_Moonpool', 'id': 633,
            'class_name': 'PrimalItemStructure_UnderwaterBase_Moonpool_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Vacuum_Compartment.png'
        },
        {
            'name': 'Vacuum Compartment', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/BuildingBases/PrimalItemStructure_UnderwaterBase.PrimalItemStructure_UnderwaterBase\'"',
            'description': 'Place underwater, power with Tek Generator, and you can live and breath in it!',
            'url': 'https://ark.fandom.com/wiki/Vacuum_Compartment', 'id': 634,
            'class_name': 'PrimalItemStructure_UnderwaterBase_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Vacuum_Compartment.png'
        },
        {
            'name': 'Vessel', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/DesertFurnitureSet/Vessel/PrimalItemStructure_Vessel.PrimalItemStructure_Vessel\'"',
            'description': 'Stores preserving salts and makes them last longer.',
            'url': 'https://ark.fandom.com/wiki/Vessel_(Scorched_Earth)', 'id': 635,
            'class_name': 'PrimalItemStructure_Vessel_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/07/Vessel_%28Scorched_Earth%29.png'
        },
        {
            'name': 'VR Boss Flag', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Genesis/CoreBlueprints/Structures/PrimalItemStructure_Flag_VRBoss.PrimalItemStructure_Flag_VRBoss\'"',
            'description': 'This flag is proof that you have defeated the VR Boss.',
            'url': 'https://ark.fandom.com/wiki/VR_Boss_Flag_(Genesis:_Part_1)', 'id': 636,
            'class_name': 'PrimalItemStructure_Flag_VRBoss_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/23/VR_Boss_Flag_%28Genesis_Part_1%29.png'
        },
        {
            'name': 'Wall Torch', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_WallTorch.PrimalItemStructure_WallTorch\'"',
            'description': 'A torch on a metal connector that lights and warms the immediate area. Must be placed on a wall.',
            'url': 'https://ark.fandom.com/wiki/Wall_Torch', 'id': 637, 'class_name': 'PrimalItemStructure_WallTorch_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Wall_Torch.png'
        },
        {
            'name': 'War Map', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WarMap.PrimalItemStructure_WarMap\'"',
            'description': 'A map of the Island upon which you can draw your plans.',
            'url': 'https://ark.fandom.com/wiki/War_Map', 'id': 638, 'class_name': 'PrimalItemStructure_WarMap_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7a/War_Map.png'
        },
        {
            'name': 'Wardrums', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Wardrums.PrimalItemStructure_Wardrums\'"',
            'description': 'A set of tribal wardrums, to let everyone around hear the power of your tribe.',
            'url': 'https://ark.fandom.com/wiki/Wardrums', 'id': 639, 'class_name': 'PrimalItemStructure_Wardrums_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/db/Wardrums.png'
        },
        {
            'name': 'Water Well', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/WaterWell/PrimalItemStructure_WaterWell.PrimalItemStructure_WaterWell\'"',
            'description': 'This stone tap allows access to the water in an irrigation network. Can refill containers, irrigate crop plots, or provide a refreshing drink.',
            'url': 'https://ark.fandom.com/wiki/Water_Well_(Scorched_Earth)', 'id': 640,
            'class_name': 'PrimalItemStructure_WaterWell_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Water_Well_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Wind Turbine', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Structures/WindTurbine/PrimalItemStructure_WindTurbine.PrimalItemStructure_WindTurbine\'"',
            'description': 'Converts the force of the wind into electricity.',
            'url': 'https://ark.fandom.com/wiki/Wind_Turbine_(Scorched_Earth)', 'id': 641,
            'class_name': 'PrimalItemStructure_WindTurbine_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8c/Wind_Turbine_%28Scorched_Earth%29.png'
        },
        {
            'name': 'Wood Elevator Top Switch', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorTopSwitch.PrimalItemStructure_WoodElevatorTopSwitch\'"',
            'description': 'Attach to the top of a Wood Elevator Track to complete an Elevator!',
            'url': 'https://ark.fandom.com/wiki/Wood_Elevator_Top_Switch_(Aberration)', 'id': 642,
            'class_name': 'PrimalItemStructure_WoodElevatorTopSwitch_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Wood_Elevator_Top_Switch_%28Aberration%29.png'
        },
        {
            'name': 'Wood Elevator Track', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/Structures/PrimitiveElevator/PrimalItemStructure_WoodElevatorTrack.PrimalItemStructure_WoodElevatorTrack\'"',
            'description': 'Attach a Wood Elevator Platform to these to complete an elevator!',
            'url': 'https://ark.fandom.com/wiki/Wood_Elevator_Track_(Aberration)', 'id': 643,
            'class_name': 'PrimalItemStructure_WoodElevatorTrack_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Wood_Elevator_Track_%28Aberration%29.png'
        },
        {
            'name': 'Wood Ocean Platform', 'stack_size': 3,
            'blueprint': '"Blueprint\'/Game/Genesis/Structures/OceanPlatform/OceanPlatform_Wood/PrimalItemStructure_Wood_OceanPlatform.PrimalItemStructure_Wood_OceanPlatform\'"',
            'description': 'Floats on the surface of bodies of water.',
            'url': 'https://ark.fandom.com/wiki/Wood_Ocean_Platform_(Genesis:_Part_1)', 'id': 644,
            'class_name': 'PrimalItemStructure_Wood_OceanPlatform_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Wood_Ocean_Platform_%28Genesis_Part_1%29.png'
        },
        {
            'name': 'Wooden Bench', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_WoodBench.PrimalItemStructure_Furniture_WoodBench\'"',
            'description': 'A simple wooden bench for group sitting.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Bench', 'id': 645,
            'class_name': 'PrimalItemStructure_Furniture_WoodBench_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Wooden_Bench.png'
        },
        {
            'name': 'Wooden Cage', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodCage.PrimalItemStructure_WoodCage\'"',
            'description': 'A portable cage in which to imprison victims.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Cage', 'id': 646, 'class_name': 'PrimalItemStructure_WoodCage_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4b/Wooden_Cage.png'
        },
        {
            'name': 'Wooden Chair', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_WoodChair.PrimalItemStructure_Furniture_WoodChair\'"',
            'description': 'A simple wooden chair for solo sitting.', 'url': 'https://ark.fandom.com/wiki/Wooden_Chair',
            'id': 647, 'class_name': 'PrimalItemStructure_Furniture_WoodChair_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/87/Wooden_Chair.png'
        },
        {
            'name': 'Wooden Railing', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodRailing.PrimalItemStructure_WoodRailing\'"',
            'description': 'A sturdy wooden railing that acts as a simple barrier to prevent people from falling.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Railing', 'id': 648,
            'class_name': 'PrimalItemStructure_WoodRailing_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7b/Wooden_Railing.png'
        },
        {
            'name': 'Wooden Staircase', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_WoodStairs.PrimalItemStructure_WoodStairs\'"',
            'description': 'A wooden spiral staircase, useful in constructing multi-level buildings.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Staircase', 'id': 649,
            'class_name': 'PrimalItemStructure_WoodStairs_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c2/Wooden_Staircase.png'
        },
        {
            'name': 'Wooden Table', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_Furniture_WoodTable.PrimalItemStructure_Furniture_WoodTable\'"',
            'description': 'A simple wooden table with a variety of uses.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Table', 'id': 650,
            'class_name': 'PrimalItemStructure_Furniture_WoodTable_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Wooden_Table.png'
        },
        {
            'name': 'Wooden Tree Platform', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Wooden/PrimalItemStructure_TreePlatform_Wood.PrimalItemStructure_TreePlatform_Wood\'"',
            'description': 'Attaches to a large tree, enabling you to build on it.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Tree_Platform', 'id': 651,
            'class_name': 'PrimalItemStructure_TreePlatform_Wood_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Wooden_Tree_Platform.png'
        },
        {
            'name': 'Plant Species X', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_TurretPlant.PrimalItemStructure_TurretPlant\'"',
            'description': None, 'url': 'https://ark.fandom.com/wiki/Plant_Species_X', 'id': 652,
            'class_name': 'PrimalItemStructure_TurretPlant_C',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0d/Plant_Species_X.png'
        },
        {
            'name': 'Tek ATV', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Vehicles/VH_Buggy/Blueprint/PrimalItemVHBuggy.PrimalItemVHBuggy\'"',
            'description': 'Cruise around in this jaunty Element-powered ride. Supports a driver and one passenger, both of whom are able to wield weapons!',
            'url': 'https://ark.fandom.com/wiki/Tek_ATV', 'id': 653, 'class_name': None,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Tek_ATV.png'
        }
    ]
    models.Structure.bulk_insert(items)
