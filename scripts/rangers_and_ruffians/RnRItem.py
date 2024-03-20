from .RnRAbility import RnRAbility

class RnRItem:
	def __init__(self, item_def):
		self.name = item_def['name'] 
		self.gold_value = item_def['goldValue'] 
		self.type = item_def['type']
		self.subtype = item_def.get('subtype', '')
		self.ability = RnRAbility(item_def['ability'])
	

    

	def serialize(self):
		serial = dict()
		serial['name'] = self.name 
		serial['goldValue'] = self.gold_value 
		serial['type'] = self.type
		serial['subtype'] = self.subtype
		serial['ability'] = self.ability.serialize()
		
		return serial

