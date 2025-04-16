import wx
class TranslatorAdaptiveView():
	def __init__(self, data_en, data_ru):
		self.array_words_english = data_en
		self.array_words_russian = data_ru
		
		self.app = wx.App()
		self.frame = wx.Frame(None, title="Translator", size=(600,400))
		self.panel = wx.Panel(self.frame)
		self.btn = wx.Button(self.panel, label="click", pos=(100,100))
		self.frame.show()

	def run(self):
		self.app.MainLoop()

