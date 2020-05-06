import tkinter as tk
from random import randint
import PIL as p
import PIL.ImageTk as ptk
from playsound import playsound

def timer_function():
	global timer
	t = 15
	while t > 0:
		root.after(1000, lambda: timer.config(text = str(t)))
		t -= 1

	wrong_func()
	print('TIME')


root = tk.Tk()
root.title('Dragonmath 1.0')
root.geometry('1000x1000')

score = 0
wrong = 0

numlist = [1,2,3,4,5,6,7,8,9,10,11,12]
font = 'Dragonlands'

#build_cobble():
#	cobble = []
#		for i in range(10):
#			cobhol = 'cobblestone' + str(i)
#			cobhol = p.Image.open('media/cobblestone%s.jpg' % i)
#			cob = 
#			cb = 


score_label = tk.Label(root, font = (font, 20), text = 'SCORE      '+str(score))
score_label.place(x= 40, y=0)

def guess(a):

		def wrong_func(num):
			def game_over_func():
				game_over_window = tk.Toplevel()

				game_over_holder = p.Image.open('media/game_over.jpg')
				game_over_img = ptk.PhotoImage(game_over_holder)
				game_over_bg = tk.Label(game_over_window, image = game_over_img)
				game_over_bg.image = game_over_img
				game_over_bg.pack()

				#final_time = tk.Label(game_over_window, text = 'Final time - {}'.format(total_time), font = (font, 40)).place(x = 1200, y = 650)
				final_score = tk.Label(game_over_window, text = 'Final score - {}'.format(score), font = (font, 40)).place(x = 1200, y = 850)

				#playsound('media/pain.mp3')

				game_over_window.mainloop()

			
			xpos = 995 - (num * 40)

			shield_bg_holder = p.Image.open('media/shield.jpg')
			shield_img = ptk.PhotoImage(shield_bg_holder)
			shield_icon = tk.Label(root, image = shield_img)
			shield_icon.image = shield_img
			shield_icon.place(x=xpos, y=0)

			playsound('media/grunt.mp3')

			if num == 1:
				game_over_func()


		global score, wrong, question, answer, ans
		try:
			if int(answer.get()) == ans:
				playsound('media/roar.mp3')
				score += 1
				score_label.configure(text = 'SCORE      '+str(score))
				question.destroy()
				answer.delete(0,'end')
				problem()
			else:
				print('WRONG, TRY AGAIN')
				wrong += 1
				wrong_func(wrong)
		except ValueError:
			pass

def problem():
	
	global question, ans, timer
	numa = 5       #numlist[randint(0,11)]
	numb = numlist[randint(0,11)]

	ans = numa * numb

	question_bg_holder = p.Image.open('media/bg1.jpg').crop((0,500,1000,800))
	bg = ptk.PhotoImage(question_bg_holder)
	question = tk.Label(root, image = bg, text = str(numa) + ' x ' + str(numb), fg = 'white', compound = tk.CENTER, font = (font, 150))
	question.image = bg
	question.place(x=0, y=40)

	timer_function()

	timer_holder = p.Image.open('media/bg1.jpg')
	timer_img = ptk.PhotoImage(timer_holder)
	timer = tk.Label(root, font = (font, 40), text = str(t))
	timer.image = timer_img
	timer.place(x=500, y=860)




cobble = [['cobblestone1', 340], ['cobblestone2', 410], ['cobblestone3', 480], ['cobblestone4', 550], ['cobblestone5', 620], ['cobblestone6', 690], ['cobblestone7', 760], ['cobblestone8', 830], ['cobblestone9', 900], ['cobblestone10', 970]]

#def apply_cobble():
#	str(cobble[i][0]) + '_holder' =_holder = p.Image.open('media/%s.jpg' % str(cobble[i][0]))  
#	str(cobble[i][0]) + '_aaa' = ptk.PhotoImage(str(cobble[i][0] + '_holder')
#	str(cobble[i][0]) = tk.Label(root, image = str(cobble[i][0]) + '_aaa')
#	str(cobble[i][0]).image = dr_bg
#	str(cobble[i][0]).place(x=0, y=cobble[i][1])

dragon_bg_holder = p.Image.open('media/dragon1.jpg')     #images must be 500x700
dr_bg = ptk.PhotoImage(dragon_bg_holder)
dragon = tk.Label(root, image = dr_bg)
dragon.image = dr_bg
dragon.place(x=0, y=340)

cob_bg_holder = p.Image.open('media/cobblestone1.jpg')     #images must be 500x700
print(cob_bg_holder.size[1])
cob_bg = ptk.PhotoImage(cob_bg_holder)
cobble = tk.Label(root, image = cob_bg)
cobble.image = cob_bg
cobble.place(x=0, y=340)


knight_bg_holder = p.Image.open('media/knight.jpg')     #images must be 500x700
kn_bg = ptk.PhotoImage(knight_bg_holder)
knight = tk.Label(root, image = kn_bg, text = 'Answer', font = (font, 50), fg = 'white', compound = 'center')
knight.image = kn_bg
knight.place(x=500, y=340)

answer = tk.Entry(font = (font, 50), width = 3, justify = 'center')
answer.place(x = 660, y = 770)
answer.focus()

root.bind('<Return>', guess)




#apply_cobble()
problem()
"""
v = StringVar()
Label(master, textvariable=v).pack()

v.set("New Text!")
"""
root.mainloop()
