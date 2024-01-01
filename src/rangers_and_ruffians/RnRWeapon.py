from .RnRAbility import RnRAbility

class RnRWeapon:
	def __init__(self, weapon_def):
		self.name = weapon_def['name'] 
		self.base_stat = weapon_def['base_stat'] 
		self.gold_value = weapon_def['value'] 
		self.damage_scaling = weapon_def['damage_scaling']
		self.range = weapon_def['range']
		self.harried = weapon_def['harried']
		self.handedness = weapon_def['handedness']
		
		self.abilities = list()
		for ability in weapon_def.get('abilities', []):
			self.abilities.append(RnRAbility(ability))
			
	def get_markdown(self, level=None):
		ret = f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
		ret += f'__{self.handedness}, {self.base_stat}'
		ret += ', Harried__' if self.harried else '__' 
		ret += '  \n'
		
		for rng, value in self.range.items():
			ret += f'{value}ft {rng} '
		ret += '  \n'
	
		ret += '__Damage:__  \n'
		for value in ['Common', 'Mastercraft 1', 'Mastercraft 2']:
			ret += f' *  {value}: Priced at {self.gold_value}, deals {self.damage_scaling[value]} {self.damage_scaling["damage_type"]} damage  \n'
		ret += '  \n'

		ret += '__Abilities:__  \n'
		for ability in self.abilities:
			ability_level = level + 1 if level is not None else None
			ret += ability.get_markdown(level=None, succinct=True)
		ret += '  \n'
		return ret



