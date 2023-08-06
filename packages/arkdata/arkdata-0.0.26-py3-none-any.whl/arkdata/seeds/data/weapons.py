from arkdata import models


def seed():
    items = [
        {
            'id': 1, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponGun.PrimalItem_WeaponGun\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Simple_Pistol.png',
            'class_name': 'PrimalItem_WeaponGun_C', 'name': 'Simple Pistol',
            'description': 'This simple revolver trades accuracy for flexibility.',
            'url': 'https://ark.fandom.com/wiki/Simple_Pistol'
        },
        {
            'id': 2, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponRifle.PrimalItem_WeaponRifle\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e0/Assault_Rifle.png',
            'class_name': 'PrimalItem_WeaponRifle_C', 'name': 'Assault Rifle',
            'description': 'The fastest way to fill a target with holes.',
            'url': 'https://ark.fandom.com/wiki/Assault_Rifle'
        },
        {
            'id': 3, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponRocketLauncher.PrimalItem_WeaponRocketLauncher\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Rocket_Launcher.png',
            'class_name': 'PrimalItem_WeaponRocketLauncher_C', 'name': 'Rocket Launcher',
            'description': "Mankind's ultimate portable killing device.",
            'url': 'https://ark.fandom.com/wiki/Rocket_Launcher'
        },
        {
            'id': 5, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponBow.PrimalItem_WeaponBow\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Bow.png',
            'class_name': 'PrimalItem_WeaponBow_C', 'name': 'Bow',
            'description': 'Masters of the bow often became great conquerors. Requires arrows to fire.',
            'url': 'https://ark.fandom.com/wiki/Bow'
        },
        {
            'id': 6, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponGrenade.PrimalItem_WeaponGrenade\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Grenade.png',
            'class_name': 'PrimalItem_WeaponGrenade_C', 'name': 'Grenade',
            'description': "Pulling the pin starts a 5 second timer to an explosion. Make sure you've thrown it by then.",
            'url': 'https://ark.fandom.com/wiki/Grenade'
        },
        {
            'id': 42, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponC4.PrimalItem_WeaponC4\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/85/C4_Remote_Detonator.png',
            'class_name': 'PrimalItem_WeaponC4_C', 'name': 'C4 Remote Detonator',
            'description': 'This device uses radio waves to detonate all primed C4 packages on the same frequency.',
            'url': 'https://ark.fandom.com/wiki/C4_Remote_Detonator'
        },
        {
            'id': 46, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTripwireC4.PrimalItem_WeaponTripwireC4\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/15/Improvised_Explosive_Device.png',
            'class_name': 'PrimalItem_WeaponTripwireC4_C', 'name': 'Improvised Explosive Device',
            'description': 'Place two of these near each other to create an explosive trap.',
            'url': 'https://ark.fandom.com/wiki/Improvised_Explosive_Device'
        },
        {
            'id': 57, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSpear.PrimalItem_WeaponSpear\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Spear.png',
            'class_name': 'PrimalItem_WeaponSpear_C', 'name': 'Spear',
            'description': 'An easily made melee weapon that can also be thrown. Has a chance to break when used.',
            'url': 'https://ark.fandom.com/wiki/Spear'
        },
        {
            'id': 131, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponOneShotRifle.PrimalItem_WeaponOneShotRifle\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a2/Longneck_Rifle.png',
            'class_name': 'PrimalItem_WeaponOneShotRifle_C', 'name': 'Longneck Rifle',
            'description': 'This simple single-shot rifle is highly accurate, but has a long reload time.',
            'url': 'https://ark.fandom.com/wiki/Longneck_Rifle'
        },
        {
            'id': 138, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSlingshot.PrimalItem_WeaponSlingshot\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3f/Slingshot.png',
            'class_name': 'PrimalItem_WeaponSlingshot_C', 'name': 'Slingshot',
            'description': 'A simple ranged weapon that deals damage from afar. Better for knocking out a target than killing it outright. Requires stone to fire.',
            'url': 'https://ark.fandom.com/wiki/Slingshot'
        },
        {
            'id': 139, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponPike.PrimalItem_WeaponPike\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Pike.png',
            'class_name': 'PrimalItem_WeaponPike_C', 'name': 'Pike',
            'description': 'A powerful weapon tipped with metal. Unlike the spear, it cannot be thrown.',
            'url': 'https://ark.fandom.com/wiki/Pike'
        },
        {
            'id': 181, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponFlareGun.PrimalItem_WeaponFlareGun\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/57/Flare_Gun.png',
            'class_name': 'PrimalItem_WeaponFlareGun_C', 'name': 'Flare Gun',
            'description': 'A single-use flare launcher. Fires a bright ball of Sparkpowder to temporarily light an area.',
            'url': 'https://ark.fandom.com/wiki/Flare_Gun'
        },
        {
            'id': 240, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMachinedPistol.PrimalItem_WeaponMachinedPistol\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Fabricated_Pistol.png',
            'class_name': 'PrimalItem_WeaponMachinedPistol_C', 'name': 'Fabricated Pistol',
            'description': 'This advanced pistol gains a high rate of fire and a large magazine size by sacrificing stopping power.',
            'url': 'https://ark.fandom.com/wiki/Fabricated_Pistol'
        },
        {
            'id': 263, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponShotgun.PrimalItem_WeaponShotgun\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Shotgun.png',
            'class_name': 'PrimalItem_WeaponShotgun_C', 'name': 'Shotgun',
            'description': 'Very powerful up close, but less reliable with range.',
            'url': 'https://ark.fandom.com/wiki/Shotgun'
        },
        {
            'id': 321, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponPoisonTrap.PrimalItem_WeaponPoisonTrap\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ab/Tripwire_Narcotic_Trap.png',
            'class_name': 'PrimalItem_WeaponPoisonTrap_C', 'name': 'Tripwire Narcotic Trap',
            'description': 'Place two of these near each other to create a poisonous trap.',
            'url': 'https://ark.fandom.com/wiki/Tripwire_Narcotic_Trap'
        },
        {
            'id': 322, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponAlarmTrap.PrimalItem_WeaponAlarmTrap\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Tripwire_Alarm_Trap.png',
            'class_name': 'PrimalItem_WeaponAlarmTrap_C', 'name': 'Tripwire Alarm Trap',
            'description': 'Place two of these near each other to create a trap.',
            'url': 'https://ark.fandom.com/wiki/Tripwire_Alarm_Trap'
        },
        {
            'id': 357, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMachinedShotgun.PrimalItem_WeaponMachinedShotgun\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Shotgun.png',
            'class_name': 'PrimalItem_WeaponMachinedShotgun_C', 'name': 'Pump-Action Shotgun',
            'description': 'Very powerful up close, but less reliable with range.',
            'url': 'https://ark.fandom.com/wiki/Pump-Action_Shotgun'
        },
        {
            'id': 358, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponCrossbow.PrimalItem_WeaponCrossbow\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/79/Crossbow.png',
            'class_name': 'PrimalItem_WeaponCrossbow_C', 'name': 'Crossbow',
            'description': 'Has significantly more power than the Bow, but cannot fire rapidly. Can be fired underwater.',
            'url': 'https://ark.fandom.com/wiki/Crossbow'
        },
        {
            'id': 368, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTransGPS.PrimalItem_WeaponTransGPS\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/66/Transponder_Tracker.png',
            'class_name': 'PrimalItem_WeaponTransGPS_C', 'name': 'Transponder Tracker',
            'description': 'Uses strange energy from the three Obelisks to triangulate all Transponder Nodes on the specified frequency.',
            'url': 'https://ark.fandom.com/wiki/Transponder_Tracker'
        },
        {
            'id': 372, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponCompoundBow.PrimalItem_WeaponCompoundBow\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9e/Compound_Bow.png',
            'class_name': 'PrimalItem_WeaponCompoundBow_C', 'name': 'Compound Bow',
            'description': 'A high-tech bow made of durable alloy, can launch arrows at high velocity. Requires arrows to fire.',
            'url': 'https://ark.fandom.com/wiki/Compound_Bow'
        },
        {
            'id': 379, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_BearTrap.PrimalItemStructure_BearTrap\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Bear_Trap.png',
            'class_name': 'PrimalItemStructure_BearTrap_C', 'name': 'Bear Trap',
            'description': 'Immobilizes humans and small creatures.', 'url': 'https://ark.fandom.com/wiki/Bear_Trap'
        },
        {
            'id': 380, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_BearTrap_Large.PrimalItemStructure_BearTrap_Large\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Large_Bear_Trap.png',
            'class_name': 'PrimalItemStructure_BearTrap_Large_C', 'name': 'Large Bear Trap',
            'description': 'Immobilizes large creatures only.', 'url': 'https://ark.fandom.com/wiki/Large_Bear_Trap'
        },
        {
            'id': 388, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSprayPaint.PrimalItem_WeaponSprayPaint\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Spray_Painter.png',
            'class_name': 'PrimalItem_WeaponSprayPaint_C', 'name': 'Spray Painter',
            'description': 'Apply a dye to this, then shoot it at structures to paint them. Hold Alt Fire + Hotkey Number to set painting region.',
            'url': 'https://ark.fandom.com/wiki/Spray_Painter'
        },
        {
            'id': 429, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponStoneClub.PrimalItem_WeaponStoneClub\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Wooden_Club.png',
            'class_name': 'PrimalItem_WeaponStoneClub_C', 'name': 'Wooden Club',
            'description': 'A easily made melee weapon that is excellent for knocking out targets. Only effective at short range.',
            'url': 'https://ark.fandom.com/wiki/Wooden_Club'
        },
        {
            'id': 430, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_PoisonGrenade.PrimalItem_PoisonGrenade\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Poison_Grenade.png',
            'class_name': 'PrimalItem_PoisonGrenade_C', 'name': 'Poison Grenade',
            'description': 'Releases narcotic smoke to knock out anything in the area - only affects humans. Pulling the pin starts a 2.5 second timer to the gas release.',
            'url': 'https://ark.fandom.com/wiki/Poison_Grenade'
        },
        {
            'id': 431, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMachinedSniper.PrimalItem_WeaponMachinedSniper\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9e/Fabricated_Sniper_Rifle.png',
            'class_name': 'PrimalItem_WeaponMachinedSniper_C', 'name': 'Fabricated Sniper Rifle',
            'description': 'This semi-automatic rifle has less punch than a Longneck Rifle, but can be fired much more rapidly.',
            'url': 'https://ark.fandom.com/wiki/Fabricated_Sniper_Rifle'
        },
        {
            'id': 446, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponProd.PrimalItem_WeaponProd\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/48/Electric_Prod.png',
            'class_name': 'PrimalItem_WeaponProd_C', 'name': 'Electric Prod',
            'description': 'Powerful stunning weapon, but can only be used for a single strike before recharge is needed.',
            'url': 'https://ark.fandom.com/wiki/Electric_Prod'
        },
        {
            'id': 447, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponHandcuffs.PrimalItem_WeaponHandcuffs\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/14/Handcuffs.png',
            'class_name': 'PrimalItem_WeaponHandcuffs_C', 'name': 'Handcuffs',
            'description': "Equip this onto an unconscious player, and they'll be restrained when they wake up!",
            'url': 'https://ark.fandom.com/wiki/Handcuffs'
        },
        {
            'id': 448, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Extinction/Weapon_AdminBlinkRifle/PrimalItem_WeaponAdminBlinkRifle.PrimalItem_WeaponAdminBlinkRifle\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Admin_Blink_Rifle.png',
            'class_name': 'PrimalItem_WeaponAdminBlinkRifle_C', 'name': 'Admin Blink Rifle',
            'description': 'Admin tool for easily moving around the world, and some other misc tools',
            'url': 'https://ark.fandom.com/wiki/Admin_Blink_Rifle'
        },
        {
            'id': 449, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponBola.PrimalItem_WeaponBola\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Bola.png',
            'class_name': 'PrimalItem_WeaponBola_C', 'name': 'Bola', 'description': 'Wind it up and throw!',
            'url': 'https://ark.fandom.com/wiki/Bola'
        },
        {
            'id': 450, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/WeaponBoomerang/PrimalItem_WeaponBoomerang.PrimalItem_WeaponBoomerang\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Boomerang_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItem_WeaponBoomerang_C', 'name': 'Boomerang',
            'description': 'Your trusty ranged weapon.', 'url': 'https://ark.fandom.com/wiki/Boomerang_(Scorched_Earth)'
        },
        {
            'id': 451, 'stack_size': 20,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ChainBola.PrimalItemAmmo_ChainBola\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Chain_Bola.png',
            'class_name': 'PrimalItemAmmo_ChainBola_C', 'name': 'Chain Bola',
            'description': 'A gigantic bola made of metal chain, capable of ensnaring larger creatures. Usable within a Ballista turret.',
            'url': 'https://ark.fandom.com/wiki/Chain_Bola'
        },
        {
            'id': 452, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Aberration/WeaponRadioactiveLanternCharge/PrimalItem_WeaponRadioactiveLanternCharge.PrimalItem_WeaponRadioactiveLanternCharge\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Charge_Lantern_%28Aberration%29.png',
            'class_name': 'PrimalItem_WeaponRadioactiveLanternCharge_C', 'name': 'Charge Lantern',
            'description': 'Weaponized Charge Light that damages and stuns lifeforms. Place down to ward off dangers in an area. Uses Charge Batteries as fuel.',
            'url': 'https://ark.fandom.com/wiki/Charge_Lantern_(Aberration)'
        },
        {
            'id': 453, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Aberration/CoreBlueprints/Weapons/PrimalItem_WeaponClimbPick.PrimalItem_WeaponClimbPick\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a5/Climbing_Pick_%28Aberration%29.png',
            'class_name': 'PrimalItem_WeaponClimbPick_C', 'name': 'Climbing Pick',
            'description': 'Climb up and hang from nearly any surface with these!',
            'url': 'https://ark.fandom.com/wiki/Climbing_Pick_(Aberration)'
        },
        {
            'id': 454, 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/WeaponClusterGrenade/PrimalItem_WeaponClusterGrenade.PrimalItem_WeaponClusterGrenade\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Grenade.png',
            'class_name': 'PrimalItem_WeaponClusterGrenade_C', 'name': 'Cluster Grenade',
            'description': "Pulling the pin starts a 5 second timer to an explosion. Make sure you've thrown it by then.",
            'url': 'https://ark.fandom.com/wiki/Cluster_Grenade_(Scorched_Earth)'
        },
        {
            'id': 455, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Weapons/CruiseMissile/PrimalItem_WeaponTekCruiseMissile.PrimalItem_WeaponTekCruiseMissile\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Cruise_Missile_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItem_WeaponTekCruiseMissile_C', 'name': 'Cruise Missile',
            'description': 'A powerful Tek missile that can be controlled remotely or fired and forgotten. Equipping this requires learning its Tekgram.',
            'url': 'https://ark.fandom.com/wiki/Cruise_Missile_(Genesis:_Part_1)'
        },
        {
            'id': 456, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/WeaponFlamethrower/PrimalItem_WeapFlamethrower.PrimalItem_WeapFlamethrower\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Flamethrower_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItem_WeapFlamethrower_C', 'name': 'Flamethrower',
            'description': 'The fastest way to roast a target.',
            'url': 'https://ark.fandom.com/wiki/Flamethrower_(Scorched_Earth)'
        },
        {
            'id': 457, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/CoreBlueprints/Weapons/Mission/PrimalItem_WeaponSpear_Flame_Gauntlet.PrimalItem_WeaponSpear_Flame_Gauntlet\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Spear.png',
            'class_name': 'PrimalItem_WeaponSpear_Flame_Gauntlet_C', 'name': 'Flaming Spear',
            'description': 'An easily made melee weapon that can also be thrown. Has a chance to break when used.',
            'url': 'https://ark.fandom.com/wiki/Flaming_Spear_(Genesis:_Part_1)'
        },
        {
            'id': 458, 'stack_size': 20,
            'blueprint': '"Blueprint\'/Game/Aberration/WeaponGlowStickThrow/PrimalItem_GlowStick.PrimalItem_GlowStick\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6c/Glow_Stick_%28Aberration%29.png',
            'class_name': 'PrimalItem_GlowStick_C', 'name': 'Glow Stick',
            'description': 'Glow Sticks generate light in a radius around them. Throw it and it will stick immediately to the location they first impact.',
            'url': 'https://ark.fandom.com/wiki/Glow_Stick_(Aberration)'
        },
        {
            'id': 459, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponHarpoon.PrimalItem_WeaponHarpoon\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Harpoon_Launcher.png',
            'class_name': 'PrimalItem_WeaponHarpoon_C', 'name': 'Harpoon Launcher',
            'description': 'Has tremendous power and speed underwater, but ineffective range out of water. Uses Spear Bolts for ammunition.',
            'url': 'https://ark.fandom.com/wiki/Harpoon_Launcher'
        },
        {
            'id': 460, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponLance.PrimalItem_WeaponLance\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f8/Lance.png',
            'class_name': 'PrimalItem_WeaponLance_C', 'name': 'Lance',
            'description': 'Knock your foes off their mounts! Can only be utilized when riding a mount.',
            'url': 'https://ark.fandom.com/wiki/Lance'
        },
        {
            'id': 461, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponLasso.PrimalItem_WeaponLasso\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Lasso.png',
            'class_name': 'PrimalItem_WeaponLasso_C', 'name': 'Lasso',
            'description': 'An easily-crafted ranged tool that can ensnare and pull a target. Can only be wielded when riding a certain creature.',
            'url': 'https://ark.fandom.com/wiki/Lasso'
        },
        {
            'id': 462, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/ScorchedEarth/WeaponOilJar/PrimalItem_WeaponOilJar.PrimalItem_WeaponOilJar\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c1/Oil_Jar_%28Scorched_Earth%29.png',
            'class_name': 'PrimalItem_WeaponOilJar_C', 'name': 'Oil Jar',
            'description': 'Throw it to create an oil slick which can be lit on fire! This sticky substance can also slow people down which step in it!',
            'url': 'https://ark.fandom.com/wiki/Oil_Jar_(Scorched_Earth)'
        },
        {
            'id': 463, 'stack_size': 100,
            'blueprint': '"Blueprint\'/Game/Aberration/WeaponPlantSpeciesZ/PrimalItem_PlantSpeciesZ_Grenade.PrimalItem_PlantSpeciesZ_Grenade\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Plant_Species_Z_Fruit_%28Aberration%29.png',
            'class_name': 'PrimalItem_PlantSpeciesZ_Grenade_C', 'name': 'Plant Species Z Fruit',
            'description': 'Bioluminescent Fruit that provides a flash of Charge lighting',
            'url': 'https://ark.fandom.com/wiki/Plant_Species_Z_Fruit_(Aberration)'
        },
        {
            'id': 464, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Extinction/Dinos/Scout/PrimalItem_WeaponScoutRemote.PrimalItem_WeaponScoutRemote\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Scout_Remote_%28Extinction%29.png',
            'class_name': 'PrimalItem_WeaponScoutRemote_C', 'name': 'Scout Remote', 'description': None,
            'url': 'https://ark.fandom.com/wiki/Scout_Remote_(Extinction)'
        },
        {
            'id': 465, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_GasGrenade.PrimalItem_GasGrenade\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Smoke_Grenade.png',
            'class_name': 'PrimalItem_GasGrenade_C', 'name': 'Smoke Grenade',
            'description': 'Releases a lot of smoke to obscure your plans. Pulling the pin starts a 5 second timer to an explosion.',
            'url': 'https://ark.fandom.com/wiki/Smoke_Grenade'
        },
        {
            'id': 466, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSword.PrimalItem_WeaponSword\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/89/Sword.png',
            'class_name': 'PrimalItem_WeaponSword_C', 'name': 'Sword',
            'description': 'The undisputed ruler of short-range combat. Needs a hotter flame to be forged.',
            'url': 'https://ark.fandom.com/wiki/Sword'
        },
        {
            'id': 467, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Weapons/TekHandBlades/PrimalItem_WeaponTekClaws.PrimalItem_WeaponTekClaws\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Tek_Claws_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItem_WeaponTekClaws_C', 'name': 'Tek Claws',
            'description': 'Rips through metal and armor when infused with Element and can chain hits to temporarily increase their speed and damage. Equipping this requires learning its Tekgram.',
            'url': 'https://ark.fandom.com/wiki/Tek_Claws_(Genesis:_Part_1)'
        },
        {
            'id': 468, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/Extinction/CoreBlueprints/Weapons/PrimalItem_WeaponTekGravityGrenade.PrimalItem_WeaponTekGravityGrenade\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/51/Tek_Gravity_Grenade_%28Extinction%29.png',
            'class_name': 'PrimalItem_WeaponTekGravityGrenade_C', 'name': 'Tek Gravity Grenade',
            'description': "Pulling the pin starts a 5 second timer to an explosion. Make sure you've thrown it by then.",
            'url': 'https://ark.fandom.com/wiki/Tek_Gravity_Grenade_(Extinction)'
        },
        {
            'id': 469, 'stack_size': 10,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_TekGrenade.PrimalItem_TekGrenade\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/75/Tek_Grenade.png',
            'class_name': 'PrimalItem_TekGrenade_C', 'name': 'Tek Grenade',
            'description': 'Sticks to targets with a powerful Tek Explosion after 5 seconds. Equipping requires learning this Tekgram.',
            'url': 'https://ark.fandom.com/wiki/Tek_Grenade'
        },
        {
            'id': 470, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Genesis/Weapons/TekGrenadeLauncher/PrimalItem_WeaponTekGrenadeLauncher.PrimalItem_WeaponTekGrenadeLauncher\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Tek_Grenade_Launcher_%28Genesis_Part_1%29.png',
            'class_name': 'PrimalItem_WeaponTekGrenadeLauncher_C', 'name': 'Tek Grenade Launcher',
            'description': 'An advanced launcher that can shoot various grenade types and can enable on-impact explosions. Equipping this requires learning its Tekgram.',
            'url': 'https://ark.fandom.com/wiki/Tek_Grenade_Launcher_(Genesis:_Part_1)'
        },
        {
            'id': 471, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/Aberration/WeaponTekSniper/PrimalItem_TekSniper.PrimalItem_TekSniper\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Tek_Railgun_%28Aberration%29.png',
            'class_name': 'PrimalItem_TekSniper_C', 'name': 'Tek Railgun',
            'description': 'Shoots explosive plasma bolts, with an infrared zoomable scope. Equipping requires learning this Tekgram.',
            'url': 'https://ark.fandom.com/wiki/Tek_Railgun_(Aberration)'
        },
        {
            'id': 472, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_TekRifle.PrimalItem_TekRifle\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d4/Tek_Rifle.png',
            'class_name': 'PrimalItem_TekRifle_C', 'name': 'Tek Rifle',
            'description': 'Shoots explosive plasma bolts, with an infrared zoomable scope. Equipping requires learning this Tekgram.',
            'url': 'https://ark.fandom.com/wiki/Tek_Rifle'
        },
        {
            'id': 473, 'stack_size': 1,
            'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTekSword.PrimalItem_WeaponTekSword\'"',
            'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9b/Tek_Sword_%28Ragnarok%29.png',
            'class_name': 'PrimalItem_WeaponTekSword_C', 'name': 'Tek Sword',
            'description': 'Cuts through metal and armor when infused with Element, and supports a Charge Attack. Equipping requires learning this Tekgram.',
            'url': 'https://ark.fandom.com/wiki/Tek_Sword'
        }
    ]
    models.Weapon.bulk_insert(items)


def backup_seed():
    models.Weapon.new(id=429, name='Wooden Club', stack_size=1, class_name='PrimalItem_WeaponStoneClub_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponStoneClub.PrimalItem_WeaponStoneClub\'"',
                      url='https://ark.fandom.com/wiki/Wooden_Club',
                      description='A easily made melee weapon that is excellent for knocking out targets. Only effective at short range.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Wooden_Club.png')
    models.Weapon.new(id=321, name='Tripwire Narcotic Trap', stack_size=10, class_name='PrimalItem_WeaponPoisonTrap_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponPoisonTrap.PrimalItem_WeaponPoisonTrap\'"',
                      url='https://ark.fandom.com/wiki/Tripwire_Narcotic_Trap',
                      description='Place two of these near each other to create a poisonous trap.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ab/Tripwire_Narcotic_Trap.png')
    models.Weapon.new(id=322, name='Tripwire Alarm Trap', stack_size=10, class_name='PrimalItem_WeaponAlarmTrap_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponAlarmTrap.PrimalItem_WeaponAlarmTrap\'"',
                      url='https://ark.fandom.com/wiki/Tripwire_Alarm_Trap',
                      description='Place two of these near each other to create a trap.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Tripwire_Alarm_Trap.png')
    models.Weapon.new(id=368, name='Transponder Tracker', stack_size=1, class_name='PrimalItem_WeaponTransGPS_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTransGPS.PrimalItem_WeaponTransGPS\'"',
                      url='https://ark.fandom.com/wiki/Transponder_Tracker',
                      description='Uses strange energy from the three Obelisks to triangulate all Transponder Nodes on the specified frequency.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/66/Transponder_Tracker.png')
    models.Weapon.new(id=388, name='Spray Painter', stack_size=1, class_name='PrimalItem_WeaponSprayPaint_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSprayPaint.PrimalItem_WeaponSprayPaint\'"',
                      url='https://ark.fandom.com/wiki/Spray_Painter',
                      description='Apply a dye to this, then shoot it at structures to paint them. Hold Alt Fire + Hotkey Number to set painting region.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/38/Spray_Painter.png')
    models.Weapon.new(id=57, name='Spear', stack_size=10, class_name='PrimalItem_WeaponSpear_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSpear.PrimalItem_WeaponSpear\'"',
                      url='https://ark.fandom.com/wiki/Spear',
                      description='An easily made melee weapon that can also be thrown. Has a chance to break when used.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Spear.png')
    models.Weapon.new(id=138, name='Slingshot', stack_size=1, class_name='PrimalItem_WeaponSlingshot_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSlingshot.PrimalItem_WeaponSlingshot\'"',
                      url='https://ark.fandom.com/wiki/Slingshot',
                      description='A simple ranged weapon that deals damage from afar. Better for knocking out a target than killing it outright. Requires stone to fire.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/3f/Slingshot.png')
    models.Weapon.new(id=1, name='Simple Pistol', stack_size=1, class_name='PrimalItem_WeaponGun_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponGun.PrimalItem_WeaponGun\'"',
                      url='https://ark.fandom.com/wiki/Simple_Pistol',
                      description='This simple revolver trades accuracy for flexibility.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d0/Simple_Pistol.png')
    models.Weapon.new(id=263, name='Shotgun', stack_size=1, class_name='PrimalItem_WeaponShotgun_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponShotgun.PrimalItem_WeaponShotgun\'"',
                      url='https://ark.fandom.com/wiki/Shotgun',
                      description='Very powerful up close, but less reliable with range.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Shotgun.png')
    models.Weapon.new(id=3, name='Rocket Launcher', stack_size=1, class_name='PrimalItem_WeaponRocketLauncher_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponRocketLauncher.PrimalItem_WeaponRocketLauncher\'"',
                      url='https://ark.fandom.com/wiki/Rocket_Launcher',
                      description="Mankind's ultimate portable killing device.",
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Rocket_Launcher.png')
    models.Weapon.new(id=357, name='Pump-Action Shotgun', stack_size=1, class_name='PrimalItem_WeaponMachinedShotgun_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMachinedShotgun.PrimalItem_WeaponMachinedShotgun\'"',
                      url='https://ark.fandom.com/wiki/Pump-Action_Shotgun',
                      description='Very powerful up close, but less reliable with range.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/61/Shotgun.png')
    models.Weapon.new(id=430, name='Poison Grenade', stack_size=10, class_name='PrimalItem_PoisonGrenade_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_PoisonGrenade.PrimalItem_PoisonGrenade\'"',
                      url='https://ark.fandom.com/wiki/Poison_Grenade',
                      description='Releases narcotic smoke to knock out anything in the area - only affects humans. Pulling the pin starts a 2.5 second timer to the gas release.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/0/05/Poison_Grenade.png')
    models.Weapon.new(id=139, name='Pike', stack_size=1, class_name='PrimalItem_WeaponPike_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponPike.PrimalItem_WeaponPike\'"',
                      url='https://ark.fandom.com/wiki/Pike',
                      description='A powerful weapon tipped with metal. Unlike the spear, it cannot be thrown.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/31/Pike.png')
    models.Weapon.new(id=131, name='Longneck Rifle', stack_size=1, class_name='PrimalItem_WeaponOneShotRifle_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponOneShotRifle.PrimalItem_WeaponOneShotRifle\'"',
                      url='https://ark.fandom.com/wiki/Longneck_Rifle',
                      description='This simple single-shot rifle is highly accurate, but has a long reload time.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a2/Longneck_Rifle.png')
    models.Weapon.new(id=380, name='Large Bear Trap', stack_size=10, class_name='PrimalItemStructure_BearTrap_Large_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_BearTrap_Large.PrimalItemStructure_BearTrap_Large\'"',
                      url='https://ark.fandom.com/wiki/Large_Bear_Trap',
                      description='Immobilizes large creatures only.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7c/Large_Bear_Trap.png')
    models.Weapon.new(id=46, name='Improvised Explosive Device', stack_size=10,
                      class_name='PrimalItem_WeaponTripwireC4_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTripwireC4.PrimalItem_WeaponTripwireC4\'"',
                      url='https://ark.fandom.com/wiki/Improvised_Explosive_Device',
                      description='Place two of these near each other to create an explosive trap.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/15/Improvised_Explosive_Device.png')
    models.Weapon.new(id=447, name='Handcuffs', stack_size=1, class_name='PrimalItem_WeaponHandcuffs_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponHandcuffs.PrimalItem_WeaponHandcuffs\'"',
                      url='https://ark.fandom.com/wiki/Handcuffs',
                      description="Equip this onto an unconscious player, and they'll be restrained when they wake up!",
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/14/Handcuffs.png')
    models.Weapon.new(id=6, name='Grenade', stack_size=10, class_name='PrimalItem_WeaponGrenade_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponGrenade.PrimalItem_WeaponGrenade\'"',
                      url='https://ark.fandom.com/wiki/Grenade',
                      description="Pulling the pin starts a 5 second timer to an explosion. Make sure you've thrown it by then.",
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Grenade.png')
    models.Weapon.new(id=181, name='Flare Gun', stack_size=10, class_name='PrimalItem_WeaponFlareGun_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponFlareGun.PrimalItem_WeaponFlareGun\'"',
                      url='https://ark.fandom.com/wiki/Flare_Gun',
                      description='A single-use flare launcher. Fires a bright ball of Sparkpowder to temporarily light an area.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/57/Flare_Gun.png')
    models.Weapon.new(id=431, name='Fabricated Sniper Rifle', stack_size=1,
                      class_name='PrimalItem_WeaponMachinedSniper_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMachinedSniper.PrimalItem_WeaponMachinedSniper\'"',
                      url='https://ark.fandom.com/wiki/Fabricated_Sniper_Rifle',
                      description='This semi-automatic rifle has less punch than a Longneck Rifle, but can be fired much more rapidly.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9e/Fabricated_Sniper_Rifle.png')
    models.Weapon.new(id=240, name='Fabricated Pistol', stack_size=1, class_name='PrimalItem_WeaponMachinedPistol_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMachinedPistol.PrimalItem_WeaponMachinedPistol\'"',
                      url='https://ark.fandom.com/wiki/Fabricated_Pistol',
                      description='This advanced pistol gains a high rate of fire and a large magazine size by sacrificing stopping power.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2e/Fabricated_Pistol.png')
    models.Weapon.new(id=446, name='Electric Prod', stack_size=1, class_name='PrimalItem_WeaponProd_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponProd.PrimalItem_WeaponProd\'"',
                      url='https://ark.fandom.com/wiki/Electric_Prod',
                      description='Powerful stunning weapon, but can only be used for a single strike before recharge is needed.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/48/Electric_Prod.png')
    models.Weapon.new(id=358, name='Crossbow', stack_size=1, class_name='PrimalItem_WeaponCrossbow_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponCrossbow.PrimalItem_WeaponCrossbow\'"',
                      url='https://ark.fandom.com/wiki/Crossbow',
                      description='Has significantly more power than the Bow, but cannot fire rapidly. Can be fired underwater.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/79/Crossbow.png')
    models.Weapon.new(id=372, name='Compound Bow', stack_size=1, class_name='PrimalItem_WeaponCompoundBow_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponCompoundBow.PrimalItem_WeaponCompoundBow\'"',
                      url='https://ark.fandom.com/wiki/Compound_Bow',
                      description='A high-tech bow made of durable alloy, can launch arrows at high velocity. Requires arrows to fire.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9e/Compound_Bow.png')
    models.Weapon.new(id=42, name='C4 Remote Detonator', stack_size=1, class_name='PrimalItem_WeaponC4_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponC4.PrimalItem_WeaponC4\'"',
                      url='https://ark.fandom.com/wiki/C4_Remote_Detonator',
                      description='This device uses radio waves to detonate all primed C4 packages on the same frequency.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/85/C4_Remote_Detonator.png')
    models.Weapon.new(id=5, name='Bow', stack_size=1, class_name='PrimalItem_WeaponBow_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponBow.PrimalItem_WeaponBow\'"',
                      url='https://ark.fandom.com/wiki/Bow',
                      description='Masters of the bow often became great conquerors. Requires arrows to fire.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/65/Bow.png')
    models.Weapon.new(id=379, name='Bear Trap', stack_size=10, class_name='PrimalItemStructure_BearTrap_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_BearTrap.PrimalItemStructure_BearTrap\'"',
                      url='https://ark.fandom.com/wiki/Bear_Trap',
                      description='Immobilizes humans and small creatures.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/92/Bear_Trap.png')
    models.Weapon.new(id=2, name='Assault Rifle', stack_size=1, class_name='PrimalItem_WeaponRifle_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponRifle.PrimalItem_WeaponRifle\'"',
                      url='https://ark.fandom.com/wiki/Assault_Rifle',
                      description='The fastest way to fill a target with holes.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/e0/Assault_Rifle.png')
    models.Weapon.new(name='Admin Blink Rifle', stack_size=1, class_name='PrimalItem_WeaponAdminBlinkRifle_C',
                      blueprint='"Blueprint\'/Game/Extinction/Weapon_AdminBlinkRifle/PrimalItem_WeaponAdminBlinkRifle.PrimalItem_WeaponAdminBlinkRifle\'"',
                      url='https://ark.fandom.com/wiki/Admin_Blink_Rifle',
                      description='Admin tool for easily moving around the world, and some other misc tools',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6b/Admin_Blink_Rifle.png')
    models.Weapon.new(name='Bola', stack_size=10, class_name='PrimalItem_WeaponBola_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponBola.PrimalItem_WeaponBola\'"',
                      url='https://ark.fandom.com/wiki/Bola', description='Wind it up and throw!',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/ae/Bola.png')
    models.Weapon.new(name='Boomerang', stack_size=10, class_name='PrimalItem_WeaponBoomerang_C',
                      blueprint='"Blueprint\'/Game/ScorchedEarth/WeaponBoomerang/PrimalItem_WeaponBoomerang.PrimalItem_WeaponBoomerang\'"',
                      url='https://ark.fandom.com/wiki/Boomerang_(Scorched_Earth)',
                      description='Your trusty ranged weapon.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/17/Boomerang_%28Scorched_Earth%29.png')
    models.Weapon.new(name='Chain Bola', stack_size=20, class_name='PrimalItemAmmo_ChainBola_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItemAmmo_ChainBola.PrimalItemAmmo_ChainBola\'"',
                      url='https://ark.fandom.com/wiki/Chain_Bola',
                      description='A gigantic bola made of metal chain, capable of ensnaring larger creatures. Usable within a Ballista turret.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/25/Chain_Bola.png')
    models.Weapon.new(name='Charge Lantern', stack_size=1, class_name='PrimalItem_WeaponRadioactiveLanternCharge_C',
                      blueprint='"Blueprint\'/Game/Aberration/WeaponRadioactiveLanternCharge/PrimalItem_WeaponRadioactiveLanternCharge.PrimalItem_WeaponRadioactiveLanternCharge\'"',
                      url='https://ark.fandom.com/wiki/Charge_Lantern_(Aberration)',
                      description='Weaponized Charge Light that damages and stuns lifeforms. Place down to ward off dangers in an area. Uses Charge Batteries as fuel.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/8a/Charge_Lantern_%28Aberration%29.png')
    models.Weapon.new(name='Climbing Pick', stack_size=1, class_name='PrimalItem_WeaponClimbPick_C',
                      blueprint='"Blueprint\'/Game/Aberration/CoreBlueprints/Weapons/PrimalItem_WeaponClimbPick.PrimalItem_WeaponClimbPick\'"',
                      url='https://ark.fandom.com/wiki/Climbing_Pick_(Aberration)',
                      description='Climb up and hang from nearly any surface with these!',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a5/Climbing_Pick_%28Aberration%29.png')
    models.Weapon.new(name='Cluster Grenade', stack_size=100, class_name='PrimalItem_WeaponClusterGrenade_C',
                      blueprint='"Blueprint\'/Game/ScorchedEarth/WeaponClusterGrenade/PrimalItem_WeaponClusterGrenade.PrimalItem_WeaponClusterGrenade\'"',
                      url='https://ark.fandom.com/wiki/Cluster_Grenade_(Scorched_Earth)',
                      description="Pulling the pin starts a 5 second timer to an explosion. Make sure you've thrown it by then.",
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/fb/Grenade.png')
    models.Weapon.new(name='Cruise Missile', stack_size=1, class_name='PrimalItem_WeaponTekCruiseMissile_C',
                      blueprint='"Blueprint\'/Game/Genesis/Weapons/CruiseMissile/PrimalItem_WeaponTekCruiseMissile.PrimalItem_WeaponTekCruiseMissile\'"',
                      url='https://ark.fandom.com/wiki/Cruise_Missile_(Genesis:_Part_1)',
                      description='A powerful Tek missile that can be controlled remotely or fired and forgotten. Equipping this requires learning its Tekgram.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/1/13/Cruise_Missile_%28Genesis_Part_1%29.png')
    models.Weapon.new(name='Flamethrower', stack_size=1, class_name='PrimalItem_WeapFlamethrower_C',
                      blueprint='"Blueprint\'/Game/ScorchedEarth/WeaponFlamethrower/PrimalItem_WeapFlamethrower.PrimalItem_WeapFlamethrower\'"',
                      url='https://ark.fandom.com/wiki/Flamethrower_(Scorched_Earth)',
                      description='The fastest way to roast a target.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/47/Flamethrower_%28Scorched_Earth%29.png')
    models.Weapon.new(name='Flaming Spear', stack_size=1, class_name='PrimalItem_WeaponSpear_Flame_Gauntlet_C',
                      blueprint='"Blueprint\'/Game/Genesis/CoreBlueprints/Weapons/Mission/PrimalItem_WeaponSpear_Flame_Gauntlet.PrimalItem_WeaponSpear_Flame_Gauntlet\'"',
                      url='https://ark.fandom.com/wiki/Flaming_Spear_(Genesis:_Part_1)',
                      description='An easily made melee weapon that can also be thrown. Has a chance to break when used.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/4/4f/Spear.png')
    models.Weapon.new(name='Glow Stick', stack_size=20, class_name='PrimalItem_GlowStick_C',
                      blueprint='"Blueprint\'/Game/Aberration/WeaponGlowStickThrow/PrimalItem_GlowStick.PrimalItem_GlowStick\'"',
                      url='https://ark.fandom.com/wiki/Glow_Stick_(Aberration)',
                      description='Glow Sticks generate light in a radius around them. Throw it and it will stick immediately to the location they first impact.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/6/6c/Glow_Stick_%28Aberration%29.png')
    models.Weapon.new(name='Harpoon Launcher', stack_size=1, class_name='PrimalItem_WeaponHarpoon_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponHarpoon.PrimalItem_WeaponHarpoon\'"',
                      url='https://ark.fandom.com/wiki/Harpoon_Launcher',
                      description='Has tremendous power and speed underwater, but ineffective range out of water. Uses Spear Bolts for ammunition.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ec/Harpoon_Launcher.png')
    models.Weapon.new(name='Lance', stack_size=1, class_name='PrimalItem_WeaponLance_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponLance.PrimalItem_WeaponLance\'"',
                      url='https://ark.fandom.com/wiki/Lance',
                      description='Knock your foes off their mounts! Can only be utilized when riding a mount.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/f/f8/Lance.png')
    models.Weapon.new(name='Lasso', stack_size=10, class_name='PrimalItem_WeaponLasso_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponLasso.PrimalItem_WeaponLasso\'"',
                      url='https://ark.fandom.com/wiki/Lasso',
                      description='An easily-crafted ranged tool that can ensnare and pull a target. Can only be wielded when riding a certain creature.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ea/Lasso.png')
    models.Weapon.new(name='Oil Jar', stack_size=10, class_name='PrimalItem_WeaponOilJar_C',
                      blueprint='"Blueprint\'/Game/ScorchedEarth/WeaponOilJar/PrimalItem_WeaponOilJar.PrimalItem_WeaponOilJar\'"',
                      url='https://ark.fandom.com/wiki/Oil_Jar_(Scorched_Earth)',
                      description='Throw it to create an oil slick which can be lit on fire! This sticky substance can also slow people down which step in it!',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c1/Oil_Jar_%28Scorched_Earth%29.png')
    models.Weapon.new(name='Plant Species Z Fruit', stack_size=100, class_name='PrimalItem_PlantSpeciesZ_Grenade_C',
                      blueprint='"Blueprint\'/Game/Aberration/WeaponPlantSpeciesZ/PrimalItem_PlantSpeciesZ_Grenade.PrimalItem_PlantSpeciesZ_Grenade\'"',
                      url='https://ark.fandom.com/wiki/Plant_Species_Z_Fruit_(Aberration)',
                      description='Bioluminescent Fruit that provides a flash of Charge lighting',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/e/ee/Plant_Species_Z_Fruit_%28Aberration%29.png')
    models.Weapon.new(name='Scout Remote', stack_size=1, class_name='PrimalItem_WeaponScoutRemote_C',
                      blueprint='"Blueprint\'/Game/Extinction/Dinos/Scout/PrimalItem_WeaponScoutRemote.PrimalItem_WeaponScoutRemote\'"',
                      url='https://ark.fandom.com/wiki/Scout_Remote_(Extinction)', description=None,
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/7e/Scout_Remote_%28Extinction%29.png')
    models.Weapon.new(name='Smoke Grenade', stack_size=10, class_name='PrimalItem_GasGrenade_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_GasGrenade.PrimalItem_GasGrenade\'"',
                      url='https://ark.fandom.com/wiki/Smoke_Grenade',
                      description='Releases a lot of smoke to obscure your plans. Pulling the pin starts a 5 second timer to an explosion.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d5/Smoke_Grenade.png')
    models.Weapon.new(name='Sword', stack_size=1, class_name='PrimalItem_WeaponSword_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponSword.PrimalItem_WeaponSword\'"',
                      url='https://ark.fandom.com/wiki/Sword',
                      description='The undisputed ruler of short-range combat. Needs a hotter flame to be forged.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/8/89/Sword.png')
    models.Weapon.new(name='Tek Claws', stack_size=1, class_name='PrimalItem_WeaponTekClaws_C',
                      blueprint='"Blueprint\'/Game/Genesis/Weapons/TekHandBlades/PrimalItem_WeaponTekClaws.PrimalItem_WeaponTekClaws\'"',
                      url='https://ark.fandom.com/wiki/Tek_Claws_(Genesis:_Part_1)',
                      description='Rips through metal and armor when infused with Element and can chain hits to temporarily increase their speed and damage. Equipping this requires learning its Tekgram.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/c/c8/Tek_Claws_%28Genesis_Part_1%29.png')
    models.Weapon.new(name='Tek Gravity Grenade', stack_size=10, class_name='PrimalItem_WeaponTekGravityGrenade_C',
                      blueprint='"Blueprint\'/Game/Extinction/CoreBlueprints/Weapons/PrimalItem_WeaponTekGravityGrenade.PrimalItem_WeaponTekGravityGrenade\'"',
                      url='https://ark.fandom.com/wiki/Tek_Gravity_Grenade_(Extinction)',
                      description="Pulling the pin starts a 5 second timer to an explosion. Make sure you've thrown it by then.",
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/5/51/Tek_Gravity_Grenade_%28Extinction%29.png')
    models.Weapon.new(name='Tek Grenade', stack_size=10, class_name='PrimalItem_TekGrenade_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_TekGrenade.PrimalItem_TekGrenade\'"',
                      url='https://ark.fandom.com/wiki/Tek_Grenade',
                      description='Sticks to targets with a powerful Tek Explosion after 5 seconds. Equipping requires learning this Tekgram.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/7/75/Tek_Grenade.png')
    models.Weapon.new(name='Tek Grenade Launcher', stack_size=1, class_name='PrimalItem_WeaponTekGrenadeLauncher_C',
                      blueprint='"Blueprint\'/Game/Genesis/Weapons/TekGrenadeLauncher/PrimalItem_WeaponTekGrenadeLauncher.PrimalItem_WeaponTekGrenadeLauncher\'"',
                      url='https://ark.fandom.com/wiki/Tek_Grenade_Launcher_(Genesis:_Part_1)',
                      description='An advanced launcher that can shoot various grenade types and can enable on-impact explosions. Equipping this requires learning its Tekgram.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a9/Tek_Grenade_Launcher_%28Genesis_Part_1%29.png')
    models.Weapon.new(name='Tek Railgun', stack_size=1, class_name='PrimalItem_TekSniper_C',
                      blueprint='"Blueprint\'/Game/Aberration/WeaponTekSniper/PrimalItem_TekSniper.PrimalItem_TekSniper\'"',
                      url='https://ark.fandom.com/wiki/Tek_Railgun_(Aberration)',
                      description='Shoots explosive plasma bolts, with an infrared zoomable scope. Equipping requires learning this Tekgram.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/2/2b/Tek_Railgun_%28Aberration%29.png')
    models.Weapon.new(name='Tek Rifle', stack_size=1, class_name='PrimalItem_TekRifle_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_TekRifle.PrimalItem_TekRifle\'"',
                      url='https://ark.fandom.com/wiki/Tek_Rifle',
                      description='Shoots explosive plasma bolts, with an infrared zoomable scope. Equipping requires learning this Tekgram.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/d/d4/Tek_Rifle.png')
    models.Weapon.new(name='Tek Sword', stack_size=1, class_name='PrimalItem_WeaponTekSword_C',
                      blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponTekSword.PrimalItem_WeaponTekSword\'"',
                      url='https://ark.fandom.com/wiki/Tek_Sword',
                      description='Cuts through metal and armor when infused with Element, and supports a Charge Attack. Equipping requires learning this Tekgram.',
                      image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/9/9b/Tek_Sword_%28Ragnarok%29.png')
    items = [item.to_json() for item in models.Weapon.all()]
    print(items)
