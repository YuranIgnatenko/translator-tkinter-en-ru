from tkinter import*
from tkinter.messagebox import showinfo

class Window():
	def __init__(self):
		self.root = Tk()
		self.root.geometry("1000x500+50+0")
		self.root.title('TRANSLATOR - ENGLISH - RUSSIAN - FOR - CODER.py')
		self.root['bg'] = 'cyan'

		text = open("dictionary.txt", 'r', encoding='utf-8')
		dict_words = text.read()
		self.array_words_all = dict_words.split("\n")
		self.array_words_english = []
		self.array_words_russian = []

		# self.run_en = True
		# self.run_ru = True

		for word in self.array_words_all:
			separator = word.index('=')
			word_en = word[0:separator]
			word_ru = word[separator+1:]
			self.array_words_english.append(word_en)
			self.array_words_russian.append(word_ru)

		self.select_arr = self.array_words_english
		self.select_arr_reverse = self.array_words_russian
		self.new_know_word = ''
		self.user_world = ''
		self.text_output_translate = 'Not found word'
		self.counter_word = len(self.array_words_english)
		self.theme_relief = 'groove'
		self.theme_bd = 4
		self.theme_bd_name = 2

	def init_names_elements(self):
		self.name_list = Label(self.root, text='Words from dictinary:',
							   relief=self.theme_relief,bd=self.theme_bd_name,
							   bg='violet')
		self.name_list.place(x=15,y=3,width=150,height=20)
		self.name_counter = Label(self.root, text=('Words all:  '+str(self.counter_word)),
							   relief=self.theme_relief, bd=self.theme_bd_name,
								bg='violet')
		self.name_counter.place(x=355, y=3, width=150, height=20)
		self.name_entry = Label(self.root, text='Enter your word:',
								relief=self.theme_relief,bd=self.theme_bd_name,
								bg='violet')
		self.name_entry.place(x=15,y=413,width=110,height=20)
		self.name_settings = Label(self.root, text='Selected language inputing:',
								relief=self.theme_relief,bd=self.theme_bd_name,
								bg='violet')
		self.name_settings.place(x=525,y=3,width=190,height=20)
		self.name_know = Label(self.root, text='Knows word:',
								relief=self.theme_relief,bd=self.theme_bd_name,
							   	bg='violet')
		self.name_know.place(x=525,y=113,width=115,height=20)
		self.name_translate = Label(self.root, text='Translate word:',
								relief=self.theme_relief,bd=self.theme_bd_name,
								bg='violet')
		self.name_translate.place(x=525,y=277,width=115,height=20)
		self.name_btns = Label(self.root, text='Constrols:',
								relief=self.theme_relief,bd=self.theme_bd_name,
							    bg='violet')
		self.name_btns.place(x=525,y=345,width=115,height=20)


	def init_elements_frames(self):
		self.frame_list = Frame(self.root,relief=self.theme_relief,bd=self.theme_bd)
		self.frame_list.place(x=10,y=10,width=500,height=400)

		self.frame_user_entry = Frame(self.root,relief=self.theme_relief,bd=self.theme_bd)
		self.frame_user_entry.place(x=10,y=420,width=500,height=70)

		self.frame_other = Frame(self.root,relief=self.theme_relief,bd=self.theme_bd)
		self.frame_other.place(x=520,y=10,width=470,height=480)

	def init_elements_list_words(self):
		self.list_words = Listbox(self.frame_list,font='consolas 20', selectmode=SINGLE)
		for word in self.array_words_english:
			self.list_words.insert(END, word)
		self.list_words.place(x=10,y=10,width=470,height=370)

	def init_elements_entry_user(self):
		self.entry_user_word = Entry(self.frame_user_entry, font='consolas 24')
		self.entry_user_word.place(x=10,y=10,width=470,height=40)

	def init_elements_settings(self):
		self.ch_en = IntVar()
		self.ch_en.set(0)
		self.ch_ru = IntVar()
		self.ch_ru.set(0)
		self.lang_en = Checkbutton(self.frame_other,text='EN',
								   font='consolas 15',variable=self.ch_en,
								   relief=self.theme_relief,bd=self.theme_bd)
		self.lang_en.place(x=10,y=10,width=440,height=40)
		self.lang_ru = Checkbutton(self.frame_other,text='RU',
								   font='consolas 15',variable=self.ch_ru,
								   relief=self.theme_relief,bd=self.theme_bd)
		self.lang_ru.place(x=10,y=50,width=440,height=40)

	def init_elements_translate(self):
		self.text_know = Text(self.frame_other, font='consolas 10')
		self.text_know.place(x=10,y=120,width=440,height=140)
		self.text_translate = Text(self.frame_other, font='consolas 24')
		self.text_translate.place(x=10,y=280,width=440,height=50)

	def init_elements_buttons(self):
		self.btn_apply = Button(self.frame_other, text='Apply settings',
								relief=self.theme_relief,bd=self.theme_bd,
								font='consolas 15', command = self.command_apply_settings)
		self.btn_apply.place(x=10,y=350,width=440,height=40)

		self.btn_info = Button(self.frame_other, text='Information',
							   relief=self.theme_relief,bd=self.theme_bd,
							   font='consolas 15', command=self.command_information)
		self.btn_info.place(x=10,y=390,width=440,height=40)

		self.btn_open_dict = Button(self.frame_other, text='Add word',
									relief=self.theme_relief,bd=self.theme_bd,
									font='consolas 15', command=self.command_add_word)
		self.btn_open_dict.place(x=10,y=430,width=440,height=40)


	def command_add_word(self):
		r = Toplevel()
		r.geometry("200x150+500+300")
		r.title("ADD")
		Label(r, text='English word:').pack()
		self.e_en = Entry(r)
		self.e_en.pack()
		Label(r, text='Russian word:').pack()
		self.e_ru = Entry(r)
		self.e_ru.pack()
		b = Button(r, text='ADDITION', font=' 20', command=self.command_add_wordYES)
		b.pack()

	def command_add_wordYES(self):
		enw, ruw = self.e_en.get(), self.e_ru.get()
		file = open('dictionary.txt', 'a', encoding='utf-8')
		new = '\n' + str(enw) + '=' + str(ruw)
		file.write(new)
		file.close()
		showinfo("Great Add", "New 2 \nwords addition \nin dictionary")



	def command_information(self):
		r = Toplevel()
		r.geometry("150x200+500+300")
		t = Text(r)
		t.insert(END, '--INFORMATION--\n\n'
					  'THIS PROGRAM\n'
					  'BE INTERACTIVE\n'
					  'TRANSLATOR \n'
					  'ENGLISH-RUSSIAN\n'
					  'AND\n'
					  'RUSSIAN-ENGLISH\n'
					  'LANGUAGES\n'
					  'THAT EASILY !\n'
					  '\n'
					  'THANKS YOU!\n')
		t.pack()


	def command_apply_settings(self):
		chen = self.ch_en.get()
		chru = self.ch_ru.get()
		if chen == 1:
			self.ch_ru.set(0)
			self.convert_program_english()
			self.select_arr = self.array_words_english
			self.select_arr_reverse = self.array_words_russian
		elif chen == 0:
			self.ch_ru.set(1)
			self.convert_program_russian()
			self.select_arr = self.array_words_russian
			self.select_arr_reverse = self.array_words_english



	def run_loop_wait_translate(self):
		self.user_world = self.entry_user_word.get()
		length_user_world = len(self.user_world)
		self.new_know_word = ''
		for word in self.select_arr:
			if word[0:length_user_world] == self.user_world:
				self.new_know_word_not_n = word
				self.new_know_word += (word+'\n')
				if self.user_world in self.select_arr:
					self.text_translate.delete(0.0, END)
					self.text_translate.insert(END, self.select_arr_reverse[self.select_arr.index(self.user_world)])
				else:
					self.text_translate.delete(0.0, END)
					self.text_translate.insert(END, self.text_output_translate)
			self.text_know.delete(0.0, END)
			self.text_know.insert(0.0, self.new_know_word + '\n')
			if self.user_world == '':
				self.text_know.delete(0.0, END)
				self.text_know.insert(0.0, '--------------------------------------------------------------\n'
										   '-----c-c-c--------o-o-o-------d-dd-d-------e-e-e-e------------\n'
										   '----c------------o-------o-----d-----d-----e------------------\n'
										   '----c------------o--------o----d------d-----e-----------------\n'
										   '----c------------o--------o----d-------d----e-e-e-------------\n'
										   '-----c------c-----o-------o-----d-----d------e----------------\n'
										   '-------c-c-c---------o-o-o-----d--d-d-d-------e-e-e-e---------\n'
										   '--------------------------------------------------------------\n')

		self.root.after(1,self.run_loop_wait_translate)




	def convert_program_english(self):
		# if self.run_en == True:
		self.name_list['text']='Words from dictinary:'
		self.name_entry['text']='Enter your word:'
		self.name_settings['text']='Selected language inputing:'
		self.name_know['text']='Knows word:'
		self.name_translate['text']='Translate word:'
		self.name_btns['text']='Constrols:'
		self.btn_apply['text'] = 'Apply settings'
		self.btn_info['text'] = 'Information'
		self.btn_open_dict['text'] = 'Add word'
		self.text_output_translate = 'Not found word'
		self.list_words.delete(0, END)
		for word in self.array_words_english:
			self.list_words.insert(0, word)
			# run_en = False

	def convert_program_russian(self):
		# if self.run_ru == True:
		self.name_list['text']='Слова из словаря:'
		self.name_entry['text']='Введите слово:'
		self.name_settings['text']='Выбор языка для ввода:'
		self.name_know['text']='Распознаное слово:'
		self.name_translate['text']='Перевод слово:'
		self.name_btns['text']='Контроллы:'
		self.btn_apply['text'] = 'Принять настройки'
		self.btn_info['text'] = 'Информация'
		self.btn_open_dict['text'] = 'Добавить слово'
		self.text_output_translate = 'Слово не найдено'
		self.list_words.delete(0, END)
		for word in self.array_words_russian:
			self.list_words.insert(0, word)

		# self.run_ru = False
	def end(self):
		self.root.mainloop()




win = Window()
win.init_elements_frames()
win.init_elements_list_words()
win.init_elements_entry_user()
win.init_elements_settings()
win.init_elements_translate()
win.init_elements_buttons()
win.init_names_elements()
win.run_loop_wait_translate()
win.end()
