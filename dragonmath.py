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
		shield_remaining = [s1, s2, s3, s4, s5]														#add shields

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

		d1 = Dead_dragon(root, xpos)													#add a dragon icon to indicate passed level

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
			cobble_list = ['media/slices/a0.jpg', 'media/slices/a1.jpg', 'media/slices/a2.jpg', 'media/slices/a3.jpg', 'media/slices/a4.jpg', 'media/slices/a5.jpg', 'media/slices/a6.jpg', 'media/slices/a7.jpg', 'media/slices/a8.jpg', 'media/slices/a9.jpg']
		if num == 1:
			cobble_list = ['media/slices/b0.jpg', 'media/slices/b1.jpg', 'media/slices/b2.jpg', 'media/slices/b3.jpg', 'media/slices/b4.jpg', 'media/slices/b5.jpg', 'media/slices/b6.jpg', 'media/slices/b7.jpg', 'media/slices/b8.jpg', 'media/slices/b9.jpg']
		if num == 2:
			cobble_list = ['media/slices/c0.jpg', 'media/slices/c1.jpg', 'media/slices/c2.jpg', 'media/slices/c3.jpg', 'media/slices/c4.jpg', 'media/slices/c5.jpg', 'media/slices/c6.jpg', 'media/slices/c7.jpg', 'media/slices/c8.jpg', 'media/slices/c9.jpg']
		if num == 3:
			cobble_list = ['media/slices/d0.jpg', 'media/slices/d1.jpg', 'media/slices/d2.jpg', 'media/slices/d3.jpg', 'media/slices/d4.jpg', 'media/slices/d5.jpg', 'media/slices/d6.jpg', 'media/slices/d7.jpg', 'media/slices/d8.jpg', 'media/slices/d9.jpg']
		if num == 4:
			cobble_list = ['media/slices/e0.jpg', 'media/slices/e1.jpg', 'media/slices/e2.jpg', 'media/slices/e3.jpg', 'media/slices/e4.jpg', 'media/slices/e5.jpg', 'media/slices/e6.jpg', 'media/slices/e7.jpg', 'media/slices/e8.jpg', 'media/slices/e9.jpg']
		if num == 5:
			cobble_list = ['media/slices/f0.jpg', 'media/slices/f1.jpg', 'media/slices/f2.jpg', 'media/slices/f3.jpg', 'media/slices/f4.jpg', 'media/slices/f5.jpg', 'media/slices/f6.jpg', 'media/slices/f7.jpg', 'media/slices/f8.jpg', 'media/slices/f9.jpg']
		if num == 6:
			cobble_list = ['media/slices/g0.jpg', 'media/slices/g1.jpg', 'media/slices/g2.jpg', 'media/slices/g3.jpg', 'media/slices/g4.jpg', 'media/slices/g5.jpg', 'media/slices/g6.jpg', 'media/slices/g7.jpg', 'media/slices/g8.jpg', 'media/slices/g9.jpg']
		if num == 7:
			cobble_list = ['media/slices/h0.jpg', 'media/slices/h1.jpg', 'media/slices/h2.jpg', 'media/slices/h3.jpg', 'media/slices/h4.jpg', 'media/slices/h5.jpg', 'media/slices/h6.jpg', 'media/slices/h7.jpg', 'media/slices/h8.jpg', 'media/slices/h9.jpg']
		if num == 8:
			cobble_list = ['media/slices/i0.jpg', 'media/slices/i1.jpg', 'media/slices/i2.jpg', 'media/slices/i3.jpg', 'media/slices/i4.jpg', 'media/slices/i5.jpg', 'media/slices/i6.jpg', 'media/slices/i7.jpg', 'media/slices/i8.jpg', 'media/slices/i9.jpg']
		if num == 9:
			cobble_list = ['media/slices/j0.jpg', 'media/slices/j1.jpg', 'media/slices/j2.jpg', 'media/slices/j3.jpg', 'media/slices/j4.jpg', 'media/slices/j5.jpg', 'media/slices/j6.jpg', 'media/slices/j7.jpg', 'media/slices/j8.jpg', 'media/slices/j9.jpg']

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
		cobble_remaining = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]														#obscure the main image

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
		d1 = Dragon(root, dragon_list[num])														#set the main image

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
		bg1 = Bg(root, bg_list[num])															#set the background


def setup(num):	
	playsound('media/dead_dragon.mp3')
	playsound('media/fanfare.mp3')

	bg1.bg_label.destroy()
	Bg.apply_bg(num)

	d1.dragon.destroy()
	Dragon.apply_dragon(num)
	Cobble.apply_cobble(num)

	problem()													#setup the window, num is the level they are on


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
		if int(answer.get()) == ans:									#checks for correct answer and update score
			score += 1
			score_label.configure(text = 'SCORE      '+str(score))

			if len(cobble_remaining) == 1:								#check for last piece to flag end of level
				num_of_wins += 1
				cobble_remaining[0].cobble_label.destroy()				#destroy last piece of 'cobble'
				Dead_dragon.apply_dead_dragon(num_of_wins)				#apply level pass icon
				root.after(2, lambda: setup(num_of_wins))				#had to do this to prevent last piece turning grey???

			else:
				playsound('media/roar.mp3')
				random_cobble = choice(cobble_remaining)				#delete random piece of 'cobble' and ask a new question
				random_cobble.cobble_label.destroy()
				cobble_remaining.remove(random_cobble)
				problem()

		else:															#wrong answer, delete a shield and same question again
			shield_remaining.pop().shield_label.destroy()

			if shield_remaining == []:
				game_over_func()

			playsound('media/grunt.mp3')
		
		answer.delete(0,'end')
		
	except ValueError:
		pass

def problem():
	
	global question, ans, timer, t
	numa = numlist[randint(0,11)]										#random numers to multiply, update bg image with sum
	numb = numlist[randint(0,11)]

	ans = numa * numb

	bg1.bg_label.configure(text = str(numa) + ' x ' + str(numb), fg = 'white', compound = tk.CENTER, font = (font, 150))



score_label = tk.Label(root, font = (font, 20), text = 'SCORE      '+str(score))
score_label.place(x= 40, y=0)

Shield.apply_shield()
Bg.apply_bg(0)


Dragon.apply_dragon(0)
Cobble.apply_cobble(0)



knight_bg_holder = p.Image.open('media/knight.jpg')     				#set knight image IMAGES MUST BE 500x700
kn_bg = ptk.PhotoImage(knight_bg_holder)
knight = tk.Label(root, image = kn_bg, text = 'Answer', font = (font, 50), fg = 'white', compound = 'center')
knight.image = kn_bg
knight.place(x=500, y=340)

answer = tk.Entry(font = (font, 50), width = 3, justify = 'center')		#set answer box
answer.place(x = 660, y = 770)
answer.focus()




root.bind('<KP_Enter>', guess)											#numpad enter to submit answer



problem()


root.mainloop()
