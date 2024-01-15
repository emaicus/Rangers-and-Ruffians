class RnRBackground:
	def __init__(self, background_def):
		self.name = background_def['name'] 
		self.description = background_def['description'] 
		self.options = background_def['options'] 
		self.starting_equipment = background_def['starting_equipment']

	def serialize(self):
		serial = dict()
		serial['name'] = self.name 
		serial['description'] = self.description
		serial['options'] = self.options 
		serial['starting_equipment'] = self.starting_equipment
		return serial

	def get_markdown(self, level=None):
		ret = f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
		ret += f'{self.description}  \n'
		ret += '  \n'
		
		for option in self.options:
			ret += f'__{option["question"]}__  \n'
			for i in range(len(option['answers'])):
				ret += f' {i+1}. {option["answers"][i]}    \n'
			ret += '  \n'
		ret += '  \n'
		
		ret += '__Starting Equipment__  \n'
		a_an = 'an' if self.name.lower()[0] in ['a', 'e', 'i', 'o', 'u'] else 'a'
		ret += f'As {a_an} {self.name}, you begin your journey with:  \n'
		for item in self.starting_equipment:
			ret += f'* {item}  \n'
		ret += '  \n'
		
		return ret


