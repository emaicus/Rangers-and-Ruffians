class RnRBackground:
	def __init__(self, background_def):
		self.name = background_def['name'] 
		self.description = background_def['description'] 
		self.options = background_def['options'] 
		self.starting_equiptment = background_def['starting_equiptment']
				
	def get_markdown(self, level=None):
		ret = f'__{self.name}__  \n' if level == None else '#' * level + f' {self.name}  \n'
		ret += f'{self.description}  \n'
		ret += '  \n'
		
		for option in self.options:
			ret += f'__{option["question"]}__  \n'
			for answer in option['answers']:
				ret += f' * {answer}  \n'
			ret += '  \n'
		ret += '  \n'
		
		ret += '__Starting Equiptment__  \n'
		a_an = 'an' if self.name.lower()[0] in ['a', 'e', 'i', 'o', 'u'] else 'a'
		ret += f'As {a_an} {self.name}, you begin your journey with:  \n'
		for item in self.starting_equiptment:
			ret += f'* {item}  \n'
		ret += '  \n'
		
		return ret




