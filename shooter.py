import pygame, random
#Tamanio de la pantalla
WIDTH = 800
HEIGHT = 600
#Color Keys para los sprites
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

#Inicio
pygame.init()
#Declaracion de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#Titulo de la ventana
pygame.display.set_caption("Food Race V0.9 Alpha")
#Reloj para el juego
clock = pygame.time.Clock()

#Clase jugador, contiene su imagen, coordenadas y velocidad
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/player2.png").convert()
		self.image = pygame.transform.scale(self.image, (50,80))
		self.image.set_colorkey(GREEN)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

#Clase sano (Alimentos Sanos), selecciona su imagen, coordenadas y velocidad
class Sano(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(sanos_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 10)

#Clase Malo (Alimentos Malos), selecciona su imagen, coordenadas y velocidad
class Malo(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(malos_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 10)

#Clase Sello, selecciona su imagen, coordenadas y velocidad
class Sello(pygame.sprite.Sprite):
	def __init__(self, numero):
		super().__init__()
		self.image = sellos_img[numero]
		self.image.set_colorkey(GREEN)
		self.rect = self.image.get_rect()
		self.rect.x = 55 * numero
		self.rect.y = 10
		self.speedy = 0
		self.speedx = 0

#Función para dibujar texto en pantalla
def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("Comic Sans MS", size)
	text_surface = font.render(text, True, BLACK)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

#Función para mostrar la pantalla de inicio
def show_go_screen():
	screen.blit(background, [0,0])
	draw_text(screen, "Food Race", 65, WIDTH // 2, 10)
	draw_text(screen, "El juego foot race consiste en mostrar a los niños pequeños que la mala alimentación", 18, WIDTH // 2, 100)
	draw_text(screen, "trae consecuencias por lo tanto las siguientes reglas se aplicaran al juego:", 18, WIDTH // 2, 120)

	draw_text(screen, "1.- El personaje no deberá comer ningún alimento", 18, WIDTH // 2, 150)
	draw_text(screen, "chatarra para que puedan continuar el juego", 18, WIDTH // 2, 170)

	draw_text(screen, "2.- Tendrá 4 oportunidades al tocar alimentos chatarra, una", 18, WIDTH // 2, 200)
	draw_text(screen, "vez que como cuatro alimentos chatarra el juego acabara", 18, WIDTH // 2, 220)

	draw_text(screen, "3.-Cada que el personaje coma un alimento chatarra, en la ", 18, WIDTH // 2, 250)
	draw_text(screen, "pantalla se mostrara uno de los tres sellos de nutrición ", 18, WIDTH // 2, 270)
	draw_text(screen, "así podremos mostrarles que el juego esta por terminar.", 18, WIDTH // 2, 290)

	draw_text(screen, "4.- Si el jugador come alimentos saludables irá", 18, WIDTH // 2, 320)
	draw_text(screen, "aumentando su puntuación", 18, WIDTH // 2, 340)

	draw_text(screen, "Presiona cualquier tecla", 20, WIDTH // 2, HEIGHT * 3/4)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False

#Función para mostrar la pantalla de Game Over
def show_dead_screen():
	screen.blit(background, [0,0])
	draw_text(screen, "Has Perdido", 65, WIDTH // 2, HEIGHT // 4)
	draw_text(screen, "Alimentate sanamente, eres lo que comes", 27, WIDTH // 2, HEIGHT // 2)
	draw_text(screen, "Presiona [SPACE] para jugar de nuevo", 20, WIDTH // 2, HEIGHT * 3/4)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					waiting = False

	#Listas de imagenes
#Lista de alimentos sanos
sanos_images = []
sanos_list = ["assets/frutas/1.png","assets/frutas/2.png","assets/frutas/3.png",
				"assets/frutas/4.png","assets/frutas/5.png","assets/frutas/6.png"]
#Se cargan las imagenes, se escalan y se agregan
for img in sanos_list:
	frutatemp = pygame.image.load(img).convert()
	frutatemp = pygame.transform.scale(frutatemp, (60,60))
	sanos_images.append(frutatemp)
	
#Lista de alimentos malos
malos_images = []
malos_list = ["assets/malos/1.png", "assets/malos/2.png","assets/malos/3.png",
				"assets/malos/4.png","assets/malos/5.png",]
#Se cargan las imagenes, se escalan y se agregan
for imgMalo in malos_list:
	imgtemp = pygame.image.load(imgMalo).convert()
	imgtemp = pygame.transform.scale(imgtemp, (60,60))
	malos_images.append(imgtemp)

#Lista de sellos
sellos_img = []
sellos_list = ["assets/sellos/01.png","assets/sellos/02.png","assets/sellos/03.png","assets/sellos/03.png"]
#Se cargan las imagenes
for imgSello in sellos_list:
	sellos_img.append(pygame.image.load(imgSello).convert())

#Carga del fondo del juego
background = pygame.image.load("assets/back1.png").convert()

running = True
game_over = True

#Se muestra la pantalla de inicio
show_go_screen()
#Ciclo del juego mientras siga jugando "Game Over"
while running:
	if game_over:
		game_over = False

		#Se agregan las imagenes como un grupo
		all_sprites = pygame.sprite.Group()
		sanos_list = pygame.sprite.Group()
		malos_list = pygame.sprite.Group()
		sellos_list = pygame.sprite.Group()

		#Se inicializa el jugador y se agrega al juego
		player = Player()
		all_sprites.add(player)

		#Se cargan 7 alimentos sanos aleartorios
		for i in range(7):
			sano = Sano()
			all_sprites.add(sano)
			sanos_list.add(sano)

		#Se cargan 5 alimentos malos aleartorios
		for i in range(5):
			malos = Malo()
			all_sprites.add(malos)
			malos_list.add(malos)

		#Se declara el Score y los Fallos en 0
		score = 0
		fallos = 0

	#Control del reloj en 60 FPS
	clock.tick(60)
	#Control de Quit del juego
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#Se actualizan las imagenes (sprites)
	all_sprites.update()

	#Colisiones de los objetos sanos
	hits = pygame.sprite.spritecollide(player, sanos_list, True)
	#Si un objeto sano choca con el jugador, se suma su puntacion y se 
	#aniade otro objeto sano
	for hit in hits:
		score += 5
		sano = Sano()
		all_sprites.add(sano)
		sanos_list.add(sano)

	#Colisiones de los objetos malos
	hits1 = pygame.sprite.spritecollide(player, malos_list, True)
	#Si un objeto malo choca con el jugador, se aumenta un fallo y se 
	#aniade otro objeto malo
	for hit in hits1:
		fallos +=1
		malo = Malo()
		sello = Sello(fallos-1)
		all_sprites.add(sello)
		sellos_list.add(sello)
		all_sprites.add(malo)
		malos_list.add(malo)
		#Si falla 4 veces se mandara la pantalla de game over
		if fallos == 4:
			show_dead_screen()
			game_over = True

	#Se dibuja el fondo del juego
	screen.blit(background, [0, 0])
	#Se dibujan todas las imagenes en pantalla
	all_sprites.draw(screen)

	#Se dibuja el marcador del score en pantalla
	draw_text(screen, str(score), 25, WIDTH // 2, 10)
	#Se actualiza la pantalla
	pygame.display.flip()

#Fin del juego
pygame.quit()