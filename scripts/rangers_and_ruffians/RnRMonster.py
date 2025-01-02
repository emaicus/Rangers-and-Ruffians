from .RnRAbility import RnRAbility

class RnRMonster:
	def __init__(self, monster_def):
		self.name = monster_def['name'] 
		self.type = monster_def['metadata']['type']
		self.tier = monster_def['metadata']['tier']
		self.monster_family = monster_def['metadata'].get('monster_family', self.name)
		self.monster_class = monster_def['metadata']['monster_class']
		self.full_type = f"{self.tier} {self.type}"
		
		self.summons = monster_def['summons']
		self.stats = monster_def['stats']
		self.health = self.stats['health']
		self.armor = self.stats['armor']
		self.spell_power = 'TMP_SPELL_POWER' #stats['spell_power']
		self.speed = self.stats['speed']
		self.stat_bonus = self.stats['stat_bonus']
		self.size = self.stats['size']

		moveset = monster_def['moveset']
		self.moveset = dict()
		self.moveset['actions_per_turn'] = moveset['actions_per_turn']

		for action_type in ['passive_abilities', 'combat_actions', 'villain_actions', 'lair_actions', 'dynamic_actions']:
			self.moveset[action_type] = list()
			for ability in moveset.get(action_type, []):
				self.moveset[action_type].append(RnRAbility(ability))
			
	def serialize(self):
		serial = dict()
		serial['metadata'] = dict()
		serial['name'] = self.name
		serial['metadata']['type'] = self.type 
		serial['metadata']['tier'] = self.tier 
		serial['metadata']['monster_family'] = self.monster_family 
		serial['metadata']['monster_class'] = self.monster_class 
		serial['metadata']['full_type'] = self.full_type 

		serial['summons'] = self.summons
		serial['stats'] = self.stats 
		
		serial['moveset'] = dict()
		serial['moveset']['actions_per_turn'] = self.moveset['actions_per_turn']
		
		for action_type in ['passive_abilities', 'combat_actions', 'villain_actions', 'lair_actions', 'dynamic_actions']:
			serial['moveset'][action_type] = list()
			for ability in self.moveset.get(action_type, []):
				serial['moveset'][action_type].append(ability.serialize())

		return serial


	def get_markdown(self, level=None):
		ret = f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
		ability_header_level = None if level is None else level + 1
		ability_level = None if level is None else level + 2
		ret += f'__{self.full_type}__'
		
		summon_str = ''
		for summon, is_summon in self.summons.items():
			if is_summon:
				summon_str += f' {summon.title()}'
		ret += f'{summon_str}  \n'
		
		ret += f'__Health:__ {self.health} __Armor:__ {self.armor} __Spell Power:__ {self.spell_power} __Stat Bonus:__ {self.stat_bonus}  \n'
		
		speed_str = ''
		for speed_type, speed_value in self.speed.items():
			speed_str += f' {speed_type.title()} {speed_value}ft'
		ret += f'__Movement:__ {speed_str}  \n'

		if len(self.moveset['passive_abilities']) > 0:
			ret += f'{ability_header_level * "#"} Passive Abilities  \n'
		for passive_ability in self.moveset['passive_abilities']:
			ret += passive_ability.get_markdown(level=ability_level, succinct=True)
		ret += '  \n'
		
		if len(self.moveset['combat_actions']) > 0:
			ret += f'{ability_header_level * "#"} Combat Actions  \n'
			action_or_actions = "action" if self.moveset['actions_per_turn'] == 1 else 'actions'
			ret += f"This creature can take {self.moveset['actions_per_turn']} {action_or_actions} per turn.  \n"
		for action in self.moveset['combat_actions']:
			ret += action.get_markdown(level=ability_level, succinct=True)
		ret += '  \n'
		
		return ret

	



