#convert TheBattle to python 
import random
#primary character class
class Character:

	#initialize character object with some attributes
	def __init__(self,name,hp,strength,defence,agility):
		self.name = name
		self.hp = hp
		self.strength = strength
		self.defence = defence
		self.agility = agility

	#kills method to print winner and loser of the battle
	def kills(self,opponent):
		print('{} kills {}!!!'.format(self.name.upper(),opponent.name.upper()))

	#human controlled attack method
	def cqc(self,opponent):
		print("{} attacks {}".format(self.name,opponent.name))
		print("....")
		
		choice = input("choose kick, punch, or toss\n")
		items = ['kick', 'punch','toss']
		
		while choice not in items:
			print("what?")
			choice = input("choose kick, punch, or toss\n")
		
		#some random conditions for attack to fail
		if opponent.agility == random.randint(3,5):
			print("{}'s attack misses".format(self.name))
		elif opponent.agility >= 3 and random.randint(1,5) == 2:
			print("{} blocks the attack!".format(opponent.name))
		else:
			#attacking options
			if choice == 'kick':
				print("{} kicks {}".format(self.name,opponent.name))
				opponent.hp -= random.randint(2,5)
				opponent.defence -= random.randint(2,3)
				opponent.agility -= 1
				opponent.strength -= random.randint(1,3)
			elif choice == 'punch':
				opponent.hp -= random.randint(1,4)
				opponent.defence -= random.randint(1,2)
				opponent.agility -= 1
				opponent.strength -= random.randint(1,2)
			elif choice == 'toss':
				if self.strength >= 3:
					opponent.hp -= random.randint(2,5)
					opponent.defence -= random.randint(2,4)
					opponent.agility -= 1
					opponent.strength -= random.randint(1,3)
				else:
					print("{} tries to toss {} but isn't strong enough and takes a hit!".format(self.name,opponent.name))
					self.agility -= random.randint(1,3)
					self.defence -= random.randint(1,3)
			else:
				pass
		print("{}'s hp: {}".format(opponent.name,opponent.hp))

	#computer controlled attack method
	def computer_attack(self,opponent):
		print("{} attacks {}".format(self.name,opponent.name))
		print("....")
		
		#possible computer attack options
		items = ['shoot', 'grenade','raven']
		#grab one of the three choices at random per iteration
		rand_items = items[random.randint(0,2)]

		#some random conditions for attack to fail
		if self.agility == random.randint(3,5):
			print("{}'s attack misses".format(self.name))
		elif self.agility >= 3 and random.randint(1,5) == 2:
			print("{} blocks the attack!".format(opponent.name))
		else:
			#computer attacking options
			if rand_items == 'shoot':
				print("{} shoots {}".format(self.name,opponent.name))
				opponent.hp -= random.randint(2,5)
				opponent.defence -= random.randint(2,3)
				opponent.agility -= 1
				opponent.strength -= random.randint(1,3)
			elif rand_items == 'grenade':
				print("{} blows up {} with a 'nade".format(self.name,opponent.name))
				opponent.hp -= random.randint(1,4)
				opponent.defence -= random.randint(1,2)
				opponent.agility -= 1
				opponent.strength -= random.randint(1,2)
			elif rand_items == 'raven':
				if enemy.strength >= 3:
					print("{} sends out the raven".format(self.name))
					print("{}'s hp and agility are severely reduced".format(opponent.name))
					opponent.hp -= random.randint(2,5)
					opponent.defence -= random.randint(2,4)
					opponent.agility -= 1
					opponent.strength -= random.randint(1,3)
				else:
					print("{} sends out the Raven, but isn't strong enough to control it!".format(enemy.name))
					opponent.agility -= random.randint(1,3)
					opponent.defence -= random.randint(1,3)
			else:
				pass
		print("{}'s hp: {}".format(opponent.name,opponent.hp))

#hero subclass 
class Hero(Character):
	
	def stats(self):
		print("Your hero's name is {}, and he has {} hp, {} strength, {} defence, and {} agility".format(self.name,self.hp,self.strength,self.defence,self.agility))

#enemy subclass
class Enemy(Character):

	def stats(self):
		print("Your enemy's name is {}, and he has {} hp, {} strength, {} defence, and {} agility".format(self.name,self.hp,self.strength,self.defence,self.agility))


###################################################
#instantiate hero and enemy subclasses of character object with random integer value attributes
hero = Hero("Snake",random.randint(3,4),random.randint(1,5),random.randint(1,5),random.randint(1,5))
enemy = Enemy("Vulcan Raven",random.randint(3,4),random.randint(1,5),random.randint(1,5),random.randint(1,5))

###################################################

#game engine
def gameloop():
	hero.stats()
	enemy.stats()
	print()
	while True:
		hero.cqc(enemy)
		if enemy.hp >0:
			enemy.computer_attack(hero)
		if hero.hp <= 0:
			enemy.kills(hero)
			break
		elif enemy.hp <= 0:
			hero.kills(enemy)
			break
		else:
			continue

gameloop()