import random
from random import randint
from time import sleep

# switches that I need through the game
alarm = False
enemies = True
search_dining = False
bomb = False
weapon = False
wake = False
dining = False
alien = True

# secret codes
armory_code = int(f"{randint(1,9)}{randint(1,9)}{randint(1,9)}")
escape_code = ['beati pauperes spiritu quoniam ipsorum est regnum caelorum', 'beati qui lugent quoniam ipsi consolabuntur', 'beati misericordes quia ipsi misericordiam consequentur', 'beati mundo corde quoniam ipsi Deum videbunt', 'beati pacifici quoniam filii Dei vocabuntur']
george = (random.choice(escape_code))
words = len(george)//2
pod_phrase = (george[:int(words)])
phrase_pod = (george[int(words):])
passphrase = pod_phrase + phrase_pod

# instructions
burla = "In here you can move in four directions: north, west, south and east"
choose = {'north', 'west', 'south', 'east', 'search'}
not_available = "I'm sorry but the requested command is not available."

# my printer
class stamp():

	def __init__(self, text):
		self.text = text

	def printer(self):
		for x in self.text:
			sleep(0.01)
			print(x, end='', flush=True)



def death():
	global alarm, enemies, search_dining, bomb, weapon, wake, dining
	g = stamp("""\nYou died, you kinda suck at this.\nDo you want to try again?\n""")
	g.printer()
	key = input("""
> """)

	yes = {'yes', 'y', 'yeah', 'ye', ''}
	no = {'no', 'n', 'nah', 'nope', 'nay'}

	if key in yes: 
		
		alarm = False
		enemies = True
		search_dining = False
		bomb = False
		weapon = False
		wake = False
		dining = False
		alien = True
		return wake_room()

	if key in no:
		p = ('G O O D B Y E  L O S E R')
		for c in p:
			sleep(0.6)
			print(c, end='', flush=True)
		exit()
	else:
		print(f"Even a monkey could have guessed among {yes} or {no}")
		print("Goodbye loser")
		exit()

def main():
	global alarm
	c = stamp("""\nThe magic room, as the captain Haste used to call it.
		\nThe room is empty, terminals are laying there as usual with the piloting helmets in front of them like if someone is there.
		\nYou lose a couple of seconds looking outside the windows bridge where you can contemplate the vastness of the space and the uncountable stars.""")
	c.printer()
	sleep(2)
	p = stamp("Wait! There's really someone at one terminal!!!")
	p.printer()
	sleep(2)
	f = stamp(f"""\nIT'S THE CAPTAIN!
		\nYou rush to him just to discover that he is already dead, while honoring his death you discover that he wrote something on a paper :{pod_phrase}:
		\nWhile trying to understand what it could mean you clumsily press a button and your attention is captured by the flickering screen beeping""")
	f.printer()
	sleep(2)
	l = stamp("""\n
		\nSELF-DESTRUCTION ACTIVATED - T minus 4 minutes remaining\n""")
	l.printer()
	sleep(1)
	m = stamp("""\nDefinitely you need to get that escape pod. You run into the dining room""")
	m.printer()
	
	alarm = True
	return dining_room()

def library(): # in here there is the other half ot the code for the escape pod
	global dining, alien

	options = 'attack, roll or back'

	if alarm == True and alien == True:
		a = stamp(f"""\nEverything is dark. Except for a tiny light on the other side of the room.
			\nMoved by curiosity you move close only to realize that is an alien trying to understand a book.
			\nHe noticed you and he is preaparing to jump on you.\nWhat do you do? {options}.""")
		a.printer()
		pick = input('''\n> ''')

		if pick == 'roll' and weapon == True:
			d = stamp("The alien jumps on you with his claws but quick on your draw you polverize it with your gun")
			d.printer()
			alien = False
			return inside_library()
		else:
			p = ("Quickly you try to make a move but weaponless you couldn't do much and it rips apart your chest with his claws.")
			for c in p:
				sleep(0.1)
				print(c, end='', flush=True)
			return death()

	if alarm == False and alien == True:
		j = stamp(f"""\nThe emergency light waves his red creepy light all around the room making \nyou notice that there's someone on the other side of the room.\n""")
		j.printer()
		sleep(1)
		o = stamp(f"""\nWhen you get closer you realize that is an alien trying to understand how to read a book. Quirky.\nHe hasn't noticed you yet, what do you do? {options}""")
		o.printer()

		pick = input('''\n> ''')

		if pick == 'attack' and weapon == True:
			m = stamp("You point your weapon at it, he notices you but it's too late for him")
			m.printer()
			alien = False
			return inside_library()
		if pick == 'back':
			p = ("""You run for your life outside that hell!.""")
			for c in p:
				sleep(0.01)
				print(c, end='', flush=True)
			wake = True
			return wake_room()
		else:
			p = ("Quickly you try to make a move but weaponless you couldn't do much and it rips apart your chest with his claws.")
			for c in p:
				sleep(0.1)
				print(c, end='', flush=True)
			return death()
	else:
		g = stamp(f"""\nThe library it's still the same, Beatty used to keep it disorganized; 'It helps to discover new things'.
			\nShe used to say, close to a dead body there's an open book left in haste, you can read :{phrase_pod}:)\n""")	

		return wake_room()

def inside_library():
	
	sleep(3)
	l = stamp('\nYou sit on a chair to recover from the fright and you notice a body.\n')
	l.printer()
	sleep(2)
	n = stamp("You approach it and you touch the east shoulder hoping the best but it fall on the ground lifeless.")
	n.printer()
	sleep(2)
	m = stamp(f"\nWhile looking around you notice a book opened recently and left in a rush, you look into the page and discover this phrase :{phrase_pod}: but it doesn't seems anything to you. ")
	m.printer()
	dining = True
	return dining_room()

def dining_room():
	global search_dining, enemies, wake, dining

	if alarm == True and enemies == True: #when the players enters the next north room(main) the alarm gets deactivated and he get attacked
		
		options = 'shoot, threat or run off'
		p = stamp(f'A group of aliens jumps out from the elevator, they notice you and point their guns. {options}')
		p.printer()

		pick = input('''\n> ''')

		if pick == 'shoot' and weapon == True:
			k = stamp("Fearless you draw your wepon but when press the trigger they have already shot you twice and you miss the target.")
			k.printer()
			return death()

		if pick == 'shoot' and weapon == False:
			l = stamp("Your hand reach instinctively the empty gun holder making the aliens shoot before realizing you were unarmed.")
			l.printer()
			return death()
			
		if pick == 'threat' and bomb == True:
			d = stamp("You use their attention to make them notice that you carry a triggered bomb")
			d.printer()
			enemies = False
			s = stamp("They realize the danger and retreat to the elevator while you make your way to the door.")
			s.printer()
			wake = True
			return wake_room()
		if pick == 'threat' and bomb == False:
			h = ("You try your best to fool them into thinking you are holding a real bomb in your hand, but you weren't convincing enough")
			h.printer()
			return death()
		if pick == 'run off':
			w = ("Scared, you make dietrofront and try to reach the previous room but...")
			w.printer()
			return death()
		else:
			f = stamp('Poor untrained monkey.')
			f.printer()
			return death()

	d = stamp(f"""The light is fuzzy you can barely distinguish objects.
		\nYou can distinguish the dinner table but everything is scattered across the room like if a tornado just passed by.
		\nWhat do you do?""")
	d.printer()

	daddy = 'tette'
	choice = 'r'

	while choice != daddy:
		choice = input(f'''
{burla}:
> ''')

		if choice == 'north':
			return main()
		if choice == 'west':
			f = stamp("There is an elevator but it appears to be locked")
			f.printer()
		if choice == 'south':
			wake = True
			return wake_room()
		if choice == 'east':
			return library()
		if choice == 'search' and search_dining == True:
			g = stamp(f"{not_available}")
			g.printer()
		if choice == 'search' and search_dining == False:
			z = stamp(f"Looking on the table you find {armory_code}")
			z.printer()
			search_dining = True 

def armory(): #in here the player retrieve the weapons to survive through the game the code is obtained through 'search' in the dining room
	global bomb, weapon, wake

	options = "try or back"

	h = stamp(f'You enter inside a dark tunnel that later reveal a massive door locked by a keypad, you can:{options}')
	h.printer()

	choice = input("""
> """)

	if choice == 'try':
		l = stamp("There's the armory pad waiting numbers" )
		l.printer()
		cheat = 852
		guess = int(input("""\n[keypad]> """))
		
		if guess == armory_code or guess == cheat:
			p = stamp('\nACCESS GRANTED -- WELCOME BACK CAPTAIN HASTE')
			p.printer()
			sleep(4)
			k = stamp('\nThe door opens slowly revealing what it was hiding')
			k.printer()
			sleep(3)
			m = stamp("\nThis is the armory, you feel relief while surrounded by several weapons like: rifles, shotguns, pistols and carbines! Which one do you pick?")
			m.printer()
			
			weapons = {'rifle', 'pistol', 'shotgun', 'carbine', }
			pick = 'e'
			daddy = 'tette'

			while daddy == 'tette':

				pick = input('''
> ''')

				if pick == 'search' and bomb == True:
					not_available

				if pick == 'search' and bomb == False:
					j = stamp('You notice a little sphere hiding beneath a big gun, you look closer and you discover a proton bomb')
					j.printer() # testing -- avoid this interaction if already picked
					bomb = True 
				
				if pick == 'pistol':
					v = stamp("When you pick up your wepon you notice a little sphere, you look closer and you discover that is a proton bomb.")
					v.printer()
					weapon = True
					bomb = True
					wake = True
					return wake_room()

				if pick in weapons:
					l = stamp('What a powerful weapon!')
					l.printer()
					weapon = True 
					wake = True
					return wake_room()

				else:
					k = stamp(f'please choose among the weapon listed {weapons}\n')
					k.printer()
		else:
			c = stamp('DOOR LOCKED - PERMISSION CODE REQUIRED')
			c.printer()
			wake = True
			return wake_room()
	if choice == 'back':
		wake = True
		return wake_room()

	else:
		g = stamp('DOOR LOCKED - CODE REQUIRED')
		g.printer()
		wake = True
		return wake_room()


def finished():
	f = stamp('Good job, you won. Do you want to play again?')
	f.printer()
	
	yes = {'yes', 'y', 'yeah', 'ye', ''}
	no = {'no', 'n', 'nah'}
	
	pick = input('\n> ')

	if pick in yes:
		g = stamp("With pleasure, my friend")
		g.printer()
		alarm = False
		enemies = True
		search_dining = False
		bomb = False
		weapon = False
		wake = False
		dining = False
		return wake_room()
	if pick in no:
		l = stamp("It's been a pleasure. Goodbye")
		l.printer()
		exit()
	else:
		print(f"Even a monkey could have guessed among {yes} or {no}")
		exit()

def escape_pod(): # last room positioned behind the wake room (south)
	global wake
	options = "try or back"
	p = stamp(f"""There is a screen saying: 

' PLEASE INSERT THE PASSPHRASE '

you can:{options}""")
	p.printer()

	choice = input("\n> ")

	if choice == 'try':
		guesses = 0

		while guesses < 9:
			guesses += 1
			guess = input("[INSERT PASSPHRASE]> ")

			if guess == passphrase:
				return finished()
			if guess != passphrase:
				print("E R R O R!")

		else:
			wake = True
			return wake_room()
	
	if choice == 'back':
		wake = True
		return wake_room()

	else:
		g = stamp('DOOR LOCKED - PASSPHRASE REQUIRED')
		g.printer()
		wake = True
		return wake_room()

def wake_room():

	if wake == True:
		w = stamp("\nBack to the beginning! You're standing in the middle of the room, which way do you choose?")
		w.printer()
	if wake == False:
		welcome = stamp(f"""Welcome aboard of the commercial spacecraft CSS A Z U R A registered to the Weyland-Yutani Corporation named in honor to the daedric prince of dusk and dawn. The mother of the rose, Queen of the sky.
			\nUnknown alien beings have invaded your ship and during the fight for survival you lost contact with your crew.
			\nNow you could be the last one, but hope is not dead yet.\nThe emergency lockdown is yelling out loud, to deactivate it you need to go to the main room which is two rooms north.
			\nRemember the jolly command 'search' is available sometimes and won't be prompted! Try it! \nNow your standing, ready to go. Which way do you choose?""")
		welcome.printer()


	daddy = 'tette'
	choice = 'r'
	while choice != daddy:
		choice = input(f'''
{burla}:
> ''')

		if choice == 'north':
			dining_room()
		if choice == 'west':
			return armory()
		if choice == 'south':
			return escape_pod()
		if choice == 'east':
			g = stamp("You walk through a long dark corridor until you almost hit the door with your nose.\n")
			g.printer()
			return library()
		if choice == 'search':
			f = stamp(f'{not_available}')
			f.printer()

wake_room()