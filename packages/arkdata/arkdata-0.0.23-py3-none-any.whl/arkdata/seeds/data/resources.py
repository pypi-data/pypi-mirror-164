from arkdata import models


def backup_seed():
    models.Resource.new(id=7, name='Wood', stack_size=100, class_name='PrimalItemResource_Wood_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wood.PrimalItemResource_Wood\'"',
                        url='https://ark.fandom.com/wiki/Wood', description='A thick, sturdy cutting from a tree.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Wood.png')
    models.Resource.new(id=74, name='Thatch', stack_size=200, class_name='PrimalItemResource_Thatch_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Thatch.PrimalItemResource_Thatch\'"',
                        url='https://ark.fandom.com/wiki/Thatch',
                        description='Sticks torn from trees. Useful for primitive buildings.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/51/Thatch.png')
    models.Resource.new(id=8, name='Stone', stack_size=100, class_name='PrimalItemResource_Stone_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Stone.PrimalItemResource_Stone\'"',
                        url='https://ark.fandom.com/wiki/Stone', description='A hefty chunk of stone.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d4/Stone.png')
    models.Resource.new(id=123, name='Stimulant', stack_size=100, class_name='PrimalItemConsumable_Stimulant_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Stimulant.PrimalItemConsumable_Stimulant\'"',
                        url='https://ark.fandom.com/wiki/Stimulant', description='Keeps you awake, but dehydrates you.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e2/Stimulant.png')
    models.Resource.new(id=107, name='Sparkpowder', stack_size=100, class_name='PrimalItemResource_Sparkpowder_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Sparkpowder.PrimalItemResource_Sparkpowder\'"',
                        url='https://ark.fandom.com/wiki/Sparkpowder',
                        description='Created by grinding flint with stone in a Mortar and Pestle or Chemistry Table.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/56/Sparkpowder.png')
    models.Resource.new(id=160, name='Silica Pearls', stack_size=100, class_name='PrimalItemResource_Silicon_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Silicon.PrimalItemResource_Silicon\'"',
                        url='https://ark.fandom.com/wiki/Silica_Pearls',
                        description='These pearls are made almost entirely of silicon. Can be refined into silicon plates.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4a/Silica_Pearls.png')
    models.Resource.new(id=382, name='Re-Fertilizer', stack_size=100, class_name='PrimalItemConsumableMiracleGro_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/BaseBPs/PrimalItemConsumableMiracleGro.PrimalItemConsumableMiracleGro\'"',
                        url='https://ark.fandom.com/wiki/Re-Fertilizer',
                        description='Spread these seeds of concentrated nutrients around and what was once harvested may yet regrow, even nearby a structure!',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Re-Fertilizer.png')
    models.Resource.new(id=247, name='Rare Mushroom', stack_size=100, class_name='PrimalItemResource_RareMushroom_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_RareMushroom.PrimalItemResource_RareMushroom\'"',
                        url='https://ark.fandom.com/wiki/Rare_Mushroom',
                        description='You feel lightheaded after just touching this. Ingesting it would be dangerous.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/30/Rare_Mushroom.png')
    models.Resource.new(id=246, name='Rare Flower', stack_size=100, class_name='PrimalItemResource_RareFlower_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_RareFlower.PrimalItemResource_RareFlower\'"',
                        url='https://ark.fandom.com/wiki/Rare_Flower',
                        description='Even the smell of this flower makes you slightly angry.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bb/Rare_Flower.png')
    models.Resource.new(id=163, name='Polymer', stack_size=100, class_name='PrimalItemResource_Polymer_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Polymer.PrimalItemResource_Polymer\'"',
                        url='https://ark.fandom.com/wiki/Polymer',
                        description='These incredibly strong, lightweight plates can be shaped and then heat treated into casings for anything.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Polymer.png')
    models.Resource.new(id=419, name='Pelt', stack_size=200, class_name='PrimalItemResource_Pelt_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Pelt.PrimalItemResource_Pelt\'"',
                        url='https://ark.fandom.com/wiki/Pelt',
                        description='A thick piece of skin, densely covered with heavy insulating fur. Carefully hacked from a dead animal.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Pelt.png')
    models.Resource.new(id=159, name='Oil', stack_size=100, class_name='PrimalItemResource_Oil_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Oil.PrimalItemResource_Oil\'"',
                        url='https://ark.fandom.com/wiki/Oil',
                        description='A thick blob of unrefined oil. Can be refined with hide to make gasoline.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/06/Oil.png')
    models.Resource.new(id=141, name='Obsidian', stack_size=100, class_name='PrimalItemResource_Obsidian_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Obsidian.PrimalItemResource_Obsidian\'"',
                        url='https://ark.fandom.com/wiki/Obsidian',
                        description='A very rare resource, found underground. Can be broken down and used to make modern tech.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/23/Obsidian.png')
    models.Resource.new(id=122, name='Narcotic', stack_size=100, class_name='PrimalItemConsumable_Narcotic_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Narcotic.PrimalItemConsumable_Narcotic\'"',
                        url='https://ark.fandom.com/wiki/Narcotic',
                        description='Increases your health, but puts you to sleep.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Narcotic.png')
    models.Resource.new(id=9, name='Metal', stack_size=200, class_name='PrimalItemResource_Metal_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Metal.PrimalItemResource_Metal\'"',
                        url='https://ark.fandom.com/wiki/Metal',
                        description='A lump of unrefined metal ore, mined from rocks usually found high on mountains, or in caves. Can be refined in a Forge.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Metal.png')
    models.Resource.new(id=73, name='Metal Ingot', stack_size=200, class_name='PrimalItemResource_MetalIngot_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_MetalIngot.PrimalItemResource_MetalIngot\'"',
                        url='https://ark.fandom.com/wiki/Metal_Ingot',
                        description='A lump of unrefined metal ore, mined from rocks usually found high on mountains, or in caves. Can be refined in a Forge.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Metal_Ingot.png')
    models.Resource.new(id=213, name='Keratin', stack_size=100, class_name='PrimalItemResource_Keratin_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Keratin.PrimalItemResource_Keratin\'"',
                        url='https://ark.fandom.com/wiki/Keratin',
                        description='A firm, flexible material. Can be found in some animal horns, plates, shells, and ridges.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/88/Keratin.png')
    models.Resource.new(id=10, name='Hide', stack_size=200, class_name='PrimalItemResource_Hide_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Hide.PrimalItemResource_Hide\'"',
                        url='https://ark.fandom.com/wiki/Hide',
                        description='Thick skin, hacked from most dead animals.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Hide.png')
    models.Resource.new(id=108, name='Gunpowder', stack_size=100, class_name='PrimalItemResource_Gunpowder_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gunpowder.PrimalItemResource_Gunpowder\'"',
                        url='https://ark.fandom.com/wiki/Gunpowder',
                        description='A powerful propellant. Necessary for any firearm or explosive.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Gunpowder.png')
    models.Resource.new(id=161, name='Gasoline', stack_size=100, class_name='PrimalItemResource_Gasoline_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gasoline.PrimalItemResource_Gasoline\'"',
                        url='https://ark.fandom.com/wiki/Gasoline',
                        description='An advanced fuel. Can only be used in machines designed to consume it.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6e/Gasoline.png')
    models.Resource.new(id=72, name='Flint', stack_size=100, class_name='PrimalItemResource_Flint_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Flint.PrimalItemResource_Flint\'"',
                        url='https://ark.fandom.com/wiki/Flint',
                        description='Ferroceric flint that holds an edge better than regular stone.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Flint.png')
    models.Resource.new(id=75, name='Fiber', stack_size=300, class_name='PrimalItemResource_Fibers_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Fibers.PrimalItemResource_Fibers\'"',
                        url='https://ark.fandom.com/wiki/Fiber',
                        description='Delicately collected strands of plant. Perfect for making thread, cloth or rope.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Fiber.png')
    models.Resource.new(id=50, name='Fertilizer', stack_size=1, class_name='PrimalItemConsumable_Fertilizer_Compost_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Fertilizer_Compost.PrimalItemConsumable_Fertilizer_Compost\'"',
                        url='https://ark.fandom.com/wiki/Fertilizer',
                        description='A fertilizer high in nitrogen. Use this to help your crops grow.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Fertilizer.png')
    models.Resource.new(id=162, name='Electronics', stack_size=100, class_name='PrimalItemResource_Electronics_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Electronics.PrimalItemResource_Electronics\'"',
                        url='https://ark.fandom.com/wiki/Electronics',
                        description='This multipurpose computer chip can be used to create electronic devices.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dd/Electronics.png')
    models.Resource.new(id=77, name='Crystal', stack_size=100, class_name='PrimalItemResource_Crystal_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Crystal.PrimalItemResource_Crystal\'"',
                        url='https://ark.fandom.com/wiki/Crystal',
                        description='This strange crystalline material can be shaped into lenses, used as an electronics component, or mixed into powerful explosives.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Crystal.png')
    models.Resource.new(id=11, name='Chitin', stack_size=100, class_name='PrimalItemResource_Chitin_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Chitin.PrimalItemResource_Chitin\'"',
                        url='https://ark.fandom.com/wiki/Chitin',
                        description='This firm, flexible material makes up exoskeletons. Hacked primarily from dead insects.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Chitin.png')
    models.Resource.new(id=212, name='Chitin or Keratin', stack_size=100,
                        class_name='PrimalItemResource_ChitinOrKeratin_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ChitinOrKeratin.PrimalItemResource_ChitinOrKeratin\'"',
                        url='https://ark.fandom.com/wiki/Chitin_or_Keratin',
                        description='A firm, flexible material. Can be found in some animal horns, plates, shells, and ridges.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/88/Keratin.png')
    models.Resource.new(id=76, name='Charcoal', stack_size=100, class_name='PrimalItemResource_Charcoal_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Charcoal.PrimalItemResource_Charcoal\'"',
                        url='https://ark.fandom.com/wiki/Charcoal', description='Created by burning wood.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Charcoal.png')
    models.Resource.new(id=144, name='Cementing Paste', stack_size=100, class_name='PrimalItemResource_ChitinPaste_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ChitinPaste.PrimalItemResource_ChitinPaste\'"',
                        url='https://ark.fandom.com/wiki/Cementing_Paste',
                        description='Paste created at Mortar and Pestle.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Cementing_Paste.png')
    models.Resource.new(id=45, name='Blood Pack', stack_size=100, class_name='PrimalItemConsumable_BloodPack_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_BloodPack.PrimalItemConsumable_BloodPack\'"',
                        url='https://ark.fandom.com/wiki/Blood_Pack',
                        description='Use this to replace lost blood. Restores Health over time.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/58/Blood_Pack.png')
    models.Resource.new(name='Wishbone', stack_size=200, class_name='PrimalItemResource_Wishbone_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wishbone.PrimalItemResource_Wishbone\'"',
                        url='https://ark.fandom.com/wiki/Wishbone', description=None,
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bc/Wishbone.png')
    models.Resource.new(name='Mistletoe', stack_size=200, class_name='PrimalItemResource_MistleToe_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_MistleToe.PrimalItemResource_MistleToe\'"',
                        url='https://ark.fandom.com/wiki/Mistletoe', description='Have you been nice?',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Mistletoe.png')
    models.Resource.new(name='Coal', stack_size=200, class_name='PrimalItemResource_Coal_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Coal.PrimalItemResource_Coal\'"',
                        url='https://ark.fandom.com/wiki/Coal', description='Have you been naughty?',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a7/Coal.png')
    models.Resource.new(name='Birthday Candle', stack_size=200, class_name=None,
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_BirthdayCandle.PrimalItemResource_BirthdayCandle\'"',
                        url='https://ark.fandom.com/wiki/Birthday_Candle',
                        description='The critical ingredient for a Birthday Party.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Birthday_Candle.png')
    models.Resource.new(name='ARK Anniversary Surprise Cake', stack_size=50,
                        class_name='PrimalItemStructure_BirthdayCake_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/Structures/PopOutCake/PrimalItemStructure_BirthdayCake.PrimalItemStructure_BirthdayCake\'"',
                        url='https://ark.fandom.com/wiki/ARK_Anniversary_Surprise_Cake',
                        description='HAPPY 5th ARK Anniversary! Place it, write a custom message & hop inside, then jump out to surprise your friends! Or just use it to hide from danger...',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/ARK_Anniversary_Surprise_Cake.png')
    models.Resource.new(name='Cake Slice', stack_size=50, class_name='PrimalItemResource_CakeSlice_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_CakeSlice.PrimalItemResource_CakeSlice\'"',
                        url='https://ark.fandom.com/wiki/Cake_Slice',
                        description='A delicious piece of birthday cake, recovered from a theiving dodo! Sweet revenge!',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Cake_Slice.png')
    models.Resource.new(name='Absorbent Substrate', stack_size=100,
                        class_name='PrimalItemResource_SubstrateAbsorbent_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_SubstrateAbsorbent.PrimalItemResource_SubstrateAbsorbent\'"',
                        url='https://ark.fandom.com/wiki/Absorbent_Substrate',
                        description='This sticky compound excels at absorbing other chemicals.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Absorbent_Substrate.png')
    models.Resource.new(name='Achatina Paste', stack_size=100, class_name='PrimalItemResource_SnailPaste_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/Dinos/Achatina/PrimalItemResource_SnailPaste.PrimalItemResource_SnailPaste\'"',
                        url='https://ark.fandom.com/wiki/Achatina_Paste',
                        description='Achatina secretion chemically similar to Cementing Paste.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Cementing_Paste.png')
    models.Resource.new(name='Ambergris', stack_size=1, class_name='PrimalItemResource_Ambergris_C',
                        blueprint='"Blueprint\'/Game/Genesis/Dinos/SpaceWhale/PrimalItemResource_Ambergris.PrimalItemResource_Ambergris\'"',
                        url='https://ark.fandom.com/wiki/Ambergris_(Genesis:_Part_1)',
                        description='A waxy substance secreted by the Astrocetus. Used to create ordnance for the Astrocetus Tek Saddle.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/06/Ambergris_%28Genesis_Part_1%29.png')
    models.Resource.new(name='Ammonite Bile', stack_size=50, class_name='PrimalItemResource_AmmoniteBlood_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_AmmoniteBlood.PrimalItemResource_AmmoniteBlood\'"',
                        url='https://ark.fandom.com/wiki/Ammonite_Bile',
                        description='A congealed glob of Ammonite Bile. Can be used for medicinal purposes when carefully prepared.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fd/Ammonite_Bile.png')
    models.Resource.new(name='AnglerGel', stack_size=100, class_name='PrimalItemResource_AnglerGel_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_AnglerGel.PrimalItemResource_AnglerGel\'"',
                        url='https://ark.fandom.com/wiki/AnglerGel',
                        description='A thick, viscous substance that can sustain a flame for a remarkably long time.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/75/AnglerGel.png')
    models.Resource.new(name='Black Pearl', stack_size=200, class_name='PrimalItemResource_BlackPearl_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_BlackPearl.PrimalItemResource_BlackPearl\'"',
                        url='https://ark.fandom.com/wiki/Black_Pearl',
                        description='A rare resource from the bottom of the sea...',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4c/Black_Pearl.png')
    models.Resource.new(name='Blue Crystalized Sap', stack_size=100, class_name='PrimalItemResource_BlueSap_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_BlueSap.PrimalItemResource_BlueSap\'"',
                        url='https://ark.fandom.com/wiki/Blue_Crystalized_Sap_(Extinction)',
                        description='A thick blob of unrefined sap.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/73/Sap.png')
    models.Resource.new(name='Blue Gem', stack_size=100, class_name='PrimalItemResource_Gem_BioLum_C',
                        blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_BioLum.PrimalItemResource_Gem_BioLum\'"',
                        url='https://ark.fandom.com/wiki/Blue_Gem_(Aberration)',
                        description='This strange Gem has unusual properties that makes it ideal for increasing the structural integrity of items, armor, and structures.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Blue_Gem_%28Aberration%29.png')
    models.Resource.new(name='Charge Battery', stack_size=1, class_name='PrimalItem_ChargeBattery_C',
                        blueprint='"Blueprint\'/Game/Aberration/WeaponGlowStickCharge/PrimalItem_ChargeBattery.PrimalItem_ChargeBattery\'"',
                        url='https://ark.fandom.com/wiki/Charge_Battery_(Aberration)',
                        description='Stores Charge from Power Nodes, and can be placed in various Electrical Devices to power them.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Charge_Battery_%28Aberration%29.png')
    models.Resource.new(name='Clay', stack_size=100, class_name='PrimalItemResource_Clay_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Clay.PrimalItemResource_Clay\'"',
                        url='https://ark.fandom.com/wiki/Clay_(Scorched_Earth)',
                        description='Created by grinding Sand with Cactus Sap in a Mortar and Pestle.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Clay_%28Scorched_Earth%29.png')
    models.Resource.new(name='Condensed Gas', stack_size=100, class_name='PrimalItemResource_CondensedGas_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CondensedGas.PrimalItemResource_CondensedGas\'"',
                        url='https://ark.fandom.com/wiki/Condensed_Gas_(Extinction)',
                        description="A highly concentrated and hardened gas deposit. This could be refined back into it's gaseous form.",
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/70/Condensed_Gas_%28Extinction%29.png')
    models.Resource.new(name='Congealed Gas Ball', stack_size=100, class_name='PrimalItemResource_Gas_C',
                        blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gas.PrimalItemResource_Gas\'"',
                        url='https://ark.fandom.com/wiki/Congealed_Gas_Ball_(Aberration)',
                        description='Used for crafting, can be found within Gas Veins.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Congealed_Gas_Ball_%28Aberration%29.png')
    models.Resource.new(name='Corrupted Nodule', stack_size=10, class_name='PrimalItemResource_CorruptedPolymer_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CorruptedPolymer.PrimalItemResource_CorruptedPolymer\'"',
                        url='https://ark.fandom.com/wiki/Corrupted_Nodule_(Extinction)',
                        description='These incredibly strong, lightweight nodules are somehow naturally made in corrupted creatures. Incredibly hazardous to human health if consumed.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/67/Corrupted_Nodule_%28Extinction%29.png')
    models.Resource.new(name='Crafted Element Dust', stack_size=1000,
                        class_name='PrimalItemResource_ElementDustFromShards_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ElementDustFromShards.PrimalItemResource_ElementDustFromShards\'"',
                        url='https://ark.fandom.com/wiki/Crafted_Element_Dust_(Extinction)',
                        description='A small pile of Dust that could be refined into Element or Element Shards.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Element_Dust.png')
    models.Resource.new(name='Deathworm Horn', stack_size=20, class_name='PrimalItemResource_KeratinSpike_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/Dinos/Deathworm/PrimalItemResource_KeratinSpike.PrimalItemResource_KeratinSpike\'"',
                        url='https://ark.fandom.com/wiki/Deathworm_Horn_(Scorched_Earth)',
                        description='Beloved by large desert insects, and also can be used in very specialized Recipes...',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Deathworm_Horn_%28Scorched_Earth%29.png')
    models.Resource.new(name='Deathworm Horn or Woolly Rhino Horn', stack_size=None, class_name=None, blueprint=None,
                        url='https://ark.fandom.com/wiki/Deathworm_Horn_or_Woolly_Rhino_Horn',
                        description='Used in very specialized Recipes.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Woolly_Rhino_Horn.png')
    models.Resource.new(name='Dermis', stack_size=1, class_name='PrimalItem_TaxidermyDermis_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItem_TaxidermyDermis.PrimalItem_TaxidermyDermis\'"',
                        url='https://ark.fandom.com/wiki/Dermis_(Extinction)',
                        description='Attach this Dermis to a Taxidermy Base to display it!',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/35/Dermis_%28Extinction%29.png')
    models.Resource.new(name='Dinosaur Bone', stack_size=200, class_name='PrimalItemResource_ARKBone_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ARKBone.PrimalItemResource_ARKBone\'"',
                        url='https://ark.fandom.com/wiki/Dinosaur_Bone',
                        description='A very ancient looking bone, must be usefull for something!',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/50/Dinosaur_Bone.png')
    models.Resource.new(name='Element', stack_size=100, class_name='PrimalItemResource_Element_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Element.PrimalItemResource_Element\'"',
                        url='https://ark.fandom.com/wiki/Element',
                        description='A strange, highly advanced material humming with energy. It dissolves when transferred across ARKs.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a5/Element.png')
    models.Resource.new(name='Element Dust', stack_size=1000, class_name='PrimalItemResource_ElementDust_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ElementDust.PrimalItemResource_ElementDust\'"',
                        url='https://ark.fandom.com/wiki/Element_Dust',
                        description='A small pile of Dust that could be refined into Element or Element Shards.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Element_Dust.png')
    models.Resource.new(name='Element Ore', stack_size=100, class_name='PrimalItemResource_ElementOre_C',
                        blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_ElementOre.PrimalItemResource_ElementOre\'"',
                        url='https://ark.fandom.com/wiki/Element_Ore_(Aberration)', description='Unrefined Element.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Element_Ore_%28Aberration%29.png')
    models.Resource.new(name='Element Shard', stack_size=1000, class_name='PrimalItemResource_ElementShard_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ElementShard.PrimalItemResource_ElementShard\'"',
                        url='https://ark.fandom.com/wiki/Element_Shard',
                        description='A small chunk of strange, highly advanced material. It dissolves when transferred across ARKs.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/be/Element_Shard.png')
    models.Resource.new(name='Fragmented Green Gem', stack_size=100, class_name='PrimalItemResource_FracturedGem_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_FracturedGem.PrimalItemResource_FracturedGem\'"',
                        url='https://ark.fandom.com/wiki/Fragmented_Green_Gem_(Extinction)',
                        description='This strange Gem is used as a crafting ingredient in primitive tools and saddles.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Green_Gem_%28Aberration%29.png')
    models.Resource.new(name='Fungal Wood', stack_size=100, class_name='PrimalItemResource_FungalWood_C',
                        blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_FungalWood.PrimalItemResource_FungalWood\'"',
                        url='https://ark.fandom.com/wiki/Fungal_Wood_(Aberration)',
                        description='A thick, sturdy cutting from a tree.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Wood.png')
    models.Resource.new(name='Corrupted Wood', stack_size=100, class_name='PrimalItemResource_CorruptedWood_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CorruptedWood.PrimalItemResource_CorruptedWood\'"',
                        url='https://ark.fandom.com/wiki/Corrupted_Wood_(Extinction)',
                        description='A thick, sturdy cutting from a tree.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Wood.png')
    models.Resource.new(name='Golden Nugget', stack_size=1, class_name='PrimalItemResource_GoldenNugget_C',
                        blueprint='"Blueprint\'/Game/Genesis/Missions/Retrieve/RetrieveItems/GoldenNugget/PrimalItemResource_GoldenNugget.PrimalItemResource_GoldenNugget\'"',
                        url='https://ark.fandom.com/wiki/Golden_Nugget_(Genesis:_Part_1)',
                        description='A lump of unrefined golden ore. Creatures have been known to be attracted to its natural shine, with many of them burying it for safekeeping.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cb/Golden_Nugget_%28Genesis_Part_1%29.png')
    models.Resource.new(name='Green Gem', stack_size=100, class_name='PrimalItemResource_Gem_Fertile_C',
                        blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_Fertile.PrimalItemResource_Gem_Fertile\'"',
                        url='https://ark.fandom.com/wiki/Green_Gem_(Aberration)',
                        description='This strange Gem is used as a crafting ingredient in primitive tools and saddles.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Green_Gem_%28Aberration%29.png')
    models.Resource.new(name='High Quality Pollen', stack_size=1, class_name='PrimalItemResource_HighQualityPollen_C',
                        blueprint='"Blueprint\'/Game/Genesis/Missions/Retrieve/RetrieveItems/HighQualityPollen/PrimalItemResource_HighQualityPollen.PrimalItemResource_HighQualityPollen\'"',
                        url='https://ark.fandom.com/wiki/High_Quality_Pollen_(Genesis:_Part_1)',
                        description='A high quality pollen spore. These are often dropped by specific pollen plants within the Bog biome.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/High_Quality_Pollen_%28Genesis_Part_1%29.png')
    models.Resource.new(name='Human Hair', stack_size=200, class_name='PrimalItemResource_Hair_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Hair.PrimalItemResource_Hair\'"',
                        url='https://ark.fandom.com/wiki/Human_Hair', description='A lock of human hair!',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/16/Human_Hair.png')
    models.Resource.new(name='Leech Blood', stack_size=50, class_name='PrimalItemResource_LeechBlood_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_LeechBlood.PrimalItemResource_LeechBlood\'"',
                        url='https://ark.fandom.com/wiki/Leech_Blood',
                        description='A congealed glob of Leech Blood. Can be used for medicinal purposes when carefully prepared.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Leech_Blood.png')
    models.Resource.new(name='Leech Blood or Horns', stack_size=100, class_name='PrimalItemResourceGeneric_Curing_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResourceGeneric_Curing.PrimalItemResourceGeneric_Curing\'"',
                        url='https://ark.fandom.com/wiki/Leech_Blood_or_Horns',
                        description='A congealed glob of Leech Blood. Can be used for medicinal purposes when carefully prepared.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Leech_Blood.png')
    models.Resource.new(name='Mutagel', stack_size=100, class_name='PrimalItemConsumable_Mutagel_C',
                        blueprint='"Blueprint\'/Game/Genesis2/CoreBlueprints/Environment/Mutagen/PrimalItemConsumable_Mutagel.PrimalItemConsumable_Mutagel\'"',
                        url='https://ark.fandom.com/wiki/Mutagel_(Genesis:_Part_2)',
                        description='Rare mechanochemical substance derived from Mutagen. Use with caution to tame autonomous Stryders.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9c/Mutagel_%28Genesis_Part_2%29.png')
    models.Resource.new(name='Mutagen', stack_size=100, class_name='PrimalItemConsumable_Mutagen_C',
                        blueprint='"Blueprint\'/Game/Genesis2/CoreBlueprints/Environment/Mutagen/PrimalItemConsumable_Mutagen.PrimalItemConsumable_Mutagen\'"',
                        url='https://ark.fandom.com/wiki/Mutagen_(Genesis:_Part_2)',
                        description="Rare substance with aggravating and mutagentic properties. Use with caution to boost creature stats and gain access to Rockwell's Inner Sanctum.",
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Mutagen_%28Genesis_Part_2%29.png')
    models.Resource.new(name='Oil (Tusoteuthis)', stack_size=100, class_name='PrimalItemResource_SquidOil_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/Dinos/Tusoteuthis/PrimalItemResource_SquidOil.PrimalItemResource_SquidOil\'"',
                        url='https://ark.fandom.com/wiki/Oil',
                        description='A thick blob of unrefined oil. Can be refined with hide to make gasoline.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Oil_%28Tusoteuthis%29.png')
    models.Resource.new(name='Organic Polymer', stack_size=20, class_name='PrimalItemResource_Polymer_Organic_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Polymer_Organic.PrimalItemResource_Polymer_Organic\'"',
                        url='https://ark.fandom.com/wiki/Organic_Polymer',
                        description='These incredibly strong, lightweight plates can be shaped and then heat treated into casings for anything.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Polymer.png')
    models.Resource.new(name='Pelt, Hair, or Wool', stack_size=200, class_name='PrimalItemResource_PeltOrHair_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_PeltOrHair.PrimalItemResource_PeltOrHair\'"',
                        url='https://ark.fandom.com/wiki/Pelt,_Hair,_or_Wool', description='Sheared from a sheep!',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Wool.png')
    models.Resource.new(name='Primal Crystal', stack_size=1, class_name='PrimalItemResource_Crystal_IslesPrimal_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/Dinos/CrystalWyvern/CrystalResources/Primal/PrimalItemResource_Crystal_IslesPrimal.PrimalItemResource_Crystal_IslesPrimal\'"',
                        url='https://ark.fandom.com/wiki/Primal_Crystal_(Crystal_Isles)',
                        description="This strange crystalline material can be shaped into lenses, used as an electronics component, or mixed into powerful explosives. This particular crystal pulses with primal energy and is the Crystal Wyvern's favorite treat.",
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Primal_Crystal_%28Crystal_Isles%29.png')
    models.Resource.new(name='Preserving Salt', stack_size=6, class_name='PrimalItemResource_PreservingSalt_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_PreservingSalt.PrimalItemResource_PreservingSalt\'"',
                        url='https://ark.fandom.com/wiki/Preserving_Salt_(Scorched_Earth)',
                        description='Created by grinding salt with sulfur in a Mortar and Pestle. Preserves food.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/ba/Preserving_Salt_%28Scorched_Earth%29.png')
    models.Resource.new(name='Propellant', stack_size=100, class_name='PrimalItemResource_Propellant_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Propellant.PrimalItemResource_Propellant\'"',
                        url='https://ark.fandom.com/wiki/Propellant_(Scorched_Earth)',
                        description='Used to manufacture highly flammable substances.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2f/Propellant_%28Scorched_Earth%29.png')
    models.Resource.new(name='Raw Salt', stack_size=100, class_name='PrimalItemResource_RawSalt_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_RawSalt.PrimalItemResource_RawSalt\'"',
                        url='https://ark.fandom.com/wiki/Raw_Salt_(Scorched_Earth)',
                        description='Mix it with sulfur to obtain Preserving Salt.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Raw_Salt_%28Scorched_Earth%29.png')
    models.Resource.new(name='Red Crystalized Sap', stack_size=100, class_name='PrimalItemResource_RedSap_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_RedSap.PrimalItemResource_RedSap\'"',
                        url='https://ark.fandom.com/wiki/Red_Crystalized_Sap_(Extinction)',
                        description='A thick blob of unrefined sap.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/73/Sap.png')
    models.Resource.new(name='Red Gem', stack_size=100, class_name='PrimalItemResource_Gem_Element_C',
                        blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_Element.PrimalItemResource_Gem_Element\'"',
                        url='https://ark.fandom.com/wiki/Red_Gem_(Aberration)',
                        description='This strange Gem has many unique properties that make it ideal for crafting.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Red_Gem_%28Aberration%29.png')
    models.Resource.new(name='Sand', stack_size=100, class_name='PrimalItemResource_Sand_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Sand.PrimalItemResource_Sand\'"',
                        url='https://ark.fandom.com/wiki/Sand_(Scorched_Earth)',
                        description='Used to craft Clay. Can be found in Sand rocks',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0c/Sand_%28Scorched_Earth%29.png')
    models.Resource.new(name='Sap', stack_size=30, class_name='PrimalItemResource_Sap_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Sap.PrimalItemResource_Sap\'"',
                        url='https://ark.fandom.com/wiki/Sap', description='A thick blob of unrefined sap.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/73/Sap.png')
    models.Resource.new(name='Scrap Metal', stack_size=200, class_name='PrimalItemResource_ScrapMetal_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ScrapMetal.PrimalItemResource_ScrapMetal\'"',
                        url='https://ark.fandom.com/wiki/Scrap_Metal',
                        description='A small pile of Scrap Metal. Can be refined in a Forge.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Scrap_Metal.png')
    models.Resource.new(name='Scrap Metal Ingot', stack_size=200, class_name='PrimalItemResource_ScrapMetalIngot_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ScrapMetalIngot.PrimalItemResource_ScrapMetalIngot\'"',
                        url='https://ark.fandom.com/wiki/Scrap_Metal_Ingot',
                        description='Created by refining Scrap Metal in a Forge. Very similar to standard Metal Ingots.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/20/Scrap_Metal_Ingot.png')
    models.Resource.new(name='Shell Fragment', stack_size=100, class_name='PrimalItemResource_TurtleShell_C',
                        blueprint='"Blueprint\'/Game/Genesis/CoreBlueprints/Resources/PrimalItemResource_TurtleShell.PrimalItemResource_TurtleShell\'"',
                        url='https://ark.fandom.com/wiki/Shell_Fragment_(Genesis:_Part_1)',
                        description='A firm, flexible material from the shell of a Megachelon. Can be used as a replacement for Keratin.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/87/Shell_Fragment_%28Genesis_Part_1%29.png')
    models.Resource.new(name='Silicate', stack_size=100, class_name='PrimalItemResource_Silicate_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_Silicate.PrimalItemResource_Silicate\'"',
                        url='https://ark.fandom.com/wiki/Silicate_(Extinction)',
                        description='Hardened deposits of silicon. Can be refined into Silicon plates.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/90/Silicate_%28Extinction%29.png')
    models.Resource.new(name='Silk', stack_size=200, class_name='PrimalItemResource_Silk_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Silk.PrimalItemResource_Silk\'"',
                        url='https://ark.fandom.com/wiki/Silk_(Scorched_Earth)',
                        description='Obtained from the Moth creatures. Used to craft desert clothes and the tent.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Silk_%28Scorched_Earth%29.png')
    models.Resource.new(name='Sulfur', stack_size=100, class_name='PrimalItemResource_Sulfur_C',
                        blueprint='"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Sulfur.PrimalItemResource_Sulfur\'"',
                        url='https://ark.fandom.com/wiki/Sulfur_(Scorched_Earth)',
                        description='Used to craft distinct kind of ammunition. Can be found in the Caves',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Sulfur_%28Scorched_Earth%29.png')
    models.Resource.new(name='Unstable Element', stack_size=1, class_name='PrimalItemResource_ElementRefined_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ElementRefined.PrimalItemResource_ElementRefined\'"',
                        url='https://ark.fandom.com/wiki/Unstable_Element_(Extinction)',
                        description='Refined Element Dust that is unstable. Over time it will stabilize and become element.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/63/Unstable_Element_%28Extinction%29.png')
    models.Resource.new(name='Unstable Element Shard', stack_size=1, class_name='PrimalItemResource_ShardRefined_C',
                        blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ShardRefined.PrimalItemResource_ShardRefined\'"',
                        url='https://ark.fandom.com/wiki/Unstable_Element_Shard_(Extinction)',
                        description='Refined Element Dust that is unstable. Over time it will stabilize and become an Element Shard.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/be/Element_Shard.png')
    models.Resource.new(name='Wool', stack_size=200, class_name='PrimalItemResource_Wool_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wool.PrimalItemResource_Wool\'"',
                        url='https://ark.fandom.com/wiki/Wool', description='Sheared from a sheep!',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Wool.png')
    models.Resource.new(name='Woolly Rhino Horn', stack_size=20, class_name='PrimalItemResource_Horn_C',
                        blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Horn.PrimalItemResource_Horn\'"',
                        url='https://ark.fandom.com/wiki/Woolly_Rhino_Horn',
                        description='Used in very specialized Recipes.',
                        image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Woolly_Rhino_Horn.png')
    items = [item.to_json() for item in models.Resource.all()]
    print(items)


def seed():
    items = [
        {
            'class_name': 'PrimalItemResource_Wood_C', 'id': 7, 'description': 'A thick, sturdy cutting from a tree.',
            'url': 'https://ark.fandom.com/wiki/Wood', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wood.PrimalItemResource_Wood\'"',
            'name': 'Wood',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Wood.png'
        },
        {
            'class_name': 'PrimalItemResource_Stone_C', 'id': 8, 'description': 'A hefty chunk of stone.',
            'url': 'https://ark.fandom.com/wiki/Stone', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Stone.PrimalItemResource_Stone\'"',
            'name': 'Stone',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d4/Stone.png'
        },
        {
            'class_name': 'PrimalItemResource_Metal_C', 'id': 9,
            'description': 'A lump of unrefined metal ore, mined from rocks usually found high on mountains, or in caves. Can be refined in a Forge.',
            'url': 'https://ark.fandom.com/wiki/Metal', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Metal.PrimalItemResource_Metal\'"',
            'name': 'Metal',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Metal.png'
        },
        {
            'class_name': 'PrimalItemResource_Hide_C', 'id': 10,
            'description': 'Thick skin, hacked from most dead animals.', 'url': 'https://ark.fandom.com/wiki/Hide',
            'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Hide.PrimalItemResource_Hide\'"',
            'name': 'Hide',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Hide.png'
        },
        {
            'class_name': 'PrimalItemResource_Chitin_C', 'id': 11,
            'description': 'This firm, flexible material makes up exoskeletons. Hacked primarily from dead insects.',
            'url': 'https://ark.fandom.com/wiki/Chitin', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Chitin.PrimalItemResource_Chitin\'"',
            'name': 'Chitin',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Chitin.png'
        },
        {
            'class_name': 'PrimalItemConsumable_BloodPack_C', 'id': 45,
            'description': 'Use this to replace lost blood. Restores Health over time.',
            'url': 'https://ark.fandom.com/wiki/Blood_Pack', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_BloodPack.PrimalItemConsumable_BloodPack\'"',
            'name': 'Blood Pack',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/58/Blood_Pack.png'
        },
        {
            'class_name': 'PrimalItemConsumable_Fertilizer_Compost_C', 'id': 50,
            'description': 'A fertilizer high in nitrogen. Use this to help your crops grow.',
            'url': 'https://ark.fandom.com/wiki/Fertilizer', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Fertilizer_Compost.PrimalItemConsumable_Fertilizer_Compost\'"',
            'name': 'Fertilizer',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Fertilizer.png'
        },
        {
            'class_name': 'PrimalItemResource_Flint_C', 'id': 72,
            'description': 'Ferroceric flint that holds an edge better than regular stone.',
            'url': 'https://ark.fandom.com/wiki/Flint', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Flint.PrimalItemResource_Flint\'"',
            'name': 'Flint',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Flint.png'
        },
        {
            'class_name': 'PrimalItemResource_MetalIngot_C', 'id': 73,
            'description': 'A lump of unrefined metal ore, mined from rocks usually found high on mountains, or in caves. Can be refined in a Forge.',
            'url': 'https://ark.fandom.com/wiki/Metal_Ingot', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_MetalIngot.PrimalItemResource_MetalIngot\'"',
            'name': 'Metal Ingot',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Metal_Ingot.png'
        },
        {
            'class_name': 'PrimalItemResource_Thatch_C', 'id': 74,
            'description': 'Sticks torn from trees. Useful for primitive buildings.',
            'url': 'https://ark.fandom.com/wiki/Thatch', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Thatch.PrimalItemResource_Thatch\'"',
            'name': 'Thatch',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/51/Thatch.png'
        },
        {
            'class_name': 'PrimalItemResource_Fibers_C', 'id': 75,
            'description': 'Delicately collected strands of plant. Perfect for making thread, cloth or rope.',
            'url': 'https://ark.fandom.com/wiki/Fiber', 'stack_size': 300,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Fibers.PrimalItemResource_Fibers\'"',
            'name': 'Fiber',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Fiber.png'
        },
        {
            'class_name': 'PrimalItemResource_Charcoal_C', 'id': 76, 'description': 'Created by burning wood.',
            'url': 'https://ark.fandom.com/wiki/Charcoal', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Charcoal.PrimalItemResource_Charcoal\'"',
            'name': 'Charcoal',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Charcoal.png'
        },
        {
            'class_name': 'PrimalItemResource_Crystal_C', 'id': 77,
            'description': 'This strange crystalline material can be shaped into lenses, used as an electronics component, or mixed into powerful explosives.',
            'url': 'https://ark.fandom.com/wiki/Crystal', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Crystal.PrimalItemResource_Crystal\'"',
            'name': 'Crystal',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Crystal.png'
        },
        {
            'class_name': 'PrimalItem_Note_C', 'id': 97,
            'description': 'Write your own text on a note! Or put it in a Cooking Pot to make a Custom Recipe!',
            'url': 'https://ark.fandom.com/wiki/Note', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_Note.PrimalItem_Note\'"',
            'name': 'Note',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cc/Note.png'
        },
        {
            'class_name': 'PrimalItemResource_Sparkpowder_C', 'id': 107,
            'description': 'Created by grinding flint with stone in a Mortar and Pestle or Chemistry Table.',
            'url': 'https://ark.fandom.com/wiki/Sparkpowder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Sparkpowder.PrimalItemResource_Sparkpowder\'"',
            'name': 'Sparkpowder',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/56/Sparkpowder.png'
        },
        {
            'class_name': 'PrimalItemResource_Gunpowder_C', 'id': 108,
            'description': 'A powerful propellant. Necessary for any firearm or explosive.',
            'url': 'https://ark.fandom.com/wiki/Gunpowder', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gunpowder.PrimalItemResource_Gunpowder\'"',
            'name': 'Gunpowder',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Gunpowder.png'
        },
        {
            'class_name': 'PrimalItemConsumable_Narcotic_C', 'id': 122,
            'description': 'Increases your health, but puts you to sleep.',
            'url': 'https://ark.fandom.com/wiki/Narcotic', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Narcotic.PrimalItemConsumable_Narcotic\'"',
            'name': 'Narcotic',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Narcotic.png'
        },
        {
            'class_name': 'PrimalItemConsumable_Stimulant_C', 'id': 123,
            'description': 'Keeps you awake, but dehydrates you.', 'url': 'https://ark.fandom.com/wiki/Stimulant',
            'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/PrimalItemConsumable_Stimulant.PrimalItemConsumable_Stimulant\'"',
            'name': 'Stimulant',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e2/Stimulant.png'
        },
        {
            'class_name': 'PrimalItemResource_Obsidian_C', 'id': 141,
            'description': 'A very rare resource, found underground. Can be broken down and used to make modern tech.',
            'url': 'https://ark.fandom.com/wiki/Obsidian', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Obsidian.PrimalItemResource_Obsidian\'"',
            'name': 'Obsidian',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/23/Obsidian.png'
        },
        {
            'class_name': 'PrimalItemResource_ChitinPaste_C', 'id': 144,
            'description': 'Paste created at Mortar and Pestle.', 'url': 'https://ark.fandom.com/wiki/Cementing_Paste',
            'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ChitinPaste.PrimalItemResource_ChitinPaste\'"',
            'name': 'Cementing Paste',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Cementing_Paste.png'
        },
        {
            'class_name': 'PrimalItemResource_Oil_C', 'id': 159,
            'description': 'A thick blob of unrefined oil. Can be refined with hide to make gasoline.',
            'url': 'https://ark.fandom.com/wiki/Oil', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Oil.PrimalItemResource_Oil\'"',
            'name': 'Oil',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/06/Oil.png'
        },
        {
            'class_name': 'PrimalItemResource_Silicon_C', 'id': 160,
            'description': 'These pearls are made almost entirely of silicon. Can be refined into silicon plates.',
            'url': 'https://ark.fandom.com/wiki/Silica_Pearls', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Silicon.PrimalItemResource_Silicon\'"',
            'name': 'Silica Pearls',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4a/Silica_Pearls.png'
        },
        {
            'class_name': 'PrimalItemResource_Gasoline_C', 'id': 161,
            'description': 'An advanced fuel. Can only be used in machines designed to consume it.',
            'url': 'https://ark.fandom.com/wiki/Gasoline', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Gasoline.PrimalItemResource_Gasoline\'"',
            'name': 'Gasoline',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6e/Gasoline.png'
        },
        {
            'class_name': 'PrimalItemResource_Electronics_C', 'id': 162,
            'description': 'This multipurpose computer chip can be used to create electronic devices.',
            'url': 'https://ark.fandom.com/wiki/Electronics', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Electronics.PrimalItemResource_Electronics\'"',
            'name': 'Electronics',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dd/Electronics.png'
        },
        {
            'class_name': 'PrimalItemResource_Polymer_C', 'id': 163,
            'description': 'These incredibly strong, lightweight plates can be shaped and then heat treated into casings for anything.',
            'url': 'https://ark.fandom.com/wiki/Polymer', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Polymer.PrimalItemResource_Polymer\'"',
            'name': 'Polymer',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Polymer.png'
        },
        {
            'class_name': 'PrimalItemResource_ChitinOrKeratin_C', 'id': 212,
            'description': 'A firm, flexible material. Can be found in some animal horns, plates, shells, and ridges.',
            'url': 'https://ark.fandom.com/wiki/Chitin_or_Keratin', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ChitinOrKeratin.PrimalItemResource_ChitinOrKeratin\'"',
            'name': 'Chitin or Keratin',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/88/Keratin.png'
        },
        {
            'class_name': 'PrimalItemResource_Keratin_C', 'id': 213,
            'description': 'A firm, flexible material. Can be found in some animal horns, plates, shells, and ridges.',
            'url': 'https://ark.fandom.com/wiki/Keratin', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Keratin.PrimalItemResource_Keratin\'"',
            'name': 'Keratin',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/88/Keratin.png'
        },
        {
            'class_name': 'PrimalItemResource_RareFlower_C', 'id': 246,
            'description': 'Even the smell of this flower makes you slightly angry.',
            'url': 'https://ark.fandom.com/wiki/Rare_Flower', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_RareFlower.PrimalItemResource_RareFlower\'"',
            'name': 'Rare Flower',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bb/Rare_Flower.png'
        },
        {
            'class_name': 'PrimalItemResource_RareMushroom_C', 'id': 247,
            'description': 'You feel lightheaded after just touching this. Ingesting it would be dangerous.',
            'url': 'https://ark.fandom.com/wiki/Rare_Mushroom', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_RareMushroom.PrimalItemResource_RareMushroom\'"',
            'name': 'Rare Mushroom',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/30/Rare_Mushroom.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_EnduroStew_C', 'id': 252,
            'description': 'This hearty dish is like a workout in the form of a meal. You will find yourself hitting harder and running longer after eating this.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Enduro_Stew', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_EnduroStew.PrimalItem_RecipeNote_EnduroStew\'"',
            'name': 'Rockwell Recipes: Enduro Stew',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1e/Rockwell_Recipes-_Enduro_Stew.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_LazarusChowder_C', 'id': 253,
            'description': "This creamy dish improves the body's natural constitution. You will recover from injury more quickly after eating this, and your body will need less oxygen.",
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Lazarus_Chowder', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_LazarusChowder.PrimalItem_RecipeNote_LazarusChowder\'"',
            'name': 'Rockwell Recipes: Lazarus Chowder',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Rockwell_Recipes-_Lazarus_Chowder.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_CalienSoup_C', 'id': 254,
            'description': 'This simple vegetarian dish refreshes your body like an oasis. Helps keep you stay hydrated and feel cool.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Calien_Soup', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_CalienSoup.PrimalItem_RecipeNote_CalienSoup\'"',
            'name': 'Rockwell Recipes: Calien Soup',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Rockwell_Recipes-_Calien_Soup.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_FriaCurry_C', 'id': 255,
            'description': 'This spicy vegetarian dish fills the body with a comfortable warmth. It controls your apetite while helping you ignore the cold.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Fria_Curry', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_FriaCurry.PrimalItem_RecipeNote_FriaCurry\'"',
            'name': 'Rockwell Recipes: Fria Curry',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3d/Rockwell_Recipes-_Fria_Curry.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_FocalChili_C', 'id': 256,
            'description': 'This filling dish is full of nutritional energy. You will notice your mind more focused after eating this, allowing you to avoid obstacles and distractions.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Focal_Chili', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_FocalChili.PrimalItem_RecipeNote_FocalChili\'"',
            'name': 'Rockwell Recipes: Focal Chili',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Rockwell_Recipes-_Focal_Chili.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_BattleTartare_C', 'id': 257,
            'description': 'Only eat this dish when you intend to go into a brawl. It causes pain and stress to your body, but grants you almost supernatural strength, speed, and resilience. Warning: This concoction can be habit-forming.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Battle_Tartare', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_BattleTartare.PrimalItem_RecipeNote_BattleTartare\'"',
            'name': 'Rockwell Recipes: Battle Tartare',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/84/Rockwell_Recipes-_Battle_Tartare.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_ShadowSteak_C', 'id': 258,
            'description': 'Only eat this dish in the dark. It causes the light receptors in your eyes to become hyperactive, improves your hand-eye coordination, and allows your body to ignore extreme temperatures. Warning: this concoction can be habit-forming.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Shadow_Steak_Saute', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_ShadowSteak.PrimalItem_RecipeNote_ShadowSteak\'"',
            'name': 'Rockwell Recipes: Shadow Steak Saute',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Rockwell_Recipes-_Shadow_Steak_Saute.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_Measurements_C', 'id': 259,
            'description': "I'm pretty sure I've figured out the measuring system used in those Rockwell Recipe sheets I've seen people packing away.",
            'url': 'https://ark.fandom.com/wiki/Notes_on_Rockwell_Recipes', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_Measurements.PrimalItem_RecipeNote_Measurements\'"',
            'name': 'Notes on Rockwell Recipes',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/06/Notes_on_Rockwell_Recipes.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_HealSoup_C', 'id': 297,
            'description': "This simple tonic immediately jump-starts your body's natural healing.",
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Medical_Brew', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_HealSoup.PrimalItem_RecipeNote_HealSoup\'"',
            'name': 'Rockwell Recipes: Medical Brew',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f6/Rockwell_Recipes-_Medical_Brew.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_StaminaSoup_C', 'id': 298,
            'description': "This simple tonic quickly rejuvenates your body's natural energy stores.",
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Energy_Brew', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_StaminaSoup.PrimalItem_RecipeNote_StaminaSoup\'"',
            'name': 'Rockwell Recipes: Energy Brew',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dd/Rockwell_Recipes-_Energy_Brew.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_Jerky_C', 'id': 300,
            'description': 'While it might not taste as good as freshly cooked meat, jerky is just as nutritious and lasts much longer.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Meat_Jerky', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_Jerky.PrimalItem_RecipeNote_Jerky\'"',
            'name': 'Rockwell Recipes: Meat Jerky',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/99/Rockwell_Recipes-_Meat_Jerky.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_Dye_C', 'id': 367,
            'description': 'This substance can be used to color certain items and structures.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Decorative_Coloring', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_Dye.PrimalItem_RecipeNote_Dye\'"',
            'name': 'Rockwell Recipes: Decorative Coloring',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Sky_Coloring.png'
        },
        {
            'class_name': 'PrimalItemConsumableMiracleGro_C', 'id': 382,
            'description': 'Spread these seeds of concentrated nutrients around and what was once harvested may yet regrow, even nearby a structure!',
            'url': 'https://ark.fandom.com/wiki/Re-Fertilizer', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Consumables/BaseBPs/PrimalItemConsumableMiracleGro.PrimalItemConsumableMiracleGro\'"',
            'name': 'Re-Fertilizer',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Re-Fertilizer.png'
        },
        {
            'class_name': 'PrimalItem_RecipeNote_RespecSoup_C', 'id': 415,
            'description': 'When consumed, this tonic causes neural overload. Synapses fire off too quickly resulting in damage to the memory centers of the brain related to construction. Warning: this concoctions may cause temporary memory loss, and resetting of Engrams.',
            'url': 'https://ark.fandom.com/wiki/Rockwell_Recipes-_Mindwipe_Tonic', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Notes/PrimalItem_RecipeNote_RespecSoup.PrimalItem_RecipeNote_RespecSoup\'"',
            'name': 'Rockwell Recipes: Mindwipe Tonic',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/30/Rockwell_Recipes-_Mindwipe_Tonic.png'
        },
        {
            'class_name': 'PrimalItemResource_Pelt_C', 'id': 419,
            'description': 'A thick piece of skin, densely covered with heavy insulating fur. Carefully hacked from a dead animal.',
            'url': 'https://ark.fandom.com/wiki/Pelt', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Pelt.PrimalItemResource_Pelt\'"',
            'name': 'Pelt',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Pelt.png'
        },
        {
            'class_name': 'PrimalItemResource_Wishbone_C', 'id': 420, 'description': None,
            'url': 'https://ark.fandom.com/wiki/Wishbone', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wishbone.PrimalItemResource_Wishbone\'"',
            'name': 'Wishbone',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bc/Wishbone.png'
        },
        {
            'class_name': 'PrimalItemResource_MistleToe_C', 'id': 421, 'description': 'Have you been nice?',
            'url': 'https://ark.fandom.com/wiki/Mistletoe', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_MistleToe.PrimalItemResource_MistleToe\'"',
            'name': 'Mistletoe',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Mistletoe.png'
        },
        {
            'class_name': 'PrimalItemResource_Coal_C', 'id': 422, 'description': 'Have you been naughty?',
            'url': 'https://ark.fandom.com/wiki/Coal', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Coal.PrimalItemResource_Coal\'"',
            'name': 'Coal',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a7/Coal.png'
        },
        {
            'class_name': None, 'id': 423, 'description': 'The critical ingredient for a Birthday Party.',
            'url': 'https://ark.fandom.com/wiki/Birthday_Candle', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_BirthdayCandle.PrimalItemResource_BirthdayCandle\'"',
            'name': 'Birthday Candle',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Birthday_Candle.png'
        },
        {
            'class_name': 'PrimalItemStructure_BirthdayCake_C', 'id': 424,
            'description': 'HAPPY 5th ARK Anniversary! Place it, write a custom message & hop inside, then jump out to surprise your friends! Or just use it to hide from danger...',
            'url': 'https://ark.fandom.com/wiki/ARK_Anniversary_Surprise_Cake', 'stack_size': 50,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Structures/PopOutCake/PrimalItemStructure_BirthdayCake.PrimalItemStructure_BirthdayCake\'"',
            'name': 'ARK Anniversary Surprise Cake',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/ARK_Anniversary_Surprise_Cake.png'
        },
        {
            'class_name': 'PrimalItemResource_CakeSlice_C', 'id': 425,
            'description': 'A delicious piece of birthday cake, recovered from a theiving dodo! Sweet revenge!',
            'url': 'https://ark.fandom.com/wiki/Cake_Slice', 'stack_size': 50,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_CakeSlice.PrimalItemResource_CakeSlice\'"',
            'name': 'Cake Slice',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Cake_Slice.png'
        },
        {
            'class_name': 'PrimalItemResource_SubstrateAbsorbent_C', 'id': 426,
            'description': 'This sticky compound excels at absorbing other chemicals.',
            'url': 'https://ark.fandom.com/wiki/Absorbent_Substrate', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_SubstrateAbsorbent.PrimalItemResource_SubstrateAbsorbent\'"',
            'name': 'Absorbent Substrate',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Absorbent_Substrate.png'
        },
        {
            'class_name': 'PrimalItemResource_SnailPaste_C', 'id': 427,
            'description': 'Achatina secretion chemically similar to Cementing Paste.',
            'url': 'https://ark.fandom.com/wiki/Achatina_Paste', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Dinos/Achatina/PrimalItemResource_SnailPaste.PrimalItemResource_SnailPaste\'"',
            'name': 'Achatina Paste',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Cementing_Paste.png'
        },
        {
            'class_name': 'PrimalItemResource_Ambergris_C', 'id': 428,
            'description': 'A waxy substance secreted by the Astrocetus. Used to create ordnance for the Astrocetus Tek Saddle.',
            'url': 'https://ark.fandom.com/wiki/Ambergris_(Genesis:_Part_1)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Dinos/SpaceWhale/PrimalItemResource_Ambergris.PrimalItemResource_Ambergris\'"',
            'name': 'Ambergris',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/06/Ambergris_%28Genesis_Part_1%29.png'
        },
        {
            'class_name': 'PrimalItemResource_AmmoniteBlood_C', 'id': 429,
            'description': 'A congealed glob of Ammonite Bile. Can be used for medicinal purposes when carefully prepared.',
            'url': 'https://ark.fandom.com/wiki/Ammonite_Bile', 'stack_size': 50,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_AmmoniteBlood.PrimalItemResource_AmmoniteBlood\'"',
            'name': 'Ammonite Bile',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fd/Ammonite_Bile.png'
        },
        {
            'class_name': 'PrimalItemResource_AnglerGel_C', 'id': 430,
            'description': 'A thick, viscous substance that can sustain a flame for a remarkably long time.',
            'url': 'https://ark.fandom.com/wiki/AnglerGel', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_AnglerGel.PrimalItemResource_AnglerGel\'"',
            'name': 'AnglerGel',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/75/AnglerGel.png'
        },
        {
            'class_name': 'PrimalItemResource_BlackPearl_C', 'id': 431,
            'description': 'A rare resource from the bottom of the sea...',
            'url': 'https://ark.fandom.com/wiki/Black_Pearl', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_BlackPearl.PrimalItemResource_BlackPearl\'"',
            'name': 'Black Pearl',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4c/Black_Pearl.png'
        },
        {
            'class_name': 'PrimalItemResource_BlueSap_C', 'id': 432, 'description': 'A thick blob of unrefined sap.',
            'url': 'https://ark.fandom.com/wiki/Blue_Crystalized_Sap_(Extinction)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_BlueSap.PrimalItemResource_BlueSap\'"',
            'name': 'Blue Crystalized Sap',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/73/Sap.png'
        },
        {
            'class_name': 'PrimalItemResource_Gem_BioLum_C', 'id': 433,
            'description': 'This strange Gem has unusual properties that makes it ideal for increasing the structural integrity of items, armor, and structures.',
            'url': 'https://ark.fandom.com/wiki/Blue_Gem_(Aberration)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_BioLum.PrimalItemResource_Gem_BioLum\'"',
            'name': 'Blue Gem',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Blue_Gem_%28Aberration%29.png'
        },
        {
            'class_name': 'PrimalItem_ChargeBattery_C', 'id': 434,
            'description': 'Stores Charge from Power Nodes, and can be placed in various Electrical Devices to power them.',
            'url': 'https://ark.fandom.com/wiki/Charge_Battery_(Aberration)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Aberration/WeaponGlowStickCharge/PrimalItem_ChargeBattery.PrimalItem_ChargeBattery\'"',
            'name': 'Charge Battery',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Charge_Battery_%28Aberration%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Clay_C', 'id': 435,
            'description': 'Created by grinding Sand with Cactus Sap in a Mortar and Pestle.',
            'url': 'https://ark.fandom.com/wiki/Clay_(Scorched_Earth)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Clay.PrimalItemResource_Clay\'"',
            'name': 'Clay',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Clay_%28Scorched_Earth%29.png'
        },
        {
            'class_name': 'PrimalItemResource_CondensedGas_C', 'id': 436,
            'description': "A highly concentrated and hardened gas deposit. This could be refined back into it's gaseous form.",
            'url': 'https://ark.fandom.com/wiki/Condensed_Gas_(Extinction)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CondensedGas.PrimalItemResource_CondensedGas\'"',
            'name': 'Condensed Gas',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/70/Condensed_Gas_%28Extinction%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Gas_C', 'id': 437,
            'description': 'Used for crafting, can be found within Gas Veins.',
            'url': 'https://ark.fandom.com/wiki/Congealed_Gas_Ball_(Aberration)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gas.PrimalItemResource_Gas\'"',
            'name': 'Congealed Gas Ball',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Congealed_Gas_Ball_%28Aberration%29.png'
        },
        {
            'class_name': 'PrimalItemResource_CorruptedPolymer_C', 'id': 438,
            'description': 'These incredibly strong, lightweight nodules are somehow naturally made in corrupted creatures. Incredibly hazardous to human health if consumed.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Nodule_(Extinction)', 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CorruptedPolymer.PrimalItemResource_CorruptedPolymer\'"',
            'name': 'Corrupted Nodule',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/67/Corrupted_Nodule_%28Extinction%29.png'
        },
        {
            'class_name': 'PrimalItemResource_ElementDustFromShards_C', 'id': 439,
            'description': 'A small pile of Dust that could be refined into Element or Element Shards.',
            'url': 'https://ark.fandom.com/wiki/Crafted_Element_Dust_(Extinction)', 'stack_size': 1000,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ElementDustFromShards.PrimalItemResource_ElementDustFromShards\'"',
            'name': 'Crafted Element Dust',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Element_Dust.png'
        },
        {
            'class_name': 'PrimalItemResource_KeratinSpike_C', 'id': 440,
            'description': 'Beloved by large desert insects, and also can be used in very specialized Recipes...',
            'url': 'https://ark.fandom.com/wiki/Deathworm_Horn_(Scorched_Earth)', 'stack_size': 20,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Dinos/Deathworm/PrimalItemResource_KeratinSpike.PrimalItemResource_KeratinSpike\'"',
            'name': 'Deathworm Horn',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Deathworm_Horn_%28Scorched_Earth%29.png'
        },
        {
            'class_name': None, 'id': 441, 'description': 'Used in very specialized Recipes.',
            'url': 'https://ark.fandom.com/wiki/Deathworm_Horn_or_Woolly_Rhino_Horn', 'stack_size': None,
            'blueprint': None, 'name': 'Deathworm Horn or Woolly Rhino Horn',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Woolly_Rhino_Horn.png'
        },
        {
            'class_name': 'PrimalItem_TaxidermyDermis_C', 'id': 442,
            'description': 'Attach this Dermis to a Taxidermy Base to display it!',
            'url': 'https://ark.fandom.com/wiki/Dermis_(Extinction)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/PrimalItem_TaxidermyDermis.PrimalItem_TaxidermyDermis\'"',
            'name': 'Dermis',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/35/Dermis_%28Extinction%29.png'
        },
        {
            'class_name': 'PrimalItemResource_ARKBone_C', 'id': 443,
            'description': 'A very ancient looking bone, must be usefull for something!',
            'url': 'https://ark.fandom.com/wiki/Dinosaur_Bone', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ARKBone.PrimalItemResource_ARKBone\'"',
            'name': 'Dinosaur Bone',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/50/Dinosaur_Bone.png'
        },
        {
            'class_name': 'PrimalItemResource_Element_C', 'id': 444,
            'description': 'A strange, highly advanced material humming with energy. It dissolves when transferred across ARKs.',
            'url': 'https://ark.fandom.com/wiki/Element', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Element.PrimalItemResource_Element\'"',
            'name': 'Element',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a5/Element.png'
        },
        {
            'class_name': 'PrimalItemResource_ElementDust_C', 'id': 445,
            'description': 'A small pile of Dust that could be refined into Element or Element Shards.',
            'url': 'https://ark.fandom.com/wiki/Element_Dust', 'stack_size': 1000,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ElementDust.PrimalItemResource_ElementDust\'"',
            'name': 'Element Dust',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Element_Dust.png'
        },
        {
            'class_name': 'PrimalItemResource_ElementOre_C', 'id': 446, 'description': 'Unrefined Element.',
            'url': 'https://ark.fandom.com/wiki/Element_Ore_(Aberration)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_ElementOre.PrimalItemResource_ElementOre\'"',
            'name': 'Element Ore',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Element_Ore_%28Aberration%29.png'
        },
        {
            'class_name': 'PrimalItemResource_ElementShard_C', 'id': 447,
            'description': 'A small chunk of strange, highly advanced material. It dissolves when transferred across ARKs.',
            'url': 'https://ark.fandom.com/wiki/Element_Shard', 'stack_size': 1000,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_ElementShard.PrimalItemResource_ElementShard\'"',
            'name': 'Element Shard',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/be/Element_Shard.png'
        },
        {
            'class_name': 'PrimalItemResource_FracturedGem_C', 'id': 448,
            'description': 'This strange Gem is used as a crafting ingredient in primitive tools and saddles.',
            'url': 'https://ark.fandom.com/wiki/Fragmented_Green_Gem_(Extinction)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_FracturedGem.PrimalItemResource_FracturedGem\'"',
            'name': 'Fragmented Green Gem',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Green_Gem_%28Aberration%29.png'
        },
        {
            'class_name': 'PrimalItemResource_FungalWood_C', 'id': 449,
            'description': 'A thick, sturdy cutting from a tree.',
            'url': 'https://ark.fandom.com/wiki/Fungal_Wood_(Aberration)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_FungalWood.PrimalItemResource_FungalWood\'"',
            'name': 'Fungal Wood',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Wood.png'
        },
        {
            'class_name': 'PrimalItemResource_CorruptedWood_C', 'id': 450,
            'description': 'A thick, sturdy cutting from a tree.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Wood_(Extinction)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_CorruptedWood.PrimalItemResource_CorruptedWood\'"',
            'name': 'Corrupted Wood',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Wood.png'
        },
        {
            'class_name': 'PrimalItemResource_GoldenNugget_C', 'id': 451,
            'description': 'A lump of unrefined golden ore. Creatures have been known to be attracted to its natural shine, with many of them burying it for safekeeping.',
            'url': 'https://ark.fandom.com/wiki/Golden_Nugget_(Genesis:_Part_1)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Missions/Retrieve/RetrieveItems/GoldenNugget/PrimalItemResource_GoldenNugget.PrimalItemResource_GoldenNugget\'"',
            'name': 'Golden Nugget',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cb/Golden_Nugget_%28Genesis_Part_1%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Gem_Fertile_C', 'id': 452,
            'description': 'This strange Gem is used as a crafting ingredient in primitive tools and saddles.',
            'url': 'https://ark.fandom.com/wiki/Green_Gem_(Aberration)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_Fertile.PrimalItemResource_Gem_Fertile\'"',
            'name': 'Green Gem',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c3/Green_Gem_%28Aberration%29.png'
        },
        {
            'class_name': 'PrimalItemResource_HighQualityPollen_C', 'id': 453,
            'description': 'A high quality pollen spore. These are often dropped by specific pollen plants within the Bog biome.',
            'url': 'https://ark.fandom.com/wiki/High_Quality_Pollen_(Genesis:_Part_1)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Missions/Retrieve/RetrieveItems/HighQualityPollen/PrimalItemResource_HighQualityPollen.PrimalItemResource_HighQualityPollen\'"',
            'name': 'High Quality Pollen',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/High_Quality_Pollen_%28Genesis_Part_1%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Hair_C', 'id': 454, 'description': 'A lock of human hair!',
            'url': 'https://ark.fandom.com/wiki/Human_Hair', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Hair.PrimalItemResource_Hair\'"',
            'name': 'Human Hair',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/16/Human_Hair.png'
        },
        {
            'class_name': 'PrimalItemResource_LeechBlood_C', 'id': 455,
            'description': 'A congealed glob of Leech Blood. Can be used for medicinal purposes when carefully prepared.',
            'url': 'https://ark.fandom.com/wiki/Leech_Blood', 'stack_size': 50,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_LeechBlood.PrimalItemResource_LeechBlood\'"',
            'name': 'Leech Blood',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Leech_Blood.png'
        },
        {
            'class_name': 'PrimalItemResourceGeneric_Curing_C', 'id': 456,
            'description': 'A congealed glob of Leech Blood. Can be used for medicinal purposes when carefully prepared.',
            'url': 'https://ark.fandom.com/wiki/Leech_Blood_or_Horns', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResourceGeneric_Curing.PrimalItemResourceGeneric_Curing\'"',
            'name': 'Leech Blood or Horns',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e3/Leech_Blood.png'
        },
        {
            'class_name': 'PrimalItemConsumable_Mutagel_C', 'id': 457,
            'description': 'Rare mechanochemical substance derived from Mutagen. Use with caution to tame autonomous Stryders.',
            'url': 'https://ark.fandom.com/wiki/Mutagel_(Genesis:_Part_2)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Genesis2/CoreBlueprints/Environment/Mutagen/PrimalItemConsumable_Mutagel.PrimalItemConsumable_Mutagel\'"',
            'name': 'Mutagel',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9c/Mutagel_%28Genesis_Part_2%29.png'
        },
        {
            'class_name': 'PrimalItemConsumable_Mutagen_C', 'id': 458,
            'description': "Rare substance with aggravating and mutagentic properties. Use with caution to boost creature stats and gain access to Rockwell's Inner Sanctum.",
            'url': 'https://ark.fandom.com/wiki/Mutagen_(Genesis:_Part_2)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Genesis2/CoreBlueprints/Environment/Mutagen/PrimalItemConsumable_Mutagen.PrimalItemConsumable_Mutagen\'"',
            'name': 'Mutagen',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Mutagen_%28Genesis_Part_2%29.png'
        },
        {
            'class_name': 'PrimalItemResource_SquidOil_C', 'id': 459,
            'description': 'A thick blob of unrefined oil. Can be refined with hide to make gasoline.',
            'url': 'https://ark.fandom.com/wiki/Oil', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Dinos/Tusoteuthis/PrimalItemResource_SquidOil.PrimalItemResource_SquidOil\'"',
            'name': 'Oil (Tusoteuthis)',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Oil_%28Tusoteuthis%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Polymer_Organic_C', 'id': 460,
            'description': 'These incredibly strong, lightweight plates can be shaped and then heat treated into casings for anything.',
            'url': 'https://ark.fandom.com/wiki/Organic_Polymer', 'stack_size': 20,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Polymer_Organic.PrimalItemResource_Polymer_Organic\'"',
            'name': 'Organic Polymer',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Polymer.png'
        },
        {
            'class_name': 'PrimalItemResource_PeltOrHair_C', 'id': 461, 'description': 'Sheared from a sheep!',
            'url': 'https://ark.fandom.com/wiki/Pelt,_Hair,_or_Wool', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_PeltOrHair.PrimalItemResource_PeltOrHair\'"',
            'name': 'Pelt, Hair, or Wool',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Wool.png'
        },
        {
            'class_name': 'PrimalItemResource_Crystal_IslesPrimal_C', 'id': 462,
            'description': "This strange crystalline material can be shaped into lenses, used as an electronics component, or mixed into powerful explosives. This particular crystal pulses with primal energy and is the Crystal Wyvern's favorite treat.",
            'url': 'https://ark.fandom.com/wiki/Primal_Crystal_(Crystal_Isles)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/Dinos/CrystalWyvern/CrystalResources/Primal/PrimalItemResource_Crystal_IslesPrimal.PrimalItemResource_Crystal_IslesPrimal\'"',
            'name': 'Primal Crystal',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bd/Primal_Crystal_%28Crystal_Isles%29.png'
        },
        {
            'class_name': 'PrimalItemResource_PreservingSalt_C', 'id': 463,
            'description': 'Created by grinding salt with sulfur in a Mortar and Pestle. Preserves food.',
            'url': 'https://ark.fandom.com/wiki/Preserving_Salt_(Scorched_Earth)', 'stack_size': 6,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_PreservingSalt.PrimalItemResource_PreservingSalt\'"',
            'name': 'Preserving Salt',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/ba/Preserving_Salt_%28Scorched_Earth%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Propellant_C', 'id': 464,
            'description': 'Used to manufacture highly flammable substances.',
            'url': 'https://ark.fandom.com/wiki/Propellant_(Scorched_Earth)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Propellant.PrimalItemResource_Propellant\'"',
            'name': 'Propellant',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2f/Propellant_%28Scorched_Earth%29.png'
        },
        {
            'class_name': 'PrimalItemResource_RawSalt_C', 'id': 465,
            'description': 'Mix it with sulfur to obtain Preserving Salt.',
            'url': 'https://ark.fandom.com/wiki/Raw_Salt_(Scorched_Earth)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_RawSalt.PrimalItemResource_RawSalt\'"',
            'name': 'Raw Salt',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Raw_Salt_%28Scorched_Earth%29.png'
        },
        {
            'class_name': 'PrimalItemResource_RedSap_C', 'id': 466, 'description': 'A thick blob of unrefined sap.',
            'url': 'https://ark.fandom.com/wiki/Red_Crystalized_Sap_(Extinction)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_RedSap.PrimalItemResource_RedSap\'"',
            'name': 'Red Crystalized Sap',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/73/Sap.png'
        },
        {
            'class_name': 'PrimalItemResource_Gem_Element_C', 'id': 467,
            'description': 'This strange Gem has many unique properties that make it ideal for crafting.',
            'url': 'https://ark.fandom.com/wiki/Red_Gem_(Aberration)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Resources/PrimalItemResource_Gem_Element.PrimalItemResource_Gem_Element\'"',
            'name': 'Red Gem',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Red_Gem_%28Aberration%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Sand_C', 'id': 468,
            'description': 'Used to craft Clay. Can be found in Sand rocks',
            'url': 'https://ark.fandom.com/wiki/Sand_(Scorched_Earth)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Sand.PrimalItemResource_Sand\'"',
            'name': 'Sand',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0c/Sand_%28Scorched_Earth%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Sap_C', 'id': 469, 'description': 'A thick blob of unrefined sap.',
            'url': 'https://ark.fandom.com/wiki/Sap', 'stack_size': 30,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Sap.PrimalItemResource_Sap\'"',
            'name': 'Sap',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/73/Sap.png'
        },
        {
            'class_name': 'PrimalItemResource_ScrapMetal_C', 'id': 470,
            'description': 'A small pile of Scrap Metal. Can be refined in a Forge.',
            'url': 'https://ark.fandom.com/wiki/Scrap_Metal', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ScrapMetal.PrimalItemResource_ScrapMetal\'"',
            'name': 'Scrap Metal',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Scrap_Metal.png'
        },
        {
            'class_name': 'PrimalItemResource_ScrapMetalIngot_C', 'id': 471,
            'description': 'Created by refining Scrap Metal in a Forge. Very similar to standard Metal Ingots.',
            'url': 'https://ark.fandom.com/wiki/Scrap_Metal_Ingot', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ScrapMetalIngot.PrimalItemResource_ScrapMetalIngot\'"',
            'name': 'Scrap Metal Ingot',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/20/Scrap_Metal_Ingot.png'
        },
        {
            'class_name': 'PrimalItemResource_TurtleShell_C', 'id': 472,
            'description': 'A firm, flexible material from the shell of a Megachelon. Can be used as a replacement for Keratin.',
            'url': 'https://ark.fandom.com/wiki/Shell_Fragment_(Genesis:_Part_1)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Genesis/CoreBlueprints/Resources/PrimalItemResource_TurtleShell.PrimalItemResource_TurtleShell\'"',
            'name': 'Shell Fragment',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/87/Shell_Fragment_%28Genesis_Part_1%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Silicate_C', 'id': 473,
            'description': 'Hardened deposits of silicon. Can be refined into Silicon plates.',
            'url': 'https://ark.fandom.com/wiki/Silicate_(Extinction)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_Silicate.PrimalItemResource_Silicate\'"',
            'name': 'Silicate',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/90/Silicate_%28Extinction%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Silk_C', 'id': 474,
            'description': 'Obtained from the Moth creatures. Used to craft desert clothes and the tent.',
            'url': 'https://ark.fandom.com/wiki/Silk_(Scorched_Earth)', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Silk.PrimalItemResource_Silk\'"',
            'name': 'Silk',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Silk_%28Scorched_Earth%29.png'
        },
        {
            'class_name': 'PrimalItemResource_Sulfur_C', 'id': 475,
            'description': 'Used to craft distinct kind of ammunition. Can be found in the Caves',
            'url': 'https://ark.fandom.com/wiki/Sulfur_(Scorched_Earth)', 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/CoreBlueprints/Resources/PrimalItemResource_Sulfur.PrimalItemResource_Sulfur\'"',
            'name': 'Sulfur',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Sulfur_%28Scorched_Earth%29.png'
        },
        {
            'class_name': 'PrimalItemResource_ElementRefined_C', 'id': 476,
            'description': 'Refined Element Dust that is unstable. Over time it will stabilize and become element.',
            'url': 'https://ark.fandom.com/wiki/Unstable_Element_(Extinction)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ElementRefined.PrimalItemResource_ElementRefined\'"',
            'name': 'Unstable Element',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/63/Unstable_Element_%28Extinction%29.png'
        },
        {
            'class_name': 'PrimalItemResource_ShardRefined_C', 'id': 477,
            'description': 'Refined Element Dust that is unstable. Over time it will stabilize and become an Element Shard.',
            'url': 'https://ark.fandom.com/wiki/Unstable_Element_Shard_(Extinction)', 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Resources/PrimalItemResource_ShardRefined.PrimalItemResource_ShardRefined\'"',
            'name': 'Unstable Element Shard',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/be/Element_Shard.png'
        },
        {
            'class_name': 'PrimalItemResource_Wool_C', 'id': 478, 'description': 'Sheared from a sheep!',
            'url': 'https://ark.fandom.com/wiki/Wool', 'stack_size': 200,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Wool.PrimalItemResource_Wool\'"',
            'name': 'Wool',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Wool.png'
        },
        {
            'class_name': 'PrimalItemResource_Horn_C', 'id': 479, 'description': 'Used in very specialized Recipes.',
            'url': 'https://ark.fandom.com/wiki/Woolly_Rhino_Horn', 'stack_size': 20,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Resources/PrimalItemResource_Horn.PrimalItemResource_Horn\'"',
            'name': 'Woolly Rhino Horn',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Woolly_Rhino_Horn.png'
        }
    ]
    models.Resource.bulk_insert(items)
