import pygame
import random

#rows, cols = (480, 480)
#all_points = [[0 for i in range(cols)] for j in range(rows)]

# ^ THE HOLY CODE





class Weapon:

    all = []

    def __repr__(self):
        return f"Weapon('name={self.name}', damage={self.damage}, speed={self.speed}, type={self.type}, range={self.range}, knockback={self.knockback}, slowdown={self.slowdown}, angle={self.angle}, charge_time={self.charge_time}, locks_aim={self.locks_aim})"

    def __init__(self, name: str, damage: float, speed: float, type: str, range: float, life_time: float, knockback=0, slowdown=0.0, angle=0.0, charge_time=0.0, locks_aim=False):

        #validate
        assert damage >= 0, f"Damage {damage} is negative! You don't want to heal the enemies, dummy!"
        assert speed >= 0, f"Speed {speed} is negative! yeah it is.."

        #assign mandatory
        self.name = name
        self.damage = damage
        self.speed = speed
        self.type = type
        self.range = range
        self.life_time = life_time

        #assign optional
        self.knockback = knockback
        self.slowdown = slowdown
        self.angle = angle
        self.charge_time = charge_time
        self.locks_aim = locks_aim

        #actions to execute
        Weapon.all.append(self)

class Entity:
    all = []

    def __repr__(self):
        return f"Entity(weapon={self.weapon}, x_cord={self.x_cord}, y_cord={self.y_cord}, size={self.size}, max_health={self.max_health}, current_health={self.current_health}, is_player={self.is_player})"

    def __init__(self, weapon, x_cord, y_cord, size, max_health, current_health, movement, is_player=False):

        self.weapon = weapon
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.size = size
        self.max_health = max_health
        self.current_health = current_health
        self.movement = movement

        self.is_player = is_player

    def move(self):
        self.x_cord = self.x_cord + 0.33*self.movement[0]
        self.y_cord = self.y_cord + 0.33*self.movement[1]


knife = Weapon("Knife", 5, 5, "hitscan", 1.5, 5)
sword = Weapon("Sword", 10, 3, "sweep", 2.7, 10, 0, 0.5, 15)



if __name__ == '__main__':
    screen = pygame.display.set_mode((1280,720))
    pygame.mixer.init()

    g_player_unlocked = pygame.image.load("player_unlocked.png").convert_alpha()
    g_player_locked = pygame.image.load("player_locked.png").convert_alpha()



    player_weapon = Weapon.all[random.randint(0, len(Weapon.all)-1)]

    player = Entity(player_weapon, 0, 0, 1, 10, 10, [0,0], True)
    print(player)

    running = True


    while running:
        screen.fill((0,0,0))

        screen.blit(g_player_unlocked, (player.x_cord, player.y_cord))

        player.move()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_DOWN:
                    player.movement[1] = 1
                elif event.key == pygame.K_UP:
                    player.movement[1] = -1
                elif event.key == pygame.K_RIGHT:
                    player.movement[0] = 1
                elif event.key == pygame.K_LEFT:
                    player.movement[0] = -1

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP and player.movement[1] == -1) or (event.key == pygame.K_DOWN and player.movement[1] == 1):
                    player.movement[1] = 0
                elif (event.key == pygame.K_RIGHT and player.movement[0] == 1) or (event.key == pygame.K_LEFT and player.movement[0] == -1):
                    player.movement[0] = 0

        pygame.display.update()