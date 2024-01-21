from .RnRAbility import RnRAbility

class RnRWeapon:
	def __init__(self, weapon_def):
		self.name = weapon_def['name'] 
		self.base_stat = weapon_def['base_stat'] 
		self.gold_value = weapon_def['goldValue'] 
		self.damage_scaling = weapon_def['damage_scaling']
		self.range = weapon_def['range']
		self.harried = weapon_def['harried']
		self.handedness = weapon_def['handedness']
		
		self.abilities = list()
		for ability in weapon_def.get('abilities', []):
			self.abilities.append(RnRAbility(ability))
	
	def serialize(self):
		serial = dict()
		serial['name'] = self.name 
		serial['base_stat'] = self.base_stat 
		serial['goldValue'] = self.gold_value 
		serial['damage_scaling'] = self.damage_scaling
		serial['range'] = self.range 
		serial['harried'] = self.harried 
		serial['handedness'] = self.handedness 

		serial['abilities'] = list() 
		for ability in self.abilities:
			serial['abilities'].append(ability.serialize())
		
		return serial

	def get_markdown(self, level=None):
		ret = f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
		ret += f'__{self.handedness}, {self.base_stat}'
		ret += ', Harried__' if self.harried else '__' 
		ret += '  \n'
		
		for rng, value in self.range.items():
			ret += f'{value}ft {rng} '
		ret += '  \n'
	
		ret += '__Damage:__  \n'
		scaler = 1
		for value in ['Common', 'Mastercraft 1', 'Mastercraft 2']:
			ret += f' *  {value}: Priced at {self.gold_value * scaler}, deals {self.damage_scaling[value]} {self.damage_scaling["damage_type"]} damage  \n'
			scaler *= 10
		ret += '  \n'

		ret += '__Abilities:__  \n'
		for ability in self.abilities:
			ability_level = level + 1 if level is not None else None
			ret += ability.get_markdown(level=None, succinct=True)
		ret += '  \n'
		return ret
	




