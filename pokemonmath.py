import tkinter as tk
from random import randint, choice
import PIL as p
import PIL.ImageTk as ptk
from playsound import playsound


root = tk.Tk()
root.title('Pokemath 1.0')
root.geometry('1000x1000')

score = 0
wrong = 0
num_of_wins = 0

font = 'Pokemon Solid'

class Shield:
	def __init__(self, master, xpos):
		self.shield_holder = p.Image.open('media/p/ball.jpg')
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
		self.dead_dragon_holder = p.Image.open('media/p/pik.jpg')
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
		cobble_list = ['media/p/c0.jpg', 'media/p/c1.jpg', 'media/p/c2.jpg', 'media/p/c3.jpg', 'media/p/c4.jpg', 'media/p/c5.jpg', 'media/p/c6.jpg', 'media/p/c7.jpg', 'media/p/c8.jpg', 'media/p/c9.jpg']
		
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
		dragon_list = ['media/p/dr/p0.jpg','media/p/dr/p1.jpg','media/p/dr/p2.jpg','media/p/dr/p3.jpg','media/p/dr/p4.jpg','media/p/dr/p5.jpg','media/p/dr/p6.jpg','media/p/dr/p7.jpg','media/p/dr/p8.jpg','media/p/dr/p9.jpg']
		d1 = Dragon(root, dragon_list[num])														#set the main image

class Bg:
	def __init__(self, master, file):
		self.bg_holder = p.Image.open(file).crop((0,100,1000,395))
		self.bg_img = ptk.PhotoImage(self.bg_holder)
		self.bg_label = tk.Label(master, image = self.bg_img) #text = str(numa) + ' x ' + str(numb), fg = 'white', compound = tk.CENTER, font = (font, 150))
		self.bg_label.image = self.bg_img
		self.bg_label.place(x=0, y=40)


	def apply_bg(num):
		global bg1
		bg_list = ['media/p/bg/bg0.jpg', 'media/p/bg/bg1.jpg', 'media/p/bg/bg2.jpg', 'media/p/bg/bg3.jpg', 'media/p/bg/bg4.jpg', 'media/p/bg/bg5.jpg', 'media/p/bg/bg6.jpg', 'media/p/bg/bg7.jpg', 'media/p/bg/bg8.jpg', 'media/p/bg/bg9.jpg']
		bg1 = Bg(root, bg_list[num])															#set the background


def setup(num):	
	playsound('media/p/pika.mp3')

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
		if int(answer.get()) == ans:
			print('CORRECT')									#checks for correct answer and update score
			score += 1
			score_label.configure(text = 'SCORE      '+str(score))

			if len(cobble_remaining) == 1:
				print('WIN')								#check for last piece to flag end of level
				num_of_wins += 1
				cobble_remaining[0].cobble_label.destroy()				#destroy last piece of 'cobble'
				Dead_dragon.apply_dead_dragon(num_of_wins)				#apply level pass icon
				root.after(2, lambda: setup(num_of_wins))				#had to do this to prevent last piece turning grey???

			else:
				print('ELSE')
				playsound('media/p/togepy.mp3')
				print('cobble remain 1- {}'.format(str(cobble_remaining)))
				random_cobble = choice(cobble_remaining)				#delete random piece of 'cobble' and ask a new question
				random_cobble.cobble_label.destroy()
				cobble_remaining.remove(random_cobble)
				print('cobble remain 1- {}'.format(str(cobble_remaining)))

				problem()

		else:															#wrong answer, delete a shield and same question again
			shield_remaining.pop().shield_label.destroy()

			if shield_remaining == []:
				game_over_func()

			playsound('media/p/squirtle.mp3')
		
		answer.delete(0,'end')
		
	except ValueError:
		pass

def problem():
	
	global question, ans, timer, t
	numa = randint(0,10)						#random numers to multiply, update bg image with sum
	numb = randint(0,10)

	operator = randint(1,2)
	if operator == 1:
		ans = numa + numb
		operator = '+'
	else:
		ans = numa - numb
		operator = '-'
		if ans < 0:							#swap numbers if answer is negative
			temp = numa
			numa = numb
			numb = temp
			ans = numa - numb



	bg1.bg_label.configure(text = str(numa) + ' {} '.format(operator) + str(numb), fg = 'black', compound = tk.CENTER, font = (font, 140))



score_label = tk.Label(root, font = (font, 15), text = 'SCORE      '+str(score))
score_label.place(x= 40, y=0)

Shield.apply_shield()
Bg.apply_bg(0)


Dragon.apply_dragon(0)
Cobble.apply_cobble(0)



knight_bg_holder = p.Image.open('media/p/ash.jpg')     				#set knight image IMAGES MUST BE 500x700
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
