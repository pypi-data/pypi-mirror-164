from arkdata import models


def backup_seed():
    models.Skin.new(id=381, name='Trike Bone Helmet Skin', stack_size=1, class_name='PrimalItemSkin_TrikeSkullHelmet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TrikeSkullHelmet.PrimalItemSkin_TrikeSkullHelmet\'"',
                    url='https://ark.fandom.com/wiki/Trike_Bone_Helmet_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a noble look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Trike_Bone_Helmet_Skin.png')
    models.Skin.new(id=278, name='Rex Stomped Glasses Saddle Skin', stack_size=1,
                    class_name='PrimalItemArmor_RexSaddle_StompedGlasses_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemArmor_RexSaddle_StompedGlasses.PrimalItemArmor_RexSaddle_StompedGlasses\'"',
                    url='https://ark.fandom.com/wiki/Rex_Stomped_Glasses_Saddle_Skin',
                    description='Welcome to ARK! Equip a Tyrannosaurus with this to live the high life.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Rex_Stomped_Glasses_Saddle_Skin.png')
    models.Skin.new(id=295, name='Rex Bone Helmet', stack_size=1, class_name='PrimalItemSkin_BoneHelmet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BoneHelmet.PrimalItemSkin_BoneHelmet\'"',
                    url='https://ark.fandom.com/wiki/Rex_Bone_Helmet',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a scary look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Rex_Bone_Helmet_Skin.png')
    models.Skin.new(id=289, name='Parasaur Stylish Saddle Skin', stack_size=1,
                    class_name='PrimalItemArmor_ParaSaddle_Launch_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemArmor_ParaSaddle_Launch.PrimalItemArmor_ParaSaddle_Launch\'"',
                    url='https://ark.fandom.com/wiki/Parasaur_Stylish_Saddle_Skin',
                    description='Use this on a Parasaurolophus saddle to ride in posh style.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Parasaur_Stylish_Saddle_Skin.png')
    models.Skin.new(id=277, name='Hunter Hat Skin', stack_size=1, class_name='PrimalItemArmor_HideHelmetAlt_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HideHelmetAlt.PrimalItemArmor_HideHelmetAlt\'"',
                    url='https://ark.fandom.com/wiki/Hunter_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides an adventurous look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Hunter_Hat_Skin.png')
    models.Skin.new(id=320, name='Fireworks Flaregun Skin', stack_size=1,
                    class_name='PrimalItemSkin_FlaregunFireworks_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_FlaregunFireworks.PrimalItemSkin_FlaregunFireworks\'"',
                    url='https://ark.fandom.com/wiki/Fireworks_Flaregun_Skin',
                    description='Light up the sky with these independent fireworks!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Fireworks_Flaregun_Skin.png')
    models.Skin.new(id=432, name='DodoRex Mask Skin', stack_size=1, class_name='PrimalItemSkin_DodorexMask_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DodorexMask.PrimalItemSkin_DodorexMask\'"',
                    url='https://ark.fandom.com/wiki/DodoRex_Mask_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a hallowed look',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/DodoRex_Mask_Skin.png')
    models.Skin.new(id=304, name='Dino Glasses Skin', stack_size=1, class_name='PrimalItemSkin_DinoSpecs_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoSpecs.PrimalItemSkin_DinoSpecs\'"',
                    url='https://ark.fandom.com/wiki/Dino_Glasses_Skin',
                    description='You can use this to skin the appearance of a Saddle. Make your mount look distinguished and well-read with these impressive looking hand-made spectacles.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Dino_Glasses_Skin.png')
    models.Skin.new(name='Chibi Party Rex', stack_size=1, class_name='PrimalItemSkin_ChibiDino_PartyRex_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_PartyRex.PrimalItemSkin_ChibiDino_PartyRex\'"',
                    url='https://ark.fandom.com/wiki/Chibi_Party_Rex',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Chibi-Rex.png')
    models.Skin.new(name='Chibi-Allosaurus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Allosaurus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Allosaurus.PrimalItemSkin_ChibiDino_Allosaurus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Allosaurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/69/Chibi-Allosaurus.png')
    models.Skin.new(name='Chibi-Ammonite', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Ammonite_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Ammonite.PrimalItemSkin_ChibiDino_Ammonite\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Ammonite',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Chibi-Ammonite.png')
    models.Skin.new(name='Chibi-Ankylosaurus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Ankylosaurus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Ankylosaurus.PrimalItemSkin_ChibiDino_Ankylosaurus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Ankylosaurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/49/Chibi-Ankylosaurus.png')
    models.Skin.new(name='Chibi-Argentavis', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Argent_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Argent.PrimalItemSkin_ChibiDino_Argent\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Argentavis',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Chibi-Argentavis.png')
    models.Skin.new(name='Chibi-Astrocetus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Astrocetus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Astrocetus.PrimalItemSkin_ChibiDino_Astrocetus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Astrocetus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Chibi-Astrocetus.png')
    models.Skin.new(name='Chibi-Baryonyx', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Baryonyx_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Baryonyx.PrimalItemSkin_ChibiDino_Baryonyx\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Baryonyx',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0c/Chibi-Baryonyx.png')
    models.Skin.new(name='Chibi-Basilisk', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Basilisk_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Basilisk.PrimalItemSkin_ChibiDino_Basilisk\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Basilisk',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Chibi-Basilisk.png')
    models.Skin.new(name='Chibi-Beelzebufo', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Beelzebufo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Beelzebufo.PrimalItemSkin_ChibiDino_Beelzebufo\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Beelzebufo',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ac/Chibi-Beelzebufo.png')
    models.Skin.new(name='Chibi-Bloodstalker', stack_size=1, class_name='PrimalItemSkin_ChibiDino_BogSpider_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_BogSpider.PrimalItemSkin_ChibiDino_BogSpider\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Bloodstalker',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/67/Chibi-Bloodstalker.png')
    models.Skin.new(name='Chibi-Bonnet Otter', stack_size=1, class_name='PrimalItemSkin_ChibiDino_OtterBonnet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_OtterBonnet.PrimalItemSkin_ChibiDino_OtterBonnet\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Bonnet_Otter',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Chibi-Bonnet_Otter.png')
    models.Skin.new(name='Chibi-Brontosaurus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Bronto_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bronto.PrimalItemSkin_ChibiDino_Bronto\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Brontosaurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Chibi-Brontosaurus.png')
    models.Skin.new(name='Chibi-Broodmother', stack_size=1, class_name='PrimalItemSkin_ChibiDino_BroodMother_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_BroodMother.PrimalItemSkin_ChibiDino_BroodMother\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Broodmother',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/51/Chibi-Broodmother.png')
    models.Skin.new(name='Chibi-Bulbdog', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Bulbdog_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bulbdog.PrimalItemSkin_ChibiDino_Bulbdog\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Bulbdog',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Chibi-Bulbdog.png')
    models.Skin.new(name='Chibi-Bunny', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Bunny_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bunny.PrimalItemSkin_ChibiDino_Bunny\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Bunny',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ed/Chibi-Bunny.png')
    models.Skin.new(name='Chibi-Carbonemys', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Carbonemys_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Carbonemys.PrimalItemSkin_ChibiDino_Carbonemys\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Carbonemys',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Chibi-Carbonemys.png')
    models.Skin.new(name='Chibi-Carno', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Carnotaurus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Carnotaurus.PrimalItemSkin_ChibiDino_Carnotaurus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Carno',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Chibi-Carno.png')
    models.Skin.new(name='Chibi-Castroides', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Castroides_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Castroides.PrimalItemSkin_ChibiDino_Castroides\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Castroides',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/78/Chibi-Castroides.png')
    models.Skin.new(name='Chibi-Cnidaria', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Cnidaria_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Cnidaria.PrimalItemSkin_ChibiDino_Cnidaria\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Cnidaria',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Chibi-Cnidaria.png')
    models.Skin.new(name='Chibi-Crystal Wyvern', stack_size=1, class_name='PrimalItemSkin_ChibiDino_WyvernCrystal_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_WyvernCrystal.PrimalItemSkin_ChibiDino_WyvernCrystal\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Crystal_Wyvern',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Chibi-Crystal_Wyvern.png')
    models.Skin.new(name='Chibi-Daeodon', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Daeodon_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Daeodon.PrimalItemSkin_ChibiDino_Daeodon\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Daeodon',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6e/Chibi-Daeodon.png')
    models.Skin.new(name='Chibi-Direbear', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Direbear_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Direbear.PrimalItemSkin_ChibiDino_Direbear\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Direbear',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Direbear.png')
    models.Skin.new(name='Chibi-Direwolf', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Direwolf_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Direwolf.PrimalItemSkin_ChibiDino_Direwolf\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Direwolf',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/12/Chibi-Direwolf.png')
    models.Skin.new(name='Chibi-Dodo', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Dodo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Dodo.PrimalItemSkin_ChibiDino_Dodo\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Dodo',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d1/Chibi-Dodo.png')
    models.Skin.new(name='Chibi-Doedicurus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Doedicurus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Doedicurus.PrimalItemSkin_ChibiDino_Doedicurus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Doedicurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Chibi-Doedicurus.png')
    models.Skin.new(name='Chibi-Dunkleosteus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Dunkleo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Dunkleo.PrimalItemSkin_ChibiDino_Dunkleo\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Dunkleosteus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/87/Chibi-Dunkleosteus.png')
    models.Skin.new(name='Chibi-Enforcer', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Enforcer_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Enforcer.PrimalItemSkin_ChibiDino_Enforcer\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Enforcer',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Chibi-Enforcer.png')
    models.Skin.new(name='Chibi-Equus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Equus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Equus.PrimalItemSkin_ChibiDino_Equus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Equus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/35/Chibi-Equus.png')
    models.Skin.new(name='Chibi-Featherlight', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Featherlight_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Featherlight.PrimalItemSkin_ChibiDino_Featherlight\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Featherlight',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Chibi-Featherlight.png')
    models.Skin.new(name='Chibi-Ferox (Large)', stack_size=1,
                    class_name='PrimalItemSkin_ChibiDino_Shapeshifter_Large_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Shapeshifter_Large.PrimalItemSkin_ChibiDino_Shapeshifter_Large\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Ferox_(Large)',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ce/Chibi-Ferox_%28Large%29.png')
    models.Skin.new(name='Chibi-Ferox (Small)', stack_size=1,
                    class_name='PrimalItemSkin_ChibiDino_Shapeshifter_Small_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Shapeshifter_Small.PrimalItemSkin_ChibiDino_Shapeshifter_Small\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Ferox_(Small)',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Chibi-Ferox_%28Small%29.png')
    models.Skin.new(name='Chibi-Gacha Claus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_GachaClaus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_GachaClaus.PrimalItemSkin_ChibiDino_GachaClaus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Gacha_Claus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/af/Chibi-Gacha_Claus.png')
    models.Skin.new(name='Chibi-Gasbag', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Gasbag_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gasbag.PrimalItemSkin_ChibiDino_Gasbag\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Gasbag',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5d/Chibi-Gasbag.png')
    models.Skin.new(name='Chibi-Giganotosaurus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Gigant_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gigant.PrimalItemSkin_ChibiDino_Gigant\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Giganotosaurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Chibi-Giganotosaurus.png')
    models.Skin.new(name='Chibi-Gigantopithecus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Gigantopithecus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gigantopithecus.PrimalItemSkin_ChibiDino_Gigantopithecus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Gigantopithecus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Chibi-Gigantopithecus.png')
    models.Skin.new(name='Chibi-Glowtail', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Glowtail_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Glowtail.PrimalItemSkin_ChibiDino_Glowtail\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Glowtail',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/de/Chibi-Glowtail.png')
    models.Skin.new(name='Chibi-Griffin', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Griffin_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Griffin.PrimalItemSkin_ChibiDino_Griffin\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Griffin',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Chibi-Griffin.png')
    models.Skin.new(name='Chibi-Iguanodon', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Iguanodon_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Iguanodon.PrimalItemSkin_ChibiDino_Iguanodon\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Iguanodon',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Chibi-Iguanodon.png')
    models.Skin.new(name='Chibi-Karkinos', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Karkinos_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Karkinos.PrimalItemSkin_ChibiDino_Karkinos\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Karkinos',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Chibi-Karkinos.png')
    models.Skin.new(name='Chibi-Kentrosaurus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Kentrosaurus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Kentrosaurus.PrimalItemSkin_ChibiDino_Kentrosaurus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Kentrosaurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Chibi-Kentrosaurus.png')
    models.Skin.new(name='Chibi-Magmasaur', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Cherufe_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Cherufe.PrimalItemSkin_ChibiDino_Cherufe\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Magmasaur',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Chibi-Magmasaur.png')
    models.Skin.new(name='Chibi-Mammoth', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Mammoth_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Mammoth.PrimalItemSkin_ChibiDino_Mammoth\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Mammoth',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/32/Chibi-Mammoth.png')
    models.Skin.new(name='Chibi-Managarmr', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Managarmr_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Managarmr.PrimalItemSkin_ChibiDino_Managarmr\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Managarmr',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Chibi-Managarmr.png')
    models.Skin.new(name='Chibi-Manta', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Manta_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Manta.PrimalItemSkin_ChibiDino_Manta\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Manta',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/33/Chibi-Manta.png')
    models.Skin.new(name='Chibi-Mantis', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Mantis_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Mantis.PrimalItemSkin_ChibiDino_Mantis\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Mantis',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Chibi-Mantis.png')
    models.Skin.new(name='Chibi-Megalania', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Megalania_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megalania.PrimalItemSkin_ChibiDino_Megalania\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Megalania',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/93/Chibi-Megalania.png')
    models.Skin.new(name='Chibi-Megaloceros', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Megaloceros_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megaloceros.PrimalItemSkin_ChibiDino_Megaloceros\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Megaloceros',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ac/Chibi-Megaloceros.png')
    models.Skin.new(name='Chibi-Megalodon', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Megalodon_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megalodon.PrimalItemSkin_ChibiDino_Megalodon\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Megalodon',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Chibi-Megalodon.png')
    models.Skin.new(name='Chibi-Megatherium', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Megatherium_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megatherium.PrimalItemSkin_ChibiDino_Megatherium\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Megatherium',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d1/Chibi-Megatherium.png')
    models.Skin.new(name='Chibi-Mesopithecus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Mesopithecus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Mesopithecus.PrimalItemSkin_ChibiDino_Mesopithecus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Mesopithecus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Chibi-Mesopithecus.png')
    models.Skin.new(name='Chibi-Moschops', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Moschops_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Moschops.PrimalItemSkin_ChibiDino_Moschops\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Moschops',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Chibi-Moschops.png')
    models.Skin.new(name='Chibi-Otter', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Otter_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Otter.PrimalItemSkin_ChibiDino_Otter\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Otter',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/99/Chibi-Otter.png')
    models.Skin.new(name='Chibi-Oviraptor', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Oviraptor_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Oviraptor.PrimalItemSkin_ChibiDino_Oviraptor\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Oviraptor',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Chibi-Oviraptor.png')
    models.Skin.new(name='Chibi-Ovis', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Sheep_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Sheep.PrimalItemSkin_ChibiDino_Sheep\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Ovis',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6e/Chibi-Ovis.png')
    models.Skin.new(name='Chibi-Paraceratherium', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Paraceratherium_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Paraceratherium.PrimalItemSkin_ChibiDino_Paraceratherium\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Paraceratherium',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Chibi-Paraceratherium.png')
    models.Skin.new(name='Chibi-Parasaur', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Parasaur_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Parasaur.PrimalItemSkin_ChibiDino_Parasaur\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Parasaur',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Parasaur.png')
    models.Skin.new(name='Chibi-Phiomia', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Phiomia_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Phiomia.PrimalItemSkin_ChibiDino_Phiomia\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Phiomia',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Chibi-Phiomia.png')
    models.Skin.new(name='Chibi-Phoenix', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Phoenix_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Phoenix.PrimalItemSkin_ChibiDino_Phoenix\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Phoenix',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6c/Chibi-Phoenix.png')
    models.Skin.new(name='Chibi-Plesiosaur', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Plesiosaur_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Plesiosaur.PrimalItemSkin_ChibiDino_Plesiosaur\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Plesiosaur',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Chibi-Plesiosaur.png')
    models.Skin.new(name='Chibi-Procoptodon', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Procoptodon_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Procoptodon.PrimalItemSkin_ChibiDino_Procoptodon\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Procoptodon',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Chibi-Procoptodon.png')
    models.Skin.new(name='Chibi-Pteranodon', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Pteranodon_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Pteranodon.PrimalItemSkin_ChibiDino_Pteranodon\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Pteranodon',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2d/Chibi-Pteranodon.png')
    models.Skin.new(name='Chibi-Pulmonoscorpius', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Pulmonoscorpius_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Pulmonoscorpius.PrimalItemSkin_ChibiDino_Pulmonoscorpius\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Pulmonoscorpius',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Chibi-Pulmonoscorpius.png')
    models.Skin.new(name='Chibi-Quetzal', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Quetzal_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Quetzal.PrimalItemSkin_ChibiDino_Quetzal\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Quetzal',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Chibi-Quetzal.png')
    models.Skin.new(name='Chibi-Raptor', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Raptor_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Raptor.PrimalItemSkin_ChibiDino_Raptor\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Raptor',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Chibi-Raptor.png')
    models.Skin.new(name='Chibi-Reaper', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Reaper_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Reaper.PrimalItemSkin_ChibiDino_Reaper\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Reaper',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b5/Chibi-Reaper.png')
    models.Skin.new(name='Chibi-Reindeer', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Reindeer_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Reindeer.PrimalItemSkin_ChibiDino_Reindeer\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Reindeer',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Chibi-Reindeer.png')
    models.Skin.new(name='Chibi-Rex', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Rex_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Rex.PrimalItemSkin_ChibiDino_Rex\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Rex',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Chibi-Rex.png')
    models.Skin.new(name='Chibi-Rhino', stack_size=1, class_name='PrimalItemSkin_ChibiDino_WoollyRhino_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_WoollyRhino.PrimalItemSkin_ChibiDino_WoollyRhino\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Rhino',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/83/Chibi-Rhino.png')
    models.Skin.new(name='Chibi-Rock Drake', stack_size=1, class_name='PrimalItemSkin_ChibiDino_RockDrake_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_RockDrake.PrimalItemSkin_ChibiDino_RockDrake\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Rock_Drake',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Chibi-Rock_Drake.png')
    models.Skin.new(name='Chibi-Rock Golem', stack_size=1, class_name='PrimalItemSkin_ChibiDino_RockGolem_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_RockGolem.PrimalItemSkin_ChibiDino_RockGolem\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Rock_Golem',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Chibi-Rock_Golem.png')
    models.Skin.new(name='Chibi-Rollrat', stack_size=1, class_name='PrimalItemSkin_ChibiDino_MoleRat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_MoleRat.PrimalItemSkin_ChibiDino_MoleRat\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Rollrat',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/44/Chibi-Rollrat.png')
    models.Skin.new(name='Chibi-Sabertooth', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Saber_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Saber.PrimalItemSkin_ChibiDino_Saber\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Sabertooth',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Chibi-Sabertooth.png')
    models.Skin.new(name='Chibi-Sarco', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Sarco_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Sarco.PrimalItemSkin_ChibiDino_Sarco\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Sarco',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Chibi-Sarco.png')
    models.Skin.new(name='Chibi-Seeker', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Seeker_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Seeker.PrimalItemSkin_ChibiDino_Seeker\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Seeker',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Chibi-Seeker.png')
    models.Skin.new(name='Chibi-Shadowmane', stack_size=1, class_name='PrimalItemSkin_ChibiDino_ShadowMane_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_ShadowMane.PrimalItemSkin_ChibiDino_ShadowMane\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Shadowmane_(Genesis:_Part_2)',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Chibi-Shadowmane_%28Genesis_Part_2%29.png')
    models.Skin.new(name='Chibi-Shinehorn', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Shinehorn_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Shinehorn.PrimalItemSkin_ChibiDino_Shinehorn\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Shinehorn',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/70/Chibi-Shinehorn.png')
    models.Skin.new(name='Chibi-Skeletal Brontosaurus', stack_size=1,
                    class_name='PrimalItemSkin_ChibiDino_Bronto_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bronto_Bone.PrimalItemSkin_ChibiDino_Bronto_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Brontosaurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Skeletal_Brontosaurus.png')
    models.Skin.new(name='Chibi-Skeletal Carno', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Carnotaurus_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Carnotaurus_Bone.PrimalItemSkin_ChibiDino_Carnotaurus_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Carno',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Chibi-Skeletal_Carno.png')
    models.Skin.new(name='Chibi-Skeletal Giganotosaurus', stack_size=1,
                    class_name='PrimalItemSkin_ChibiDino_Gigant_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gigant_Bone.PrimalItemSkin_ChibiDino_Gigant_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Giganotosaurus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5a/Chibi-Skeletal_Giganotosaurus.png')
    models.Skin.new(name='Chibi-Skeletal Jerboa', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Jerboa_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Jerboa_Bone.PrimalItemSkin_ChibiDino_Jerboa_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Jerboa',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/06/Chibi-Skeletal_Jerboa.png')
    models.Skin.new(name='Chibi-Skeletal Quetzal', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Quetzal_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Quetzal_Bone.PrimalItemSkin_ChibiDino_Quetzal_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Quetzal',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Chibi-Skeletal_Quetzal.png')
    models.Skin.new(name='Chibi-Skeletal Raptor', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Raptor_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Raptor_Bone.PrimalItemSkin_ChibiDino_Raptor_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Raptor',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Chibi-Skeletal_Raptor.png')
    models.Skin.new(name='Chibi-Skeletal Rex', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Rex_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Rex_Bone.PrimalItemSkin_ChibiDino_Rex_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Rex',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/ba/Chibi-Skeletal_Rex.png')
    models.Skin.new(name='Chibi-Skeletal Stego', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Stego_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Stego_Bone.PrimalItemSkin_ChibiDino_Stego_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Stego',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/ff/Chibi-Skeletal_Stego.png')
    models.Skin.new(name='Chibi-Skeletal Trike', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Trike_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Trike_Bone.PrimalItemSkin_ChibiDino_Trike_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Trike',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/10/Chibi-Skeletal_Trike.png')
    models.Skin.new(name='Chibi-Skeletal Wyvern', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Wyvern_Bone_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Wyvern_Bone.PrimalItemSkin_ChibiDino_Wyvern_Bone\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Skeletal_Wyvern',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Chibi-Skeletal_Wyvern.png')
    models.Skin.new(name='Chibi-Snow Owl', stack_size=1, class_name='PrimalItemSkin_ChibiDino_SnowOwl_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_SnowOwl.PrimalItemSkin_ChibiDino_SnowOwl\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Snow_Owl',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Chibi-Snow_Owl.png')
    models.Skin.new(name='Chibi-Spino', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Spino_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Spino.PrimalItemSkin_ChibiDino_Spino\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Spino',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Chibi-Spino.png')
    models.Skin.new(name='Chibi-Stego', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Stego_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Stego.PrimalItemSkin_ChibiDino_Stego\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Stego',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Chibi-Stego.png')
    models.Skin.new(name='Chibi-Tapejara', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Tapejara_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Tapejara.PrimalItemSkin_ChibiDino_Tapejara\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Tapejara',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Tapejara.png')
    models.Skin.new(name='Chibi-Terror Bird', stack_size=1, class_name='PrimalItemSkin_ChibiDino_TerrorBird_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_TerrorBird.PrimalItemSkin_ChibiDino_TerrorBird\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Terror_Bird',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Chibi-Terror_Bird.png')
    models.Skin.new(name='Chibi-Therizino', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Therizino_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Therizino.PrimalItemSkin_ChibiDino_Therizino\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Therizino',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cb/Chibi-Therizino.png')
    models.Skin.new(name='Chibi-Thylacoleo', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Thylacoleo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Thylacoleo.PrimalItemSkin_ChibiDino_Thylacoleo\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Thylacoleo',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/Chibi-Thylacoleo.png')
    models.Skin.new(name='Chibi-Trike', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Trike_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Trike.PrimalItemSkin_ChibiDino_Trike\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Trike',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/16/Chibi-Trike.png')
    models.Skin.new(name='Chibi-Troodon', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Troodon_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Troodon.PrimalItemSkin_ChibiDino_Troodon\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Troodon',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/53/Chibi-Troodon.png')
    models.Skin.new(name='Chibi-Tropeognathus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Tropeognathus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Tropeognathus.PrimalItemSkin_ChibiDino_Tropeognathus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Tropeognathus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Chibi-Tropeognathus.png')
    models.Skin.new(name='Chibi-Tusoteuthis', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Tuso_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Tuso.PrimalItemSkin_ChibiDino_Tuso\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Tusoteuthis',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Chibi-Tusoteuthis.png')
    models.Skin.new(name='Chibi-Unicorn', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Unicorn_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Unicorn.PrimalItemSkin_ChibiDino_Unicorn\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Unicorn',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Chibi-Unicorn.png')
    models.Skin.new(name='Chibi-Velonasaur', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Velonasaur_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Velonasaur.PrimalItemSkin_ChibiDino_Velonasaur\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Velonasaur',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Chibi-Velonasaur.png')
    models.Skin.new(name='Chibi-Wyvern', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Wyvern_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Wyvern.PrimalItemSkin_ChibiDino_Wyvern\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Wyvern',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Chibi-Wyvern.png')
    models.Skin.new(name='Chibi-Yutyrannus', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Yutyrannus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Yutyrannus.PrimalItemSkin_ChibiDino_Yutyrannus\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Yutyrannus',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Chibi-Yutyrannus.png')
    models.Skin.new(name='Chibi-Zombie Wyvern', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Wyvern_Zombie_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Wyvern_Zombie.PrimalItemSkin_ChibiDino_Wyvern_Zombie\'"',
                    url='https://ark.fandom.com/wiki/Chibi-Zombie_Wyvern',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Chibi-Skeletal_Wyvern.png')
    models.Skin.new(name='Pair-o-Saurs Chibi', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Pairosaurs_VDay_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Pairosaurs_VDay.PrimalItemSkin_ChibiDino_Pairosaurs_VDay\'"',
                    url='https://ark.fandom.com/wiki/Pair-o-Saurs_Chibi',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Pair-o-Saurs_Chibi.png')
    models.Skin.new(name='Teeny Tiny Titano', stack_size=1, class_name='PrimalItemSkin_ChibiDino_Titano_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Titano.PrimalItemSkin_ChibiDino_Titano\'"',
                    url='https://ark.fandom.com/wiki/Teeny_Tiny_Titano',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7b/Teeny_Tiny_Titano.png')
    models.Skin.new(name='White-Collar Kairuku', stack_size=1, class_name='PrimalItemSkin_ChibiDino_TophatKairuku_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_TophatKairuku.PrimalItemSkin_ChibiDino_TophatKairuku\'"',
                    url='https://ark.fandom.com/wiki/White-Collar_Kairuku',
                    description='Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/White-Collar_Kairuku_Chibi.png')
    models.Skin.new(name='Aberrant Helmet Skin', stack_size=1, class_name='PrimalItemSkin_AberrationHelmet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_AberrationHelmet.PrimalItemSkin_AberrationHelmet\'"',
                    url='https://ark.fandom.com/wiki/Aberrant_Helmet_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a ferocious look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Aberrant_Helmet_Skin_%28Aberration%29.png')
    models.Skin.new(name='Aberrant Sword Skin', stack_size=1, class_name='PrimalItemSkin_AberrationSword_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_AberrationSword.PrimalItemSkin_AberrationSword\'"',
                    url='https://ark.fandom.com/wiki/Aberrant_Sword_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a Sword. A strange blade imbued with energy...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Aberrant_Sword_Skin_%28Aberration%29.png')
    models.Skin.new(name='Alpha Raptor Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimPants_Alpha_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Alpha.PrimalItemSkin_SummerSwimPants_Alpha\'"',
                    url='https://ark.fandom.com/wiki/Alpha_Raptor_Swim_Bottom_Skin',
                    description="You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Become this summer's hottest predator with a Alpha Raptor swim suit.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Alpha_Raptor_Swim_Bottom_Skin.png')
    models.Skin.new(name='Alpha Raptor Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimShirt_Alpha_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Alpha.PrimalItemSkin_SummerSwimShirt_Alpha\'"',
                    url='https://ark.fandom.com/wiki/Alpha_Raptor_Swim_Top_Skin',
                    description="You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Like an Alpha Raptor, your fashion sense can't be tamed.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Alpha_Raptor_Swim_Top_Skin.png')
    models.Skin.new(name='Araneo Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_FE_Underwear_Araneo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Araneo.PrimalItemSkin_FE_Underwear_Araneo\'"',
                    url='https://ark.fandom.com/wiki/Araneo_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  A swim suit that clings to you like a spider.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Araneo_Swim_Bottom_Skin.png')
    models.Skin.new(name='Araneo Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_FE_SwimShirt_Araneo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Araneo.PrimalItemSkin_FE_SwimShirt_Araneo\'"',
                    url='https://ark.fandom.com/wiki/Araneo_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  A swim suit that clings to you like a spider.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/95/Araneo_Swim_Top_Skin.png')
    models.Skin.new(name='ARK Tester Hat Skin', stack_size=1, class_name='PrimalItem_Skin_Account_GameTester_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_GameTester.PrimalItem_Skin_Account_GameTester\'"',
                    url='https://ark.fandom.com/wiki/ARK_Tester_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a super-cool elite look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/ARK_Tester_Hat_Skin.png')
    models.Skin.new(name='Basilisk Ghost Costume', stack_size=1, class_name='PrimalItemCostume_GhostBasilisk_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostBasilisk.PrimalItemCostume_GhostBasilisk\'"',
                    url='https://ark.fandom.com/wiki/Basilisk_Ghost_Costume',
                    description='Use this spectrally spooky costume to get your Basilisk into the spirit of the season!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/Basilisk_Ghost_Costume.png')
    models.Skin.new(name='Birthday Suit Pants Skin', stack_size=1, class_name='PrimalItemSkin_BirthdayPants_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BirthdayPants.PrimalItemSkin_BirthdayPants\'"',
                    url='https://ark.fandom.com/wiki/Birthday_Suit_Pants_Skin',
                    description='You can use this to skin the appearance of pants. Provides a natural look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Birthday_Suit_Pants_Skin.png')
    models.Skin.new(name='Birthday Suit Shirt Skin', stack_size=1, class_name='PrimalItemSkin_BirthdayShirt_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BirthdayShirt.PrimalItemSkin_BirthdayShirt\'"',
                    url='https://ark.fandom.com/wiki/Birthday_Suit_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt. Provides a natural look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3b/Birthday_Suit_Shirt_Skin.png')
    models.Skin.new(name='Blue-Ball Winter Beanie Skin', stack_size=1, class_name='PrimalItemSkin_WW_WinterHatD_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatD.PrimalItemSkin_WW_WinterHatD\'"',
                    url='https://ark.fandom.com/wiki/Blue-Ball_Winter_Beanie_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Features a parade of dinos and an ARK patch.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Blue-Ball_Winter_Beanie_Skin.png')
    models.Skin.new(name='Bonnet Hat Skin', stack_size=1, class_name='PrimalItemSkin_TT_BonnetHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_BonnetHat.PrimalItemSkin_TT_BonnetHat\'"',
                    url='https://ark.fandom.com/wiki/Bonnet_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. A new hat for a new world.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Bonnet_Hat_Skin.png')
    models.Skin.new(name='Bow & Eros Skin', stack_size=1, class_name='PrimalItemSkin_CupidBow_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CupidBow.PrimalItemSkin_CupidBow\'"',
                    url='https://ark.fandom.com/wiki/Bow_%26_Eros_Skin',
                    description="You can use this to skin the appearance of a bow into Cupid's bow and arrows. Show your desire with an arrow through the heart.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0a/Bow_%26_Eros_Skin.png')
    models.Skin.new(name='Brachiosaurus Costume', stack_size=1, class_name='PrimalItemCostume_Brachiosaurus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemCostume_Brachiosaurus.PrimalItemCostume_Brachiosaurus\'"',
                    url='https://ark.fandom.com/wiki/Brachiosaurus_Costume',
                    description='This costume can be used to make your Brontosaurus look like a Brachiosaurus!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/44/Brachiosaurus_Costume.png')
    models.Skin.new(name='Bronto Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneSauro_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneSauro.PrimalItemCostume_BoneSauro\'"',
                    url='https://ark.fandom.com/wiki/Bronto_Bone_Costume',
                    description='This costume can be used to make your Bronto look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/24/Bronto_Bone_Costume.png')
    models.Skin.new(name='Bulbdog Ghost Costume', stack_size=1, class_name='PrimalItemCostume_GhostLanternPug_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostLanternPug.PrimalItemCostume_GhostLanternPug\'"',
                    url='https://ark.fandom.com/wiki/Bulbdog_Ghost_Costume',
                    description='Use this spectrally spooky costume to get your Bulbdog into the spirit of the season!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Bulbdog_Ghost_Costume.png')
    models.Skin.new(name='Bulbdog Mask Skin', stack_size=1, class_name='PrimalItemSkin_PugMask_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_PugMask.PrimalItemSkin_PugMask\'"',
                    url='https://ark.fandom.com/wiki/Bulbdog_Mask_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a friendly look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/30/Bulbdog_Mask_Skin_%28Aberration%29.png')
    models.Skin.new(name='Bulbdog-Print Shirt Skin', stack_size=1, class_name='PrimalItemSkin_HawaiianShirt_Bulbdog_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Bulbdog.PrimalItemSkin_HawaiianShirt_Bulbdog\'"',
                    url='https://ark.fandom.com/wiki/Bulbdog-Print_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt. Wear your favorite party animal!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/49/Bulbdog-Print_Shirt_Skin.png')
    models.Skin.new(name='Bunny Ears Skin', stack_size=1, class_name='PrimalItemSkin_BunnyHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_BunnyHat.PrimalItemSkin_BunnyHat\'"',
                    url='https://ark.fandom.com/wiki/Bunny_Ears_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a eggcellent look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Bunny_Ears_Skin.png')
    models.Skin.new(name='Candy Cane Club Skin', stack_size=1, class_name='PrimalItemSkin_CandyClub_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_CandyClub.PrimalItemSkin_CandyClub\'"',
                    url='https://ark.fandom.com/wiki/Candy_Cane_Club_Skin',
                    description='Useful for issuing sweet, sweet beatdowns!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Candy_Cane_Club_Skin.png')
    models.Skin.new(name="Captain's Hat Skin", stack_size=1, class_name='PrimalItemSkin_CaptainsHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CaptainsHat.PrimalItemSkin_CaptainsHat\'"',
                    url='https://ark.fandom.com/wiki/Captain%27s_Hat_Skin',
                    description='Found deep within the belly of a great white beast, this hat is all that remains of the last brave soul that tried to slay the creature.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Captain%27s_Hat_Skin.png')
    models.Skin.new(name='Carno Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneCarno_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneCarno.PrimalItemCostume_BoneCarno\'"',
                    url='https://ark.fandom.com/wiki/Carno_Bone_Costume',
                    description='This costume can be used to make your Carno look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Carno_Bone_Costume.png')
    models.Skin.new(name='Chieftan Hat Skin', stack_size=1, class_name='PrimalItemSkin_TurkeyHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TurkeyHat.PrimalItemSkin_TurkeyHat\'"',
                    url='https://ark.fandom.com/wiki/Chieftan_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or a hat. Provides a chiefly look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Chieftan_Hat_Skin.png')
    models.Skin.new(name='Chili Helmet Skin', stack_size=1, class_name='PrimalItemSkin_Chili_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Chili.PrimalItemSkin_Chili\'"',
                    url='https://ark.fandom.com/wiki/Chili_Helmet_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a helmet or hat.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b6/Chili_Helmet_Skin_%28Aberration%29.png')
    models.Skin.new(name='Chocolate Rabbit Club Skin', stack_size=1, class_name='PrimalItemSkin_Club_ChocolateRabbit_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Club_ChocolateRabbit.PrimalItemSkin_Club_ChocolateRabbit\'"',
                    url='https://ark.fandom.com/wiki/Chocolate_Rabbit_Club_Skin',
                    description='Useful for issuing sweet, sweet beatdowns!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d7/Chocolate_Rabbit_Club_Skin.png')
    models.Skin.new(name='Christmas Bola Skin', stack_size=1, class_name='PrimalItemSkin_WW_Xmas_Bola_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Xmas_Bola.PrimalItemSkin_WW_Xmas_Bola\'"',
                    url='https://ark.fandom.com/wiki/Christmas_Bola_Skin',
                    description="You can use this to skin a bola into ornaments connected with ribbon. There's no escaping your holiday cheer!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ab/Christmas_Bola_Skin.png')
    models.Skin.new(name='Clown Mask Skin', stack_size=1, class_name='PrimalItemSkin_ClownMask_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ClownMask.PrimalItemSkin_ClownMask\'"',
                    url='https://ark.fandom.com/wiki/Clown_Mask_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a jovial look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Clown_Mask_Skin.png')
    models.Skin.new(name='Corrupted Avatar Boots Skin', stack_size=1, class_name='PrimalItemSkin_Gen1AvatartBoots_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatartBoots.PrimalItemSkin_Gen1AvatartBoots\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Avatar_Boots_Skin_(Genesis:_Part_1)',
                    description='You can use this to skin the appearance of a pair of boots. A fractal look from the Genesis simulation.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/12/Corrupted_Avatar_Boots_Skin_%28Genesis_Part_1%29.png')
    models.Skin.new(name='Corrupted Avatar Gloves Skin', stack_size=1, class_name='PrimalItemSkin_Gen1AvatarGloves_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarGloves.PrimalItemSkin_Gen1AvatarGloves\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Avatar_Gloves_Skin_(Genesis:_Part_1)',
                    description='You can use this to skin the appearance of gloves. A fractal look from the Genesis simulation.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Corrupted_Avatar_Gloves_Skin_%28Genesis_Part_1%29.png')
    models.Skin.new(name='Corrupted Avatar Helmet Skin', stack_size=1, class_name='PrimalItemSkin_Gen1AvatarHelmet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarHelmet.PrimalItemSkin_Gen1AvatarHelmet\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Avatar_Helmet_Skin_(Genesis:_Part_1)',
                    description='You can use this to skin the appearance of a helmet or hat. A fractal look from the Genesis simulation.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7a/Corrupted_Avatar_Helmet_Skin_%28Genesis_Part_1%29.png')
    models.Skin.new(name='Corrupted Avatar Pants Skin', stack_size=1, class_name='PrimalItemSkin_Gen1AvatarPants_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarPants.PrimalItemSkin_Gen1AvatarPants\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Avatar_Pants_Skin_(Genesis:_Part_1)',
                    description='You can use this to skin the appearance of a pants. A fractal look from the Genesis simulation.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/Corrupted_Avatar_Pants_Skin_%28Genesis_Part_1%29.png')
    models.Skin.new(name='Corrupted Avatar Shirt Skin', stack_size=1, class_name='PrimalItemSkin_Gen1AvatarShirt_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarShirt.PrimalItemSkin_Gen1AvatarShirt\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Avatar_Shirt_Skin_(Genesis:_Part_1)',
                    description='You can use this to skin the appearance of chest armor. A fractal look from the Genesis simulation.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Corrupted_Avatar_Shirt_Skin_%28Genesis_Part_1%29.png')
    models.Skin.new(name='Corrupted Boots Skin', stack_size=1, class_name='PrimalItemSkin_CorruptedBoots_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedBoots.PrimalItemSkin_CorruptedBoots\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Boots_Skin',
                    description='You can use this to skin the appearance of boots. Provides a terrifying look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/95/Corrupted_Boots_Skin.png')
    models.Skin.new(name='Corrupted Chestpiece Skin', stack_size=1, class_name='PrimalItemSkin_CorruptedShirt_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedShirt.PrimalItemSkin_CorruptedShirt\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Chestpiece_Skin',
                    description='You can use this to skin the appearance of a shirt or chestpiece. Provides a terrifying look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/53/Corrupted_Chestpiece_Skin.png')
    models.Skin.new(name='Corrupted Gloves Skin', stack_size=1, class_name='PrimalItemSkin_CorruptedGloves_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedGloves.PrimalItemSkin_CorruptedGloves\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Gloves_Skin',
                    description='You can use this to skin the appearance of gloves. Provides a terrifying look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Corrupted_Gloves_Skin.png')
    models.Skin.new(name='Corrupted Helmet Skin', stack_size=1, class_name='PrimalItemSkin_CorruptedHelmet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedHelmet.PrimalItemSkin_CorruptedHelmet\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Helmet_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a terrifying look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Corrupted_Helmet_Skin.png')
    models.Skin.new(name='Corrupted Pants Skin', stack_size=1, class_name='PrimalItemSkin_CorruptedPants_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedPants.PrimalItemSkin_CorruptedPants\'"',
                    url='https://ark.fandom.com/wiki/Corrupted_Pants_Skin',
                    description='You can use this to skin the appearance of pants. Provides a terrifying look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Corrupted_Pants_Skin.png')
    models.Skin.new(name='Crab Fest Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimPants_CrabParty_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_CrabParty.PrimalItemSkin_SummerSwimPants_CrabParty\'"',
                    url='https://ark.fandom.com/wiki/Crab_Fest_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Warning—might pinch a little.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3e/Crab_Fest_Swim_Bottom_Skin.png')
    models.Skin.new(name='Crab Fest Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimShirt_CrabParty_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_CrabParty.PrimalItemSkin_SummerSwimShirt_CrabParty\'"',
                    url='https://ark.fandom.com/wiki/Crab_Fest_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Warning—might pinch a little.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c2/Crab_Fest_Swim_Top_Skin.png')
    models.Skin.new(name='Cupid Couture Bottom Skin', stack_size=1, class_name='PrimalItemSkin_ValentinePants_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ValentinePants.PrimalItemSkin_ValentinePants\'"',
                    url='https://ark.fandom.com/wiki/Cupid_Couture_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into a festive tutu for men or women. Love the way you look this season.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1d/Cupid_Couture_Bottom_Skin.png')
    models.Skin.new(name='Cupid Couture Top Skin', stack_size=1, class_name='PrimalItemSkin_ValentineShirt_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ValentineShirt.PrimalItemSkin_ValentineShirt\'"',
                    url='https://ark.fandom.com/wiki/Cupid_Couture_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a festive sash and wings for men or women. Love the way you look this season.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/59/Cupid_Couture_Top_Skin.png')
    models.Skin.new(name='Cute Dino Helmet Skin', stack_size=1, class_name='PrimalItemSkin_DinoCute_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoCute.PrimalItemSkin_DinoCute\'"',
                    url='https://ark.fandom.com/wiki/Cute_Dino_Helmet_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a helmet or hat.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/36/Cute_Dino_Helmet_Skin_%28Aberration%29.png')
    models.Skin.new(name='Decorative Ravager Saddle Skin', stack_size=1,
                    class_name='PrimalItemArmor_CavewolfPromoSaddle_C',
                    blueprint='"Blueprint\'/Game/Aberration/Dinos/CaveWolf/PrimalItemArmor_CavewolfPromoSaddle.PrimalItemArmor_CavewolfPromoSaddle\'"',
                    url='https://ark.fandom.com/wiki/Decorative_Ravager_Saddle_Skin_(Aberration)',
                    description='Place this on a Ravager Saddle to have a more aesthetically pleasing saddle.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Decorative_Ravager_Saddle_Skin_%28Aberration%29.png')
    models.Skin.new(name='Dilo Mask Skin', stack_size=1, class_name='PrimalItemSkin_DiloMask_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DiloMask.PrimalItemSkin_DiloMask\'"',
                    url='https://ark.fandom.com/wiki/Dilo_Mask_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a jovial look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Dilo_Mask_Skin.png')
    models.Skin.new(name='Dino Bunny Ears Skin', stack_size=1, class_name='PrimalItemSkin_DinoBunnyHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoBunnyHat.PrimalItemSkin_DinoBunnyHat\'"',
                    url='https://ark.fandom.com/wiki/Dino_Bunny_Ears_Skin',
                    description='You can use this to skin the appearance of a Saddle. Make your mount look eggcellent!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Bunny_Ears_Skin.png')
    models.Skin.new(name='Dino Easter Chick Hat', stack_size=1, class_name='PrimalItemSkin_DinoChickHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoChickHat.PrimalItemSkin_DinoChickHat\'"',
                    url='https://ark.fandom.com/wiki/Dino_Easter_Chick_Hat',
                    description='You can use this skin to change the appearance of your headgear. Equip for an adorable look resembling a baby spring chick!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Easter_Chick_Hat.png')
    models.Skin.new(name='Dino Easter Egg Hat', stack_size=1, class_name='PrimalItemSkin_DinoEasterEggHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoEasterEggHat.PrimalItemSkin_DinoEasterEggHat\'"',
                    url='https://ark.fandom.com/wiki/Dino_Easter_Egg_Hat',
                    description='You can use this to skin the appearance of your headgear. Provides a freshly hatched look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Easter_Egg_Hat.png')
    models.Skin.new(name='Dino Marshmallow Hat Skin', stack_size=1, class_name='PrimalItemSkin_DinoMarshmallowHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoMarshmallowHat.PrimalItemSkin_DinoMarshmallowHat\'"',
                    url='https://ark.fandom.com/wiki/Dino_Marshmallow_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Gives a fluffy look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Marshmallow_Hat_Skin.png')
    models.Skin.new(name='Dino Ornament Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_Underwear_DinoOrnaments_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_DinoOrnaments.PrimalItemSkin_WW_Underwear_DinoOrnaments\'"',
                    url='https://ark.fandom.com/wiki/Dino_Ornament_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. Give yourself that festive holiday look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Dino_Ornament_Swim_Bottom_Skin.png')
    models.Skin.new(name='Dino Ornament Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_SwimShirt_DinoOrnaments_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_DinoOrnaments.PrimalItemSkin_WW_SwimShirt_DinoOrnaments\'"',
                    url='https://ark.fandom.com/wiki/Dino_Ornament_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. Give yourself that festive holiday look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b8/Dino_Ornament_Swim_Top_Skin.png')
    models.Skin.new(name='Dino Party Hat Skin', stack_size=1, class_name='PrimalItemSkin_DinoPartyHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoPartyHat.PrimalItemSkin_DinoPartyHat\'"',
                    url='https://ark.fandom.com/wiki/Dino_Party_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a festive look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Party_Hat_Skin.png')
    models.Skin.new(name='Dino Santa Hat Skin', stack_size=1, class_name='PrimalItemSkin_DinoSantaHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoSantaHat.PrimalItemSkin_DinoSantaHat\'"',
                    url='https://ark.fandom.com/wiki/Dino_Santa_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a jolly look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d2/Santa_Hat_Skin.png')
    models.Skin.new(name='Dino Uncle Sam Hat Skin', stack_size=1, class_name='PrimalItemSkin_TopHat_Summer_Dino_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TopHat_Summer_Dino.PrimalItemSkin_TopHat_Summer_Dino\'"',
                    url='https://ark.fandom.com/wiki/Dino_Uncle_Sam_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat.  I want YOU to survive in star-spangled style.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Uncle_Sam_Hat_Skin.png')
    models.Skin.new(name='Dino Witch Hat Skin', stack_size=1, class_name='PrimalItemSkin_DinoWitchHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoWitchHat.PrimalItemSkin_DinoWitchHat\'"',
                    url='https://ark.fandom.com/wiki/Dino_Witch_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a bewitching look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Witch_Hat_Skin.png')
    models.Skin.new(name='Direwolf Ghost Costume', stack_size=1, class_name='PrimalItemCostume_GhostDirewolf_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostDirewolf.PrimalItemCostume_GhostDirewolf\'"',
                    url='https://ark.fandom.com/wiki/Direwolf_Ghost_Costume',
                    description='Use this spectrally spooky costume to get your Direwolf into the spirit of the season!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b9/Direwolf_Ghost_Costume.png')
    models.Skin.new(name='Dodo Pie Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_TT_SwimPants_DodoPie_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimPants_DodoPie.PrimalItemSkin_TT_SwimPants_DodoPie\'"',
                    url='https://ark.fandom.com/wiki/Dodo_Pie_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Bake me up before you dodo.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5d/Dodo_Pie_Swim_Bottom_Skin.png')
    models.Skin.new(name='Dodo Pie Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_TT_SwimShirt_DodoPie_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimShirt_DodoPie.PrimalItemSkin_TT_SwimShirt_DodoPie\'"',
                    url='https://ark.fandom.com/wiki/Dodo_Pie_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Bake me up before you dodo.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dc/Dodo_Pie_Swim_Top_Skin.png')
    models.Skin.new(name='Dodorex Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_SwimPants_Dodo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimPants_Dodo.PrimalItemSkin_SwimPants_Dodo\'"',
                    url='https://ark.fandom.com/wiki/Dodorex_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. Mama DodoRex says to wait thirty minutes to go swimming after dinner.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Dodorex_Swim_Bottom_Skin.png')
    models.Skin.new(name='Dodorex Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_SwimShirt_Dodo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimShirt_Dodo.PrimalItemSkin_SwimShirt_Dodo\'"',
                    url='https://ark.fandom.com/wiki/Dodorex_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. Mama DodoRex says to wait thirty minutes to go swimming after dinner.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Dodorex_Swim_Top_Skin.png')
    models.Skin.new(name='Dodorex-Print Shirt Skin', stack_size=1, class_name='PrimalItemSkin_HawaiianShirt_Dodo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Dodo.PrimalItemSkin_HawaiianShirt_Dodo\'"',
                    url='https://ark.fandom.com/wiki/Dodorex-Print_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt. Can you smell what Mama DodoRex is cooking?',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/86/Dodorex-Print_Shirt_Skin.png')
    models.Skin.new(name='DodoWyvern Mask Skin', stack_size=1, class_name='PrimalItemSkin_DodowyvernHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DodowyvernHat.PrimalItemSkin_DodowyvernHat\'"',
                    url='https://ark.fandom.com/wiki/DodoWyvern_Mask_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a hallowed look',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8e/DodoWyvern_Mask_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='E4 Remote Eggsplosives Skin', stack_size=1, class_name='PrimalItemSkin_EasterBasket_C4_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EasterBasket_C4.PrimalItemSkin_EasterBasket_C4\'"',
                    url='https://ark.fandom.com/wiki/E4_Remote_Eggsplosives_Skin',
                    description="You can use this to skin the appearance of C4 into an eggsplosive Easter basket. Nothing beats these eggs for poaching your enemies... it'll be over easy!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/78/E4_Remote_Eggsplosives_Skin.png')
    models.Skin.new(name='Easter Chick Hat', stack_size=1, class_name='PrimalItemSkin_EasterChick_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EasterChick.PrimalItemSkin_EasterChick\'"',
                    url='https://ark.fandom.com/wiki/Easter_Chick_Hat',
                    description='You can use this skin to change the appearance of your headgear. Equip for an adorable look resembling a baby spring chick!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Easter_Chick_Hat.png')
    models.Skin.new(name='Easter Egg Hat', stack_size=1, class_name='PrimalItemSkin_EasterEggHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EasterEggHat.PrimalItemSkin_EasterEggHat\'"',
                    url='https://ark.fandom.com/wiki/Easter_Egg_Hat',
                    description='You can use this to skin the appearance of your headgear. Provides a freshly hatched look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Easter_Egg_Hat.png')
    models.Skin.new(name='Easter Egghead Skin', stack_size=1, class_name='PrimalItemSkin_EggNestHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EggNestHat.PrimalItemSkin_EggNestHat\'"',
                    url='https://ark.fandom.com/wiki/Easter_Egghead_Skin',
                    description="You can use this to skin the appearance of a helmet or hat into a eggstraordinary chocolate egg nest. This bird's nest on your head will be no yolk!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Easter_Egghead_Skin.png')
    models.Skin.new(name='Fan Ballcap Skin', stack_size=1, class_name='PrimalItem_Skin_Account_WildcardAdmin',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_WildcardAdmin.PrimalItem_Skin_Account_WildcardAdmin\'"',
                    url='https://ark.fandom.com/wiki/Fan_Ballcap_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides an authoritative look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Fan_Ballcap_Skin.png')
    models.Skin.new(name='Federation Exo Boots Skin', stack_size=1, class_name='PrimalItemSkin_TekBoots_V2_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekBoots_V2.PrimalItemSkin_TekBoots_V2\'"',
                    url='https://ark.fandom.com/wiki/Federation_Exo_Boots_Skin_(Genesis:_Part_2)',
                    description='You can use this to skin the appearance of a pair of boots. Looks like a genuine pair of Terran Federation tek-reinforced exo-boots!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Federation_Exo_Boots_Skin_%28Genesis_Part_2%29.png')
    models.Skin.new(name='Federation Exo Helmet Skin', stack_size=1, class_name='PrimalItemSkin_TekHelmet_V2_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekHelmet_V2.PrimalItemSkin_TekHelmet_V2\'"',
                    url='https://ark.fandom.com/wiki/Federation_Exo_Helmet_Skin_(Genesis:_Part_2)',
                    description='You can use this to skin the appearance of a helmet or hat. Looks like a genuine Terran Federation tek-reinforced exo-helmet!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Federation_Exo_Helmet_Skin_%28Genesis_Part_2%29.png')
    models.Skin.new(name='Federation Exo-Chestpiece Skin', stack_size=1, class_name='PrimalItemSkin_TekShirt_V2_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekShirt_V2.PrimalItemSkin_TekShirt_V2\'"',
                    url='https://ark.fandom.com/wiki/Federation_Exo-Chestpiece_Skin_(Genesis:_Part_2)',
                    description='You can use this to skin the appearance of a shirt or chestpiece. Looks like a genuine pair of Terran Federation tek-reinforced exo-shirt!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Federation_Exo-Chestpiece_Skin_%28Genesis_Part_2%29.png')
    models.Skin.new(name='Federation Exo-Gloves Skin', stack_size=1, class_name='PrimalItemSkin_TekGloves_V2_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekGloves_V2.PrimalItemSkin_TekGloves_V2\'"',
                    url='https://ark.fandom.com/wiki/Federation_Exo-Gloves_Skin_(Genesis:_Part_2)',
                    description='You can use this to skin the appearance of gloves. Looks like a genuine pair of Terran Federation tek-reinforced Exo-Gloves!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d2/Federation_Exo-Gloves_Skin_%28Genesis_Part_2%29.png')
    models.Skin.new(name='Federation Exo-leggings Skin', stack_size=1, class_name='PrimalItemSkin_TekPants_V2_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekPants_V2.PrimalItemSkin_TekPants_V2\'"',
                    url='https://ark.fandom.com/wiki/Federation_Exo-leggings_Skin_(Genesis:_Part_2)',
                    description='You can use this to skin the appearance of leggings or pants. Looks like a genuine pair of Terran Federation tek-reinforced exo-pants!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b5/Federation_Exo-leggings_Skin_%28Genesis_Part_2%29.png')
    models.Skin.new(name='Felt Reindeer Antlers Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_ReindeerAntlersHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_ReindeerAntlersHat.PrimalItemSkin_WW_ReindeerAntlersHat\'"',
                    url='https://ark.fandom.com/wiki/Felt_Reindeer_Antlers_Skin',
                    description="You can use this to skin the appearance of a helmet or hat. Slay 'em with the reindeer look this holiday season.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Felt_Reindeer_Antlers_Skin.png')
    models.Skin.new(name='Fireworks Rocket Launcher Skin', stack_size=1,
                    class_name='PrimalItemSkin_RocketLauncherFireworks_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_RocketLauncherFireworks.PrimalItemSkin_RocketLauncherFireworks\'"',
                    url='https://ark.fandom.com/wiki/Fireworks_Rocket_Launcher_Skin',
                    description='Blow up your enemies with style using these colorful exploding fireworks!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/50/Fireworks_Rocket_Launcher_Skin.png')
    models.Skin.new(name='Fish Bite Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimPants_FishBite_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_FishBite.PrimalItemSkin_SummerSwimPants_FishBite\'"',
                    url='https://ark.fandom.com/wiki/Fish_Bite_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Watch out for those teeth!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Fish_Bite_Swim_Bottom_Skin.png')
    models.Skin.new(name='Fish Bite Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimShirt_FishBite_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_FishBite.PrimalItemSkin_SummerSwimShirt_FishBite\'"',
                    url='https://ark.fandom.com/wiki/Fish_Bite_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Watch out for those teeth!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a7/Fish_Bite_Swim_Top_Skin.png')
    models.Skin.new(name='Floral Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_SummerSwimPants_Flowers_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Flowers.PrimalItemSkin_SummerSwimPants_Flowers\'"',
                    url='https://ark.fandom.com/wiki/Floral_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Rule the beach this summer with the power of flowers.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Floral_Swim_Bottom_Skin.png')
    models.Skin.new(name='Floral Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_SummerSwimShirt_Flowers_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Flowers.PrimalItemSkin_SummerSwimShirt_Flowers\'"',
                    url='https://ark.fandom.com/wiki/Floral_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Blossom into the beach bod of your dreams.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Floral_Swim_Top_Skin.png')
    models.Skin.new(name='Flying Disc Skin', stack_size=1, class_name='PrimalItemSkin_Boomerang_Frisbee_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Boomerang_Frisbee.PrimalItemSkin_Boomerang_Frisbee\'"',
                    url='https://ark.fandom.com/wiki/Flying_Disc_Skin',
                    description='You can use this to skin the appearance of a Boomerang. Portable fun for the beach!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Flying_Disc_Skin.png')
    models.Skin.new(name='Gasbags-Print Shirt Skin', stack_size=1, class_name='PrimalItemSkin_HawaiianShirt_Gasbags_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Gasbags.PrimalItemSkin_HawaiianShirt_Gasbags\'"',
                    url='https://ark.fandom.com/wiki/Gasbags-Print_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt. Breezy summerwear.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Gasbags-Print_Shirt_Skin.png')
    models.Skin.new(name='Giga Bionic Costume', stack_size=1, class_name='PrimalItemCostume_BionicGigant_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicGigant.PrimalItemCostume_BionicGigant\'"',
                    url='https://ark.fandom.com/wiki/Giga_Bionic_Costume',
                    description='This costume can be used to make your Giga look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Giga_Bionic_Costume.png')
    models.Skin.new(name='Giga Poop Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimPants_Carno_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Carno.PrimalItemSkin_SummerSwimPants_Carno\'"',
                    url='https://ark.fandom.com/wiki/Giga_Poop_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  With swimwear this fashionable, no one minds you floating in their pool.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1a/Giga_Poop_Swim_Bottom_Skin.png')
    models.Skin.new(name='Giga Poop Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_SummerSwimShirt_Carno_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Carno.PrimalItemSkin_SummerSwimShirt_Carno\'"',
                    url='https://ark.fandom.com/wiki/Giga_Poop_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  The perfect look for those who want the beach to themselves.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Giga_Poop_Swim_Top_Skin.png')
    models.Skin.new(name='Giganotosaurus Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneGigant_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneGigant.PrimalItemCostume_BoneGigant\'"',
                    url='https://ark.fandom.com/wiki/Giganotosaurus_Bone_Costume',
                    description='This costume can be used to make your Giganotosaurus look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Giganotosaurus_Bone_Costume.png')
    models.Skin.new(name='Glider Suit', stack_size=1, class_name='PrimalItemArmor_Glider_C',
                    blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Armor/PrimalItemArmor_Glider.PrimalItemArmor_Glider\'"',
                    url='https://ark.fandom.com/wiki/Glider_Suit_(Aberration)',
                    description='When attached to a Chest Armor, the Glider Suit enables sailing through the air by double-tapping jump, while gaining speed by running and diving!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Glider_Suit_Skin_%28Aberration%29.png')
    models.Skin.new(name='Gray-Ball Winter Beanie Skin', stack_size=1, class_name='PrimalItemSkin_WW_WinterHatB_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatB.PrimalItemSkin_WW_WinterHatB\'"',
                    url='https://ark.fandom.com/wiki/Gray-Ball_Winter_Beanie_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Features big dinos and an ARK patch.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d7/Gray-Ball_Winter_Beanie_Skin.png')
    models.Skin.new(name='Green-Ball Winter Beanie Skin', stack_size=1, class_name='PrimalItemSkin_WW_WinterHatF_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatF.PrimalItemSkin_WW_WinterHatF\'"',
                    url='https://ark.fandom.com/wiki/Green-Ball_Winter_Beanie_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Features a parade of dinos and an ARK patch.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Green-Ball_Winter_Beanie_Skin.png')
    models.Skin.new(name='Grilling Spatula Skin', stack_size=1, class_name='PrimalItemSkin_Club_BBQSpatula_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Club_BBQSpatula.PrimalItemSkin_Club_BBQSpatula\'"',
                    url='https://ark.fandom.com/wiki/Grilling_Spatula_Skin',
                    description='You can use this to skin the appearance of a Club. How do you want your meat?',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Grilling_Spatula_Skin.png')
    models.Skin.new(name='Halo Headband Skin', stack_size=1, class_name='PrimalItemSkin_ValentineHaloHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ValentineHaloHat.PrimalItemSkin_ValentineHaloHat\'"',
                    url='https://ark.fandom.com/wiki/Halo_Headband_Skin',
                    description='You can use this to skin the appearance of a helmet or hat into a decorative halo headband. For those times you want to look good... really good.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Halo_Headband_Skin.png')
    models.Skin.new(name='Headless Costume Skin', stack_size=1, class_name='PrimalItemSkin_FE_HeadlessHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_HeadlessHat.PrimalItemSkin_FE_HeadlessHat\'"',
                    url='https://ark.fandom.com/wiki/Headless_Costume_Skin',
                    description="You can use this to skin the appearance of a helmet or hat. Because some days you just can't get a head.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2d/Headless_Costume_Skin.png')
    models.Skin.new(name='Heart-shaped Shield Skin', stack_size=1, class_name='PrimalItemSkin_Vday_Shield_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Vday_Shield.PrimalItemSkin_Vday_Shield\'"',
                    url='https://ark.fandom.com/wiki/Heart-shaped_Shield_Skin',
                    description='You can use this to skin the appearance of a shield. Protect yourself and the ones you love.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9d/Heart-shaped_Shield_Skin.png')
    models.Skin.new(name='Heart-shaped Sunglasses Skin', stack_size=1, class_name='PrimalItemSkin_SunGlasses_Vday_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SunGlasses_Vday.PrimalItemSkin_SunGlasses_Vday\'"',
                    url='https://ark.fandom.com/wiki/Heart-shaped_Sunglasses_Skin',
                    description='You can use this to skin the appearance of a Hat. No one will catch you staring.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Sunglasses_Skin.png')
    models.Skin.new(name='Hockey Mask Skin', stack_size=1, class_name='PrimalItemSkin_FE_ScaryFaceMask_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_ScaryFaceMask.PrimalItemSkin_FE_ScaryFaceMask\'"',
                    url='https://ark.fandom.com/wiki/Hockey_Mask_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. And by "hockey," we mean "chasing teenage campers."',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/20/Hockey_Mask_Skin.png')
    models.Skin.new(name='HomoDeus Boots Skin', stack_size=1, class_name='PrimalItemSkin_HomoDeusBoots_C',
                    blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusBoots.PrimalItemSkin_HomoDeusBoots\'"',
                    url='https://ark.fandom.com/wiki/HomoDeus_Boots_Skin_(Extinction)',
                    description='You can use this to skin the appearance of a pair of boots. Provides an enlightened look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/HomoDeus_Boots_Skin_%28Extinction%29.png')
    models.Skin.new(name='HomoDeus Gloves Skin', stack_size=1, class_name='PrimalItemSkin_HomoDeusGloves_C',
                    blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusGloves.PrimalItemSkin_HomoDeusGloves\'"',
                    url='https://ark.fandom.com/wiki/HomoDeus_Gloves_Skin_(Extinction)',
                    description='You can use this to skin the appearance of gloves. Provides an enlightened look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c4/HomoDeus_Gloves_Skin_%28Extinction%29.png')
    models.Skin.new(name='HomoDeus Helmet Skin', stack_size=1, class_name='PrimalItemSkin_HomoDeusHelmet_C',
                    blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusHelmet.PrimalItemSkin_HomoDeusHelmet\'"',
                    url='https://ark.fandom.com/wiki/HomoDeus_Helmet_Skin_(Extinction)',
                    description='You can use this to skin the appearance of a helmet or hat. Provides an enlightened look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/HomoDeus_Helmet_Skin_%28Extinction%29.png')
    models.Skin.new(name='HomoDeus Pants Skin', stack_size=1, class_name='PrimalItemSkin_HomoDeusPants_C',
                    blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusPants.PrimalItemSkin_HomoDeusPants\'"',
                    url='https://ark.fandom.com/wiki/HomoDeus_Pants_Skin_(Extinction)',
                    description='You can use this to skin the appearance of a pants. Provides an enlightened look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/90/HomoDeus_Pants_Skin_%28Extinction%29.png')
    models.Skin.new(name='HomoDeus Shirt Skin', stack_size=1, class_name='PrimalItemSkin_HomoDeusShirt_C',
                    blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusShirt.PrimalItemSkin_HomoDeusShirt\'"',
                    url='https://ark.fandom.com/wiki/HomoDeus_Shirt_Skin_(Extinction)',
                    description='You can use this to skin the appearance of chest armor. Provides an enlightened look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2f/HomoDeus_Shirt_Skin_%28Extinction%29.png')
    models.Skin.new(name='Ice Pop-Print Shirt Skin', stack_size=1, class_name='PrimalItemSkin_HawaiianShirt_Island_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Island.PrimalItemSkin_HawaiianShirt_Island\'"',
                    url='https://ark.fandom.com/wiki/Ice_Pop-Print_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt. Look cool and chill out.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/23/Ice_Pop-Print_Shirt_Skin.png')
    models.Skin.new(name='Ichthy Isles Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimPants_IslandRetreat_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_IslandRetreat.PrimalItemSkin_SummerSwimPants_IslandRetreat\'"',
                    url='https://ark.fandom.com/wiki/Ichthy_Isles_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Swim with the ichthyosaurs!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Ichthy_Isles_Swim_Bottom_Skin.png')
    models.Skin.new(name='Ichthy Isles Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_SummerSwimShirt_IslandRetreat_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_IslandRetreat.PrimalItemSkin_SummerSwimShirt_IslandRetreat\'"',
                    url='https://ark.fandom.com/wiki/Ichthy_Isles_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Swim with the ichthyosaurs!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Ichthy_Isles_Swim_Top_Skin.png')
    models.Skin.new(name='Jack-O-Lantern Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_FE_Underwear_Pumpkin_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Pumpkin.PrimalItemSkin_FE_Underwear_Pumpkin\'"',
                    url='https://ark.fandom.com/wiki/Jack-O-Lantern_Swim_Bottom_Skin',
                    description="You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women, and give 'em all pumpkin to talk about!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Jack-O-Lantern_Swim_Bottom_Skin.png')
    models.Skin.new(name='Jack-O-Lantern Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_FE_SwimShirt_Pumpkin_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Pumpkin.PrimalItemSkin_FE_SwimShirt_Pumpkin\'"',
                    url='https://ark.fandom.com/wiki/Jack-O-Lantern_Swim_Top_Skin',
                    description="You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women, and give 'em all pumpkin to talk about!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6a/Jack-O-Lantern_Swim_Top_Skin.png')
    models.Skin.new(name='Jack-O-Lantern-Print Shirt Skin', stack_size=1,
                    class_name='PrimalItemSkin_HawaiianShirt_Pumpkin_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Pumpkin.PrimalItemSkin_HawaiianShirt_Pumpkin\'"',
                    url='https://ark.fandom.com/wiki/Jack-O-Lantern-Print_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt. Let the gourd times roll!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/da/Jack-O-Lantern-Print_Shirt_Skin.png')
    models.Skin.new(name='Jerboa Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneJerboa_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneJerboa.PrimalItemCostume_BoneJerboa\'"',
                    url='https://ark.fandom.com/wiki/Jerboa_Bone_Costume',
                    description='This costume can be used to make your Jerboa look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Jerboa_Bone_Costume.png')
    models.Skin.new(name='Jerboa Wreath Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_Underwear_JerboaWreath_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_JerboaWreath.PrimalItemSkin_WW_Underwear_JerboaWreath\'"',
                    url='https://ark.fandom.com/wiki/Jerboa_Wreath_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. "Ears" wishing you happy holidays!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Jerboa_Wreath_Swim_Bottom_Skin.png')
    models.Skin.new(name='Jerboa Wreath Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_SwimShirt_JerboaWreath_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_JerboaWreath.PrimalItemSkin_WW_SwimShirt_JerboaWreath\'"',
                    url='https://ark.fandom.com/wiki/Jerboa_Wreath_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. "Ears" wishing you happy holidays!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Jerboa_Wreath_Swim_Top_Skin.png')
    models.Skin.new(name='Love Shackles Skin', stack_size=1, class_name='PrimalItemSkin_Vday_Handcuffs_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Vday_Handcuffs.PrimalItemSkin_Vday_Handcuffs\'"',
                    url='https://ark.fandom.com/wiki/Love_Shackles_Skin',
                    description='You can use this to skin the appearance of handcuffs into a fuzzy, pink variant. Don\'t let "the one" get away.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Love_Shackles_Skin.png')
    models.Skin.new(name='Manticore Boots Skin', stack_size=1, class_name='PrimalItemSkin_ManticoreBoots_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreBoots.PrimalItemSkin_ManticoreBoots\'"',
                    url='https://ark.fandom.com/wiki/Manticore_Boots_Skin',
                    description='You can use this to skin the appearance of boots. Provides a ferocious look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4a/Manticore_Boots_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Manticore Chestpiece Skin', stack_size=1, class_name='PrimalItemSkin_ManticoreShirt_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreShirt.PrimalItemSkin_ManticoreShirt\'"',
                    url='https://ark.fandom.com/wiki/Manticore_Chestpiece_Skin',
                    description='You can use this to skin the appearance of a shirt or chestpiece. Provides a ferocious look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Manticore_Chestpiece_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Manticore Gauntlets Skin', stack_size=1, class_name='PrimalItemSkin_ManticoreGloves_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreGloves.PrimalItemSkin_ManticoreGloves\'"',
                    url='https://ark.fandom.com/wiki/Manticore_Gauntlets_Skin',
                    description='You can use this to skin the appearance of gloves. Provides a ferocious look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7a/Manticore_Gauntlets_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Manticore Helmet Skin', stack_size=1, class_name='PrimalItemSkin_ManticoreHelmet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreHelmet.PrimalItemSkin_ManticoreHelmet\'"',
                    url='https://ark.fandom.com/wiki/Manticore_Helmet_Skin_(Scorched_Earth)',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a ferocious look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5c/Manticore_Helmet_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Manticore Leggings Skin', stack_size=1, class_name='PrimalItemSkin_ManticorePants_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticorePants.PrimalItemSkin_ManticorePants\'"',
                    url='https://ark.fandom.com/wiki/Manticore_Leggings_Skin',
                    description='You can use this to skin the appearance of leggings or pants. Provides a ferocious look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5e/Manticore_Leggings_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Manticore Shield Skin', stack_size=1, class_name='PrimalItemSkin_ManticoreShield_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreShield.PrimalItemSkin_ManticoreShield\'"',
                    url='https://ark.fandom.com/wiki/Manticore_Shield_Skin_(Scorched_Earth)',
                    description='You can use this to skin the appearance of a shield. Brought back from the far reaches of the Scorched Earth!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3e/Manticore_Shield_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Mantis Ghost Costume', stack_size=1, class_name='PrimalItemCostume_GhostMantis_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostMantis.PrimalItemCostume_GhostMantis\'"',
                    url='https://ark.fandom.com/wiki/Mantis_Ghost_Costume',
                    description='Use this spectrally spooky costume to get your Mantis into the spirit of the season!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ab/Mantis_Ghost_Costume.png')
    models.Skin.new(name='Marshmallow Hat Skin', stack_size=1, class_name='PrimalItemSkin_MarshmallowHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_MarshmallowHat.PrimalItemSkin_MarshmallowHat\'"',
                    url='https://ark.fandom.com/wiki/Marshmallow_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Gives a fluffy look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Marshmallow_Hat_Skin.png')
    models.Skin.new(name='Master Controller Helmet Skin', stack_size=1,
                    class_name='PrimalItemSkin_MasterControllerHelmet_C',
                    blueprint='"Blueprint\'/Game/Genesis/CoreBlueprints/Items/PrimalItemSkin_MasterControllerHelmet.PrimalItemSkin_MasterControllerHelmet\'"',
                    url='https://ark.fandom.com/wiki/Master_Controller_Helmet_Skin_(Genesis:_Part_1)',
                    description='You can use this to skin the appearance of a helmet or hat. Displays your dominance over the Master Controller.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Master_Controller_Helmet_Skin_%28Genesis_Part_1%29.png')
    models.Skin.new(name='Meat Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_TT_SwimPants_Meat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimPants_Meat.PrimalItemSkin_TT_SwimPants_Meat\'"',
                    url='https://ark.fandom.com/wiki/Meat_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  When fashion swimwear "meats" holiday attire.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/55/Meat_Swim_Bottom_Skin.png')
    models.Skin.new(name='Meat Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_TT_SwimShirt_Meat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimShirt_Meat.PrimalItemSkin_TT_SwimShirt_Meat\'"',
                    url='https://ark.fandom.com/wiki/Meat_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  When fashion swimwear "meats" holiday attire.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Meat_Swim_Top_Skin.png')
    models.Skin.new(name='Megaloceros Reindeer Costume', stack_size=1, class_name='PrimalItemCostume_ReindeerStag_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_ReindeerStag.PrimalItemCostume_ReindeerStag\'"',
                    url='https://ark.fandom.com/wiki/Megaloceros_Reindeer_Costume',
                    description='This costume can be used to make your Megaloceros look like a festive creature!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ce/Megaloceros_Reindeer_Costume.png')
    models.Skin.new(name='Mini-HLNA Skin', stack_size=1, class_name='PrimalItemSkin_MiniHLNA_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_MiniHLNA.PrimalItemSkin_MiniHLNA\'"',
                    url='https://ark.fandom.com/wiki/Mini-HLNA_Skin_(Genesis:_Part_1)',
                    description='HLNA can be equipped to the shield slot or attach HLNA to an existing shield.  Scanning the Elemental Disturbances in caves may reveal hidden information.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Mini-HLNA_Skin_%28Genesis_Part_1%29.png')
    models.Skin.new(name='Mosasaurus Bionic Costume', stack_size=1, class_name='PrimalItemCostume_BionicMosa_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicMosa.PrimalItemCostume_BionicMosa\'"',
                    url='https://ark.fandom.com/wiki/Mosasaurus_Bionic_Costume',
                    description='This costume can be used to make your Mosasaurus look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Mosasaurus_Bionic_Costume.png')
    models.Skin.new(name='Murder Turkey Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_SwimPants_MurderTurkey_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimPants_MurderTurkey.PrimalItemSkin_SwimPants_MurderTurkey\'"',
                    url='https://ark.fandom.com/wiki/Murder_Turkey_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Give thanks for another great day on the beach.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cc/Turkey_Swim_Bottom_Skin.png')
    models.Skin.new(name='Murder Turkey Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_SwimShirt_MurderTurkey_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimShirt_MurderTurkey.PrimalItemSkin_SwimShirt_MurderTurkey\'"',
                    url='https://ark.fandom.com/wiki/Murder_Turkey_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Give thanks for another great day on the beach.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Turkey_Swim_Top_Skin.png')
    models.Skin.new(name='Murder-Turkey-Print Shirt Skin', stack_size=1,
                    class_name='PrimalItemSkin_HawaiianShirt_MurderTurkey_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_MurderTurkey.PrimalItemSkin_HawaiianShirt_MurderTurkey\'"',
                    url='https://ark.fandom.com/wiki/Murder-Turkey-Print_Shirt_Skin',
                    description="You can use this to skin the appearance of a shirt. Looks like you're on the holiday menu this year!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Murder-Turkey-Print_Shirt_Skin.png')
    models.Skin.new(name='Nerdry Glasses Skin', stack_size=1, class_name='PrimalItemSkin_Glasses_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_Glasses.PrimalItemSkin_Glasses\'"',
                    url='https://ark.fandom.com/wiki/Nerdry_Glasses_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Slightly cracked and chewed, but still provides an intelligent look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Nerdry_Glasses_Skin.png')
    models.Skin.new(name='Noglin Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_WW_Underwear_Noglin_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_Noglin.PrimalItemSkin_WW_Underwear_Noglin\'"',
                    url='https://ark.fandom.com/wiki/Noglin_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. Unwrap a mind-bending surprise... A gift to make your head swim!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5b/Noglin_Swim_Bottom_Skin.png')
    models.Skin.new(name='Noglin Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_WW_SwimShirt_Noglin_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_Noglin.PrimalItemSkin_WW_SwimShirt_Noglin\'"',
                    url='https://ark.fandom.com/wiki/Noglin_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. Unwrap a mind-bending surprise... A gift to make your head swim!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c4/Noglin_Swim_Top_Skin.png')
    models.Skin.new(name='Nutcracker Slingshot Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_Nutcracker_Slingshot_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_WW_Nutcracker_Slingshot.PrimalItemSkin_WW_Nutcracker_Slingshot\'"',
                    url='https://ark.fandom.com/wiki/Nutcracker_Slingshot_Skin',
                    description='You can use this to skin a slingshot into shooting walnuts. Launch your very own snack attack!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Nutcracker_Slingshot_Skin.png')
    models.Skin.new(name='Onyc Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_FE_Underwear_Onyc_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Onyc.PrimalItemSkin_FE_Underwear_Onyc\'"',
                    url='https://ark.fandom.com/wiki/Onyc_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  A swim suit with lots of "bat"-itude..',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Onyc_Swim_Bottom_Skin.png')
    models.Skin.new(name='Onyc Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_FE_SwimShirt_Onyc_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Onyc.PrimalItemSkin_FE_SwimShirt_Onyc\'"',
                    url='https://ark.fandom.com/wiki/Onyc_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  A swim suit with lots of "bat"-itude..',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Onyc_Swim_Top_Skin.png')
    models.Skin.new(name='Otter Mask Skin', stack_size=1, class_name='PrimalItemSkin_OtterMask_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_OtterMask.PrimalItemSkin_OtterMask\'"',
                    url='https://ark.fandom.com/wiki/Otter_Mask_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a helmet or hat.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c1/Otter_Mask_Skin_%28Aberration%29.png')
    models.Skin.new(name='Parasaur Bionic Costume', stack_size=1, class_name='PrimalItemCostume_BionicParasaur_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicParasaur.PrimalItemCostume_BionicParasaur\'"',
                    url='https://ark.fandom.com/wiki/Parasaur_Bionic_Costume',
                    description='This costume can be used to make your Parasaur look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9b/Parasaur_Bionic_Costume.png')
    models.Skin.new(name='Party Hat Skin', stack_size=1, class_name='PrimalItemSkin_PartyHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_PartyHat.PrimalItemSkin_PartyHat\'"',
                    url='https://ark.fandom.com/wiki/Party_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a festive look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Party_Hat_Skin.png')
    models.Skin.new(name='Pilgrim Hat Skin', stack_size=1, class_name='PrimalItemSkin_TT_PilgrimHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_PilgrimHat.PrimalItemSkin_TT_PilgrimHat\'"',
                    url='https://ark.fandom.com/wiki/Pilgrim_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Because someone around here should show prudence and modesty.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Pilgrim_Hat_Skin.png')
    models.Skin.new(name='Pitchfork Skin', stack_size=1, class_name='PrimalItemSkin_TT_Pike_Pitchfork_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_Pike_Pitchfork.PrimalItemSkin_TT_Pike_Pitchfork\'"',
                    url='https://ark.fandom.com/wiki/Pitchfork_Skin',
                    description='You can use this to skin the appearance of a pike weapon into a pitchfork. There are four good reasons to listen to the survivor with a pitchfork...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/24/Pitchfork_Skin.png')
    models.Skin.new(name='Poglin Mask Skin', stack_size=1, class_name='PrimalItemSkin_PoglinHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_PoglinHat.PrimalItemSkin_PoglinHat\'"',
                    url='https://ark.fandom.com/wiki/Poglin_Mask_Skin_(Genesis:_Part_2)',
                    description="You can use this to skin the appearance of a helmet or hat. Drain everyone's will to live with this disturbing headwear!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Poglin_Mask_Skin_%28Genesis_Part_2%29.png')
    models.Skin.new(name='Procoptodon Bunny Costume', stack_size=1, class_name='PrimalItemCostume_ProcopBunny_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_ProcopBunny.PrimalItemCostume_ProcopBunny\'"',
                    url='https://ark.fandom.com/wiki/Procoptodon_Bunny_Costume',
                    description='This costume can be used to make your Procoptodon look eggcellent!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Procoptodon_Bunny_Costume.png')
    models.Skin.new(name='Purple-Ball Winter Beanie Skin', stack_size=1, class_name='PrimalItemSkin_WW_WinterHatC_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_WW_WinterHatC.PrimalItemSkin_WW_WinterHatC\'"',
                    url='https://ark.fandom.com/wiki/Purple-Ball_Winter_Beanie_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Features a dino design and the ARK logo.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4d/Purple-Ball_Winter_Beanie_Skin.png')
    models.Skin.new(name='Purple-Ball Winter Beanie Skin (Winter Wonderland 5)', stack_size=1,
                    class_name='PrimalItemSkin_WW_WinterHatE_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatE.PrimalItemSkin_WW_WinterHatE\'"',
                    url='https://ark.fandom.com/wiki/Purple-Ball_Winter_Beanie_Skin_(Winter_Wonderland_5)',
                    description='You can use this to skin the appearance of a helmet or hat. Features a parade of dinos and an ARK patch.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Purple-Ball_Winter_Beanie_Skin_%28Winter_Wonderland_5%29.png')
    models.Skin.new(name='Quetzal Bionic Costume', stack_size=1, class_name='PrimalItemCostume_BionicQuetzal_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicQuetzal.PrimalItemCostume_BionicQuetzal\'"',
                    url='https://ark.fandom.com/wiki/Quetzal_Bionic_Costume',
                    description='This costume can be used to make your Quetzal look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d1/Quetzal_Bionic_Costume.png')
    models.Skin.new(name="Raptor 'ARK: The Animated Series' Costume", stack_size=1,
                    class_name='PrimalItemCostume_AnimeRaptor_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_AnimeRaptor.PrimalItemCostume_AnimeRaptor\'"',
                    url='https://ark.fandom.com/wiki/Raptor_%27ARK:_The_Animated_Series%27_Costume',
                    description="This costume can be used to make your Raptor look like those in 'ARK: The Animated Series'!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Raptor_%27ARK_The_Animated_Series%27_Costume.png')
    models.Skin.new(name='Raptor Bionic Costume', stack_size=1, class_name='PrimalItemCostume_BionicRaptor_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicRaptor.PrimalItemCostume_BionicRaptor\'"',
                    url='https://ark.fandom.com/wiki/Raptor_Bionic_Costume',
                    description='This costume can be used to make your Raptor look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Raptor_Bionic_Costume.png')
    models.Skin.new(name='Quetzalcoatlus Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneQuetz_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneQuetz.PrimalItemCostume_BoneQuetz\'"',
                    url='https://ark.fandom.com/wiki/Quetzalcoatlus_Bone_Costume',
                    description='This costume can be used to make your Quetzalcoatlus look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Quetzalcoatlus_Bone_Costume.png')
    models.Skin.new(name='Raptor Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneRaptor_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneRaptor.PrimalItemCostume_BoneRaptor\'"',
                    url='https://ark.fandom.com/wiki/Raptor_Bone_Costume',
                    description='This costume can be used to make your Raptor look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Raptor_Bone_Costume.png')
    models.Skin.new(name='Reaper Ghost Costume', stack_size=1, class_name='PrimalItemCostume_GhostReaper_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostReaper.PrimalItemCostume_GhostReaper\'"',
                    url='https://ark.fandom.com/wiki/Reaper_Ghost_Costume',
                    description='Use this spectrally spooky costume to get your Reaper into the spirit of the season!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0c/Reaper_Ghost_Costume.png')
    models.Skin.new(name='Reaper Helmet Skin', stack_size=1, class_name='PrimalItemSkin_ReaperHelmet_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ReaperHelmet.PrimalItemSkin_ReaperHelmet\'"',
                    url='https://ark.fandom.com/wiki/Reaper_Helmet_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a helmet or hat. Provides an alien look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bc/Reaper_Helmet_Skin_%28Aberration%29.png')
    models.Skin.new(name='Reaper Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_FE_Underwear_Reaper_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Reaper.PrimalItemSkin_FE_Underwear_Reaper\'"',
                    url='https://ark.fandom.com/wiki/Reaper_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women, for a splashy burst of monstrous fun!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5f/Reaper_Swim_Bottom_Skin.png')
    models.Skin.new(name='Reaper Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_FE_SwimShirt_Reaper_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Reaper.PrimalItemSkin_FE_SwimShirt_Reaper\'"',
                    url='https://ark.fandom.com/wiki/Reaper_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women, for a splashy burst of monstrous fun!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/19/Reaper_Swim_Top_Skin.png')
    models.Skin.new(name='Reaper-Print Shirt Skin', stack_size=1, class_name='PrimalItemSkin_HawaiianShirt_Reaper_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Reaper.PrimalItemSkin_HawaiianShirt_Reaper\'"',
                    url='https://ark.fandom.com/wiki/Reaper-Print_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt, and represent your favorite party monster!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/71/Reaper-Print_Shirt_Skin.png')
    models.Skin.new(name='Red-Ball Winter Beanie Skin', stack_size=1, class_name='PrimalItemSkin_WW_WinterHatA_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_WW_WinterHatA.PrimalItemSkin_WW_WinterHatA\'"',
                    url='https://ark.fandom.com/wiki/Red-Ball_Winter_Beanie_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Features an assortment of dinos on parade.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Red-Ball_Winter_Beanie_Skin.png')
    models.Skin.new(name='Rex Bionic Costume', stack_size=1, class_name='null',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicRex.PrimalItemCostume_BionicRex\'"',
                    url='https://ark.fandom.com/wiki/Rex_Bionic_Costume',
                    description='This costume can be used to make your Rex look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f8/Rex_Bionic_Costume.png')
    models.Skin.new(name='Rex Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneRex_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneRex.PrimalItemCostume_BoneRex\'"',
                    url='https://ark.fandom.com/wiki/Rex_Bone_Costume',
                    description='This costume can be used to make your Rex look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Rex_Bone_Costume.png')
    models.Skin.new(name='Rex Ghost Costume', stack_size=1, class_name='PrimalItemCostume_GhostRex_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostRex.PrimalItemCostume_GhostRex\'"',
                    url='https://ark.fandom.com/wiki/Rex_Ghost_Costume',
                    description='Use this spectrally spooky costume to get your Rex into the spirit of the season!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f8/Rex_Ghost_Costume.png')
    models.Skin.new(name='Safari Hat Skin', stack_size=1, class_name='PrimalItemSkin_ExplorerHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ExplorerHat.PrimalItemSkin_ExplorerHat\'"',
                    url='https://ark.fandom.com/wiki/Safari_Hat_Skin_(Scorched_Earth)',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a heat-beating look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2a/Safari_Hat_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Santa Hat Skin', stack_size=1, class_name='PrimalItemSkin_SantaHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SantaHat.PrimalItemSkin_SantaHat\'"',
                    url='https://ark.fandom.com/wiki/Santa_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a jolly look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d2/Santa_Hat_Skin.png')
    models.Skin.new(name="Santiago's Axe Skin", stack_size=1, class_name='PrimalItemSkin_Hatchet_Santiago_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemSkin_Hatchet_Santiago.PrimalItemSkin_Hatchet_Santiago\'"',
                    url='https://ark.fandom.com/wiki/Santiago%27s_Axe_Skin',
                    description='You can use this to skin the appearance of a hatchet to look like the axe Santiago used in the ARK II trailer!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6f/Santiago%27s_Axe_Skin.png')
    models.Skin.new(name="Santiago's Spear Skin", stack_size=1, class_name='PrimalItemSkin_Spear_Santiago_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemSkin_Spear_Santiago.PrimalItemSkin_Spear_Santiago\'"',
                    url='https://ark.fandom.com/wiki/Santiago%27s_Spear_Skin',
                    description='You can use this to skin the appearance of a spear or pike to look like the spear Santiago used in the ARK II trailer!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8e/Santiago%27s_Spear_Skin.png')
    models.Skin.new(name='Scary Pumpkin Helmet Skin', stack_size=1, class_name='PrimalItemSkin_FE_PumpkinHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_PumpkinHat.PrimalItemSkin_FE_PumpkinHat\'"',
                    url='https://ark.fandom.com/wiki/Scary_Pumpkin_Helmet_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Good for Jack or Jill-o-Lanterns.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Scary_Pumpkin_Helmet_Skin.png')
    models.Skin.new(name='Scary Skull Helmet Skin', stack_size=1, class_name='PrimalItemSkin_ScarySkull_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ScarySkull.PrimalItemSkin_ScarySkull\'"',
                    url='https://ark.fandom.com/wiki/Scary_Skull_Helmet_Skin_(Aberration)',
                    description='You can use this to skin the appearance of a helmet or hat.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Scary_Skull_Helmet_Skin_%28Aberration%29.png')
    models.Skin.new(name='Scorched Spike Skin', stack_size=1, class_name='PrimalItemSkin_ScorchedSpear_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_ScorchedSpear.PrimalItemSkin_ScorchedSpear\'"',
                    url='https://ark.fandom.com/wiki/Scorched_Spike_Skin_(Scorched_Earth)',
                    description='Frighten your enemies with this imposing Spear or Pike skin!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/15/Scorched_Spike_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Scorched Sword Skin', stack_size=1, class_name='PrimalItemSkin_ScorchedSword_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_ScorchedSword.PrimalItemSkin_ScorchedSword\'"',
                    url='https://ark.fandom.com/wiki/Scorched_Sword_Skin_(Scorched_Earth)',
                    description='You can use this to skin the appearance of a Sword. A noble blade...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/80/Scorched_Sword_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Scorched Torch Skin', stack_size=1, class_name='PrimalItemSkin_TorchScorched_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TorchScorched.PrimalItemSkin_TorchScorched\'"',
                    url='https://ark.fandom.com/wiki/Scorched_Torch_Skin_(Scorched_Earth)',
                    description='Light up the desert night with this themed Torch skin!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Scorched_Torch_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Sea Life-Print Shirt Skin', stack_size=1,
                    class_name='PrimalItemSkin_HawaiianShirt_SeaStuff_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_SeaStuff.PrimalItemSkin_HawaiianShirt_SeaStuff\'"',
                    url='https://ark.fandom.com/wiki/Sea_Life-Print_Shirt_Skin',
                    description='You can use this to skin the appearance of a shirt. Make a splash at the luau!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Sea_Life-Print_Shirt_Skin.png')
    models.Skin.new(name='Snow Owl Ghost Costume', stack_size=1, class_name='PrimalItemCostume_GhostOwl_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostOwl.PrimalItemCostume_GhostOwl\'"',
                    url='https://ark.fandom.com/wiki/Snow_Owl_Ghost_Costume',
                    description='Use this spectrally spooky costume to get your Snow Owl into the spirit of the season!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/68/Snow_Owl_Ghost_Costume.png')
    models.Skin.new(name='Stego Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneStego_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneStego.PrimalItemCostume_BoneStego\'"',
                    url='https://ark.fandom.com/wiki/Stego_Bone_Costume',
                    description='This costume can be used to make your Stego look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/99/Stego_Bone_Costume.png')
    models.Skin.new(name='Stegosaurus Bionic Costume', stack_size=1, class_name='PrimalItemCostume_BionicStego_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicStego.PrimalItemCostume_BionicStego\'"',
                    url='https://ark.fandom.com/wiki/Stegosaurus_Bionic_Costume',
                    description='This costume can be used to make your Stegosaurus look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Stegosaurus_Bionic_Costume.png')
    models.Skin.new(name='Stygimoloch Costume', stack_size=1, class_name='PrimalItemCostume_Stygimoloch_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemCostume_Stygimoloch.PrimalItemCostume_Stygimoloch\'"',
                    url='https://ark.fandom.com/wiki/Stygimoloch_Costume',
                    description='This costume can be used to make your Pachycephalosaurus look like a Stygimoloch!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Stygimoloch_Costume.png')
    models.Skin.new(name='Styracosaurus Costume', stack_size=1, class_name='PrimalItemCostume_Styracosaurus_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemCostume_Styracosaurus.PrimalItemCostume_Styracosaurus\'"',
                    url='https://ark.fandom.com/wiki/Styracosaurus_Costume',
                    description='This costume can be used to make your Triceratops look like a Styracosaurus!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Styracosaurus_Costume.png')
    models.Skin.new(name='Sunglasses Skin', stack_size=1, class_name='PrimalItemSkin_SunGlasses_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SunGlasses.PrimalItemSkin_SunGlasses\'"',
                    url='https://ark.fandom.com/wiki/Sunglasses_Skin',
                    description='You can use this to skin the appearance of a Hat. No one will catch you staring.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Sunglasses_Skin.png')
    models.Skin.new(name='Sweet Spear Carrot Skin', stack_size=1, class_name='PrimalItemSkin_Spear_Carrot_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemSkin_Spear_Carrot.PrimalItemSkin_Spear_Carrot\'"',
                    url='https://ark.fandom.com/wiki/Sweet_Spear_Carrot_Skin',
                    description="You can use this to skin the appearance of a spear into a deliciously crunchy weapon. It may break, but you won't carrot all.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Sweet_Spear_Carrot_Skin.png')
    models.Skin.new(name='T-Rex Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_SummerSwimPants_Arthro_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Arthro.PrimalItemSkin_SummerSwimPants_Arthro\'"',
                    url='https://ark.fandom.com/wiki/T-Rex_Swim_Bottom_Skin',
                    description="You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  You'll be the terror of the beach with swimwear inspired by the T-Rex itself.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/T-Rex_Swim_Bottom_Skin.png')
    models.Skin.new(name='T-Rex Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_SummerSwimShirt_Arthro_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Arthro.PrimalItemSkin_SummerSwimShirt_Arthro\'"',
                    url='https://ark.fandom.com/wiki/T-Rex_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  With a beach look inspired by the T-Rex, no one will notice whether your arms are tiny or not.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/T-Rex_Swim_Top_Skin.png')
    models.Skin.new(name='Teddy Bear Grenades Skin', stack_size=1,
                    class_name='PrimalItemSkin_VDay_Grenade_ValentineBear_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_VDay_Grenade_ValentineBear.PrimalItemSkin_VDay_Grenade_ValentineBear\'"',
                    url='https://ark.fandom.com/wiki/Teddy_Bear_Grenades_Skin',
                    description="You can use this to skin the appearance of grenades to look like an unbearably cute toy. Deliver it to that special someone so they know you're thinking about them.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Teddy_Bear_Grenades_Skin.png')
    models.Skin.new(name='Thorny Dragon Vagabond Saddle Skin', stack_size=1,
                    class_name='PrimalItemArmor_SpineyLizardPromoSaddle_C',
                    blueprint='"Blueprint\'/Game/ScorchedEarth/Dinos/SpineyLizard/PrimalItemArmor_SpineyLizardPromoSaddle.PrimalItemArmor_SpineyLizardPromoSaddle\'"',
                    url='https://ark.fandom.com/wiki/Thorny_Dragon_Vagabond_Saddle_Skin_(Scorched_Earth)',
                    description='Use this on a Thorny Dragon saddle to ride in nomadic style.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/78/Thorny_Dragon_Vagabond_Saddle_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Top Hat Skin', stack_size=1, class_name='PrimalItemSkin_TopHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TopHat.PrimalItemSkin_TopHat\'"',
                    url='https://ark.fandom.com/wiki/Top_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a fancy look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/14/Top_Hat_Skin.png')
    models.Skin.new(name='Torch Sparkler Skin', stack_size=1, class_name='PrimalItemSkin_TorchSparkler_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TorchSparkler.PrimalItemSkin_TorchSparkler\'"',
                    url='https://ark.fandom.com/wiki/Torch_Sparkler_Skin',
                    description='Celebrate a holiday with sparkles! When applied to a Torch, can also be placed as a Wall Torch.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3e/Torch_Sparkler_Skin.png')
    models.Skin.new(name='Triceratops Bionic Costume', stack_size=1, class_name='PrimalItemCostume_BionicTrike_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicTrike.PrimalItemCostume_BionicTrike\'"',
                    url='https://ark.fandom.com/wiki/Triceratops_Bionic_Costume',
                    description='This costume can be used to make your Triceratops look like it was manufactured...',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Triceratops_Bionic_Costume.png')
    models.Skin.new(name='Trike Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneTrike_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneTrike.PrimalItemCostume_BoneTrike\'"',
                    url='https://ark.fandom.com/wiki/Trike_Bone_Costume',
                    description='This costume can be used to make your Trike look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Trike_Bone_Costume.png')
    models.Skin.new(name='Turkey Hat Skin', stack_size=1, class_name='PrimalItemSkin_TT_ActualTurkeyHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_ActualTurkeyHat.PrimalItemSkin_TT_ActualTurkeyHat\'"',
                    url='https://ark.fandom.com/wiki/Turkey_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. No one can call you a chicken.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Turkey_Hat_Skin.png')
    models.Skin.new(name='Turkey Leg Skin', stack_size=1, class_name='PrimalItemSkin_TT_Club_TurkeyLeg_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_Club_TurkeyLeg.PrimalItemSkin_TT_Club_TurkeyLeg\'"',
                    url='https://ark.fandom.com/wiki/Turkey_Leg_Skin',
                    description="You can use this to skin the appearance of a club. Hit 'em right in the dark meat!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Turkey_Leg_Skin.png')
    models.Skin.new(name='Turkey Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_TT_SwimPants_TurkeyBerry_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimPants_TurkeyBerry.PrimalItemSkin_TT_SwimPants_TurkeyBerry\'"',
                    url='https://ark.fandom.com/wiki/Turkey_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Give thanks for another great day on the beach.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cc/Turkey_Swim_Bottom_Skin.png')
    models.Skin.new(name='Turkey Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_TT_SwimShirt_TurkeyBerry_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimShirt_TurkeyBerry.PrimalItemSkin_TT_SwimShirt_TurkeyBerry\'"',
                    url='https://ark.fandom.com/wiki/Turkey_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Give thanks for another great day on the beach.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Turkey_Swim_Top_Skin.png')
    models.Skin.new(name='Ugly Bronto Sweater Skin', stack_size=1, class_name='PrimalItemSkin_WW_XmasSweaterBronto_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweaterBronto.PrimalItemSkin_WW_XmasSweaterBronto\'"',
                    url='https://ark.fandom.com/wiki/Ugly_Bronto_Sweater_Skin',
                    description='You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Brontos are good for hanging lights in high places.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d4/Ugly_Bronto_Sweater_Skin.png')
    models.Skin.new(name='Ugly Bulbdog Sweater Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_XmasSweater_Bulbdog_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweater_Bulbdog.PrimalItemSkin_WW_XmasSweater_Bulbdog\'"',
                    url='https://ark.fandom.com/wiki/Ugly_Bulbdog_Sweater_Skin',
                    description="You can use this to skin the appearance of a shirt into an ugly holiday sweater.  With a bulb so shiny, you'll even say it glows.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/15/Ugly_Bulbdog_Sweater_Skin.png')
    models.Skin.new(name='Ugly Carno Sweater Skin', stack_size=1, class_name='PrimalItemSkin_WW_XmasSweaterCarno_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweaterCarno.PrimalItemSkin_WW_XmasSweaterCarno\'"',
                    url='https://ark.fandom.com/wiki/Ugly_Carno_Sweater_Skin',
                    description='You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Holiday carols make some dinos hungry.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bb/Ugly_Carno_Sweater_Skin.png')
    models.Skin.new(name='Ugly Caroling Sweater Skin', stack_size=1,
                    class_name='PrimalItemSkin_WW_XmasSweater_Carolers_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweater_Carolers.PrimalItemSkin_WW_XmasSweater_Carolers\'"',
                    url='https://ark.fandom.com/wiki/Ugly_Caroling_Sweater_Skin',
                    description='You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Warm yourself up with this roaring choir.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/30/Ugly_Caroling_Sweater_Skin.png')
    models.Skin.new(name='Ugly Chibi Sweater Skin', stack_size=1, class_name='PrimalItemSkin_WW_XmasSweaterChibi_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweaterChibi.PrimalItemSkin_WW_XmasSweaterChibi\'"',
                    url='https://ark.fandom.com/wiki/Ugly_Chibi_Sweater_Skin',
                    description="You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Dinos make great gifts — when they're chibi-sized.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Ugly_Chibi_Sweater_Skin.png')
    models.Skin.new(name='Ugly Cornucopia Sweater Skin', stack_size=1, class_name='PrimalItemSkin_Sweater_Cornucopia_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Sweater_Cornucopia.PrimalItemSkin_Sweater_Cornucopia\'"',
                    url='https://ark.fandom.com/wiki/Ugly_Cornucopia_Sweater_Skin',
                    description="You can use this to skin the appearance of a shirt into an ugly holiday sweater. Harvest season means there's plenty to go around!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Ugly_Cornucopia_Sweater_Skin.png')
    models.Skin.new(name='Ugly T-Rex Sweater Skin', stack_size=1, class_name='PrimalItemSkin_WW_XmasSweater_Rex_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweater_Rex.PrimalItemSkin_WW_XmasSweater_Rex\'"',
                    url='https://ark.fandom.com/wiki/Ugly_T-Rex_Sweater_Skin',
                    description="You can use this to skin the appearance of a shirt into an ugly holiday sweater.  It's not the size of your arms, it's what you've got in the sack.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Ugly_T-Rex_Sweater_Skin.png')
    models.Skin.new(name='Ugly Trike Sweater Skin', stack_size=1, class_name='PrimalItemSkin_Sweater_Trike_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Sweater_Trike.PrimalItemSkin_Sweater_Trike\'"',
                    url='https://ark.fandom.com/wiki/Ugly_Trike_Sweater_Skin',
                    description='You can use this to skin the appearance of a shirt into an ugly holiday sweater. Fall foliage and triceratops, uh, plumage...?',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/26/Ugly_Trike_Sweater_Skin.png')
    models.Skin.new(name='Uncle Sam Hat Skin', stack_size=1, class_name='PrimalItemSkin_TopHat_Summer_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TopHat_Summer.PrimalItemSkin_TopHat_Summer\'"',
                    url='https://ark.fandom.com/wiki/Uncle_Sam_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat.  I want YOU to survive in star-spangled style.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Uncle_Sam_Hat_Skin.png')
    models.Skin.new(name='Vampire Dodo Swim Bottom Skin', stack_size=1,
                    class_name='PrimalItemSkin_FE_Underwear_VampireDodo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_VampireDodo.PrimalItemSkin_FE_Underwear_VampireDodo\'"',
                    url='https://ark.fandom.com/wiki/Vampire_Dodo_Swim_Bottom_Skin',
                    description="You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  A swim suit so cute it's scary -- but stay away from garlic.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4a/Vampire_Dodo_Swim_Bottom_Skin.png')
    models.Skin.new(name='Vampire Dodo Swim Top Skin', stack_size=1,
                    class_name='PrimalItemSkin_FE_SwimShirt_VampireDodo_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_VampireDodo.PrimalItemSkin_FE_SwimShirt_VampireDodo\'"',
                    url='https://ark.fandom.com/wiki/Vampire_Dodo_Swim_Top_Skin',
                    description="You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  A swim suit so cute it's scary -- but stay away from garlic.",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Vampire_Dodo_Swim_Top_Skin.png')
    models.Skin.new(name='Vampire Eyes Skin', stack_size=1, class_name='PrimalItemSkin_VampireEyes_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_VampireEyes.PrimalItemSkin_VampireEyes\'"',
                    url='https://ark.fandom.com/wiki/Vampire_Eyes_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a bloodthirsty look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Vampire_Eyes_Skin.png')
    models.Skin.new(name='Water Soaker Skin', stack_size=1, class_name='PrimalItemSkin_Flamethrower_SuperSoaker_C',
                    blueprint='"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Flamethrower_SuperSoaker.PrimalItemSkin_Flamethrower_SuperSoaker\'"',
                    url='https://ark.fandom.com/wiki/Water_Soaker_Skin',
                    description="You can use this to skin the appearance of a Flamethrower. Someone's getting wet!",
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Water_Soaker_Skin.png')
    models.Skin.new(name='Werewolf Mask Skin', stack_size=1, class_name='PrimalItemSkin_WerewolfHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WerewolfHat.PrimalItemSkin_WerewolfHat\'"',
                    url='https://ark.fandom.com/wiki/Werewolf_Mask_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a wolfish look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/33/Werewolf_Mask_Skin.png')
    models.Skin.new(name='Witch Hat Skin', stack_size=1, class_name='PrimalItemSkin_WitchHat_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WitchHat.PrimalItemSkin_WitchHat\'"',
                    url='https://ark.fandom.com/wiki/Witch_Hat_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a bewitching look.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Witch_Hat_Skin.png')
    models.Skin.new(name='Wizard Ballcap Skin', stack_size=1, class_name='PrimalItem_Skin_Account_DevKitMaster_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_DevKitMaster.PrimalItem_Skin_Account_DevKitMaster\'"',
                    url='https://ark.fandom.com/wiki/Wizard_Ballcap_Skin',
                    description='You can use this to skin the appearance of a helmet or hat. Provides a mystical look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3b/Wizard_Ballcap_Skin.png')
    models.Skin.new(name='Wyvern Bone Costume', stack_size=1, class_name='PrimalItemCostume_BoneWyvern_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneWyvern.PrimalItemCostume_BoneWyvern\'"',
                    url='https://ark.fandom.com/wiki/Wyvern_Bone_Costume',
                    description='This costume can be used to make your Wyvern look just like a skeleton! Spoopy!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Wyvern_Bone_Costume.png')
    models.Skin.new(name='Wyvern Gloves Skin', stack_size=1, class_name='PrimalItemSkin_WyvernGloves_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WyvernGloves.PrimalItemSkin_WyvernGloves\'"',
                    url='https://ark.fandom.com/wiki/Wyvern_Gloves_Skin_(Scorched_Earth)',
                    description='You can use this to skin the appearance of gloves. Provides a dangerous look!',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Wyvern_Gloves_Skin_%28Scorched_Earth%29.png')
    models.Skin.new(name='Yeti Swim Bottom Skin', stack_size=1, class_name='PrimalItemSkin_WW_Underwear_Yeti_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_Yeti.PrimalItemSkin_WW_Underwear_Yeti\'"',
                    url='https://ark.fandom.com/wiki/Yeti_Swim_Bottom_Skin',
                    description='You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. For swimmers with abominable taste in swimwear.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Yeti_Swim_Bottom_Skin.png')
    models.Skin.new(name='Yeti Swim Top Skin', stack_size=1, class_name='PrimalItemSkin_WW_SwimShirt_Yeti_C',
                    blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_Yeti.PrimalItemSkin_WW_SwimShirt_Yeti\'"',
                    url='https://ark.fandom.com/wiki/Yeti_Swim_Top_Skin',
                    description='You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. For swimmers with abominable taste in swimwear.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Yeti_Swim_Top_Skin.png')
    models.Skin.new(name='Zip-Line Motor Attachment Skin', stack_size=1, class_name='PrimalItemArmor_ZiplineMotor_C',
                    blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Armor/PrimalItemArmor_ZiplineMotor.PrimalItemArmor_ZiplineMotor\'"',
                    url='https://ark.fandom.com/wiki/Zip-Line_Motor_Attachment_Skin_(Aberration)',
                    description='Equip onto pants and combine with Gasoline to power yourself up a Zip-Line.',
                    image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Zip-Line_Motor_Attachment_Skin_%28Aberration%29.png')
    items = [item.to_json() for item in models.Skin.all()]
    print(items)


def seed():
    items = [
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemArmor_HideHelmetAlt.PrimalItemArmor_HideHelmetAlt\'"',
            'name': 'Hunter Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/45/Hunter_Hat_Skin.png',
            'class_name': 'PrimalItemArmor_HideHelmetAlt_C', 'id': 277,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides an adventurous look!',
            'url': 'https://ark.fandom.com/wiki/Hunter_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemArmor_RexSaddle_StompedGlasses.PrimalItemArmor_RexSaddle_StompedGlasses\'"',
            'name': 'Rex Stomped Glasses Saddle Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Rex_Stomped_Glasses_Saddle_Skin.png',
            'class_name': 'PrimalItemArmor_RexSaddle_StompedGlasses_C', 'id': 278,
            'description': 'Welcome to ARK! Equip a Tyrannosaurus with this to live the high life.',
            'url': 'https://ark.fandom.com/wiki/Rex_Stomped_Glasses_Saddle_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemArmor_ParaSaddle_Launch.PrimalItemArmor_ParaSaddle_Launch\'"',
            'name': 'Parasaur Stylish Saddle Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Parasaur_Stylish_Saddle_Skin.png',
            'class_name': 'PrimalItemArmor_ParaSaddle_Launch_C', 'id': 289,
            'description': 'Use this on a Parasaurolophus saddle to ride in posh style.',
            'url': 'https://ark.fandom.com/wiki/Parasaur_Stylish_Saddle_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BoneHelmet.PrimalItemSkin_BoneHelmet\'"',
            'name': 'Rex Bone Helmet', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Rex_Bone_Helmet_Skin.png',
            'class_name': 'PrimalItemSkin_BoneHelmet_C', 'id': 295,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a scary look!',
            'url': 'https://ark.fandom.com/wiki/Rex_Bone_Helmet'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoSpecs.PrimalItemSkin_DinoSpecs\'"',
            'name': 'Dino Glasses Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Dino_Glasses_Skin.png',
            'class_name': 'PrimalItemSkin_DinoSpecs_C', 'id': 304,
            'description': 'You can use this to skin the appearance of a Saddle. Make your mount look distinguished and well-read with these impressive looking hand-made spectacles.',
            'url': 'https://ark.fandom.com/wiki/Dino_Glasses_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_FlaregunFireworks.PrimalItemSkin_FlaregunFireworks\'"',
            'name': 'Fireworks Flaregun Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Fireworks_Flaregun_Skin.png',
            'class_name': 'PrimalItemSkin_FlaregunFireworks_C', 'id': 320,
            'description': 'Light up the sky with these independent fireworks!',
            'url': 'https://ark.fandom.com/wiki/Fireworks_Flaregun_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TrikeSkullHelmet.PrimalItemSkin_TrikeSkullHelmet\'"',
            'name': 'Trike Bone Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Trike_Bone_Helmet_Skin.png',
            'class_name': 'PrimalItemSkin_TrikeSkullHelmet_C', 'id': 381,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a noble look.',
            'url': 'https://ark.fandom.com/wiki/Trike_Bone_Helmet_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DodorexMask.PrimalItemSkin_DodorexMask\'"',
            'name': 'DodoRex Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d8/DodoRex_Mask_Skin.png',
            'class_name': 'PrimalItemSkin_DodorexMask_C', 'id': 432,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a hallowed look',
            'url': 'https://ark.fandom.com/wiki/DodoRex_Mask_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_PartyRex.PrimalItemSkin_ChibiDino_PartyRex\'"',
            'name': 'Chibi Party Rex', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Chibi-Rex.png',
            'class_name': 'PrimalItemSkin_ChibiDino_PartyRex_C', 'id': 433,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi_Party_Rex'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Allosaurus.PrimalItemSkin_ChibiDino_Allosaurus\'"',
            'name': 'Chibi-Allosaurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/69/Chibi-Allosaurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Allosaurus_C', 'id': 434,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Allosaurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Ammonite.PrimalItemSkin_ChibiDino_Ammonite\'"',
            'name': 'Chibi-Ammonite', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Chibi-Ammonite.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Ammonite_C', 'id': 435,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Ammonite'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Ankylosaurus.PrimalItemSkin_ChibiDino_Ankylosaurus\'"',
            'name': 'Chibi-Ankylosaurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/49/Chibi-Ankylosaurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Ankylosaurus_C', 'id': 436,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Ankylosaurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Argent.PrimalItemSkin_ChibiDino_Argent\'"',
            'name': 'Chibi-Argentavis', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Chibi-Argentavis.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Argent_C', 'id': 437,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Argentavis'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Astrocetus.PrimalItemSkin_ChibiDino_Astrocetus\'"',
            'name': 'Chibi-Astrocetus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Chibi-Astrocetus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Astrocetus_C', 'id': 438,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Astrocetus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Baryonyx.PrimalItemSkin_ChibiDino_Baryonyx\'"',
            'name': 'Chibi-Baryonyx', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0c/Chibi-Baryonyx.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Baryonyx_C', 'id': 439,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Baryonyx'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Basilisk.PrimalItemSkin_ChibiDino_Basilisk\'"',
            'name': 'Chibi-Basilisk', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Chibi-Basilisk.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Basilisk_C', 'id': 440,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Basilisk'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Beelzebufo.PrimalItemSkin_ChibiDino_Beelzebufo\'"',
            'name': 'Chibi-Beelzebufo', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ac/Chibi-Beelzebufo.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Beelzebufo_C', 'id': 441,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Beelzebufo'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_BogSpider.PrimalItemSkin_ChibiDino_BogSpider\'"',
            'name': 'Chibi-Bloodstalker', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/67/Chibi-Bloodstalker.png',
            'class_name': 'PrimalItemSkin_ChibiDino_BogSpider_C', 'id': 442,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Bloodstalker'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_OtterBonnet.PrimalItemSkin_ChibiDino_OtterBonnet\'"',
            'name': 'Chibi-Bonnet Otter', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Chibi-Bonnet_Otter.png',
            'class_name': 'PrimalItemSkin_ChibiDino_OtterBonnet_C', 'id': 443,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Bonnet_Otter'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bronto.PrimalItemSkin_ChibiDino_Bronto\'"',
            'name': 'Chibi-Brontosaurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Chibi-Brontosaurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Bronto_C', 'id': 444,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Brontosaurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_BroodMother.PrimalItemSkin_ChibiDino_BroodMother\'"',
            'name': 'Chibi-Broodmother', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/51/Chibi-Broodmother.png',
            'class_name': 'PrimalItemSkin_ChibiDino_BroodMother_C', 'id': 445,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Broodmother'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bulbdog.PrimalItemSkin_ChibiDino_Bulbdog\'"',
            'name': 'Chibi-Bulbdog', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Chibi-Bulbdog.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Bulbdog_C', 'id': 446,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Bulbdog'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bunny.PrimalItemSkin_ChibiDino_Bunny\'"',
            'name': 'Chibi-Bunny', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ed/Chibi-Bunny.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Bunny_C', 'id': 447,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Bunny'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Carbonemys.PrimalItemSkin_ChibiDino_Carbonemys\'"',
            'name': 'Chibi-Carbonemys', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Chibi-Carbonemys.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Carbonemys_C', 'id': 448,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Carbonemys'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Carnotaurus.PrimalItemSkin_ChibiDino_Carnotaurus\'"',
            'name': 'Chibi-Carno', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Chibi-Carno.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Carnotaurus_C', 'id': 449,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Carno'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Castroides.PrimalItemSkin_ChibiDino_Castroides\'"',
            'name': 'Chibi-Castroides', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/78/Chibi-Castroides.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Castroides_C', 'id': 450,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Castroides'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Cnidaria.PrimalItemSkin_ChibiDino_Cnidaria\'"',
            'name': 'Chibi-Cnidaria', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Chibi-Cnidaria.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Cnidaria_C', 'id': 451,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Cnidaria'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_WyvernCrystal.PrimalItemSkin_ChibiDino_WyvernCrystal\'"',
            'name': 'Chibi-Crystal Wyvern', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Chibi-Crystal_Wyvern.png',
            'class_name': 'PrimalItemSkin_ChibiDino_WyvernCrystal_C', 'id': 452,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Crystal_Wyvern'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Daeodon.PrimalItemSkin_ChibiDino_Daeodon\'"',
            'name': 'Chibi-Daeodon', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6e/Chibi-Daeodon.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Daeodon_C', 'id': 453,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Daeodon'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Direbear.PrimalItemSkin_ChibiDino_Direbear\'"',
            'name': 'Chibi-Direbear', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Direbear.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Direbear_C', 'id': 454,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Direbear'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Direwolf.PrimalItemSkin_ChibiDino_Direwolf\'"',
            'name': 'Chibi-Direwolf', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/12/Chibi-Direwolf.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Direwolf_C', 'id': 455,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Direwolf'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Dodo.PrimalItemSkin_ChibiDino_Dodo\'"',
            'name': 'Chibi-Dodo', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d1/Chibi-Dodo.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Dodo_C', 'id': 456,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Dodo'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Doedicurus.PrimalItemSkin_ChibiDino_Doedicurus\'"',
            'name': 'Chibi-Doedicurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Chibi-Doedicurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Doedicurus_C', 'id': 457,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Doedicurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Dunkleo.PrimalItemSkin_ChibiDino_Dunkleo\'"',
            'name': 'Chibi-Dunkleosteus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/87/Chibi-Dunkleosteus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Dunkleo_C', 'id': 458,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Dunkleosteus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Enforcer.PrimalItemSkin_ChibiDino_Enforcer\'"',
            'name': 'Chibi-Enforcer', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Chibi-Enforcer.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Enforcer_C', 'id': 459,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Enforcer'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Equus.PrimalItemSkin_ChibiDino_Equus\'"',
            'name': 'Chibi-Equus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/35/Chibi-Equus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Equus_C', 'id': 460,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Equus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Featherlight.PrimalItemSkin_ChibiDino_Featherlight\'"',
            'name': 'Chibi-Featherlight', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Chibi-Featherlight.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Featherlight_C', 'id': 461,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Featherlight'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Shapeshifter_Large.PrimalItemSkin_ChibiDino_Shapeshifter_Large\'"',
            'name': 'Chibi-Ferox (Large)', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ce/Chibi-Ferox_%28Large%29.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Shapeshifter_Large_C', 'id': 462,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Ferox_(Large)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Shapeshifter_Small.PrimalItemSkin_ChibiDino_Shapeshifter_Small\'"',
            'name': 'Chibi-Ferox (Small)', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Chibi-Ferox_%28Small%29.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Shapeshifter_Small_C', 'id': 463,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Ferox_(Small)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_GachaClaus.PrimalItemSkin_ChibiDino_GachaClaus\'"',
            'name': 'Chibi-Gacha Claus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/af/Chibi-Gacha_Claus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_GachaClaus_C', 'id': 464,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Gacha_Claus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gasbag.PrimalItemSkin_ChibiDino_Gasbag\'"',
            'name': 'Chibi-Gasbag', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5d/Chibi-Gasbag.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Gasbag_C', 'id': 465,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Gasbag'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gigant.PrimalItemSkin_ChibiDino_Gigant\'"',
            'name': 'Chibi-Giganotosaurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Chibi-Giganotosaurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Gigant_C', 'id': 466,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Giganotosaurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gigantopithecus.PrimalItemSkin_ChibiDino_Gigantopithecus\'"',
            'name': 'Chibi-Gigantopithecus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Chibi-Gigantopithecus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Gigantopithecus_C', 'id': 467,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Gigantopithecus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Glowtail.PrimalItemSkin_ChibiDino_Glowtail\'"',
            'name': 'Chibi-Glowtail', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/de/Chibi-Glowtail.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Glowtail_C', 'id': 468,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Glowtail'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Griffin.PrimalItemSkin_ChibiDino_Griffin\'"',
            'name': 'Chibi-Griffin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Chibi-Griffin.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Griffin_C', 'id': 469,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Griffin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Iguanodon.PrimalItemSkin_ChibiDino_Iguanodon\'"',
            'name': 'Chibi-Iguanodon', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Chibi-Iguanodon.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Iguanodon_C', 'id': 470,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Iguanodon'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Karkinos.PrimalItemSkin_ChibiDino_Karkinos\'"',
            'name': 'Chibi-Karkinos', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Chibi-Karkinos.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Karkinos_C', 'id': 471,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Karkinos'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Kentrosaurus.PrimalItemSkin_ChibiDino_Kentrosaurus\'"',
            'name': 'Chibi-Kentrosaurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Chibi-Kentrosaurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Kentrosaurus_C', 'id': 472,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Kentrosaurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Cherufe.PrimalItemSkin_ChibiDino_Cherufe\'"',
            'name': 'Chibi-Magmasaur', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Chibi-Magmasaur.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Cherufe_C', 'id': 473,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Magmasaur'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Mammoth.PrimalItemSkin_ChibiDino_Mammoth\'"',
            'name': 'Chibi-Mammoth', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/32/Chibi-Mammoth.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Mammoth_C', 'id': 474,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Mammoth'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Managarmr.PrimalItemSkin_ChibiDino_Managarmr\'"',
            'name': 'Chibi-Managarmr', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1c/Chibi-Managarmr.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Managarmr_C', 'id': 475,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Managarmr'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Manta.PrimalItemSkin_ChibiDino_Manta\'"',
            'name': 'Chibi-Manta', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/33/Chibi-Manta.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Manta_C', 'id': 476,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Manta'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Mantis.PrimalItemSkin_ChibiDino_Mantis\'"',
            'name': 'Chibi-Mantis', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Chibi-Mantis.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Mantis_C', 'id': 477,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Mantis'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megalania.PrimalItemSkin_ChibiDino_Megalania\'"',
            'name': 'Chibi-Megalania', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/93/Chibi-Megalania.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Megalania_C', 'id': 478,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Megalania'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megaloceros.PrimalItemSkin_ChibiDino_Megaloceros\'"',
            'name': 'Chibi-Megaloceros', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ac/Chibi-Megaloceros.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Megaloceros_C', 'id': 479,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Megaloceros'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megalodon.PrimalItemSkin_ChibiDino_Megalodon\'"',
            'name': 'Chibi-Megalodon', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Chibi-Megalodon.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Megalodon_C', 'id': 480,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Megalodon'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Megatherium.PrimalItemSkin_ChibiDino_Megatherium\'"',
            'name': 'Chibi-Megatherium', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d1/Chibi-Megatherium.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Megatherium_C', 'id': 481,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Megatherium'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Mesopithecus.PrimalItemSkin_ChibiDino_Mesopithecus\'"',
            'name': 'Chibi-Mesopithecus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Chibi-Mesopithecus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Mesopithecus_C', 'id': 482,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Mesopithecus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Moschops.PrimalItemSkin_ChibiDino_Moschops\'"',
            'name': 'Chibi-Moschops', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Chibi-Moschops.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Moschops_C', 'id': 483,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Moschops'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Otter.PrimalItemSkin_ChibiDino_Otter\'"',
            'name': 'Chibi-Otter', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/99/Chibi-Otter.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Otter_C', 'id': 484,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Otter'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Oviraptor.PrimalItemSkin_ChibiDino_Oviraptor\'"',
            'name': 'Chibi-Oviraptor', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Chibi-Oviraptor.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Oviraptor_C', 'id': 485,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Oviraptor'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Sheep.PrimalItemSkin_ChibiDino_Sheep\'"',
            'name': 'Chibi-Ovis', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6e/Chibi-Ovis.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Sheep_C', 'id': 486,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Ovis'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Paraceratherium.PrimalItemSkin_ChibiDino_Paraceratherium\'"',
            'name': 'Chibi-Paraceratherium', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Chibi-Paraceratherium.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Paraceratherium_C', 'id': 487,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Paraceratherium'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Parasaur.PrimalItemSkin_ChibiDino_Parasaur\'"',
            'name': 'Chibi-Parasaur', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Parasaur.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Parasaur_C', 'id': 488,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Parasaur'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Phiomia.PrimalItemSkin_ChibiDino_Phiomia\'"',
            'name': 'Chibi-Phiomia', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Chibi-Phiomia.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Phiomia_C', 'id': 489,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Phiomia'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Phoenix.PrimalItemSkin_ChibiDino_Phoenix\'"',
            'name': 'Chibi-Phoenix', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6c/Chibi-Phoenix.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Phoenix_C', 'id': 490,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Phoenix'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Plesiosaur.PrimalItemSkin_ChibiDino_Plesiosaur\'"',
            'name': 'Chibi-Plesiosaur', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fe/Chibi-Plesiosaur.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Plesiosaur_C', 'id': 491,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Plesiosaur'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Procoptodon.PrimalItemSkin_ChibiDino_Procoptodon\'"',
            'name': 'Chibi-Procoptodon', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Chibi-Procoptodon.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Procoptodon_C', 'id': 492,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Procoptodon'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Pteranodon.PrimalItemSkin_ChibiDino_Pteranodon\'"',
            'name': 'Chibi-Pteranodon', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2d/Chibi-Pteranodon.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Pteranodon_C', 'id': 493,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Pteranodon'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Pulmonoscorpius.PrimalItemSkin_ChibiDino_Pulmonoscorpius\'"',
            'name': 'Chibi-Pulmonoscorpius', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Chibi-Pulmonoscorpius.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Pulmonoscorpius_C', 'id': 494,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Pulmonoscorpius'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Quetzal.PrimalItemSkin_ChibiDino_Quetzal\'"',
            'name': 'Chibi-Quetzal', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Chibi-Quetzal.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Quetzal_C', 'id': 495,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Quetzal'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Raptor.PrimalItemSkin_ChibiDino_Raptor\'"',
            'name': 'Chibi-Raptor', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Chibi-Raptor.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Raptor_C', 'id': 496,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Raptor'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Reaper.PrimalItemSkin_ChibiDino_Reaper\'"',
            'name': 'Chibi-Reaper', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b5/Chibi-Reaper.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Reaper_C', 'id': 497,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Reaper'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Reindeer.PrimalItemSkin_ChibiDino_Reindeer\'"',
            'name': 'Chibi-Reindeer', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Chibi-Reindeer.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Reindeer_C', 'id': 498,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Reindeer'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Rex.PrimalItemSkin_ChibiDino_Rex\'"',
            'name': 'Chibi-Rex', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/96/Chibi-Rex.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Rex_C', 'id': 499,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Rex'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_WoollyRhino.PrimalItemSkin_ChibiDino_WoollyRhino\'"',
            'name': 'Chibi-Rhino', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/83/Chibi-Rhino.png',
            'class_name': 'PrimalItemSkin_ChibiDino_WoollyRhino_C', 'id': 500,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Rhino'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_RockDrake.PrimalItemSkin_ChibiDino_RockDrake\'"',
            'name': 'Chibi-Rock Drake', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ca/Chibi-Rock_Drake.png',
            'class_name': 'PrimalItemSkin_ChibiDino_RockDrake_C', 'id': 501,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Rock_Drake'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_RockGolem.PrimalItemSkin_ChibiDino_RockGolem\'"',
            'name': 'Chibi-Rock Golem', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Chibi-Rock_Golem.png',
            'class_name': 'PrimalItemSkin_ChibiDino_RockGolem_C', 'id': 502,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Rock_Golem'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_MoleRat.PrimalItemSkin_ChibiDino_MoleRat\'"',
            'name': 'Chibi-Rollrat', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/44/Chibi-Rollrat.png',
            'class_name': 'PrimalItemSkin_ChibiDino_MoleRat_C', 'id': 503,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Rollrat'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Saber.PrimalItemSkin_ChibiDino_Saber\'"',
            'name': 'Chibi-Sabertooth', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Chibi-Sabertooth.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Saber_C', 'id': 504,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Sabertooth'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Sarco.PrimalItemSkin_ChibiDino_Sarco\'"',
            'name': 'Chibi-Sarco', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/60/Chibi-Sarco.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Sarco_C', 'id': 505,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Sarco'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Seeker.PrimalItemSkin_ChibiDino_Seeker\'"',
            'name': 'Chibi-Seeker', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Chibi-Seeker.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Seeker_C', 'id': 506,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Seeker'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_ShadowMane.PrimalItemSkin_ChibiDino_ShadowMane\'"',
            'name': 'Chibi-Shadowmane', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Chibi-Shadowmane_%28Genesis_Part_2%29.png',
            'class_name': 'PrimalItemSkin_ChibiDino_ShadowMane_C', 'id': 507,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Shadowmane_(Genesis:_Part_2)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Shinehorn.PrimalItemSkin_ChibiDino_Shinehorn\'"',
            'name': 'Chibi-Shinehorn', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/70/Chibi-Shinehorn.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Shinehorn_C', 'id': 508,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Shinehorn'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Bronto_Bone.PrimalItemSkin_ChibiDino_Bronto_Bone\'"',
            'name': 'Chibi-Skeletal Brontosaurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Skeletal_Brontosaurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Bronto_Bone_C', 'id': 509,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Brontosaurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Carnotaurus_Bone.PrimalItemSkin_ChibiDino_Carnotaurus_Bone\'"',
            'name': 'Chibi-Skeletal Carno', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Chibi-Skeletal_Carno.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Carnotaurus_Bone_C', 'id': 510,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Carno'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Gigant_Bone.PrimalItemSkin_ChibiDino_Gigant_Bone\'"',
            'name': 'Chibi-Skeletal Giganotosaurus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5a/Chibi-Skeletal_Giganotosaurus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Gigant_Bone_C', 'id': 511,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Giganotosaurus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Jerboa_Bone.PrimalItemSkin_ChibiDino_Jerboa_Bone\'"',
            'name': 'Chibi-Skeletal Jerboa', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/06/Chibi-Skeletal_Jerboa.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Jerboa_Bone_C', 'id': 512,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Jerboa'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Quetzal_Bone.PrimalItemSkin_ChibiDino_Quetzal_Bone\'"',
            'name': 'Chibi-Skeletal Quetzal', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Chibi-Skeletal_Quetzal.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Quetzal_Bone_C', 'id': 513,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Quetzal'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Raptor_Bone.PrimalItemSkin_ChibiDino_Raptor_Bone\'"',
            'name': 'Chibi-Skeletal Raptor', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Chibi-Skeletal_Raptor.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Raptor_Bone_C', 'id': 514,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Raptor'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Rex_Bone.PrimalItemSkin_ChibiDino_Rex_Bone\'"',
            'name': 'Chibi-Skeletal Rex', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/ba/Chibi-Skeletal_Rex.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Rex_Bone_C', 'id': 515,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Rex'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Stego_Bone.PrimalItemSkin_ChibiDino_Stego_Bone\'"',
            'name': 'Chibi-Skeletal Stego', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/ff/Chibi-Skeletal_Stego.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Stego_Bone_C', 'id': 516,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Stego'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Trike_Bone.PrimalItemSkin_ChibiDino_Trike_Bone\'"',
            'name': 'Chibi-Skeletal Trike', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/10/Chibi-Skeletal_Trike.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Trike_Bone_C', 'id': 517,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Trike'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Wyvern_Bone.PrimalItemSkin_ChibiDino_Wyvern_Bone\'"',
            'name': 'Chibi-Skeletal Wyvern', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Chibi-Skeletal_Wyvern.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Wyvern_Bone_C', 'id': 518,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Skeletal_Wyvern'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_SnowOwl.PrimalItemSkin_ChibiDino_SnowOwl\'"',
            'name': 'Chibi-Snow Owl', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Chibi-Snow_Owl.png',
            'class_name': 'PrimalItemSkin_ChibiDino_SnowOwl_C', 'id': 519,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Snow_Owl'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Spino.PrimalItemSkin_ChibiDino_Spino\'"',
            'name': 'Chibi-Spino', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Chibi-Spino.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Spino_C', 'id': 520,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Spino'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Stego.PrimalItemSkin_ChibiDino_Stego\'"',
            'name': 'Chibi-Stego', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Chibi-Stego.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Stego_C', 'id': 521,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Stego'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Tapejara.PrimalItemSkin_ChibiDino_Tapejara\'"',
            'name': 'Chibi-Tapejara', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Chibi-Tapejara.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Tapejara_C', 'id': 522,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Tapejara'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_TerrorBird.PrimalItemSkin_ChibiDino_TerrorBird\'"',
            'name': 'Chibi-Terror Bird', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ad/Chibi-Terror_Bird.png',
            'class_name': 'PrimalItemSkin_ChibiDino_TerrorBird_C', 'id': 523,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Terror_Bird'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Therizino.PrimalItemSkin_ChibiDino_Therizino\'"',
            'name': 'Chibi-Therizino', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cb/Chibi-Therizino.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Therizino_C', 'id': 524,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Therizino'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Thylacoleo.PrimalItemSkin_ChibiDino_Thylacoleo\'"',
            'name': 'Chibi-Thylacoleo', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6d/Chibi-Thylacoleo.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Thylacoleo_C', 'id': 525,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Thylacoleo'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Trike.PrimalItemSkin_ChibiDino_Trike\'"',
            'name': 'Chibi-Trike', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/16/Chibi-Trike.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Trike_C', 'id': 526,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Trike'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Troodon.PrimalItemSkin_ChibiDino_Troodon\'"',
            'name': 'Chibi-Troodon', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/53/Chibi-Troodon.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Troodon_C', 'id': 527,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Troodon'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Tropeognathus.PrimalItemSkin_ChibiDino_Tropeognathus\'"',
            'name': 'Chibi-Tropeognathus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Chibi-Tropeognathus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Tropeognathus_C', 'id': 528,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Tropeognathus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Tuso.PrimalItemSkin_ChibiDino_Tuso\'"',
            'name': 'Chibi-Tusoteuthis', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Chibi-Tusoteuthis.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Tuso_C', 'id': 529,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Tusoteuthis'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Unicorn.PrimalItemSkin_ChibiDino_Unicorn\'"',
            'name': 'Chibi-Unicorn', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Chibi-Unicorn.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Unicorn_C', 'id': 530,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Unicorn'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Velonasaur.PrimalItemSkin_ChibiDino_Velonasaur\'"',
            'name': 'Chibi-Velonasaur', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Chibi-Velonasaur.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Velonasaur_C', 'id': 531,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Velonasaur'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Wyvern.PrimalItemSkin_ChibiDino_Wyvern\'"',
            'name': 'Chibi-Wyvern', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Chibi-Wyvern.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Wyvern_C', 'id': 532,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Wyvern'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Yutyrannus.PrimalItemSkin_ChibiDino_Yutyrannus\'"',
            'name': 'Chibi-Yutyrannus', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/82/Chibi-Yutyrannus.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Yutyrannus_C', 'id': 533,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Yutyrannus'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Wyvern_Zombie.PrimalItemSkin_ChibiDino_Wyvern_Zombie\'"',
            'name': 'Chibi-Zombie Wyvern', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/03/Chibi-Skeletal_Wyvern.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Wyvern_Zombie_C', 'id': 534,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Chibi-Zombie_Wyvern'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Pairosaurs_VDay.PrimalItemSkin_ChibiDino_Pairosaurs_VDay\'"',
            'name': 'Pair-o-Saurs Chibi', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Pair-o-Saurs_Chibi.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Pairosaurs_VDay_C', 'id': 535,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Pair-o-Saurs_Chibi'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_Titano.PrimalItemSkin_ChibiDino_Titano\'"',
            'name': 'Teeny Tiny Titano', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7b/Teeny_Tiny_Titano.png',
            'class_name': 'PrimalItemSkin_ChibiDino_Titano_C', 'id': 536,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/Teeny_Tiny_Titano'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/ChibiDinos/PrimalItemSkin_ChibiDino_TophatKairuku.PrimalItemSkin_ChibiDino_TophatKairuku\'"',
            'name': 'White-Collar Kairuku', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/11/White-Collar_Kairuku_Chibi.png',
            'class_name': 'PrimalItemSkin_ChibiDino_TophatKairuku_C', 'id': 537,
            'description': 'Earn XP from Alpha creature kills when equipped, to increase its level and earn additional max-levels for your Survivor!',
            'url': 'https://ark.fandom.com/wiki/White-Collar_Kairuku'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_AberrationHelmet.PrimalItemSkin_AberrationHelmet\'"',
            'name': 'Aberrant Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Aberrant_Helmet_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_AberrationHelmet_C', 'id': 538,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a ferocious look!',
            'url': 'https://ark.fandom.com/wiki/Aberrant_Helmet_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_AberrationSword.PrimalItemSkin_AberrationSword\'"',
            'name': 'Aberrant Sword Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Aberrant_Sword_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_AberrationSword_C', 'id': 539,
            'description': 'You can use this to skin the appearance of a Sword. A strange blade imbued with energy...',
            'url': 'https://ark.fandom.com/wiki/Aberrant_Sword_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Alpha.PrimalItemSkin_SummerSwimPants_Alpha\'"',
            'name': 'Alpha Raptor Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Alpha_Raptor_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimPants_Alpha_C', 'id': 540,
            'description': "You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Become this summer's hottest predator with a Alpha Raptor swim suit.",
            'url': 'https://ark.fandom.com/wiki/Alpha_Raptor_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Alpha.PrimalItemSkin_SummerSwimShirt_Alpha\'"',
            'name': 'Alpha Raptor Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Alpha_Raptor_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimShirt_Alpha_C', 'id': 541,
            'description': "You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Like an Alpha Raptor, your fashion sense can't be tamed.",
            'url': 'https://ark.fandom.com/wiki/Alpha_Raptor_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Araneo.PrimalItemSkin_FE_Underwear_Araneo\'"',
            'name': 'Araneo Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Araneo_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_FE_Underwear_Araneo_C', 'id': 542,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  A swim suit that clings to you like a spider.',
            'url': 'https://ark.fandom.com/wiki/Araneo_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Araneo.PrimalItemSkin_FE_SwimShirt_Araneo\'"',
            'name': 'Araneo Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/95/Araneo_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_FE_SwimShirt_Araneo_C', 'id': 543,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  A swim suit that clings to you like a spider.',
            'url': 'https://ark.fandom.com/wiki/Araneo_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_GameTester.PrimalItem_Skin_Account_GameTester\'"',
            'name': 'ARK Tester Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/ARK_Tester_Hat_Skin.png',
            'class_name': 'PrimalItem_Skin_Account_GameTester_C', 'id': 544,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a super-cool elite look!',
            'url': 'https://ark.fandom.com/wiki/ARK_Tester_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostBasilisk.PrimalItemCostume_GhostBasilisk\'"',
            'name': 'Basilisk Ghost Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/Basilisk_Ghost_Costume.png',
            'class_name': 'PrimalItemCostume_GhostBasilisk_C', 'id': 545,
            'description': 'Use this spectrally spooky costume to get your Basilisk into the spirit of the season!',
            'url': 'https://ark.fandom.com/wiki/Basilisk_Ghost_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BirthdayPants.PrimalItemSkin_BirthdayPants\'"',
            'name': 'Birthday Suit Pants Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Birthday_Suit_Pants_Skin.png',
            'class_name': 'PrimalItemSkin_BirthdayPants_C', 'id': 546,
            'description': 'You can use this to skin the appearance of pants. Provides a natural look!',
            'url': 'https://ark.fandom.com/wiki/Birthday_Suit_Pants_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_BirthdayShirt.PrimalItemSkin_BirthdayShirt\'"',
            'name': 'Birthday Suit Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3b/Birthday_Suit_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_BirthdayShirt_C', 'id': 547,
            'description': 'You can use this to skin the appearance of a shirt. Provides a natural look!',
            'url': 'https://ark.fandom.com/wiki/Birthday_Suit_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatD.PrimalItemSkin_WW_WinterHatD\'"',
            'name': 'Blue-Ball Winter Beanie Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Blue-Ball_Winter_Beanie_Skin.png',
            'class_name': 'PrimalItemSkin_WW_WinterHatD_C', 'id': 548,
            'description': 'You can use this to skin the appearance of a helmet or hat. Features a parade of dinos and an ARK patch.',
            'url': 'https://ark.fandom.com/wiki/Blue-Ball_Winter_Beanie_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_BonnetHat.PrimalItemSkin_TT_BonnetHat\'"',
            'name': 'Bonnet Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Bonnet_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_TT_BonnetHat_C', 'id': 549,
            'description': 'You can use this to skin the appearance of a helmet or hat. A new hat for a new world.',
            'url': 'https://ark.fandom.com/wiki/Bonnet_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CupidBow.PrimalItemSkin_CupidBow\'"',
            'name': 'Bow & Eros Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0a/Bow_%26_Eros_Skin.png',
            'class_name': 'PrimalItemSkin_CupidBow_C', 'id': 550,
            'description': "You can use this to skin the appearance of a bow into Cupid's bow and arrows. Show your desire with an arrow through the heart.",
            'url': 'https://ark.fandom.com/wiki/Bow_%26_Eros_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemCostume_Brachiosaurus.PrimalItemCostume_Brachiosaurus\'"',
            'name': 'Brachiosaurus Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/44/Brachiosaurus_Costume.png',
            'class_name': 'PrimalItemCostume_Brachiosaurus_C', 'id': 551,
            'description': 'This costume can be used to make your Brontosaurus look like a Brachiosaurus!',
            'url': 'https://ark.fandom.com/wiki/Brachiosaurus_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneSauro.PrimalItemCostume_BoneSauro\'"',
            'name': 'Bronto Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/24/Bronto_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneSauro_C', 'id': 552,
            'description': 'This costume can be used to make your Bronto look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Bronto_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostLanternPug.PrimalItemCostume_GhostLanternPug\'"',
            'name': 'Bulbdog Ghost Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Bulbdog_Ghost_Costume.png',
            'class_name': 'PrimalItemCostume_GhostLanternPug_C', 'id': 553,
            'description': 'Use this spectrally spooky costume to get your Bulbdog into the spirit of the season!',
            'url': 'https://ark.fandom.com/wiki/Bulbdog_Ghost_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_PugMask.PrimalItemSkin_PugMask\'"',
            'name': 'Bulbdog Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/30/Bulbdog_Mask_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_PugMask_C', 'id': 554,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a friendly look!',
            'url': 'https://ark.fandom.com/wiki/Bulbdog_Mask_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Bulbdog.PrimalItemSkin_HawaiianShirt_Bulbdog\'"',
            'name': 'Bulbdog-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/49/Bulbdog-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_Bulbdog_C', 'id': 555,
            'description': 'You can use this to skin the appearance of a shirt. Wear your favorite party animal!',
            'url': 'https://ark.fandom.com/wiki/Bulbdog-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_BunnyHat.PrimalItemSkin_BunnyHat\'"',
            'name': 'Bunny Ears Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Bunny_Ears_Skin.png',
            'class_name': 'PrimalItemSkin_BunnyHat_C', 'id': 556,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a eggcellent look.',
            'url': 'https://ark.fandom.com/wiki/Bunny_Ears_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_CandyClub.PrimalItemSkin_CandyClub\'"',
            'name': 'Candy Cane Club Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/df/Candy_Cane_Club_Skin.png',
            'class_name': 'PrimalItemSkin_CandyClub_C', 'id': 557,
            'description': 'Useful for issuing sweet, sweet beatdowns!',
            'url': 'https://ark.fandom.com/wiki/Candy_Cane_Club_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CaptainsHat.PrimalItemSkin_CaptainsHat\'"',
            'name': "Captain's Hat Skin", 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/Captain%27s_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_CaptainsHat_C', 'id': 558,
            'description': 'Found deep within the belly of a great white beast, this hat is all that remains of the last brave soul that tried to slay the creature.',
            'url': 'https://ark.fandom.com/wiki/Captain%27s_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneCarno.PrimalItemCostume_BoneCarno\'"',
            'name': 'Carno Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Carno_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneCarno_C', 'id': 559,
            'description': 'This costume can be used to make your Carno look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Carno_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TurkeyHat.PrimalItemSkin_TurkeyHat\'"',
            'name': 'Chieftan Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Chieftan_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_TurkeyHat_C', 'id': 560,
            'description': 'You can use this to skin the appearance of a helmet or a hat. Provides a chiefly look.',
            'url': 'https://ark.fandom.com/wiki/Chieftan_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Chili.PrimalItemSkin_Chili\'"',
            'name': 'Chili Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b6/Chili_Helmet_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_Chili_C', 'id': 561,
            'description': 'You can use this to skin the appearance of a helmet or hat.',
            'url': 'https://ark.fandom.com/wiki/Chili_Helmet_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Club_ChocolateRabbit.PrimalItemSkin_Club_ChocolateRabbit\'"',
            'name': 'Chocolate Rabbit Club Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d7/Chocolate_Rabbit_Club_Skin.png',
            'class_name': 'PrimalItemSkin_Club_ChocolateRabbit_C', 'id': 562,
            'description': 'Useful for issuing sweet, sweet beatdowns!',
            'url': 'https://ark.fandom.com/wiki/Chocolate_Rabbit_Club_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Xmas_Bola.PrimalItemSkin_WW_Xmas_Bola\'"',
            'name': 'Christmas Bola Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ab/Christmas_Bola_Skin.png',
            'class_name': 'PrimalItemSkin_WW_Xmas_Bola_C', 'id': 563,
            'description': "You can use this to skin a bola into ornaments connected with ribbon. There's no escaping your holiday cheer!",
            'url': 'https://ark.fandom.com/wiki/Christmas_Bola_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ClownMask.PrimalItemSkin_ClownMask\'"',
            'name': 'Clown Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Clown_Mask_Skin.png',
            'class_name': 'PrimalItemSkin_ClownMask_C', 'id': 564,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a jovial look.',
            'url': 'https://ark.fandom.com/wiki/Clown_Mask_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatartBoots.PrimalItemSkin_Gen1AvatartBoots\'"',
            'name': 'Corrupted Avatar Boots Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/12/Corrupted_Avatar_Boots_Skin_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItemSkin_Gen1AvatartBoots_C', 'id': 565,
            'description': 'You can use this to skin the appearance of a pair of boots. A fractal look from the Genesis simulation.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Avatar_Boots_Skin_(Genesis:_Part_1)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarGloves.PrimalItemSkin_Gen1AvatarGloves\'"',
            'name': 'Corrupted Avatar Gloves Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Corrupted_Avatar_Gloves_Skin_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItemSkin_Gen1AvatarGloves_C', 'id': 566,
            'description': 'You can use this to skin the appearance of gloves. A fractal look from the Genesis simulation.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Avatar_Gloves_Skin_(Genesis:_Part_1)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarHelmet.PrimalItemSkin_Gen1AvatarHelmet\'"',
            'name': 'Corrupted Avatar Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7a/Corrupted_Avatar_Helmet_Skin_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItemSkin_Gen1AvatarHelmet_C', 'id': 567,
            'description': 'You can use this to skin the appearance of a helmet or hat. A fractal look from the Genesis simulation.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Avatar_Helmet_Skin_(Genesis:_Part_1)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarPants.PrimalItemSkin_Gen1AvatarPants\'"',
            'name': 'Corrupted Avatar Pants Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8b/Corrupted_Avatar_Pants_Skin_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItemSkin_Gen1AvatarPants_C', 'id': 568,
            'description': 'You can use this to skin the appearance of a pants. A fractal look from the Genesis simulation.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Avatar_Pants_Skin_(Genesis:_Part_1)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Gen1AvatarShirt.PrimalItemSkin_Gen1AvatarShirt\'"',
            'name': 'Corrupted Avatar Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e8/Corrupted_Avatar_Shirt_Skin_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItemSkin_Gen1AvatarShirt_C', 'id': 569,
            'description': 'You can use this to skin the appearance of chest armor. A fractal look from the Genesis simulation.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Avatar_Shirt_Skin_(Genesis:_Part_1)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedBoots.PrimalItemSkin_CorruptedBoots\'"',
            'name': 'Corrupted Boots Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/95/Corrupted_Boots_Skin.png',
            'class_name': 'PrimalItemSkin_CorruptedBoots_C', 'id': 570,
            'description': 'You can use this to skin the appearance of boots. Provides a terrifying look.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Boots_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedShirt.PrimalItemSkin_CorruptedShirt\'"',
            'name': 'Corrupted Chestpiece Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/53/Corrupted_Chestpiece_Skin.png',
            'class_name': 'PrimalItemSkin_CorruptedShirt_C', 'id': 571,
            'description': 'You can use this to skin the appearance of a shirt or chestpiece. Provides a terrifying look!',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Chestpiece_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedGloves.PrimalItemSkin_CorruptedGloves\'"',
            'name': 'Corrupted Gloves Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Corrupted_Gloves_Skin.png',
            'class_name': 'PrimalItemSkin_CorruptedGloves_C', 'id': 572,
            'description': 'You can use this to skin the appearance of gloves. Provides a terrifying look!',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Gloves_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedHelmet.PrimalItemSkin_CorruptedHelmet\'"',
            'name': 'Corrupted Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/81/Corrupted_Helmet_Skin.png',
            'class_name': 'PrimalItemSkin_CorruptedHelmet_C', 'id': 573,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a terrifying look.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Helmet_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_CorruptedPants.PrimalItemSkin_CorruptedPants\'"',
            'name': 'Corrupted Pants Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Corrupted_Pants_Skin.png',
            'class_name': 'PrimalItemSkin_CorruptedPants_C', 'id': 574,
            'description': 'You can use this to skin the appearance of pants. Provides a terrifying look.',
            'url': 'https://ark.fandom.com/wiki/Corrupted_Pants_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_CrabParty.PrimalItemSkin_SummerSwimPants_CrabParty\'"',
            'name': 'Crab Fest Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3e/Crab_Fest_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimPants_CrabParty_C', 'id': 575,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Warning—might pinch a little.',
            'url': 'https://ark.fandom.com/wiki/Crab_Fest_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_CrabParty.PrimalItemSkin_SummerSwimShirt_CrabParty\'"',
            'name': 'Crab Fest Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c2/Crab_Fest_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimShirt_CrabParty_C', 'id': 576,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Warning—might pinch a little.',
            'url': 'https://ark.fandom.com/wiki/Crab_Fest_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ValentinePants.PrimalItemSkin_ValentinePants\'"',
            'name': 'Cupid Couture Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1d/Cupid_Couture_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_ValentinePants_C', 'id': 577,
            'description': 'You can use this to skin the appearance of pants into a festive tutu for men or women. Love the way you look this season.',
            'url': 'https://ark.fandom.com/wiki/Cupid_Couture_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ValentineShirt.PrimalItemSkin_ValentineShirt\'"',
            'name': 'Cupid Couture Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/59/Cupid_Couture_Top_Skin.png',
            'class_name': 'PrimalItemSkin_ValentineShirt_C', 'id': 578,
            'description': 'You can use this to skin the appearance of a shirt into a festive sash and wings for men or women. Love the way you look this season.',
            'url': 'https://ark.fandom.com/wiki/Cupid_Couture_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoCute.PrimalItemSkin_DinoCute\'"',
            'name': 'Cute Dino Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/36/Cute_Dino_Helmet_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_DinoCute_C', 'id': 579,
            'description': 'You can use this to skin the appearance of a helmet or hat.',
            'url': 'https://ark.fandom.com/wiki/Cute_Dino_Helmet_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/Aberration/Dinos/CaveWolf/PrimalItemArmor_CavewolfPromoSaddle.PrimalItemArmor_CavewolfPromoSaddle\'"',
            'name': 'Decorative Ravager Saddle Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Decorative_Ravager_Saddle_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemArmor_CavewolfPromoSaddle_C', 'id': 580,
            'description': 'Place this on a Ravager Saddle to have a more aesthetically pleasing saddle.',
            'url': 'https://ark.fandom.com/wiki/Decorative_Ravager_Saddle_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DiloMask.PrimalItemSkin_DiloMask\'"',
            'name': 'Dilo Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Dilo_Mask_Skin.png',
            'class_name': 'PrimalItemSkin_DiloMask_C', 'id': 581,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a jovial look.',
            'url': 'https://ark.fandom.com/wiki/Dilo_Mask_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoBunnyHat.PrimalItemSkin_DinoBunnyHat\'"',
            'name': 'Dino Bunny Ears Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Bunny_Ears_Skin.png',
            'class_name': 'PrimalItemSkin_DinoBunnyHat_C', 'id': 582,
            'description': 'You can use this to skin the appearance of a Saddle. Make your mount look eggcellent!',
            'url': 'https://ark.fandom.com/wiki/Dino_Bunny_Ears_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoChickHat.PrimalItemSkin_DinoChickHat\'"',
            'name': 'Dino Easter Chick Hat', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Easter_Chick_Hat.png',
            'class_name': 'PrimalItemSkin_DinoChickHat_C', 'id': 583,
            'description': 'You can use this skin to change the appearance of your headgear. Equip for an adorable look resembling a baby spring chick!',
            'url': 'https://ark.fandom.com/wiki/Dino_Easter_Chick_Hat'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoEasterEggHat.PrimalItemSkin_DinoEasterEggHat\'"',
            'name': 'Dino Easter Egg Hat', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Easter_Egg_Hat.png',
            'class_name': 'PrimalItemSkin_DinoEasterEggHat_C', 'id': 584,
            'description': 'You can use this to skin the appearance of your headgear. Provides a freshly hatched look!',
            'url': 'https://ark.fandom.com/wiki/Dino_Easter_Egg_Hat'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoMarshmallowHat.PrimalItemSkin_DinoMarshmallowHat\'"',
            'name': 'Dino Marshmallow Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Marshmallow_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_DinoMarshmallowHat_C', 'id': 585,
            'description': 'You can use this to skin the appearance of a helmet or hat. Gives a fluffy look.',
            'url': 'https://ark.fandom.com/wiki/Dino_Marshmallow_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_DinoOrnaments.PrimalItemSkin_WW_Underwear_DinoOrnaments\'"',
            'name': 'Dino Ornament Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Dino_Ornament_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_WW_Underwear_DinoOrnaments_C', 'id': 586,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. Give yourself that festive holiday look.',
            'url': 'https://ark.fandom.com/wiki/Dino_Ornament_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_DinoOrnaments.PrimalItemSkin_WW_SwimShirt_DinoOrnaments\'"',
            'name': 'Dino Ornament Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b8/Dino_Ornament_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_WW_SwimShirt_DinoOrnaments_C', 'id': 587,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. Give yourself that festive holiday look.',
            'url': 'https://ark.fandom.com/wiki/Dino_Ornament_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoPartyHat.PrimalItemSkin_DinoPartyHat\'"',
            'name': 'Dino Party Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Party_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_DinoPartyHat_C', 'id': 588,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a festive look!',
            'url': 'https://ark.fandom.com/wiki/Dino_Party_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DinoSantaHat.PrimalItemSkin_DinoSantaHat\'"',
            'name': 'Dino Santa Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d2/Santa_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_DinoSantaHat_C', 'id': 589,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a jolly look.',
            'url': 'https://ark.fandom.com/wiki/Dino_Santa_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TopHat_Summer_Dino.PrimalItemSkin_TopHat_Summer_Dino\'"',
            'name': 'Dino Uncle Sam Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Uncle_Sam_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_TopHat_Summer_Dino_C', 'id': 590,
            'description': 'You can use this to skin the appearance of a helmet or hat.  I want YOU to survive in star-spangled style.',
            'url': 'https://ark.fandom.com/wiki/Dino_Uncle_Sam_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_DinoWitchHat.PrimalItemSkin_DinoWitchHat\'"',
            'name': 'Dino Witch Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Witch_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_DinoWitchHat_C', 'id': 591,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a bewitching look.',
            'url': 'https://ark.fandom.com/wiki/Dino_Witch_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostDirewolf.PrimalItemCostume_GhostDirewolf\'"',
            'name': 'Direwolf Ghost Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b9/Direwolf_Ghost_Costume.png',
            'class_name': 'PrimalItemCostume_GhostDirewolf_C', 'id': 592,
            'description': 'Use this spectrally spooky costume to get your Direwolf into the spirit of the season!',
            'url': 'https://ark.fandom.com/wiki/Direwolf_Ghost_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimPants_DodoPie.PrimalItemSkin_TT_SwimPants_DodoPie\'"',
            'name': 'Dodo Pie Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5d/Dodo_Pie_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_TT_SwimPants_DodoPie_C', 'id': 593,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Bake me up before you dodo.',
            'url': 'https://ark.fandom.com/wiki/Dodo_Pie_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimShirt_DodoPie.PrimalItemSkin_TT_SwimShirt_DodoPie\'"',
            'name': 'Dodo Pie Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/dc/Dodo_Pie_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_TT_SwimShirt_DodoPie_C', 'id': 594,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Bake me up before you dodo.',
            'url': 'https://ark.fandom.com/wiki/Dodo_Pie_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimPants_Dodo.PrimalItemSkin_SwimPants_Dodo\'"',
            'name': 'Dodorex Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d3/Dodorex_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SwimPants_Dodo_C', 'id': 595,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. Mama DodoRex says to wait thirty minutes to go swimming after dinner.',
            'url': 'https://ark.fandom.com/wiki/Dodorex_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimShirt_Dodo.PrimalItemSkin_SwimShirt_Dodo\'"',
            'name': 'Dodorex Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f3/Dodorex_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SwimShirt_Dodo_C', 'id': 596,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. Mama DodoRex says to wait thirty minutes to go swimming after dinner.',
            'url': 'https://ark.fandom.com/wiki/Dodorex_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Dodo.PrimalItemSkin_HawaiianShirt_Dodo\'"',
            'name': 'Dodorex-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/86/Dodorex-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_Dodo_C', 'id': 597,
            'description': 'You can use this to skin the appearance of a shirt. Can you smell what Mama DodoRex is cooking?',
            'url': 'https://ark.fandom.com/wiki/Dodorex-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_DodowyvernHat.PrimalItemSkin_DodowyvernHat\'"',
            'name': 'DodoWyvern Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8e/DodoWyvern_Mask_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_DodowyvernHat_C', 'id': 598,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a hallowed look',
            'url': 'https://ark.fandom.com/wiki/DodoWyvern_Mask_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EasterBasket_C4.PrimalItemSkin_EasterBasket_C4\'"',
            'name': 'E4 Remote Eggsplosives Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/78/E4_Remote_Eggsplosives_Skin.png',
            'class_name': 'PrimalItemSkin_EasterBasket_C4_C', 'id': 599,
            'description': "You can use this to skin the appearance of C4 into an eggsplosive Easter basket. Nothing beats these eggs for poaching your enemies... it'll be over easy!",
            'url': 'https://ark.fandom.com/wiki/E4_Remote_Eggsplosives_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EasterChick.PrimalItemSkin_EasterChick\'"',
            'name': 'Easter Chick Hat', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Easter_Chick_Hat.png',
            'class_name': 'PrimalItemSkin_EasterChick_C', 'id': 600,
            'description': 'You can use this skin to change the appearance of your headgear. Equip for an adorable look resembling a baby spring chick!',
            'url': 'https://ark.fandom.com/wiki/Easter_Chick_Hat'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EasterEggHat.PrimalItemSkin_EasterEggHat\'"',
            'name': 'Easter Egg Hat', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Easter_Egg_Hat.png',
            'class_name': 'PrimalItemSkin_EasterEggHat_C', 'id': 601,
            'description': 'You can use this to skin the appearance of your headgear. Provides a freshly hatched look!',
            'url': 'https://ark.fandom.com/wiki/Easter_Egg_Hat'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_EggNestHat.PrimalItemSkin_EggNestHat\'"',
            'name': 'Easter Egghead Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Easter_Egghead_Skin.png',
            'class_name': 'PrimalItemSkin_EggNestHat_C', 'id': 602,
            'description': "You can use this to skin the appearance of a helmet or hat into a eggstraordinary chocolate egg nest. This bird's nest on your head will be no yolk!",
            'url': 'https://ark.fandom.com/wiki/Easter_Egghead_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_WildcardAdmin.PrimalItem_Skin_Account_WildcardAdmin\'"',
            'name': 'Fan Ballcap Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Fan_Ballcap_Skin.png',
            'class_name': 'PrimalItem_Skin_Account_WildcardAdmin', 'id': 603,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides an authoritative look!',
            'url': 'https://ark.fandom.com/wiki/Fan_Ballcap_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekBoots_V2.PrimalItemSkin_TekBoots_V2\'"',
            'name': 'Federation Exo Boots Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Federation_Exo_Boots_Skin_%28Genesis_Part_2%29.png',
            'class_name': 'PrimalItemSkin_TekBoots_V2_C', 'id': 604,
            'description': 'You can use this to skin the appearance of a pair of boots. Looks like a genuine pair of Terran Federation tek-reinforced exo-boots!',
            'url': 'https://ark.fandom.com/wiki/Federation_Exo_Boots_Skin_(Genesis:_Part_2)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekHelmet_V2.PrimalItemSkin_TekHelmet_V2\'"',
            'name': 'Federation Exo Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f0/Federation_Exo_Helmet_Skin_%28Genesis_Part_2%29.png',
            'class_name': 'PrimalItemSkin_TekHelmet_V2_C', 'id': 605,
            'description': 'You can use this to skin the appearance of a helmet or hat. Looks like a genuine Terran Federation tek-reinforced exo-helmet!',
            'url': 'https://ark.fandom.com/wiki/Federation_Exo_Helmet_Skin_(Genesis:_Part_2)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekShirt_V2.PrimalItemSkin_TekShirt_V2\'"',
            'name': 'Federation Exo-Chestpiece Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Federation_Exo-Chestpiece_Skin_%28Genesis_Part_2%29.png',
            'class_name': 'PrimalItemSkin_TekShirt_V2_C', 'id': 606,
            'description': 'You can use this to skin the appearance of a shirt or chestpiece. Looks like a genuine pair of Terran Federation tek-reinforced exo-shirt!',
            'url': 'https://ark.fandom.com/wiki/Federation_Exo-Chestpiece_Skin_(Genesis:_Part_2)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekGloves_V2.PrimalItemSkin_TekGloves_V2\'"',
            'name': 'Federation Exo-Gloves Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d2/Federation_Exo-Gloves_Skin_%28Genesis_Part_2%29.png',
            'class_name': 'PrimalItemSkin_TekGloves_V2_C', 'id': 607,
            'description': 'You can use this to skin the appearance of gloves. Looks like a genuine pair of Terran Federation tek-reinforced Exo-Gloves!',
            'url': 'https://ark.fandom.com/wiki/Federation_Exo-Gloves_Skin_(Genesis:_Part_2)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TekPants_V2.PrimalItemSkin_TekPants_V2\'"',
            'name': 'Federation Exo-leggings Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b5/Federation_Exo-leggings_Skin_%28Genesis_Part_2%29.png',
            'class_name': 'PrimalItemSkin_TekPants_V2_C', 'id': 608,
            'description': 'You can use this to skin the appearance of leggings or pants. Looks like a genuine pair of Terran Federation tek-reinforced exo-pants!',
            'url': 'https://ark.fandom.com/wiki/Federation_Exo-leggings_Skin_(Genesis:_Part_2)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_ReindeerAntlersHat.PrimalItemSkin_WW_ReindeerAntlersHat\'"',
            'name': 'Felt Reindeer Antlers Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Felt_Reindeer_Antlers_Skin.png',
            'class_name': 'PrimalItemSkin_WW_ReindeerAntlersHat_C', 'id': 609,
            'description': "You can use this to skin the appearance of a helmet or hat. Slay 'em with the reindeer look this holiday season.",
            'url': 'https://ark.fandom.com/wiki/Felt_Reindeer_Antlers_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_RocketLauncherFireworks.PrimalItemSkin_RocketLauncherFireworks\'"',
            'name': 'Fireworks Rocket Launcher Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/50/Fireworks_Rocket_Launcher_Skin.png',
            'class_name': 'PrimalItemSkin_RocketLauncherFireworks_C', 'id': 610,
            'description': 'Blow up your enemies with style using these colorful exploding fireworks!',
            'url': 'https://ark.fandom.com/wiki/Fireworks_Rocket_Launcher_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_FishBite.PrimalItemSkin_SummerSwimPants_FishBite\'"',
            'name': 'Fish Bite Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Fish_Bite_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimPants_FishBite_C', 'id': 611,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Watch out for those teeth!',
            'url': 'https://ark.fandom.com/wiki/Fish_Bite_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_FishBite.PrimalItemSkin_SummerSwimShirt_FishBite\'"',
            'name': 'Fish Bite Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a7/Fish_Bite_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimShirt_FishBite_C', 'id': 612,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Watch out for those teeth!',
            'url': 'https://ark.fandom.com/wiki/Fish_Bite_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Flowers.PrimalItemSkin_SummerSwimPants_Flowers\'"',
            'name': 'Floral Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Floral_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimPants_Flowers_C', 'id': 613,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Rule the beach this summer with the power of flowers.',
            'url': 'https://ark.fandom.com/wiki/Floral_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Flowers.PrimalItemSkin_SummerSwimShirt_Flowers\'"',
            'name': 'Floral Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Floral_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimShirt_Flowers_C', 'id': 614,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Blossom into the beach bod of your dreams.',
            'url': 'https://ark.fandom.com/wiki/Floral_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Boomerang_Frisbee.PrimalItemSkin_Boomerang_Frisbee\'"',
            'name': 'Flying Disc Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Flying_Disc_Skin.png',
            'class_name': 'PrimalItemSkin_Boomerang_Frisbee_C', 'id': 615,
            'description': 'You can use this to skin the appearance of a Boomerang. Portable fun for the beach!',
            'url': 'https://ark.fandom.com/wiki/Flying_Disc_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Gasbags.PrimalItemSkin_HawaiianShirt_Gasbags\'"',
            'name': 'Gasbags-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Gasbags-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_Gasbags_C', 'id': 616,
            'description': 'You can use this to skin the appearance of a shirt. Breezy summerwear.',
            'url': 'https://ark.fandom.com/wiki/Gasbags-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicGigant.PrimalItemCostume_BionicGigant\'"',
            'name': 'Giga Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Giga_Bionic_Costume.png',
            'class_name': 'PrimalItemCostume_BionicGigant_C', 'id': 617,
            'description': 'This costume can be used to make your Giga look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Giga_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Carno.PrimalItemSkin_SummerSwimPants_Carno\'"',
            'name': 'Giga Poop Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/1a/Giga_Poop_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimPants_Carno_C', 'id': 618,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  With swimwear this fashionable, no one minds you floating in their pool.',
            'url': 'https://ark.fandom.com/wiki/Giga_Poop_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Carno.PrimalItemSkin_SummerSwimShirt_Carno\'"',
            'name': 'Giga Poop Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Giga_Poop_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimShirt_Carno_C', 'id': 619,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  The perfect look for those who want the beach to themselves.',
            'url': 'https://ark.fandom.com/wiki/Giga_Poop_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneGigant.PrimalItemCostume_BoneGigant\'"',
            'name': 'Giganotosaurus Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ef/Giganotosaurus_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneGigant_C', 'id': 620,
            'description': 'This costume can be used to make your Giganotosaurus look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Giganotosaurus_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Armor/PrimalItemArmor_Glider.PrimalItemArmor_Glider\'"',
            'name': 'Glider Suit', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f7/Glider_Suit_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemArmor_Glider_C', 'id': 621,
            'description': 'When attached to a Chest Armor, the Glider Suit enables sailing through the air by double-tapping jump, while gaining speed by running and diving!',
            'url': 'https://ark.fandom.com/wiki/Glider_Suit_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatB.PrimalItemSkin_WW_WinterHatB\'"',
            'name': 'Gray-Ball Winter Beanie Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d7/Gray-Ball_Winter_Beanie_Skin.png',
            'class_name': 'PrimalItemSkin_WW_WinterHatB_C', 'id': 622,
            'description': 'You can use this to skin the appearance of a helmet or hat. Features big dinos and an ARK patch.',
            'url': 'https://ark.fandom.com/wiki/Gray-Ball_Winter_Beanie_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatF.PrimalItemSkin_WW_WinterHatF\'"',
            'name': 'Green-Ball Winter Beanie Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bf/Green-Ball_Winter_Beanie_Skin.png',
            'class_name': 'PrimalItemSkin_WW_WinterHatF_C', 'id': 623,
            'description': 'You can use this to skin the appearance of a helmet or hat. Features a parade of dinos and an ARK patch.',
            'url': 'https://ark.fandom.com/wiki/Green-Ball_Winter_Beanie_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Club_BBQSpatula.PrimalItemSkin_Club_BBQSpatula\'"',
            'name': 'Grilling Spatula Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Grilling_Spatula_Skin.png',
            'class_name': 'PrimalItemSkin_Club_BBQSpatula_C', 'id': 624,
            'description': 'You can use this to skin the appearance of a Club. How do you want your meat?',
            'url': 'https://ark.fandom.com/wiki/Grilling_Spatula_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ValentineHaloHat.PrimalItemSkin_ValentineHaloHat\'"',
            'name': 'Halo Headband Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Halo_Headband_Skin.png',
            'class_name': 'PrimalItemSkin_ValentineHaloHat_C', 'id': 625,
            'description': 'You can use this to skin the appearance of a helmet or hat into a decorative halo headband. For those times you want to look good... really good.',
            'url': 'https://ark.fandom.com/wiki/Halo_Headband_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_HeadlessHat.PrimalItemSkin_FE_HeadlessHat\'"',
            'name': 'Headless Costume Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2d/Headless_Costume_Skin.png',
            'class_name': 'PrimalItemSkin_FE_HeadlessHat_C', 'id': 626,
            'description': "You can use this to skin the appearance of a helmet or hat. Because some days you just can't get a head.",
            'url': 'https://ark.fandom.com/wiki/Headless_Costume_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Vday_Shield.PrimalItemSkin_Vday_Shield\'"',
            'name': 'Heart-shaped Shield Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9d/Heart-shaped_Shield_Skin.png',
            'class_name': 'PrimalItemSkin_Vday_Shield_C', 'id': 627,
            'description': 'You can use this to skin the appearance of a shield. Protect yourself and the ones you love.',
            'url': 'https://ark.fandom.com/wiki/Heart-shaped_Shield_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SunGlasses_Vday.PrimalItemSkin_SunGlasses_Vday\'"',
            'name': 'Heart-shaped Sunglasses Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Sunglasses_Skin.png',
            'class_name': 'PrimalItemSkin_SunGlasses_Vday_C', 'id': 628,
            'description': 'You can use this to skin the appearance of a Hat. No one will catch you staring.',
            'url': 'https://ark.fandom.com/wiki/Heart-shaped_Sunglasses_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_ScaryFaceMask.PrimalItemSkin_FE_ScaryFaceMask\'"',
            'name': 'Hockey Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/20/Hockey_Mask_Skin.png',
            'class_name': 'PrimalItemSkin_FE_ScaryFaceMask_C', 'id': 629,
            'description': 'You can use this to skin the appearance of a helmet or hat. And by "hockey," we mean "chasing teenage campers."',
            'url': 'https://ark.fandom.com/wiki/Hockey_Mask_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusBoots.PrimalItemSkin_HomoDeusBoots\'"',
            'name': 'HomoDeus Boots Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/74/HomoDeus_Boots_Skin_%28Extinction%29.png',
            'class_name': 'PrimalItemSkin_HomoDeusBoots_C', 'id': 630,
            'description': 'You can use this to skin the appearance of a pair of boots. Provides an enlightened look.',
            'url': 'https://ark.fandom.com/wiki/HomoDeus_Boots_Skin_(Extinction)'
        },
        {
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusGloves.PrimalItemSkin_HomoDeusGloves\'"',
            'name': 'HomoDeus Gloves Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c4/HomoDeus_Gloves_Skin_%28Extinction%29.png',
            'class_name': 'PrimalItemSkin_HomoDeusGloves_C', 'id': 631,
            'description': 'You can use this to skin the appearance of gloves. Provides an enlightened look.',
            'url': 'https://ark.fandom.com/wiki/HomoDeus_Gloves_Skin_(Extinction)'
        },
        {
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusHelmet.PrimalItemSkin_HomoDeusHelmet\'"',
            'name': 'HomoDeus Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/HomoDeus_Helmet_Skin_%28Extinction%29.png',
            'class_name': 'PrimalItemSkin_HomoDeusHelmet_C', 'id': 632,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides an enlightened look.',
            'url': 'https://ark.fandom.com/wiki/HomoDeus_Helmet_Skin_(Extinction)'
        },
        {
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusPants.PrimalItemSkin_HomoDeusPants\'"',
            'name': 'HomoDeus Pants Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/90/HomoDeus_Pants_Skin_%28Extinction%29.png',
            'class_name': 'PrimalItemSkin_HomoDeusPants_C', 'id': 633,
            'description': 'You can use this to skin the appearance of a pants. Provides an enlightened look.',
            'url': 'https://ark.fandom.com/wiki/HomoDeus_Pants_Skin_(Extinction)'
        },
        {
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Items/Skin/PrimalItemSkin_HomoDeusShirt.PrimalItemSkin_HomoDeusShirt\'"',
            'name': 'HomoDeus Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2f/HomoDeus_Shirt_Skin_%28Extinction%29.png',
            'class_name': 'PrimalItemSkin_HomoDeusShirt_C', 'id': 634,
            'description': 'You can use this to skin the appearance of chest armor. Provides an enlightened look.',
            'url': 'https://ark.fandom.com/wiki/HomoDeus_Shirt_Skin_(Extinction)'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Island.PrimalItemSkin_HawaiianShirt_Island\'"',
            'name': 'Ice Pop-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/23/Ice_Pop-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_Island_C', 'id': 635,
            'description': 'You can use this to skin the appearance of a shirt. Look cool and chill out.',
            'url': 'https://ark.fandom.com/wiki/Ice_Pop-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_IslandRetreat.PrimalItemSkin_SummerSwimPants_IslandRetreat\'"',
            'name': 'Ichthy Isles Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Ichthy_Isles_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimPants_IslandRetreat_C', 'id': 636,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Swim with the ichthyosaurs!',
            'url': 'https://ark.fandom.com/wiki/Ichthy_Isles_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_IslandRetreat.PrimalItemSkin_SummerSwimShirt_IslandRetreat\'"',
            'name': 'Ichthy Isles Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b1/Ichthy_Isles_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimShirt_IslandRetreat_C', 'id': 637,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Swim with the ichthyosaurs!',
            'url': 'https://ark.fandom.com/wiki/Ichthy_Isles_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Pumpkin.PrimalItemSkin_FE_Underwear_Pumpkin\'"',
            'name': 'Jack-O-Lantern Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Jack-O-Lantern_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_FE_Underwear_Pumpkin_C', 'id': 638,
            'description': "You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women, and give 'em all pumpkin to talk about!",
            'url': 'https://ark.fandom.com/wiki/Jack-O-Lantern_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Pumpkin.PrimalItemSkin_FE_SwimShirt_Pumpkin\'"',
            'name': 'Jack-O-Lantern Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6a/Jack-O-Lantern_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_FE_SwimShirt_Pumpkin_C', 'id': 639,
            'description': "You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women, and give 'em all pumpkin to talk about!",
            'url': 'https://ark.fandom.com/wiki/Jack-O-Lantern_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Pumpkin.PrimalItemSkin_HawaiianShirt_Pumpkin\'"',
            'name': 'Jack-O-Lantern-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/da/Jack-O-Lantern-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_Pumpkin_C', 'id': 640,
            'description': 'You can use this to skin the appearance of a shirt. Let the gourd times roll!',
            'url': 'https://ark.fandom.com/wiki/Jack-O-Lantern-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneJerboa.PrimalItemCostume_BoneJerboa\'"',
            'name': 'Jerboa Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/98/Jerboa_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneJerboa_C', 'id': 641,
            'description': 'This costume can be used to make your Jerboa look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Jerboa_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_JerboaWreath.PrimalItemSkin_WW_Underwear_JerboaWreath\'"',
            'name': 'Jerboa Wreath Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/00/Jerboa_Wreath_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_WW_Underwear_JerboaWreath_C', 'id': 642,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. "Ears" wishing you happy holidays!',
            'url': 'https://ark.fandom.com/wiki/Jerboa_Wreath_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_JerboaWreath.PrimalItemSkin_WW_SwimShirt_JerboaWreath\'"',
            'name': 'Jerboa Wreath Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Jerboa_Wreath_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_WW_SwimShirt_JerboaWreath_C', 'id': 643,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. "Ears" wishing you happy holidays!',
            'url': 'https://ark.fandom.com/wiki/Jerboa_Wreath_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Vday_Handcuffs.PrimalItemSkin_Vday_Handcuffs\'"',
            'name': 'Love Shackles Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Love_Shackles_Skin.png',
            'class_name': 'PrimalItemSkin_Vday_Handcuffs_C', 'id': 644,
            'description': 'You can use this to skin the appearance of handcuffs into a fuzzy, pink variant. Don\'t let "the one" get away.',
            'url': 'https://ark.fandom.com/wiki/Love_Shackles_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreBoots.PrimalItemSkin_ManticoreBoots\'"',
            'name': 'Manticore Boots Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4a/Manticore_Boots_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ManticoreBoots_C', 'id': 645,
            'description': 'You can use this to skin the appearance of boots. Provides a ferocious look!',
            'url': 'https://ark.fandom.com/wiki/Manticore_Boots_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreShirt.PrimalItemSkin_ManticoreShirt\'"',
            'name': 'Manticore Chestpiece Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e6/Manticore_Chestpiece_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ManticoreShirt_C', 'id': 646,
            'description': 'You can use this to skin the appearance of a shirt or chestpiece. Provides a ferocious look!',
            'url': 'https://ark.fandom.com/wiki/Manticore_Chestpiece_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreGloves.PrimalItemSkin_ManticoreGloves\'"',
            'name': 'Manticore Gauntlets Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7a/Manticore_Gauntlets_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ManticoreGloves_C', 'id': 647,
            'description': 'You can use this to skin the appearance of gloves. Provides a ferocious look!',
            'url': 'https://ark.fandom.com/wiki/Manticore_Gauntlets_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreHelmet.PrimalItemSkin_ManticoreHelmet\'"',
            'name': 'Manticore Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5c/Manticore_Helmet_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ManticoreHelmet_C', 'id': 648,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a ferocious look!',
            'url': 'https://ark.fandom.com/wiki/Manticore_Helmet_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticorePants.PrimalItemSkin_ManticorePants\'"',
            'name': 'Manticore Leggings Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5e/Manticore_Leggings_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ManticorePants_C', 'id': 649,
            'description': 'You can use this to skin the appearance of leggings or pants. Provides a ferocious look!',
            'url': 'https://ark.fandom.com/wiki/Manticore_Leggings_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ManticoreShield.PrimalItemSkin_ManticoreShield\'"',
            'name': 'Manticore Shield Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3e/Manticore_Shield_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ManticoreShield_C', 'id': 650,
            'description': 'You can use this to skin the appearance of a shield. Brought back from the far reaches of the Scorched Earth!',
            'url': 'https://ark.fandom.com/wiki/Manticore_Shield_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostMantis.PrimalItemCostume_GhostMantis\'"',
            'name': 'Mantis Ghost Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ab/Mantis_Ghost_Costume.png',
            'class_name': 'PrimalItemCostume_GhostMantis_C', 'id': 651,
            'description': 'Use this spectrally spooky costume to get your Mantis into the spirit of the season!',
            'url': 'https://ark.fandom.com/wiki/Mantis_Ghost_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_MarshmallowHat.PrimalItemSkin_MarshmallowHat\'"',
            'name': 'Marshmallow Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f5/Marshmallow_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_MarshmallowHat_C', 'id': 652,
            'description': 'You can use this to skin the appearance of a helmet or hat. Gives a fluffy look.',
            'url': 'https://ark.fandom.com/wiki/Marshmallow_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/Genesis/CoreBlueprints/Items/PrimalItemSkin_MasterControllerHelmet.PrimalItemSkin_MasterControllerHelmet\'"',
            'name': 'Master Controller Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Master_Controller_Helmet_Skin_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItemSkin_MasterControllerHelmet_C', 'id': 653,
            'description': 'You can use this to skin the appearance of a helmet or hat. Displays your dominance over the Master Controller.',
            'url': 'https://ark.fandom.com/wiki/Master_Controller_Helmet_Skin_(Genesis:_Part_1)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimPants_Meat.PrimalItemSkin_TT_SwimPants_Meat\'"',
            'name': 'Meat Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/55/Meat_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_TT_SwimPants_Meat_C', 'id': 654,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  When fashion swimwear "meats" holiday attire.',
            'url': 'https://ark.fandom.com/wiki/Meat_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimShirt_Meat.PrimalItemSkin_TT_SwimShirt_Meat\'"',
            'name': 'Meat Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Meat_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_TT_SwimShirt_Meat_C', 'id': 655,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  When fashion swimwear "meats" holiday attire.',
            'url': 'https://ark.fandom.com/wiki/Meat_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_ReindeerStag.PrimalItemCostume_ReindeerStag\'"',
            'name': 'Megaloceros Reindeer Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/ce/Megaloceros_Reindeer_Costume.png',
            'class_name': 'PrimalItemCostume_ReindeerStag_C', 'id': 656,
            'description': 'This costume can be used to make your Megaloceros look like a festive creature!',
            'url': 'https://ark.fandom.com/wiki/Megaloceros_Reindeer_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_MiniHLNA.PrimalItemSkin_MiniHLNA\'"',
            'name': 'Mini-HLNA Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/37/Mini-HLNA_Skin_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItemSkin_MiniHLNA_C', 'id': 657,
            'description': 'HLNA can be equipped to the shield slot or attach HLNA to an existing shield.  Scanning the Elemental Disturbances in caves may reveal hidden information.',
            'url': 'https://ark.fandom.com/wiki/Mini-HLNA_Skin_(Genesis:_Part_1)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicMosa.PrimalItemCostume_BionicMosa\'"',
            'name': 'Mosasaurus Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a6/Mosasaurus_Bionic_Costume.png',
            'class_name': 'PrimalItemCostume_BionicMosa_C', 'id': 658,
            'description': 'This costume can be used to make your Mosasaurus look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Mosasaurus_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimPants_MurderTurkey.PrimalItemSkin_SwimPants_MurderTurkey\'"',
            'name': 'Murder Turkey Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cc/Turkey_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SwimPants_MurderTurkey_C', 'id': 659,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Give thanks for another great day on the beach.',
            'url': 'https://ark.fandom.com/wiki/Murder_Turkey_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SwimShirt_MurderTurkey.PrimalItemSkin_SwimShirt_MurderTurkey\'"',
            'name': 'Murder Turkey Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Turkey_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SwimShirt_MurderTurkey_C', 'id': 660,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Give thanks for another great day on the beach.',
            'url': 'https://ark.fandom.com/wiki/Murder_Turkey_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_MurderTurkey.PrimalItemSkin_HawaiianShirt_MurderTurkey\'"',
            'name': 'Murder-Turkey-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/34/Murder-Turkey-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_MurderTurkey_C', 'id': 661,
            'description': "You can use this to skin the appearance of a shirt. Looks like you're on the holiday menu this year!",
            'url': 'https://ark.fandom.com/wiki/Murder-Turkey-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_Glasses.PrimalItemSkin_Glasses\'"',
            'name': 'Nerdry Glasses Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8f/Nerdry_Glasses_Skin.png',
            'class_name': 'PrimalItemSkin_Glasses_C', 'id': 662,
            'description': 'You can use this to skin the appearance of a helmet or hat. Slightly cracked and chewed, but still provides an intelligent look!',
            'url': 'https://ark.fandom.com/wiki/Nerdry_Glasses_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_Noglin.PrimalItemSkin_WW_Underwear_Noglin\'"',
            'name': 'Noglin Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5b/Noglin_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_WW_Underwear_Noglin_C', 'id': 663,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. Unwrap a mind-bending surprise... A gift to make your head swim!',
            'url': 'https://ark.fandom.com/wiki/Noglin_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_Noglin.PrimalItemSkin_WW_SwimShirt_Noglin\'"',
            'name': 'Noglin Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c4/Noglin_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_WW_SwimShirt_Noglin_C', 'id': 664,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. Unwrap a mind-bending surprise... A gift to make your head swim!',
            'url': 'https://ark.fandom.com/wiki/Noglin_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_WW_Nutcracker_Slingshot.PrimalItemSkin_WW_Nutcracker_Slingshot\'"',
            'name': 'Nutcracker Slingshot Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3a/Nutcracker_Slingshot_Skin.png',
            'class_name': 'PrimalItemSkin_WW_Nutcracker_Slingshot_C', 'id': 665,
            'description': 'You can use this to skin a slingshot into shooting walnuts. Launch your very own snack attack!',
            'url': 'https://ark.fandom.com/wiki/Nutcracker_Slingshot_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Onyc.PrimalItemSkin_FE_Underwear_Onyc\'"',
            'name': 'Onyc Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Onyc_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_FE_Underwear_Onyc_C', 'id': 666,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  A swim suit with lots of "bat"-itude..',
            'url': 'https://ark.fandom.com/wiki/Onyc_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Onyc.PrimalItemSkin_FE_SwimShirt_Onyc\'"',
            'name': 'Onyc Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Onyc_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_FE_SwimShirt_Onyc_C', 'id': 667,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  A swim suit with lots of "bat"-itude..',
            'url': 'https://ark.fandom.com/wiki/Onyc_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_OtterMask.PrimalItemSkin_OtterMask\'"',
            'name': 'Otter Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c1/Otter_Mask_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_OtterMask_C', 'id': 668,
            'description': 'You can use this to skin the appearance of a helmet or hat.',
            'url': 'https://ark.fandom.com/wiki/Otter_Mask_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicParasaur.PrimalItemCostume_BionicParasaur\'"',
            'name': 'Parasaur Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9b/Parasaur_Bionic_Costume.png',
            'class_name': 'PrimalItemCostume_BionicParasaur_C', 'id': 669,
            'description': 'This costume can be used to make your Parasaur look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Parasaur_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_PartyHat.PrimalItemSkin_PartyHat\'"',
            'name': 'Party Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/01/Party_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_PartyHat_C', 'id': 670,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a festive look!',
            'url': 'https://ark.fandom.com/wiki/Party_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_PilgrimHat.PrimalItemSkin_TT_PilgrimHat\'"',
            'name': 'Pilgrim Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Pilgrim_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_TT_PilgrimHat_C', 'id': 671,
            'description': 'You can use this to skin the appearance of a helmet or hat. Because someone around here should show prudence and modesty.',
            'url': 'https://ark.fandom.com/wiki/Pilgrim_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_Pike_Pitchfork.PrimalItemSkin_TT_Pike_Pitchfork\'"',
            'name': 'Pitchfork Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/24/Pitchfork_Skin.png',
            'class_name': 'PrimalItemSkin_TT_Pike_Pitchfork_C', 'id': 672,
            'description': 'You can use this to skin the appearance of a pike weapon into a pitchfork. There are four good reasons to listen to the survivor with a pitchfork...',
            'url': 'https://ark.fandom.com/wiki/Pitchfork_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_PoglinHat.PrimalItemSkin_PoglinHat\'"',
            'name': 'Poglin Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Poglin_Mask_Skin_%28Genesis_Part_2%29.png',
            'class_name': 'PrimalItemSkin_PoglinHat_C', 'id': 673,
            'description': "You can use this to skin the appearance of a helmet or hat. Drain everyone's will to live with this disturbing headwear!",
            'url': 'https://ark.fandom.com/wiki/Poglin_Mask_Skin_(Genesis:_Part_2)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_ProcopBunny.PrimalItemCostume_ProcopBunny\'"',
            'name': 'Procoptodon Bunny Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/62/Procoptodon_Bunny_Costume.png',
            'class_name': 'PrimalItemCostume_ProcopBunny_C', 'id': 674,
            'description': 'This costume can be used to make your Procoptodon look eggcellent!',
            'url': 'https://ark.fandom.com/wiki/Procoptodon_Bunny_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_WW_WinterHatC.PrimalItemSkin_WW_WinterHatC\'"',
            'name': 'Purple-Ball Winter Beanie Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4d/Purple-Ball_Winter_Beanie_Skin.png',
            'class_name': 'PrimalItemSkin_WW_WinterHatC_C', 'id': 675,
            'description': 'You can use this to skin the appearance of a helmet or hat. Features a dino design and the ARK logo.',
            'url': 'https://ark.fandom.com/wiki/Purple-Ball_Winter_Beanie_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_WinterHatE.PrimalItemSkin_WW_WinterHatE\'"',
            'name': 'Purple-Ball Winter Beanie Skin (Winter Wonderland 5)', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/18/Purple-Ball_Winter_Beanie_Skin_%28Winter_Wonderland_5%29.png',
            'class_name': 'PrimalItemSkin_WW_WinterHatE_C', 'id': 676,
            'description': 'You can use this to skin the appearance of a helmet or hat. Features a parade of dinos and an ARK patch.',
            'url': 'https://ark.fandom.com/wiki/Purple-Ball_Winter_Beanie_Skin_(Winter_Wonderland_5)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicQuetzal.PrimalItemCostume_BionicQuetzal\'"',
            'name': 'Quetzal Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d1/Quetzal_Bionic_Costume.png',
            'class_name': 'PrimalItemCostume_BionicQuetzal_C', 'id': 677,
            'description': 'This costume can be used to make your Quetzal look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Quetzal_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_AnimeRaptor.PrimalItemCostume_AnimeRaptor\'"',
            'name': "Raptor 'ARK: The Animated Series' Costume", 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f9/Raptor_%27ARK_The_Animated_Series%27_Costume.png',
            'class_name': 'PrimalItemCostume_AnimeRaptor_C', 'id': 678,
            'description': "This costume can be used to make your Raptor look like those in 'ARK: The Animated Series'!",
            'url': 'https://ark.fandom.com/wiki/Raptor_%27ARK:_The_Animated_Series%27_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicRaptor.PrimalItemCostume_BionicRaptor\'"',
            'name': 'Raptor Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cf/Raptor_Bionic_Costume.png',
            'class_name': 'PrimalItemCostume_BionicRaptor_C', 'id': 679,
            'description': 'This costume can be used to make your Raptor look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Raptor_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneQuetz.PrimalItemCostume_BoneQuetz\'"',
            'name': 'Quetzalcoatlus Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/29/Quetzalcoatlus_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneQuetz_C', 'id': 680,
            'description': 'This costume can be used to make your Quetzalcoatlus look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Quetzalcoatlus_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneRaptor.PrimalItemCostume_BoneRaptor\'"',
            'name': 'Raptor Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Raptor_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneRaptor_C', 'id': 681,
            'description': 'This costume can be used to make your Raptor look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Raptor_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostReaper.PrimalItemCostume_GhostReaper\'"',
            'name': 'Reaper Ghost Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0c/Reaper_Ghost_Costume.png',
            'class_name': 'PrimalItemCostume_GhostReaper_C', 'id': 682,
            'description': 'Use this spectrally spooky costume to get your Reaper into the spirit of the season!',
            'url': 'https://ark.fandom.com/wiki/Reaper_Ghost_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ReaperHelmet.PrimalItemSkin_ReaperHelmet\'"',
            'name': 'Reaper Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bc/Reaper_Helmet_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_ReaperHelmet_C', 'id': 683,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides an alien look!',
            'url': 'https://ark.fandom.com/wiki/Reaper_Helmet_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_Reaper.PrimalItemSkin_FE_Underwear_Reaper\'"',
            'name': 'Reaper Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/5f/Reaper_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_FE_Underwear_Reaper_C', 'id': 684,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women, for a splashy burst of monstrous fun!',
            'url': 'https://ark.fandom.com/wiki/Reaper_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_Reaper.PrimalItemSkin_FE_SwimShirt_Reaper\'"',
            'name': 'Reaper Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/19/Reaper_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_FE_SwimShirt_Reaper_C', 'id': 685,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women, for a splashy burst of monstrous fun!',
            'url': 'https://ark.fandom.com/wiki/Reaper_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_Reaper.PrimalItemSkin_HawaiianShirt_Reaper\'"',
            'name': 'Reaper-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/71/Reaper-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_Reaper_C', 'id': 686,
            'description': 'You can use this to skin the appearance of a shirt, and represent your favorite party monster!',
            'url': 'https://ark.fandom.com/wiki/Reaper-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_WW_WinterHatA.PrimalItemSkin_WW_WinterHatA\'"',
            'name': 'Red-Ball Winter Beanie Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Red-Ball_Winter_Beanie_Skin.png',
            'class_name': 'PrimalItemSkin_WW_WinterHatA_C', 'id': 687,
            'description': 'You can use this to skin the appearance of a helmet or hat. Features an assortment of dinos on parade.',
            'url': 'https://ark.fandom.com/wiki/Red-Ball_Winter_Beanie_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicRex.PrimalItemCostume_BionicRex\'"',
            'name': 'Rex Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f8/Rex_Bionic_Costume.png',
            'class_name': 'null', 'id': 688,
            'description': 'This costume can be used to make your Rex look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Rex_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneRex.PrimalItemCostume_BoneRex\'"',
            'name': 'Rex Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fa/Rex_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneRex_C', 'id': 689,
            'description': 'This costume can be used to make your Rex look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Rex_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostRex.PrimalItemCostume_GhostRex\'"',
            'name': 'Rex Ghost Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f8/Rex_Ghost_Costume.png',
            'class_name': 'PrimalItemCostume_GhostRex_C', 'id': 690,
            'description': 'Use this spectrally spooky costume to get your Rex into the spirit of the season!',
            'url': 'https://ark.fandom.com/wiki/Rex_Ghost_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ExplorerHat.PrimalItemSkin_ExplorerHat\'"',
            'name': 'Safari Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2a/Safari_Hat_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ExplorerHat_C', 'id': 691,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a heat-beating look!',
            'url': 'https://ark.fandom.com/wiki/Safari_Hat_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SantaHat.PrimalItemSkin_SantaHat\'"',
            'name': 'Santa Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d2/Santa_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_SantaHat_C', 'id': 692,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a jolly look.',
            'url': 'https://ark.fandom.com/wiki/Santa_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemSkin_Hatchet_Santiago.PrimalItemSkin_Hatchet_Santiago\'"',
            'name': "Santiago's Axe Skin", 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6f/Santiago%27s_Axe_Skin.png',
            'class_name': 'PrimalItemSkin_Hatchet_Santiago_C', 'id': 693,
            'description': 'You can use this to skin the appearance of a hatchet to look like the axe Santiago used in the ARK II trailer!',
            'url': 'https://ark.fandom.com/wiki/Santiago%27s_Axe_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemSkin_Spear_Santiago.PrimalItemSkin_Spear_Santiago\'"',
            'name': "Santiago's Spear Skin", 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8e/Santiago%27s_Spear_Skin.png',
            'class_name': 'PrimalItemSkin_Spear_Santiago_C', 'id': 694,
            'description': 'You can use this to skin the appearance of a spear or pike to look like the spear Santiago used in the ARK II trailer!',
            'url': 'https://ark.fandom.com/wiki/Santiago%27s_Spear_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_PumpkinHat.PrimalItemSkin_FE_PumpkinHat\'"',
            'name': 'Scary Pumpkin Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a8/Scary_Pumpkin_Helmet_Skin.png',
            'class_name': 'PrimalItemSkin_FE_PumpkinHat_C', 'id': 695,
            'description': 'You can use this to skin the appearance of a helmet or hat. Good for Jack or Jill-o-Lanterns.',
            'url': 'https://ark.fandom.com/wiki/Scary_Pumpkin_Helmet_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_ScarySkull.PrimalItemSkin_ScarySkull\'"',
            'name': 'Scary Skull Helmet Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Scary_Skull_Helmet_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemSkin_ScarySkull_C', 'id': 696,
            'description': 'You can use this to skin the appearance of a helmet or hat.',
            'url': 'https://ark.fandom.com/wiki/Scary_Skull_Helmet_Skin_(Aberration)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_ScorchedSpear.PrimalItemSkin_ScorchedSpear\'"',
            'name': 'Scorched Spike Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/15/Scorched_Spike_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ScorchedSpear_C', 'id': 697,
            'description': 'Frighten your enemies with this imposing Spear or Pike skin!',
            'url': 'https://ark.fandom.com/wiki/Scorched_Spike_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_ScorchedSword.PrimalItemSkin_ScorchedSword\'"',
            'name': 'Scorched Sword Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/80/Scorched_Sword_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_ScorchedSword_C', 'id': 698,
            'description': 'You can use this to skin the appearance of a Sword. A noble blade...',
            'url': 'https://ark.fandom.com/wiki/Scorched_Sword_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TorchScorched.PrimalItemSkin_TorchScorched\'"',
            'name': 'Scorched Torch Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f1/Scorched_Torch_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_TorchScorched_C', 'id': 699,
            'description': 'Light up the desert night with this themed Torch skin!',
            'url': 'https://ark.fandom.com/wiki/Scorched_Torch_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_HawaiianShirt_SeaStuff.PrimalItemSkin_HawaiianShirt_SeaStuff\'"',
            'name': 'Sea Life-Print Shirt Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Sea_Life-Print_Shirt_Skin.png',
            'class_name': 'PrimalItemSkin_HawaiianShirt_SeaStuff_C', 'id': 700,
            'description': 'You can use this to skin the appearance of a shirt. Make a splash at the luau!',
            'url': 'https://ark.fandom.com/wiki/Sea_Life-Print_Shirt_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_GhostOwl.PrimalItemCostume_GhostOwl\'"',
            'name': 'Snow Owl Ghost Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/68/Snow_Owl_Ghost_Costume.png',
            'class_name': 'PrimalItemCostume_GhostOwl_C', 'id': 701,
            'description': 'Use this spectrally spooky costume to get your Snow Owl into the spirit of the season!',
            'url': 'https://ark.fandom.com/wiki/Snow_Owl_Ghost_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneStego.PrimalItemCostume_BoneStego\'"',
            'name': 'Stego Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/99/Stego_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneStego_C', 'id': 702,
            'description': 'This costume can be used to make your Stego look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Stego_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicStego.PrimalItemCostume_BionicStego\'"',
            'name': 'Stegosaurus Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cd/Stegosaurus_Bionic_Costume.png',
            'class_name': 'PrimalItemCostume_BionicStego_C', 'id': 703,
            'description': 'This costume can be used to make your Stegosaurus look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Stegosaurus_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemCostume_Stygimoloch.PrimalItemCostume_Stygimoloch\'"',
            'name': 'Stygimoloch Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c7/Stygimoloch_Costume.png',
            'class_name': 'PrimalItemCostume_Stygimoloch_C', 'id': 704,
            'description': 'This costume can be used to make your Pachycephalosaurus look like a Stygimoloch!',
            'url': 'https://ark.fandom.com/wiki/Stygimoloch_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemCostume_Styracosaurus.PrimalItemCostume_Styracosaurus\'"',
            'name': 'Styracosaurus Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/08/Styracosaurus_Costume.png',
            'class_name': 'PrimalItemCostume_Styracosaurus_C', 'id': 705,
            'description': 'This costume can be used to make your Triceratops look like a Styracosaurus!',
            'url': 'https://ark.fandom.com/wiki/Styracosaurus_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SunGlasses.PrimalItemSkin_SunGlasses\'"',
            'name': 'Sunglasses Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fc/Sunglasses_Skin.png',
            'class_name': 'PrimalItemSkin_SunGlasses_C', 'id': 706,
            'description': 'You can use this to skin the appearance of a Hat. No one will catch you staring.',
            'url': 'https://ark.fandom.com/wiki/Sunglasses_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemSkin_Spear_Carrot.PrimalItemSkin_Spear_Carrot\'"',
            'name': 'Sweet Spear Carrot Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/02/Sweet_Spear_Carrot_Skin.png',
            'class_name': 'PrimalItemSkin_Spear_Carrot_C', 'id': 707,
            'description': "You can use this to skin the appearance of a spear into a deliciously crunchy weapon. It may break, but you won't carrot all.",
            'url': 'https://ark.fandom.com/wiki/Sweet_Spear_Carrot_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimPants_Arthro.PrimalItemSkin_SummerSwimPants_Arthro\'"',
            'name': 'T-Rex Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e9/T-Rex_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimPants_Arthro_C', 'id': 708,
            'description': "You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  You'll be the terror of the beach with swimwear inspired by the T-Rex itself.",
            'url': 'https://ark.fandom.com/wiki/T-Rex_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_SummerSwimShirt_Arthro.PrimalItemSkin_SummerSwimShirt_Arthro\'"',
            'name': 'T-Rex Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/0b/T-Rex_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_SummerSwimShirt_Arthro_C', 'id': 709,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  With a beach look inspired by the T-Rex, no one will notice whether your arms are tiny or not.',
            'url': 'https://ark.fandom.com/wiki/T-Rex_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_VDay_Grenade_ValentineBear.PrimalItemSkin_VDay_Grenade_ValentineBear\'"',
            'name': 'Teddy Bear Grenades Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Teddy_Bear_Grenades_Skin.png',
            'class_name': 'PrimalItemSkin_VDay_Grenade_ValentineBear_C', 'id': 710,
            'description': "You can use this to skin the appearance of grenades to look like an unbearably cute toy. Deliver it to that special someone so they know you're thinking about them.",
            'url': 'https://ark.fandom.com/wiki/Teddy_Bear_Grenades_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/Dinos/SpineyLizard/PrimalItemArmor_SpineyLizardPromoSaddle.PrimalItemArmor_SpineyLizardPromoSaddle\'"',
            'name': 'Thorny Dragon Vagabond Saddle Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/78/Thorny_Dragon_Vagabond_Saddle_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemArmor_SpineyLizardPromoSaddle_C', 'id': 711,
            'description': 'Use this on a Thorny Dragon saddle to ride in nomadic style.',
            'url': 'https://ark.fandom.com/wiki/Thorny_Dragon_Vagabond_Saddle_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TopHat.PrimalItemSkin_TopHat\'"',
            'name': 'Top Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/14/Top_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_TopHat_C', 'id': 712,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a fancy look.',
            'url': 'https://ark.fandom.com/wiki/Top_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItemSkin_TorchSparkler.PrimalItemSkin_TorchSparkler\'"',
            'name': 'Torch Sparkler Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3e/Torch_Sparkler_Skin.png',
            'class_name': 'PrimalItemSkin_TorchSparkler_C', 'id': 713,
            'description': 'Celebrate a holiday with sparkles! When applied to a Torch, can also be placed as a Wall Torch.',
            'url': 'https://ark.fandom.com/wiki/Torch_Sparkler_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BionicTrike.PrimalItemCostume_BionicTrike\'"',
            'name': 'Triceratops Bionic Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Triceratops_Bionic_Costume.png',
            'class_name': 'PrimalItemCostume_BionicTrike_C', 'id': 714,
            'description': 'This costume can be used to make your Triceratops look like it was manufactured...',
            'url': 'https://ark.fandom.com/wiki/Triceratops_Bionic_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneTrike.PrimalItemCostume_BoneTrike\'"',
            'name': 'Trike Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Trike_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneTrike_C', 'id': 715,
            'description': 'This costume can be used to make your Trike look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Trike_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_ActualTurkeyHat.PrimalItemSkin_TT_ActualTurkeyHat\'"',
            'name': 'Turkey Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/94/Turkey_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_TT_ActualTurkeyHat_C', 'id': 716,
            'description': 'You can use this to skin the appearance of a helmet or hat. No one can call you a chicken.',
            'url': 'https://ark.fandom.com/wiki/Turkey_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_Club_TurkeyLeg.PrimalItemSkin_TT_Club_TurkeyLeg\'"',
            'name': 'Turkey Leg Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e1/Turkey_Leg_Skin.png',
            'class_name': 'PrimalItemSkin_TT_Club_TurkeyLeg_C', 'id': 717,
            'description': "You can use this to skin the appearance of a club. Hit 'em right in the dark meat!",
            'url': 'https://ark.fandom.com/wiki/Turkey_Leg_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimPants_TurkeyBerry.PrimalItemSkin_TT_SwimPants_TurkeyBerry\'"',
            'name': 'Turkey Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/cc/Turkey_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_TT_SwimPants_TurkeyBerry_C', 'id': 718,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  Give thanks for another great day on the beach.',
            'url': 'https://ark.fandom.com/wiki/Turkey_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TT_SwimShirt_TurkeyBerry.PrimalItemSkin_TT_SwimShirt_TurkeyBerry\'"',
            'name': 'Turkey Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Turkey_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_TT_SwimShirt_TurkeyBerry_C', 'id': 719,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  Give thanks for another great day on the beach.',
            'url': 'https://ark.fandom.com/wiki/Turkey_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweaterBronto.PrimalItemSkin_WW_XmasSweaterBronto\'"',
            'name': 'Ugly Bronto Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d4/Ugly_Bronto_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_WW_XmasSweaterBronto_C', 'id': 720,
            'description': 'You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Brontos are good for hanging lights in high places.',
            'url': 'https://ark.fandom.com/wiki/Ugly_Bronto_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweater_Bulbdog.PrimalItemSkin_WW_XmasSweater_Bulbdog\'"',
            'name': 'Ugly Bulbdog Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/15/Ugly_Bulbdog_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_WW_XmasSweater_Bulbdog_C', 'id': 721,
            'description': "You can use this to skin the appearance of a shirt into an ugly holiday sweater.  With a bulb so shiny, you'll even say it glows.",
            'url': 'https://ark.fandom.com/wiki/Ugly_Bulbdog_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweaterCarno.PrimalItemSkin_WW_XmasSweaterCarno\'"',
            'name': 'Ugly Carno Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/bb/Ugly_Carno_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_WW_XmasSweaterCarno_C', 'id': 722,
            'description': 'You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Holiday carols make some dinos hungry.',
            'url': 'https://ark.fandom.com/wiki/Ugly_Carno_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweater_Carolers.PrimalItemSkin_WW_XmasSweater_Carolers\'"',
            'name': 'Ugly Caroling Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/30/Ugly_Caroling_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_WW_XmasSweater_Carolers_C', 'id': 723,
            'description': 'You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Warm yourself up with this roaring choir.',
            'url': 'https://ark.fandom.com/wiki/Ugly_Caroling_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweaterChibi.PrimalItemSkin_WW_XmasSweaterChibi\'"',
            'name': 'Ugly Chibi Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Ugly_Chibi_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_WW_XmasSweaterChibi_C', 'id': 724,
            'description': "You can use this to skin the appearance of a shirt into an ugly holiday sweater.  Dinos make great gifts — when they're chibi-sized.",
            'url': 'https://ark.fandom.com/wiki/Ugly_Chibi_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Sweater_Cornucopia.PrimalItemSkin_Sweater_Cornucopia\'"',
            'name': 'Ugly Cornucopia Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/72/Ugly_Cornucopia_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_Sweater_Cornucopia_C', 'id': 725,
            'description': "You can use this to skin the appearance of a shirt into an ugly holiday sweater. Harvest season means there's plenty to go around!",
            'url': 'https://ark.fandom.com/wiki/Ugly_Cornucopia_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_XmasSweater_Rex.PrimalItemSkin_WW_XmasSweater_Rex\'"',
            'name': 'Ugly T-Rex Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/43/Ugly_T-Rex_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_WW_XmasSweater_Rex_C', 'id': 726,
            'description': "You can use this to skin the appearance of a shirt into an ugly holiday sweater.  It's not the size of your arms, it's what you've got in the sack.",
            'url': 'https://ark.fandom.com/wiki/Ugly_T-Rex_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Sweater_Trike.PrimalItemSkin_Sweater_Trike\'"',
            'name': 'Ugly Trike Sweater Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/26/Ugly_Trike_Sweater_Skin.png',
            'class_name': 'PrimalItemSkin_Sweater_Trike_C', 'id': 727,
            'description': 'You can use this to skin the appearance of a shirt into an ugly holiday sweater. Fall foliage and triceratops, uh, plumage...?',
            'url': 'https://ark.fandom.com/wiki/Ugly_Trike_Sweater_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_TopHat_Summer.PrimalItemSkin_TopHat_Summer\'"',
            'name': 'Uncle Sam Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a1/Uncle_Sam_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_TopHat_Summer_C', 'id': 728,
            'description': 'You can use this to skin the appearance of a helmet or hat.  I want YOU to survive in star-spangled style.',
            'url': 'https://ark.fandom.com/wiki/Uncle_Sam_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_Underwear_VampireDodo.PrimalItemSkin_FE_Underwear_VampireDodo\'"',
            'name': 'Vampire Dodo Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4a/Vampire_Dodo_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_FE_Underwear_VampireDodo_C', 'id': 729,
            'description': "You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women.  A swim suit so cute it's scary -- but stay away from garlic.",
            'url': 'https://ark.fandom.com/wiki/Vampire_Dodo_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_FE_SwimShirt_VampireDodo.PrimalItemSkin_FE_SwimShirt_VampireDodo\'"',
            'name': 'Vampire Dodo Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4e/Vampire_Dodo_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_FE_SwimShirt_VampireDodo_C', 'id': 730,
            'description': "You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women.  A swim suit so cute it's scary -- but stay away from garlic.",
            'url': 'https://ark.fandom.com/wiki/Vampire_Dodo_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_VampireEyes.PrimalItemSkin_VampireEyes\'"',
            'name': 'Vampire Eyes Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Vampire_Eyes_Skin.png',
            'class_name': 'PrimalItemSkin_VampireEyes_C', 'id': 731,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a bloodthirsty look.',
            'url': 'https://ark.fandom.com/wiki/Vampire_Eyes_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/ PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_Flamethrower_SuperSoaker.PrimalItemSkin_Flamethrower_SuperSoaker\'"',
            'name': 'Water Soaker Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f4/Water_Soaker_Skin.png',
            'class_name': 'PrimalItemSkin_Flamethrower_SuperSoaker_C', 'id': 732,
            'description': "You can use this to skin the appearance of a Flamethrower. Someone's getting wet!",
            'url': 'https://ark.fandom.com/wiki/Water_Soaker_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WerewolfHat.PrimalItemSkin_WerewolfHat\'"',
            'name': 'Werewolf Mask Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/33/Werewolf_Mask_Skin.png',
            'class_name': 'PrimalItemSkin_WerewolfHat_C', 'id': 733,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a wolfish look.',
            'url': 'https://ark.fandom.com/wiki/Werewolf_Mask_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WitchHat.PrimalItemSkin_WitchHat\'"',
            'name': 'Witch Hat Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Witch_Hat_Skin.png',
            'class_name': 'PrimalItemSkin_WitchHat_C', 'id': 734,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a bewitching look.',
            'url': 'https://ark.fandom.com/wiki/Witch_Hat_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Leather/PrimalItem_Skin_Account_DevKitMaster.PrimalItem_Skin_Account_DevKitMaster\'"',
            'name': 'Wizard Ballcap Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3b/Wizard_Ballcap_Skin.png',
            'class_name': 'PrimalItem_Skin_Account_DevKitMaster_C', 'id': 735,
            'description': 'You can use this to skin the appearance of a helmet or hat. Provides a mystical look!',
            'url': 'https://ark.fandom.com/wiki/Wizard_Ballcap_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Saddles/PrimalItemCostume_BoneWyvern.PrimalItemCostume_BoneWyvern\'"',
            'name': 'Wyvern Bone Costume', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e4/Wyvern_Bone_Costume.png',
            'class_name': 'PrimalItemCostume_BoneWyvern_C', 'id': 736,
            'description': 'This costume can be used to make your Wyvern look just like a skeleton! Spoopy!',
            'url': 'https://ark.fandom.com/wiki/Wyvern_Bone_Costume'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WyvernGloves.PrimalItemSkin_WyvernGloves\'"',
            'name': 'Wyvern Gloves Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9a/Wyvern_Gloves_Skin_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItemSkin_WyvernGloves_C', 'id': 737,
            'description': 'You can use this to skin the appearance of gloves. Provides a dangerous look!',
            'url': 'https://ark.fandom.com/wiki/Wyvern_Gloves_Skin_(Scorched_Earth)'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_Underwear_Yeti.PrimalItemSkin_WW_Underwear_Yeti\'"',
            'name': 'Yeti Swim Bottom Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2c/Yeti_Swim_Bottom_Skin.png',
            'class_name': 'PrimalItemSkin_WW_Underwear_Yeti_C', 'id': 738,
            'description': 'You can use this to skin the appearance of pants into swim trunks on men or a bikini bottom on women. For swimmers with abominable taste in swimwear.',
            'url': 'https://ark.fandom.com/wiki/Yeti_Swim_Bottom_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Armor/Skin/PrimalItemSkin_WW_SwimShirt_Yeti.PrimalItemSkin_WW_SwimShirt_Yeti\'"',
            'name': 'Yeti Swim Top Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/41/Yeti_Swim_Top_Skin.png',
            'class_name': 'PrimalItemSkin_WW_SwimShirt_Yeti_C', 'id': 739,
            'description': 'You can use this to skin the appearance of a shirt into a bare chest on men or a bikini top on women. For swimmers with abominable taste in swimwear.',
            'url': 'https://ark.fandom.com/wiki/Yeti_Swim_Top_Skin'
        },
        {
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Items/Armor/PrimalItemArmor_ZiplineMotor.PrimalItemArmor_ZiplineMotor\'"',
            'name': 'Zip-Line Motor Attachment Skin', 'stack_size': 1,
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/22/Zip-Line_Motor_Attachment_Skin_%28Aberration%29.png',
            'class_name': 'PrimalItemArmor_ZiplineMotor_C', 'id': 740,
            'description': 'Equip onto pants and combine with Gasoline to power yourself up a Zip-Line.',
            'url': 'https://ark.fandom.com/wiki/Zip-Line_Motor_Attachment_Skin_(Aberration)'
        }
    ]
    models.Skin.bulk_insert(items)
