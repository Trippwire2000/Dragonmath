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
num_of_wins = 0

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

	def apply_dead_dragon(num):
		global shield_remaining

		xpos = 260 + (num * 40)

		d1 = Dead_dragon(root, xpos)

class Cobble:
	def __init__(self, master, ypos, file):

		self.cobble_holder = p.Image.open(file)
		self.cobble_img = ptk.PhotoImage(self.cobble_holder)
		self.cobble_label = tk.Label(master, image = self.cobble_img)
		self.cobble_label.image = self.cobble_img
		self.cobble_label.place(x = 0, y = ypos)

	def apply_cobble(num):
		global cobble_remaining
		if num == 0:
			cobble_list = ['media/slices/cobblestone0.jpg', 'media/slices/cobblestone1.jpg', 'media/slices/cobblestone2.jpg', 'media/slices/cobblestone3.jpg', 'media/slices/cobblestone4.jpg', 'media/slices/cobblestone5.jpg', 'media/slices/cobblestone6.jpg', 'media/slices/cobblestone7.jpg', 'media/slices/cobblestone8.jpg', 'media/slices/cobblestone9.jpg']
		elif num == 1:
			cobble_list = ['media/slices/gold0.jpg', 'media/slices/gold1.jpg', 'media/slices/gold2.jpg', 'media/slices/gold3.jpg', 'media/slices/gold4.jpg', 'media/slices/gold5.jpg', 'media/slices/gold6.jpg', 'media/slices/gold7.jpg', 'media/slices/gold8.jpg', 'media/slices/gold9.jpg']

		c0 = Cobble(root, 340, cobble_list[0])
		c1 = Cobble(root, 410, cobble_list[1])
		c2 = Cobble(root, 480, cobble_list[2])
		c3 = Cobble(root, 550, cobble_list[3])
		c4 = Cobble(root, 620, cobble_list[4])
		c5 = Cobble(root, 690, cobble_list[5])
		c6 = Cobble(root, 760, cobble_list[6])
		c7 = Cobble(root, 830, cobble_list[7])
		c8 = Cobble(root, 900, cobble_list[8])
		c9 = Cobble(root, 9700, cobble_list[9])
		cobble_remaining = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]

class Dragon:
	def __init__(self, master, file):
		self.dragon_bg_holder = p.Image.open(file)     #images must be 500x700
		self.dr_bg = ptk.PhotoImage(self.dragon_bg_holder)
		self.dragon = tk.Label(master, image = self.dr_bg)
		self.dragon.image = self.dr_bg
		self.dragon.place(x=0, y=340)

	def apply_dragon(num):
		global d1
		dragon_list = ['media/dr/dragon0.jpg', 'media/dr/dragon1.jpg', 'media/dr/dragon2.jpg', 'media/dr/dragon3.jpg', 'media/dr/dragon4.jpg', 'media/dr/dragon5.jpg', 'media/dr/dragon6.jpg', 'media/dr/dragon7.jpg', 'media/dr/dragon8.jpg', 'media/dr/dragon9.jpg']
		d1 = Dragon(root, dragon_list[num])

class Bg:
	def __init__(self, master, file):
		self.bg_holder = p.Image.open(file).crop((0,500,1000,800))
		self.bg_img = ptk.PhotoImage(self.bg_holder)
		self.bg_label = tk.Label(master, image = self.bg_img) #text = str(numa) + ' x ' + str(numb), fg = 'white', compound = tk.CENTER, font = (font, 150))
		self.bg_label.image = self.bg_img
		self.bg_label.place(x=0, y=40)


	def apply_bg(num):
		global bg1
		bg_list = ['media/bg/bg0.jpg', 'media/bg/bg1.jpg', 'media/bg/bg2.jpg', 'media/bg/bg3.jpg', 'media/bg/bg4.jpg', 'media/bg/bg5.jpg', 'media/bg/bg6.jpg', 'media/bg/bg7.jpg', 'media/bg/bg8.jpg', 'media/bg/bg9.jpg']
		bg1 = Bg(root, bg_list[num])


def setup(num):
	playsound('media/dead_dragon.mp3')
	playsound('media/fanfare.mp3')

	bg1.bg_label.destroy()
	Bg.apply_bg(num)

	d1.dragon.destroy()
	Dragon.apply_dragon(num)
	Cobble.apply_cobble(num)

	problem()


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
	
	global score, wrong, question, answer, ans, num_of_wins
	try:
		if int(answer.get()) == ans:
			score += 1
			score_label.configure(text = 'SCORE      '+str(score))
			answer.delete(0,'end')

			if len(cobble_remaining) == 1:
				num_of_wins += 1
				cobble_remaining[0].cobble_label.destroy()
				Dragon.apply_dragon(num_of_wins)
				Dead_dragon.apply_dead_dragon(num_of_wins)
				setup(num_of_wins)
			else:
				playsound('media/roar.mp3')
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

	bg1.bg_label.configure(text = str(numa) + ' x ' + str(numb), fg = 'white', compound = tk.CENTER, font = (font, 150))



score_label = tk.Label(root, font = (font, 20), text = 'SCORE      '+str(score))
score_label.place(x= 40, y=0)

Shield.apply_shield()
Bg.apply_bg(0)


Dragon.apply_dragon(0)
Cobble.apply_cobble(0)



knight_bg_holder = p.Image.open('media/knight.jpg')     #images must be 500x700
kn_bg = ptk.PhotoImage(knight_bg_holder)
knight = tk.Label(root, image = kn_bg, text = 'Answer', font = (font, 50), fg = 'white', compound = 'center')
knight.image = kn_bg
knight.place(x=500, y=340)

answer = tk.Entry(font = (font, 50), width = 3, justify = 'center')
answer.place(x = 660, y = 770)
answer.focus()




root.bind('<KP_Enter>', guess)



problem()


root.mainloop()
