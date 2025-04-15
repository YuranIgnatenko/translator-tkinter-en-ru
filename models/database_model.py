CONST_NAMEFILE_DATABASE_TXT = "data/database.txt"

class DatabaseTxt():
	def __init__(self, namefile:str):
		self.data_en_ru = {}
		self.data_ru_en = {}
		self.load_data(namefile)

	def load_data(self, namefile:str) -> None:
		with open(namefile, 'r', encoding='utf-8') as file:
			temp_data = file.read().split("\n")
			for row in temp_data:
				en, ru = row.split("=")[0],row.split("=")[1]
				en, ru = en.strip(), ru.strip()
				self.data_en_ru[en] = ru
				self.data_ru_en[ru] = en

	def get_ru(self, en:str) -> str:
		return self.data_ru_en[en]

	def get_en(self, ru:str) -> str:
		return self.data_en_ru[ru]
	
	def get_all_en(self) -> list[str]:
		return self.data_en_ru.items()
	
	def get_all_ru(self) -> list[str]:
		return self.data_ru_en.items()


# dbtxt = DatabaseTxt()
# dbtxt.load_data()
# print(dbtxt.data_ru_en)