import tkinter as tk
from random import randint, choice
import PIL as p
import PIL.ImageTk as ptk
from playsound import playsound


root = tk.Tk()
root.title('Dragonmath 1.0')
root.geometry('1000x1000')

score = 0
wrong = 0

numlist = [1,2,3,4,5,6,7,8,9,10,11,12]
font = 'Dragonlands'

class Shield:
	def __init__(self, master, xpos):
		self.shield_holder = p.Image.open('media/shield.jpg')
		self.shield_img = ptk.PhotoImage(self.shield_holder)
		self.shield_label = tk.Label(master, image = self.shield_img)
		self.shield_label.image = self.shield_img
		self.shield_label.place(x = xpos, y = 0)

	def apply_shield():
		global shield_remaining
		s1 = Shield(root, 955)
		s2 = Shield(root, 915)
		s3 = Shield(root, 875)
		s4 = Shield(root, 835)
		s5 = Shield(root, 795)
		shield_remaining = [s1, s2, s3, s4, s5]


class Dead_dragon:
	def __init__(self, master, xpos):
		self.dead_dragon_holder = p.Image.open('media/dead_dragon.jpeg')
		self.dead_dragon_img = ptk.PhotoImage(self.dead_dragon_holder)
		self.dead_dragon_label = tk.Label(master, image = self.dead_dragon_img)
		self.dead_dragon_label.image = self.dead_dragon_img
		self.dead_dragon_label.place(x = xpos, y = 0)

	def apply_dead_dragon():
		global shield_remaining
		d1 = Dead_dragon(root, 300)


class Cobble:
	def __init__(self, master, ypos, file):

		self.cobble_holder = p.Image.open(file)
		self.cobble_img = ptk.PhotoImage(self.cobble_holder)
		self.cobble_label = tk.Label(master, image = self.cobble_img)
		self.cobble_label.image = self.cobble_img
		self.cobble_label.place(x = 0, y = ypos)

	def apply_cobble():
		global cobble_remaining
		c1 = Cobble(root, 340, 'media/cobblestone1.jpg')
		c2 = Cobble(root, 410, 'media/cobblestone2.jpg')
		c3 = Cobble(root, 480, 'media/cobblestone3.jpg')
		c4 = Cobble(root, 550, 'media/cobblestone4.jpg')
		c5 = Cobble(root, 620, 'media/cobblestone5.jpg')
		c6 = Cobble(root, 690, 'media/cobblestone6.jpg')
		c7 = Cobble(root, 760, 'media/cobblestone7.jpg')
		c8 = Cobble(root, 830, 'media/cobblestone8.jpg')
		c9 = Cobble(root, 900, 'media/cobblestone9.jpg')
		c10 = Cobble(root, 9700, 'media/cobblestone10.jpg')
		cobble_remaining = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]


score_label = tk.Label(root, font = (font, 20), text = 'SCORE      '+str(score))
score_label.place(x= 40, y=0)

def game_over_func():
	game_over_window = tk.Toplevel()

	game_over_holder = p.Image.open('media/game_over.jpg')
	game_over_img = ptk.PhotoImage(game_over_holder)
	game_over_bg = tk.Label(game_over_window, image = game_over_img)
	game_over_bg.image = game_over_img
	game_over_bg.pack()

	#final_time = tk.Label(game_over_window, text = 'Final time - {}'.format(total_time), font = (font, 40)).place(x = 1200, y = 650)
	final_score = tk.Label(game_over_window, text = 'Final score - {}'.format(score), font = (font, 40)).place(x = 1200, y = 850)

	playsound('media/pain.mp3')

	game_over_window.mainloop()


def guess(a):
	
	global score, wrong, question, answer, ans
	try:
		if int(answer.get()) == ans:
			playsound('media/roar.mp3')
			score += 1
			score_label.configure(text = 'SCORE      '+str(score))
			question.destroy()
			answer.delete(0,'end')

			if len(cobble_remaining) == 1:
				Dead_dragon.apply_dead_dragon()
			else:
				random_cobble = choice(cobble_remaining)
				random_cobble.cobble_label.destroy()
				cobble_remaining.remove(random_cobble)

			problem()
		else:
			print('WRONG, TRY AGAIN')
				
			shield_remaining.pop().shield_label.destroy()
			answer.delete(0,'end')

			if shield_remaining == []:
				game_over_func()

			playsound('media/grunt.mp3')
				
	except ValueError:
		pass

def problem():
	
	global question, ans, timer, t
	numa = numlist[randint(0,11)]
	numb = numlist[randint(0,11)]

	ans = numa * numb

	question_bg_holder = p.Image.open('media/bg/bg1.jpg').crop((0,500,1000,800))
	bg = ptk.PhotoImage(question_bg_holder)
	question = tk.Label(root, image = bg, text = str(numa) + ' x ' + str(numb), fg = 'white', compound = tk.CENTER, font = (font, 150))
	question.image = bg
	question.place(x=0, y=40)

	t= 15

	timer_holder = p.Image.open('media/bg/bg1.jpg')
	timer_img = ptk.PhotoImage(timer_holder)
	timer = tk.Label(root, font = (font, 40), text = str(t))
	timer.image = timer_img
	timer.place(x=500, y=860)


	def timer_function():
		global timer, t

		while t > 0:
			root.after(1000, lambda: timer.config(text = str(t)))
			t -= 1

	timer_function()


dragon_bg_holder = p.Image.open('media/dr/dragon1.jpg')     #images must be 500x700
dr_bg = ptk.PhotoImage(dragon_bg_holder)
dragon = tk.Label(root, image = dr_bg)
dragon.image = dr_bg
dragon.place(x=0, y=340)


knight_bg_holder = p.Image.open('media/knight.jpg')     #images must be 500x700
kn_bg = ptk.PhotoImage(knight_bg_holder)
knight = tk.Label(root, image = kn_bg, text = 'Answer', font = (font, 50), fg = 'white', compound = 'center')
knight.image = kn_bg
knight.place(x=500, y=340)

answer = tk.Entry(font = (font, 50), width = 3, justify = 'center')
answer.place(x = 660, y = 770)
answer.focus()

root.bind('<Return>', guess)


Cobble.apply_cobble()
Shield.apply_shield()

problem()


root.mainloop()
