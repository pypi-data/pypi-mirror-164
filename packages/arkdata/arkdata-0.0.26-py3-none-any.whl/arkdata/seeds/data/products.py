from arkdata import models


def print_product_seed():
    classtypes = [models.Ammunition, models.Armour, models.Artifact, models.Attachment,
                  models.Saddle, models.Consumable, models.Creature, models.Dye, models.Egg, models.Farm, models.Recipe,
                  models.Resource, models.Seed, models.Skin, models.Structure, models.Tool, models.Trophy,
                  models.Weapon]
    for classtype in classtypes:
        print(f"# Create {classtype.__name__}")
        for item in classtype.all():
            print(f"models.Product.new(price=0, name={repr(item.name)}, type={repr(classtype.__type_name__)})")
        print("\n\n\n")


def backup_seed():
    # Create Ammunition
    models.Product.new(price=0, name='Simple Bullet', type='AMMUNITION')
    models.Product.new(price=0, name='Stone Arrow', type='AMMUNITION')
    models.Product.new(price=0, name='C4 Charge', type='AMMUNITION')
    models.Product.new(price=0, name='Tranq Arrow', type='AMMUNITION')
    models.Product.new(price=0, name='Simple Rifle Ammo', type='AMMUNITION')
    models.Product.new(price=0, name='Advanced Bullet', type='AMMUNITION')
    models.Product.new(price=0, name='Advanced Rifle Bullet', type='AMMUNITION')
    models.Product.new(price=0, name='Rocket Propelled Grenade', type='AMMUNITION')
    models.Product.new(price=0, name='Simple Shotgun Ammo', type='AMMUNITION')
    models.Product.new(price=0, name='Transponder Node', type='AMMUNITION')
    models.Product.new(price=0, name='Metal Arrow', type='AMMUNITION')
    models.Product.new(price=0, name='Advanced Sniper Bullet', type='AMMUNITION')
    models.Product.new(price=0, name='Boulder', type='AMMUNITION')
    models.Product.new(price=0, name='Cannon Ball', type='AMMUNITION')
    models.Product.new(price=0, name='Cannon Shell', type='AMMUNITION')
    models.Product.new(price=0, name='Explosive Arrow', type='AMMUNITION')
    models.Product.new(price=0, name='Flame Arrow', type='AMMUNITION')
    models.Product.new(price=0, name='Flamethrower Ammo', type='AMMUNITION')
    models.Product.new(price=0, name='Grappling Hook', type='AMMUNITION')
    models.Product.new(price=0, name='Jar of Pitch', type='AMMUNITION')
    models.Product.new(price=0, name='Net Projectile', type='AMMUNITION')
    models.Product.new(price=0, name='Pheromone Dart', type='AMMUNITION')
    models.Product.new(price=0, name='Rocket Homing Missile', type='AMMUNITION')
    models.Product.new(price=0, name='Rocket Pod', type='AMMUNITION')
    models.Product.new(price=0, name='Shocking Tranquilizer Dart', type='AMMUNITION')
    models.Product.new(price=0, name='Spear Bolt', type='AMMUNITION')
    models.Product.new(price=0, name='Tranquilizer Dart', type='AMMUNITION')
    models.Product.new(price=0, name='Tranq Spear Bolt', type='AMMUNITION')
    models.Product.new(price=0, name='Zip-Line Anchor', type='AMMUNITION')

    # Create Armour
    models.Product.new(price=0, name='Cloth Pants', type='ARMOUR')
    models.Product.new(price=0, name='Cloth Shirt', type='ARMOUR')
    models.Product.new(price=0, name='Cloth Hat', type='ARMOUR')
    models.Product.new(price=0, name='Cloth Boots', type='ARMOUR')
    models.Product.new(price=0, name='Cloth Gloves', type='ARMOUR')
    models.Product.new(price=0, name='Hide Pants', type='ARMOUR')
    models.Product.new(price=0, name='Hide Shirt', type='ARMOUR')
    models.Product.new(price=0, name='Hide Hat', type='ARMOUR')
    models.Product.new(price=0, name='Hide Boots', type='ARMOUR')
    models.Product.new(price=0, name='Hide Gloves', type='ARMOUR')
    models.Product.new(price=0, name='Chitin Leggings', type='ARMOUR')
    models.Product.new(price=0, name='Chitin Chestpiece', type='ARMOUR')
    models.Product.new(price=0, name='Chitin Helmet', type='ARMOUR')
    models.Product.new(price=0, name='Chitin Boots', type='ARMOUR')
    models.Product.new(price=0, name='Chitin Gauntlets', type='ARMOUR')
    models.Product.new(price=0, name='Parachute', type='ARMOUR')
    models.Product.new(price=0, name='Flak Leggings', type='ARMOUR')
    models.Product.new(price=0, name='Flak Chestpiece', type='ARMOUR')
    models.Product.new(price=0, name='Flak Helmet', type='ARMOUR')
    models.Product.new(price=0, name='Flak Boots', type='ARMOUR')
    models.Product.new(price=0, name='Flak Gauntlets', type='ARMOUR')
    models.Product.new(price=0, name="Heavy Miner's Helmet", type='ARMOUR')
    models.Product.new(price=0, name='SCUBA Tank', type='ARMOUR')
    models.Product.new(price=0, name='SCUBA Mask', type='ARMOUR')
    models.Product.new(price=0, name='SCUBA Flippers', type='ARMOUR')
    models.Product.new(price=0, name='Fur Leggings', type='ARMOUR')
    models.Product.new(price=0, name='Fur Chestpiece', type='ARMOUR')
    models.Product.new(price=0, name='Fur Cap', type='ARMOUR')
    models.Product.new(price=0, name='Fur Boots', type='ARMOUR')
    models.Product.new(price=0, name='Fur Gauntlets', type='ARMOUR')
    models.Product.new(price=0, name='Riot Leggings', type='ARMOUR')
    models.Product.new(price=0, name='Riot Chestpiece', type='ARMOUR')
    models.Product.new(price=0, name='Riot Gauntlets', type='ARMOUR')
    models.Product.new(price=0, name='Riot Boots', type='ARMOUR')
    models.Product.new(price=0, name='Riot Helmet', type='ARMOUR')
    models.Product.new(price=0, name='Tek Shoulder Cannon', type='ARMOUR')
    models.Product.new(price=0, name='Tek Boots', type='ARMOUR')
    models.Product.new(price=0, name='Tek Chestpiece', type='ARMOUR')
    models.Product.new(price=0, name='Tek Gauntlets', type='ARMOUR')
    models.Product.new(price=0, name='Tek Helmet', type='ARMOUR')
    models.Product.new(price=0, name='Tek Leggings', type='ARMOUR')
    models.Product.new(price=0, name='SCUBA Leggings', type='ARMOUR')
    models.Product.new(price=0, name='Wooden Shield', type='ARMOUR')
    models.Product.new(price=0, name='Metal Shield', type='ARMOUR')
    models.Product.new(price=0, name='Riot Shield', type='ARMOUR')
    models.Product.new(price=0, name='Tek Shield', type='ARMOUR')
    models.Product.new(price=0, name='Ghillie Boots', type='ARMOUR')
    models.Product.new(price=0, name='Ghillie Chestpiece', type='ARMOUR')
    models.Product.new(price=0, name='Ghillie Gauntlets', type='ARMOUR')
    models.Product.new(price=0, name='Ghillie Leggings', type='ARMOUR')
    models.Product.new(price=0, name='Ghillie Mask', type='ARMOUR')
    models.Product.new(price=0, name='Gas Mask', type='ARMOUR')
    models.Product.new(price=0, name='Desert Cloth Boots', type='ARMOUR')
    models.Product.new(price=0, name='Desert Cloth Gloves', type='ARMOUR')
    models.Product.new(price=0, name='Desert Goggles and Hat', type='ARMOUR')
    models.Product.new(price=0, name='Desert Cloth Pants', type='ARMOUR')
    models.Product.new(price=0, name='Desert Cloth Shirt', type='ARMOUR')
    models.Product.new(price=0, name='Night Vision Goggles', type='ARMOUR')
    models.Product.new(price=0, name='Hazard Suit Boots', type='ARMOUR')
    models.Product.new(price=0, name='Hazard Suit Gloves', type='ARMOUR')
    models.Product.new(price=0, name='Hazard Suit Hat', type='ARMOUR')
    models.Product.new(price=0, name='Hazard Suit Pants', type='ARMOUR')
    models.Product.new(price=0, name='Hazard Suit Shirt', type='ARMOUR')
    models.Product.new(price=0, name='M.D.S.M.', type='ARMOUR')
    models.Product.new(price=0, name='M.O.M.I.', type='ARMOUR')
    models.Product.new(price=0, name='M.R.L.M.', type='ARMOUR')
    models.Product.new(price=0, name='M.S.C.M.', type='ARMOUR')

    # Create Artifact
    models.Product.new(price=0, name='Specimen Implant', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Hunter', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Pack', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Massive', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Devious', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Clever', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Skylord', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Devourer', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Immune', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Strong', type='ARTIFACT')
    models.Product.new(price=0, name='Argentavis Talon', type='ARTIFACT')
    models.Product.new(price=0, name='Megalodon Tooth', type='ARTIFACT')
    models.Product.new(price=0, name='Tyrannosaurus Arm', type='ARTIFACT')
    models.Product.new(price=0, name='Sauropod Vertebra', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Brute', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Cunning', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Lost', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Gatekeeper ', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Crag ', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Destroyer ', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Depths ', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Shadows ', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Stalker ', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Chaos', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Growth', type='ARTIFACT')
    models.Product.new(price=0, name='Artifact of the Void', type='ARTIFACT')
    models.Product.new(price=0, name='Allosaurus Brain', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Basilisk Fang', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Carnotaurus Arm', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Crystal Talon', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Karkinos Claw', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Leedsichthys Blubber', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Megalodon Fin', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Mosasaur Tooth', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Raptor Claw', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Reaper King Barb', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Tusoteuthis Eye', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha Tyrannosaur Tooth', type='ARTIFACT')
    models.Product.new(price=0, name='Alpha X-Triceratops Skull', type='ARTIFACT')
    models.Product.new(price=0, name='Basilisk Scale', type='ARTIFACT')
    models.Product.new(price=0, name='Basilosaurus Blubber', type='ARTIFACT')
    models.Product.new(price=0, name='Corrupt Heart', type='ARTIFACT')
    models.Product.new(price=0, name='Crystal Talon', type='ARTIFACT')
    models.Product.new(price=0, name='Fire Talon', type='ARTIFACT')
    models.Product.new(price=0, name='Gasbags bladder', type='ARTIFACT')
    models.Product.new(price=0, name='Giganotosaurus Heart', type='ARTIFACT')
    models.Product.new(price=0, name='Golden Striped Megalodon Tooth', type='ARTIFACT')
    models.Product.new(price=0, name='Lightning Talon', type='ARTIFACT')
    models.Product.new(price=0, name='Megalania Toxin', type='ARTIFACT')
    models.Product.new(price=0, name='Poison Talon', type='ARTIFACT')
    models.Product.new(price=0, name='Reaper King Pheromone Gland', type='ARTIFACT')
    models.Product.new(price=0, name='Reaper Pheromone Gland', type='ARTIFACT')
    models.Product.new(price=0, name='Rock Drake Feather', type='ARTIFACT')
    models.Product.new(price=0, name='Sarcosuchus Skin', type='ARTIFACT')
    models.Product.new(price=0, name='Spinosaurus Sail', type='ARTIFACT')
    models.Product.new(price=0, name='Therizino Claws', type='ARTIFACT')
    models.Product.new(price=0, name='Thylacoleo Hook-Claw', type='ARTIFACT')
    models.Product.new(price=0, name='Titanoboa Venom', type='ARTIFACT')
    models.Product.new(price=0, name='Tusoteuthis Tentacle', type='ARTIFACT')
    models.Product.new(price=0, name='Yutyrannus Lungs', type='ARTIFACT')
    models.Product.new(price=0, name='Mysterious Snow Globe', type='ARTIFACT')
    models.Product.new(price=0, name='Revealed Snow Globe', type='ARTIFACT')

    # Create Attachment
    models.Product.new(price=0, name='Scope Attachment', type='ATTACHMENT')
    models.Product.new(price=0, name='Flashlight Attachment', type='ATTACHMENT')
    models.Product.new(price=0, name='Silencer Attachment', type='ATTACHMENT')
    models.Product.new(price=0, name='Holo-Scope Attachment', type='ATTACHMENT')
    models.Product.new(price=0, name='Laser Attachment', type='ATTACHMENT')

    # Create Saddle
    models.Product.new(price=0, name='Rex Saddle', type='SADDLE')
    models.Product.new(price=0, name='Parasaur Saddle', type='SADDLE')
    models.Product.new(price=0, name='Raptor Saddle', type='SADDLE')
    models.Product.new(price=0, name='Stego Saddle', type='SADDLE')
    models.Product.new(price=0, name='Trike Saddle', type='SADDLE')
    models.Product.new(price=0, name='Pulmonoscorpius Saddle', type='SADDLE')
    models.Product.new(price=0, name='Pteranodon Saddle', type='SADDLE')
    models.Product.new(price=0, name='Bronto Saddle', type='SADDLE')
    models.Product.new(price=0, name='Carbonemys Saddle', type='SADDLE')
    models.Product.new(price=0, name='Sarco Saddle', type='SADDLE')
    models.Product.new(price=0, name='Ankylo Saddle', type='SADDLE')
    models.Product.new(price=0, name='Mammoth Saddle', type='SADDLE')
    models.Product.new(price=0, name='Megalodon Saddle', type='SADDLE')
    models.Product.new(price=0, name='Sabertooth Saddle', type='SADDLE')
    models.Product.new(price=0, name='Carno Saddle', type='SADDLE')
    models.Product.new(price=0, name='Argentavis Saddle', type='SADDLE')
    models.Product.new(price=0, name='Phiomia Saddle', type='SADDLE')
    models.Product.new(price=0, name='Spino Saddle', type='SADDLE')
    models.Product.new(price=0, name='Plesiosaur Saddle', type='SADDLE')
    models.Product.new(price=0, name='Ichthyosaurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Doedicurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Bronto Platform Saddle', type='SADDLE')
    models.Product.new(price=0, name='Pachy Saddle', type='SADDLE')
    models.Product.new(price=0, name='Paracer Saddle', type='SADDLE')
    models.Product.new(price=0, name='Paracer Platform Saddle', type='SADDLE')
    models.Product.new(price=0, name='Beelzebufo Saddle', type='SADDLE')
    models.Product.new(price=0, name='Megaloceros Saddle', type='SADDLE')
    models.Product.new(price=0, name='Allosaurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Araneo Saddle', type='SADDLE')
    models.Product.new(price=0, name='Arthropluera Saddle', type='SADDLE')
    models.Product.new(price=0, name='Baryonyx Saddle', type='SADDLE')
    models.Product.new(price=0, name='Basilisk Saddle', type='SADDLE')
    models.Product.new(price=0, name='Basilosaurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Castoroides Saddle', type='SADDLE')
    models.Product.new(price=0, name='Chalicotherium Saddle', type='SADDLE')
    models.Product.new(price=0, name='Daeodon Saddle', type='SADDLE')
    models.Product.new(price=0, name='Deinonychus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Diplodocus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Direbear Saddle', type='SADDLE')
    models.Product.new(price=0, name='Dunkleosteus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Equus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Gacha Saddle', type='SADDLE')
    models.Product.new(price=0, name='Gallimimus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Gasbags Saddle', type='SADDLE')
    models.Product.new(price=0, name='Giganotosaurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Hyaenodon Meatpack', type='SADDLE')
    models.Product.new(price=0, name='Iguanodon Saddle', type='SADDLE')
    models.Product.new(price=0, name='Kaprosuchus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Karkinos Saddle', type='SADDLE')
    models.Product.new(price=0, name='Lymantria Saddle', type='SADDLE')
    models.Product.new(price=0, name='Magmasaur Saddle', type='SADDLE')
    models.Product.new(price=0, name='Managarmr Saddle', type='SADDLE')
    models.Product.new(price=0, name='Manta Saddle', type='SADDLE')
    models.Product.new(price=0, name='Mantis Saddle', type='SADDLE')
    models.Product.new(price=0, name='Megalosaurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Megalania Saddle', type='SADDLE')
    models.Product.new(price=0, name='Megatherium Saddle', type='SADDLE')
    models.Product.new(price=0, name='Morellatops Saddle', type='SADDLE')
    models.Product.new(price=0, name='Mosasaur Saddle', type='SADDLE')
    models.Product.new(price=0, name='Pachyrhinosaurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Pelagornis Saddle', type='SADDLE')
    models.Product.new(price=0, name='Procoptodon Saddle', type='SADDLE')
    models.Product.new(price=0, name='Quetz Saddle', type='SADDLE')
    models.Product.new(price=0, name='Ravager Saddle', type='SADDLE')
    models.Product.new(price=0, name='Rock Drake Saddle', type='SADDLE')
    models.Product.new(price=0, name='Rock Golem Saddle', type='SADDLE')
    models.Product.new(price=0, name='Roll Rat Saddle', type='SADDLE')
    models.Product.new(price=0, name='Snow Owl Saddle', type='SADDLE')
    models.Product.new(price=0, name='Tapejara Saddle', type='SADDLE')
    models.Product.new(price=0, name='Terror Bird Saddle', type='SADDLE')
    models.Product.new(price=0, name='Therizinosaurus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Thorny Dragon Saddle', type='SADDLE')
    models.Product.new(price=0, name='Thylacoleo Saddle', type='SADDLE')
    models.Product.new(price=0, name='Tropeognathus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Tusoteuthis Saddle', type='SADDLE')
    models.Product.new(price=0, name='Velonasaur Saddle', type='SADDLE')
    models.Product.new(price=0, name='Woolly Rhino Saddle', type='SADDLE')
    models.Product.new(price=0, name='Yutyrannus Saddle', type='SADDLE')
    models.Product.new(price=0, name='Desert Titan Saddle', type='SADDLE')
    models.Product.new(price=0, name='Forest Titan Saddle', type='SADDLE')
    models.Product.new(price=0, name='Ice Titan Saddle', type='SADDLE')
    models.Product.new(price=0, name='Titanosaur Platform Saddle', type='SADDLE')
    models.Product.new(price=0, name='Mosasaur Platform Saddle', type='SADDLE')
    models.Product.new(price=0, name='Megachelon Platform Saddle', type='SADDLE')
    models.Product.new(price=0, name='Quetz Platform Saddle', type='SADDLE')
    models.Product.new(price=0, name='Plesiosaur Platform Saddle', type='SADDLE')
    models.Product.new(price=0, name='Rex Tek Saddle', type='SADDLE')
    models.Product.new(price=0, name='Astrocetus Tek Saddle', type='SADDLE')
    models.Product.new(price=0, name='Rock Drake Tek Saddle', type='SADDLE')
    models.Product.new(price=0, name='Megalodon Tek Saddle', type='SADDLE')
    models.Product.new(price=0, name='Mosasaur Tek Saddle', type='SADDLE')
    models.Product.new(price=0, name='Tapejara Tek Saddle', type='SADDLE')

    # Create Consumable
    models.Product.new(price=0, name='Medical Brew', type='CONSUMABLE')
    models.Product.new(price=0, name='Mindwipe Tonic', type='CONSUMABLE')
    models.Product.new(price=0, name='Raw Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Spoiled Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Cooked Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Water Jar (Empty)', type='CONSUMABLE')
    models.Product.new(price=0, name='Water Jar (Full)', type='CONSUMABLE')
    models.Product.new(price=0, name='Waterskin (Empty)', type='CONSUMABLE')
    models.Product.new(price=0, name='Waterskin (Filled)', type='CONSUMABLE')
    models.Product.new(price=0, name='Bingleberry Soup', type='CONSUMABLE')
    models.Product.new(price=0, name='Energy Brew', type='CONSUMABLE')
    models.Product.new(price=0, name='Citronal', type='CONSUMABLE')
    models.Product.new(price=0, name='Amarberry', type='CONSUMABLE')
    models.Product.new(price=0, name='Azulberry', type='CONSUMABLE')
    models.Product.new(price=0, name='Tintoberry', type='CONSUMABLE')
    models.Product.new(price=0, name='Mejoberry', type='CONSUMABLE')
    models.Product.new(price=0, name='Narcoberry', type='CONSUMABLE')
    models.Product.new(price=0, name='Stimberry', type='CONSUMABLE')
    models.Product.new(price=0, name='Super Test Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Enduro Stew', type='CONSUMABLE')
    models.Product.new(price=0, name='Lazarus Chowder', type='CONSUMABLE')
    models.Product.new(price=0, name='Calien Soup', type='CONSUMABLE')
    models.Product.new(price=0, name='Fria Curry', type='CONSUMABLE')
    models.Product.new(price=0, name='Focal Chili', type='CONSUMABLE')
    models.Product.new(price=0, name='Savoroot', type='CONSUMABLE')
    models.Product.new(price=0, name='Longrass', type='CONSUMABLE')
    models.Product.new(price=0, name='Rockarrot', type='CONSUMABLE')
    models.Product.new(price=0, name='Raw Prime Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Cooked Prime Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Battle Tartare', type='CONSUMABLE')
    models.Product.new(price=0, name='Shadow Steak Saute', type='CONSUMABLE')
    models.Product.new(price=0, name='Cooked Meat Jerky', type='CONSUMABLE')
    models.Product.new(price=0, name='Prime Meat Jerky', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Ankylo Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Argentavis Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Titanboa Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Carno Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Dilo Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Dodo Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Parasaur Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Pteranodon Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Raptor Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Rex Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Sarco Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Bronto Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Pulmonoscorpius Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Araneo Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Spino Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Stego Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Trike Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Carbonemys Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Canteen (Empty)', type='CONSUMABLE')
    models.Product.new(price=0, name='Canteen (Full)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Pachy Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Dimorph Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Broth of Enlightenment', type='CONSUMABLE')
    models.Product.new(price=0, name='Raw Fish Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Cooked Fish Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Raw Prime Fish Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Cooked Prime Fish Meat', type='CONSUMABLE')
    models.Product.new(price=0, name='Raw Mutton', type='CONSUMABLE')
    models.Product.new(price=0, name='Cooked Lamb Chop', type='CONSUMABLE')
    models.Product.new(price=0, name='Filled Fish Basket', type='CONSUMABLE')
    models.Product.new(price=0, name='Wyvern Milk', type='CONSUMABLE')
    models.Product.new(price=0, name='Cactus Sap', type='CONSUMABLE')
    models.Product.new(price=0, name='Aggeravic Mushroom', type='CONSUMABLE')
    models.Product.new(price=0, name='Aquatic Mushroom', type='CONSUMABLE')
    models.Product.new(price=0, name='Ascerbic Mushroom', type='CONSUMABLE')
    models.Product.new(price=0, name='Auric Mushroom', type='CONSUMABLE')
    models.Product.new(price=0, name='Mushroom Brew', type='CONSUMABLE')
    models.Product.new(price=0, name='Iced Water Jar (Empty)', type='CONSUMABLE')
    models.Product.new(price=0, name='Iced Water Jar (Full)', type='CONSUMABLE')
    models.Product.new(price=0, name='Iced Canteen (Empty)', type='CONSUMABLE')
    models.Product.new(price=0, name='Iced Canteen (Full)', type='CONSUMABLE')
    models.Product.new(price=0, name='Beer Liquid', type='CONSUMABLE')
    models.Product.new(price=0, name='Beer Jar', type='CONSUMABLE')
    models.Product.new(price=0, name='Beer Jar (alt)', type='CONSUMABLE')
    models.Product.new(price=0, name='Bio Toxin', type='CONSUMABLE')
    models.Product.new(price=0, name='Bug Repellant', type='CONSUMABLE')
    models.Product.new(price=0, name='Cactus Broth', type='CONSUMABLE')
    models.Product.new(price=0, name='Lesser Antidote', type='CONSUMABLE')
    models.Product.new(price=0, name='Soap', type='CONSUMABLE')
    models.Product.new(price=0, name='Sweet Vegetable Cake', type='CONSUMABLE')
    models.Product.new(price=0, name='Giant Bee Honey', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Allosaurus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Archaeopteryx Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Baryonyx Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Camelsaurus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Compy Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Dimetrodon Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Diplo Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Featherlight Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Gallimimus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Glowtail Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Ichthyornis Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Iguanodon Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Kairuku Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Kaprosuchus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Kentrosaurus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Lystrosaurus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Mantis Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Megalania Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Megalosaurus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Microraptor Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Moschops Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Moth Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Oviraptor Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Pachyrhino Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Pegomastax Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Pelagornis Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Quetzal Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Rock Drake Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Tapejara Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Terror Bird Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Therizinosaurus Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Thorny Dragon Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Troodon Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Kibble (Vulture Egg)', type='CONSUMABLE')
    models.Product.new(price=0, name='Basic Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Simple Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Regular Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Superior Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Exceptional Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Extraordinary Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Basic Augmented Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Simple Augmented Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Regular Augmented Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Superior Augmented Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Exceptional Augmented Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='Extraordinary Augmented Kibble', type='CONSUMABLE')
    models.Product.new(price=0, name='"Evil" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Gacha Crystal', type='CONSUMABLE')
    models.Product.new(price=0, name='Unassembled Enforcer', type='CONSUMABLE')
    models.Product.new(price=0, name='Unassembled Mek', type='CONSUMABLE')
    models.Product.new(price=0, name='Nameless Venom', type='CONSUMABLE')
    models.Product.new(price=0, name='Reaper Pheromone Gland', type='CONSUMABLE')
    models.Product.new(price=0, name='"Turkey" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Summon DodoRex', type='CONSUMABLE')
    models.Product.new(price=0, name='"Snowball" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Festive Dino Candy', type='CONSUMABLE')
    models.Product.new(price=0, name="Box o' Chocolates", type='CONSUMABLE')
    models.Product.new(price=0, name='Valentines Dino Candy', type='CONSUMABLE')
    models.Product.new(price=0, name='"Heart" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Romantic Head Hair Style', type='CONSUMABLE')
    models.Product.new(price=0, name='Romantic Facial Hair Style', type='CONSUMABLE')
    models.Product.new(price=0, name='Festive Dino Candy (Easter)', type='CONSUMABLE')
    models.Product.new(price=0, name='"Archer Flex" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='"Bicep Smooch" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Summer Swirl Taffy', type='CONSUMABLE')
    models.Product.new(price=0, name='"Dance" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Panic Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='"Zombie" Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Dino Candy Corn', type='CONSUMABLE')
    models.Product.new(price=0, name='Belly Rub Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Food Coma Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Hungry Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Thanksgiving Candy', type='CONSUMABLE')
    models.Product.new(price=0, name='Caroling Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Happy Clap Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Nutcracker Dance Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Flirty Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Bunny Hop Dance Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Air Drums Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Air Guitar Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Mosh Pit Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Knock Emote', type='CONSUMABLE')
    models.Product.new(price=0, name='Scare Emote', type='CONSUMABLE')

    # Create Creature
    models.Product.new(price=0, name='Aberrant Achatina', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Anglerfish', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Ankylosaurus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Araneo', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Arthropluera', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Baryonyx', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Beelzebufo', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Carbonemys', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Carnotaurus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Cnidaria', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Coelacanth', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Dimetrodon', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Dimorphodon', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Diplocaulus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Diplodocus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Dire Bear', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Dodo', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Doedicurus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Dung Beetle', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Electrophorus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Equus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Gigantopithecus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Iguanodon', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Lystrosaurus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Manta', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Megalania', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Megalosaurus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Meganeura', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Moschops', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Otter', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Ovis', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Paraceratherium', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Parasaur', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Piranha', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Pulmonoscorpius', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Purlovia', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Raptor', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Sabertooth Salmon', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Sarco', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Spino', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Stegosaurus', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Titanoboa', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Triceratops', type='CREATURE')
    models.Product.new(price=0, name='Aberrant Trilobite', type='CREATURE')
    models.Product.new(price=0, name='Alpha Basilisk', type='CREATURE')
    models.Product.new(price=0, name='Alpha Karkinos', type='CREATURE')
    models.Product.new(price=0, name='Alpha Surface Reaper King', type='CREATURE')
    models.Product.new(price=0, name='Basilisk', type='CREATURE')
    models.Product.new(price=0, name='Basilisk Ghost', type='CREATURE')
    models.Product.new(price=0, name='Bulbdog', type='CREATURE')
    models.Product.new(price=0, name='Bulbdog Ghost', type='CREATURE')
    models.Product.new(price=0, name='Featherlight', type='CREATURE')
    models.Product.new(price=0, name='Glowbug', type='CREATURE')
    models.Product.new(price=0, name='Glowtail', type='CREATURE')
    models.Product.new(price=0, name='Karkinos', type='CREATURE')
    models.Product.new(price=0, name='Lamprey', type='CREATURE')
    models.Product.new(price=0, name='Nameless', type='CREATURE')
    models.Product.new(price=0, name='Ravager', type='CREATURE')
    models.Product.new(price=0, name='Reaper King', type='CREATURE')
    models.Product.new(price=0, name='Reaper King (Tamed)', type='CREATURE')
    models.Product.new(price=0, name='Reaper Queen', type='CREATURE')
    models.Product.new(price=0, name='Rock Drake', type='CREATURE')
    models.Product.new(price=0, name='Rockwell', type='CREATURE')
    models.Product.new(price=0, name='Rockwell (Alpha)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell (Beta)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell (Gamma)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Tentacle', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Tentacle (Alpha)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Tentacle (Beta)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Tentacle (Gamma)', type='CREATURE')
    models.Product.new(price=0, name='Roll Rat', type='CREATURE')
    models.Product.new(price=0, name='Seeker', type='CREATURE')
    models.Product.new(price=0, name='Shinehorn', type='CREATURE')
    models.Product.new(price=0, name='Surface Reaper King Ghost', type='CREATURE')
    models.Product.new(price=0, name='Alpha Blood Crystal Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Blood Crystal Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Crystal Wyvern Queen (Gamma)', type='CREATURE')
    models.Product.new(price=0, name='Crystal Wyvern Queen (Beta)', type='CREATURE')
    models.Product.new(price=0, name='Crystal Wyvern Queen (Alpha)', type='CREATURE')
    models.Product.new(price=0, name='Ember Crystal Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Giant Worker Bee', type='CREATURE')
    models.Product.new(price=0, name='Tropeognathus', type='CREATURE')
    models.Product.new(price=0, name='Tropical Crystal Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Alpha King Titan', type='CREATURE')
    models.Product.new(price=0, name='Beta King Titan', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Arthropluera', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Carnotaurus', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Chalicotherium', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Dilophosaur', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Dimorphodon', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Giganotosaurus', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Paraceratherium', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Pteranodon', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Raptor', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Reaper King', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Rex', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Rock Drake', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Spino', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Stegosaurus', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Triceratops', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Defense Unit', type='CREATURE')
    models.Product.new(price=0, name='Desert Titan', type='CREATURE')
    models.Product.new(price=0, name='Desert Titan Flock', type='CREATURE')
    models.Product.new(price=0, name='Enforcer', type='CREATURE')
    models.Product.new(price=0, name='Enraged Corrupted Rex', type='CREATURE')
    models.Product.new(price=0, name='Enraged Triceratops', type='CREATURE')
    models.Product.new(price=0, name='Forest Titan', type='CREATURE')
    models.Product.new(price=0, name='Forest Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Gacha', type='CREATURE')
    models.Product.new(price=0, name='GachaClaus', type='CREATURE')
    models.Product.new(price=0, name='Gamma King Titan', type='CREATURE')
    models.Product.new(price=0, name='Gasbags', type='CREATURE')
    models.Product.new(price=0, name='Ice Titan', type='CREATURE')
    models.Product.new(price=0, name='Managarmr', type='CREATURE')
    models.Product.new(price=0, name='Mega Mek', type='CREATURE')
    models.Product.new(price=0, name='Mek', type='CREATURE')
    models.Product.new(price=0, name='Scout', type='CREATURE')
    models.Product.new(price=0, name='Snow Owl', type='CREATURE')
    models.Product.new(price=0, name='Snow Owl Ghost', type='CREATURE')
    models.Product.new(price=0, name='Velonasaur', type='CREATURE')
    models.Product.new(price=0, name='Alpha Corrupted Master Controller', type='CREATURE')
    models.Product.new(price=0, name='Alpha Moeder, Master of the Ocean', type='CREATURE')
    models.Product.new(price=0, name='Alpha X-Triceratops', type='CREATURE')
    models.Product.new(price=0, name='Astrocetus', type='CREATURE')
    models.Product.new(price=0, name='Beta Corrupted Master Controller', type='CREATURE')
    models.Product.new(price=0, name='Beta Moeder, Master of the Ocean', type='CREATURE')
    models.Product.new(price=0, name='Bloodstalker', type='CREATURE')
    models.Product.new(price=0, name='Brute Araneo', type='CREATURE')
    models.Product.new(price=0, name='Brute Astrocetus', type='CREATURE')
    models.Product.new(price=0, name='Brute Basilosaurus', type='CREATURE')
    models.Product.new(price=0, name='Brute Bloodstalker', type='CREATURE')
    models.Product.new(price=0, name='Brute Ferox', type='CREATURE')
    models.Product.new(price=0, name='Brute Fire Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Brute Leedsichthys', type='CREATURE')
    models.Product.new(price=0, name='Brute Magmasaur', type='CREATURE')
    models.Product.new(price=0, name='Brute Malfunctioned Tek Giganotosaurus', type='CREATURE')
    models.Product.new(price=0, name='Brute Malfunctioned Tek Rex', type='CREATURE')
    models.Product.new(price=0, name='Brute Mammoth', type='CREATURE')
    models.Product.new(price=0, name='Brute Megaloceros', type='CREATURE')
    models.Product.new(price=0, name='Brute Plesiosaur', type='CREATURE')
    models.Product.new(price=0, name='Brute Reaper King', type='CREATURE')
    models.Product.new(price=0, name='Brute Sarco', type='CREATURE')
    models.Product.new(price=0, name='Brute Seeker', type='CREATURE')
    models.Product.new(price=0, name='Brute Tusoteuthis', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Allosaurus', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Megalodon', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Mosasaurus', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Raptor', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Rex', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Rock Elemental', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Spino', type='CREATURE')
    models.Product.new(price=0, name='Brute X-Yutyrannus', type='CREATURE')
    models.Product.new(price=0, name='Corrupted Avatar', type='CREATURE')
    models.Product.new(price=0, name='Eel Minion', type='CREATURE')
    models.Product.new(price=0, name='Gamma Corrupted Master Controller', type='CREATURE')
    models.Product.new(price=0, name='Gamma Moeder, Master of the Ocean', type='CREATURE')
    models.Product.new(price=0, name='Golden Striped Brute Megalodon', type='CREATURE')
    models.Product.new(price=0, name='Golden Striped Megalodon', type='CREATURE')
    models.Product.new(price=0, name='Ferox (Large)', type='CREATURE')
    models.Product.new(price=0, name='Ferox', type='CREATURE')
    models.Product.new(price=0, name='Injured Brute Reaper King', type='CREATURE')
    models.Product.new(price=0, name='Insect Swarm', type='CREATURE')
    models.Product.new(price=0, name='Magmasaur', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Giganotosaurus Gauntlet', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Giganotosaurus', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Parasaur', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Quetzal', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Raptor', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Rex', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Stegosaurus', type='CREATURE')
    models.Product.new(price=0, name='Malfunctioned Tek Triceratops', type='CREATURE')
    models.Product.new(price=0, name='Megachelon', type='CREATURE')
    models.Product.new(price=0, name='Parakeet Fish School', type='CREATURE')
    models.Product.new(price=0, name='Reaper Prince', type='CREATURE')
    models.Product.new(price=0, name='Tek Triceratops', type='CREATURE')
    models.Product.new(price=0, name='X-Allosaurus', type='CREATURE')
    models.Product.new(price=0, name='X-Ankylosaurus', type='CREATURE')
    models.Product.new(price=0, name='X-Argentavis', type='CREATURE')
    models.Product.new(price=0, name='X-Basilosaurus', type='CREATURE')
    models.Product.new(price=0, name='X-Dunkleosteus', type='CREATURE')
    models.Product.new(price=0, name='X-Ichthyosaurus', type='CREATURE')
    models.Product.new(price=0, name='X-Megalodon', type='CREATURE')
    models.Product.new(price=0, name='X-Mosasaurus', type='CREATURE')
    models.Product.new(price=0, name='X-Otter', type='CREATURE')
    models.Product.new(price=0, name='X-Paraceratherium', type='CREATURE')
    models.Product.new(price=0, name='X-Parasaur', type='CREATURE')
    models.Product.new(price=0, name='X-Raptor', type='CREATURE')
    models.Product.new(price=0, name='X-Rex', type='CREATURE')
    models.Product.new(price=0, name='X-Rock Elemental', type='CREATURE')
    models.Product.new(price=0, name='X-Sabertooth', type='CREATURE')
    models.Product.new(price=0, name='X-Sabertooth Salmon', type='CREATURE')
    models.Product.new(price=0, name='X-Spino', type='CREATURE')
    models.Product.new(price=0, name='X-Tapejara', type='CREATURE')
    models.Product.new(price=0, name='X-Triceratops', type='CREATURE')
    models.Product.new(price=0, name='X-Woolly Rhino', type='CREATURE')
    models.Product.new(price=0, name='X-Yutyrannus', type='CREATURE')
    models.Product.new(price=0, name='Astrodelphis', type='CREATURE')
    models.Product.new(price=0, name='Maewing', type='CREATURE')
    models.Product.new(price=0, name='Noglin', type='CREATURE')
    models.Product.new(price=0, name='Shadowmane', type='CREATURE')
    models.Product.new(price=0, name='Tek Stryder', type='CREATURE')
    models.Product.new(price=0, name='Voidwyrm', type='CREATURE')
    models.Product.new(price=0, name='R-Allosaurus', type='CREATURE')
    models.Product.new(price=0, name='R-Carnotaurus', type='CREATURE')
    models.Product.new(price=0, name='R-Daeodon', type='CREATURE')
    models.Product.new(price=0, name='R-Dilophosaur', type='CREATURE')
    models.Product.new(price=0, name='R-Dire Bear', type='CREATURE')
    models.Product.new(price=0, name='R-Direwolf', type='CREATURE')
    models.Product.new(price=0, name='R-Equus', type='CREATURE')
    models.Product.new(price=0, name='R-Gasbags', type='CREATURE')
    models.Product.new(price=0, name='R-Giganotosaurus', type='CREATURE')
    models.Product.new(price=0, name='R-Megatherium', type='CREATURE')
    models.Product.new(price=0, name='R-Snow Owl', type='CREATURE')
    models.Product.new(price=0, name='R-Parasaur', type='CREATURE')
    models.Product.new(price=0, name='R-Procoptodon', type='CREATURE')
    models.Product.new(price=0, name='R-Quetzal', type='CREATURE')
    models.Product.new(price=0, name='R-Brontosaurus', type='CREATURE')
    models.Product.new(price=0, name='R-Velonasaur', type='CREATURE')
    models.Product.new(price=0, name='R-Thylacoleo', type='CREATURE')
    models.Product.new(price=0, name='R-Carbonemys', type='CREATURE')
    models.Product.new(price=0, name='R-Reaper Queen', type='CREATURE')
    models.Product.new(price=0, name='R-Reaper King', type='CREATURE')
    models.Product.new(price=0, name='R-Reaper King (Tamed)', type='CREATURE')
    models.Product.new(price=0, name='Summoner', type='CREATURE')
    models.Product.new(price=0, name='Macrophage', type='CREATURE')
    models.Product.new(price=0, name='Exo-Mek', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Prime', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Prime (Alpha)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Prime (Beta)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Prime (Gamma)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Node', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Node (Alpha)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Node (Beta)', type='CREATURE')
    models.Product.new(price=0, name='Rockwell Node (Gamma)', type='CREATURE')
    models.Product.new(price=0, name='Achatina', type='CREATURE')
    models.Product.new(price=0, name='Allosaurus', type='CREATURE')
    models.Product.new(price=0, name='Alpha Carno', type='CREATURE')
    models.Product.new(price=0, name='Alpha Leedsichthys', type='CREATURE')
    models.Product.new(price=0, name='Alpha Megalodon', type='CREATURE')
    models.Product.new(price=0, name='Alpha Mosasaur', type='CREATURE')
    models.Product.new(price=0, name='Alpha Raptor', type='CREATURE')
    models.Product.new(price=0, name='Alpha T-Rex', type='CREATURE')
    models.Product.new(price=0, name='Alpha Tusoteuthis', type='CREATURE')
    models.Product.new(price=0, name='Ammonite', type='CREATURE')
    models.Product.new(price=0, name='Anglerfish', type='CREATURE')
    models.Product.new(price=0, name='Ankylosaurus', type='CREATURE')
    models.Product.new(price=0, name='Araneo', type='CREATURE')
    models.Product.new(price=0, name='Archaeopteryx', type='CREATURE')
    models.Product.new(price=0, name='Argentavis', type='CREATURE')
    models.Product.new(price=0, name='Arthropluera', type='CREATURE')
    models.Product.new(price=0, name='Baryonyx', type='CREATURE')
    models.Product.new(price=0, name='Basilosaurus', type='CREATURE')
    models.Product.new(price=0, name='Beelzebufo', type='CREATURE')
    models.Product.new(price=0, name='Bunny Dodo', type='CREATURE')
    models.Product.new(price=0, name='Bunny Oviraptor', type='CREATURE')
    models.Product.new(price=0, name='Brontosaurus', type='CREATURE')
    models.Product.new(price=0, name='Broodmother Lysrix', type='CREATURE')
    models.Product.new(price=0, name='Chalicotherium', type='CREATURE')
    models.Product.new(price=0, name='Carbonemys', type='CREATURE')
    models.Product.new(price=0, name='Carnotaurus', type='CREATURE')
    models.Product.new(price=0, name='Castoroides', type='CREATURE')
    models.Product.new(price=0, name='Cnidaria', type='CREATURE')
    models.Product.new(price=0, name='Coelacanth', type='CREATURE')
    models.Product.new(price=0, name='Compy', type='CREATURE')
    models.Product.new(price=0, name='Daeodon', type='CREATURE')
    models.Product.new(price=0, name='Dilophosaur', type='CREATURE')
    models.Product.new(price=0, name='Dimetrodon', type='CREATURE')
    models.Product.new(price=0, name='Dimorphodon', type='CREATURE')
    models.Product.new(price=0, name='Diplocaulus', type='CREATURE')
    models.Product.new(price=0, name='Diplodocus', type='CREATURE')
    models.Product.new(price=0, name='Dire Bear', type='CREATURE')
    models.Product.new(price=0, name='Direwolf', type='CREATURE')
    models.Product.new(price=0, name='Direwolf Ghost', type='CREATURE')
    models.Product.new(price=0, name='Dodo', type='CREATURE')
    models.Product.new(price=0, name='DodoRex', type='CREATURE')
    models.Product.new(price=0, name='Doedicurus', type='CREATURE')
    models.Product.new(price=0, name='Dragon (Gamma)', type='CREATURE')
    models.Product.new(price=0, name='Dragon (Beta)', type='CREATURE')
    models.Product.new(price=0, name='Dragon (Alpha)', type='CREATURE')
    models.Product.new(price=0, name='Dung Beetle', type='CREATURE')
    models.Product.new(price=0, name='Dunkleosteus', type='CREATURE')
    models.Product.new(price=0, name='Electrophorus', type='CREATURE')
    models.Product.new(price=0, name='Equus', type='CREATURE')
    models.Product.new(price=0, name='Unicorn', type='CREATURE')
    models.Product.new(price=0, name='Eurypterid', type='CREATURE')
    models.Product.new(price=0, name='Gallimimus', type='CREATURE')
    models.Product.new(price=0, name='Giant Bee', type='CREATURE')
    models.Product.new(price=0, name='Giganotosaurus', type='CREATURE')
    models.Product.new(price=0, name='Gigantopithecus', type='CREATURE')
    models.Product.new(price=0, name='Hesperornis', type='CREATURE')
    models.Product.new(price=0, name='Human (Male)', type='CREATURE')
    models.Product.new(price=0, name='Human (Female)', type='CREATURE')
    models.Product.new(price=0, name='Hyaenodon', type='CREATURE')
    models.Product.new(price=0, name='Ichthyornis', type='CREATURE')
    models.Product.new(price=0, name='Ichthyosaurus', type='CREATURE')
    models.Product.new(price=0, name='Iguanodon', type='CREATURE')
    models.Product.new(price=0, name='Kairuku', type='CREATURE')
    models.Product.new(price=0, name='Kaprosuchus', type='CREATURE')
    models.Product.new(price=0, name='Kentrosaurus', type='CREATURE')
    models.Product.new(price=0, name='Leech', type='CREATURE')
    models.Product.new(price=0, name='Diseased Leech', type='CREATURE')
    models.Product.new(price=0, name='Leedsichthys', type='CREATURE')
    models.Product.new(price=0, name='Liopleurodon', type='CREATURE')
    models.Product.new(price=0, name='Lystrosaurus', type='CREATURE')
    models.Product.new(price=0, name='Mammoth', type='CREATURE')
    models.Product.new(price=0, name='Manta', type='CREATURE')
    models.Product.new(price=0, name='Megalania', type='CREATURE')
    models.Product.new(price=0, name='Megaloceros', type='CREATURE')
    models.Product.new(price=0, name='Megalodon', type='CREATURE')
    models.Product.new(price=0, name='Megalosaurus', type='CREATURE')
    models.Product.new(price=0, name='Meganeura', type='CREATURE')
    models.Product.new(price=0, name='Megapithecus', type='CREATURE')
    models.Product.new(price=0, name='Megatherium', type='CREATURE')
    models.Product.new(price=0, name='Mesopithecus', type='CREATURE')
    models.Product.new(price=0, name='Microraptor', type='CREATURE')
    models.Product.new(price=0, name='Mosasaurus', type='CREATURE')
    models.Product.new(price=0, name='Moschops', type='CREATURE')
    models.Product.new(price=0, name='Onychonycteris', type='CREATURE')
    models.Product.new(price=0, name='Otter', type='CREATURE')
    models.Product.new(price=0, name='Oviraptor', type='CREATURE')
    models.Product.new(price=0, name='Ovis', type='CREATURE')
    models.Product.new(price=0, name='Pachy', type='CREATURE')
    models.Product.new(price=0, name='Pachyrhinosaurus', type='CREATURE')
    models.Product.new(price=0, name='Paraceratherium', type='CREATURE')
    models.Product.new(price=0, name='Parasaurolophus', type='CREATURE')
    models.Product.new(price=0, name='Pegomastax', type='CREATURE')
    models.Product.new(price=0, name='Pelagornis', type='CREATURE')
    models.Product.new(price=0, name='Phiomia', type='CREATURE')
    models.Product.new(price=0, name='Piranha', type='CREATURE')
    models.Product.new(price=0, name='Plesiosaur', type='CREATURE')
    models.Product.new(price=0, name='Procoptodon', type='CREATURE')
    models.Product.new(price=0, name='Pteranodon', type='CREATURE')
    models.Product.new(price=0, name='Pulmonoscorpius', type='CREATURE')
    models.Product.new(price=0, name='Purlovia', type='CREATURE')
    models.Product.new(price=0, name='Quetzalcoatlus', type='CREATURE')
    models.Product.new(price=0, name='Raptor', type='CREATURE')
    models.Product.new(price=0, name='Rex', type='CREATURE')
    models.Product.new(price=0, name='Rex Ghost', type='CREATURE')
    models.Product.new(price=0, name='Sabertooth', type='CREATURE')
    models.Product.new(price=0, name='Sabertooth Salmon', type='CREATURE')
    models.Product.new(price=0, name='Sarco', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Bronto', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Carnotaurus', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Giganotosaurus', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Quetzal', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Raptor', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Rex', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Stego', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Trike', type='CREATURE')
    models.Product.new(price=0, name='Spino', type='CREATURE')
    models.Product.new(price=0, name='Stegosaurus', type='CREATURE')
    models.Product.new(price=0, name='Tapejara', type='CREATURE')
    models.Product.new(price=0, name='Tek Parasaur', type='CREATURE')
    models.Product.new(price=0, name='Tek Quetzal', type='CREATURE')
    models.Product.new(price=0, name='Tek Raptor', type='CREATURE')
    models.Product.new(price=0, name='Tek Rex', type='CREATURE')
    models.Product.new(price=0, name='Tek Stegosaurus', type='CREATURE')
    models.Product.new(price=0, name='Terror Bird', type='CREATURE')
    models.Product.new(price=0, name='Therizinosaur', type='CREATURE')
    models.Product.new(price=0, name='Thylacoleo', type='CREATURE')
    models.Product.new(price=0, name='Titanoboa', type='CREATURE')
    models.Product.new(price=0, name='Titanomyrma Ground', type='CREATURE')
    models.Product.new(price=0, name='Titanomyrma Air', type='CREATURE')
    models.Product.new(price=0, name='Titanosaur', type='CREATURE')
    models.Product.new(price=0, name='Triceratops', type='CREATURE')
    models.Product.new(price=0, name='Trilobite', type='CREATURE')
    models.Product.new(price=0, name='Troodon', type='CREATURE')
    models.Product.new(price=0, name='Turkey', type='CREATURE')
    models.Product.new(price=0, name='Super Turkey', type='CREATURE')
    models.Product.new(price=0, name='Tusoteuthis', type='CREATURE')
    models.Product.new(price=0, name='Woolly Rhino', type='CREATURE')
    models.Product.new(price=0, name='Yeti', type='CREATURE')
    models.Product.new(price=0, name='Yutyrannus', type='CREATURE')
    models.Product.new(price=0, name='Zomdodo', type='CREATURE')
    models.Product.new(price=0, name='Griffin', type='CREATURE')
    models.Product.new(price=0, name='Ice Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Alpha Fire Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Alpha Deathworm', type='CREATURE')
    models.Product.new(price=0, name='Deathworm', type='CREATURE')
    models.Product.new(price=0, name='Dodo Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Jerboa', type='CREATURE')
    models.Product.new(price=0, name='Skeletal Jerboa', type='CREATURE')
    models.Product.new(price=0, name='Jug Bug', type='CREATURE')
    models.Product.new(price=0, name='Oil Jug Bug', type='CREATURE')
    models.Product.new(price=0, name='Water Jug Bug', type='CREATURE')
    models.Product.new(price=0, name='Lymantria', type='CREATURE')
    models.Product.new(price=0, name='Manticore (Gamma)', type='CREATURE')
    models.Product.new(price=0, name='Manticore (Beta)', type='CREATURE')
    models.Product.new(price=0, name='Manticore (Alpha)', type='CREATURE')
    models.Product.new(price=0, name='Mantis', type='CREATURE')
    models.Product.new(price=0, name='Mantis Ghost', type='CREATURE')
    models.Product.new(price=0, name='Morellatops', type='CREATURE')
    models.Product.new(price=0, name='Rock Elemental', type='CREATURE')
    models.Product.new(price=0, name='Rubble Golem', type='CREATURE')
    models.Product.new(price=0, name='Thorny Dragon', type='CREATURE')
    models.Product.new(price=0, name='Vulture', type='CREATURE')
    models.Product.new(price=0, name='Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Phoenix', type='CREATURE')
    models.Product.new(price=0, name='Fire Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Lightning Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Poison Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Bone Fire Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Zombie Fire Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Zombie Lightning Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Zombie Poison Wyvern', type='CREATURE')
    models.Product.new(price=0, name='Chalk Golem', type='CREATURE')
    models.Product.new(price=0, name='Deinonychus', type='CREATURE')
    models.Product.new(price=0, name='Ice Golem', type='CREATURE')

    # Create Dye
    models.Product.new(price=0, name='Red Coloring', type='DYE')
    models.Product.new(price=0, name='Green Coloring', type='DYE')
    models.Product.new(price=0, name='Blue Coloring', type='DYE')
    models.Product.new(price=0, name='Yellow Coloring', type='DYE')
    models.Product.new(price=0, name='Orange Coloring', type='DYE')
    models.Product.new(price=0, name='Black Coloring', type='DYE')
    models.Product.new(price=0, name='White Coloring', type='DYE')
    models.Product.new(price=0, name='Brown Coloring', type='DYE')
    models.Product.new(price=0, name='Cyan Coloring', type='DYE')
    models.Product.new(price=0, name='Purple Coloring', type='DYE')
    models.Product.new(price=0, name='Forest Coloring', type='DYE')
    models.Product.new(price=0, name='Parchment Coloring', type='DYE')
    models.Product.new(price=0, name='Pink Coloring', type='DYE')
    models.Product.new(price=0, name='Royalty Coloring', type='DYE')
    models.Product.new(price=0, name='Silver Coloring', type='DYE')
    models.Product.new(price=0, name='Sky Coloring', type='DYE')
    models.Product.new(price=0, name='Tan Coloring', type='DYE')
    models.Product.new(price=0, name='Tangerine Coloring', type='DYE')
    models.Product.new(price=0, name='Magenta Coloring', type='DYE')
    models.Product.new(price=0, name='Brick Coloring', type='DYE')
    models.Product.new(price=0, name='Cantaloupe Coloring', type='DYE')
    models.Product.new(price=0, name='Mud Coloring', type='DYE')
    models.Product.new(price=0, name='Navy Coloring', type='DYE')
    models.Product.new(price=0, name='Olive Coloring', type='DYE')
    models.Product.new(price=0, name='Slate Coloring', type='DYE')

    # Create Egg
    models.Product.new(price=0, name='Stego Egg', type='EGG')
    models.Product.new(price=0, name='Bronto Egg', type='EGG')
    models.Product.new(price=0, name='Parasaur Egg', type='EGG')
    models.Product.new(price=0, name='Raptor Egg', type='EGG')
    models.Product.new(price=0, name='Rex Egg', type='EGG')
    models.Product.new(price=0, name='Trike Egg', type='EGG')
    models.Product.new(price=0, name='Dodo Egg', type='EGG')
    models.Product.new(price=0, name='Ankylo Egg', type='EGG')
    models.Product.new(price=0, name='Argentavis Egg', type='EGG')
    models.Product.new(price=0, name='Titanoboa Egg', type='EGG')
    models.Product.new(price=0, name='Carno Egg', type='EGG')
    models.Product.new(price=0, name='Dilo Egg', type='EGG')
    models.Product.new(price=0, name='Pteranodon Egg', type='EGG')
    models.Product.new(price=0, name='Sarco Egg', type='EGG')
    models.Product.new(price=0, name='Pulmonoscorpius Egg', type='EGG')
    models.Product.new(price=0, name='Araneo Egg', type='EGG')
    models.Product.new(price=0, name='Spino Egg', type='EGG')
    models.Product.new(price=0, name='Turtle Egg', type='EGG')
    models.Product.new(price=0, name='Pachycephalosaurus Egg', type='EGG')
    models.Product.new(price=0, name='Dimorph Egg', type='EGG')
    models.Product.new(price=0, name='Allosaurus Egg', type='EGG')
    models.Product.new(price=0, name='Archaeopteryx Egg', type='EGG')
    models.Product.new(price=0, name='Arthropluera Egg', type='EGG')
    models.Product.new(price=0, name='Baryonyx Egg', type='EGG')
    models.Product.new(price=0, name='Basic Maewing Egg', type='EGG')
    models.Product.new(price=0, name='Basilisk Egg', type='EGG')
    models.Product.new(price=0, name='Blood Crystal Wyvern Egg', type='EGG')
    models.Product.new(price=0, name='Bloodstalker Egg', type='EGG')
    models.Product.new(price=0, name='Camelsaurus Egg', type='EGG')
    models.Product.new(price=0, name='Compy Egg', type='EGG')
    models.Product.new(price=0, name='Crystal Wyvern Egg', type='EGG')
    models.Product.new(price=0, name='Deinonychus Egg', type='EGG')
    models.Product.new(price=0, name='Dimetrodon Egg', type='EGG')
    models.Product.new(price=0, name='Diplo Egg', type='EGG')
    models.Product.new(price=0, name='Ember Crystal Wyvern Egg', type='EGG')
    models.Product.new(price=0, name='Exceptional Maewing Egg', type='EGG')
    models.Product.new(price=0, name='Extraordinary Maewing Egg', type='EGG')
    models.Product.new(price=0, name='Featherlight Egg', type='EGG')
    models.Product.new(price=0, name='Fish Egg', type='EGG')
    models.Product.new(price=0, name='Gallimimus Egg', type='EGG')
    models.Product.new(price=0, name='Giganotosaurus Egg', type='EGG')
    models.Product.new(price=0, name='Glowtail Egg', type='EGG')
    models.Product.new(price=0, name='Golden Hesperornis Egg', type='EGG')
    models.Product.new(price=0, name='Hesperornis Egg', type='EGG')
    models.Product.new(price=0, name='Ichthyornis Egg', type='EGG')
    models.Product.new(price=0, name='Iguanodon Egg', type='EGG')
    models.Product.new(price=0, name='Kairuku Egg', type='EGG')
    models.Product.new(price=0, name='Kaprosuchus Egg', type='EGG')
    models.Product.new(price=0, name='Kentro Egg', type='EGG')
    models.Product.new(price=0, name='Lystro Egg', type='EGG')
    models.Product.new(price=0, name='Magmasaur Egg', type='EGG')
    models.Product.new(price=0, name='Mantis Egg', type='EGG')
    models.Product.new(price=0, name='Megachelon Egg', type='EGG')
    models.Product.new(price=0, name='Megalania Egg', type='EGG')
    models.Product.new(price=0, name='Megalosaurus Egg', type='EGG')
    models.Product.new(price=0, name='Microraptor Egg', type='EGG')
    models.Product.new(price=0, name='Moschops Egg', type='EGG')
    models.Product.new(price=0, name='Moth Egg', type='EGG')
    models.Product.new(price=0, name='Oviraptor Egg', type='EGG')
    models.Product.new(price=0, name='Pachyrhino Egg', type='EGG')
    models.Product.new(price=0, name='Pegomastax Egg', type='EGG')
    models.Product.new(price=0, name='Pelagornis Egg', type='EGG')
    models.Product.new(price=0, name='Quetzal Egg', type='EGG')
    models.Product.new(price=0, name='Regular Maewing Egg', type='EGG')
    models.Product.new(price=0, name='Rock Drake Egg', type='EGG')
    models.Product.new(price=0, name='Simple Maewing Egg', type='EGG')
    models.Product.new(price=0, name='Superior Maewing Egg', type='EGG')
    models.Product.new(price=0, name='Snow Owl Egg', type='EGG')
    models.Product.new(price=0, name='Tapejara Egg', type='EGG')
    models.Product.new(price=0, name='Tek Parasaur Egg', type='EGG')
    models.Product.new(price=0, name='Tek Quetzal Egg', type='EGG')
    models.Product.new(price=0, name='Tek Raptor Egg', type='EGG')
    models.Product.new(price=0, name='Tek Rex Egg', type='EGG')
    models.Product.new(price=0, name='Tek Stego Egg', type='EGG')
    models.Product.new(price=0, name='Tek Trike Egg', type='EGG')
    models.Product.new(price=0, name='Terror Bird Egg', type='EGG')
    models.Product.new(price=0, name='Therizino Egg', type='EGG')
    models.Product.new(price=0, name='Thorny Dragon Egg', type='EGG')
    models.Product.new(price=0, name='Troodon Egg', type='EGG')
    models.Product.new(price=0, name='Tropical Crystal Wyvern Egg', type='EGG')
    models.Product.new(price=0, name='Tropeognathus Egg', type='EGG')
    models.Product.new(price=0, name='Velonasaur Egg', type='EGG')
    models.Product.new(price=0, name='Vulture Egg', type='EGG')
    models.Product.new(price=0, name='Wyvern Egg Fire', type='EGG')
    models.Product.new(price=0, name='Wyvern Egg Lightning', type='EGG')
    models.Product.new(price=0, name='Wyvern Egg Poison', type='EGG')
    models.Product.new(price=0, name='Yutyrannus Egg', type='EGG')
    models.Product.new(price=0, name='Egg', type='EGG')
    models.Product.new(price=0, name='Large Egg', type='EGG')
    models.Product.new(price=0, name='Medium Egg', type='EGG')
    models.Product.new(price=0, name='Small Egg', type='EGG')
    models.Product.new(price=0, name='Special Egg', type='EGG')
    models.Product.new(price=0, name='Extra Large Egg', type='EGG')
    models.Product.new(price=0, name='Extra Small Egg', type='EGG')

    # Create Farm
    models.Product.new(price=0, name='Small Animal Feces', type='FARM')
    models.Product.new(price=0, name='Human Feces', type='FARM')
    models.Product.new(price=0, name='Medium Animal Feces', type='FARM')
    models.Product.new(price=0, name='Large Animal Feces', type='FARM')
    models.Product.new(price=0, name='Massive Animal Feces', type='FARM')
    models.Product.new(price=0, name='Snow Owl Pellet', type='FARM')

    # Create Recipe
    models.Product.new(price=0, name='Note', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Enduro Stew', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Lazarus Chowder', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Calien Soup', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Fria Curry', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Focal Chili', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Battle Tartare', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Shadow Steak Saute', type='RECIPE')
    models.Product.new(price=0, name='Notes on Rockwell Recipes', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Medical Brew', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Energy Brew', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Meat Jerky', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Decorative Coloring', type='RECIPE')
    models.Product.new(price=0, name='Rockwell Recipes: Mindwipe Tonic', type='RECIPE')

    # Create Resource
    models.Product.new(price=0, name='Wood', type='RESOURCE')
    models.Product.new(price=0, name='Stone', type='RESOURCE')
    models.Product.new(price=0, name='Metal', type='RESOURCE')
    models.Product.new(price=0, name='Hide', type='RESOURCE')
    models.Product.new(price=0, name='Chitin', type='RESOURCE')
    models.Product.new(price=0, name='Blood Pack', type='RESOURCE')
    models.Product.new(price=0, name='Fertilizer', type='RESOURCE')
    models.Product.new(price=0, name='Flint', type='RESOURCE')
    models.Product.new(price=0, name='Metal Ingot', type='RESOURCE')
    models.Product.new(price=0, name='Thatch', type='RESOURCE')
    models.Product.new(price=0, name='Fiber', type='RESOURCE')
    models.Product.new(price=0, name='Charcoal', type='RESOURCE')
    models.Product.new(price=0, name='Crystal', type='RESOURCE')
    models.Product.new(price=0, name='Sparkpowder', type='RESOURCE')
    models.Product.new(price=0, name='Gunpowder', type='RESOURCE')
    models.Product.new(price=0, name='Narcotic', type='RESOURCE')
    models.Product.new(price=0, name='Stimulant', type='RESOURCE')
    models.Product.new(price=0, name='Obsidian', type='RESOURCE')
    models.Product.new(price=0, name='Cementing Paste', type='RESOURCE')
    models.Product.new(price=0, name='Oil', type='RESOURCE')
    models.Product.new(price=0, name='Silica Pearls', type='RESOURCE')
    models.Product.new(price=0, name='Gasoline', type='RESOURCE')
    models.Product.new(price=0, name='Electronics', type='RESOURCE')
    models.Product.new(price=0, name='Polymer', type='RESOURCE')
    models.Product.new(price=0, name='Chitin or Keratin', type='RESOURCE')
    models.Product.new(price=0, name='Keratin', type='RESOURCE')
    models.Product.new(price=0, name='Rare Flower', type='RESOURCE')
    models.Product.new(price=0, name='Rare Mushroom', type='RESOURCE')
    models.Product.new(price=0, name='Re-Fertilizer', type='RESOURCE')
    models.Product.new(price=0, name='Pelt', type='RESOURCE')
    models.Product.new(price=0, name='Wishbone', type='RESOURCE')
    models.Product.new(price=0, name='Mistletoe', type='RESOURCE')
    models.Product.new(price=0, name='Coal', type='RESOURCE')
    models.Product.new(price=0, name='Birthday Candle', type='RESOURCE')
    models.Product.new(price=0, name='ARK Anniversary Surprise Cake', type='RESOURCE')
    models.Product.new(price=0, name='Cake Slice', type='RESOURCE')
    models.Product.new(price=0, name='Absorbent Substrate', type='RESOURCE')
    models.Product.new(price=0, name='Achatina Paste', type='RESOURCE')
    models.Product.new(price=0, name='Ambergris', type='RESOURCE')
    models.Product.new(price=0, name='Ammonite Bile', type='RESOURCE')
    models.Product.new(price=0, name='AnglerGel', type='RESOURCE')
    models.Product.new(price=0, name='Black Pearl', type='RESOURCE')
    models.Product.new(price=0, name='Blue Crystalized Sap', type='RESOURCE')
    models.Product.new(price=0, name='Blue Gem', type='RESOURCE')
    models.Product.new(price=0, name='Charge Battery', type='RESOURCE')
    models.Product.new(price=0, name='Clay', type='RESOURCE')
    models.Product.new(price=0, name='Condensed Gas', type='RESOURCE')
    models.Product.new(price=0, name='Congealed Gas Ball', type='RESOURCE')
    models.Product.new(price=0, name='Corrupted Nodule', type='RESOURCE')
    models.Product.new(price=0, name='Crafted Element Dust', type='RESOURCE')
    models.Product.new(price=0, name='Deathworm Horn', type='RESOURCE')
    models.Product.new(price=0, name='Deathworm Horn or Woolly Rhino Horn', type='RESOURCE')
    models.Product.new(price=0, name='Dermis', type='RESOURCE')
    models.Product.new(price=0, name='Dinosaur Bone', type='RESOURCE')
    models.Product.new(price=0, name='Element', type='RESOURCE')
    models.Product.new(price=0, name='Element Dust', type='RESOURCE')
    models.Product.new(price=0, name='Element Ore', type='RESOURCE')
    models.Product.new(price=0, name='Element Shard', type='RESOURCE')
    models.Product.new(price=0, name='Fragmented Green Gem', type='RESOURCE')
    models.Product.new(price=0, name='Fungal Wood', type='RESOURCE')
    models.Product.new(price=0, name='Corrupted Wood', type='RESOURCE')
    models.Product.new(price=0, name='Golden Nugget', type='RESOURCE')
    models.Product.new(price=0, name='Green Gem', type='RESOURCE')
    models.Product.new(price=0, name='High Quality Pollen', type='RESOURCE')
    models.Product.new(price=0, name='Human Hair', type='RESOURCE')
    models.Product.new(price=0, name='Leech Blood', type='RESOURCE')
    models.Product.new(price=0, name='Leech Blood or Horns', type='RESOURCE')
    models.Product.new(price=0, name='Mutagel', type='RESOURCE')
    models.Product.new(price=0, name='Mutagen', type='RESOURCE')
    models.Product.new(price=0, name='Oil (Tusoteuthis)', type='RESOURCE')
    models.Product.new(price=0, name='Organic Polymer', type='RESOURCE')
    models.Product.new(price=0, name='Pelt, Hair, or Wool', type='RESOURCE')
    models.Product.new(price=0, name='Primal Crystal', type='RESOURCE')
    models.Product.new(price=0, name='Preserving Salt', type='RESOURCE')
    models.Product.new(price=0, name='Propellant', type='RESOURCE')
    models.Product.new(price=0, name='Raw Salt', type='RESOURCE')
    models.Product.new(price=0, name='Red Crystalized Sap', type='RESOURCE')
    models.Product.new(price=0, name='Red Gem', type='RESOURCE')
    models.Product.new(price=0, name='Sand', type='RESOURCE')
    models.Product.new(price=0, name='Sap', type='RESOURCE')
    models.Product.new(price=0, name='Scrap Metal', type='RESOURCE')
    models.Product.new(price=0, name='Scrap Metal Ingot', type='RESOURCE')
    models.Product.new(price=0, name='Shell Fragment', type='RESOURCE')
    models.Product.new(price=0, name='Silicate', type='RESOURCE')
    models.Product.new(price=0, name='Silk', type='RESOURCE')
    models.Product.new(price=0, name='Sulfur', type='RESOURCE')
    models.Product.new(price=0, name='Unstable Element', type='RESOURCE')
    models.Product.new(price=0, name='Unstable Element Shard', type='RESOURCE')
    models.Product.new(price=0, name='Wool', type='RESOURCE')
    models.Product.new(price=0, name='Woolly Rhino Horn', type='RESOURCE')

    # Create Seed
    models.Product.new(price=0, name='Berrybush Seeds', type='SEED')
    models.Product.new(price=0, name='Amarberry Seed', type='SEED')
    models.Product.new(price=0, name='Citronal Seed', type='SEED')
    models.Product.new(price=0, name='Azulberry Seed', type='SEED')
    models.Product.new(price=0, name='Tintoberry Seed', type='SEED')
    models.Product.new(price=0, name='Mejoberry Seed', type='SEED')
    models.Product.new(price=0, name='Narcoberry Seed', type='SEED')
    models.Product.new(price=0, name='Stimberry Seed', type='SEED')
    models.Product.new(price=0, name='Savoroot Seed', type='SEED')
    models.Product.new(price=0, name='Longrass Seed', type='SEED')
    models.Product.new(price=0, name='Rockarrot Seed', type='SEED')
    models.Product.new(price=0, name='Amarberry Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Azulberry Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Tintoberry Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Narcoberry Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Stimberry Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Mejoberry Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Citronal Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Savoroot Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Longrass Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Rockarrot Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Plant Species X Seed', type='SEED')
    models.Product.new(price=0, name='Plant Species X Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Plant Species Y Seed', type='SEED')
    models.Product.new(price=0, name='Plant Species Z Seed', type='SEED')
    models.Product.new(price=0, name='Plant Species Y Seed (instant grow)', type='SEED')
    models.Product.new(price=0, name='Plant Species Z Seed (SpeedHack)', type='SEED')

    # Create Skin
    models.Product.new(price=0, name='Hunter Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Rex Stomped Glasses Saddle Skin', type='SKIN')
    models.Product.new(price=0, name='Parasaur Stylish Saddle Skin', type='SKIN')
    models.Product.new(price=0, name='Rex Bone Helmet', type='SKIN')
    models.Product.new(price=0, name='Dino Glasses Skin', type='SKIN')
    models.Product.new(price=0, name='Fireworks Flaregun Skin', type='SKIN')
    models.Product.new(price=0, name='Trike Bone Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='DodoRex Mask Skin', type='SKIN')
    models.Product.new(price=0, name='Chibi Party Rex', type='SKIN')
    models.Product.new(price=0, name='Chibi-Allosaurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Ammonite', type='SKIN')
    models.Product.new(price=0, name='Chibi-Ankylosaurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Argentavis', type='SKIN')
    models.Product.new(price=0, name='Chibi-Astrocetus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Baryonyx', type='SKIN')
    models.Product.new(price=0, name='Chibi-Basilisk', type='SKIN')
    models.Product.new(price=0, name='Chibi-Beelzebufo', type='SKIN')
    models.Product.new(price=0, name='Chibi-Bloodstalker', type='SKIN')
    models.Product.new(price=0, name='Chibi-Bonnet Otter', type='SKIN')
    models.Product.new(price=0, name='Chibi-Brontosaurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Broodmother', type='SKIN')
    models.Product.new(price=0, name='Chibi-Bulbdog', type='SKIN')
    models.Product.new(price=0, name='Chibi-Bunny', type='SKIN')
    models.Product.new(price=0, name='Chibi-Carbonemys', type='SKIN')
    models.Product.new(price=0, name='Chibi-Carno', type='SKIN')
    models.Product.new(price=0, name='Chibi-Castroides', type='SKIN')
    models.Product.new(price=0, name='Chibi-Cnidaria', type='SKIN')
    models.Product.new(price=0, name='Chibi-Crystal Wyvern', type='SKIN')
    models.Product.new(price=0, name='Chibi-Daeodon', type='SKIN')
    models.Product.new(price=0, name='Chibi-Direbear', type='SKIN')
    models.Product.new(price=0, name='Chibi-Direwolf', type='SKIN')
    models.Product.new(price=0, name='Chibi-Dodo', type='SKIN')
    models.Product.new(price=0, name='Chibi-Doedicurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Dunkleosteus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Enforcer', type='SKIN')
    models.Product.new(price=0, name='Chibi-Equus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Featherlight', type='SKIN')
    models.Product.new(price=0, name='Chibi-Ferox (Large)', type='SKIN')
    models.Product.new(price=0, name='Chibi-Ferox (Small)', type='SKIN')
    models.Product.new(price=0, name='Chibi-Gacha Claus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Gasbag', type='SKIN')
    models.Product.new(price=0, name='Chibi-Giganotosaurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Gigantopithecus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Glowtail', type='SKIN')
    models.Product.new(price=0, name='Chibi-Griffin', type='SKIN')
    models.Product.new(price=0, name='Chibi-Iguanodon', type='SKIN')
    models.Product.new(price=0, name='Chibi-Karkinos', type='SKIN')
    models.Product.new(price=0, name='Chibi-Kentrosaurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Magmasaur', type='SKIN')
    models.Product.new(price=0, name='Chibi-Mammoth', type='SKIN')
    models.Product.new(price=0, name='Chibi-Managarmr', type='SKIN')
    models.Product.new(price=0, name='Chibi-Manta', type='SKIN')
    models.Product.new(price=0, name='Chibi-Mantis', type='SKIN')
    models.Product.new(price=0, name='Chibi-Megalania', type='SKIN')
    models.Product.new(price=0, name='Chibi-Megaloceros', type='SKIN')
    models.Product.new(price=0, name='Chibi-Megalodon', type='SKIN')
    models.Product.new(price=0, name='Chibi-Megatherium', type='SKIN')
    models.Product.new(price=0, name='Chibi-Mesopithecus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Moschops', type='SKIN')
    models.Product.new(price=0, name='Chibi-Otter', type='SKIN')
    models.Product.new(price=0, name='Chibi-Oviraptor', type='SKIN')
    models.Product.new(price=0, name='Chibi-Ovis', type='SKIN')
    models.Product.new(price=0, name='Chibi-Paraceratherium', type='SKIN')
    models.Product.new(price=0, name='Chibi-Parasaur', type='SKIN')
    models.Product.new(price=0, name='Chibi-Phiomia', type='SKIN')
    models.Product.new(price=0, name='Chibi-Phoenix', type='SKIN')
    models.Product.new(price=0, name='Chibi-Plesiosaur', type='SKIN')
    models.Product.new(price=0, name='Chibi-Procoptodon', type='SKIN')
    models.Product.new(price=0, name='Chibi-Pteranodon', type='SKIN')
    models.Product.new(price=0, name='Chibi-Pulmonoscorpius', type='SKIN')
    models.Product.new(price=0, name='Chibi-Quetzal', type='SKIN')
    models.Product.new(price=0, name='Chibi-Raptor', type='SKIN')
    models.Product.new(price=0, name='Chibi-Reaper', type='SKIN')
    models.Product.new(price=0, name='Chibi-Reindeer', type='SKIN')
    models.Product.new(price=0, name='Chibi-Rex', type='SKIN')
    models.Product.new(price=0, name='Chibi-Rhino', type='SKIN')
    models.Product.new(price=0, name='Chibi-Rock Drake', type='SKIN')
    models.Product.new(price=0, name='Chibi-Rock Golem', type='SKIN')
    models.Product.new(price=0, name='Chibi-Rollrat', type='SKIN')
    models.Product.new(price=0, name='Chibi-Sabertooth', type='SKIN')
    models.Product.new(price=0, name='Chibi-Sarco', type='SKIN')
    models.Product.new(price=0, name='Chibi-Seeker', type='SKIN')
    models.Product.new(price=0, name='Chibi-Shadowmane', type='SKIN')
    models.Product.new(price=0, name='Chibi-Shinehorn', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Brontosaurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Carno', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Giganotosaurus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Jerboa', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Quetzal', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Raptor', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Rex', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Stego', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Trike', type='SKIN')
    models.Product.new(price=0, name='Chibi-Skeletal Wyvern', type='SKIN')
    models.Product.new(price=0, name='Chibi-Snow Owl', type='SKIN')
    models.Product.new(price=0, name='Chibi-Spino', type='SKIN')
    models.Product.new(price=0, name='Chibi-Stego', type='SKIN')
    models.Product.new(price=0, name='Chibi-Tapejara', type='SKIN')
    models.Product.new(price=0, name='Chibi-Terror Bird', type='SKIN')
    models.Product.new(price=0, name='Chibi-Therizino', type='SKIN')
    models.Product.new(price=0, name='Chibi-Thylacoleo', type='SKIN')
    models.Product.new(price=0, name='Chibi-Trike', type='SKIN')
    models.Product.new(price=0, name='Chibi-Troodon', type='SKIN')
    models.Product.new(price=0, name='Chibi-Tropeognathus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Tusoteuthis', type='SKIN')
    models.Product.new(price=0, name='Chibi-Unicorn', type='SKIN')
    models.Product.new(price=0, name='Chibi-Velonasaur', type='SKIN')
    models.Product.new(price=0, name='Chibi-Wyvern', type='SKIN')
    models.Product.new(price=0, name='Chibi-Yutyrannus', type='SKIN')
    models.Product.new(price=0, name='Chibi-Zombie Wyvern', type='SKIN')
    models.Product.new(price=0, name='Pair-o-Saurs Chibi', type='SKIN')
    models.Product.new(price=0, name='Teeny Tiny Titano', type='SKIN')
    models.Product.new(price=0, name='White-Collar Kairuku', type='SKIN')
    models.Product.new(price=0, name='Aberrant Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Aberrant Sword Skin', type='SKIN')
    models.Product.new(price=0, name='Alpha Raptor Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Alpha Raptor Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Araneo Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Araneo Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='ARK Tester Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Basilisk Ghost Costume', type='SKIN')
    models.Product.new(price=0, name='Birthday Suit Pants Skin', type='SKIN')
    models.Product.new(price=0, name='Birthday Suit Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Blue-Ball Winter Beanie Skin', type='SKIN')
    models.Product.new(price=0, name='Bonnet Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Bow & Eros Skin', type='SKIN')
    models.Product.new(price=0, name='Brachiosaurus Costume', type='SKIN')
    models.Product.new(price=0, name='Bronto Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Bulbdog Ghost Costume', type='SKIN')
    models.Product.new(price=0, name='Bulbdog Mask Skin', type='SKIN')
    models.Product.new(price=0, name='Bulbdog-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Bunny Ears Skin', type='SKIN')
    models.Product.new(price=0, name='Candy Cane Club Skin', type='SKIN')
    models.Product.new(price=0, name="Captain's Hat Skin", type='SKIN')
    models.Product.new(price=0, name='Carno Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Chieftan Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Chili Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Chocolate Rabbit Club Skin', type='SKIN')
    models.Product.new(price=0, name='Christmas Bola Skin', type='SKIN')
    models.Product.new(price=0, name='Clown Mask Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Avatar Boots Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Avatar Gloves Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Avatar Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Avatar Pants Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Avatar Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Boots Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Chestpiece Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Gloves Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Corrupted Pants Skin', type='SKIN')
    models.Product.new(price=0, name='Crab Fest Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Crab Fest Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Cupid Couture Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Cupid Couture Top Skin', type='SKIN')
    models.Product.new(price=0, name='Cute Dino Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Decorative Ravager Saddle Skin', type='SKIN')
    models.Product.new(price=0, name='Dilo Mask Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Bunny Ears Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Easter Chick Hat', type='SKIN')
    models.Product.new(price=0, name='Dino Easter Egg Hat', type='SKIN')
    models.Product.new(price=0, name='Dino Marshmallow Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Ornament Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Ornament Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Party Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Santa Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Uncle Sam Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Dino Witch Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Direwolf Ghost Costume', type='SKIN')
    models.Product.new(price=0, name='Dodo Pie Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Dodo Pie Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Dodorex Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Dodorex Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Dodorex-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='DodoWyvern Mask Skin', type='SKIN')
    models.Product.new(price=0, name='E4 Remote Eggsplosives Skin', type='SKIN')
    models.Product.new(price=0, name='Easter Chick Hat', type='SKIN')
    models.Product.new(price=0, name='Easter Egg Hat', type='SKIN')
    models.Product.new(price=0, name='Easter Egghead Skin', type='SKIN')
    models.Product.new(price=0, name='Fan Ballcap Skin', type='SKIN')
    models.Product.new(price=0, name='Federation Exo Boots Skin', type='SKIN')
    models.Product.new(price=0, name='Federation Exo Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Federation Exo-Chestpiece Skin', type='SKIN')
    models.Product.new(price=0, name='Federation Exo-Gloves Skin', type='SKIN')
    models.Product.new(price=0, name='Federation Exo-leggings Skin', type='SKIN')
    models.Product.new(price=0, name='Felt Reindeer Antlers Skin', type='SKIN')
    models.Product.new(price=0, name='Fireworks Rocket Launcher Skin', type='SKIN')
    models.Product.new(price=0, name='Fish Bite Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Fish Bite Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Floral Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Floral Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Flying Disc Skin', type='SKIN')
    models.Product.new(price=0, name='Gasbags-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Giga Bionic Costume', type='SKIN')
    models.Product.new(price=0, name='Giga Poop Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Giga Poop Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Giganotosaurus Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Glider Suit', type='SKIN')
    models.Product.new(price=0, name='Gray-Ball Winter Beanie Skin', type='SKIN')
    models.Product.new(price=0, name='Green-Ball Winter Beanie Skin', type='SKIN')
    models.Product.new(price=0, name='Grilling Spatula Skin', type='SKIN')
    models.Product.new(price=0, name='Halo Headband Skin', type='SKIN')
    models.Product.new(price=0, name='Headless Costume Skin', type='SKIN')
    models.Product.new(price=0, name='Heart-shaped Shield Skin', type='SKIN')
    models.Product.new(price=0, name='Heart-shaped Sunglasses Skin', type='SKIN')
    models.Product.new(price=0, name='Hockey Mask Skin', type='SKIN')
    models.Product.new(price=0, name='HomoDeus Boots Skin', type='SKIN')
    models.Product.new(price=0, name='HomoDeus Gloves Skin', type='SKIN')
    models.Product.new(price=0, name='HomoDeus Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='HomoDeus Pants Skin', type='SKIN')
    models.Product.new(price=0, name='HomoDeus Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Ice Pop-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Ichthy Isles Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Ichthy Isles Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Jack-O-Lantern Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Jack-O-Lantern Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Jack-O-Lantern-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Jerboa Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Jerboa Wreath Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Jerboa Wreath Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Love Shackles Skin', type='SKIN')
    models.Product.new(price=0, name='Manticore Boots Skin', type='SKIN')
    models.Product.new(price=0, name='Manticore Chestpiece Skin', type='SKIN')
    models.Product.new(price=0, name='Manticore Gauntlets Skin', type='SKIN')
    models.Product.new(price=0, name='Manticore Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Manticore Leggings Skin', type='SKIN')
    models.Product.new(price=0, name='Manticore Shield Skin', type='SKIN')
    models.Product.new(price=0, name='Mantis Ghost Costume', type='SKIN')
    models.Product.new(price=0, name='Marshmallow Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Master Controller Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Meat Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Meat Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Megaloceros Reindeer Costume', type='SKIN')
    models.Product.new(price=0, name='Mini-HLNA Skin', type='SKIN')
    models.Product.new(price=0, name='Mosasaurus Bionic Costume', type='SKIN')
    models.Product.new(price=0, name='Murder Turkey Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Murder Turkey Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Murder-Turkey-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Nerdry Glasses Skin', type='SKIN')
    models.Product.new(price=0, name='Noglin Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Noglin Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Nutcracker Slingshot Skin', type='SKIN')
    models.Product.new(price=0, name='Onyc Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Onyc Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Otter Mask Skin', type='SKIN')
    models.Product.new(price=0, name='Parasaur Bionic Costume', type='SKIN')
    models.Product.new(price=0, name='Party Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Pilgrim Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Pitchfork Skin', type='SKIN')
    models.Product.new(price=0, name='Poglin Mask Skin', type='SKIN')
    models.Product.new(price=0, name='Procoptodon Bunny Costume', type='SKIN')
    models.Product.new(price=0, name='Purple-Ball Winter Beanie Skin', type='SKIN')
    models.Product.new(price=0, name='Purple-Ball Winter Beanie Skin (Winter Wonderland 5)', type='SKIN')
    models.Product.new(price=0, name='Quetzal Bionic Costume', type='SKIN')
    models.Product.new(price=0, name="Raptor 'ARK: The Animated Series' Costume", type='SKIN')
    models.Product.new(price=0, name='Raptor Bionic Costume', type='SKIN')
    models.Product.new(price=0, name='Quetzalcoatlus Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Raptor Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Reaper Ghost Costume', type='SKIN')
    models.Product.new(price=0, name='Reaper Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Reaper Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Reaper Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Reaper-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Red-Ball Winter Beanie Skin', type='SKIN')
    models.Product.new(price=0, name='Rex Bionic Costume', type='SKIN')
    models.Product.new(price=0, name='Rex Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Rex Ghost Costume', type='SKIN')
    models.Product.new(price=0, name='Safari Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Santa Hat Skin', type='SKIN')
    models.Product.new(price=0, name="Santiago's Axe Skin", type='SKIN')
    models.Product.new(price=0, name="Santiago's Spear Skin", type='SKIN')
    models.Product.new(price=0, name='Scary Pumpkin Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Scary Skull Helmet Skin', type='SKIN')
    models.Product.new(price=0, name='Scorched Spike Skin', type='SKIN')
    models.Product.new(price=0, name='Scorched Sword Skin', type='SKIN')
    models.Product.new(price=0, name='Scorched Torch Skin', type='SKIN')
    models.Product.new(price=0, name='Sea Life-Print Shirt Skin', type='SKIN')
    models.Product.new(price=0, name='Snow Owl Ghost Costume', type='SKIN')
    models.Product.new(price=0, name='Stego Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Stegosaurus Bionic Costume', type='SKIN')
    models.Product.new(price=0, name='Stygimoloch Costume', type='SKIN')
    models.Product.new(price=0, name='Styracosaurus Costume', type='SKIN')
    models.Product.new(price=0, name='Sunglasses Skin', type='SKIN')
    models.Product.new(price=0, name='Sweet Spear Carrot Skin', type='SKIN')
    models.Product.new(price=0, name='T-Rex Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='T-Rex Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Teddy Bear Grenades Skin', type='SKIN')
    models.Product.new(price=0, name='Thorny Dragon Vagabond Saddle Skin', type='SKIN')
    models.Product.new(price=0, name='Top Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Torch Sparkler Skin', type='SKIN')
    models.Product.new(price=0, name='Triceratops Bionic Costume', type='SKIN')
    models.Product.new(price=0, name='Trike Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Turkey Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Turkey Leg Skin', type='SKIN')
    models.Product.new(price=0, name='Turkey Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Turkey Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly Bronto Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly Bulbdog Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly Carno Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly Caroling Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly Chibi Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly Cornucopia Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly T-Rex Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Ugly Trike Sweater Skin', type='SKIN')
    models.Product.new(price=0, name='Uncle Sam Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Vampire Dodo Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Vampire Dodo Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Vampire Eyes Skin', type='SKIN')
    models.Product.new(price=0, name='Water Soaker Skin', type='SKIN')
    models.Product.new(price=0, name='Werewolf Mask Skin', type='SKIN')
    models.Product.new(price=0, name='Witch Hat Skin', type='SKIN')
    models.Product.new(price=0, name='Wizard Ballcap Skin', type='SKIN')
    models.Product.new(price=0, name='Wyvern Bone Costume', type='SKIN')
    models.Product.new(price=0, name='Wyvern Gloves Skin', type='SKIN')
    models.Product.new(price=0, name='Yeti Swim Bottom Skin', type='SKIN')
    models.Product.new(price=0, name='Yeti Swim Top Skin', type='SKIN')
    models.Product.new(price=0, name='Zip-Line Motor Attachment Skin', type='SKIN')

    # Create Structure
    models.Product.new(price=0, name='Campfire', type='STRUCTURE')
    models.Product.new(price=0, name='Standing Torch', type='STRUCTURE')
    models.Product.new(price=0, name='Hide Sleeping Bag', type='STRUCTURE')
    models.Product.new(price=0, name='Thatch Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Thatch Door', type='STRUCTURE')
    models.Product.new(price=0, name='Thatch Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Thatch Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Thatch Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Catwalk', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Door', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Ladder', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Pillar', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Ramp', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Windowframe', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Window', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Sign', type='STRUCTURE')
    models.Product.new(price=0, name='Storage Box', type='STRUCTURE')
    models.Product.new(price=0, name='Large Storage Box', type='STRUCTURE')
    models.Product.new(price=0, name='Mortar and Pestle', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Irrigation Pipe - Intake', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Irrigation Pipe - Straight', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Irrigation Pipe - Inclined', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Irrigation Pipe - Intersection', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Irrigation Pipe - Vertical', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Irrigation Pipe - Tap', type='STRUCTURE')
    models.Product.new(price=0, name='Refining Forge', type='STRUCTURE')
    models.Product.new(price=0, name='Smithy', type='STRUCTURE')
    models.Product.new(price=0, name='Compost Bin', type='STRUCTURE')
    models.Product.new(price=0, name='Cooking Pot', type='STRUCTURE')
    models.Product.new(price=0, name='Simple Bed', type='STRUCTURE')
    models.Product.new(price=0, name='Small Crop Plot', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Fence Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Dinosaur Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Dinosaur Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Catwalk', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Door', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Fence Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Ladder', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Pillar', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Ramp', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Windowframe', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Window', type='STRUCTURE')
    models.Product.new(price=0, name='Fabricator', type='STRUCTURE')
    models.Product.new(price=0, name='Water Reservoir', type='STRUCTURE')
    models.Product.new(price=0, name='Air Conditioner', type='STRUCTURE')
    models.Product.new(price=0, name='Electrical Generator', type='STRUCTURE')
    models.Product.new(price=0, name='Electrical Outlet', type='STRUCTURE')
    models.Product.new(price=0, name='Inclined Electrical Cable', type='STRUCTURE')
    models.Product.new(price=0, name='Electrical Cable Intersection', type='STRUCTURE')
    models.Product.new(price=0, name='Straight Electrical Cable', type='STRUCTURE')
    models.Product.new(price=0, name='Vertical Electrical Cable', type='STRUCTURE')
    models.Product.new(price=0, name='Lamppost', type='STRUCTURE')
    models.Product.new(price=0, name='Refrigerator', type='STRUCTURE')
    models.Product.new(price=0, name='Auto Turret', type='STRUCTURE')
    models.Product.new(price=0, name='Remote Keypad', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Irrigation Pipe - Inclined', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Irrigation Pipe - Intake', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Irrigation Pipe - Intersection', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Irrigation Pipe - Straight', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Irrigation Pipe - Tap', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Irrigation Pipe - Vertical', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Sign', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Billboard', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Billboard', type='STRUCTURE')
    models.Product.new(price=0, name='Medium Crop Plot', type='STRUCTURE')
    models.Product.new(price=0, name='Large Crop Plot', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Wall Sign', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Dinosaur Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Dinosaur Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Wall Sign', type='STRUCTURE')
    models.Product.new(price=0, name='Multi-Panel Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Spider Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Preserving Bin', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Spike Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Vault', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Spike Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Bookshelf', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Fence Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Water Reservoir', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Reinforced Wooden Door', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Reinforced Dinosaur Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Dinosaur Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Pillar', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Windowframe', type='STRUCTURE')
    models.Product.new(price=0, name='Reinforced Window', type='STRUCTURE')
    models.Product.new(price=0, name='Reinforced Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Omnidirectional Lamppost', type='STRUCTURE')
    models.Product.new(price=0, name='Industrial Grill', type='STRUCTURE')
    models.Product.new(price=0, name='Single Panel Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Feeding Trough', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Stone Dinosaur Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Reinforced Dinosaur Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Thatch Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Thatch Wall Left', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Thatch Wall Right', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Wooden Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Wood Wall Left', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Wood Wall Right', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Stone Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Stone Wall Left', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Stone Wall Right', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Metal Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Metal Wall Left', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Metal Wall Right', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Raft', type='STRUCTURE')
    models.Product.new(price=0, name='Painting Canvas', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Door', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Greenhouse Wall Left', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Greenhouse Wall Right', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Greenhouse Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Window', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Dedicated Storage', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Double Door', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Double Door', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Double Door', type='STRUCTURE')
    models.Product.new(price=0, name='Reinforced Double Door', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Double Door', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Double Door', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Double Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Double Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Double Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Double Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Double Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Double Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Fence Support', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Fence Support', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Fence Support', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Fence Support', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Fence Support', type='STRUCTURE')
    models.Product.new(price=0, name='Large Adobe Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Large Metal Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Large Stone Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Large Tek Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Large Wooden Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Irrigation Pipe - Flexible', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Irrigation Pipe - Flexible', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Stairs', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Stairs', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Stairs', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Stairs', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Stairs', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Triangle Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Triangle Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Triangle Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Triangle Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Triangle Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Triangle Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Triangle Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Triangle Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Triangle Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Triangle Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Triangle Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Triangle Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Greenhouse Triangle Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Triangle Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Triangle Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Triangle Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Triangle Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Flexible Electrical Cable', type='STRUCTURE')
    models.Product.new(price=0, name='Pumpkin', type='STRUCTURE')
    models.Product.new(price=0, name='Scarecrow', type='STRUCTURE')
    models.Product.new(price=0, name='Stolen Headstone', type='STRUCTURE')
    models.Product.new(price=0, name='Wreath', type='STRUCTURE')
    models.Product.new(price=0, name='Holiday Lights', type='STRUCTURE')
    models.Product.new(price=0, name='Holiday Stocking', type='STRUCTURE')
    models.Product.new(price=0, name='Holiday Tree', type='STRUCTURE')
    models.Product.new(price=0, name='Snowman', type='STRUCTURE')
    models.Product.new(price=0, name='Gift Box', type='STRUCTURE')
    models.Product.new(price=0, name='Bunny Egg', type='STRUCTURE')
    models.Product.new(price=0, name='Birthday Cake', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Dinosaur Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Dinosaur Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Door', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Fence Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Ladder', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Pillar', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Railing', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Ramp', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Staircase', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Window', type='STRUCTURE')
    models.Product.new(price=0, name='Adobe Windowframe', type='STRUCTURE')
    models.Product.new(price=0, name='Artifact Pedestal', type='STRUCTURE')
    models.Product.new(price=0, name='Ballista Turret', type='STRUCTURE')
    models.Product.new(price=0, name='Bee Hive', type='STRUCTURE')
    models.Product.new(price=0, name='Beer Barrel', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Adobe Dinosaur Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Adobe Dinosaur Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Tek Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Behemoth Tek Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Bunk Bed', type='STRUCTURE')
    models.Product.new(price=0, name='Cannon', type='STRUCTURE')
    models.Product.new(price=0, name='Catapult Turret', type='STRUCTURE')
    models.Product.new(price=0, name='Chemistry Bench', type='STRUCTURE')
    models.Product.new(price=0, name='Cloning Chamber', type='STRUCTURE')
    models.Product.new(price=0, name='Cryofridge', type='STRUCTURE')
    models.Product.new(price=0, name='Crystal Wyvern Queen Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Delivery Crate', type='STRUCTURE')
    models.Product.new(price=0, name='Dino Leash', type='STRUCTURE')
    models.Product.new(price=0, name='Dragon Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Elevator Track', type='STRUCTURE')
    models.Product.new(price=0, name='Fish Basket', type='STRUCTURE')
    models.Product.new(price=0, name='Gas Collector', type='STRUCTURE')
    models.Product.new(price=0, name='Giant Adobe Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Giant Adobe Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Giant Metal Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Giant Metal Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Giant Reinforced Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Giant Stone Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Gorilla Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Gravestone', type='STRUCTURE')
    models.Product.new(price=0, name='Heavy Auto Turret', type='STRUCTURE')
    models.Product.new(price=0, name='Homing Underwater Mine', type='STRUCTURE')
    models.Product.new(price=0, name='Industrial Cooker', type='STRUCTURE')
    models.Product.new(price=0, name='Industrial Forge', type='STRUCTURE')
    models.Product.new(price=0, name='Industrial Grinder', type='STRUCTURE')
    models.Product.new(price=0, name='King Titan Flag', type='STRUCTURE')
    models.Product.new(price=0, name='King Titan Flag (Mecha)', type='STRUCTURE')
    models.Product.new(price=0, name='Large Elevator Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Large Taxidermy Base', type='STRUCTURE')
    models.Product.new(price=0, name='Large Wood Elevator Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Manticore Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Medium Elevator Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Medium Taxidermy Base', type='STRUCTURE')
    models.Product.new(price=0, name='Medium Wood Elevator Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Cliff Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Ocean Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Railing', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Staircase', type='STRUCTURE')
    models.Product.new(price=0, name='Metal Tree Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Minigun Turret', type='STRUCTURE')
    models.Product.new(price=0, name='Mirror', type='STRUCTURE')
    models.Product.new(price=0, name='Moeder Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Motorboat', type='STRUCTURE')
    models.Product.new(price=0, name='Oil Pump', type='STRUCTURE')
    models.Product.new(price=0, name='Plant Species Y Trap', type='STRUCTURE')
    models.Product.new(price=0, name='Portable Rope Ladder', type='STRUCTURE')
    models.Product.new(price=0, name='Pressure Plate', type='STRUCTURE')
    models.Product.new(price=0, name='Rocket Turret', type='STRUCTURE')
    models.Product.new(price=0, name='Rockwell Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Rope Ladder', type='STRUCTURE')
    models.Product.new(price=0, name='Shag Rug', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Adobe Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Adobe Wall Left', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Adobe Wall Right', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Tek Roof', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Tek Wall Left', type='STRUCTURE')
    models.Product.new(price=0, name='Sloped Tek Wall Right', type='STRUCTURE')
    models.Product.new(price=0, name='Small Elevator Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Small Taxidermy Base', type='STRUCTURE')
    models.Product.new(price=0, name='Small Wood Elevator Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Cliff Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Fireplace', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Railing', type='STRUCTURE')
    models.Product.new(price=0, name='Stone Staircase', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Bridge', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Catwalk', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Ceiling', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Dinosaur Gateway', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Dinosaur Gate', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Doorframe', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Door', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Fence Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Forcefield', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Foundation', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Generator', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Hatchframe', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Jump Pad', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Ladder', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Light', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Pillar', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Railing', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Ramp', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Replicator', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Sensor', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Sleeping Pod', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Staircase', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Teleporter', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Transmitter', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Trapdoor', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Trough', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Turret', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Wall', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Windowframe', type='STRUCTURE')
    models.Product.new(price=0, name='Tek Window', type='STRUCTURE')
    models.Product.new(price=0, name='Tent', type='STRUCTURE')
    models.Product.new(price=0, name='Toilet', type='STRUCTURE')
    models.Product.new(price=0, name='Training Dummy', type='STRUCTURE')
    models.Product.new(price=0, name='Tree Sap Tap', type='STRUCTURE')
    models.Product.new(price=0, name='Trophy Wall-Mount', type='STRUCTURE')
    models.Product.new(price=0, name='Vacuum Compartment Moonpool', type='STRUCTURE')
    models.Product.new(price=0, name='Vacuum Compartment', type='STRUCTURE')
    models.Product.new(price=0, name='Vessel', type='STRUCTURE')
    models.Product.new(price=0, name='VR Boss Flag', type='STRUCTURE')
    models.Product.new(price=0, name='Wall Torch', type='STRUCTURE')
    models.Product.new(price=0, name='War Map', type='STRUCTURE')
    models.Product.new(price=0, name='Wardrums', type='STRUCTURE')
    models.Product.new(price=0, name='Water Well', type='STRUCTURE')
    models.Product.new(price=0, name='Wind Turbine', type='STRUCTURE')
    models.Product.new(price=0, name='Wood Elevator Top Switch', type='STRUCTURE')
    models.Product.new(price=0, name='Wood Elevator Track', type='STRUCTURE')
    models.Product.new(price=0, name='Wood Ocean Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Bench', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Cage', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Chair', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Railing', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Staircase', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Table', type='STRUCTURE')
    models.Product.new(price=0, name='Wooden Tree Platform', type='STRUCTURE')
    models.Product.new(price=0, name='Plant Species X', type='STRUCTURE')
    models.Product.new(price=0, name='Tek ATV', type='STRUCTURE')

    # Create Tool
    models.Product.new(price=0, name='Stone Pick', type='TOOL')
    models.Product.new(price=0, name='Stone Hatchet', type='TOOL')
    models.Product.new(price=0, name='Metal Pick', type='TOOL')
    models.Product.new(price=0, name='Metal Hatchet', type='TOOL')
    models.Product.new(price=0, name='Torch', type='TOOL')
    models.Product.new(price=0, name='Paintbrush', type='TOOL')
    models.Product.new(price=0, name='Blood Extraction Syringe', type='TOOL')
    models.Product.new(price=0, name='GPS', type='TOOL')
    models.Product.new(price=0, name='Compass', type='TOOL')
    models.Product.new(price=0, name='Radio', type='TOOL')
    models.Product.new(price=0, name='Spyglass', type='TOOL')
    models.Product.new(price=0, name='Metal Sickle', type='TOOL')
    models.Product.new(price=0, name='Camera', type='TOOL')
    models.Product.new(price=0, name='Chainsaw', type='TOOL')
    models.Product.new(price=0, name='Electronic Binoculars', type='TOOL')
    models.Product.new(price=0, name='Empty Cryopod', type='TOOL')
    models.Product.new(price=0, name='Fish Net', type='TOOL')
    models.Product.new(price=0, name='Fishing Rod', type='TOOL')
    models.Product.new(price=0, name='Magnifying Glass', type='TOOL')
    models.Product.new(price=0, name='Mining Drill', type='TOOL')
    models.Product.new(price=0, name='Pliers', type='TOOL')
    models.Product.new(price=0, name='Scissors', type='TOOL')
    models.Product.new(price=0, name='Taxidermy Tool', type='TOOL')
    models.Product.new(price=0, name='Tier 1 Lootcrate', type='TOOL')
    models.Product.new(price=0, name='Tier 2 Lootcrate', type='TOOL')
    models.Product.new(price=0, name='Tier 3 Lootcrate', type='TOOL')
    models.Product.new(price=0, name='Whip', type='TOOL')

    # Create Trophy
    models.Product.new(price=0, name='Alpha Deathworm Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Rex Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Wyvern Trophy', type='TROPHY')
    models.Product.new(price=0, name='Broodmother Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Broodmother Trophy', type='TROPHY')
    models.Product.new(price=0, name='Beta Broodmother Trophy', type='TROPHY')
    models.Product.new(price=0, name='Gamma Broodmother Trophy', type='TROPHY')
    models.Product.new(price=0, name='Megapithecus Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Megapithecus Trophy', type='TROPHY')
    models.Product.new(price=0, name='Beta Megapithecus Trophy', type='TROPHY')
    models.Product.new(price=0, name='Gamma Megapithecus Trophy', type='TROPHY')
    models.Product.new(price=0, name='Dragon Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Dragon Trophy', type='TROPHY')
    models.Product.new(price=0, name='Beta Dragon Trophy', type='TROPHY')
    models.Product.new(price=0, name='Gamma Dragon Trophy', type='TROPHY')
    models.Product.new(price=0, name='Manticore Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Manticore Trophy', type='TROPHY')
    models.Product.new(price=0, name='Beta Manticore Trophy', type='TROPHY')
    models.Product.new(price=0, name='Gamma Manticore Trophy', type='TROPHY')
    models.Product.new(price=0, name='Rockwell Trophy (Alpha)', type='TROPHY')
    models.Product.new(price=0, name='Rockwell Trophy (Beta)', type='TROPHY')
    models.Product.new(price=0, name='Rockwell Trophy (Gamma)', type='TROPHY')
    models.Product.new(price=0, name='Desert Titan Trophy', type='TROPHY')
    models.Product.new(price=0, name='Forest Titan Trophy', type='TROPHY')
    models.Product.new(price=0, name='Ice Titan Trophy', type='TROPHY')
    models.Product.new(price=0, name='King Titan Trophy (Alpha)', type='TROPHY')
    models.Product.new(price=0, name='King Titan Trophy (Beta)', type='TROPHY')
    models.Product.new(price=0, name='King Titan Trophy (Gamma)', type='TROPHY')
    models.Product.new(price=0, name='Moeder Trophy', type='TROPHY')
    models.Product.new(price=0, name='Gamma Moeder Trophy', type='TROPHY')
    models.Product.new(price=0, name='Beta Moeder Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Moeder Trophy', type='TROPHY')
    models.Product.new(price=0, name='Master Controller Trophy', type='TROPHY')
    models.Product.new(price=0, name='Crystal Wyvern Queen Trophy', type='TROPHY')
    models.Product.new(price=0, name='Gamma Crystal Wyvern Queen Trophy', type='TROPHY')
    models.Product.new(price=0, name='Beta Crystal Wyvern Queen Trophy', type='TROPHY')
    models.Product.new(price=0, name='Alpha Crystal Wyvern Queen Trophy', type='TROPHY')
    models.Product.new(price=0, name="Survivor's Trophy", type='TROPHY')
    models.Product.new(price=0, name='Survival of the Fittest Trophy: 1st Place', type='TROPHY')
    models.Product.new(price=0, name='Survival of the Fittest Trophy: 2nd Place', type='TROPHY')
    models.Product.new(price=0, name='Survival of the Fittest Trophy: 3rd Place', type='TROPHY')
    models.Product.new(price=0, name='SotF: Unnatural Selection Trophy: 1st Place', type='TROPHY')
    models.Product.new(price=0, name='SotF: Unnatural Selection Trophy: 2nd Place', type='TROPHY')
    models.Product.new(price=0, name='SotF: Unnatural Selection Trophy: 3rd Place', type='TROPHY')

    # Create Weapon
    models.Product.new(price=0, name='Simple Pistol', type='WEAPON')
    models.Product.new(price=0, name='Assault Rifle', type='WEAPON')
    models.Product.new(price=0, name='Rocket Launcher', type='WEAPON')
    models.Product.new(price=0, name='Bow', type='WEAPON')
    models.Product.new(price=0, name='Grenade', type='WEAPON')
    models.Product.new(price=0, name='C4 Remote Detonator', type='WEAPON')
    models.Product.new(price=0, name='Improvised Explosive Device', type='WEAPON')
    models.Product.new(price=0, name='Spear', type='WEAPON')
    models.Product.new(price=0, name='Longneck Rifle', type='WEAPON')
    models.Product.new(price=0, name='Slingshot', type='WEAPON')
    models.Product.new(price=0, name='Pike', type='WEAPON')
    models.Product.new(price=0, name='Flare Gun', type='WEAPON')
    models.Product.new(price=0, name='Fabricated Pistol', type='WEAPON')
    models.Product.new(price=0, name='Shotgun', type='WEAPON')
    models.Product.new(price=0, name='Tripwire Narcotic Trap', type='WEAPON')
    models.Product.new(price=0, name='Tripwire Alarm Trap', type='WEAPON')
    models.Product.new(price=0, name='Pump-Action Shotgun', type='WEAPON')
    models.Product.new(price=0, name='Crossbow', type='WEAPON')
    models.Product.new(price=0, name='Transponder Tracker', type='WEAPON')
    models.Product.new(price=0, name='Compound Bow', type='WEAPON')
    models.Product.new(price=0, name='Bear Trap', type='WEAPON')
    models.Product.new(price=0, name='Large Bear Trap', type='WEAPON')
    models.Product.new(price=0, name='Spray Painter', type='WEAPON')
    models.Product.new(price=0, name='Wooden Club', type='WEAPON')
    models.Product.new(price=0, name='Poison Grenade', type='WEAPON')
    models.Product.new(price=0, name='Fabricated Sniper Rifle', type='WEAPON')
    models.Product.new(price=0, name='Electric Prod', type='WEAPON')
    models.Product.new(price=0, name='Handcuffs', type='WEAPON')
    models.Product.new(price=0, name='Admin Blink Rifle', type='WEAPON')
    models.Product.new(price=0, name='Bola', type='WEAPON')
    models.Product.new(price=0, name='Boomerang', type='WEAPON')
    models.Product.new(price=0, name='Chain Bola', type='WEAPON')
    models.Product.new(price=0, name='Charge Lantern', type='WEAPON')
    models.Product.new(price=0, name='Climbing Pick', type='WEAPON')
    models.Product.new(price=0, name='Cluster Grenade', type='WEAPON')
    models.Product.new(price=0, name='Cruise Missile', type='WEAPON')
    models.Product.new(price=0, name='Flamethrower', type='WEAPON')
    models.Product.new(price=0, name='Flaming Spear', type='WEAPON')
    models.Product.new(price=0, name='Glow Stick', type='WEAPON')
    models.Product.new(price=0, name='Harpoon Launcher', type='WEAPON')
    models.Product.new(price=0, name='Lance', type='WEAPON')
    models.Product.new(price=0, name='Lasso', type='WEAPON')
    models.Product.new(price=0, name='Oil Jar', type='WEAPON')
    models.Product.new(price=0, name='Plant Species Z Fruit', type='WEAPON')
    models.Product.new(price=0, name='Scout Remote', type='WEAPON')
    models.Product.new(price=0, name='Smoke Grenade', type='WEAPON')
    models.Product.new(price=0, name='Sword', type='WEAPON')
    models.Product.new(price=0, name='Tek Claws', type='WEAPON')
    models.Product.new(price=0, name='Tek Gravity Grenade', type='WEAPON')
    models.Product.new(price=0, name='Tek Grenade', type='WEAPON')
    models.Product.new(price=0, name='Tek Grenade Launcher', type='WEAPON')
    models.Product.new(price=0, name='Tek Railgun', type='WEAPON')
    models.Product.new(price=0, name='Tek Rifle', type='WEAPON')
    models.Product.new(price=0, name='Tek Sword', type='WEAPON')

    items = [item.to_json() for item in models.Attachment.all()]
    print(items)


def seed():
    items = [{'name': 'Simple Bullet', 'price': 0, 'discount': 0, 'id': 1, 'type': 'AMMUNITION'},
             {'name': 'Stone Arrow', 'price': 0, 'discount': 0, 'id': 2, 'type': 'AMMUNITION'},
             {'name': 'C4 Charge', 'price': 0, 'discount': 0, 'id': 3, 'type': 'AMMUNITION'},
             {'name': 'Tranq Arrow', 'price': 0, 'discount': 0, 'id': 4, 'type': 'AMMUNITION'},
             {'name': 'Simple Rifle Ammo', 'price': 0, 'discount': 0, 'id': 5, 'type': 'AMMUNITION'},
             {'name': 'Advanced Bullet', 'price': 0, 'discount': 0, 'id': 6, 'type': 'AMMUNITION'},
             {'name': 'Advanced Rifle Bullet', 'price': 0, 'discount': 0, 'id': 7, 'type': 'AMMUNITION'},
             {'name': 'Rocket Propelled Grenade', 'price': 0, 'discount': 0, 'id': 8, 'type': 'AMMUNITION'},
             {'name': 'Simple Shotgun Ammo', 'price': 0, 'discount': 0, 'id': 9, 'type': 'AMMUNITION'},
             {'name': 'Transponder Node', 'price': 0, 'discount': 0, 'id': 10, 'type': 'AMMUNITION'},
             {'name': 'Metal Arrow', 'price': 0, 'discount': 0, 'id': 11, 'type': 'AMMUNITION'},
             {'name': 'Advanced Sniper Bullet', 'price': 0, 'discount': 0, 'id': 12, 'type': 'AMMUNITION'},
             {'name': 'Boulder', 'price': 0, 'discount': 0, 'id': 13, 'type': 'AMMUNITION'},
             {'name': 'Cannon Ball', 'price': 0, 'discount': 0, 'id': 14, 'type': 'AMMUNITION'},
             {'name': 'Cannon Shell', 'price': 0, 'discount': 0, 'id': 15, 'type': 'AMMUNITION'},
             {'name': 'Explosive Arrow', 'price': 0, 'discount': 0, 'id': 16, 'type': 'AMMUNITION'},
             {'name': 'Flame Arrow', 'price': 0, 'discount': 0, 'id': 17, 'type': 'AMMUNITION'},
             {'name': 'Flamethrower Ammo', 'price': 0, 'discount': 0, 'id': 18, 'type': 'AMMUNITION'},
             {'name': 'Grappling Hook', 'price': 0, 'discount': 0, 'id': 19, 'type': 'AMMUNITION'},
             {'name': 'Jar of Pitch', 'price': 0, 'discount': 0, 'id': 20, 'type': 'AMMUNITION'},
             {'name': 'Net Projectile', 'price': 0, 'discount': 0, 'id': 21, 'type': 'AMMUNITION'},
             {'name': 'Pheromone Dart', 'price': 0, 'discount': 0, 'id': 22, 'type': 'AMMUNITION'},
             {'name': 'Rocket Homing Missile', 'price': 0, 'discount': 0, 'id': 23, 'type': 'AMMUNITION'},
             {'name': 'Rocket Pod', 'price': 0, 'discount': 0, 'id': 24, 'type': 'AMMUNITION'},
             {'name': 'Shocking Tranquilizer Dart', 'price': 0, 'discount': 0, 'id': 25, 'type': 'AMMUNITION'},
             {'name': 'Spear Bolt', 'price': 0, 'discount': 0, 'id': 26, 'type': 'AMMUNITION'},
             {'name': 'Tranquilizer Dart', 'price': 0, 'discount': 0, 'id': 27, 'type': 'AMMUNITION'},
             {'name': 'Tranq Spear Bolt', 'price': 0, 'discount': 0, 'id': 28, 'type': 'AMMUNITION'},
             {'name': 'Zip-Line Anchor', 'price': 0, 'discount': 0, 'id': 29, 'type': 'AMMUNITION'},
             {'name': 'Cloth Pants', 'price': 0, 'discount': 0, 'id': 30, 'type': 'ARMOUR'},
             {'name': 'Cloth Shirt', 'price': 0, 'discount': 0, 'id': 31, 'type': 'ARMOUR'},
             {'name': 'Cloth Hat', 'price': 0, 'discount': 0, 'id': 32, 'type': 'ARMOUR'},
             {'name': 'Cloth Boots', 'price': 0, 'discount': 0, 'id': 33, 'type': 'ARMOUR'},
             {'name': 'Cloth Gloves', 'price': 0, 'discount': 0, 'id': 34, 'type': 'ARMOUR'},
             {'name': 'Hide Pants', 'price': 0, 'discount': 0, 'id': 35, 'type': 'ARMOUR'},
             {'name': 'Hide Shirt', 'price': 0, 'discount': 0, 'id': 36, 'type': 'ARMOUR'},
             {'name': 'Hide Hat', 'price': 0, 'discount': 0, 'id': 37, 'type': 'ARMOUR'},
             {'name': 'Hide Boots', 'price': 0, 'discount': 0, 'id': 38, 'type': 'ARMOUR'},
             {'name': 'Hide Gloves', 'price': 0, 'discount': 0, 'id': 39, 'type': 'ARMOUR'},
             {'name': 'Chitin Leggings', 'price': 0, 'discount': 0, 'id': 40, 'type': 'ARMOUR'},
             {'name': 'Chitin Chestpiece', 'price': 0, 'discount': 0, 'id': 41, 'type': 'ARMOUR'},
             {'name': 'Chitin Helmet', 'price': 0, 'discount': 0, 'id': 42, 'type': 'ARMOUR'},
             {'name': 'Chitin Boots', 'price': 0, 'discount': 0, 'id': 43, 'type': 'ARMOUR'},
             {'name': 'Chitin Gauntlets', 'price': 0, 'discount': 0, 'id': 44, 'type': 'ARMOUR'},
             {'name': 'Parachute', 'price': 0, 'discount': 0, 'id': 45, 'type': 'ARMOUR'},
             {'name': 'Flak Leggings', 'price': 0, 'discount': 0, 'id': 46, 'type': 'ARMOUR'},
             {'name': 'Flak Chestpiece', 'price': 0, 'discount': 0, 'id': 47, 'type': 'ARMOUR'},
             {'name': 'Flak Helmet', 'price': 0, 'discount': 0, 'id': 48, 'type': 'ARMOUR'},
             {'name': 'Flak Boots', 'price': 0, 'discount': 0, 'id': 49, 'type': 'ARMOUR'},
             {'name': 'Flak Gauntlets', 'price': 0, 'discount': 0, 'id': 50, 'type': 'ARMOUR'},
             {'name': "Heavy Miner's Helmet", 'price': 0, 'discount': 0, 'id': 51, 'type': 'ARMOUR'},
             {'name': 'SCUBA Tank', 'price': 0, 'discount': 0, 'id': 52, 'type': 'ARMOUR'},
             {'name': 'SCUBA Mask', 'price': 0, 'discount': 0, 'id': 53, 'type': 'ARMOUR'},
             {'name': 'SCUBA Flippers', 'price': 0, 'discount': 0, 'id': 54, 'type': 'ARMOUR'},
             {'name': 'Fur Leggings', 'price': 0, 'discount': 0, 'id': 55, 'type': 'ARMOUR'},
             {'name': 'Fur Chestpiece', 'price': 0, 'discount': 0, 'id': 56, 'type': 'ARMOUR'},
             {'name': 'Fur Cap', 'price': 0, 'discount': 0, 'id': 57, 'type': 'ARMOUR'},
             {'name': 'Fur Boots', 'price': 0, 'discount': 0, 'id': 58, 'type': 'ARMOUR'},
             {'name': 'Fur Gauntlets', 'price': 0, 'discount': 0, 'id': 59, 'type': 'ARMOUR'},
             {'name': 'Riot Leggings', 'price': 0, 'discount': 0, 'id': 60, 'type': 'ARMOUR'},
             {'name': 'Riot Chestpiece', 'price': 0, 'discount': 0, 'id': 61, 'type': 'ARMOUR'},
             {'name': 'Riot Gauntlets', 'price': 0, 'discount': 0, 'id': 62, 'type': 'ARMOUR'},
             {'name': 'Riot Boots', 'price': 0, 'discount': 0, 'id': 63, 'type': 'ARMOUR'},
             {'name': 'Riot Helmet', 'price': 0, 'discount': 0, 'id': 64, 'type': 'ARMOUR'},
             {'name': 'Tek Shoulder Cannon', 'price': 0, 'discount': 0, 'id': 65, 'type': 'ARMOUR'},
             {'name': 'Tek Boots', 'price': 0, 'discount': 0, 'id': 66, 'type': 'ARMOUR'},
             {'name': 'Tek Chestpiece', 'price': 0, 'discount': 0, 'id': 67, 'type': 'ARMOUR'},
             {'name': 'Tek Gauntlets', 'price': 0, 'discount': 0, 'id': 68, 'type': 'ARMOUR'},
             {'name': 'Tek Helmet', 'price': 0, 'discount': 0, 'id': 69, 'type': 'ARMOUR'},
             {'name': 'Tek Leggings', 'price': 0, 'discount': 0, 'id': 70, 'type': 'ARMOUR'},
             {'name': 'SCUBA Leggings', 'price': 0, 'discount': 0, 'id': 71, 'type': 'ARMOUR'},
             {'name': 'Wooden Shield', 'price': 0, 'discount': 0, 'id': 72, 'type': 'ARMOUR'},
             {'name': 'Metal Shield', 'price': 0, 'discount': 0, 'id': 73, 'type': 'ARMOUR'},
             {'name': 'Riot Shield', 'price': 0, 'discount': 0, 'id': 74, 'type': 'ARMOUR'},
             {'name': 'Tek Shield', 'price': 0, 'discount': 0, 'id': 75, 'type': 'ARMOUR'},
             {'name': 'Ghillie Boots', 'price': 0, 'discount': 0, 'id': 76, 'type': 'ARMOUR'},
             {'name': 'Ghillie Chestpiece', 'price': 0, 'discount': 0, 'id': 77, 'type': 'ARMOUR'},
             {'name': 'Ghillie Gauntlets', 'price': 0, 'discount': 0, 'id': 78, 'type': 'ARMOUR'},
             {'name': 'Ghillie Leggings', 'price': 0, 'discount': 0, 'id': 79, 'type': 'ARMOUR'},
             {'name': 'Ghillie Mask', 'price': 0, 'discount': 0, 'id': 80, 'type': 'ARMOUR'},
             {'name': 'Gas Mask', 'price': 0, 'discount': 0, 'id': 81, 'type': 'ARMOUR'},
             {'name': 'Desert Cloth Boots', 'price': 0, 'discount': 0, 'id': 82, 'type': 'ARMOUR'},
             {'name': 'Desert Cloth Gloves', 'price': 0, 'discount': 0, 'id': 83, 'type': 'ARMOUR'},
             {'name': 'Desert Goggles and Hat', 'price': 0, 'discount': 0, 'id': 84, 'type': 'ARMOUR'},
             {'name': 'Desert Cloth Pants', 'price': 0, 'discount': 0, 'id': 85, 'type': 'ARMOUR'},
             {'name': 'Desert Cloth Shirt', 'price': 0, 'discount': 0, 'id': 86, 'type': 'ARMOUR'},
             {'name': 'Night Vision Goggles', 'price': 0, 'discount': 0, 'id': 87, 'type': 'ARMOUR'},
             {'name': 'Hazard Suit Boots', 'price': 0, 'discount': 0, 'id': 88, 'type': 'ARMOUR'},
             {'name': 'Hazard Suit Gloves', 'price': 0, 'discount': 0, 'id': 89, 'type': 'ARMOUR'},
             {'name': 'Hazard Suit Hat', 'price': 0, 'discount': 0, 'id': 90, 'type': 'ARMOUR'},
             {'name': 'Hazard Suit Pants', 'price': 0, 'discount': 0, 'id': 91, 'type': 'ARMOUR'},
             {'name': 'Hazard Suit Shirt', 'price': 0, 'discount': 0, 'id': 92, 'type': 'ARMOUR'},
             {'name': 'M.D.S.M.', 'price': 0, 'discount': 0, 'id': 93, 'type': 'ARMOUR'},
             {'name': 'M.O.M.I.', 'price': 0, 'discount': 0, 'id': 94, 'type': 'ARMOUR'},
             {'name': 'M.R.L.M.', 'price': 0, 'discount': 0, 'id': 95, 'type': 'ARMOUR'},
             {'name': 'M.S.C.M.', 'price': 0, 'discount': 0, 'id': 96, 'type': 'ARMOUR'},
             {'name': 'Specimen Implant', 'price': 0, 'discount': 0, 'id': 97, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Hunter', 'price': 0, 'discount': 0, 'id': 98, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Pack', 'price': 0, 'discount': 0, 'id': 99, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Massive', 'price': 0, 'discount': 0, 'id': 100, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Devious', 'price': 0, 'discount': 0, 'id': 101, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Clever', 'price': 0, 'discount': 0, 'id': 102, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Skylord', 'price': 0, 'discount': 0, 'id': 103, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Devourer', 'price': 0, 'discount': 0, 'id': 104, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Immune', 'price': 0, 'discount': 0, 'id': 105, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Strong', 'price': 0, 'discount': 0, 'id': 106, 'type': 'ARTIFACT'},
             {'name': 'Argentavis Talon', 'price': 0, 'discount': 0, 'id': 107, 'type': 'ARTIFACT'},
             {'name': 'Megalodon Tooth', 'price': 0, 'discount': 0, 'id': 108, 'type': 'ARTIFACT'},
             {'name': 'Tyrannosaurus Arm', 'price': 0, 'discount': 0, 'id': 109, 'type': 'ARTIFACT'},
             {'name': 'Sauropod Vertebra', 'price': 0, 'discount': 0, 'id': 110, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Brute', 'price': 0, 'discount': 0, 'id': 111, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Cunning', 'price': 0, 'discount': 0, 'id': 112, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Lost', 'price': 0, 'discount': 0, 'id': 113, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Gatekeeper ', 'price': 0, 'discount': 0, 'id': 114, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Crag ', 'price': 0, 'discount': 0, 'id': 115, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Destroyer ', 'price': 0, 'discount': 0, 'id': 116, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Depths ', 'price': 0, 'discount': 0, 'id': 117, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Shadows ', 'price': 0, 'discount': 0, 'id': 118, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Stalker ', 'price': 0, 'discount': 0, 'id': 119, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Chaos', 'price': 0, 'discount': 0, 'id': 120, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Growth', 'price': 0, 'discount': 0, 'id': 121, 'type': 'ARTIFACT'},
             {'name': 'Artifact of the Void', 'price': 0, 'discount': 0, 'id': 122, 'type': 'ARTIFACT'},
             {'name': 'Allosaurus Brain', 'price': 0, 'discount': 0, 'id': 123, 'type': 'ARTIFACT'},
             {'name': 'Alpha Basilisk Fang', 'price': 0, 'discount': 0, 'id': 124, 'type': 'ARTIFACT'},
             {'name': 'Alpha Carnotaurus Arm', 'price': 0, 'discount': 0, 'id': 125, 'type': 'ARTIFACT'},
             {'name': 'Alpha Crystal Talon', 'price': 0, 'discount': 0, 'id': 126, 'type': 'ARTIFACT'},
             {'name': 'Alpha Karkinos Claw', 'price': 0, 'discount': 0, 'id': 127, 'type': 'ARTIFACT'},
             {'name': 'Alpha Leedsichthys Blubber', 'price': 0, 'discount': 0, 'id': 128, 'type': 'ARTIFACT'},
             {'name': 'Alpha Megalodon Fin', 'price': 0, 'discount': 0, 'id': 129, 'type': 'ARTIFACT'},
             {'name': 'Alpha Mosasaur Tooth', 'price': 0, 'discount': 0, 'id': 130, 'type': 'ARTIFACT'},
             {'name': 'Alpha Raptor Claw', 'price': 0, 'discount': 0, 'id': 131, 'type': 'ARTIFACT'},
             {'name': 'Alpha Reaper King Barb', 'price': 0, 'discount': 0, 'id': 132, 'type': 'ARTIFACT'},
             {'name': 'Alpha Tusoteuthis Eye', 'price': 0, 'discount': 0, 'id': 133, 'type': 'ARTIFACT'},
             {'name': 'Alpha Tyrannosaur Tooth', 'price': 0, 'discount': 0, 'id': 134, 'type': 'ARTIFACT'},
             {'name': 'Alpha X-Triceratops Skull', 'price': 0, 'discount': 0, 'id': 135, 'type': 'ARTIFACT'},
             {'name': 'Basilisk Scale', 'price': 0, 'discount': 0, 'id': 136, 'type': 'ARTIFACT'},
             {'name': 'Basilosaurus Blubber', 'price': 0, 'discount': 0, 'id': 137, 'type': 'ARTIFACT'},
             {'name': 'Corrupt Heart', 'price': 0, 'discount': 0, 'id': 138, 'type': 'ARTIFACT'},
             {'name': 'Crystal Talon', 'price': 0, 'discount': 0, 'id': 139, 'type': 'ARTIFACT'},
             {'name': 'Fire Talon', 'price': 0, 'discount': 0, 'id': 140, 'type': 'ARTIFACT'},
             {'name': 'Gasbags bladder', 'price': 0, 'discount': 0, 'id': 141, 'type': 'ARTIFACT'},
             {'name': 'Giganotosaurus Heart', 'price': 0, 'discount': 0, 'id': 142, 'type': 'ARTIFACT'},
             {'name': 'Golden Striped Megalodon Tooth', 'price': 0, 'discount': 0, 'id': 143, 'type': 'ARTIFACT'},
             {'name': 'Lightning Talon', 'price': 0, 'discount': 0, 'id': 144, 'type': 'ARTIFACT'},
             {'name': 'Megalania Toxin', 'price': 0, 'discount': 0, 'id': 145, 'type': 'ARTIFACT'},
             {'name': 'Poison Talon', 'price': 0, 'discount': 0, 'id': 146, 'type': 'ARTIFACT'},
             {'name': 'Reaper King Pheromone Gland', 'price': 0, 'discount': 0, 'id': 147, 'type': 'ARTIFACT'},
             {'name': 'Reaper Pheromone Gland', 'price': 0, 'discount': 0, 'id': 148, 'type': 'ARTIFACT'},
             {'name': 'Rock Drake Feather', 'price': 0, 'discount': 0, 'id': 149, 'type': 'ARTIFACT'},
             {'name': 'Sarcosuchus Skin', 'price': 0, 'discount': 0, 'id': 150, 'type': 'ARTIFACT'},
             {'name': 'Spinosaurus Sail', 'price': 0, 'discount': 0, 'id': 151, 'type': 'ARTIFACT'},
             {'name': 'Therizino Claws', 'price': 0, 'discount': 0, 'id': 152, 'type': 'ARTIFACT'},
             {'name': 'Thylacoleo Hook-Claw', 'price': 0, 'discount': 0, 'id': 153, 'type': 'ARTIFACT'},
             {'name': 'Titanoboa Venom', 'price': 0, 'discount': 0, 'id': 154, 'type': 'ARTIFACT'},
             {'name': 'Tusoteuthis Tentacle', 'price': 0, 'discount': 0, 'id': 155, 'type': 'ARTIFACT'},
             {'name': 'Yutyrannus Lungs', 'price': 0, 'discount': 0, 'id': 156, 'type': 'ARTIFACT'},
             {'name': 'Mysterious Snow Globe', 'price': 0, 'discount': 0, 'id': 157, 'type': 'ARTIFACT'},
             {'name': 'Revealed Snow Globe', 'price': 0, 'discount': 0, 'id': 158, 'type': 'ARTIFACT'},
             {'name': 'Scope Attachment', 'price': 0, 'discount': 0, 'id': 159, 'type': 'ATTACHMENT'},
             {'name': 'Flashlight Attachment', 'price': 0, 'discount': 0, 'id': 160, 'type': 'ATTACHMENT'},
             {'name': 'Silencer Attachment', 'price': 0, 'discount': 0, 'id': 161, 'type': 'ATTACHMENT'},
             {'name': 'Holo-Scope Attachment', 'price': 0, 'discount': 0, 'id': 162, 'type': 'ATTACHMENT'},
             {'name': 'Laser Attachment', 'price': 0, 'discount': 0, 'id': 163, 'type': 'ATTACHMENT'},
             {'name': 'Rex Saddle', 'price': 0, 'discount': 0, 'id': 164, 'type': 'SADDLE'},
             {'name': 'Parasaur Saddle', 'price': 0, 'discount': 0, 'id': 165, 'type': 'SADDLE'},
             {'name': 'Raptor Saddle', 'price': 0, 'discount': 0, 'id': 166, 'type': 'SADDLE'},
             {'name': 'Stego Saddle', 'price': 0, 'discount': 0, 'id': 167, 'type': 'SADDLE'},
             {'name': 'Trike Saddle', 'price': 0, 'discount': 0, 'id': 168, 'type': 'SADDLE'},
             {'name': 'Pulmonoscorpius Saddle', 'price': 0, 'discount': 0, 'id': 169, 'type': 'SADDLE'},
             {'name': 'Pteranodon Saddle', 'price': 0, 'discount': 0, 'id': 170, 'type': 'SADDLE'},
             {'name': 'Bronto Saddle', 'price': 0, 'discount': 0, 'id': 171, 'type': 'SADDLE'},
             {'name': 'Carbonemys Saddle', 'price': 0, 'discount': 0, 'id': 172, 'type': 'SADDLE'},
             {'name': 'Sarco Saddle', 'price': 0, 'discount': 0, 'id': 173, 'type': 'SADDLE'},
             {'name': 'Ankylo Saddle', 'price': 0, 'discount': 0, 'id': 174, 'type': 'SADDLE'},
             {'name': 'Mammoth Saddle', 'price': 0, 'discount': 0, 'id': 175, 'type': 'SADDLE'},
             {'name': 'Megalodon Saddle', 'price': 0, 'discount': 0, 'id': 176, 'type': 'SADDLE'},
             {'name': 'Sabertooth Saddle', 'price': 0, 'discount': 0, 'id': 177, 'type': 'SADDLE'},
             {'name': 'Carno Saddle', 'price': 0, 'discount': 0, 'id': 178, 'type': 'SADDLE'},
             {'name': 'Argentavis Saddle', 'price': 0, 'discount': 0, 'id': 179, 'type': 'SADDLE'},
             {'name': 'Phiomia Saddle', 'price': 0, 'discount': 0, 'id': 180, 'type': 'SADDLE'},
             {'name': 'Spino Saddle', 'price': 0, 'discount': 0, 'id': 181, 'type': 'SADDLE'},
             {'name': 'Plesiosaur Saddle', 'price': 0, 'discount': 0, 'id': 182, 'type': 'SADDLE'},
             {'name': 'Ichthyosaurus Saddle', 'price': 0, 'discount': 0, 'id': 183, 'type': 'SADDLE'},
             {'name': 'Doedicurus Saddle', 'price': 0, 'discount': 0, 'id': 184, 'type': 'SADDLE'},
             {'name': 'Bronto Platform Saddle', 'price': 0, 'discount': 0, 'id': 185, 'type': 'SADDLE'},
             {'name': 'Pachy Saddle', 'price': 0, 'discount': 0, 'id': 186, 'type': 'SADDLE'},
             {'name': 'Paracer Saddle', 'price': 0, 'discount': 0, 'id': 187, 'type': 'SADDLE'},
             {'name': 'Paracer Platform Saddle', 'price': 0, 'discount': 0, 'id': 188, 'type': 'SADDLE'},
             {'name': 'Beelzebufo Saddle', 'price': 0, 'discount': 0, 'id': 189, 'type': 'SADDLE'},
             {'name': 'Megaloceros Saddle', 'price': 0, 'discount': 0, 'id': 190, 'type': 'SADDLE'},
             {'name': 'Allosaurus Saddle', 'price': 0, 'discount': 0, 'id': 191, 'type': 'SADDLE'},
             {'name': 'Araneo Saddle', 'price': 0, 'discount': 0, 'id': 192, 'type': 'SADDLE'},
             {'name': 'Arthropluera Saddle', 'price': 0, 'discount': 0, 'id': 193, 'type': 'SADDLE'},
             {'name': 'Baryonyx Saddle', 'price': 0, 'discount': 0, 'id': 194, 'type': 'SADDLE'},
             {'name': 'Basilisk Saddle', 'price': 0, 'discount': 0, 'id': 195, 'type': 'SADDLE'},
             {'name': 'Basilosaurus Saddle', 'price': 0, 'discount': 0, 'id': 196, 'type': 'SADDLE'},
             {'name': 'Castoroides Saddle', 'price': 0, 'discount': 0, 'id': 197, 'type': 'SADDLE'},
             {'name': 'Chalicotherium Saddle', 'price': 0, 'discount': 0, 'id': 198, 'type': 'SADDLE'},
             {'name': 'Daeodon Saddle', 'price': 0, 'discount': 0, 'id': 199, 'type': 'SADDLE'},
             {'name': 'Deinonychus Saddle', 'price': 0, 'discount': 0, 'id': 200, 'type': 'SADDLE'},
             {'name': 'Diplodocus Saddle', 'price': 0, 'discount': 0, 'id': 201, 'type': 'SADDLE'},
             {'name': 'Direbear Saddle', 'price': 0, 'discount': 0, 'id': 202, 'type': 'SADDLE'},
             {'name': 'Dunkleosteus Saddle', 'price': 0, 'discount': 0, 'id': 203, 'type': 'SADDLE'},
             {'name': 'Equus Saddle', 'price': 0, 'discount': 0, 'id': 204, 'type': 'SADDLE'},
             {'name': 'Gacha Saddle', 'price': 0, 'discount': 0, 'id': 205, 'type': 'SADDLE'},
             {'name': 'Gallimimus Saddle', 'price': 0, 'discount': 0, 'id': 206, 'type': 'SADDLE'},
             {'name': 'Gasbags Saddle', 'price': 0, 'discount': 0, 'id': 207, 'type': 'SADDLE'},
             {'name': 'Giganotosaurus Saddle', 'price': 0, 'discount': 0, 'id': 208, 'type': 'SADDLE'},
             {'name': 'Hyaenodon Meatpack', 'price': 0, 'discount': 0, 'id': 209, 'type': 'SADDLE'},
             {'name': 'Iguanodon Saddle', 'price': 0, 'discount': 0, 'id': 210, 'type': 'SADDLE'},
             {'name': 'Kaprosuchus Saddle', 'price': 0, 'discount': 0, 'id': 211, 'type': 'SADDLE'},
             {'name': 'Karkinos Saddle', 'price': 0, 'discount': 0, 'id': 212, 'type': 'SADDLE'},
             {'name': 'Lymantria Saddle', 'price': 0, 'discount': 0, 'id': 213, 'type': 'SADDLE'},
             {'name': 'Magmasaur Saddle', 'price': 0, 'discount': 0, 'id': 214, 'type': 'SADDLE'},
             {'name': 'Managarmr Saddle', 'price': 0, 'discount': 0, 'id': 215, 'type': 'SADDLE'},
             {'name': 'Manta Saddle', 'price': 0, 'discount': 0, 'id': 216, 'type': 'SADDLE'},
             {'name': 'Mantis Saddle', 'price': 0, 'discount': 0, 'id': 217, 'type': 'SADDLE'},
             {'name': 'Megalosaurus Saddle', 'price': 0, 'discount': 0, 'id': 218, 'type': 'SADDLE'},
             {'name': 'Megalania Saddle', 'price': 0, 'discount': 0, 'id': 219, 'type': 'SADDLE'},
             {'name': 'Megatherium Saddle', 'price': 0, 'discount': 0, 'id': 220, 'type': 'SADDLE'},
             {'name': 'Morellatops Saddle', 'price': 0, 'discount': 0, 'id': 221, 'type': 'SADDLE'},
             {'name': 'Mosasaur Saddle', 'price': 0, 'discount': 0, 'id': 222, 'type': 'SADDLE'},
             {'name': 'Pachyrhinosaurus Saddle', 'price': 0, 'discount': 0, 'id': 223, 'type': 'SADDLE'},
             {'name': 'Pelagornis Saddle', 'price': 0, 'discount': 0, 'id': 224, 'type': 'SADDLE'},
             {'name': 'Procoptodon Saddle', 'price': 0, 'discount': 0, 'id': 225, 'type': 'SADDLE'},
             {'name': 'Quetz Saddle', 'price': 0, 'discount': 0, 'id': 226, 'type': 'SADDLE'},
             {'name': 'Ravager Saddle', 'price': 0, 'discount': 0, 'id': 227, 'type': 'SADDLE'},
             {'name': 'Rock Drake Saddle', 'price': 0, 'discount': 0, 'id': 228, 'type': 'SADDLE'},
             {'name': 'Rock Golem Saddle', 'price': 0, 'discount': 0, 'id': 229, 'type': 'SADDLE'},
             {'name': 'Roll Rat Saddle', 'price': 0, 'discount': 0, 'id': 230, 'type': 'SADDLE'},
             {'name': 'Snow Owl Saddle', 'price': 0, 'discount': 0, 'id': 231, 'type': 'SADDLE'},
             {'name': 'Tapejara Saddle', 'price': 0, 'discount': 0, 'id': 232, 'type': 'SADDLE'},
             {'name': 'Terror Bird Saddle', 'price': 0, 'discount': 0, 'id': 233, 'type': 'SADDLE'},
             {'name': 'Therizinosaurus Saddle', 'price': 0, 'discount': 0, 'id': 234, 'type': 'SADDLE'},
             {'name': 'Thorny Dragon Saddle', 'price': 0, 'discount': 0, 'id': 235, 'type': 'SADDLE'},
             {'name': 'Thylacoleo Saddle', 'price': 0, 'discount': 0, 'id': 236, 'type': 'SADDLE'},
             {'name': 'Tropeognathus Saddle', 'price': 0, 'discount': 0, 'id': 237, 'type': 'SADDLE'},
             {'name': 'Tusoteuthis Saddle', 'price': 0, 'discount': 0, 'id': 238, 'type': 'SADDLE'},
             {'name': 'Velonasaur Saddle', 'price': 0, 'discount': 0, 'id': 239, 'type': 'SADDLE'},
             {'name': 'Woolly Rhino Saddle', 'price': 0, 'discount': 0, 'id': 240, 'type': 'SADDLE'},
             {'name': 'Yutyrannus Saddle', 'price': 0, 'discount': 0, 'id': 241, 'type': 'SADDLE'},
             {'name': 'Desert Titan Saddle', 'price': 0, 'discount': 0, 'id': 242, 'type': 'SADDLE'},
             {'name': 'Forest Titan Saddle', 'price': 0, 'discount': 0, 'id': 243, 'type': 'SADDLE'},
             {'name': 'Ice Titan Saddle', 'price': 0, 'discount': 0, 'id': 244, 'type': 'SADDLE'},
             {'name': 'Titanosaur Platform Saddle', 'price': 0, 'discount': 0, 'id': 245, 'type': 'SADDLE'},
             {'name': 'Mosasaur Platform Saddle', 'price': 0, 'discount': 0, 'id': 246, 'type': 'SADDLE'},
             {'name': 'Megachelon Platform Saddle', 'price': 0, 'discount': 0, 'id': 247, 'type': 'SADDLE'},
             {'name': 'Quetz Platform Saddle', 'price': 0, 'discount': 0, 'id': 248, 'type': 'SADDLE'},
             {'name': 'Plesiosaur Platform Saddle', 'price': 0, 'discount': 0, 'id': 249, 'type': 'SADDLE'},
             {'name': 'Rex Tek Saddle', 'price': 0, 'discount': 0, 'id': 250, 'type': 'SADDLE'},
             {'name': 'Astrocetus Tek Saddle', 'price': 0, 'discount': 0, 'id': 251, 'type': 'SADDLE'},
             {'name': 'Rock Drake Tek Saddle', 'price': 0, 'discount': 0, 'id': 252, 'type': 'SADDLE'},
             {'name': 'Megalodon Tek Saddle', 'price': 0, 'discount': 0, 'id': 253, 'type': 'SADDLE'},
             {'name': 'Mosasaur Tek Saddle', 'price': 0, 'discount': 0, 'id': 254, 'type': 'SADDLE'},
             {'name': 'Tapejara Tek Saddle', 'price': 0, 'discount': 0, 'id': 255, 'type': 'SADDLE'},
             {'name': 'Medical Brew', 'price': 0, 'discount': 0, 'id': 256, 'type': 'CONSUMABLE'},
             {'name': 'Mindwipe Tonic', 'price': 0, 'discount': 0, 'id': 257, 'type': 'CONSUMABLE'},
             {'name': 'Raw Meat', 'price': 0, 'discount': 0, 'id': 258, 'type': 'CONSUMABLE'},
             {'name': 'Spoiled Meat', 'price': 0, 'discount': 0, 'id': 259, 'type': 'CONSUMABLE'},
             {'name': 'Cooked Meat', 'price': 0, 'discount': 0, 'id': 260, 'type': 'CONSUMABLE'},
             {'name': 'Water Jar (Empty)', 'price': 0, 'discount': 0, 'id': 261, 'type': 'CONSUMABLE'},
             {'name': 'Water Jar (Full)', 'price': 0, 'discount': 0, 'id': 262, 'type': 'CONSUMABLE'},
             {'name': 'Waterskin (Empty)', 'price': 0, 'discount': 0, 'id': 263, 'type': 'CONSUMABLE'},
             {'name': 'Waterskin (Filled)', 'price': 0, 'discount': 0, 'id': 264, 'type': 'CONSUMABLE'},
             {'name': 'Bingleberry Soup', 'price': 0, 'discount': 0, 'id': 265, 'type': 'CONSUMABLE'},
             {'name': 'Energy Brew', 'price': 0, 'discount': 0, 'id': 266, 'type': 'CONSUMABLE'},
             {'name': 'Citronal', 'price': 0, 'discount': 0, 'id': 267, 'type': 'CONSUMABLE'},
             {'name': 'Amarberry', 'price': 0, 'discount': 0, 'id': 268, 'type': 'CONSUMABLE'},
             {'name': 'Azulberry', 'price': 0, 'discount': 0, 'id': 269, 'type': 'CONSUMABLE'},
             {'name': 'Tintoberry', 'price': 0, 'discount': 0, 'id': 270, 'type': 'CONSUMABLE'},
             {'name': 'Mejoberry', 'price': 0, 'discount': 0, 'id': 271, 'type': 'CONSUMABLE'},
             {'name': 'Narcoberry', 'price': 0, 'discount': 0, 'id': 272, 'type': 'CONSUMABLE'},
             {'name': 'Stimberry', 'price': 0, 'discount': 0, 'id': 273, 'type': 'CONSUMABLE'},
             {'name': 'Super Test Meat', 'price': 0, 'discount': 0, 'id': 274, 'type': 'CONSUMABLE'},
             {'name': 'Enduro Stew', 'price': 0, 'discount': 0, 'id': 275, 'type': 'CONSUMABLE'},
             {'name': 'Lazarus Chowder', 'price': 0, 'discount': 0, 'id': 276, 'type': 'CONSUMABLE'},
             {'name': 'Calien Soup', 'price': 0, 'discount': 0, 'id': 277, 'type': 'CONSUMABLE'},
             {'name': 'Fria Curry', 'price': 0, 'discount': 0, 'id': 278, 'type': 'CONSUMABLE'},
             {'name': 'Focal Chili', 'price': 0, 'discount': 0, 'id': 279, 'type': 'CONSUMABLE'},
             {'name': 'Savoroot', 'price': 0, 'discount': 0, 'id': 280, 'type': 'CONSUMABLE'},
             {'name': 'Longrass', 'price': 0, 'discount': 0, 'id': 281, 'type': 'CONSUMABLE'},
             {'name': 'Rockarrot', 'price': 0, 'discount': 0, 'id': 282, 'type': 'CONSUMABLE'},
             {'name': 'Raw Prime Meat', 'price': 0, 'discount': 0, 'id': 283, 'type': 'CONSUMABLE'},
             {'name': 'Cooked Prime Meat', 'price': 0, 'discount': 0, 'id': 284, 'type': 'CONSUMABLE'},
             {'name': 'Battle Tartare', 'price': 0, 'discount': 0, 'id': 285, 'type': 'CONSUMABLE'},
             {'name': 'Shadow Steak Saute', 'price': 0, 'discount': 0, 'id': 286, 'type': 'CONSUMABLE'},
             {'name': 'Cooked Meat Jerky', 'price': 0, 'discount': 0, 'id': 287, 'type': 'CONSUMABLE'},
             {'name': 'Prime Meat Jerky', 'price': 0, 'discount': 0, 'id': 288, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Ankylo Egg)', 'price': 0, 'discount': 0, 'id': 289, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Argentavis Egg)', 'price': 0, 'discount': 0, 'id': 290, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Titanboa Egg)', 'price': 0, 'discount': 0, 'id': 291, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Carno Egg)', 'price': 0, 'discount': 0, 'id': 292, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Dilo Egg)', 'price': 0, 'discount': 0, 'id': 293, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Dodo Egg)', 'price': 0, 'discount': 0, 'id': 294, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Parasaur Egg)', 'price': 0, 'discount': 0, 'id': 295, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Pteranodon Egg)', 'price': 0, 'discount': 0, 'id': 296, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Raptor Egg)', 'price': 0, 'discount': 0, 'id': 297, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Rex Egg)', 'price': 0, 'discount': 0, 'id': 298, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Sarco Egg)', 'price': 0, 'discount': 0, 'id': 299, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Bronto Egg)', 'price': 0, 'discount': 0, 'id': 300, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Pulmonoscorpius Egg)', 'price': 0, 'discount': 0, 'id': 301, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Araneo Egg)', 'price': 0, 'discount': 0, 'id': 302, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Spino Egg)', 'price': 0, 'discount': 0, 'id': 303, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Stego Egg)', 'price': 0, 'discount': 0, 'id': 304, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Trike Egg)', 'price': 0, 'discount': 0, 'id': 305, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Carbonemys Egg)', 'price': 0, 'discount': 0, 'id': 306, 'type': 'CONSUMABLE'},
             {'name': 'Canteen (Empty)', 'price': 0, 'discount': 0, 'id': 307, 'type': 'CONSUMABLE'},
             {'name': 'Canteen (Full)', 'price': 0, 'discount': 0, 'id': 308, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Pachy Egg)', 'price': 0, 'discount': 0, 'id': 309, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Dimorph Egg)', 'price': 0, 'discount': 0, 'id': 310, 'type': 'CONSUMABLE'},
             {'name': 'Broth of Enlightenment', 'price': 0, 'discount': 0, 'id': 311, 'type': 'CONSUMABLE'},
             {'name': 'Raw Fish Meat', 'price': 0, 'discount': 0, 'id': 312, 'type': 'CONSUMABLE'},
             {'name': 'Cooked Fish Meat', 'price': 0, 'discount': 0, 'id': 313, 'type': 'CONSUMABLE'},
             {'name': 'Raw Prime Fish Meat', 'price': 0, 'discount': 0, 'id': 314, 'type': 'CONSUMABLE'},
             {'name': 'Cooked Prime Fish Meat', 'price': 0, 'discount': 0, 'id': 315, 'type': 'CONSUMABLE'},
             {'name': 'Raw Mutton', 'price': 0, 'discount': 0, 'id': 316, 'type': 'CONSUMABLE'},
             {'name': 'Cooked Lamb Chop', 'price': 0, 'discount': 0, 'id': 317, 'type': 'CONSUMABLE'},
             {'name': 'Filled Fish Basket', 'price': 0, 'discount': 0, 'id': 318, 'type': 'CONSUMABLE'},
             {'name': 'Wyvern Milk', 'price': 0, 'discount': 0, 'id': 319, 'type': 'CONSUMABLE'},
             {'name': 'Cactus Sap', 'price': 0, 'discount': 0, 'id': 320, 'type': 'CONSUMABLE'},
             {'name': 'Aggeravic Mushroom', 'price': 0, 'discount': 0, 'id': 321, 'type': 'CONSUMABLE'},
             {'name': 'Aquatic Mushroom', 'price': 0, 'discount': 0, 'id': 322, 'type': 'CONSUMABLE'},
             {'name': 'Ascerbic Mushroom', 'price': 0, 'discount': 0, 'id': 323, 'type': 'CONSUMABLE'},
             {'name': 'Auric Mushroom', 'price': 0, 'discount': 0, 'id': 324, 'type': 'CONSUMABLE'},
             {'name': 'Mushroom Brew', 'price': 0, 'discount': 0, 'id': 325, 'type': 'CONSUMABLE'},
             {'name': 'Iced Water Jar (Empty)', 'price': 0, 'discount': 0, 'id': 326, 'type': 'CONSUMABLE'},
             {'name': 'Iced Water Jar (Full)', 'price': 0, 'discount': 0, 'id': 327, 'type': 'CONSUMABLE'},
             {'name': 'Iced Canteen (Empty)', 'price': 0, 'discount': 0, 'id': 328, 'type': 'CONSUMABLE'},
             {'name': 'Iced Canteen (Full)', 'price': 0, 'discount': 0, 'id': 329, 'type': 'CONSUMABLE'},
             {'name': 'Beer Liquid', 'price': 0, 'discount': 0, 'id': 330, 'type': 'CONSUMABLE'},
             {'name': 'Beer Jar', 'price': 0, 'discount': 0, 'id': 331, 'type': 'CONSUMABLE'},
             {'name': 'Beer Jar (alt)', 'price': 0, 'discount': 0, 'id': 332, 'type': 'CONSUMABLE'},
             {'name': 'Bio Toxin', 'price': 0, 'discount': 0, 'id': 333, 'type': 'CONSUMABLE'},
             {'name': 'Bug Repellant', 'price': 0, 'discount': 0, 'id': 334, 'type': 'CONSUMABLE'},
             {'name': 'Cactus Broth', 'price': 0, 'discount': 0, 'id': 335, 'type': 'CONSUMABLE'},
             {'name': 'Lesser Antidote', 'price': 0, 'discount': 0, 'id': 336, 'type': 'CONSUMABLE'},
             {'name': 'Soap', 'price': 0, 'discount': 0, 'id': 337, 'type': 'CONSUMABLE'},
             {'name': 'Sweet Vegetable Cake', 'price': 0, 'discount': 0, 'id': 338, 'type': 'CONSUMABLE'},
             {'name': 'Giant Bee Honey', 'price': 0, 'discount': 0, 'id': 339, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Allosaurus Egg)', 'price': 0, 'discount': 0, 'id': 340, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Archaeopteryx Egg)', 'price': 0, 'discount': 0, 'id': 341, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Baryonyx Egg)', 'price': 0, 'discount': 0, 'id': 342, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Camelsaurus Egg)', 'price': 0, 'discount': 0, 'id': 343, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Compy Egg)', 'price': 0, 'discount': 0, 'id': 344, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Dimetrodon Egg)', 'price': 0, 'discount': 0, 'id': 345, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Diplo Egg)', 'price': 0, 'discount': 0, 'id': 346, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Featherlight Egg)', 'price': 0, 'discount': 0, 'id': 347, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Gallimimus Egg)', 'price': 0, 'discount': 0, 'id': 348, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Glowtail Egg)', 'price': 0, 'discount': 0, 'id': 349, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Ichthyornis Egg)', 'price': 0, 'discount': 0, 'id': 350, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Iguanodon Egg)', 'price': 0, 'discount': 0, 'id': 351, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Kairuku Egg)', 'price': 0, 'discount': 0, 'id': 352, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Kaprosuchus Egg)', 'price': 0, 'discount': 0, 'id': 353, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Kentrosaurus Egg)', 'price': 0, 'discount': 0, 'id': 354, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Lystrosaurus Egg)', 'price': 0, 'discount': 0, 'id': 355, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Mantis Egg)', 'price': 0, 'discount': 0, 'id': 356, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Megalania Egg)', 'price': 0, 'discount': 0, 'id': 357, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Megalosaurus Egg)', 'price': 0, 'discount': 0, 'id': 358, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Microraptor Egg)', 'price': 0, 'discount': 0, 'id': 359, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Moschops Egg)', 'price': 0, 'discount': 0, 'id': 360, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Moth Egg)', 'price': 0, 'discount': 0, 'id': 361, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Oviraptor Egg)', 'price': 0, 'discount': 0, 'id': 362, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Pachyrhino Egg)', 'price': 0, 'discount': 0, 'id': 363, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Pegomastax Egg)', 'price': 0, 'discount': 0, 'id': 364, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Pelagornis Egg)', 'price': 0, 'discount': 0, 'id': 365, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Quetzal Egg)', 'price': 0, 'discount': 0, 'id': 366, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Rock Drake Egg)', 'price': 0, 'discount': 0, 'id': 367, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Tapejara Egg)', 'price': 0, 'discount': 0, 'id': 368, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Terror Bird Egg)', 'price': 0, 'discount': 0, 'id': 369, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Therizinosaurus Egg)', 'price': 0, 'discount': 0, 'id': 370, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Thorny Dragon Egg)', 'price': 0, 'discount': 0, 'id': 371, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Troodon Egg)', 'price': 0, 'discount': 0, 'id': 372, 'type': 'CONSUMABLE'},
             {'name': 'Kibble (Vulture Egg)', 'price': 0, 'discount': 0, 'id': 373, 'type': 'CONSUMABLE'},
             {'name': 'Basic Kibble', 'price': 0, 'discount': 0, 'id': 374, 'type': 'CONSUMABLE'},
             {'name': 'Simple Kibble', 'price': 0, 'discount': 0, 'id': 375, 'type': 'CONSUMABLE'},
             {'name': 'Regular Kibble', 'price': 0, 'discount': 0, 'id': 376, 'type': 'CONSUMABLE'},
             {'name': 'Superior Kibble', 'price': 0, 'discount': 0, 'id': 377, 'type': 'CONSUMABLE'},
             {'name': 'Exceptional Kibble', 'price': 0, 'discount': 0, 'id': 378, 'type': 'CONSUMABLE'},
             {'name': 'Extraordinary Kibble', 'price': 0, 'discount': 0, 'id': 379, 'type': 'CONSUMABLE'},
             {'name': 'Basic Augmented Kibble', 'price': 0, 'discount': 0, 'id': 380, 'type': 'CONSUMABLE'},
             {'name': 'Simple Augmented Kibble', 'price': 0, 'discount': 0, 'id': 381, 'type': 'CONSUMABLE'},
             {'name': 'Regular Augmented Kibble', 'price': 0, 'discount': 0, 'id': 382, 'type': 'CONSUMABLE'},
             {'name': 'Superior Augmented Kibble', 'price': 0, 'discount': 0, 'id': 383, 'type': 'CONSUMABLE'},
             {'name': 'Exceptional Augmented Kibble', 'price': 0, 'discount': 0, 'id': 384, 'type': 'CONSUMABLE'},
             {'name': 'Extraordinary Augmented Kibble', 'price': 0, 'discount': 0, 'id': 385, 'type': 'CONSUMABLE'},
             {'name': '"Evil" Emote', 'price': 0, 'discount': 0, 'id': 386, 'type': 'CONSUMABLE'},
             {'name': 'Gacha Crystal', 'price': 0, 'discount': 0, 'id': 387, 'type': 'CONSUMABLE'},
             {'name': 'Unassembled Enforcer', 'price': 0, 'discount': 0, 'id': 388, 'type': 'CONSUMABLE'},
             {'name': 'Unassembled Mek', 'price': 0, 'discount': 0, 'id': 389, 'type': 'CONSUMABLE'},
             {'name': 'Nameless Venom', 'price': 0, 'discount': 0, 'id': 390, 'type': 'CONSUMABLE'},
             {'name': 'Reaper Pheromone Gland', 'price': 0, 'discount': 0, 'id': 391, 'type': 'CONSUMABLE'},
             {'name': '"Turkey" Emote', 'price': 0, 'discount': 0, 'id': 392, 'type': 'CONSUMABLE'},
             {'name': 'Summon DodoRex', 'price': 0, 'discount': 0, 'id': 393, 'type': 'CONSUMABLE'},
             {'name': '"Snowball" Emote', 'price': 0, 'discount': 0, 'id': 394, 'type': 'CONSUMABLE'},
             {'name': 'Festive Dino Candy', 'price': 0, 'discount': 0, 'id': 395, 'type': 'CONSUMABLE'},
             {'name': "Box o' Chocolates", 'price': 0, 'discount': 0, 'id': 396, 'type': 'CONSUMABLE'},
             {'name': 'Valentines Dino Candy', 'price': 0, 'discount': 0, 'id': 397, 'type': 'CONSUMABLE'},
             {'name': '"Heart" Emote', 'price': 0, 'discount': 0, 'id': 398, 'type': 'CONSUMABLE'},
             {'name': 'Romantic Head Hair Style', 'price': 0, 'discount': 0, 'id': 399, 'type': 'CONSUMABLE'},
             {'name': 'Romantic Facial Hair Style', 'price': 0, 'discount': 0, 'id': 400, 'type': 'CONSUMABLE'},
             {'name': 'Festive Dino Candy (Easter)', 'price': 0, 'discount': 0, 'id': 401, 'type': 'CONSUMABLE'},
             {'name': '"Archer Flex" Emote', 'price': 0, 'discount': 0, 'id': 402, 'type': 'CONSUMABLE'},
             {'name': '"Bicep Smooch" Emote', 'price': 0, 'discount': 0, 'id': 403, 'type': 'CONSUMABLE'},
             {'name': 'Summer Swirl Taffy', 'price': 0, 'discount': 0, 'id': 404, 'type': 'CONSUMABLE'},
             {'name': '"Dance" Emote', 'price': 0, 'discount': 0, 'id': 405, 'type': 'CONSUMABLE'},
             {'name': 'Panic Emote', 'price': 0, 'discount': 0, 'id': 406, 'type': 'CONSUMABLE'},
             {'name': '"Zombie" Emote', 'price': 0, 'discount': 0, 'id': 407, 'type': 'CONSUMABLE'},
             {'name': 'Dino Candy Corn', 'price': 0, 'discount': 0, 'id': 408, 'type': 'CONSUMABLE'},
             {'name': 'Belly Rub Emote', 'price': 0, 'discount': 0, 'id': 409, 'type': 'CONSUMABLE'},
             {'name': 'Food Coma Emote', 'price': 0, 'discount': 0, 'id': 410, 'type': 'CONSUMABLE'},
             {'name': 'Hungry Emote', 'price': 0, 'discount': 0, 'id': 411, 'type': 'CONSUMABLE'},
             {'name': 'Thanksgiving Candy', 'price': 0, 'discount': 0, 'id': 412, 'type': 'CONSUMABLE'},
             {'name': 'Caroling Emote', 'price': 0, 'discount': 0, 'id': 413, 'type': 'CONSUMABLE'},
             {'name': 'Happy Clap Emote', 'price': 0, 'discount': 0, 'id': 414, 'type': 'CONSUMABLE'},
             {'name': 'Nutcracker Dance Emote', 'price': 0, 'discount': 0, 'id': 415, 'type': 'CONSUMABLE'},
             {'name': 'Flirty Emote', 'price': 0, 'discount': 0, 'id': 416, 'type': 'CONSUMABLE'},
             {'name': 'Bunny Hop Dance Emote', 'price': 0, 'discount': 0, 'id': 417, 'type': 'CONSUMABLE'},
             {'name': 'Air Drums Emote', 'price': 0, 'discount': 0, 'id': 418, 'type': 'CONSUMABLE'},
             {'name': 'Air Guitar Emote', 'price': 0, 'discount': 0, 'id': 419, 'type': 'CONSUMABLE'},
             {'name': 'Mosh Pit Emote', 'price': 0, 'discount': 0, 'id': 420, 'type': 'CONSUMABLE'},
             {'name': 'Knock Emote', 'price': 0, 'discount': 0, 'id': 421, 'type': 'CONSUMABLE'},
             {'name': 'Scare Emote', 'price': 0, 'discount': 0, 'id': 422, 'type': 'CONSUMABLE'},
             {'name': 'Aberrant Achatina', 'price': 0, 'discount': 0, 'id': 423, 'type': 'CREATURE'},
             {'name': 'Aberrant Anglerfish', 'price': 0, 'discount': 0, 'id': 424, 'type': 'CREATURE'},
             {'name': 'Aberrant Ankylosaurus', 'price': 0, 'discount': 0, 'id': 425, 'type': 'CREATURE'},
             {'name': 'Aberrant Araneo', 'price': 0, 'discount': 0, 'id': 426, 'type': 'CREATURE'},
             {'name': 'Aberrant Arthropluera', 'price': 0, 'discount': 0, 'id': 427, 'type': 'CREATURE'},
             {'name': 'Aberrant Baryonyx', 'price': 0, 'discount': 0, 'id': 428, 'type': 'CREATURE'},
             {'name': 'Aberrant Beelzebufo', 'price': 0, 'discount': 0, 'id': 429, 'type': 'CREATURE'},
             {'name': 'Aberrant Carbonemys', 'price': 0, 'discount': 0, 'id': 430, 'type': 'CREATURE'},
             {'name': 'Aberrant Carnotaurus', 'price': 0, 'discount': 0, 'id': 431, 'type': 'CREATURE'},
             {'name': 'Aberrant Cnidaria', 'price': 0, 'discount': 0, 'id': 432, 'type': 'CREATURE'},
             {'name': 'Aberrant Coelacanth', 'price': 0, 'discount': 0, 'id': 433, 'type': 'CREATURE'},
             {'name': 'Aberrant Dimetrodon', 'price': 0, 'discount': 0, 'id': 434, 'type': 'CREATURE'},
             {'name': 'Aberrant Dimorphodon', 'price': 0, 'discount': 0, 'id': 435, 'type': 'CREATURE'},
             {'name': 'Aberrant Diplocaulus', 'price': 0, 'discount': 0, 'id': 436, 'type': 'CREATURE'},
             {'name': 'Aberrant Diplodocus', 'price': 0, 'discount': 0, 'id': 437, 'type': 'CREATURE'},
             {'name': 'Aberrant Dire Bear', 'price': 0, 'discount': 0, 'id': 438, 'type': 'CREATURE'},
             {'name': 'Aberrant Dodo', 'price': 0, 'discount': 0, 'id': 439, 'type': 'CREATURE'},
             {'name': 'Aberrant Doedicurus', 'price': 0, 'discount': 0, 'id': 440, 'type': 'CREATURE'},
             {'name': 'Aberrant Dung Beetle', 'price': 0, 'discount': 0, 'id': 441, 'type': 'CREATURE'},
             {'name': 'Aberrant Electrophorus', 'price': 0, 'discount': 0, 'id': 442, 'type': 'CREATURE'},
             {'name': 'Aberrant Equus', 'price': 0, 'discount': 0, 'id': 443, 'type': 'CREATURE'},
             {'name': 'Aberrant Gigantopithecus', 'price': 0, 'discount': 0, 'id': 444, 'type': 'CREATURE'},
             {'name': 'Aberrant Iguanodon', 'price': 0, 'discount': 0, 'id': 445, 'type': 'CREATURE'},
             {'name': 'Aberrant Lystrosaurus', 'price': 0, 'discount': 0, 'id': 446, 'type': 'CREATURE'},
             {'name': 'Aberrant Manta', 'price': 0, 'discount': 0, 'id': 447, 'type': 'CREATURE'},
             {'name': 'Aberrant Megalania', 'price': 0, 'discount': 0, 'id': 448, 'type': 'CREATURE'},
             {'name': 'Aberrant Megalosaurus', 'price': 0, 'discount': 0, 'id': 449, 'type': 'CREATURE'},
             {'name': 'Aberrant Meganeura', 'price': 0, 'discount': 0, 'id': 450, 'type': 'CREATURE'},
             {'name': 'Aberrant Moschops', 'price': 0, 'discount': 0, 'id': 451, 'type': 'CREATURE'},
             {'name': 'Aberrant Otter', 'price': 0, 'discount': 0, 'id': 452, 'type': 'CREATURE'},
             {'name': 'Aberrant Ovis', 'price': 0, 'discount': 0, 'id': 453, 'type': 'CREATURE'},
             {'name': 'Aberrant Paraceratherium', 'price': 0, 'discount': 0, 'id': 454, 'type': 'CREATURE'},
             {'name': 'Aberrant Parasaur', 'price': 0, 'discount': 0, 'id': 455, 'type': 'CREATURE'},
             {'name': 'Aberrant Piranha', 'price': 0, 'discount': 0, 'id': 456, 'type': 'CREATURE'},
             {'name': 'Aberrant Pulmonoscorpius', 'price': 0, 'discount': 0, 'id': 457, 'type': 'CREATURE'},
             {'name': 'Aberrant Purlovia', 'price': 0, 'discount': 0, 'id': 458, 'type': 'CREATURE'},
             {'name': 'Aberrant Raptor', 'price': 0, 'discount': 0, 'id': 459, 'type': 'CREATURE'},
             {'name': 'Aberrant Sabertooth Salmon', 'price': 0, 'discount': 0, 'id': 460, 'type': 'CREATURE'},
             {'name': 'Aberrant Sarco', 'price': 0, 'discount': 0, 'id': 461, 'type': 'CREATURE'},
             {'name': 'Aberrant Spino', 'price': 0, 'discount': 0, 'id': 462, 'type': 'CREATURE'},
             {'name': 'Aberrant Stegosaurus', 'price': 0, 'discount': 0, 'id': 463, 'type': 'CREATURE'},
             {'name': 'Aberrant Titanoboa', 'price': 0, 'discount': 0, 'id': 464, 'type': 'CREATURE'},
             {'name': 'Aberrant Triceratops', 'price': 0, 'discount': 0, 'id': 465, 'type': 'CREATURE'},
             {'name': 'Aberrant Trilobite', 'price': 0, 'discount': 0, 'id': 466, 'type': 'CREATURE'},
             {'name': 'Alpha Basilisk', 'price': 0, 'discount': 0, 'id': 467, 'type': 'CREATURE'},
             {'name': 'Alpha Karkinos', 'price': 0, 'discount': 0, 'id': 468, 'type': 'CREATURE'},
             {'name': 'Alpha Surface Reaper King', 'price': 0, 'discount': 0, 'id': 469, 'type': 'CREATURE'},
             {'name': 'Basilisk', 'price': 0, 'discount': 0, 'id': 470, 'type': 'CREATURE'},
             {'name': 'Basilisk Ghost', 'price': 0, 'discount': 0, 'id': 471, 'type': 'CREATURE'},
             {'name': 'Bulbdog', 'price': 0, 'discount': 0, 'id': 472, 'type': 'CREATURE'},
             {'name': 'Bulbdog Ghost', 'price': 0, 'discount': 0, 'id': 473, 'type': 'CREATURE'},
             {'name': 'Featherlight', 'price': 0, 'discount': 0, 'id': 474, 'type': 'CREATURE'},
             {'name': 'Glowbug', 'price': 0, 'discount': 0, 'id': 475, 'type': 'CREATURE'},
             {'name': 'Glowtail', 'price': 0, 'discount': 0, 'id': 476, 'type': 'CREATURE'},
             {'name': 'Karkinos', 'price': 0, 'discount': 0, 'id': 477, 'type': 'CREATURE'},
             {'name': 'Lamprey', 'price': 0, 'discount': 0, 'id': 478, 'type': 'CREATURE'},
             {'name': 'Nameless', 'price': 0, 'discount': 0, 'id': 479, 'type': 'CREATURE'},
             {'name': 'Ravager', 'price': 0, 'discount': 0, 'id': 480, 'type': 'CREATURE'},
             {'name': 'Reaper King', 'price': 0, 'discount': 0, 'id': 481, 'type': 'CREATURE'},
             {'name': 'Reaper King (Tamed)', 'price': 0, 'discount': 0, 'id': 482, 'type': 'CREATURE'},
             {'name': 'Reaper Queen', 'price': 0, 'discount': 0, 'id': 483, 'type': 'CREATURE'},
             {'name': 'Rock Drake', 'price': 0, 'discount': 0, 'id': 484, 'type': 'CREATURE'},
             {'name': 'Rockwell', 'price': 0, 'discount': 0, 'id': 485, 'type': 'CREATURE'},
             {'name': 'Rockwell (Alpha)', 'price': 0, 'discount': 0, 'id': 486, 'type': 'CREATURE'},
             {'name': 'Rockwell (Beta)', 'price': 0, 'discount': 0, 'id': 487, 'type': 'CREATURE'},
             {'name': 'Rockwell (Gamma)', 'price': 0, 'discount': 0, 'id': 488, 'type': 'CREATURE'},
             {'name': 'Rockwell Tentacle', 'price': 0, 'discount': 0, 'id': 489, 'type': 'CREATURE'},
             {'name': 'Rockwell Tentacle (Alpha)', 'price': 0, 'discount': 0, 'id': 490, 'type': 'CREATURE'},
             {'name': 'Rockwell Tentacle (Beta)', 'price': 0, 'discount': 0, 'id': 491, 'type': 'CREATURE'},
             {'name': 'Rockwell Tentacle (Gamma)', 'price': 0, 'discount': 0, 'id': 492, 'type': 'CREATURE'},
             {'name': 'Roll Rat', 'price': 0, 'discount': 0, 'id': 493, 'type': 'CREATURE'},
             {'name': 'Seeker', 'price': 0, 'discount': 0, 'id': 494, 'type': 'CREATURE'},
             {'name': 'Shinehorn', 'price': 0, 'discount': 0, 'id': 495, 'type': 'CREATURE'},
             {'name': 'Surface Reaper King Ghost', 'price': 0, 'discount': 0, 'id': 496, 'type': 'CREATURE'},
             {'name': 'Alpha Blood Crystal Wyvern', 'price': 0, 'discount': 0, 'id': 497, 'type': 'CREATURE'},
             {'name': 'Blood Crystal Wyvern', 'price': 0, 'discount': 0, 'id': 498, 'type': 'CREATURE'},
             {'name': 'Crystal Wyvern Queen (Gamma)', 'price': 0, 'discount': 0, 'id': 499, 'type': 'CREATURE'},
             {'name': 'Crystal Wyvern Queen (Beta)', 'price': 0, 'discount': 0, 'id': 500, 'type': 'CREATURE'},
             {'name': 'Crystal Wyvern Queen (Alpha)', 'price': 0, 'discount': 0, 'id': 501, 'type': 'CREATURE'},
             {'name': 'Ember Crystal Wyvern', 'price': 0, 'discount': 0, 'id': 502, 'type': 'CREATURE'},
             {'name': 'Giant Worker Bee', 'price': 0, 'discount': 0, 'id': 503, 'type': 'CREATURE'},
             {'name': 'Tropeognathus', 'price': 0, 'discount': 0, 'id': 504, 'type': 'CREATURE'},
             {'name': 'Tropical Crystal Wyvern', 'price': 0, 'discount': 0, 'id': 505, 'type': 'CREATURE'},
             {'name': 'Alpha King Titan', 'price': 0, 'discount': 0, 'id': 506, 'type': 'CREATURE'},
             {'name': 'Beta King Titan', 'price': 0, 'discount': 0, 'id': 507, 'type': 'CREATURE'},
             {'name': 'Corrupted Arthropluera', 'price': 0, 'discount': 0, 'id': 508, 'type': 'CREATURE'},
             {'name': 'Corrupted Carnotaurus', 'price': 0, 'discount': 0, 'id': 509, 'type': 'CREATURE'},
             {'name': 'Corrupted Chalicotherium', 'price': 0, 'discount': 0, 'id': 510, 'type': 'CREATURE'},
             {'name': 'Corrupted Dilophosaur', 'price': 0, 'discount': 0, 'id': 511, 'type': 'CREATURE'},
             {'name': 'Corrupted Dimorphodon', 'price': 0, 'discount': 0, 'id': 512, 'type': 'CREATURE'},
             {'name': 'Corrupted Giganotosaurus', 'price': 0, 'discount': 0, 'id': 513, 'type': 'CREATURE'},
             {'name': 'Corrupted Paraceratherium', 'price': 0, 'discount': 0, 'id': 514, 'type': 'CREATURE'},
             {'name': 'Corrupted Pteranodon', 'price': 0, 'discount': 0, 'id': 515, 'type': 'CREATURE'},
             {'name': 'Corrupted Raptor', 'price': 0, 'discount': 0, 'id': 516, 'type': 'CREATURE'},
             {'name': 'Corrupted Reaper King', 'price': 0, 'discount': 0, 'id': 517, 'type': 'CREATURE'},
             {'name': 'Corrupted Rex', 'price': 0, 'discount': 0, 'id': 518, 'type': 'CREATURE'},
             {'name': 'Corrupted Rock Drake', 'price': 0, 'discount': 0, 'id': 519, 'type': 'CREATURE'},
             {'name': 'Corrupted Spino', 'price': 0, 'discount': 0, 'id': 520, 'type': 'CREATURE'},
             {'name': 'Corrupted Stegosaurus', 'price': 0, 'discount': 0, 'id': 521, 'type': 'CREATURE'},
             {'name': 'Corrupted Triceratops', 'price': 0, 'discount': 0, 'id': 522, 'type': 'CREATURE'},
             {'name': 'Corrupted Wyvern', 'price': 0, 'discount': 0, 'id': 523, 'type': 'CREATURE'},
             {'name': 'Defense Unit', 'price': 0, 'discount': 0, 'id': 524, 'type': 'CREATURE'},
             {'name': 'Desert Titan', 'price': 0, 'discount': 0, 'id': 525, 'type': 'CREATURE'},
             {'name': 'Desert Titan Flock', 'price': 0, 'discount': 0, 'id': 526, 'type': 'CREATURE'},
             {'name': 'Enforcer', 'price': 0, 'discount': 0, 'id': 527, 'type': 'CREATURE'},
             {'name': 'Enraged Corrupted Rex', 'price': 0, 'discount': 0, 'id': 528, 'type': 'CREATURE'},
             {'name': 'Enraged Triceratops', 'price': 0, 'discount': 0, 'id': 529, 'type': 'CREATURE'},
             {'name': 'Forest Titan', 'price': 0, 'discount': 0, 'id': 530, 'type': 'CREATURE'},
             {'name': 'Forest Wyvern', 'price': 0, 'discount': 0, 'id': 531, 'type': 'CREATURE'},
             {'name': 'Gacha', 'price': 0, 'discount': 0, 'id': 532, 'type': 'CREATURE'},
             {'name': 'GachaClaus', 'price': 0, 'discount': 0, 'id': 533, 'type': 'CREATURE'},
             {'name': 'Gamma King Titan', 'price': 0, 'discount': 0, 'id': 534, 'type': 'CREATURE'},
             {'name': 'Gasbags', 'price': 0, 'discount': 0, 'id': 535, 'type': 'CREATURE'},
             {'name': 'Ice Titan', 'price': 0, 'discount': 0, 'id': 536, 'type': 'CREATURE'},
             {'name': 'Managarmr', 'price': 0, 'discount': 0, 'id': 537, 'type': 'CREATURE'},
             {'name': 'Mega Mek', 'price': 0, 'discount': 0, 'id': 538, 'type': 'CREATURE'},
             {'name': 'Mek', 'price': 0, 'discount': 0, 'id': 539, 'type': 'CREATURE'},
             {'name': 'Scout', 'price': 0, 'discount': 0, 'id': 540, 'type': 'CREATURE'},
             {'name': 'Snow Owl', 'price': 0, 'discount': 0, 'id': 541, 'type': 'CREATURE'},
             {'name': 'Snow Owl Ghost', 'price': 0, 'discount': 0, 'id': 542, 'type': 'CREATURE'},
             {'name': 'Velonasaur', 'price': 0, 'discount': 0, 'id': 543, 'type': 'CREATURE'},
             {'name': 'Alpha Corrupted Master Controller', 'price': 0, 'discount': 0, 'id': 544, 'type': 'CREATURE'},
             {'name': 'Alpha Moeder, Master of the Ocean', 'price': 0, 'discount': 0, 'id': 545, 'type': 'CREATURE'},
             {'name': 'Alpha X-Triceratops', 'price': 0, 'discount': 0, 'id': 546, 'type': 'CREATURE'},
             {'name': 'Astrocetus', 'price': 0, 'discount': 0, 'id': 547, 'type': 'CREATURE'},
             {'name': 'Beta Corrupted Master Controller', 'price': 0, 'discount': 0, 'id': 548, 'type': 'CREATURE'},
             {'name': 'Beta Moeder, Master of the Ocean', 'price': 0, 'discount': 0, 'id': 549, 'type': 'CREATURE'},
             {'name': 'Bloodstalker', 'price': 0, 'discount': 0, 'id': 550, 'type': 'CREATURE'},
             {'name': 'Brute Araneo', 'price': 0, 'discount': 0, 'id': 551, 'type': 'CREATURE'},
             {'name': 'Brute Astrocetus', 'price': 0, 'discount': 0, 'id': 552, 'type': 'CREATURE'},
             {'name': 'Brute Basilosaurus', 'price': 0, 'discount': 0, 'id': 553, 'type': 'CREATURE'},
             {'name': 'Brute Bloodstalker', 'price': 0, 'discount': 0, 'id': 554, 'type': 'CREATURE'},
             {'name': 'Brute Ferox', 'price': 0, 'discount': 0, 'id': 555, 'type': 'CREATURE'},
             {'name': 'Brute Fire Wyvern', 'price': 0, 'discount': 0, 'id': 556, 'type': 'CREATURE'},
             {'name': 'Brute Leedsichthys', 'price': 0, 'discount': 0, 'id': 557, 'type': 'CREATURE'},
             {'name': 'Brute Magmasaur', 'price': 0, 'discount': 0, 'id': 558, 'type': 'CREATURE'},
             {'name': 'Brute Malfunctioned Tek Giganotosaurus', 'price': 0, 'discount': 0, 'id': 559,
              'type': 'CREATURE'},
             {'name': 'Brute Malfunctioned Tek Rex', 'price': 0, 'discount': 0, 'id': 560, 'type': 'CREATURE'},
             {'name': 'Brute Mammoth', 'price': 0, 'discount': 0, 'id': 561, 'type': 'CREATURE'},
             {'name': 'Brute Megaloceros', 'price': 0, 'discount': 0, 'id': 562, 'type': 'CREATURE'},
             {'name': 'Brute Plesiosaur', 'price': 0, 'discount': 0, 'id': 563, 'type': 'CREATURE'},
             {'name': 'Brute Reaper King', 'price': 0, 'discount': 0, 'id': 564, 'type': 'CREATURE'},
             {'name': 'Brute Sarco', 'price': 0, 'discount': 0, 'id': 565, 'type': 'CREATURE'},
             {'name': 'Brute Seeker', 'price': 0, 'discount': 0, 'id': 566, 'type': 'CREATURE'},
             {'name': 'Brute Tusoteuthis', 'price': 0, 'discount': 0, 'id': 567, 'type': 'CREATURE'},
             {'name': 'Brute X-Allosaurus', 'price': 0, 'discount': 0, 'id': 568, 'type': 'CREATURE'},
             {'name': 'Brute X-Megalodon', 'price': 0, 'discount': 0, 'id': 569, 'type': 'CREATURE'},
             {'name': 'Brute X-Mosasaurus', 'price': 0, 'discount': 0, 'id': 570, 'type': 'CREATURE'},
             {'name': 'Brute X-Raptor', 'price': 0, 'discount': 0, 'id': 571, 'type': 'CREATURE'},
             {'name': 'Brute X-Rex', 'price': 0, 'discount': 0, 'id': 572, 'type': 'CREATURE'},
             {'name': 'Brute X-Rock Elemental', 'price': 0, 'discount': 0, 'id': 573, 'type': 'CREATURE'},
             {'name': 'Brute X-Spino', 'price': 0, 'discount': 0, 'id': 574, 'type': 'CREATURE'},
             {'name': 'Brute X-Yutyrannus', 'price': 0, 'discount': 0, 'id': 575, 'type': 'CREATURE'},
             {'name': 'Corrupted Avatar', 'price': 0, 'discount': 0, 'id': 576, 'type': 'CREATURE'},
             {'name': 'Eel Minion', 'price': 0, 'discount': 0, 'id': 577, 'type': 'CREATURE'},
             {'name': 'Gamma Corrupted Master Controller', 'price': 0, 'discount': 0, 'id': 578, 'type': 'CREATURE'},
             {'name': 'Gamma Moeder, Master of the Ocean', 'price': 0, 'discount': 0, 'id': 579, 'type': 'CREATURE'},
             {'name': 'Golden Striped Brute Megalodon', 'price': 0, 'discount': 0, 'id': 580, 'type': 'CREATURE'},
             {'name': 'Golden Striped Megalodon', 'price': 0, 'discount': 0, 'id': 581, 'type': 'CREATURE'},
             {'name': 'Ferox (Large)', 'price': 0, 'discount': 0, 'id': 582, 'type': 'CREATURE'},
             {'name': 'Ferox', 'price': 0, 'discount': 0, 'id': 583, 'type': 'CREATURE'},
             {'name': 'Injured Brute Reaper King', 'price': 0, 'discount': 0, 'id': 584, 'type': 'CREATURE'},
             {'name': 'Insect Swarm', 'price': 0, 'discount': 0, 'id': 585, 'type': 'CREATURE'},
             {'name': 'Magmasaur', 'price': 0, 'discount': 0, 'id': 586, 'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Giganotosaurus Gauntlet', 'price': 0, 'discount': 0, 'id': 587,
              'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Giganotosaurus', 'price': 0, 'discount': 0, 'id': 588, 'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Parasaur', 'price': 0, 'discount': 0, 'id': 589, 'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Quetzal', 'price': 0, 'discount': 0, 'id': 590, 'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Raptor', 'price': 0, 'discount': 0, 'id': 591, 'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Rex', 'price': 0, 'discount': 0, 'id': 592, 'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Stegosaurus', 'price': 0, 'discount': 0, 'id': 593, 'type': 'CREATURE'},
             {'name': 'Malfunctioned Tek Triceratops', 'price': 0, 'discount': 0, 'id': 594, 'type': 'CREATURE'},
             {'name': 'Megachelon', 'price': 0, 'discount': 0, 'id': 595, 'type': 'CREATURE'},
             {'name': 'Parakeet Fish School', 'price': 0, 'discount': 0, 'id': 596, 'type': 'CREATURE'},
             {'name': 'Reaper Prince', 'price': 0, 'discount': 0, 'id': 597, 'type': 'CREATURE'},
             {'name': 'Tek Triceratops', 'price': 0, 'discount': 0, 'id': 598, 'type': 'CREATURE'},
             {'name': 'X-Allosaurus', 'price': 0, 'discount': 0, 'id': 599, 'type': 'CREATURE'},
             {'name': 'X-Ankylosaurus', 'price': 0, 'discount': 0, 'id': 600, 'type': 'CREATURE'},
             {'name': 'X-Argentavis', 'price': 0, 'discount': 0, 'id': 601, 'type': 'CREATURE'},
             {'name': 'X-Basilosaurus', 'price': 0, 'discount': 0, 'id': 602, 'type': 'CREATURE'},
             {'name': 'X-Dunkleosteus', 'price': 0, 'discount': 0, 'id': 603, 'type': 'CREATURE'},
             {'name': 'X-Ichthyosaurus', 'price': 0, 'discount': 0, 'id': 604, 'type': 'CREATURE'},
             {'name': 'X-Megalodon', 'price': 0, 'discount': 0, 'id': 605, 'type': 'CREATURE'},
             {'name': 'X-Mosasaurus', 'price': 0, 'discount': 0, 'id': 606, 'type': 'CREATURE'},
             {'name': 'X-Otter', 'price': 0, 'discount': 0, 'id': 607, 'type': 'CREATURE'},
             {'name': 'X-Paraceratherium', 'price': 0, 'discount': 0, 'id': 608, 'type': 'CREATURE'},
             {'name': 'X-Parasaur', 'price': 0, 'discount': 0, 'id': 609, 'type': 'CREATURE'},
             {'name': 'X-Raptor', 'price': 0, 'discount': 0, 'id': 610, 'type': 'CREATURE'},
             {'name': 'X-Rex', 'price': 0, 'discount': 0, 'id': 611, 'type': 'CREATURE'},
             {'name': 'X-Rock Elemental', 'price': 0, 'discount': 0, 'id': 612, 'type': 'CREATURE'},
             {'name': 'X-Sabertooth', 'price': 0, 'discount': 0, 'id': 613, 'type': 'CREATURE'},
             {'name': 'X-Sabertooth Salmon', 'price': 0, 'discount': 0, 'id': 614, 'type': 'CREATURE'},
             {'name': 'X-Spino', 'price': 0, 'discount': 0, 'id': 615, 'type': 'CREATURE'},
             {'name': 'X-Tapejara', 'price': 0, 'discount': 0, 'id': 616, 'type': 'CREATURE'},
             {'name': 'X-Triceratops', 'price': 0, 'discount': 0, 'id': 617, 'type': 'CREATURE'},
             {'name': 'X-Woolly Rhino', 'price': 0, 'discount': 0, 'id': 618, 'type': 'CREATURE'},
             {'name': 'X-Yutyrannus', 'price': 0, 'discount': 0, 'id': 619, 'type': 'CREATURE'},
             {'name': 'Astrodelphis', 'price': 0, 'discount': 0, 'id': 620, 'type': 'CREATURE'},
             {'name': 'Maewing', 'price': 0, 'discount': 0, 'id': 621, 'type': 'CREATURE'},
             {'name': 'Noglin', 'price': 0, 'discount': 0, 'id': 622, 'type': 'CREATURE'},
             {'name': 'Shadowmane', 'price': 0, 'discount': 0, 'id': 623, 'type': 'CREATURE'},
             {'name': 'Tek Stryder', 'price': 0, 'discount': 0, 'id': 624, 'type': 'CREATURE'},
             {'name': 'Voidwyrm', 'price': 0, 'discount': 0, 'id': 625, 'type': 'CREATURE'},
             {'name': 'R-Allosaurus', 'price': 0, 'discount': 0, 'id': 626, 'type': 'CREATURE'},
             {'name': 'R-Carnotaurus', 'price': 0, 'discount': 0, 'id': 627, 'type': 'CREATURE'},
             {'name': 'R-Daeodon', 'price': 0, 'discount': 0, 'id': 628, 'type': 'CREATURE'},
             {'name': 'R-Dilophosaur', 'price': 0, 'discount': 0, 'id': 629, 'type': 'CREATURE'},
             {'name': 'R-Dire Bear', 'price': 0, 'discount': 0, 'id': 630, 'type': 'CREATURE'},
             {'name': 'R-Direwolf', 'price': 0, 'discount': 0, 'id': 631, 'type': 'CREATURE'},
             {'name': 'R-Equus', 'price': 0, 'discount': 0, 'id': 632, 'type': 'CREATURE'},
             {'name': 'R-Gasbags', 'price': 0, 'discount': 0, 'id': 633, 'type': 'CREATURE'},
             {'name': 'R-Giganotosaurus', 'price': 0, 'discount': 0, 'id': 634, 'type': 'CREATURE'},
             {'name': 'R-Megatherium', 'price': 0, 'discount': 0, 'id': 635, 'type': 'CREATURE'},
             {'name': 'R-Snow Owl', 'price': 0, 'discount': 0, 'id': 636, 'type': 'CREATURE'},
             {'name': 'R-Parasaur', 'price': 0, 'discount': 0, 'id': 637, 'type': 'CREATURE'},
             {'name': 'R-Procoptodon', 'price': 0, 'discount': 0, 'id': 638, 'type': 'CREATURE'},
             {'name': 'R-Quetzal', 'price': 0, 'discount': 0, 'id': 639, 'type': 'CREATURE'},
             {'name': 'R-Brontosaurus', 'price': 0, 'discount': 0, 'id': 640, 'type': 'CREATURE'},
             {'name': 'R-Velonasaur', 'price': 0, 'discount': 0, 'id': 641, 'type': 'CREATURE'},
             {'name': 'R-Thylacoleo', 'price': 0, 'discount': 0, 'id': 642, 'type': 'CREATURE'},
             {'name': 'R-Carbonemys', 'price': 0, 'discount': 0, 'id': 643, 'type': 'CREATURE'},
             {'name': 'R-Reaper Queen', 'price': 0, 'discount': 0, 'id': 644, 'type': 'CREATURE'},
             {'name': 'R-Reaper King', 'price': 0, 'discount': 0, 'id': 645, 'type': 'CREATURE'},
             {'name': 'R-Reaper King (Tamed)', 'price': 0, 'discount': 0, 'id': 646, 'type': 'CREATURE'},
             {'name': 'Summoner', 'price': 0, 'discount': 0, 'id': 647, 'type': 'CREATURE'},
             {'name': 'Macrophage', 'price': 0, 'discount': 0, 'id': 648, 'type': 'CREATURE'},
             {'name': 'Exo-Mek', 'price': 0, 'discount': 0, 'id': 649, 'type': 'CREATURE'},
             {'name': 'Rockwell Prime', 'price': 0, 'discount': 0, 'id': 650, 'type': 'CREATURE'},
             {'name': 'Rockwell Prime (Alpha)', 'price': 0, 'discount': 0, 'id': 651, 'type': 'CREATURE'},
             {'name': 'Rockwell Prime (Beta)', 'price': 0, 'discount': 0, 'id': 652, 'type': 'CREATURE'},
             {'name': 'Rockwell Prime (Gamma)', 'price': 0, 'discount': 0, 'id': 653, 'type': 'CREATURE'},
             {'name': 'Rockwell Node', 'price': 0, 'discount': 0, 'id': 654, 'type': 'CREATURE'},
             {'name': 'Rockwell Node (Alpha)', 'price': 0, 'discount': 0, 'id': 655, 'type': 'CREATURE'},
             {'name': 'Rockwell Node (Beta)', 'price': 0, 'discount': 0, 'id': 656, 'type': 'CREATURE'},
             {'name': 'Rockwell Node (Gamma)', 'price': 0, 'discount': 0, 'id': 657, 'type': 'CREATURE'},
             {'name': 'Achatina', 'price': 0, 'discount': 0, 'id': 658, 'type': 'CREATURE'},
             {'name': 'Allosaurus', 'price': 0, 'discount': 0, 'id': 659, 'type': 'CREATURE'},
             {'name': 'Alpha Carno', 'price': 0, 'discount': 0, 'id': 660, 'type': 'CREATURE'},
             {'name': 'Alpha Leedsichthys', 'price': 0, 'discount': 0, 'id': 661, 'type': 'CREATURE'},
             {'name': 'Alpha Megalodon', 'price': 0, 'discount': 0, 'id': 662, 'type': 'CREATURE'},
             {'name': 'Alpha Mosasaur', 'price': 0, 'discount': 0, 'id': 663, 'type': 'CREATURE'},
             {'name': 'Alpha Raptor', 'price': 0, 'discount': 0, 'id': 664, 'type': 'CREATURE'},
             {'name': 'Alpha T-Rex', 'price': 0, 'discount': 0, 'id': 665, 'type': 'CREATURE'},
             {'name': 'Alpha Tusoteuthis', 'price': 0, 'discount': 0, 'id': 666, 'type': 'CREATURE'},
             {'name': 'Ammonite', 'price': 0, 'discount': 0, 'id': 667, 'type': 'CREATURE'},
             {'name': 'Anglerfish', 'price': 0, 'discount': 0, 'id': 668, 'type': 'CREATURE'},
             {'name': 'Ankylosaurus', 'price': 0, 'discount': 0, 'id': 669, 'type': 'CREATURE'},
             {'name': 'Araneo', 'price': 0, 'discount': 0, 'id': 670, 'type': 'CREATURE'},
             {'name': 'Archaeopteryx', 'price': 0, 'discount': 0, 'id': 671, 'type': 'CREATURE'},
             {'name': 'Argentavis', 'price': 0, 'discount': 0, 'id': 672, 'type': 'CREATURE'},
             {'name': 'Arthropluera', 'price': 0, 'discount': 0, 'id': 673, 'type': 'CREATURE'},
             {'name': 'Baryonyx', 'price': 0, 'discount': 0, 'id': 674, 'type': 'CREATURE'},
             {'name': 'Basilosaurus', 'price': 0, 'discount': 0, 'id': 675, 'type': 'CREATURE'},
             {'name': 'Beelzebufo', 'price': 0, 'discount': 0, 'id': 676, 'type': 'CREATURE'},
             {'name': 'Bunny Dodo', 'price': 0, 'discount': 0, 'id': 677, 'type': 'CREATURE'},
             {'name': 'Bunny Oviraptor', 'price': 0, 'discount': 0, 'id': 678, 'type': 'CREATURE'},
             {'name': 'Brontosaurus', 'price': 0, 'discount': 0, 'id': 679, 'type': 'CREATURE'},
             {'name': 'Broodmother Lysrix', 'price': 0, 'discount': 0, 'id': 680, 'type': 'CREATURE'},
             {'name': 'Chalicotherium', 'price': 0, 'discount': 0, 'id': 681, 'type': 'CREATURE'},
             {'name': 'Carbonemys', 'price': 0, 'discount': 0, 'id': 682, 'type': 'CREATURE'},
             {'name': 'Carnotaurus', 'price': 0, 'discount': 0, 'id': 683, 'type': 'CREATURE'},
             {'name': 'Castoroides', 'price': 0, 'discount': 0, 'id': 684, 'type': 'CREATURE'},
             {'name': 'Cnidaria', 'price': 0, 'discount': 0, 'id': 685, 'type': 'CREATURE'},
             {'name': 'Coelacanth', 'price': 0, 'discount': 0, 'id': 686, 'type': 'CREATURE'},
             {'name': 'Compy', 'price': 0, 'discount': 0, 'id': 687, 'type': 'CREATURE'},
             {'name': 'Daeodon', 'price': 0, 'discount': 0, 'id': 688, 'type': 'CREATURE'},
             {'name': 'Dilophosaur', 'price': 0, 'discount': 0, 'id': 689, 'type': 'CREATURE'},
             {'name': 'Dimetrodon', 'price': 0, 'discount': 0, 'id': 690, 'type': 'CREATURE'},
             {'name': 'Dimorphodon', 'price': 0, 'discount': 0, 'id': 691, 'type': 'CREATURE'},
             {'name': 'Diplocaulus', 'price': 0, 'discount': 0, 'id': 692, 'type': 'CREATURE'},
             {'name': 'Diplodocus', 'price': 0, 'discount': 0, 'id': 693, 'type': 'CREATURE'},
             {'name': 'Dire Bear', 'price': 0, 'discount': 0, 'id': 694, 'type': 'CREATURE'},
             {'name': 'Direwolf', 'price': 0, 'discount': 0, 'id': 695, 'type': 'CREATURE'},
             {'name': 'Direwolf Ghost', 'price': 0, 'discount': 0, 'id': 696, 'type': 'CREATURE'},
             {'name': 'Dodo', 'price': 0, 'discount': 0, 'id': 697, 'type': 'CREATURE'},
             {'name': 'DodoRex', 'price': 0, 'discount': 0, 'id': 698, 'type': 'CREATURE'},
             {'name': 'Doedicurus', 'price': 0, 'discount': 0, 'id': 699, 'type': 'CREATURE'},
             {'name': 'Dragon (Gamma)', 'price': 0, 'discount': 0, 'id': 700, 'type': 'CREATURE'},
             {'name': 'Dragon (Beta)', 'price': 0, 'discount': 0, 'id': 701, 'type': 'CREATURE'},
             {'name': 'Dragon (Alpha)', 'price': 0, 'discount': 0, 'id': 702, 'type': 'CREATURE'},
             {'name': 'Dung Beetle', 'price': 0, 'discount': 0, 'id': 703, 'type': 'CREATURE'},
             {'name': 'Dunkleosteus', 'price': 0, 'discount': 0, 'id': 704, 'type': 'CREATURE'},
             {'name': 'Electrophorus', 'price': 0, 'discount': 0, 'id': 705, 'type': 'CREATURE'},
             {'name': 'Equus', 'price': 0, 'discount': 0, 'id': 706, 'type': 'CREATURE'},
             {'name': 'Unicorn', 'price': 0, 'discount': 0, 'id': 707, 'type': 'CREATURE'},
             {'name': 'Eurypterid', 'price': 0, 'discount': 0, 'id': 708, 'type': 'CREATURE'},
             {'name': 'Gallimimus', 'price': 0, 'discount': 0, 'id': 709, 'type': 'CREATURE'},
             {'name': 'Giant Bee', 'price': 0, 'discount': 0, 'id': 710, 'type': 'CREATURE'},
             {'name': 'Giganotosaurus', 'price': 0, 'discount': 0, 'id': 711, 'type': 'CREATURE'},
             {'name': 'Gigantopithecus', 'price': 0, 'discount': 0, 'id': 712, 'type': 'CREATURE'},
             {'name': 'Hesperornis', 'price': 0, 'discount': 0, 'id': 713, 'type': 'CREATURE'},
             {'name': 'Human (Male)', 'price': 0, 'discount': 0, 'id': 714, 'type': 'CREATURE'},
             {'name': 'Human (Female)', 'price': 0, 'discount': 0, 'id': 715, 'type': 'CREATURE'},
             {'name': 'Hyaenodon', 'price': 0, 'discount': 0, 'id': 716, 'type': 'CREATURE'},
             {'name': 'Ichthyornis', 'price': 0, 'discount': 0, 'id': 717, 'type': 'CREATURE'},
             {'name': 'Ichthyosaurus', 'price': 0, 'discount': 0, 'id': 718, 'type': 'CREATURE'},
             {'name': 'Iguanodon', 'price': 0, 'discount': 0, 'id': 719, 'type': 'CREATURE'},
             {'name': 'Kairuku', 'price': 0, 'discount': 0, 'id': 720, 'type': 'CREATURE'},
             {'name': 'Kaprosuchus', 'price': 0, 'discount': 0, 'id': 721, 'type': 'CREATURE'},
             {'name': 'Kentrosaurus', 'price': 0, 'discount': 0, 'id': 722, 'type': 'CREATURE'},
             {'name': 'Leech', 'price': 0, 'discount': 0, 'id': 723, 'type': 'CREATURE'},
             {'name': 'Diseased Leech', 'price': 0, 'discount': 0, 'id': 724, 'type': 'CREATURE'},
             {'name': 'Leedsichthys', 'price': 0, 'discount': 0, 'id': 725, 'type': 'CREATURE'},
             {'name': 'Liopleurodon', 'price': 0, 'discount': 0, 'id': 726, 'type': 'CREATURE'},
             {'name': 'Lystrosaurus', 'price': 0, 'discount': 0, 'id': 727, 'type': 'CREATURE'},
             {'name': 'Mammoth', 'price': 0, 'discount': 0, 'id': 728, 'type': 'CREATURE'},
             {'name': 'Manta', 'price': 0, 'discount': 0, 'id': 729, 'type': 'CREATURE'},
             {'name': 'Megalania', 'price': 0, 'discount': 0, 'id': 730, 'type': 'CREATURE'},
             {'name': 'Megaloceros', 'price': 0, 'discount': 0, 'id': 731, 'type': 'CREATURE'},
             {'name': 'Megalodon', 'price': 0, 'discount': 0, 'id': 732, 'type': 'CREATURE'},
             {'name': 'Megalosaurus', 'price': 0, 'discount': 0, 'id': 733, 'type': 'CREATURE'},
             {'name': 'Meganeura', 'price': 0, 'discount': 0, 'id': 734, 'type': 'CREATURE'},
             {'name': 'Megapithecus', 'price': 0, 'discount': 0, 'id': 735, 'type': 'CREATURE'},
             {'name': 'Megatherium', 'price': 0, 'discount': 0, 'id': 736, 'type': 'CREATURE'},
             {'name': 'Mesopithecus', 'price': 0, 'discount': 0, 'id': 737, 'type': 'CREATURE'},
             {'name': 'Microraptor', 'price': 0, 'discount': 0, 'id': 738, 'type': 'CREATURE'},
             {'name': 'Mosasaurus', 'price': 0, 'discount': 0, 'id': 739, 'type': 'CREATURE'},
             {'name': 'Moschops', 'price': 0, 'discount': 0, 'id': 740, 'type': 'CREATURE'},
             {'name': 'Onychonycteris', 'price': 0, 'discount': 0, 'id': 741, 'type': 'CREATURE'},
             {'name': 'Otter', 'price': 0, 'discount': 0, 'id': 742, 'type': 'CREATURE'},
             {'name': 'Oviraptor', 'price': 0, 'discount': 0, 'id': 743, 'type': 'CREATURE'},
             {'name': 'Ovis', 'price': 0, 'discount': 0, 'id': 744, 'type': 'CREATURE'},
             {'name': 'Pachy', 'price': 0, 'discount': 0, 'id': 745, 'type': 'CREATURE'},
             {'name': 'Pachyrhinosaurus', 'price': 0, 'discount': 0, 'id': 746, 'type': 'CREATURE'},
             {'name': 'Paraceratherium', 'price': 0, 'discount': 0, 'id': 747, 'type': 'CREATURE'},
             {'name': 'Parasaurolophus', 'price': 0, 'discount': 0, 'id': 748, 'type': 'CREATURE'},
             {'name': 'Pegomastax', 'price': 0, 'discount': 0, 'id': 749, 'type': 'CREATURE'},
             {'name': 'Pelagornis', 'price': 0, 'discount': 0, 'id': 750, 'type': 'CREATURE'},
             {'name': 'Phiomia', 'price': 0, 'discount': 0, 'id': 751, 'type': 'CREATURE'},
             {'name': 'Piranha', 'price': 0, 'discount': 0, 'id': 752, 'type': 'CREATURE'},
             {'name': 'Plesiosaur', 'price': 0, 'discount': 0, 'id': 753, 'type': 'CREATURE'},
             {'name': 'Procoptodon', 'price': 0, 'discount': 0, 'id': 754, 'type': 'CREATURE'},
             {'name': 'Pteranodon', 'price': 0, 'discount': 0, 'id': 755, 'type': 'CREATURE'},
             {'name': 'Pulmonoscorpius', 'price': 0, 'discount': 0, 'id': 756, 'type': 'CREATURE'},
             {'name': 'Purlovia', 'price': 0, 'discount': 0, 'id': 757, 'type': 'CREATURE'},
             {'name': 'Quetzalcoatlus', 'price': 0, 'discount': 0, 'id': 758, 'type': 'CREATURE'},
             {'name': 'Raptor', 'price': 0, 'discount': 0, 'id': 759, 'type': 'CREATURE'},
             {'name': 'Rex', 'price': 0, 'discount': 0, 'id': 760, 'type': 'CREATURE'},
             {'name': 'Rex Ghost', 'price': 0, 'discount': 0, 'id': 761, 'type': 'CREATURE'},
             {'name': 'Sabertooth', 'price': 0, 'discount': 0, 'id': 762, 'type': 'CREATURE'},
             {'name': 'Sabertooth Salmon', 'price': 0, 'discount': 0, 'id': 763, 'type': 'CREATURE'},
             {'name': 'Sarco', 'price': 0, 'discount': 0, 'id': 764, 'type': 'CREATURE'},
             {'name': 'Skeletal Bronto', 'price': 0, 'discount': 0, 'id': 765, 'type': 'CREATURE'},
             {'name': 'Skeletal Carnotaurus', 'price': 0, 'discount': 0, 'id': 766, 'type': 'CREATURE'},
             {'name': 'Skeletal Giganotosaurus', 'price': 0, 'discount': 0, 'id': 767, 'type': 'CREATURE'},
             {'name': 'Skeletal Quetzal', 'price': 0, 'discount': 0, 'id': 768, 'type': 'CREATURE'},
             {'name': 'Skeletal Raptor', 'price': 0, 'discount': 0, 'id': 769, 'type': 'CREATURE'},
             {'name': 'Skeletal Rex', 'price': 0, 'discount': 0, 'id': 770, 'type': 'CREATURE'},
             {'name': 'Skeletal Stego', 'price': 0, 'discount': 0, 'id': 771, 'type': 'CREATURE'},
             {'name': 'Skeletal Trike', 'price': 0, 'discount': 0, 'id': 772, 'type': 'CREATURE'},
             {'name': 'Spino', 'price': 0, 'discount': 0, 'id': 773, 'type': 'CREATURE'},
             {'name': 'Stegosaurus', 'price': 0, 'discount': 0, 'id': 774, 'type': 'CREATURE'},
             {'name': 'Tapejara', 'price': 0, 'discount': 0, 'id': 775, 'type': 'CREATURE'},
             {'name': 'Tek Parasaur', 'price': 0, 'discount': 0, 'id': 776, 'type': 'CREATURE'},
             {'name': 'Tek Quetzal', 'price': 0, 'discount': 0, 'id': 777, 'type': 'CREATURE'},
             {'name': 'Tek Raptor', 'price': 0, 'discount': 0, 'id': 778, 'type': 'CREATURE'},
             {'name': 'Tek Rex', 'price': 0, 'discount': 0, 'id': 779, 'type': 'CREATURE'},
             {'name': 'Tek Stegosaurus', 'price': 0, 'discount': 0, 'id': 780, 'type': 'CREATURE'},
             {'name': 'Terror Bird', 'price': 0, 'discount': 0, 'id': 781, 'type': 'CREATURE'},
             {'name': 'Therizinosaur', 'price': 0, 'discount': 0, 'id': 782, 'type': 'CREATURE'},
             {'name': 'Thylacoleo', 'price': 0, 'discount': 0, 'id': 783, 'type': 'CREATURE'},
             {'name': 'Titanoboa', 'price': 0, 'discount': 0, 'id': 784, 'type': 'CREATURE'},
             {'name': 'Titanomyrma Ground', 'price': 0, 'discount': 0, 'id': 785, 'type': 'CREATURE'},
             {'name': 'Titanomyrma Air', 'price': 0, 'discount': 0, 'id': 786, 'type': 'CREATURE'},
             {'name': 'Titanosaur', 'price': 0, 'discount': 0, 'id': 787, 'type': 'CREATURE'},
             {'name': 'Triceratops', 'price': 0, 'discount': 0, 'id': 788, 'type': 'CREATURE'},
             {'name': 'Trilobite', 'price': 0, 'discount': 0, 'id': 789, 'type': 'CREATURE'},
             {'name': 'Troodon', 'price': 0, 'discount': 0, 'id': 790, 'type': 'CREATURE'},
             {'name': 'Turkey', 'price': 0, 'discount': 0, 'id': 791, 'type': 'CREATURE'},
             {'name': 'Super Turkey', 'price': 0, 'discount': 0, 'id': 792, 'type': 'CREATURE'},
             {'name': 'Tusoteuthis', 'price': 0, 'discount': 0, 'id': 793, 'type': 'CREATURE'},
             {'name': 'Woolly Rhino', 'price': 0, 'discount': 0, 'id': 794, 'type': 'CREATURE'},
             {'name': 'Yeti', 'price': 0, 'discount': 0, 'id': 795, 'type': 'CREATURE'},
             {'name': 'Yutyrannus', 'price': 0, 'discount': 0, 'id': 796, 'type': 'CREATURE'},
             {'name': 'Zomdodo', 'price': 0, 'discount': 0, 'id': 797, 'type': 'CREATURE'},
             {'name': 'Griffin', 'price': 0, 'discount': 0, 'id': 798, 'type': 'CREATURE'},
             {'name': 'Ice Wyvern', 'price': 0, 'discount': 0, 'id': 799, 'type': 'CREATURE'},
             {'name': 'Alpha Fire Wyvern', 'price': 0, 'discount': 0, 'id': 800, 'type': 'CREATURE'},
             {'name': 'Alpha Deathworm', 'price': 0, 'discount': 0, 'id': 801, 'type': 'CREATURE'},
             {'name': 'Deathworm', 'price': 0, 'discount': 0, 'id': 802, 'type': 'CREATURE'},
             {'name': 'Dodo Wyvern', 'price': 0, 'discount': 0, 'id': 803, 'type': 'CREATURE'},
             {'name': 'Jerboa', 'price': 0, 'discount': 0, 'id': 804, 'type': 'CREATURE'},
             {'name': 'Skeletal Jerboa', 'price': 0, 'discount': 0, 'id': 805, 'type': 'CREATURE'},
             {'name': 'Jug Bug', 'price': 0, 'discount': 0, 'id': 806, 'type': 'CREATURE'},
             {'name': 'Oil Jug Bug', 'price': 0, 'discount': 0, 'id': 807, 'type': 'CREATURE'},
             {'name': 'Water Jug Bug', 'price': 0, 'discount': 0, 'id': 808, 'type': 'CREATURE'},
             {'name': 'Lymantria', 'price': 0, 'discount': 0, 'id': 809, 'type': 'CREATURE'},
             {'name': 'Manticore (Gamma)', 'price': 0, 'discount': 0, 'id': 810, 'type': 'CREATURE'},
             {'name': 'Manticore (Beta)', 'price': 0, 'discount': 0, 'id': 811, 'type': 'CREATURE'},
             {'name': 'Manticore (Alpha)', 'price': 0, 'discount': 0, 'id': 812, 'type': 'CREATURE'},
             {'name': 'Mantis', 'price': 0, 'discount': 0, 'id': 813, 'type': 'CREATURE'},
             {'name': 'Mantis Ghost', 'price': 0, 'discount': 0, 'id': 814, 'type': 'CREATURE'},
             {'name': 'Morellatops', 'price': 0, 'discount': 0, 'id': 815, 'type': 'CREATURE'},
             {'name': 'Rock Elemental', 'price': 0, 'discount': 0, 'id': 816, 'type': 'CREATURE'},
             {'name': 'Rubble Golem', 'price': 0, 'discount': 0, 'id': 817, 'type': 'CREATURE'},
             {'name': 'Thorny Dragon', 'price': 0, 'discount': 0, 'id': 818, 'type': 'CREATURE'},
             {'name': 'Vulture', 'price': 0, 'discount': 0, 'id': 819, 'type': 'CREATURE'},
             {'name': 'Wyvern', 'price': 0, 'discount': 0, 'id': 820, 'type': 'CREATURE'},
             {'name': 'Phoenix', 'price': 0, 'discount': 0, 'id': 821, 'type': 'CREATURE'},
             {'name': 'Fire Wyvern', 'price': 0, 'discount': 0, 'id': 822, 'type': 'CREATURE'},
             {'name': 'Lightning Wyvern', 'price': 0, 'discount': 0, 'id': 823, 'type': 'CREATURE'},
             {'name': 'Poison Wyvern', 'price': 0, 'discount': 0, 'id': 824, 'type': 'CREATURE'},
             {'name': 'Bone Fire Wyvern', 'price': 0, 'discount': 0, 'id': 825, 'type': 'CREATURE'},
             {'name': 'Zombie Fire Wyvern', 'price': 0, 'discount': 0, 'id': 826, 'type': 'CREATURE'},
             {'name': 'Zombie Lightning Wyvern', 'price': 0, 'discount': 0, 'id': 827, 'type': 'CREATURE'},
             {'name': 'Zombie Poison Wyvern', 'price': 0, 'discount': 0, 'id': 828, 'type': 'CREATURE'},
             {'name': 'Chalk Golem', 'price': 0, 'discount': 0, 'id': 829, 'type': 'CREATURE'},
             {'name': 'Deinonychus', 'price': 0, 'discount': 0, 'id': 830, 'type': 'CREATURE'},
             {'name': 'Ice Golem', 'price': 0, 'discount': 0, 'id': 831, 'type': 'CREATURE'},
             {'name': 'Red Coloring', 'price': 0, 'discount': 0, 'id': 832, 'type': 'DYE'},
             {'name': 'Green Coloring', 'price': 0, 'discount': 0, 'id': 833, 'type': 'DYE'},
             {'name': 'Blue Coloring', 'price': 0, 'discount': 0, 'id': 834, 'type': 'DYE'},
             {'name': 'Yellow Coloring', 'price': 0, 'discount': 0, 'id': 835, 'type': 'DYE'},
             {'name': 'Orange Coloring', 'price': 0, 'discount': 0, 'id': 836, 'type': 'DYE'},
             {'name': 'Black Coloring', 'price': 0, 'discount': 0, 'id': 837, 'type': 'DYE'},
             {'name': 'White Coloring', 'price': 0, 'discount': 0, 'id': 838, 'type': 'DYE'},
             {'name': 'Brown Coloring', 'price': 0, 'discount': 0, 'id': 839, 'type': 'DYE'},
             {'name': 'Cyan Coloring', 'price': 0, 'discount': 0, 'id': 840, 'type': 'DYE'},
             {'name': 'Purple Coloring', 'price': 0, 'discount': 0, 'id': 841, 'type': 'DYE'},
             {'name': 'Forest Coloring', 'price': 0, 'discount': 0, 'id': 842, 'type': 'DYE'},
             {'name': 'Parchment Coloring', 'price': 0, 'discount': 0, 'id': 843, 'type': 'DYE'},
             {'name': 'Pink Coloring', 'price': 0, 'discount': 0, 'id': 844, 'type': 'DYE'},
             {'name': 'Royalty Coloring', 'price': 0, 'discount': 0, 'id': 845, 'type': 'DYE'},
             {'name': 'Silver Coloring', 'price': 0, 'discount': 0, 'id': 846, 'type': 'DYE'},
             {'name': 'Sky Coloring', 'price': 0, 'discount': 0, 'id': 847, 'type': 'DYE'},
             {'name': 'Tan Coloring', 'price': 0, 'discount': 0, 'id': 848, 'type': 'DYE'},
             {'name': 'Tangerine Coloring', 'price': 0, 'discount': 0, 'id': 849, 'type': 'DYE'},
             {'name': 'Magenta Coloring', 'price': 0, 'discount': 0, 'id': 850, 'type': 'DYE'},
             {'name': 'Brick Coloring', 'price': 0, 'discount': 0, 'id': 851, 'type': 'DYE'},
             {'name': 'Cantaloupe Coloring', 'price': 0, 'discount': 0, 'id': 852, 'type': 'DYE'},
             {'name': 'Mud Coloring', 'price': 0, 'discount': 0, 'id': 853, 'type': 'DYE'},
             {'name': 'Navy Coloring', 'price': 0, 'discount': 0, 'id': 854, 'type': 'DYE'},
             {'name': 'Olive Coloring', 'price': 0, 'discount': 0, 'id': 855, 'type': 'DYE'},
             {'name': 'Slate Coloring', 'price': 0, 'discount': 0, 'id': 856, 'type': 'DYE'},
             {'name': 'Stego Egg', 'price': 0, 'discount': 0, 'id': 857, 'type': 'EGG'},
             {'name': 'Bronto Egg', 'price': 0, 'discount': 0, 'id': 858, 'type': 'EGG'},
             {'name': 'Parasaur Egg', 'price': 0, 'discount': 0, 'id': 859, 'type': 'EGG'},
             {'name': 'Raptor Egg', 'price': 0, 'discount': 0, 'id': 860, 'type': 'EGG'},
             {'name': 'Rex Egg', 'price': 0, 'discount': 0, 'id': 861, 'type': 'EGG'},
             {'name': 'Trike Egg', 'price': 0, 'discount': 0, 'id': 862, 'type': 'EGG'},
             {'name': 'Dodo Egg', 'price': 0, 'discount': 0, 'id': 863, 'type': 'EGG'},
             {'name': 'Ankylo Egg', 'price': 0, 'discount': 0, 'id': 864, 'type': 'EGG'},
             {'name': 'Argentavis Egg', 'price': 0, 'discount': 0, 'id': 865, 'type': 'EGG'},
             {'name': 'Titanoboa Egg', 'price': 0, 'discount': 0, 'id': 866, 'type': 'EGG'},
             {'name': 'Carno Egg', 'price': 0, 'discount': 0, 'id': 867, 'type': 'EGG'},
             {'name': 'Dilo Egg', 'price': 0, 'discount': 0, 'id': 868, 'type': 'EGG'},
             {'name': 'Pteranodon Egg', 'price': 0, 'discount': 0, 'id': 869, 'type': 'EGG'},
             {'name': 'Sarco Egg', 'price': 0, 'discount': 0, 'id': 870, 'type': 'EGG'},
             {'name': 'Pulmonoscorpius Egg', 'price': 0, 'discount': 0, 'id': 871, 'type': 'EGG'},
             {'name': 'Araneo Egg', 'price': 0, 'discount': 0, 'id': 872, 'type': 'EGG'},
             {'name': 'Spino Egg', 'price': 0, 'discount': 0, 'id': 873, 'type': 'EGG'},
             {'name': 'Turtle Egg', 'price': 0, 'discount': 0, 'id': 874, 'type': 'EGG'},
             {'name': 'Pachycephalosaurus Egg', 'price': 0, 'discount': 0, 'id': 875, 'type': 'EGG'},
             {'name': 'Dimorph Egg', 'price': 0, 'discount': 0, 'id': 876, 'type': 'EGG'},
             {'name': 'Allosaurus Egg', 'price': 0, 'discount': 0, 'id': 877, 'type': 'EGG'},
             {'name': 'Archaeopteryx Egg', 'price': 0, 'discount': 0, 'id': 878, 'type': 'EGG'},
             {'name': 'Arthropluera Egg', 'price': 0, 'discount': 0, 'id': 879, 'type': 'EGG'},
             {'name': 'Baryonyx Egg', 'price': 0, 'discount': 0, 'id': 880, 'type': 'EGG'},
             {'name': 'Basic Maewing Egg', 'price': 0, 'discount': 0, 'id': 881, 'type': 'EGG'},
             {'name': 'Basilisk Egg', 'price': 0, 'discount': 0, 'id': 882, 'type': 'EGG'},
             {'name': 'Blood Crystal Wyvern Egg', 'price': 0, 'discount': 0, 'id': 883, 'type': 'EGG'},
             {'name': 'Bloodstalker Egg', 'price': 0, 'discount': 0, 'id': 884, 'type': 'EGG'},
             {'name': 'Camelsaurus Egg', 'price': 0, 'discount': 0, 'id': 885, 'type': 'EGG'},
             {'name': 'Compy Egg', 'price': 0, 'discount': 0, 'id': 886, 'type': 'EGG'},
             {'name': 'Crystal Wyvern Egg', 'price': 0, 'discount': 0, 'id': 887, 'type': 'EGG'},
             {'name': 'Deinonychus Egg', 'price': 0, 'discount': 0, 'id': 888, 'type': 'EGG'},
             {'name': 'Dimetrodon Egg', 'price': 0, 'discount': 0, 'id': 889, 'type': 'EGG'},
             {'name': 'Diplo Egg', 'price': 0, 'discount': 0, 'id': 890, 'type': 'EGG'},
             {'name': 'Ember Crystal Wyvern Egg', 'price': 0, 'discount': 0, 'id': 891, 'type': 'EGG'},
             {'name': 'Exceptional Maewing Egg', 'price': 0, 'discount': 0, 'id': 892, 'type': 'EGG'},
             {'name': 'Extraordinary Maewing Egg', 'price': 0, 'discount': 0, 'id': 893, 'type': 'EGG'},
             {'name': 'Featherlight Egg', 'price': 0, 'discount': 0, 'id': 894, 'type': 'EGG'},
             {'name': 'Fish Egg', 'price': 0, 'discount': 0, 'id': 895, 'type': 'EGG'},
             {'name': 'Gallimimus Egg', 'price': 0, 'discount': 0, 'id': 896, 'type': 'EGG'},
             {'name': 'Giganotosaurus Egg', 'price': 0, 'discount': 0, 'id': 897, 'type': 'EGG'},
             {'name': 'Glowtail Egg', 'price': 0, 'discount': 0, 'id': 898, 'type': 'EGG'},
             {'name': 'Golden Hesperornis Egg', 'price': 0, 'discount': 0, 'id': 899, 'type': 'EGG'},
             {'name': 'Hesperornis Egg', 'price': 0, 'discount': 0, 'id': 900, 'type': 'EGG'},
             {'name': 'Ichthyornis Egg', 'price': 0, 'discount': 0, 'id': 901, 'type': 'EGG'},
             {'name': 'Iguanodon Egg', 'price': 0, 'discount': 0, 'id': 902, 'type': 'EGG'},
             {'name': 'Kairuku Egg', 'price': 0, 'discount': 0, 'id': 903, 'type': 'EGG'},
             {'name': 'Kaprosuchus Egg', 'price': 0, 'discount': 0, 'id': 904, 'type': 'EGG'},
             {'name': 'Kentro Egg', 'price': 0, 'discount': 0, 'id': 905, 'type': 'EGG'},
             {'name': 'Lystro Egg', 'price': 0, 'discount': 0, 'id': 906, 'type': 'EGG'},
             {'name': 'Magmasaur Egg', 'price': 0, 'discount': 0, 'id': 907, 'type': 'EGG'},
             {'name': 'Mantis Egg', 'price': 0, 'discount': 0, 'id': 908, 'type': 'EGG'},
             {'name': 'Megachelon Egg', 'price': 0, 'discount': 0, 'id': 909, 'type': 'EGG'},
             {'name': 'Megalania Egg', 'price': 0, 'discount': 0, 'id': 910, 'type': 'EGG'},
             {'name': 'Megalosaurus Egg', 'price': 0, 'discount': 0, 'id': 911, 'type': 'EGG'},
             {'name': 'Microraptor Egg', 'price': 0, 'discount': 0, 'id': 912, 'type': 'EGG'},
             {'name': 'Moschops Egg', 'price': 0, 'discount': 0, 'id': 913, 'type': 'EGG'},
             {'name': 'Moth Egg', 'price': 0, 'discount': 0, 'id': 914, 'type': 'EGG'},
             {'name': 'Oviraptor Egg', 'price': 0, 'discount': 0, 'id': 915, 'type': 'EGG'},
             {'name': 'Pachyrhino Egg', 'price': 0, 'discount': 0, 'id': 916, 'type': 'EGG'},
             {'name': 'Pegomastax Egg', 'price': 0, 'discount': 0, 'id': 917, 'type': 'EGG'},
             {'name': 'Pelagornis Egg', 'price': 0, 'discount': 0, 'id': 918, 'type': 'EGG'},
             {'name': 'Quetzal Egg', 'price': 0, 'discount': 0, 'id': 919, 'type': 'EGG'},
             {'name': 'Regular Maewing Egg', 'price': 0, 'discount': 0, 'id': 920, 'type': 'EGG'},
             {'name': 'Rock Drake Egg', 'price': 0, 'discount': 0, 'id': 921, 'type': 'EGG'},
             {'name': 'Simple Maewing Egg', 'price': 0, 'discount': 0, 'id': 922, 'type': 'EGG'},
             {'name': 'Superior Maewing Egg', 'price': 0, 'discount': 0, 'id': 923, 'type': 'EGG'},
             {'name': 'Snow Owl Egg', 'price': 0, 'discount': 0, 'id': 924, 'type': 'EGG'},
             {'name': 'Tapejara Egg', 'price': 0, 'discount': 0, 'id': 925, 'type': 'EGG'},
             {'name': 'Tek Parasaur Egg', 'price': 0, 'discount': 0, 'id': 926, 'type': 'EGG'},
             {'name': 'Tek Quetzal Egg', 'price': 0, 'discount': 0, 'id': 927, 'type': 'EGG'},
             {'name': 'Tek Raptor Egg', 'price': 0, 'discount': 0, 'id': 928, 'type': 'EGG'},
             {'name': 'Tek Rex Egg', 'price': 0, 'discount': 0, 'id': 929, 'type': 'EGG'},
             {'name': 'Tek Stego Egg', 'price': 0, 'discount': 0, 'id': 930, 'type': 'EGG'},
             {'name': 'Tek Trike Egg', 'price': 0, 'discount': 0, 'id': 931, 'type': 'EGG'},
             {'name': 'Terror Bird Egg', 'price': 0, 'discount': 0, 'id': 932, 'type': 'EGG'},
             {'name': 'Therizino Egg', 'price': 0, 'discount': 0, 'id': 933, 'type': 'EGG'},
             {'name': 'Thorny Dragon Egg', 'price': 0, 'discount': 0, 'id': 934, 'type': 'EGG'},
             {'name': 'Troodon Egg', 'price': 0, 'discount': 0, 'id': 935, 'type': 'EGG'},
             {'name': 'Tropical Crystal Wyvern Egg', 'price': 0, 'discount': 0, 'id': 936, 'type': 'EGG'},
             {'name': 'Tropeognathus Egg', 'price': 0, 'discount': 0, 'id': 937, 'type': 'EGG'},
             {'name': 'Velonasaur Egg', 'price': 0, 'discount': 0, 'id': 938, 'type': 'EGG'},
             {'name': 'Vulture Egg', 'price': 0, 'discount': 0, 'id': 939, 'type': 'EGG'},
             {'name': 'Wyvern Egg Fire', 'price': 0, 'discount': 0, 'id': 940, 'type': 'EGG'},
             {'name': 'Wyvern Egg Lightning', 'price': 0, 'discount': 0, 'id': 941, 'type': 'EGG'},
             {'name': 'Wyvern Egg Poison', 'price': 0, 'discount': 0, 'id': 942, 'type': 'EGG'},
             {'name': 'Yutyrannus Egg', 'price': 0, 'discount': 0, 'id': 943, 'type': 'EGG'},
             {'name': 'Egg', 'price': 0, 'discount': 0, 'id': 944, 'type': 'EGG'},
             {'name': 'Large Egg', 'price': 0, 'discount': 0, 'id': 945, 'type': 'EGG'},
             {'name': 'Medium Egg', 'price': 0, 'discount': 0, 'id': 946, 'type': 'EGG'},
             {'name': 'Small Egg', 'price': 0, 'discount': 0, 'id': 947, 'type': 'EGG'},
             {'name': 'Special Egg', 'price': 0, 'discount': 0, 'id': 948, 'type': 'EGG'},
             {'name': 'Extra Large Egg', 'price': 0, 'discount': 0, 'id': 949, 'type': 'EGG'},
             {'name': 'Extra Small Egg', 'price': 0, 'discount': 0, 'id': 950, 'type': 'EGG'},
             {'name': 'Small Animal Feces', 'price': 0, 'discount': 0, 'id': 951, 'type': 'FARM'},
             {'name': 'Human Feces', 'price': 0, 'discount': 0, 'id': 952, 'type': 'FARM'},
             {'name': 'Medium Animal Feces', 'price': 0, 'discount': 0, 'id': 953, 'type': 'FARM'},
             {'name': 'Large Animal Feces', 'price': 0, 'discount': 0, 'id': 954, 'type': 'FARM'},
             {'name': 'Massive Animal Feces', 'price': 0, 'discount': 0, 'id': 955, 'type': 'FARM'},
             {'name': 'Snow Owl Pellet', 'price': 0, 'discount': 0, 'id': 956, 'type': 'FARM'},
             {'name': 'Note', 'price': 0, 'discount': 0, 'id': 957, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Enduro Stew', 'price': 0, 'discount': 0, 'id': 958, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Lazarus Chowder', 'price': 0, 'discount': 0, 'id': 959, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Calien Soup', 'price': 0, 'discount': 0, 'id': 960, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Fria Curry', 'price': 0, 'discount': 0, 'id': 961, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Focal Chili', 'price': 0, 'discount': 0, 'id': 962, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Battle Tartare', 'price': 0, 'discount': 0, 'id': 963, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Shadow Steak Saute', 'price': 0, 'discount': 0, 'id': 964, 'type': 'RECIPE'},
             {'name': 'Notes on Rockwell Recipes', 'price': 0, 'discount': 0, 'id': 965, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Medical Brew', 'price': 0, 'discount': 0, 'id': 966, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Energy Brew', 'price': 0, 'discount': 0, 'id': 967, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Meat Jerky', 'price': 0, 'discount': 0, 'id': 968, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Decorative Coloring', 'price': 0, 'discount': 0, 'id': 969, 'type': 'RECIPE'},
             {'name': 'Rockwell Recipes: Mindwipe Tonic', 'price': 0, 'discount': 0, 'id': 970, 'type': 'RECIPE'},
             {'name': 'Wood', 'price': 0, 'discount': 0, 'id': 971, 'type': 'RESOURCE'},
             {'name': 'Stone', 'price': 0, 'discount': 0, 'id': 972, 'type': 'RESOURCE'},
             {'name': 'Metal', 'price': 0, 'discount': 0, 'id': 973, 'type': 'RESOURCE'},
             {'name': 'Hide', 'price': 0, 'discount': 0, 'id': 974, 'type': 'RESOURCE'},
             {'name': 'Chitin', 'price': 0, 'discount': 0, 'id': 975, 'type': 'RESOURCE'},
             {'name': 'Blood Pack', 'price': 0, 'discount': 0, 'id': 976, 'type': 'RESOURCE'},
             {'name': 'Fertilizer', 'price': 0, 'discount': 0, 'id': 977, 'type': 'RESOURCE'},
             {'name': 'Flint', 'price': 0, 'discount': 0, 'id': 978, 'type': 'RESOURCE'},
             {'name': 'Metal Ingot', 'price': 0, 'discount': 0, 'id': 979, 'type': 'RESOURCE'},
             {'name': 'Thatch', 'price': 0, 'discount': 0, 'id': 980, 'type': 'RESOURCE'},
             {'name': 'Fiber', 'price': 0, 'discount': 0, 'id': 981, 'type': 'RESOURCE'},
             {'name': 'Charcoal', 'price': 0, 'discount': 0, 'id': 982, 'type': 'RESOURCE'},
             {'name': 'Crystal', 'price': 0, 'discount': 0, 'id': 983, 'type': 'RESOURCE'},
             {'name': 'Sparkpowder', 'price': 0, 'discount': 0, 'id': 984, 'type': 'RESOURCE'},
             {'name': 'Gunpowder', 'price': 0, 'discount': 0, 'id': 985, 'type': 'RESOURCE'},
             {'name': 'Narcotic', 'price': 0, 'discount': 0, 'id': 986, 'type': 'RESOURCE'},
             {'name': 'Stimulant', 'price': 0, 'discount': 0, 'id': 987, 'type': 'RESOURCE'},
             {'name': 'Obsidian', 'price': 0, 'discount': 0, 'id': 988, 'type': 'RESOURCE'},
             {'name': 'Cementing Paste', 'price': 0, 'discount': 0, 'id': 989, 'type': 'RESOURCE'},
             {'name': 'Oil', 'price': 0, 'discount': 0, 'id': 990, 'type': 'RESOURCE'},
             {'name': 'Silica Pearls', 'price': 0, 'discount': 0, 'id': 991, 'type': 'RESOURCE'},
             {'name': 'Gasoline', 'price': 0, 'discount': 0, 'id': 992, 'type': 'RESOURCE'},
             {'name': 'Electronics', 'price': 0, 'discount': 0, 'id': 993, 'type': 'RESOURCE'},
             {'name': 'Polymer', 'price': 0, 'discount': 0, 'id': 994, 'type': 'RESOURCE'},
             {'name': 'Chitin or Keratin', 'price': 0, 'discount': 0, 'id': 995, 'type': 'RESOURCE'},
             {'name': 'Keratin', 'price': 0, 'discount': 0, 'id': 996, 'type': 'RESOURCE'},
             {'name': 'Rare Flower', 'price': 0, 'discount': 0, 'id': 997, 'type': 'RESOURCE'},
             {'name': 'Rare Mushroom', 'price': 0, 'discount': 0, 'id': 998, 'type': 'RESOURCE'},
             {'name': 'Re-Fertilizer', 'price': 0, 'discount': 0, 'id': 999, 'type': 'RESOURCE'},
             {'name': 'Pelt', 'price': 0, 'discount': 0, 'id': 1000, 'type': 'RESOURCE'},
             {'name': 'Wishbone', 'price': 0, 'discount': 0, 'id': 1001, 'type': 'RESOURCE'},
             {'name': 'Mistletoe', 'price': 0, 'discount': 0, 'id': 1002, 'type': 'RESOURCE'},
             {'name': 'Coal', 'price': 0, 'discount': 0, 'id': 1003, 'type': 'RESOURCE'},
             {'name': 'Birthday Candle', 'price': 0, 'discount': 0, 'id': 1004, 'type': 'RESOURCE'},
             {'name': 'ARK Anniversary Surprise Cake', 'price': 0, 'discount': 0, 'id': 1005, 'type': 'RESOURCE'},
             {'name': 'Cake Slice', 'price': 0, 'discount': 0, 'id': 1006, 'type': 'RESOURCE'},
             {'name': 'Absorbent Substrate', 'price': 0, 'discount': 0, 'id': 1007, 'type': 'RESOURCE'},
             {'name': 'Achatina Paste', 'price': 0, 'discount': 0, 'id': 1008, 'type': 'RESOURCE'},
             {'name': 'Ambergris', 'price': 0, 'discount': 0, 'id': 1009, 'type': 'RESOURCE'},
             {'name': 'Ammonite Bile', 'price': 0, 'discount': 0, 'id': 1010, 'type': 'RESOURCE'},
             {'name': 'AnglerGel', 'price': 0, 'discount': 0, 'id': 1011, 'type': 'RESOURCE'},
             {'name': 'Black Pearl', 'price': 0, 'discount': 0, 'id': 1012, 'type': 'RESOURCE'},
             {'name': 'Blue Crystalized Sap', 'price': 0, 'discount': 0, 'id': 1013, 'type': 'RESOURCE'},
             {'name': 'Blue Gem', 'price': 0, 'discount': 0, 'id': 1014, 'type': 'RESOURCE'},
             {'name': 'Charge Battery', 'price': 0, 'discount': 0, 'id': 1015, 'type': 'RESOURCE'},
             {'name': 'Clay', 'price': 0, 'discount': 0, 'id': 1016, 'type': 'RESOURCE'},
             {'name': 'Condensed Gas', 'price': 0, 'discount': 0, 'id': 1017, 'type': 'RESOURCE'},
             {'name': 'Congealed Gas Ball', 'price': 0, 'discount': 0, 'id': 1018, 'type': 'RESOURCE'},
             {'name': 'Corrupted Nodule', 'price': 0, 'discount': 0, 'id': 1019, 'type': 'RESOURCE'},
             {'name': 'Crafted Element Dust', 'price': 0, 'discount': 0, 'id': 1020, 'type': 'RESOURCE'},
             {'name': 'Deathworm Horn', 'price': 0, 'discount': 0, 'id': 1021, 'type': 'RESOURCE'},
             {'name': 'Deathworm Horn or Woolly Rhino Horn', 'price': 0, 'discount': 0, 'id': 1022, 'type': 'RESOURCE'},
             {'name': 'Dermis', 'price': 0, 'discount': 0, 'id': 1023, 'type': 'RESOURCE'},
             {'name': 'Dinosaur Bone', 'price': 0, 'discount': 0, 'id': 1024, 'type': 'RESOURCE'},
             {'name': 'Element', 'price': 0, 'discount': 0, 'id': 1025, 'type': 'RESOURCE'},
             {'name': 'Element Dust', 'price': 0, 'discount': 0, 'id': 1026, 'type': 'RESOURCE'},
             {'name': 'Element Ore', 'price': 0, 'discount': 0, 'id': 1027, 'type': 'RESOURCE'},
             {'name': 'Element Shard', 'price': 0, 'discount': 0, 'id': 1028, 'type': 'RESOURCE'},
             {'name': 'Fragmented Green Gem', 'price': 0, 'discount': 0, 'id': 1029, 'type': 'RESOURCE'},
             {'name': 'Fungal Wood', 'price': 0, 'discount': 0, 'id': 1030, 'type': 'RESOURCE'},
             {'name': 'Corrupted Wood', 'price': 0, 'discount': 0, 'id': 1031, 'type': 'RESOURCE'},
             {'name': 'Golden Nugget', 'price': 0, 'discount': 0, 'id': 1032, 'type': 'RESOURCE'},
             {'name': 'Green Gem', 'price': 0, 'discount': 0, 'id': 1033, 'type': 'RESOURCE'},
             {'name': 'High Quality Pollen', 'price': 0, 'discount': 0, 'id': 1034, 'type': 'RESOURCE'},
             {'name': 'Human Hair', 'price': 0, 'discount': 0, 'id': 1035, 'type': 'RESOURCE'},
             {'name': 'Leech Blood', 'price': 0, 'discount': 0, 'id': 1036, 'type': 'RESOURCE'},
             {'name': 'Leech Blood or Horns', 'price': 0, 'discount': 0, 'id': 1037, 'type': 'RESOURCE'},
             {'name': 'Mutagel', 'price': 0, 'discount': 0, 'id': 1038, 'type': 'RESOURCE'},
             {'name': 'Mutagen', 'price': 0, 'discount': 0, 'id': 1039, 'type': 'RESOURCE'},
             {'name': 'Oil (Tusoteuthis)', 'price': 0, 'discount': 0, 'id': 1040, 'type': 'RESOURCE'},
             {'name': 'Organic Polymer', 'price': 0, 'discount': 0, 'id': 1041, 'type': 'RESOURCE'},
             {'name': 'Pelt, Hair, or Wool', 'price': 0, 'discount': 0, 'id': 1042, 'type': 'RESOURCE'},
             {'name': 'Primal Crystal', 'price': 0, 'discount': 0, 'id': 1043, 'type': 'RESOURCE'},
             {'name': 'Preserving Salt', 'price': 0, 'discount': 0, 'id': 1044, 'type': 'RESOURCE'},
             {'name': 'Propellant', 'price': 0, 'discount': 0, 'id': 1045, 'type': 'RESOURCE'},
             {'name': 'Raw Salt', 'price': 0, 'discount': 0, 'id': 1046, 'type': 'RESOURCE'},
             {'name': 'Red Crystalized Sap', 'price': 0, 'discount': 0, 'id': 1047, 'type': 'RESOURCE'},
             {'name': 'Red Gem', 'price': 0, 'discount': 0, 'id': 1048, 'type': 'RESOURCE'},
             {'name': 'Sand', 'price': 0, 'discount': 0, 'id': 1049, 'type': 'RESOURCE'},
             {'name': 'Sap', 'price': 0, 'discount': 0, 'id': 1050, 'type': 'RESOURCE'},
             {'name': 'Scrap Metal', 'price': 0, 'discount': 0, 'id': 1051, 'type': 'RESOURCE'},
             {'name': 'Scrap Metal Ingot', 'price': 0, 'discount': 0, 'id': 1052, 'type': 'RESOURCE'},
             {'name': 'Shell Fragment', 'price': 0, 'discount': 0, 'id': 1053, 'type': 'RESOURCE'},
             {'name': 'Silicate', 'price': 0, 'discount': 0, 'id': 1054, 'type': 'RESOURCE'},
             {'name': 'Silk', 'price': 0, 'discount': 0, 'id': 1055, 'type': 'RESOURCE'},
             {'name': 'Sulfur', 'price': 0, 'discount': 0, 'id': 1056, 'type': 'RESOURCE'},
             {'name': 'Unstable Element', 'price': 0, 'discount': 0, 'id': 1057, 'type': 'RESOURCE'},
             {'name': 'Unstable Element Shard', 'price': 0, 'discount': 0, 'id': 1058, 'type': 'RESOURCE'},
             {'name': 'Wool', 'price': 0, 'discount': 0, 'id': 1059, 'type': 'RESOURCE'},
             {'name': 'Woolly Rhino Horn', 'price': 0, 'discount': 0, 'id': 1060, 'type': 'RESOURCE'},
             {'name': 'Berrybush Seeds', 'price': 0, 'discount': 0, 'id': 1061, 'type': 'SEED'},
             {'name': 'Amarberry Seed', 'price': 0, 'discount': 0, 'id': 1062, 'type': 'SEED'},
             {'name': 'Citronal Seed', 'price': 0, 'discount': 0, 'id': 1063, 'type': 'SEED'},
             {'name': 'Azulberry Seed', 'price': 0, 'discount': 0, 'id': 1064, 'type': 'SEED'},
             {'name': 'Tintoberry Seed', 'price': 0, 'discount': 0, 'id': 1065, 'type': 'SEED'},
             {'name': 'Mejoberry Seed', 'price': 0, 'discount': 0, 'id': 1066, 'type': 'SEED'},
             {'name': 'Narcoberry Seed', 'price': 0, 'discount': 0, 'id': 1067, 'type': 'SEED'},
             {'name': 'Stimberry Seed', 'price': 0, 'discount': 0, 'id': 1068, 'type': 'SEED'},
             {'name': 'Savoroot Seed', 'price': 0, 'discount': 0, 'id': 1069, 'type': 'SEED'},
             {'name': 'Longrass Seed', 'price': 0, 'discount': 0, 'id': 1070, 'type': 'SEED'},
             {'name': 'Rockarrot Seed', 'price': 0, 'discount': 0, 'id': 1071, 'type': 'SEED'},
             {'name': 'Amarberry Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1072, 'type': 'SEED'},
             {'name': 'Azulberry Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1073, 'type': 'SEED'},
             {'name': 'Tintoberry Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1074, 'type': 'SEED'},
             {'name': 'Narcoberry Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1075, 'type': 'SEED'},
             {'name': 'Stimberry Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1076, 'type': 'SEED'},
             {'name': 'Mejoberry Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1077, 'type': 'SEED'},
             {'name': 'Citronal Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1078, 'type': 'SEED'},
             {'name': 'Savoroot Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1079, 'type': 'SEED'},
             {'name': 'Longrass Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1080, 'type': 'SEED'},
             {'name': 'Rockarrot Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1081, 'type': 'SEED'},
             {'name': 'Plant Species X Seed', 'price': 0, 'discount': 0, 'id': 1082, 'type': 'SEED'},
             {'name': 'Plant Species X Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1083, 'type': 'SEED'},
             {'name': 'Plant Species Y Seed', 'price': 0, 'discount': 0, 'id': 1084, 'type': 'SEED'},
             {'name': 'Plant Species Z Seed', 'price': 0, 'discount': 0, 'id': 1085, 'type': 'SEED'},
             {'name': 'Plant Species Y Seed (instant grow)', 'price': 0, 'discount': 0, 'id': 1086, 'type': 'SEED'},
             {'name': 'Plant Species Z Seed (SpeedHack)', 'price': 0, 'discount': 0, 'id': 1087, 'type': 'SEED'},
             {'name': 'Hunter Hat Skin', 'price': 0, 'discount': 0, 'id': 1088, 'type': 'SKIN'},
             {'name': 'Rex Stomped Glasses Saddle Skin', 'price': 0, 'discount': 0, 'id': 1089, 'type': 'SKIN'},
             {'name': 'Parasaur Stylish Saddle Skin', 'price': 0, 'discount': 0, 'id': 1090, 'type': 'SKIN'},
             {'name': 'Rex Bone Helmet', 'price': 0, 'discount': 0, 'id': 1091, 'type': 'SKIN'},
             {'name': 'Dino Glasses Skin', 'price': 0, 'discount': 0, 'id': 1092, 'type': 'SKIN'},
             {'name': 'Fireworks Flaregun Skin', 'price': 0, 'discount': 0, 'id': 1093, 'type': 'SKIN'},
             {'name': 'Trike Bone Helmet Skin', 'price': 0, 'discount': 0, 'id': 1094, 'type': 'SKIN'},
             {'name': 'DodoRex Mask Skin', 'price': 0, 'discount': 0, 'id': 1095, 'type': 'SKIN'},
             {'name': 'Chibi Party Rex', 'price': 0, 'discount': 0, 'id': 1096, 'type': 'SKIN'},
             {'name': 'Chibi-Allosaurus', 'price': 0, 'discount': 0, 'id': 1097, 'type': 'SKIN'},
             {'name': 'Chibi-Ammonite', 'price': 0, 'discount': 0, 'id': 1098, 'type': 'SKIN'},
             {'name': 'Chibi-Ankylosaurus', 'price': 0, 'discount': 0, 'id': 1099, 'type': 'SKIN'},
             {'name': 'Chibi-Argentavis', 'price': 0, 'discount': 0, 'id': 1100, 'type': 'SKIN'},
             {'name': 'Chibi-Astrocetus', 'price': 0, 'discount': 0, 'id': 1101, 'type': 'SKIN'},
             {'name': 'Chibi-Baryonyx', 'price': 0, 'discount': 0, 'id': 1102, 'type': 'SKIN'},
             {'name': 'Chibi-Basilisk', 'price': 0, 'discount': 0, 'id': 1103, 'type': 'SKIN'},
             {'name': 'Chibi-Beelzebufo', 'price': 0, 'discount': 0, 'id': 1104, 'type': 'SKIN'},
             {'name': 'Chibi-Bloodstalker', 'price': 0, 'discount': 0, 'id': 1105, 'type': 'SKIN'},
             {'name': 'Chibi-Bonnet Otter', 'price': 0, 'discount': 0, 'id': 1106, 'type': 'SKIN'},
             {'name': 'Chibi-Brontosaurus', 'price': 0, 'discount': 0, 'id': 1107, 'type': 'SKIN'},
             {'name': 'Chibi-Broodmother', 'price': 0, 'discount': 0, 'id': 1108, 'type': 'SKIN'},
             {'name': 'Chibi-Bulbdog', 'price': 0, 'discount': 0, 'id': 1109, 'type': 'SKIN'},
             {'name': 'Chibi-Bunny', 'price': 0, 'discount': 0, 'id': 1110, 'type': 'SKIN'},
             {'name': 'Chibi-Carbonemys', 'price': 0, 'discount': 0, 'id': 1111, 'type': 'SKIN'},
             {'name': 'Chibi-Carno', 'price': 0, 'discount': 0, 'id': 1112, 'type': 'SKIN'},
             {'name': 'Chibi-Castroides', 'price': 0, 'discount': 0, 'id': 1113, 'type': 'SKIN'},
             {'name': 'Chibi-Cnidaria', 'price': 0, 'discount': 0, 'id': 1114, 'type': 'SKIN'},
             {'name': 'Chibi-Crystal Wyvern', 'price': 0, 'discount': 0, 'id': 1115, 'type': 'SKIN'},
             {'name': 'Chibi-Daeodon', 'price': 0, 'discount': 0, 'id': 1116, 'type': 'SKIN'},
             {'name': 'Chibi-Direbear', 'price': 0, 'discount': 0, 'id': 1117, 'type': 'SKIN'},
             {'name': 'Chibi-Direwolf', 'price': 0, 'discount': 0, 'id': 1118, 'type': 'SKIN'},
             {'name': 'Chibi-Dodo', 'price': 0, 'discount': 0, 'id': 1119, 'type': 'SKIN'},
             {'name': 'Chibi-Doedicurus', 'price': 0, 'discount': 0, 'id': 1120, 'type': 'SKIN'},
             {'name': 'Chibi-Dunkleosteus', 'price': 0, 'discount': 0, 'id': 1121, 'type': 'SKIN'},
             {'name': 'Chibi-Enforcer', 'price': 0, 'discount': 0, 'id': 1122, 'type': 'SKIN'},
             {'name': 'Chibi-Equus', 'price': 0, 'discount': 0, 'id': 1123, 'type': 'SKIN'},
             {'name': 'Chibi-Featherlight', 'price': 0, 'discount': 0, 'id': 1124, 'type': 'SKIN'},
             {'name': 'Chibi-Ferox (Large)', 'price': 0, 'discount': 0, 'id': 1125, 'type': 'SKIN'},
             {'name': 'Chibi-Ferox (Small)', 'price': 0, 'discount': 0, 'id': 1126, 'type': 'SKIN'},
             {'name': 'Chibi-Gacha Claus', 'price': 0, 'discount': 0, 'id': 1127, 'type': 'SKIN'},
             {'name': 'Chibi-Gasbag', 'price': 0, 'discount': 0, 'id': 1128, 'type': 'SKIN'},
             {'name': 'Chibi-Giganotosaurus', 'price': 0, 'discount': 0, 'id': 1129, 'type': 'SKIN'},
             {'name': 'Chibi-Gigantopithecus', 'price': 0, 'discount': 0, 'id': 1130, 'type': 'SKIN'},
             {'name': 'Chibi-Glowtail', 'price': 0, 'discount': 0, 'id': 1131, 'type': 'SKIN'},
             {'name': 'Chibi-Griffin', 'price': 0, 'discount': 0, 'id': 1132, 'type': 'SKIN'},
             {'name': 'Chibi-Iguanodon', 'price': 0, 'discount': 0, 'id': 1133, 'type': 'SKIN'},
             {'name': 'Chibi-Karkinos', 'price': 0, 'discount': 0, 'id': 1134, 'type': 'SKIN'},
             {'name': 'Chibi-Kentrosaurus', 'price': 0, 'discount': 0, 'id': 1135, 'type': 'SKIN'},
             {'name': 'Chibi-Magmasaur', 'price': 0, 'discount': 0, 'id': 1136, 'type': 'SKIN'},
             {'name': 'Chibi-Mammoth', 'price': 0, 'discount': 0, 'id': 1137, 'type': 'SKIN'},
             {'name': 'Chibi-Managarmr', 'price': 0, 'discount': 0, 'id': 1138, 'type': 'SKIN'},
             {'name': 'Chibi-Manta', 'price': 0, 'discount': 0, 'id': 1139, 'type': 'SKIN'},
             {'name': 'Chibi-Mantis', 'price': 0, 'discount': 0, 'id': 1140, 'type': 'SKIN'},
             {'name': 'Chibi-Megalania', 'price': 0, 'discount': 0, 'id': 1141, 'type': 'SKIN'},
             {'name': 'Chibi-Megaloceros', 'price': 0, 'discount': 0, 'id': 1142, 'type': 'SKIN'},
             {'name': 'Chibi-Megalodon', 'price': 0, 'discount': 0, 'id': 1143, 'type': 'SKIN'},
             {'name': 'Chibi-Megatherium', 'price': 0, 'discount': 0, 'id': 1144, 'type': 'SKIN'},
             {'name': 'Chibi-Mesopithecus', 'price': 0, 'discount': 0, 'id': 1145, 'type': 'SKIN'},
             {'name': 'Chibi-Moschops', 'price': 0, 'discount': 0, 'id': 1146, 'type': 'SKIN'},
             {'name': 'Chibi-Otter', 'price': 0, 'discount': 0, 'id': 1147, 'type': 'SKIN'},
             {'name': 'Chibi-Oviraptor', 'price': 0, 'discount': 0, 'id': 1148, 'type': 'SKIN'},
             {'name': 'Chibi-Ovis', 'price': 0, 'discount': 0, 'id': 1149, 'type': 'SKIN'},
             {'name': 'Chibi-Paraceratherium', 'price': 0, 'discount': 0, 'id': 1150, 'type': 'SKIN'},
             {'name': 'Chibi-Parasaur', 'price': 0, 'discount': 0, 'id': 1151, 'type': 'SKIN'},
             {'name': 'Chibi-Phiomia', 'price': 0, 'discount': 0, 'id': 1152, 'type': 'SKIN'},
             {'name': 'Chibi-Phoenix', 'price': 0, 'discount': 0, 'id': 1153, 'type': 'SKIN'},
             {'name': 'Chibi-Plesiosaur', 'price': 0, 'discount': 0, 'id': 1154, 'type': 'SKIN'},
             {'name': 'Chibi-Procoptodon', 'price': 0, 'discount': 0, 'id': 1155, 'type': 'SKIN'},
             {'name': 'Chibi-Pteranodon', 'price': 0, 'discount': 0, 'id': 1156, 'type': 'SKIN'},
             {'name': 'Chibi-Pulmonoscorpius', 'price': 0, 'discount': 0, 'id': 1157, 'type': 'SKIN'},
             {'name': 'Chibi-Quetzal', 'price': 0, 'discount': 0, 'id': 1158, 'type': 'SKIN'},
             {'name': 'Chibi-Raptor', 'price': 0, 'discount': 0, 'id': 1159, 'type': 'SKIN'},
             {'name': 'Chibi-Reaper', 'price': 0, 'discount': 0, 'id': 1160, 'type': 'SKIN'},
             {'name': 'Chibi-Reindeer', 'price': 0, 'discount': 0, 'id': 1161, 'type': 'SKIN'},
             {'name': 'Chibi-Rex', 'price': 0, 'discount': 0, 'id': 1162, 'type': 'SKIN'},
             {'name': 'Chibi-Rhino', 'price': 0, 'discount': 0, 'id': 1163, 'type': 'SKIN'},
             {'name': 'Chibi-Rock Drake', 'price': 0, 'discount': 0, 'id': 1164, 'type': 'SKIN'},
             {'name': 'Chibi-Rock Golem', 'price': 0, 'discount': 0, 'id': 1165, 'type': 'SKIN'},
             {'name': 'Chibi-Rollrat', 'price': 0, 'discount': 0, 'id': 1166, 'type': 'SKIN'},
             {'name': 'Chibi-Sabertooth', 'price': 0, 'discount': 0, 'id': 1167, 'type': 'SKIN'},
             {'name': 'Chibi-Sarco', 'price': 0, 'discount': 0, 'id': 1168, 'type': 'SKIN'},
             {'name': 'Chibi-Seeker', 'price': 0, 'discount': 0, 'id': 1169, 'type': 'SKIN'},
             {'name': 'Chibi-Shadowmane', 'price': 0, 'discount': 0, 'id': 1170, 'type': 'SKIN'},
             {'name': 'Chibi-Shinehorn', 'price': 0, 'discount': 0, 'id': 1171, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Brontosaurus', 'price': 0, 'discount': 0, 'id': 1172, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Carno', 'price': 0, 'discount': 0, 'id': 1173, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Giganotosaurus', 'price': 0, 'discount': 0, 'id': 1174, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Jerboa', 'price': 0, 'discount': 0, 'id': 1175, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Quetzal', 'price': 0, 'discount': 0, 'id': 1176, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Raptor', 'price': 0, 'discount': 0, 'id': 1177, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Rex', 'price': 0, 'discount': 0, 'id': 1178, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Stego', 'price': 0, 'discount': 0, 'id': 1179, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Trike', 'price': 0, 'discount': 0, 'id': 1180, 'type': 'SKIN'},
             {'name': 'Chibi-Skeletal Wyvern', 'price': 0, 'discount': 0, 'id': 1181, 'type': 'SKIN'},
             {'name': 'Chibi-Snow Owl', 'price': 0, 'discount': 0, 'id': 1182, 'type': 'SKIN'},
             {'name': 'Chibi-Spino', 'price': 0, 'discount': 0, 'id': 1183, 'type': 'SKIN'},
             {'name': 'Chibi-Stego', 'price': 0, 'discount': 0, 'id': 1184, 'type': 'SKIN'},
             {'name': 'Chibi-Tapejara', 'price': 0, 'discount': 0, 'id': 1185, 'type': 'SKIN'},
             {'name': 'Chibi-Terror Bird', 'price': 0, 'discount': 0, 'id': 1186, 'type': 'SKIN'},
             {'name': 'Chibi-Therizino', 'price': 0, 'discount': 0, 'id': 1187, 'type': 'SKIN'},
             {'name': 'Chibi-Thylacoleo', 'price': 0, 'discount': 0, 'id': 1188, 'type': 'SKIN'},
             {'name': 'Chibi-Trike', 'price': 0, 'discount': 0, 'id': 1189, 'type': 'SKIN'},
             {'name': 'Chibi-Troodon', 'price': 0, 'discount': 0, 'id': 1190, 'type': 'SKIN'},
             {'name': 'Chibi-Tropeognathus', 'price': 0, 'discount': 0, 'id': 1191, 'type': 'SKIN'},
             {'name': 'Chibi-Tusoteuthis', 'price': 0, 'discount': 0, 'id': 1192, 'type': 'SKIN'},
             {'name': 'Chibi-Unicorn', 'price': 0, 'discount': 0, 'id': 1193, 'type': 'SKIN'},
             {'name': 'Chibi-Velonasaur', 'price': 0, 'discount': 0, 'id': 1194, 'type': 'SKIN'},
             {'name': 'Chibi-Wyvern', 'price': 0, 'discount': 0, 'id': 1195, 'type': 'SKIN'},
             {'name': 'Chibi-Yutyrannus', 'price': 0, 'discount': 0, 'id': 1196, 'type': 'SKIN'},
             {'name': 'Chibi-Zombie Wyvern', 'price': 0, 'discount': 0, 'id': 1197, 'type': 'SKIN'},
             {'name': 'Pair-o-Saurs Chibi', 'price': 0, 'discount': 0, 'id': 1198, 'type': 'SKIN'},
             {'name': 'Teeny Tiny Titano', 'price': 0, 'discount': 0, 'id': 1199, 'type': 'SKIN'},
             {'name': 'White-Collar Kairuku', 'price': 0, 'discount': 0, 'id': 1200, 'type': 'SKIN'},
             {'name': 'Aberrant Helmet Skin', 'price': 0, 'discount': 0, 'id': 1201, 'type': 'SKIN'},
             {'name': 'Aberrant Sword Skin', 'price': 0, 'discount': 0, 'id': 1202, 'type': 'SKIN'},
             {'name': 'Alpha Raptor Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1203, 'type': 'SKIN'},
             {'name': 'Alpha Raptor Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1204, 'type': 'SKIN'},
             {'name': 'Araneo Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1205, 'type': 'SKIN'},
             {'name': 'Araneo Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1206, 'type': 'SKIN'},
             {'name': 'ARK Tester Hat Skin', 'price': 0, 'discount': 0, 'id': 1207, 'type': 'SKIN'},
             {'name': 'Basilisk Ghost Costume', 'price': 0, 'discount': 0, 'id': 1208, 'type': 'SKIN'},
             {'name': 'Birthday Suit Pants Skin', 'price': 0, 'discount': 0, 'id': 1209, 'type': 'SKIN'},
             {'name': 'Birthday Suit Shirt Skin', 'price': 0, 'discount': 0, 'id': 1210, 'type': 'SKIN'},
             {'name': 'Blue-Ball Winter Beanie Skin', 'price': 0, 'discount': 0, 'id': 1211, 'type': 'SKIN'},
             {'name': 'Bonnet Hat Skin', 'price': 0, 'discount': 0, 'id': 1212, 'type': 'SKIN'},
             {'name': 'Bow & Eros Skin', 'price': 0, 'discount': 0, 'id': 1213, 'type': 'SKIN'},
             {'name': 'Brachiosaurus Costume', 'price': 0, 'discount': 0, 'id': 1214, 'type': 'SKIN'},
             {'name': 'Bronto Bone Costume', 'price': 0, 'discount': 0, 'id': 1215, 'type': 'SKIN'},
             {'name': 'Bulbdog Ghost Costume', 'price': 0, 'discount': 0, 'id': 1216, 'type': 'SKIN'},
             {'name': 'Bulbdog Mask Skin', 'price': 0, 'discount': 0, 'id': 1217, 'type': 'SKIN'},
             {'name': 'Bulbdog-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1218, 'type': 'SKIN'},
             {'name': 'Bunny Ears Skin', 'price': 0, 'discount': 0, 'id': 1219, 'type': 'SKIN'},
             {'name': 'Candy Cane Club Skin', 'price': 0, 'discount': 0, 'id': 1220, 'type': 'SKIN'},
             {'name': "Captain's Hat Skin", 'price': 0, 'discount': 0, 'id': 1221, 'type': 'SKIN'},
             {'name': 'Carno Bone Costume', 'price': 0, 'discount': 0, 'id': 1222, 'type': 'SKIN'},
             {'name': 'Chieftan Hat Skin', 'price': 0, 'discount': 0, 'id': 1223, 'type': 'SKIN'},
             {'name': 'Chili Helmet Skin', 'price': 0, 'discount': 0, 'id': 1224, 'type': 'SKIN'},
             {'name': 'Chocolate Rabbit Club Skin', 'price': 0, 'discount': 0, 'id': 1225, 'type': 'SKIN'},
             {'name': 'Christmas Bola Skin', 'price': 0, 'discount': 0, 'id': 1226, 'type': 'SKIN'},
             {'name': 'Clown Mask Skin', 'price': 0, 'discount': 0, 'id': 1227, 'type': 'SKIN'},
             {'name': 'Corrupted Avatar Boots Skin', 'price': 0, 'discount': 0, 'id': 1228, 'type': 'SKIN'},
             {'name': 'Corrupted Avatar Gloves Skin', 'price': 0, 'discount': 0, 'id': 1229, 'type': 'SKIN'},
             {'name': 'Corrupted Avatar Helmet Skin', 'price': 0, 'discount': 0, 'id': 1230, 'type': 'SKIN'},
             {'name': 'Corrupted Avatar Pants Skin', 'price': 0, 'discount': 0, 'id': 1231, 'type': 'SKIN'},
             {'name': 'Corrupted Avatar Shirt Skin', 'price': 0, 'discount': 0, 'id': 1232, 'type': 'SKIN'},
             {'name': 'Corrupted Boots Skin', 'price': 0, 'discount': 0, 'id': 1233, 'type': 'SKIN'},
             {'name': 'Corrupted Chestpiece Skin', 'price': 0, 'discount': 0, 'id': 1234, 'type': 'SKIN'},
             {'name': 'Corrupted Gloves Skin', 'price': 0, 'discount': 0, 'id': 1235, 'type': 'SKIN'},
             {'name': 'Corrupted Helmet Skin', 'price': 0, 'discount': 0, 'id': 1236, 'type': 'SKIN'},
             {'name': 'Corrupted Pants Skin', 'price': 0, 'discount': 0, 'id': 1237, 'type': 'SKIN'},
             {'name': 'Crab Fest Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1238, 'type': 'SKIN'},
             {'name': 'Crab Fest Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1239, 'type': 'SKIN'},
             {'name': 'Cupid Couture Bottom Skin', 'price': 0, 'discount': 0, 'id': 1240, 'type': 'SKIN'},
             {'name': 'Cupid Couture Top Skin', 'price': 0, 'discount': 0, 'id': 1241, 'type': 'SKIN'},
             {'name': 'Cute Dino Helmet Skin', 'price': 0, 'discount': 0, 'id': 1242, 'type': 'SKIN'},
             {'name': 'Decorative Ravager Saddle Skin', 'price': 0, 'discount': 0, 'id': 1243, 'type': 'SKIN'},
             {'name': 'Dilo Mask Skin', 'price': 0, 'discount': 0, 'id': 1244, 'type': 'SKIN'},
             {'name': 'Dino Bunny Ears Skin', 'price': 0, 'discount': 0, 'id': 1245, 'type': 'SKIN'},
             {'name': 'Dino Easter Chick Hat', 'price': 0, 'discount': 0, 'id': 1246, 'type': 'SKIN'},
             {'name': 'Dino Easter Egg Hat', 'price': 0, 'discount': 0, 'id': 1247, 'type': 'SKIN'},
             {'name': 'Dino Marshmallow Hat Skin', 'price': 0, 'discount': 0, 'id': 1248, 'type': 'SKIN'},
             {'name': 'Dino Ornament Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1249, 'type': 'SKIN'},
             {'name': 'Dino Ornament Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1250, 'type': 'SKIN'},
             {'name': 'Dino Party Hat Skin', 'price': 0, 'discount': 0, 'id': 1251, 'type': 'SKIN'},
             {'name': 'Dino Santa Hat Skin', 'price': 0, 'discount': 0, 'id': 1252, 'type': 'SKIN'},
             {'name': 'Dino Uncle Sam Hat Skin', 'price': 0, 'discount': 0, 'id': 1253, 'type': 'SKIN'},
             {'name': 'Dino Witch Hat Skin', 'price': 0, 'discount': 0, 'id': 1254, 'type': 'SKIN'},
             {'name': 'Direwolf Ghost Costume', 'price': 0, 'discount': 0, 'id': 1255, 'type': 'SKIN'},
             {'name': 'Dodo Pie Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1256, 'type': 'SKIN'},
             {'name': 'Dodo Pie Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1257, 'type': 'SKIN'},
             {'name': 'Dodorex Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1258, 'type': 'SKIN'},
             {'name': 'Dodorex Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1259, 'type': 'SKIN'},
             {'name': 'Dodorex-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1260, 'type': 'SKIN'},
             {'name': 'DodoWyvern Mask Skin', 'price': 0, 'discount': 0, 'id': 1261, 'type': 'SKIN'},
             {'name': 'E4 Remote Eggsplosives Skin', 'price': 0, 'discount': 0, 'id': 1262, 'type': 'SKIN'},
             {'name': 'Easter Chick Hat', 'price': 0, 'discount': 0, 'id': 1263, 'type': 'SKIN'},
             {'name': 'Easter Egg Hat', 'price': 0, 'discount': 0, 'id': 1264, 'type': 'SKIN'},
             {'name': 'Easter Egghead Skin', 'price': 0, 'discount': 0, 'id': 1265, 'type': 'SKIN'},
             {'name': 'Fan Ballcap Skin', 'price': 0, 'discount': 0, 'id': 1266, 'type': 'SKIN'},
             {'name': 'Federation Exo Boots Skin', 'price': 0, 'discount': 0, 'id': 1267, 'type': 'SKIN'},
             {'name': 'Federation Exo Helmet Skin', 'price': 0, 'discount': 0, 'id': 1268, 'type': 'SKIN'},
             {'name': 'Federation Exo-Chestpiece Skin', 'price': 0, 'discount': 0, 'id': 1269, 'type': 'SKIN'},
             {'name': 'Federation Exo-Gloves Skin', 'price': 0, 'discount': 0, 'id': 1270, 'type': 'SKIN'},
             {'name': 'Federation Exo-leggings Skin', 'price': 0, 'discount': 0, 'id': 1271, 'type': 'SKIN'},
             {'name': 'Felt Reindeer Antlers Skin', 'price': 0, 'discount': 0, 'id': 1272, 'type': 'SKIN'},
             {'name': 'Fireworks Rocket Launcher Skin', 'price': 0, 'discount': 0, 'id': 1273, 'type': 'SKIN'},
             {'name': 'Fish Bite Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1274, 'type': 'SKIN'},
             {'name': 'Fish Bite Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1275, 'type': 'SKIN'},
             {'name': 'Floral Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1276, 'type': 'SKIN'},
             {'name': 'Floral Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1277, 'type': 'SKIN'},
             {'name': 'Flying Disc Skin', 'price': 0, 'discount': 0, 'id': 1278, 'type': 'SKIN'},
             {'name': 'Gasbags-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1279, 'type': 'SKIN'},
             {'name': 'Giga Bionic Costume', 'price': 0, 'discount': 0, 'id': 1280, 'type': 'SKIN'},
             {'name': 'Giga Poop Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1281, 'type': 'SKIN'},
             {'name': 'Giga Poop Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1282, 'type': 'SKIN'},
             {'name': 'Giganotosaurus Bone Costume', 'price': 0, 'discount': 0, 'id': 1283, 'type': 'SKIN'},
             {'name': 'Glider Suit', 'price': 0, 'discount': 0, 'id': 1284, 'type': 'SKIN'},
             {'name': 'Gray-Ball Winter Beanie Skin', 'price': 0, 'discount': 0, 'id': 1285, 'type': 'SKIN'},
             {'name': 'Green-Ball Winter Beanie Skin', 'price': 0, 'discount': 0, 'id': 1286, 'type': 'SKIN'},
             {'name': 'Grilling Spatula Skin', 'price': 0, 'discount': 0, 'id': 1287, 'type': 'SKIN'},
             {'name': 'Halo Headband Skin', 'price': 0, 'discount': 0, 'id': 1288, 'type': 'SKIN'},
             {'name': 'Headless Costume Skin', 'price': 0, 'discount': 0, 'id': 1289, 'type': 'SKIN'},
             {'name': 'Heart-shaped Shield Skin', 'price': 0, 'discount': 0, 'id': 1290, 'type': 'SKIN'},
             {'name': 'Heart-shaped Sunglasses Skin', 'price': 0, 'discount': 0, 'id': 1291, 'type': 'SKIN'},
             {'name': 'Hockey Mask Skin', 'price': 0, 'discount': 0, 'id': 1292, 'type': 'SKIN'},
             {'name': 'HomoDeus Boots Skin', 'price': 0, 'discount': 0, 'id': 1293, 'type': 'SKIN'},
             {'name': 'HomoDeus Gloves Skin', 'price': 0, 'discount': 0, 'id': 1294, 'type': 'SKIN'},
             {'name': 'HomoDeus Helmet Skin', 'price': 0, 'discount': 0, 'id': 1295, 'type': 'SKIN'},
             {'name': 'HomoDeus Pants Skin', 'price': 0, 'discount': 0, 'id': 1296, 'type': 'SKIN'},
             {'name': 'HomoDeus Shirt Skin', 'price': 0, 'discount': 0, 'id': 1297, 'type': 'SKIN'},
             {'name': 'Ice Pop-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1298, 'type': 'SKIN'},
             {'name': 'Ichthy Isles Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1299, 'type': 'SKIN'},
             {'name': 'Ichthy Isles Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1300, 'type': 'SKIN'},
             {'name': 'Jack-O-Lantern Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1301, 'type': 'SKIN'},
             {'name': 'Jack-O-Lantern Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1302, 'type': 'SKIN'},
             {'name': 'Jack-O-Lantern-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1303, 'type': 'SKIN'},
             {'name': 'Jerboa Bone Costume', 'price': 0, 'discount': 0, 'id': 1304, 'type': 'SKIN'},
             {'name': 'Jerboa Wreath Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1305, 'type': 'SKIN'},
             {'name': 'Jerboa Wreath Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1306, 'type': 'SKIN'},
             {'name': 'Love Shackles Skin', 'price': 0, 'discount': 0, 'id': 1307, 'type': 'SKIN'},
             {'name': 'Manticore Boots Skin', 'price': 0, 'discount': 0, 'id': 1308, 'type': 'SKIN'},
             {'name': 'Manticore Chestpiece Skin', 'price': 0, 'discount': 0, 'id': 1309, 'type': 'SKIN'},
             {'name': 'Manticore Gauntlets Skin', 'price': 0, 'discount': 0, 'id': 1310, 'type': 'SKIN'},
             {'name': 'Manticore Helmet Skin', 'price': 0, 'discount': 0, 'id': 1311, 'type': 'SKIN'},
             {'name': 'Manticore Leggings Skin', 'price': 0, 'discount': 0, 'id': 1312, 'type': 'SKIN'},
             {'name': 'Manticore Shield Skin', 'price': 0, 'discount': 0, 'id': 1313, 'type': 'SKIN'},
             {'name': 'Mantis Ghost Costume', 'price': 0, 'discount': 0, 'id': 1314, 'type': 'SKIN'},
             {'name': 'Marshmallow Hat Skin', 'price': 0, 'discount': 0, 'id': 1315, 'type': 'SKIN'},
             {'name': 'Master Controller Helmet Skin', 'price': 0, 'discount': 0, 'id': 1316, 'type': 'SKIN'},
             {'name': 'Meat Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1317, 'type': 'SKIN'},
             {'name': 'Meat Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1318, 'type': 'SKIN'},
             {'name': 'Megaloceros Reindeer Costume', 'price': 0, 'discount': 0, 'id': 1319, 'type': 'SKIN'},
             {'name': 'Mini-HLNA Skin', 'price': 0, 'discount': 0, 'id': 1320, 'type': 'SKIN'},
             {'name': 'Mosasaurus Bionic Costume', 'price': 0, 'discount': 0, 'id': 1321, 'type': 'SKIN'},
             {'name': 'Murder Turkey Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1322, 'type': 'SKIN'},
             {'name': 'Murder Turkey Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1323, 'type': 'SKIN'},
             {'name': 'Murder-Turkey-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1324, 'type': 'SKIN'},
             {'name': 'Nerdry Glasses Skin', 'price': 0, 'discount': 0, 'id': 1325, 'type': 'SKIN'},
             {'name': 'Noglin Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1326, 'type': 'SKIN'},
             {'name': 'Noglin Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1327, 'type': 'SKIN'},
             {'name': 'Nutcracker Slingshot Skin', 'price': 0, 'discount': 0, 'id': 1328, 'type': 'SKIN'},
             {'name': 'Onyc Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1329, 'type': 'SKIN'},
             {'name': 'Onyc Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1330, 'type': 'SKIN'},
             {'name': 'Otter Mask Skin', 'price': 0, 'discount': 0, 'id': 1331, 'type': 'SKIN'},
             {'name': 'Parasaur Bionic Costume', 'price': 0, 'discount': 0, 'id': 1332, 'type': 'SKIN'},
             {'name': 'Party Hat Skin', 'price': 0, 'discount': 0, 'id': 1333, 'type': 'SKIN'},
             {'name': 'Pilgrim Hat Skin', 'price': 0, 'discount': 0, 'id': 1334, 'type': 'SKIN'},
             {'name': 'Pitchfork Skin', 'price': 0, 'discount': 0, 'id': 1335, 'type': 'SKIN'},
             {'name': 'Poglin Mask Skin', 'price': 0, 'discount': 0, 'id': 1336, 'type': 'SKIN'},
             {'name': 'Procoptodon Bunny Costume', 'price': 0, 'discount': 0, 'id': 1337, 'type': 'SKIN'},
             {'name': 'Purple-Ball Winter Beanie Skin', 'price': 0, 'discount': 0, 'id': 1338, 'type': 'SKIN'},
             {'name': 'Purple-Ball Winter Beanie Skin (Winter Wonderland 5)', 'price': 0, 'discount': 0, 'id': 1339,
              'type': 'SKIN'},
             {'name': 'Quetzal Bionic Costume', 'price': 0, 'discount': 0, 'id': 1340, 'type': 'SKIN'},
             {'name': "Raptor 'ARK: The Animated Series' Costume", 'price': 0, 'discount': 0, 'id': 1341,
              'type': 'SKIN'},
             {'name': 'Raptor Bionic Costume', 'price': 0, 'discount': 0, 'id': 1342, 'type': 'SKIN'},
             {'name': 'Quetzalcoatlus Bone Costume', 'price': 0, 'discount': 0, 'id': 1343, 'type': 'SKIN'},
             {'name': 'Raptor Bone Costume', 'price': 0, 'discount': 0, 'id': 1344, 'type': 'SKIN'},
             {'name': 'Reaper Ghost Costume', 'price': 0, 'discount': 0, 'id': 1345, 'type': 'SKIN'},
             {'name': 'Reaper Helmet Skin', 'price': 0, 'discount': 0, 'id': 1346, 'type': 'SKIN'},
             {'name': 'Reaper Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1347, 'type': 'SKIN'},
             {'name': 'Reaper Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1348, 'type': 'SKIN'},
             {'name': 'Reaper-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1349, 'type': 'SKIN'},
             {'name': 'Red-Ball Winter Beanie Skin', 'price': 0, 'discount': 0, 'id': 1350, 'type': 'SKIN'},
             {'name': 'Rex Bionic Costume', 'price': 0, 'discount': 0, 'id': 1351, 'type': 'SKIN'},
             {'name': 'Rex Bone Costume', 'price': 0, 'discount': 0, 'id': 1352, 'type': 'SKIN'},
             {'name': 'Rex Ghost Costume', 'price': 0, 'discount': 0, 'id': 1353, 'type': 'SKIN'},
             {'name': 'Safari Hat Skin', 'price': 0, 'discount': 0, 'id': 1354, 'type': 'SKIN'},
             {'name': 'Santa Hat Skin', 'price': 0, 'discount': 0, 'id': 1355, 'type': 'SKIN'},
             {'name': "Santiago's Axe Skin", 'price': 0, 'discount': 0, 'id': 1356, 'type': 'SKIN'},
             {'name': "Santiago's Spear Skin", 'price': 0, 'discount': 0, 'id': 1357, 'type': 'SKIN'},
             {'name': 'Scary Pumpkin Helmet Skin', 'price': 0, 'discount': 0, 'id': 1358, 'type': 'SKIN'},
             {'name': 'Scary Skull Helmet Skin', 'price': 0, 'discount': 0, 'id': 1359, 'type': 'SKIN'},
             {'name': 'Scorched Spike Skin', 'price': 0, 'discount': 0, 'id': 1360, 'type': 'SKIN'},
             {'name': 'Scorched Sword Skin', 'price': 0, 'discount': 0, 'id': 1361, 'type': 'SKIN'},
             {'name': 'Scorched Torch Skin', 'price': 0, 'discount': 0, 'id': 1362, 'type': 'SKIN'},
             {'name': 'Sea Life-Print Shirt Skin', 'price': 0, 'discount': 0, 'id': 1363, 'type': 'SKIN'},
             {'name': 'Snow Owl Ghost Costume', 'price': 0, 'discount': 0, 'id': 1364, 'type': 'SKIN'},
             {'name': 'Stego Bone Costume', 'price': 0, 'discount': 0, 'id': 1365, 'type': 'SKIN'},
             {'name': 'Stegosaurus Bionic Costume', 'price': 0, 'discount': 0, 'id': 1366, 'type': 'SKIN'},
             {'name': 'Stygimoloch Costume', 'price': 0, 'discount': 0, 'id': 1367, 'type': 'SKIN'},
             {'name': 'Styracosaurus Costume', 'price': 0, 'discount': 0, 'id': 1368, 'type': 'SKIN'},
             {'name': 'Sunglasses Skin', 'price': 0, 'discount': 0, 'id': 1369, 'type': 'SKIN'},
             {'name': 'Sweet Spear Carrot Skin', 'price': 0, 'discount': 0, 'id': 1370, 'type': 'SKIN'},
             {'name': 'T-Rex Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1371, 'type': 'SKIN'},
             {'name': 'T-Rex Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1372, 'type': 'SKIN'},
             {'name': 'Teddy Bear Grenades Skin', 'price': 0, 'discount': 0, 'id': 1373, 'type': 'SKIN'},
             {'name': 'Thorny Dragon Vagabond Saddle Skin', 'price': 0, 'discount': 0, 'id': 1374, 'type': 'SKIN'},
             {'name': 'Top Hat Skin', 'price': 0, 'discount': 0, 'id': 1375, 'type': 'SKIN'},
             {'name': 'Torch Sparkler Skin', 'price': 0, 'discount': 0, 'id': 1376, 'type': 'SKIN'},
             {'name': 'Triceratops Bionic Costume', 'price': 0, 'discount': 0, 'id': 1377, 'type': 'SKIN'},
             {'name': 'Trike Bone Costume', 'price': 0, 'discount': 0, 'id': 1378, 'type': 'SKIN'},
             {'name': 'Turkey Hat Skin', 'price': 0, 'discount': 0, 'id': 1379, 'type': 'SKIN'},
             {'name': 'Turkey Leg Skin', 'price': 0, 'discount': 0, 'id': 1380, 'type': 'SKIN'},
             {'name': 'Turkey Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1381, 'type': 'SKIN'},
             {'name': 'Turkey Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1382, 'type': 'SKIN'},
             {'name': 'Ugly Bronto Sweater Skin', 'price': 0, 'discount': 0, 'id': 1383, 'type': 'SKIN'},
             {'name': 'Ugly Bulbdog Sweater Skin', 'price': 0, 'discount': 0, 'id': 1384, 'type': 'SKIN'},
             {'name': 'Ugly Carno Sweater Skin', 'price': 0, 'discount': 0, 'id': 1385, 'type': 'SKIN'},
             {'name': 'Ugly Caroling Sweater Skin', 'price': 0, 'discount': 0, 'id': 1386, 'type': 'SKIN'},
             {'name': 'Ugly Chibi Sweater Skin', 'price': 0, 'discount': 0, 'id': 1387, 'type': 'SKIN'},
             {'name': 'Ugly Cornucopia Sweater Skin', 'price': 0, 'discount': 0, 'id': 1388, 'type': 'SKIN'},
             {'name': 'Ugly T-Rex Sweater Skin', 'price': 0, 'discount': 0, 'id': 1389, 'type': 'SKIN'},
             {'name': 'Ugly Trike Sweater Skin', 'price': 0, 'discount': 0, 'id': 1390, 'type': 'SKIN'},
             {'name': 'Uncle Sam Hat Skin', 'price': 0, 'discount': 0, 'id': 1391, 'type': 'SKIN'},
             {'name': 'Vampire Dodo Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1392, 'type': 'SKIN'},
             {'name': 'Vampire Dodo Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1393, 'type': 'SKIN'},
             {'name': 'Vampire Eyes Skin', 'price': 0, 'discount': 0, 'id': 1394, 'type': 'SKIN'},
             {'name': 'Water Soaker Skin', 'price': 0, 'discount': 0, 'id': 1395, 'type': 'SKIN'},
             {'name': 'Werewolf Mask Skin', 'price': 0, 'discount': 0, 'id': 1396, 'type': 'SKIN'},
             {'name': 'Witch Hat Skin', 'price': 0, 'discount': 0, 'id': 1397, 'type': 'SKIN'},
             {'name': 'Wizard Ballcap Skin', 'price': 0, 'discount': 0, 'id': 1398, 'type': 'SKIN'},
             {'name': 'Wyvern Bone Costume', 'price': 0, 'discount': 0, 'id': 1399, 'type': 'SKIN'},
             {'name': 'Wyvern Gloves Skin', 'price': 0, 'discount': 0, 'id': 1400, 'type': 'SKIN'},
             {'name': 'Yeti Swim Bottom Skin', 'price': 0, 'discount': 0, 'id': 1401, 'type': 'SKIN'},
             {'name': 'Yeti Swim Top Skin', 'price': 0, 'discount': 0, 'id': 1402, 'type': 'SKIN'},
             {'name': 'Zip-Line Motor Attachment Skin', 'price': 0, 'discount': 0, 'id': 1403, 'type': 'SKIN'},
             {'name': 'Campfire', 'price': 0, 'discount': 0, 'id': 1404, 'type': 'STRUCTURE'},
             {'name': 'Standing Torch', 'price': 0, 'discount': 0, 'id': 1405, 'type': 'STRUCTURE'},
             {'name': 'Hide Sleeping Bag', 'price': 0, 'discount': 0, 'id': 1406, 'type': 'STRUCTURE'},
             {'name': 'Thatch Ceiling', 'price': 0, 'discount': 0, 'id': 1407, 'type': 'STRUCTURE'},
             {'name': 'Thatch Door', 'price': 0, 'discount': 0, 'id': 1408, 'type': 'STRUCTURE'},
             {'name': 'Thatch Foundation', 'price': 0, 'discount': 0, 'id': 1409, 'type': 'STRUCTURE'},
             {'name': 'Thatch Wall', 'price': 0, 'discount': 0, 'id': 1410, 'type': 'STRUCTURE'},
             {'name': 'Thatch Doorframe', 'price': 0, 'discount': 0, 'id': 1411, 'type': 'STRUCTURE'},
             {'name': 'Wooden Catwalk', 'price': 0, 'discount': 0, 'id': 1412, 'type': 'STRUCTURE'},
             {'name': 'Wooden Ceiling', 'price': 0, 'discount': 0, 'id': 1413, 'type': 'STRUCTURE'},
             {'name': 'Wooden Hatchframe', 'price': 0, 'discount': 0, 'id': 1414, 'type': 'STRUCTURE'},
             {'name': 'Wooden Door', 'price': 0, 'discount': 0, 'id': 1415, 'type': 'STRUCTURE'},
             {'name': 'Wooden Foundation', 'price': 0, 'discount': 0, 'id': 1416, 'type': 'STRUCTURE'},
             {'name': 'Wooden Ladder', 'price': 0, 'discount': 0, 'id': 1417, 'type': 'STRUCTURE'},
             {'name': 'Wooden Pillar', 'price': 0, 'discount': 0, 'id': 1418, 'type': 'STRUCTURE'},
             {'name': 'Wooden Ramp', 'price': 0, 'discount': 0, 'id': 1419, 'type': 'STRUCTURE'},
             {'name': 'Wooden Trapdoor', 'price': 0, 'discount': 0, 'id': 1420, 'type': 'STRUCTURE'},
             {'name': 'Wooden Wall', 'price': 0, 'discount': 0, 'id': 1421, 'type': 'STRUCTURE'},
             {'name': 'Wooden Doorframe', 'price': 0, 'discount': 0, 'id': 1422, 'type': 'STRUCTURE'},
             {'name': 'Wooden Windowframe', 'price': 0, 'discount': 0, 'id': 1423, 'type': 'STRUCTURE'},
             {'name': 'Wooden Window', 'price': 0, 'discount': 0, 'id': 1424, 'type': 'STRUCTURE'},
             {'name': 'Wooden Sign', 'price': 0, 'discount': 0, 'id': 1425, 'type': 'STRUCTURE'},
             {'name': 'Storage Box', 'price': 0, 'discount': 0, 'id': 1426, 'type': 'STRUCTURE'},
             {'name': 'Large Storage Box', 'price': 0, 'discount': 0, 'id': 1427, 'type': 'STRUCTURE'},
             {'name': 'Mortar and Pestle', 'price': 0, 'discount': 0, 'id': 1428, 'type': 'STRUCTURE'},
             {'name': 'Stone Irrigation Pipe - Intake', 'price': 0, 'discount': 0, 'id': 1429, 'type': 'STRUCTURE'},
             {'name': 'Stone Irrigation Pipe - Straight', 'price': 0, 'discount': 0, 'id': 1430, 'type': 'STRUCTURE'},
             {'name': 'Stone Irrigation Pipe - Inclined', 'price': 0, 'discount': 0, 'id': 1431, 'type': 'STRUCTURE'},
             {'name': 'Stone Irrigation Pipe - Intersection', 'price': 0, 'discount': 0, 'id': 1432,
              'type': 'STRUCTURE'},
             {'name': 'Stone Irrigation Pipe - Vertical', 'price': 0, 'discount': 0, 'id': 1433, 'type': 'STRUCTURE'},
             {'name': 'Stone Irrigation Pipe - Tap', 'price': 0, 'discount': 0, 'id': 1434, 'type': 'STRUCTURE'},
             {'name': 'Refining Forge', 'price': 0, 'discount': 0, 'id': 1435, 'type': 'STRUCTURE'},
             {'name': 'Smithy', 'price': 0, 'discount': 0, 'id': 1436, 'type': 'STRUCTURE'},
             {'name': 'Compost Bin', 'price': 0, 'discount': 0, 'id': 1437, 'type': 'STRUCTURE'},
             {'name': 'Cooking Pot', 'price': 0, 'discount': 0, 'id': 1438, 'type': 'STRUCTURE'},
             {'name': 'Simple Bed', 'price': 0, 'discount': 0, 'id': 1439, 'type': 'STRUCTURE'},
             {'name': 'Small Crop Plot', 'price': 0, 'discount': 0, 'id': 1440, 'type': 'STRUCTURE'},
             {'name': 'Wooden Fence Foundation', 'price': 0, 'discount': 0, 'id': 1441, 'type': 'STRUCTURE'},
             {'name': 'Dinosaur Gateway', 'price': 0, 'discount': 0, 'id': 1442, 'type': 'STRUCTURE'},
             {'name': 'Dinosaur Gate', 'price': 0, 'discount': 0, 'id': 1443, 'type': 'STRUCTURE'},
             {'name': 'Metal Catwalk', 'price': 0, 'discount': 0, 'id': 1444, 'type': 'STRUCTURE'},
             {'name': 'Metal Ceiling', 'price': 0, 'discount': 0, 'id': 1445, 'type': 'STRUCTURE'},
             {'name': 'Metal Hatchframe', 'price': 0, 'discount': 0, 'id': 1446, 'type': 'STRUCTURE'},
             {'name': 'Metal Door', 'price': 0, 'discount': 0, 'id': 1447, 'type': 'STRUCTURE'},
             {'name': 'Metal Fence Foundation', 'price': 0, 'discount': 0, 'id': 1448, 'type': 'STRUCTURE'},
             {'name': 'Metal Foundation', 'price': 0, 'discount': 0, 'id': 1449, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Gate', 'price': 0, 'discount': 0, 'id': 1450, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Gateway', 'price': 0, 'discount': 0, 'id': 1451, 'type': 'STRUCTURE'},
             {'name': 'Metal Ladder', 'price': 0, 'discount': 0, 'id': 1452, 'type': 'STRUCTURE'},
             {'name': 'Metal Pillar', 'price': 0, 'discount': 0, 'id': 1453, 'type': 'STRUCTURE'},
             {'name': 'Metal Ramp', 'price': 0, 'discount': 0, 'id': 1454, 'type': 'STRUCTURE'},
             {'name': 'Metal Trapdoor', 'price': 0, 'discount': 0, 'id': 1455, 'type': 'STRUCTURE'},
             {'name': 'Metal Wall', 'price': 0, 'discount': 0, 'id': 1456, 'type': 'STRUCTURE'},
             {'name': 'Metal Doorframe', 'price': 0, 'discount': 0, 'id': 1457, 'type': 'STRUCTURE'},
             {'name': 'Metal Windowframe', 'price': 0, 'discount': 0, 'id': 1458, 'type': 'STRUCTURE'},
             {'name': 'Metal Window', 'price': 0, 'discount': 0, 'id': 1459, 'type': 'STRUCTURE'},
             {'name': 'Fabricator', 'price': 0, 'discount': 0, 'id': 1460, 'type': 'STRUCTURE'},
             {'name': 'Water Reservoir', 'price': 0, 'discount': 0, 'id': 1461, 'type': 'STRUCTURE'},
             {'name': 'Air Conditioner', 'price': 0, 'discount': 0, 'id': 1462, 'type': 'STRUCTURE'},
             {'name': 'Electrical Generator', 'price': 0, 'discount': 0, 'id': 1463, 'type': 'STRUCTURE'},
             {'name': 'Electrical Outlet', 'price': 0, 'discount': 0, 'id': 1464, 'type': 'STRUCTURE'},
             {'name': 'Inclined Electrical Cable', 'price': 0, 'discount': 0, 'id': 1465, 'type': 'STRUCTURE'},
             {'name': 'Electrical Cable Intersection', 'price': 0, 'discount': 0, 'id': 1466, 'type': 'STRUCTURE'},
             {'name': 'Straight Electrical Cable', 'price': 0, 'discount': 0, 'id': 1467, 'type': 'STRUCTURE'},
             {'name': 'Vertical Electrical Cable', 'price': 0, 'discount': 0, 'id': 1468, 'type': 'STRUCTURE'},
             {'name': 'Lamppost', 'price': 0, 'discount': 0, 'id': 1469, 'type': 'STRUCTURE'},
             {'name': 'Refrigerator', 'price': 0, 'discount': 0, 'id': 1470, 'type': 'STRUCTURE'},
             {'name': 'Auto Turret', 'price': 0, 'discount': 0, 'id': 1471, 'type': 'STRUCTURE'},
             {'name': 'Remote Keypad', 'price': 0, 'discount': 0, 'id': 1472, 'type': 'STRUCTURE'},
             {'name': 'Metal Irrigation Pipe - Inclined', 'price': 0, 'discount': 0, 'id': 1473, 'type': 'STRUCTURE'},
             {'name': 'Metal Irrigation Pipe - Intake', 'price': 0, 'discount': 0, 'id': 1474, 'type': 'STRUCTURE'},
             {'name': 'Metal Irrigation Pipe - Intersection', 'price': 0, 'discount': 0, 'id': 1475,
              'type': 'STRUCTURE'},
             {'name': 'Metal Irrigation Pipe - Straight', 'price': 0, 'discount': 0, 'id': 1476, 'type': 'STRUCTURE'},
             {'name': 'Metal Irrigation Pipe - Tap', 'price': 0, 'discount': 0, 'id': 1477, 'type': 'STRUCTURE'},
             {'name': 'Metal Irrigation Pipe - Vertical', 'price': 0, 'discount': 0, 'id': 1478, 'type': 'STRUCTURE'},
             {'name': 'Metal Sign', 'price': 0, 'discount': 0, 'id': 1479, 'type': 'STRUCTURE'},
             {'name': 'Wooden Billboard', 'price': 0, 'discount': 0, 'id': 1480, 'type': 'STRUCTURE'},
             {'name': 'Metal Billboard', 'price': 0, 'discount': 0, 'id': 1481, 'type': 'STRUCTURE'},
             {'name': 'Medium Crop Plot', 'price': 0, 'discount': 0, 'id': 1482, 'type': 'STRUCTURE'},
             {'name': 'Large Crop Plot', 'price': 0, 'discount': 0, 'id': 1483, 'type': 'STRUCTURE'},
             {'name': 'Wooden Wall Sign', 'price': 0, 'discount': 0, 'id': 1484, 'type': 'STRUCTURE'},
             {'name': 'Metal Dinosaur Gateway', 'price': 0, 'discount': 0, 'id': 1485, 'type': 'STRUCTURE'},
             {'name': 'Metal Dinosaur Gate', 'price': 0, 'discount': 0, 'id': 1486, 'type': 'STRUCTURE'},
             {'name': 'Metal Wall Sign', 'price': 0, 'discount': 0, 'id': 1487, 'type': 'STRUCTURE'},
             {'name': 'Multi-Panel Flag', 'price': 0, 'discount': 0, 'id': 1488, 'type': 'STRUCTURE'},
             {'name': 'Spider Flag', 'price': 0, 'discount': 0, 'id': 1489, 'type': 'STRUCTURE'},
             {'name': 'Preserving Bin', 'price': 0, 'discount': 0, 'id': 1490, 'type': 'STRUCTURE'},
             {'name': 'Metal Spike Wall', 'price': 0, 'discount': 0, 'id': 1491, 'type': 'STRUCTURE'},
             {'name': 'Vault', 'price': 0, 'discount': 0, 'id': 1492, 'type': 'STRUCTURE'},
             {'name': 'Wooden Spike Wall', 'price': 0, 'discount': 0, 'id': 1493, 'type': 'STRUCTURE'},
             {'name': 'Bookshelf', 'price': 0, 'discount': 0, 'id': 1494, 'type': 'STRUCTURE'},
             {'name': 'Stone Fence Foundation', 'price': 0, 'discount': 0, 'id': 1495, 'type': 'STRUCTURE'},
             {'name': 'Stone Wall', 'price': 0, 'discount': 0, 'id': 1496, 'type': 'STRUCTURE'},
             {'name': 'Metal Water Reservoir', 'price': 0, 'discount': 0, 'id': 1497, 'type': 'STRUCTURE'},
             {'name': 'Stone Ceiling', 'price': 0, 'discount': 0, 'id': 1498, 'type': 'STRUCTURE'},
             {'name': 'Stone Hatchframe', 'price': 0, 'discount': 0, 'id': 1499, 'type': 'STRUCTURE'},
             {'name': 'Reinforced Wooden Door', 'price': 0, 'discount': 0, 'id': 1500, 'type': 'STRUCTURE'},
             {'name': 'Stone Foundation', 'price': 0, 'discount': 0, 'id': 1501, 'type': 'STRUCTURE'},
             {'name': 'Reinforced Dinosaur Gate', 'price': 0, 'discount': 0, 'id': 1502, 'type': 'STRUCTURE'},
             {'name': 'Stone Dinosaur Gateway', 'price': 0, 'discount': 0, 'id': 1503, 'type': 'STRUCTURE'},
             {'name': 'Stone Pillar', 'price': 0, 'discount': 0, 'id': 1504, 'type': 'STRUCTURE'},
             {'name': 'Stone Doorframe', 'price': 0, 'discount': 0, 'id': 1505, 'type': 'STRUCTURE'},
             {'name': 'Stone Windowframe', 'price': 0, 'discount': 0, 'id': 1506, 'type': 'STRUCTURE'},
             {'name': 'Reinforced Window', 'price': 0, 'discount': 0, 'id': 1507, 'type': 'STRUCTURE'},
             {'name': 'Reinforced Trapdoor', 'price': 0, 'discount': 0, 'id': 1508, 'type': 'STRUCTURE'},
             {'name': 'Omnidirectional Lamppost', 'price': 0, 'discount': 0, 'id': 1509, 'type': 'STRUCTURE'},
             {'name': 'Industrial Grill', 'price': 0, 'discount': 0, 'id': 1510, 'type': 'STRUCTURE'},
             {'name': 'Single Panel Flag', 'price': 0, 'discount': 0, 'id': 1511, 'type': 'STRUCTURE'},
             {'name': 'Feeding Trough', 'price': 0, 'discount': 0, 'id': 1512, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Stone Dinosaur Gateway', 'price': 0, 'discount': 0, 'id': 1513, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Reinforced Dinosaur Gate', 'price': 0, 'discount': 0, 'id': 1514, 'type': 'STRUCTURE'},
             {'name': 'Sloped Thatch Roof', 'price': 0, 'discount': 0, 'id': 1515, 'type': 'STRUCTURE'},
             {'name': 'Sloped Thatch Wall Left', 'price': 0, 'discount': 0, 'id': 1516, 'type': 'STRUCTURE'},
             {'name': 'Sloped Thatch Wall Right', 'price': 0, 'discount': 0, 'id': 1517, 'type': 'STRUCTURE'},
             {'name': 'Sloped Wooden Roof', 'price': 0, 'discount': 0, 'id': 1518, 'type': 'STRUCTURE'},
             {'name': 'Sloped Wood Wall Left', 'price': 0, 'discount': 0, 'id': 1519, 'type': 'STRUCTURE'},
             {'name': 'Sloped Wood Wall Right', 'price': 0, 'discount': 0, 'id': 1520, 'type': 'STRUCTURE'},
             {'name': 'Sloped Stone Roof', 'price': 0, 'discount': 0, 'id': 1521, 'type': 'STRUCTURE'},
             {'name': 'Sloped Stone Wall Left', 'price': 0, 'discount': 0, 'id': 1522, 'type': 'STRUCTURE'},
             {'name': 'Sloped Stone Wall Right', 'price': 0, 'discount': 0, 'id': 1523, 'type': 'STRUCTURE'},
             {'name': 'Sloped Metal Roof', 'price': 0, 'discount': 0, 'id': 1524, 'type': 'STRUCTURE'},
             {'name': 'Sloped Metal Wall Left', 'price': 0, 'discount': 0, 'id': 1525, 'type': 'STRUCTURE'},
             {'name': 'Sloped Metal Wall Right', 'price': 0, 'discount': 0, 'id': 1526, 'type': 'STRUCTURE'},
             {'name': 'Wooden Raft', 'price': 0, 'discount': 0, 'id': 1527, 'type': 'STRUCTURE'},
             {'name': 'Painting Canvas', 'price': 0, 'discount': 0, 'id': 1528, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Wall', 'price': 0, 'discount': 0, 'id': 1529, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Ceiling', 'price': 0, 'discount': 0, 'id': 1530, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Doorframe', 'price': 0, 'discount': 0, 'id': 1531, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Door', 'price': 0, 'discount': 0, 'id': 1532, 'type': 'STRUCTURE'},
             {'name': 'Sloped Greenhouse Wall Left', 'price': 0, 'discount': 0, 'id': 1533, 'type': 'STRUCTURE'},
             {'name': 'Sloped Greenhouse Wall Right', 'price': 0, 'discount': 0, 'id': 1534, 'type': 'STRUCTURE'},
             {'name': 'Sloped Greenhouse Roof', 'price': 0, 'discount': 0, 'id': 1535, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Window', 'price': 0, 'discount': 0, 'id': 1536, 'type': 'STRUCTURE'},
             {'name': 'Tek Dedicated Storage', 'price': 0, 'discount': 0, 'id': 1537, 'type': 'STRUCTURE'},
             {'name': 'Adobe Double Door', 'price': 0, 'discount': 0, 'id': 1538, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Double Door', 'price': 0, 'discount': 0, 'id': 1539, 'type': 'STRUCTURE'},
             {'name': 'Metal Double Door', 'price': 0, 'discount': 0, 'id': 1540, 'type': 'STRUCTURE'},
             {'name': 'Reinforced Double Door', 'price': 0, 'discount': 0, 'id': 1541, 'type': 'STRUCTURE'},
             {'name': 'Tek Double Door', 'price': 0, 'discount': 0, 'id': 1542, 'type': 'STRUCTURE'},
             {'name': 'Wooden Double Door', 'price': 0, 'discount': 0, 'id': 1543, 'type': 'STRUCTURE'},
             {'name': 'Adobe Double Doorframe', 'price': 0, 'discount': 0, 'id': 1544, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Double Doorframe', 'price': 0, 'discount': 0, 'id': 1545, 'type': 'STRUCTURE'},
             {'name': 'Metal Double Doorframe', 'price': 0, 'discount': 0, 'id': 1546, 'type': 'STRUCTURE'},
             {'name': 'Stone Double Doorframe', 'price': 0, 'discount': 0, 'id': 1547, 'type': 'STRUCTURE'},
             {'name': 'Tek Double Doorframe', 'price': 0, 'discount': 0, 'id': 1548, 'type': 'STRUCTURE'},
             {'name': 'Wooden Double Doorframe', 'price': 0, 'discount': 0, 'id': 1549, 'type': 'STRUCTURE'},
             {'name': 'Adobe Fence Support', 'price': 0, 'discount': 0, 'id': 1550, 'type': 'STRUCTURE'},
             {'name': 'Metal Fence Support', 'price': 0, 'discount': 0, 'id': 1551, 'type': 'STRUCTURE'},
             {'name': 'Stone Fence Support', 'price': 0, 'discount': 0, 'id': 1552, 'type': 'STRUCTURE'},
             {'name': 'Tek Fence Support', 'price': 0, 'discount': 0, 'id': 1553, 'type': 'STRUCTURE'},
             {'name': 'Wooden Fence Support', 'price': 0, 'discount': 0, 'id': 1554, 'type': 'STRUCTURE'},
             {'name': 'Large Adobe Wall', 'price': 0, 'discount': 0, 'id': 1555, 'type': 'STRUCTURE'},
             {'name': 'Large Metal Wall', 'price': 0, 'discount': 0, 'id': 1556, 'type': 'STRUCTURE'},
             {'name': 'Large Stone Wall', 'price': 0, 'discount': 0, 'id': 1557, 'type': 'STRUCTURE'},
             {'name': 'Large Tek Wall', 'price': 0, 'discount': 0, 'id': 1558, 'type': 'STRUCTURE'},
             {'name': 'Large Wooden Wall', 'price': 0, 'discount': 0, 'id': 1559, 'type': 'STRUCTURE'},
             {'name': 'Metal Irrigation Pipe - Flexible', 'price': 0, 'discount': 0, 'id': 1560, 'type': 'STRUCTURE'},
             {'name': 'Stone Irrigation Pipe - Flexible', 'price': 0, 'discount': 0, 'id': 1561, 'type': 'STRUCTURE'},
             {'name': 'Adobe Stairs', 'price': 0, 'discount': 0, 'id': 1562, 'type': 'STRUCTURE'},
             {'name': 'Metal Stairs', 'price': 0, 'discount': 0, 'id': 1563, 'type': 'STRUCTURE'},
             {'name': 'Stone Stairs', 'price': 0, 'discount': 0, 'id': 1564, 'type': 'STRUCTURE'},
             {'name': 'Tek Stairs', 'price': 0, 'discount': 0, 'id': 1565, 'type': 'STRUCTURE'},
             {'name': 'Wooden Stairs', 'price': 0, 'discount': 0, 'id': 1566, 'type': 'STRUCTURE'},
             {'name': 'Adobe Triangle Ceiling', 'price': 0, 'discount': 0, 'id': 1567, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Triangle Ceiling', 'price': 0, 'discount': 0, 'id': 1568, 'type': 'STRUCTURE'},
             {'name': 'Metal Triangle Ceiling', 'price': 0, 'discount': 0, 'id': 1569, 'type': 'STRUCTURE'},
             {'name': 'Stone Triangle Ceiling', 'price': 0, 'discount': 0, 'id': 1570, 'type': 'STRUCTURE'},
             {'name': 'Tek Triangle Ceiling', 'price': 0, 'discount': 0, 'id': 1571, 'type': 'STRUCTURE'},
             {'name': 'Wooden Triangle Ceiling', 'price': 0, 'discount': 0, 'id': 1572, 'type': 'STRUCTURE'},
             {'name': 'Adobe Triangle Foundation', 'price': 0, 'discount': 0, 'id': 1573, 'type': 'STRUCTURE'},
             {'name': 'Metal Triangle Foundation', 'price': 0, 'discount': 0, 'id': 1574, 'type': 'STRUCTURE'},
             {'name': 'Stone Triangle Foundation', 'price': 0, 'discount': 0, 'id': 1575, 'type': 'STRUCTURE'},
             {'name': 'Tek Triangle Foundation', 'price': 0, 'discount': 0, 'id': 1576, 'type': 'STRUCTURE'},
             {'name': 'Wooden Triangle Foundation', 'price': 0, 'discount': 0, 'id': 1577, 'type': 'STRUCTURE'},
             {'name': 'Adobe Triangle Roof', 'price': 0, 'discount': 0, 'id': 1578, 'type': 'STRUCTURE'},
             {'name': 'Greenhouse Triangle Roof', 'price': 0, 'discount': 0, 'id': 1579, 'type': 'STRUCTURE'},
             {'name': 'Metal Triangle Roof', 'price': 0, 'discount': 0, 'id': 1580, 'type': 'STRUCTURE'},
             {'name': 'Stone Triangle Roof', 'price': 0, 'discount': 0, 'id': 1581, 'type': 'STRUCTURE'},
             {'name': 'Tek Triangle Roof', 'price': 0, 'discount': 0, 'id': 1582, 'type': 'STRUCTURE'},
             {'name': 'Wooden Triangle Roof', 'price': 0, 'discount': 0, 'id': 1583, 'type': 'STRUCTURE'},
             {'name': 'Flexible Electrical Cable', 'price': 0, 'discount': 0, 'id': 1584, 'type': 'STRUCTURE'},
             {'name': 'Pumpkin', 'price': 0, 'discount': 0, 'id': 1585, 'type': 'STRUCTURE'},
             {'name': 'Scarecrow', 'price': 0, 'discount': 0, 'id': 1586, 'type': 'STRUCTURE'},
             {'name': 'Stolen Headstone', 'price': 0, 'discount': 0, 'id': 1587, 'type': 'STRUCTURE'},
             {'name': 'Wreath', 'price': 0, 'discount': 0, 'id': 1588, 'type': 'STRUCTURE'},
             {'name': 'Holiday Lights', 'price': 0, 'discount': 0, 'id': 1589, 'type': 'STRUCTURE'},
             {'name': 'Holiday Stocking', 'price': 0, 'discount': 0, 'id': 1590, 'type': 'STRUCTURE'},
             {'name': 'Holiday Tree', 'price': 0, 'discount': 0, 'id': 1591, 'type': 'STRUCTURE'},
             {'name': 'Snowman', 'price': 0, 'discount': 0, 'id': 1592, 'type': 'STRUCTURE'},
             {'name': 'Gift Box', 'price': 0, 'discount': 0, 'id': 1593, 'type': 'STRUCTURE'},
             {'name': 'Bunny Egg', 'price': 0, 'discount': 0, 'id': 1594, 'type': 'STRUCTURE'},
             {'name': 'Birthday Cake', 'price': 0, 'discount': 0, 'id': 1595, 'type': 'STRUCTURE'},
             {'name': 'Adobe Ceiling', 'price': 0, 'discount': 0, 'id': 1596, 'type': 'STRUCTURE'},
             {'name': 'Adobe Dinosaur Gate', 'price': 0, 'discount': 0, 'id': 1597, 'type': 'STRUCTURE'},
             {'name': 'Adobe Dinosaur Gateway', 'price': 0, 'discount': 0, 'id': 1598, 'type': 'STRUCTURE'},
             {'name': 'Adobe Door', 'price': 0, 'discount': 0, 'id': 1599, 'type': 'STRUCTURE'},
             {'name': 'Adobe Doorframe', 'price': 0, 'discount': 0, 'id': 1600, 'type': 'STRUCTURE'},
             {'name': 'Adobe Fence Foundation', 'price': 0, 'discount': 0, 'id': 1601, 'type': 'STRUCTURE'},
             {'name': 'Adobe Foundation', 'price': 0, 'discount': 0, 'id': 1602, 'type': 'STRUCTURE'},
             {'name': 'Adobe Hatchframe', 'price': 0, 'discount': 0, 'id': 1603, 'type': 'STRUCTURE'},
             {'name': 'Adobe Ladder', 'price': 0, 'discount': 0, 'id': 1604, 'type': 'STRUCTURE'},
             {'name': 'Adobe Pillar', 'price': 0, 'discount': 0, 'id': 1605, 'type': 'STRUCTURE'},
             {'name': 'Adobe Railing', 'price': 0, 'discount': 0, 'id': 1606, 'type': 'STRUCTURE'},
             {'name': 'Adobe Ramp', 'price': 0, 'discount': 0, 'id': 1607, 'type': 'STRUCTURE'},
             {'name': 'Adobe Staircase', 'price': 0, 'discount': 0, 'id': 1608, 'type': 'STRUCTURE'},
             {'name': 'Adobe Trapdoor', 'price': 0, 'discount': 0, 'id': 1609, 'type': 'STRUCTURE'},
             {'name': 'Adobe Wall', 'price': 0, 'discount': 0, 'id': 1610, 'type': 'STRUCTURE'},
             {'name': 'Adobe Window', 'price': 0, 'discount': 0, 'id': 1611, 'type': 'STRUCTURE'},
             {'name': 'Adobe Windowframe', 'price': 0, 'discount': 0, 'id': 1612, 'type': 'STRUCTURE'},
             {'name': 'Artifact Pedestal', 'price': 0, 'discount': 0, 'id': 1613, 'type': 'STRUCTURE'},
             {'name': 'Ballista Turret', 'price': 0, 'discount': 0, 'id': 1614, 'type': 'STRUCTURE'},
             {'name': 'Bee Hive', 'price': 0, 'discount': 0, 'id': 1615, 'type': 'STRUCTURE'},
             {'name': 'Beer Barrel', 'price': 0, 'discount': 0, 'id': 1616, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Adobe Dinosaur Gate', 'price': 0, 'discount': 0, 'id': 1617, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Adobe Dinosaur Gateway', 'price': 0, 'discount': 0, 'id': 1618, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Tek Gateway', 'price': 0, 'discount': 0, 'id': 1619, 'type': 'STRUCTURE'},
             {'name': 'Behemoth Tek Gate', 'price': 0, 'discount': 0, 'id': 1620, 'type': 'STRUCTURE'},
             {'name': 'Bunk Bed', 'price': 0, 'discount': 0, 'id': 1621, 'type': 'STRUCTURE'},
             {'name': 'Cannon', 'price': 0, 'discount': 0, 'id': 1622, 'type': 'STRUCTURE'},
             {'name': 'Catapult Turret', 'price': 0, 'discount': 0, 'id': 1623, 'type': 'STRUCTURE'},
             {'name': 'Chemistry Bench', 'price': 0, 'discount': 0, 'id': 1624, 'type': 'STRUCTURE'},
             {'name': 'Cloning Chamber', 'price': 0, 'discount': 0, 'id': 1625, 'type': 'STRUCTURE'},
             {'name': 'Cryofridge', 'price': 0, 'discount': 0, 'id': 1626, 'type': 'STRUCTURE'},
             {'name': 'Crystal Wyvern Queen Flag', 'price': 0, 'discount': 0, 'id': 1627, 'type': 'STRUCTURE'},
             {'name': 'Delivery Crate', 'price': 0, 'discount': 0, 'id': 1628, 'type': 'STRUCTURE'},
             {'name': 'Dino Leash', 'price': 0, 'discount': 0, 'id': 1629, 'type': 'STRUCTURE'},
             {'name': 'Dragon Flag', 'price': 0, 'discount': 0, 'id': 1630, 'type': 'STRUCTURE'},
             {'name': 'Elevator Track', 'price': 0, 'discount': 0, 'id': 1631, 'type': 'STRUCTURE'},
             {'name': 'Fish Basket', 'price': 0, 'discount': 0, 'id': 1632, 'type': 'STRUCTURE'},
             {'name': 'Gas Collector', 'price': 0, 'discount': 0, 'id': 1633, 'type': 'STRUCTURE'},
             {'name': 'Giant Adobe Hatchframe', 'price': 0, 'discount': 0, 'id': 1634, 'type': 'STRUCTURE'},
             {'name': 'Giant Adobe Trapdoor', 'price': 0, 'discount': 0, 'id': 1635, 'type': 'STRUCTURE'},
             {'name': 'Giant Metal Hatchframe', 'price': 0, 'discount': 0, 'id': 1636, 'type': 'STRUCTURE'},
             {'name': 'Giant Metal Trapdoor', 'price': 0, 'discount': 0, 'id': 1637, 'type': 'STRUCTURE'},
             {'name': 'Giant Reinforced Trapdoor', 'price': 0, 'discount': 0, 'id': 1638, 'type': 'STRUCTURE'},
             {'name': 'Giant Stone Hatchframe', 'price': 0, 'discount': 0, 'id': 1639, 'type': 'STRUCTURE'},
             {'name': 'Gorilla Flag', 'price': 0, 'discount': 0, 'id': 1640, 'type': 'STRUCTURE'},
             {'name': 'Gravestone', 'price': 0, 'discount': 0, 'id': 1641, 'type': 'STRUCTURE'},
             {'name': 'Heavy Auto Turret', 'price': 0, 'discount': 0, 'id': 1642, 'type': 'STRUCTURE'},
             {'name': 'Homing Underwater Mine', 'price': 0, 'discount': 0, 'id': 1643, 'type': 'STRUCTURE'},
             {'name': 'Industrial Cooker', 'price': 0, 'discount': 0, 'id': 1644, 'type': 'STRUCTURE'},
             {'name': 'Industrial Forge', 'price': 0, 'discount': 0, 'id': 1645, 'type': 'STRUCTURE'},
             {'name': 'Industrial Grinder', 'price': 0, 'discount': 0, 'id': 1646, 'type': 'STRUCTURE'},
             {'name': 'King Titan Flag', 'price': 0, 'discount': 0, 'id': 1647, 'type': 'STRUCTURE'},
             {'name': 'King Titan Flag (Mecha)', 'price': 0, 'discount': 0, 'id': 1648, 'type': 'STRUCTURE'},
             {'name': 'Large Elevator Platform', 'price': 0, 'discount': 0, 'id': 1649, 'type': 'STRUCTURE'},
             {'name': 'Large Taxidermy Base', 'price': 0, 'discount': 0, 'id': 1650, 'type': 'STRUCTURE'},
             {'name': 'Large Wood Elevator Platform', 'price': 0, 'discount': 0, 'id': 1651, 'type': 'STRUCTURE'},
             {'name': 'Manticore Flag', 'price': 0, 'discount': 0, 'id': 1652, 'type': 'STRUCTURE'},
             {'name': 'Medium Elevator Platform', 'price': 0, 'discount': 0, 'id': 1653, 'type': 'STRUCTURE'},
             {'name': 'Medium Taxidermy Base', 'price': 0, 'discount': 0, 'id': 1654, 'type': 'STRUCTURE'},
             {'name': 'Medium Wood Elevator Platform', 'price': 0, 'discount': 0, 'id': 1655, 'type': 'STRUCTURE'},
             {'name': 'Metal Cliff Platform', 'price': 0, 'discount': 0, 'id': 1656, 'type': 'STRUCTURE'},
             {'name': 'Metal Ocean Platform', 'price': 0, 'discount': 0, 'id': 1657, 'type': 'STRUCTURE'},
             {'name': 'Metal Railing', 'price': 0, 'discount': 0, 'id': 1658, 'type': 'STRUCTURE'},
             {'name': 'Metal Staircase', 'price': 0, 'discount': 0, 'id': 1659, 'type': 'STRUCTURE'},
             {'name': 'Metal Tree Platform', 'price': 0, 'discount': 0, 'id': 1660, 'type': 'STRUCTURE'},
             {'name': 'Minigun Turret', 'price': 0, 'discount': 0, 'id': 1661, 'type': 'STRUCTURE'},
             {'name': 'Mirror', 'price': 0, 'discount': 0, 'id': 1662, 'type': 'STRUCTURE'},
             {'name': 'Moeder Flag', 'price': 0, 'discount': 0, 'id': 1663, 'type': 'STRUCTURE'},
             {'name': 'Motorboat', 'price': 0, 'discount': 0, 'id': 1664, 'type': 'STRUCTURE'},
             {'name': 'Oil Pump', 'price': 0, 'discount': 0, 'id': 1665, 'type': 'STRUCTURE'},
             {'name': 'Plant Species Y Trap', 'price': 0, 'discount': 0, 'id': 1666, 'type': 'STRUCTURE'},
             {'name': 'Portable Rope Ladder', 'price': 0, 'discount': 0, 'id': 1667, 'type': 'STRUCTURE'},
             {'name': 'Pressure Plate', 'price': 0, 'discount': 0, 'id': 1668, 'type': 'STRUCTURE'},
             {'name': 'Rocket Turret', 'price': 0, 'discount': 0, 'id': 1669, 'type': 'STRUCTURE'},
             {'name': 'Rockwell Flag', 'price': 0, 'discount': 0, 'id': 1670, 'type': 'STRUCTURE'},
             {'name': 'Rope Ladder', 'price': 0, 'discount': 0, 'id': 1671, 'type': 'STRUCTURE'},
             {'name': 'Shag Rug', 'price': 0, 'discount': 0, 'id': 1672, 'type': 'STRUCTURE'},
             {'name': 'Sloped Adobe Roof', 'price': 0, 'discount': 0, 'id': 1673, 'type': 'STRUCTURE'},
             {'name': 'Sloped Adobe Wall Left', 'price': 0, 'discount': 0, 'id': 1674, 'type': 'STRUCTURE'},
             {'name': 'Sloped Adobe Wall Right', 'price': 0, 'discount': 0, 'id': 1675, 'type': 'STRUCTURE'},
             {'name': 'Sloped Tek Roof', 'price': 0, 'discount': 0, 'id': 1676, 'type': 'STRUCTURE'},
             {'name': 'Sloped Tek Wall Left', 'price': 0, 'discount': 0, 'id': 1677, 'type': 'STRUCTURE'},
             {'name': 'Sloped Tek Wall Right', 'price': 0, 'discount': 0, 'id': 1678, 'type': 'STRUCTURE'},
             {'name': 'Small Elevator Platform', 'price': 0, 'discount': 0, 'id': 1679, 'type': 'STRUCTURE'},
             {'name': 'Small Taxidermy Base', 'price': 0, 'discount': 0, 'id': 1680, 'type': 'STRUCTURE'},
             {'name': 'Small Wood Elevator Platform', 'price': 0, 'discount': 0, 'id': 1681, 'type': 'STRUCTURE'},
             {'name': 'Stone Cliff Platform', 'price': 0, 'discount': 0, 'id': 1682, 'type': 'STRUCTURE'},
             {'name': 'Stone Fireplace', 'price': 0, 'discount': 0, 'id': 1683, 'type': 'STRUCTURE'},
             {'name': 'Stone Railing', 'price': 0, 'discount': 0, 'id': 1684, 'type': 'STRUCTURE'},
             {'name': 'Stone Staircase', 'price': 0, 'discount': 0, 'id': 1685, 'type': 'STRUCTURE'},
             {'name': 'Tek Bridge', 'price': 0, 'discount': 0, 'id': 1686, 'type': 'STRUCTURE'},
             {'name': 'Tek Catwalk', 'price': 0, 'discount': 0, 'id': 1687, 'type': 'STRUCTURE'},
             {'name': 'Tek Ceiling', 'price': 0, 'discount': 0, 'id': 1688, 'type': 'STRUCTURE'},
             {'name': 'Tek Dinosaur Gateway', 'price': 0, 'discount': 0, 'id': 1689, 'type': 'STRUCTURE'},
             {'name': 'Tek Dinosaur Gate', 'price': 0, 'discount': 0, 'id': 1690, 'type': 'STRUCTURE'},
             {'name': 'Tek Doorframe', 'price': 0, 'discount': 0, 'id': 1691, 'type': 'STRUCTURE'},
             {'name': 'Tek Door', 'price': 0, 'discount': 0, 'id': 1692, 'type': 'STRUCTURE'},
             {'name': 'Tek Fence Foundation', 'price': 0, 'discount': 0, 'id': 1693, 'type': 'STRUCTURE'},
             {'name': 'Tek Forcefield', 'price': 0, 'discount': 0, 'id': 1694, 'type': 'STRUCTURE'},
             {'name': 'Tek Foundation', 'price': 0, 'discount': 0, 'id': 1695, 'type': 'STRUCTURE'},
             {'name': 'Tek Generator', 'price': 0, 'discount': 0, 'id': 1696, 'type': 'STRUCTURE'},
             {'name': 'Tek Hatchframe', 'price': 0, 'discount': 0, 'id': 1697, 'type': 'STRUCTURE'},
             {'name': 'Tek Jump Pad', 'price': 0, 'discount': 0, 'id': 1698, 'type': 'STRUCTURE'},
             {'name': 'Tek Ladder', 'price': 0, 'discount': 0, 'id': 1699, 'type': 'STRUCTURE'},
             {'name': 'Tek Light', 'price': 0, 'discount': 0, 'id': 1700, 'type': 'STRUCTURE'},
             {'name': 'Tek Pillar', 'price': 0, 'discount': 0, 'id': 1701, 'type': 'STRUCTURE'},
             {'name': 'Tek Railing', 'price': 0, 'discount': 0, 'id': 1702, 'type': 'STRUCTURE'},
             {'name': 'Tek Ramp', 'price': 0, 'discount': 0, 'id': 1703, 'type': 'STRUCTURE'},
             {'name': 'Tek Replicator', 'price': 0, 'discount': 0, 'id': 1704, 'type': 'STRUCTURE'},
             {'name': 'Tek Sensor', 'price': 0, 'discount': 0, 'id': 1705, 'type': 'STRUCTURE'},
             {'name': 'Tek Sleeping Pod', 'price': 0, 'discount': 0, 'id': 1706, 'type': 'STRUCTURE'},
             {'name': 'Tek Staircase', 'price': 0, 'discount': 0, 'id': 1707, 'type': 'STRUCTURE'},
             {'name': 'Tek Teleporter', 'price': 0, 'discount': 0, 'id': 1708, 'type': 'STRUCTURE'},
             {'name': 'Tek Transmitter', 'price': 0, 'discount': 0, 'id': 1709, 'type': 'STRUCTURE'},
             {'name': 'Tek Trapdoor', 'price': 0, 'discount': 0, 'id': 1710, 'type': 'STRUCTURE'},
             {'name': 'Tek Trough', 'price': 0, 'discount': 0, 'id': 1711, 'type': 'STRUCTURE'},
             {'name': 'Tek Turret', 'price': 0, 'discount': 0, 'id': 1712, 'type': 'STRUCTURE'},
             {'name': 'Tek Wall', 'price': 0, 'discount': 0, 'id': 1713, 'type': 'STRUCTURE'},
             {'name': 'Tek Windowframe', 'price': 0, 'discount': 0, 'id': 1714, 'type': 'STRUCTURE'},
             {'name': 'Tek Window', 'price': 0, 'discount': 0, 'id': 1715, 'type': 'STRUCTURE'},
             {'name': 'Tent', 'price': 0, 'discount': 0, 'id': 1716, 'type': 'STRUCTURE'},
             {'name': 'Toilet', 'price': 0, 'discount': 0, 'id': 1717, 'type': 'STRUCTURE'},
             {'name': 'Training Dummy', 'price': 0, 'discount': 0, 'id': 1718, 'type': 'STRUCTURE'},
             {'name': 'Tree Sap Tap', 'price': 0, 'discount': 0, 'id': 1719, 'type': 'STRUCTURE'},
             {'name': 'Trophy Wall-Mount', 'price': 0, 'discount': 0, 'id': 1720, 'type': 'STRUCTURE'},
             {'name': 'Vacuum Compartment Moonpool', 'price': 0, 'discount': 0, 'id': 1721, 'type': 'STRUCTURE'},
             {'name': 'Vacuum Compartment', 'price': 0, 'discount': 0, 'id': 1722, 'type': 'STRUCTURE'},
             {'name': 'Vessel', 'price': 0, 'discount': 0, 'id': 1723, 'type': 'STRUCTURE'},
             {'name': 'VR Boss Flag', 'price': 0, 'discount': 0, 'id': 1724, 'type': 'STRUCTURE'},
             {'name': 'Wall Torch', 'price': 0, 'discount': 0, 'id': 1725, 'type': 'STRUCTURE'},
             {'name': 'War Map', 'price': 0, 'discount': 0, 'id': 1726, 'type': 'STRUCTURE'},
             {'name': 'Wardrums', 'price': 0, 'discount': 0, 'id': 1727, 'type': 'STRUCTURE'},
             {'name': 'Water Well', 'price': 0, 'discount': 0, 'id': 1728, 'type': 'STRUCTURE'},
             {'name': 'Wind Turbine', 'price': 0, 'discount': 0, 'id': 1729, 'type': 'STRUCTURE'},
             {'name': 'Wood Elevator Top Switch', 'price': 0, 'discount': 0, 'id': 1730, 'type': 'STRUCTURE'},
             {'name': 'Wood Elevator Track', 'price': 0, 'discount': 0, 'id': 1731, 'type': 'STRUCTURE'},
             {'name': 'Wood Ocean Platform', 'price': 0, 'discount': 0, 'id': 1732, 'type': 'STRUCTURE'},
             {'name': 'Wooden Bench', 'price': 0, 'discount': 0, 'id': 1733, 'type': 'STRUCTURE'},
             {'name': 'Wooden Cage', 'price': 0, 'discount': 0, 'id': 1734, 'type': 'STRUCTURE'},
             {'name': 'Wooden Chair', 'price': 0, 'discount': 0, 'id': 1735, 'type': 'STRUCTURE'},
             {'name': 'Wooden Railing', 'price': 0, 'discount': 0, 'id': 1736, 'type': 'STRUCTURE'},
             {'name': 'Wooden Staircase', 'price': 0, 'discount': 0, 'id': 1737, 'type': 'STRUCTURE'},
             {'name': 'Wooden Table', 'price': 0, 'discount': 0, 'id': 1738, 'type': 'STRUCTURE'},
             {'name': 'Wooden Tree Platform', 'price': 0, 'discount': 0, 'id': 1739, 'type': 'STRUCTURE'},
             {'name': 'Plant Species X', 'price': 0, 'discount': 0, 'id': 1740, 'type': 'STRUCTURE'},
             {'name': 'Tek ATV', 'price': 0, 'discount': 0, 'id': 1741, 'type': 'STRUCTURE'},
             {'name': 'Stone Pick', 'price': 0, 'discount': 0, 'id': 1742, 'type': 'TOOL'},
             {'name': 'Stone Hatchet', 'price': 0, 'discount': 0, 'id': 1743, 'type': 'TOOL'},
             {'name': 'Metal Pick', 'price': 0, 'discount': 0, 'id': 1744, 'type': 'TOOL'},
             {'name': 'Metal Hatchet', 'price': 0, 'discount': 0, 'id': 1745, 'type': 'TOOL'},
             {'name': 'Torch', 'price': 0, 'discount': 0, 'id': 1746, 'type': 'TOOL'},
             {'name': 'Paintbrush', 'price': 0, 'discount': 0, 'id': 1747, 'type': 'TOOL'},
             {'name': 'Blood Extraction Syringe', 'price': 0, 'discount': 0, 'id': 1748, 'type': 'TOOL'},
             {'name': 'GPS', 'price': 0, 'discount': 0, 'id': 1749, 'type': 'TOOL'},
             {'name': 'Compass', 'price': 0, 'discount': 0, 'id': 1750, 'type': 'TOOL'},
             {'name': 'Radio', 'price': 0, 'discount': 0, 'id': 1751, 'type': 'TOOL'},
             {'name': 'Spyglass', 'price': 0, 'discount': 0, 'id': 1752, 'type': 'TOOL'},
             {'name': 'Metal Sickle', 'price': 0, 'discount': 0, 'id': 1753, 'type': 'TOOL'},
             {'name': 'Camera', 'price': 0, 'discount': 0, 'id': 1754, 'type': 'TOOL'},
             {'name': 'Chainsaw', 'price': 0, 'discount': 0, 'id': 1755, 'type': 'TOOL'},
             {'name': 'Electronic Binoculars', 'price': 0, 'discount': 0, 'id': 1756, 'type': 'TOOL'},
             {'name': 'Empty Cryopod', 'price': 0, 'discount': 0, 'id': 1757, 'type': 'TOOL'},
             {'name': 'Fish Net', 'price': 0, 'discount': 0, 'id': 1758, 'type': 'TOOL'},
             {'name': 'Fishing Rod', 'price': 0, 'discount': 0, 'id': 1759, 'type': 'TOOL'},
             {'name': 'Magnifying Glass', 'price': 0, 'discount': 0, 'id': 1760, 'type': 'TOOL'},
             {'name': 'Mining Drill', 'price': 0, 'discount': 0, 'id': 1761, 'type': 'TOOL'},
             {'name': 'Pliers', 'price': 0, 'discount': 0, 'id': 1762, 'type': 'TOOL'},
             {'name': 'Scissors', 'price': 0, 'discount': 0, 'id': 1763, 'type': 'TOOL'},
             {'name': 'Taxidermy Tool', 'price': 0, 'discount': 0, 'id': 1764, 'type': 'TOOL'},
             {'name': 'Tier 1 Lootcrate', 'price': 0, 'discount': 0, 'id': 1765, 'type': 'TOOL'},
             {'name': 'Tier 2 Lootcrate', 'price': 0, 'discount': 0, 'id': 1766, 'type': 'TOOL'},
             {'name': 'Tier 3 Lootcrate', 'price': 0, 'discount': 0, 'id': 1767, 'type': 'TOOL'},
             {'name': 'Whip', 'price': 0, 'discount': 0, 'id': 1768, 'type': 'TOOL'},
             {'name': 'Alpha Deathworm Trophy', 'price': 0, 'discount': 0, 'id': 1769, 'type': 'TROPHY'},
             {'name': 'Alpha Rex Trophy', 'price': 0, 'discount': 0, 'id': 1770, 'type': 'TROPHY'},
             {'name': 'Alpha Wyvern Trophy', 'price': 0, 'discount': 0, 'id': 1771, 'type': 'TROPHY'},
             {'name': 'Broodmother Trophy', 'price': 0, 'discount': 0, 'id': 1772, 'type': 'TROPHY'},
             {'name': 'Alpha Broodmother Trophy', 'price': 0, 'discount': 0, 'id': 1773, 'type': 'TROPHY'},
             {'name': 'Beta Broodmother Trophy', 'price': 0, 'discount': 0, 'id': 1774, 'type': 'TROPHY'},
             {'name': 'Gamma Broodmother Trophy', 'price': 0, 'discount': 0, 'id': 1775, 'type': 'TROPHY'},
             {'name': 'Megapithecus Trophy', 'price': 0, 'discount': 0, 'id': 1776, 'type': 'TROPHY'},
             {'name': 'Alpha Megapithecus Trophy', 'price': 0, 'discount': 0, 'id': 1777, 'type': 'TROPHY'},
             {'name': 'Beta Megapithecus Trophy', 'price': 0, 'discount': 0, 'id': 1778, 'type': 'TROPHY'},
             {'name': 'Gamma Megapithecus Trophy', 'price': 0, 'discount': 0, 'id': 1779, 'type': 'TROPHY'},
             {'name': 'Dragon Trophy', 'price': 0, 'discount': 0, 'id': 1780, 'type': 'TROPHY'},
             {'name': 'Alpha Dragon Trophy', 'price': 0, 'discount': 0, 'id': 1781, 'type': 'TROPHY'},
             {'name': 'Beta Dragon Trophy', 'price': 0, 'discount': 0, 'id': 1782, 'type': 'TROPHY'},
             {'name': 'Gamma Dragon Trophy', 'price': 0, 'discount': 0, 'id': 1783, 'type': 'TROPHY'},
             {'name': 'Manticore Trophy', 'price': 0, 'discount': 0, 'id': 1784, 'type': 'TROPHY'},
             {'name': 'Alpha Manticore Trophy', 'price': 0, 'discount': 0, 'id': 1785, 'type': 'TROPHY'},
             {'name': 'Beta Manticore Trophy', 'price': 0, 'discount': 0, 'id': 1786, 'type': 'TROPHY'},
             {'name': 'Gamma Manticore Trophy', 'price': 0, 'discount': 0, 'id': 1787, 'type': 'TROPHY'},
             {'name': 'Rockwell Trophy (Alpha)', 'price': 0, 'discount': 0, 'id': 1788, 'type': 'TROPHY'},
             {'name': 'Rockwell Trophy (Beta)', 'price': 0, 'discount': 0, 'id': 1789, 'type': 'TROPHY'},
             {'name': 'Rockwell Trophy (Gamma)', 'price': 0, 'discount': 0, 'id': 1790, 'type': 'TROPHY'},
             {'name': 'Desert Titan Trophy', 'price': 0, 'discount': 0, 'id': 1791, 'type': 'TROPHY'},
             {'name': 'Forest Titan Trophy', 'price': 0, 'discount': 0, 'id': 1792, 'type': 'TROPHY'},
             {'name': 'Ice Titan Trophy', 'price': 0, 'discount': 0, 'id': 1793, 'type': 'TROPHY'},
             {'name': 'King Titan Trophy (Alpha)', 'price': 0, 'discount': 0, 'id': 1794, 'type': 'TROPHY'},
             {'name': 'King Titan Trophy (Beta)', 'price': 0, 'discount': 0, 'id': 1795, 'type': 'TROPHY'},
             {'name': 'King Titan Trophy (Gamma)', 'price': 0, 'discount': 0, 'id': 1796, 'type': 'TROPHY'},
             {'name': 'Moeder Trophy', 'price': 0, 'discount': 0, 'id': 1797, 'type': 'TROPHY'},
             {'name': 'Gamma Moeder Trophy', 'price': 0, 'discount': 0, 'id': 1798, 'type': 'TROPHY'},
             {'name': 'Beta Moeder Trophy', 'price': 0, 'discount': 0, 'id': 1799, 'type': 'TROPHY'},
             {'name': 'Alpha Moeder Trophy', 'price': 0, 'discount': 0, 'id': 1800, 'type': 'TROPHY'},
             {'name': 'Master Controller Trophy', 'price': 0, 'discount': 0, 'id': 1801, 'type': 'TROPHY'},
             {'name': 'Crystal Wyvern Queen Trophy', 'price': 0, 'discount': 0, 'id': 1802, 'type': 'TROPHY'},
             {'name': 'Gamma Crystal Wyvern Queen Trophy', 'price': 0, 'discount': 0, 'id': 1803, 'type': 'TROPHY'},
             {'name': 'Beta Crystal Wyvern Queen Trophy', 'price': 0, 'discount': 0, 'id': 1804, 'type': 'TROPHY'},
             {'name': 'Alpha Crystal Wyvern Queen Trophy', 'price': 0, 'discount': 0, 'id': 1805, 'type': 'TROPHY'},
             {'name': "Survivor's Trophy", 'price': 0, 'discount': 0, 'id': 1806, 'type': 'TROPHY'},
             {'name': 'Survival of the Fittest Trophy: 1st Place', 'price': 0, 'discount': 0, 'id': 1807,
              'type': 'TROPHY'},
             {'name': 'Survival of the Fittest Trophy: 2nd Place', 'price': 0, 'discount': 0, 'id': 1808,
              'type': 'TROPHY'},
             {'name': 'Survival of the Fittest Trophy: 3rd Place', 'price': 0, 'discount': 0, 'id': 1809,
              'type': 'TROPHY'},
             {'name': 'SotF: Unnatural Selection Trophy: 1st Place', 'price': 0, 'discount': 0, 'id': 1810,
              'type': 'TROPHY'},
             {'name': 'SotF: Unnatural Selection Trophy: 2nd Place', 'price': 0, 'discount': 0, 'id': 1811,
              'type': 'TROPHY'},
             {'name': 'SotF: Unnatural Selection Trophy: 3rd Place', 'price': 0, 'discount': 0, 'id': 1812,
              'type': 'TROPHY'},
             {'name': 'Simple Pistol', 'price': 0, 'discount': 0, 'id': 1813, 'type': 'WEAPON'},
             {'name': 'Assault Rifle', 'price': 0, 'discount': 0, 'id': 1814, 'type': 'WEAPON'},
             {'name': 'Rocket Launcher', 'price': 0, 'discount': 0, 'id': 1815, 'type': 'WEAPON'},
             {'name': 'Bow', 'price': 0, 'discount': 0, 'id': 1816, 'type': 'WEAPON'},
             {'name': 'Grenade', 'price': 0, 'discount': 0, 'id': 1817, 'type': 'WEAPON'},
             {'name': 'C4 Remote Detonator', 'price': 0, 'discount': 0, 'id': 1818, 'type': 'WEAPON'},
             {'name': 'Improvised Explosive Device', 'price': 0, 'discount': 0, 'id': 1819, 'type': 'WEAPON'},
             {'name': 'Spear', 'price': 0, 'discount': 0, 'id': 1820, 'type': 'WEAPON'},
             {'name': 'Longneck Rifle', 'price': 0, 'discount': 0, 'id': 1821, 'type': 'WEAPON'},
             {'name': 'Slingshot', 'price': 0, 'discount': 0, 'id': 1822, 'type': 'WEAPON'},
             {'name': 'Pike', 'price': 0, 'discount': 0, 'id': 1823, 'type': 'WEAPON'},
             {'name': 'Flare Gun', 'price': 0, 'discount': 0, 'id': 1824, 'type': 'WEAPON'},
             {'name': 'Fabricated Pistol', 'price': 0, 'discount': 0, 'id': 1825, 'type': 'WEAPON'},
             {'name': 'Shotgun', 'price': 0, 'discount': 0, 'id': 1826, 'type': 'WEAPON'},
             {'name': 'Tripwire Narcotic Trap', 'price': 0, 'discount': 0, 'id': 1827, 'type': 'WEAPON'},
             {'name': 'Tripwire Alarm Trap', 'price': 0, 'discount': 0, 'id': 1828, 'type': 'WEAPON'},
             {'name': 'Pump-Action Shotgun', 'price': 0, 'discount': 0, 'id': 1829, 'type': 'WEAPON'},
             {'name': 'Crossbow', 'price': 0, 'discount': 0, 'id': 1830, 'type': 'WEAPON'},
             {'name': 'Transponder Tracker', 'price': 0, 'discount': 0, 'id': 1831, 'type': 'WEAPON'},
             {'name': 'Compound Bow', 'price': 0, 'discount': 0, 'id': 1832, 'type': 'WEAPON'},
             {'name': 'Bear Trap', 'price': 0, 'discount': 0, 'id': 1833, 'type': 'WEAPON'},
             {'name': 'Large Bear Trap', 'price': 0, 'discount': 0, 'id': 1834, 'type': 'WEAPON'},
             {'name': 'Spray Painter', 'price': 0, 'discount': 0, 'id': 1835, 'type': 'WEAPON'},
             {'name': 'Wooden Club', 'price': 0, 'discount': 0, 'id': 1836, 'type': 'WEAPON'},
             {'name': 'Poison Grenade', 'price': 0, 'discount': 0, 'id': 1837, 'type': 'WEAPON'},
             {'name': 'Fabricated Sniper Rifle', 'price': 0, 'discount': 0, 'id': 1838, 'type': 'WEAPON'},
             {'name': 'Electric Prod', 'price': 0, 'discount': 0, 'id': 1839, 'type': 'WEAPON'},
             {'name': 'Handcuffs', 'price': 0, 'discount': 0, 'id': 1840, 'type': 'WEAPON'},
             {'name': 'Admin Blink Rifle', 'price': 0, 'discount': 0, 'id': 1841, 'type': 'WEAPON'},
             {'name': 'Bola', 'price': 0, 'discount': 0, 'id': 1842, 'type': 'WEAPON'},
             {'name': 'Boomerang', 'price': 0, 'discount': 0, 'id': 1843, 'type': 'WEAPON'},
             {'name': 'Chain Bola', 'price': 0, 'discount': 0, 'id': 1844, 'type': 'WEAPON'},
             {'name': 'Charge Lantern', 'price': 0, 'discount': 0, 'id': 1845, 'type': 'WEAPON'},
             {'name': 'Climbing Pick', 'price': 0, 'discount': 0, 'id': 1846, 'type': 'WEAPON'},
             {'name': 'Cluster Grenade', 'price': 0, 'discount': 0, 'id': 1847, 'type': 'WEAPON'},
             {'name': 'Cruise Missile', 'price': 0, 'discount': 0, 'id': 1848, 'type': 'WEAPON'},
             {'name': 'Flamethrower', 'price': 0, 'discount': 0, 'id': 1849, 'type': 'WEAPON'},
             {'name': 'Flaming Spear', 'price': 0, 'discount': 0, 'id': 1850, 'type': 'WEAPON'},
             {'name': 'Glow Stick', 'price': 0, 'discount': 0, 'id': 1851, 'type': 'WEAPON'},
             {'name': 'Harpoon Launcher', 'price': 0, 'discount': 0, 'id': 1852, 'type': 'WEAPON'},
             {'name': 'Lance', 'price': 0, 'discount': 0, 'id': 1853, 'type': 'WEAPON'},
             {'name': 'Lasso', 'price': 0, 'discount': 0, 'id': 1854, 'type': 'WEAPON'},
             {'name': 'Oil Jar', 'price': 0, 'discount': 0, 'id': 1855, 'type': 'WEAPON'},
             {'name': 'Plant Species Z Fruit', 'price': 0, 'discount': 0, 'id': 1856, 'type': 'WEAPON'},
             {'name': 'Scout Remote', 'price': 0, 'discount': 0, 'id': 1857, 'type': 'WEAPON'},
             {'name': 'Smoke Grenade', 'price': 0, 'discount': 0, 'id': 1858, 'type': 'WEAPON'},
             {'name': 'Sword', 'price': 0, 'discount': 0, 'id': 1859, 'type': 'WEAPON'},
             {'name': 'Tek Claws', 'price': 0, 'discount': 0, 'id': 1860, 'type': 'WEAPON'},
             {'name': 'Tek Gravity Grenade', 'price': 0, 'discount': 0, 'id': 1861, 'type': 'WEAPON'},
             {'name': 'Tek Grenade', 'price': 0, 'discount': 0, 'id': 1862, 'type': 'WEAPON'},
             {'name': 'Tek Grenade Launcher', 'price': 0, 'discount': 0, 'id': 1863, 'type': 'WEAPON'},
             {'name': 'Tek Railgun', 'price': 0, 'discount': 0, 'id': 1864, 'type': 'WEAPON'},
             {'name': 'Tek Rifle', 'price': 0, 'discount': 0, 'id': 1865, 'type': 'WEAPON'},
             {'name': 'Tek Sword', 'price': 0, 'discount': 0, 'id': 1866, 'type': 'WEAPON'}]
    models.Product.bulk_insert(items)
