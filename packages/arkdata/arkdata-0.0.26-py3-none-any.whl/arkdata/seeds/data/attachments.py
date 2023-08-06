from arkdata import models


def backup_seed():
	# Keep if need to reformat, change, or enhance
	models.Attachment.new(id=203, name='Silencer Attachment', stack_size=1, class_name='PrimalItemWeaponAttachment_Silencer_C', blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Silencer.PrimalItemWeaponAttachment_Silencer\'"', url='https://ark.fandom.com/wiki/Silencer_Attachment', description='The lubricated materials in this silencer slow the gases released from a gunshot, muffling the sounds. Attach this to a supporting weapon for reduced noise when firing.', image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Silencer_Attachment.png')
	models.Attachment.new(id=137, name='Scope Attachment', stack_size=1, class_name='PrimalItemWeaponAttachment_Scope_C', blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Scope.PrimalItemWeaponAttachment_Scope\'"', url='https://ark.fandom.com/wiki/Scope_Attachment', description='The carefully shaped crystal lenses in this scope grant the user a telescopic aim when firing. Attach this to a supporting weapon to gain more accurate aiming.', image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b3/Scope_Attachment.png')
	models.Attachment.new(id=216, name='Laser Attachment', stack_size=1, class_name='PrimalItemWeaponAttachment_Laser_C', blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Laser.PrimalItemWeaponAttachment_Laser\'"', url='https://ark.fandom.com/wiki/Laser_Attachment', description='This advanced aiming device places a red dot where the weapon is pointed. Attach this to a supporting weapon to add a laser sight.', image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b3/Laser_Attachment.png')
	models.Attachment.new(id=215, name='Holo-Scope Attachment', stack_size=1, class_name='PrimalItemWeaponAttachment_HoloScope_C', blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_HoloScope.PrimalItemWeaponAttachment_HoloScope\'"', url='https://ark.fandom.com/wiki/Holo-Scope_Attachment', description='The carefully shaped crystal lenses in this scope grant the user a telescopic aim when firing. Attach this to a supporting weapon to gain more accurate aiming.', image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b3/Scope_Attachment.png')
	models.Attachment.new(id=202, name='Flashlight Attachment', stack_size=1, class_name='PrimalItemWeaponAttachment_Flashlight_C', blueprint='"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Flashlight.PrimalItemWeaponAttachment_Flashlight\'"', url='https://ark.fandom.com/wiki/Flashlight_Attachment', description='This flashlight sheds light out in a wide area, but makes you easier to see too. Attach this to a supporting weapon to shine light from a weapon.', image_url='https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a3/Flashlight_Attachment.png')

	items = [item.to_json() for item in models.Attachment.all()]
	print(items)


def seed():
	items = [
		{
			'stack_size': 1,
			'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Scope.PrimalItemWeaponAttachment_Scope\'"',
			'name': 'Scope Attachment',
			'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b3/Scope_Attachment.png',
			'class_name': 'PrimalItemWeaponAttachment_Scope_C', 'id': 137,
			'description': 'The carefully shaped crystal lenses in this scope grant the user a telescopic aim when firing. Attach this to a supporting weapon to gain more accurate aiming.',
			'url': 'https://ark.fandom.com/wiki/Scope_Attachment'
		},
		{
			'stack_size': 1,
			'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Flashlight.PrimalItemWeaponAttachment_Flashlight\'"',
			'name': 'Flashlight Attachment',
			'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/a/a3/Flashlight_Attachment.png',
			'class_name': 'PrimalItemWeaponAttachment_Flashlight_C',
			'id': 202,
			'description': 'This flashlight sheds light out in a wide area, but makes you easier to see too. Attach this to a supporting weapon to shine light from a weapon.',
			'url': 'https://ark.fandom.com/wiki/Flashlight_Attachment'
		},
		{
			'stack_size': 1,
			'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Silencer.PrimalItemWeaponAttachment_Silencer\'"',
			'name': 'Silencer Attachment',
			'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/3/39/Silencer_Attachment.png',
			'class_name': 'PrimalItemWeaponAttachment_Silencer_C', 'id': 203,
			'description': 'The lubricated materials in this silencer slow the gases released from a gunshot, muffling the sounds. Attach this to a supporting weapon for reduced noise when firing.',
			'url': 'https://ark.fandom.com/wiki/Silencer_Attachment'},
		{
			'stack_size': 1,
			'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_HoloScope.PrimalItemWeaponAttachment_HoloScope\'"',
			'name': 'Holo-Scope Attachment',
			'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b3/Scope_Attachment.png',
			'class_name': 'PrimalItemWeaponAttachment_HoloScope_C',
			'id': 215,
			'description': 'The carefully shaped crystal lenses in this scope grant the user a telescopic aim when firing. Attach this to a supporting weapon to gain more accurate aiming.',
			'url': 'https://ark.fandom.com/wiki/Holo-Scope_Attachment'
		},
		{
			'stack_size': 1,
			'blueprint': '"Blueprint\'/Game/PrimalEarth/CoreBlueprints/Items/WeaponAttachments/PrimalItemWeaponAttachment_Laser.PrimalItemWeaponAttachment_Laser\'"',
			'name': 'Laser Attachment',
			'image_url': 'https://static.wikia.nocookie.net/arksurvivalevolved_gamepedia/images/b/b3/Laser_Attachment.png',
			'class_name': 'PrimalItemWeaponAttachment_Laser_C', 'id': 216,
			'description': 'This advanced aiming device places a red dot where the weapon is pointed. Attach this to a supporting weapon to add a laser sight.',
			'url': 'https://ark.fandom.com/wiki/Laser_Attachment'
		}
	]
	models.Attachment.bulk_insert(items)

