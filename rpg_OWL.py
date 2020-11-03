import os
import sys
from time import sleep
import random

######################################
all_items = ['Axe_of_War', 'Arrow_of_Morgin', 'Shoose','Stick_of_True','Rock','Shield_by_grass','anime']
all_items_ = {'Axe_of_War':15,'Arrow_of_Morgin':20,'Shoose':4,'Stick_of_True':2,'Rock':1,'Shield_by_grass':3,'anime':0}


class Hero:
	"""docstring for Hero"""
	def __init__(self, name, classs = "" , level=0,gold = 0,xp = 0, god_item=[], equipe=[], defense = 0, attack = 2):
		self.attack = attack
		self.god_item = god_item
		self.xp = xp
		self.xpp = 500
		self.classs = classs
		self.defense = defense
		self.hp = random.randint(100, 125)
		self.mp = random.randint(50, 100)
		self.equipe = equipe
		self.level = level
		self.name = name
		self.gold = gold


	def status(self):
		print("  *********************  ")
		print(" *********************** ")
		print(f"** Ваш режим: {self.name}    ")
		print(f"**                     ")
		print(f"** Ваш класс: {self.classs} ")
		print(f"**                     ")
		print(f"** Уровень: {self.level}, xp - {self.xp}  ")
		print(f"**                     ")
		print(f"** Золото: {self.gold}           ")
		print(f"**                     ")
		print(f"** Атака: {self.attack}           ")
		print(f"**                     ")
		print(f"** Ваше здоровье: {self.hp}  ")
		print(f"**                                        ")
		print(f"** Ваша мана: {self.mp}                   ")
		print(f"**                                        ")
		print(f"** Ваша броня: {self.defense}             ")
		print(f"**                                        ")
		print(" ***********************  ")
		print("  *********************  \n")

	def __str__(self):
		return f"Ваш режим: {self.name}"	

	def lvl_up(self):
		self.level += 1
		print(f"Ваш уровень {self.name} повысился до {self.level}")
		if self.classs == "Warriror":
			self.hp +=100
			self.mp +=50
			self.defense +=1
			self.attack += random.randint(1,3)
			print(f"Жизни увеличились - {self.hp}")
			print(f"Мана увеличилась - {self.mp}")
			print(f"Защита увеличилась - {self.defense}")
			print(f"Атака увеличилась - {self.attack}")
		elif self.classs == "Archer":
			self.hp +=75
			self.mp +=80
			self.defense += 1
			self.attack += random.randint(1,3)
			print(f"Жизни увеличились - {self.hp}")
			print(f"Мана увеличилась - {self.mp}")
			print(f"Защита увеличилась - {self.defense}")
			print(f"Атака увеличилась - {self.attack}")
		elif self.classs == "Def":
			self.hp += 200
			self.mp += 40
			self.defense +=1
			self.attack += random.randint(1,3)
			print(f"Жизни увеличились - {self.hp}")
			print(f"Мана увеличилась - {self.mp}")
			print(f"Защита увеличилась - {self.defense}")
			print(f"Атака увеличилась - {self.attack}")
		
class Devil:
	"""docstring for Devil"""
	def __init__(self, name, classs = "" , level=0,gold = 0,xp = 0, hell_item=[], equipe=[], defense = 0, attack = 2):
		self.attack = attack
		self.hell_item = hell_item
		self.xp = xp
		self.xpp = 500
		self.classs = classs
		self.defense = defense
		self.hp = random.randint(100, 125)
		self.mp = random.randint(50, 100)
		self.equipe = equipe
		self.level = level
		self.name = name
		self.gold = gold


	def status(self):
		print("  *********************  ")
		print(" *********************** ")
		print(f"** Ваш режим: {self.name}    ")
		print(f"**                     ")
		print(f"** Ваш класс: {self.classs} ")
		print(f"**                     ")
		print(f"** Уровень: {self.level}, xp - {self.xp}  ")
		print(f"**                     ")
		print(f"** Золото: {self.gold}           ")
		print(f"**                     ")
		print(f"** Атака: {self.attack}           ")
		print(f"**                     ")
		print(f"** Ваше здоровье: {self.hp}  ")
		print(f"**                                        ")
		print(f"** Ваша мана: {self.mp}                   ")
		print(f"**                                        ")
		print(f"** Ваша броня: {self.defense}             ")
		print(f"**                                        ")
		print(" ***********************  ")
		print("  *********************  \n")

	def __str__(self):
		return f"Ваш режим: {self.name}"	

	def lvl_up(self):
		self.level += 1
		print(f"Ваш уровень {self.name} повысился до {self.level}")
		if self.classs == "Necromantic":
			self.hp +=100
			self.mp +=50
			self.defense +=1
			self.attack += random.randint(1,3)
			print(f"Жизни увеличились - {self.hp}")
			print(f"Мана увеличилась - {self.mp}")
			print(f"Защита увеличилась - {self.defense}")
			print(f"Атака увеличилась - {self.attack}")
		elif self.classs == "Summoner":
			self.hp +=75
			self.mp +=80
			self.defense += 1
			self.attack += random.randint(1,3)
			print(f"Жизни увеличились - {self.hp}")
			print(f"Мана увеличилась - {self.mp}")
			print(f"Защита увеличилась - {self.defense}")
			print(f"Атака увеличилась - {self.attack}")
		elif self.classs == "Mother_of_element":
			self.hp += 200
			self.mp += 40
			self.defense +=1
			self.attack += random.randint(1,3)
			print(f"Жизни увеличились - {self.hp}")
			print(f"Мана увеличилась - {self.mp}")
			print(f"Защита увеличилась - {self.defense}")
			print(f"Атака увеличилась - {self.attack}")

class Monster:
	"""docstring for ClassName"""
	def __init__(self):
		self.defense = 0
		self.hp = random.randint(10,20)
		self.attack = random.randint(2,3)
		self.gold = random.randint(2,5)
		self.xp = 100
		

######################################
		

class Warriror(Hero):
	"""docstring for ClassName"""	

	def __str__(self):
		return super().__str__()

	def hits(self, monster):
		if monster.hp!=0:
			monster.hp = (monster.hp - self.attack)+monster.defense
			if monster.hp <= 0:
				print("\nУбит")
				print(f"Получено Золото: {monster.gold}")
				self.gold += monster.gold
				print(f"Получено Опыта: {monster.xp}")
				self.xp += monster.xp
				if (self.xp == self.xpp):
					self.lvl_up()
					self.xpp += 500
			return monster.hp
		else:
			print("Уже мертв")
		
#class Def(Hero):
#	"""docstring for Def"""
#	def __str__(self):
#		return super().__str__()
#
#	def hits(self, monster):
#		if monster.hp!=0:
#			monster.hp = (monster.hp - self.attack)+monster.defense
#			if monster.hp <= 0:
#				print("\nУбит")
#				print(f"Получено Золото: {monster.gold}")
#				self.gold += monster.gold
#				print(f"Получено Опыта: {monster.xp}")
#				self.xp += monster.xp
#				if (self.xp == self.xpp):
#					self.lvl_up()
#					self.xpp += random.randint(500, 1500)
#			return monster.hp
#		else:
#			print("Уже мертв")
#
#class Archer(Hero):
#		"""docstring for Archer"""
#	def __str__(self):
#		return super().__str__()
#
#	def hits(self, monster):
#		if monster.hp!=0:
#			monster.hp = (monster.hp - self.attack)+monster.defense
#			if monster.hp <= 0:
#				print("\nУбит")
#				print(f"Получено Золото: {monster.gold}")
#				self.gold += monster.gold
#				print(f"Получено Опыта: {monster.xp}")
#				self.xp += monster.xp
#				if (self.xp == self.xpp):
#					self.lvl_up()
#					self.xpp += random.randint(500, 1500)
#			return monster.hp
#		else:
#			print("Уже мертв")
#		
########################################
#
#class Necromantic(Devil):
#	"""docstring for Necromantic"""
#	def __str__(self):
#		return super().__str__()
#
#	def hits(self, monster):
#		if monster.hp!=0:
#			monster.hp = (monster.hp - self.attack)+monster.defense
#			if monster.hp <= 0:
#				print("\nУбит")
#				print(f"Получено Золото: {monster.gold}")
#				self.gold += monster.gold
#				print(f"Получено Опыта: {monster.xp}")
#				self.xp += monster.xp
#				if (self.xp == self.xpp):
#					self.lvl_up()
#					self.xpp += random.randint(500, 1500)
#			return monster.hp
#		else:
#			print("Уже мертв")
#
#class Summoner(Devil):
#	"""docstring for Summoner"""
#	def __str__(self):
#		return super().__str__()
#
#	def hits(self, monster):
#		if monster.hp!=0:
#			monster.hp = (monster.hp - self.attack)+monster.defense
#			if monster.hp <= 0:
#				print("\nУбит")
#				print(f"Получено Золото: {monster.gold}")
#				self.gold += monster.gold
#				print(f"Получено Опыта: {monster.xp}")
#				self.xp += monster.xp
#				if (self.xp == self.xpp):
#					self.lvl_up()
#					self.xpp += random.randint(500, 1500)
#			return monster.hp
#		else:
#			print("Уже мертв")
#		
#class Mother_of_element(Devil):
#	"""docstring for Mother_of_element"""
#	def __str__(self):
#		return super().__str__()
#
#	def hits(self, monster):
#		if monster.hp!=0:
#			monster.hp = (monster.hp - self.attack)+monster.defense
#			if monster.hp <= 0:
#				print("\nУбит")
#				print(f"Получено Золото: {monster.gold}")
#				self.gold += monster.gold
#				print(f"Получено Опыта: {monster.xp}")
#				self.xp += monster.xp
#				if (self.xp == self.xpp):
#					self.lvl_up()
#					self.xpp += random.randint(500, 1500)
#			return monster.hp
#		else:
#			print("Уже мертв")
###########################################	


class Wolf(Monster):
	"""docstring for Wolf"""
	def __init__(self):
		return super().__init__()
		
	def hitss(self, Player):
		if Player.hp!=0:
			Player.hp -= self.attack
			if Player.hp == 0:
				print(f"{Player.name} - Убит")
				print("Перезапуск игры...")
				sleep(5)
				restart_game()
			return Player.hp
		else:
			print("Уже мертв")

		
#class Ogre(Monster):
#	"""docstring for Ogre"""
#	def __init__(self):
#		return super().__init__()
#		
#	def hitss(self, Player):
#		if Player.hp!=0:
#			Player.hp -= (self.attack - Player.defense)
#			if Player.hp == 0:
#				print(f"{Player.name} - Убит")
#				print("Перезапуск игры...")
#				sleep(5)
#				restart_game()
#			return Player.hp
#		else:
#			print("Уже мертв")
#		
#class Pidor(Monster):
#	"""docstring for Pidor"""
#	def __init__(self):
#		return super().__init__()
#		
#	def hitss(self, Player):
#		if Player.hp!=0:
#			Player.hp -= (self.attack - Player.defense)
#			if Player.hp == 0:
#				print(f"{Player.name} - Убит")
#				print("Перезапуск игры...")
#				sleep(5)
#				restart_game()
#			return Player.hp
#		else:
#			print("Уже мертв")
#
############################################	

def create_player():
	print("Веберите сторону силы [Герой, Злодей]")
	s = True
	n = True
	while (s):
		inputs = "Герой"
		if inputs=="Герой" or inputs=="герой":
			Pl_1 = Hero("Герой")
			print(f"Вы выбрали - {inputs}")
			print("######################")
			print("Выберите Ваш класс: ")
			print("Warriror")
			print("Archer")
			print("Def")
			print("######################")
			s = False
			while (n):
				inputs = "Warriror"
				if inputs=="Warriror" or inputs=="warriror":
					print(f"Вы выбрали класс - {inputs}")
					strr = Pl_1.__str__()
					Player = Warriror(strr[11:])
					Player.classs = "Warriror"
					Player.lvl_up()
					s = False
					return Player
				if inputs == "Archer" or inputs=="archer":
					print(f"Вы выбрали класс - {inputs}")
					strr = Pl_1.__str__()
					Player = Archer(strr[11:])
					n = False
					return Player
				if inputs == "Def" or inputs=="def":
					print(f"Вы выбрали класс - {inputs}")
					strr = Pl_1.__str__()
					Player = Def(strr[11:])
					n = False
					return Player
		elif inputs=="Злодей" or inputs=="злодей":
			Pl_1 = Hero("Злодей")
			print(f"Вы выбрали - {inputs}")
			print("######################")
			print("Выберите Ваш класс: ")
			print("Necromantic")
			print("Summoner")
			print("Mother_of_element")
			print("######################")
			s = False
			while (n):
				inputs = input()
				if inputs=="Necromantic" or inputs=="necromantic":
					print(f"Вы выбрали класс - {inputs}")
					strr = Pl_1.__str__()
					Player = Necromantic(strr[11:])
					n = False
					return Player
				if inputs == "Summoner" or inputs=="summoner":
					print(f"Вы выбрали класс - {inputs}")
					strr = Pl_1.__str__()
					Player = Summoner(strr[11:])
					n = False
					return Player
				if inputs == "Mother_of_element" or inputs=="mother_of_element":
					print(f"Вы выбрали класс - {inputs}")
					strr = Pl_1.__str__()
					Player = Mother_of_element(strr[11:])
					n = False
					return Player

def restart_game():
	if __name__ == '__main__':
		main()

def Privetstvie():
	line = "Чёрное и ясное небо над головой. Вдали слышны взрывы и звуки ломающегося на части корабля.\nНа безмятежной глади лазурного океана распологается лодка,\nс единственно выжившим человеком на борту. Он плыл 7 дней и 7 ночей.\nУ него закончились запасы продовольствия и депресанты, помогающие ему не свехнуться.\nОн закрыл глаза и приготовился к смерти."
	sleep(2)
	line_2 = "Слышны голоса чаек и лодка больше не волновалась. Человек открыл глаза и сказал \n\"Я еще жив?\"\nПоняв, что так оно и есть, он встал с лодки и отправился\nна неизвестную ему землю в поисках еды и воды. Пробираясь через заросли\nлистьев и веток, Он наконец-то обнаруживает источник воды.\nНо неожиданно на него нападает стая диких волков~~~\n.Человек в растеряности и не знает куда бежать...Как вдруг\n"
	sleep(2)
	line_3 = "Яркая вспышка ослепила и прогнала волков. Перед человеком появился сам Ангел по плоти.\n\"Я вижу сокрытую в глубине твоей души истинную силу.Я\nнаделю тебя всем чем необходимо, чтобы раскрыть твой истинный потенциал\"\n"
	for x in line:
		print(x, end='')
		sys.stdout.flush()
		sleep(0.05)
	for x in line_2:
		print(x, end='')
		sys.stdout.flush()
		sleep(0.05)
	for x in line_3:
		print(x, end='')
		sys.stdout.flush()
		sleep(0.05)
	pass

def gameOver():
	print("...gameOver...")
	os.system("exit")
	os.system("pause")
	

def victory():
	print("Victory!!!")
	print("Желаем всего хорошего и Счастливого пути")
	os.system("exit")
	os.system("pause")
	

def Error():
	print("Error///")
	return 0
	



def main():
	############
	os.system("title " + "Online World Leins _ OWL")
	############
	#Privetstvie()
	############
	sleep(1)
	print("##################")
	print("# #   #      #   #")
	print("##@# #@#    @@@  #")
	print("#@@@#@@@#  #@@@@ #")
	print("##@@#@@@@#  ######")
	print("##$$##$$####$$####")
	sleep(1)
	print("\\\\\\Создание персонажа///")
	Player = create_player()
	###############
	print("1")
	print("2")
	sleep(2)
	print("Ваши характеристики")
	Player.status()
	############
	gameOver_ = True
	sleep(2)
	print("Сейчас вам будет предложено меню, пожалуйста, ознакомтесь\n")
	sleep(2)

	if Player.name == "Герой":
	
		while (gameOver_):
			print("\n")
			print(Player)
			print("##################")
			print("Shop")
			print("inventory")
			print("equipe")
			print("quest")
			print("status")
			print("##################")
	
			x = input()

			if x == "quest":
				print("На вашем пути встретился волк, тот, который недавно пытался вас загрызть у источника воды, кажется он выбился из стаи")
				print("fight!")
				Wolf_ = Wolf()
				print(Wolf_.hp)
				while Player.hp > 0 and Wolf_.hp > 0:
					count = random.random()
					if count>0.5:
						print("Player - attack", Player.hits(Wolf_))
					else:
						print("Monster - attack", Wolf_.hitss(Player))
					

			if x == "status":
				print("Ваши характеристики ")
				Player.status()
			
			if x == "inventory":
				while (1):
					print("Ваше снаряжение")
					for x in range(len(Player.god_item)):
						print(f"{x+1}.{Player.god_item[x]}", end='\n')
	
					print("~~~Сортировка~~~")
					print("~~~Надеть предмет~~~")
					print("~~~Выпить эликсир~~~")

					




			if x == "shop":
				print("Товары на любой вкус и цвет, Да?")
				for x in range(len(all_items)):
					print(f"{x+1}.{all_items[x]}")
					
				xf = int(input())

				for x in range(len(all_items)):
					
					if xf <= 0 or xf >=8:
						Error()
						

					if xf == x+1 and Player.gold >= all_items_.get(all_items[x]):
						Player.god_item.append(all_items[x])

						Player.gold -= all_items_.get(all_items[x])

						all_items_.pop(all_items[x])

						all_items.pop(x)


	
					


#	elif Player.name == "Злодей":
#		print("\n")
#		print(Player)
#		print("##################")
#		print("shop")
#		print("inventory")
#		print("equipe")
#		print("quest")
#		print("status")
#		print("##################")
#
#		x = input()
#		if x == "quest":
#			print("На вашем пути встретился волк, тот, который недавно пытался вас загрызть у источника воды, кажется он выбился из стаи")
#			print("fight!")
#			Wolf_ = Wolf()
#			print(Wolf_.hp)
#			while Player.hp>0 and Wolf_.hp > 0:
#				count = random.random()
#				if count>0.5:
#					print("Player - attack", Player.hits(Wolf_))
#				else:
#					print("Monster - attack", Wolf_.hitss(Player))
#				
#		if x == "status":
#			print("Ваши характеристики ")
#			Player.status()
#		
#		if x == "inventory":
#			print("Ваше снаряжение")
#			for x in range(len(Player.god_item)):
#				print(f"{x+1}.{Player.god_item[x]}", end='\n')
#
#		if x == "equipe":
#			pass
#
#		if x == "shop":
#			print("Товары на любой вкус и цвет, Да?")
#			for x in range(len(all_items)):
#				print(f"{x+1}.{all_items[x]}")
#				
#			xf = int(input())
#			
#			if (xf == x+1) and (Player.gold >= all_items_.get(all_items[x])):
#				Player.god_item.append(all_items[x])
#				print("1")
#				Player.gold -= all_items_.keys(x)
#				print("1")
#				all_items_.pop(all_items[x])
#				print("1")
#				all_items.pop(x)
#				print("1")


	os.system("pause")



if __name__ == '__main__':
	main()