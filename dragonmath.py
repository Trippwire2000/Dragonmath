import tkinter as tk
from random import randint
import PIL as p
import PIL.ImageTk as ptk
from playsound import playsound

root = tk.Tk()
root.title('Dragonmath 1.0')
root.geometry('1000x1000')

score = 0

numlist = [1,2,3,4,5,6,7,8,9,10,11,12]
font = 'Dragonlands'


def guess(a):
		global score, question, answer, ans
		try:
			if int(answer.get()) == ans:
				score += 1
				score_label.configure(text = 'SCORE      '+str(score))
				question.destroy()
				answer.delete(0,'end')
				problem()
			else:
				print('WRONG, TRY AGAIN')
				playsound('media/roar.mp3')
		except ValueError:
			pass


def problem():
	
	global question, ans
	numa = 5       #numlist[randint(0,11)]
	numb = numlist[randint(0,11)]

	ans = numa * numb

	question_bg_holder = p.Image.open('media/bg1.jpg').resize((1000,400))
	bg = ptk.PhotoImage(question_bg_holder)
	question = tk.Label(question_frame, image = bg, text = str(numa) + ' x ' + str(numb), fg = 'white', compound = tk.CENTER, font = (font, 190))
	question.image = bg
	question.pack()


blackout = {1:'blackout1',2:'blackout2',3:'blackout3',4:'blackout4',5:'blackout5',6:'blackout6',7:'blackout7',8:'blackout8',9:'blackout9',10:'blackout10'}

score_label = tk.Label(root, font = (font, 20), text = 'SCORE      '+str(score))
score_label.pack(anchor = 'nw', fill = 'x')

question_frame = tk.Frame(root, height = 400, width = 1000)
question_frame.pack(anchor = 'n')

dragon_frame = tk.Frame(root, height = 600, width = 1000)
dragon_frame.pack(anchor = 's')


dragon_bg_holder = p.Image.open('media/dragon1.jpg').resize((500,600))
dr_bg = ptk.PhotoImage(dragon_bg_holder)
dragon = tk.Label(dragon_frame, image = dr_bg)
dragon.image = dr_bg
dragon.pack(side = 'left')


#for i in range(1,10):
	#blackout[i] = tk.Label(dragon_frame, bg = 'black', height = 60)
	#blackout[i].pack(side = 'bottom', fill = 'x')

sword_holder = p.Image.open('media/sword.png').resize((500, 100))
sword_bg = ptk.PhotoImage(sword_holder)
sword = tk.Button(dragon_frame, image = sword_bg, bd = 7, text = 'ATTACK',font = (font, 30), fg = 'white', command = guess, compound = tk.CENTER)
sword.image = sword_bg
#sword.pack(side = 'bottom')

aaa = tk.Label(dragon_frame, font = (font, 30), text = 'YOUR ANSWER').pack(fill = 'x')
answer = tk.Entry(dragon_frame, width = 5, bd = 7, font = (font, 90), justify = 'center')
answer.pack(side = 'top')
answer.focus()

root.bind('<Return>', guess)

problem()





root.mainloop()