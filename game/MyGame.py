from os import system
from random import randint

gametitle='Castle Dungeons - an interactive story game'
system('mode 110,30')
system('title '+gametitle)

def cls():
	system('cls')

character_name = None
character_race = None
character_class = None
character_strength = None
character_magic = None
character_dexterity = None
character_life = None

cls()
print('Castle Dungeons- An interactive story game')

def Intro():
	print('')
	print('In this adventure, you are the hero.')
	print('Your choices and skills and a bit of luck, will influence the outcome of the game')
	print('')
	print('An evil sorcerer is holding your fellow adventures a prisoners')
	print('Will you succeed in this game?')
	print(' ')
	print('Press enter to start...')

Intro()

def create_character():
	cls()
	global character_name
	character_name=input("""
		Let's begin by creating your character.
		What is your character name?

		>""")
	global character_race
	while character_race is None:
		race_choice=input("""
			Choose your character race from this list
			1-elif
			2-dwarf
			>""") 
		if race_choice=='1':
			character_race='Elf'
		elif race_choice=='2':
			character_race=='dwarf'
		else:
			print('Nota a valid  :/')
	cls()
	global character_class
	while character_class is None:
		class_choice=input("""
			Choose your character  class from this list
			1 - Warrior
			2 - Wizard
			>""")
		if class_choice=='1':
			character_class='Warrior'
		elif class_choice=='2':
			character_class='Wizard'
		else:
			print('Not a valid choice :/')
	cls()

create_character()
					