from models.database_model import *
from views.translator_adaptive_view import *

class TranslatorController():
	def __init__(self):
		self.database = DatabaseTxt(CONST_NAMEFILE_DATABASE_TXT)
		data_en = self.database.get_all_en()
		data_ru = self.database.get_all_ru()
		self.view = TranslatorAdaptiveView(data_en, data_ru)

	
	def run(self):
		self.view.run()