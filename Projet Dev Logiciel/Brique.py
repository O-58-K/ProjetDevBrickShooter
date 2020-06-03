import pygame 
import random 
#--------------------------------------------------#
# définition de la classe pour la brique de niveau 1
class Brique(pygame.sprite.Sprite): 

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu 
        self.pointVie = 10
        self.Max_pointVie = 10
        self.attaque = 12
        self.image = pygame.image.load('image/virus2.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 485)                # horizontal
        self.rect.y = 0                                     # vertical
        self.vitesse = 1

    def Suppr(self):
        #---------------------------------------#
        # fonction de suppression de(s) brique(s)
        self.jeu.briqueT.remove(self)

    def degats(self, nombre):
        self.pointVie -= nombre
        if self.pointVie <= 0 :
            self.rect.x = random.randint(0, 485) 
            self.rect.y = 0
            self.pointVie = self.Max_pointVie

    def VieChange(self, place):
        (120,224,51)
        [self.rect.x, self.rect.y - 10, self.pointVie, 4]
        
    def Avance(self):
        if not self.jeu.collision(self, self.jeu.joueurs):
            self.rect.y += self.vitesse 
        else:
            self.jeu.joueur.degats(self.attaque, self.jeu)
        if self.rect.y > 730 :
            # self.rect.x = random.randint(0, 485) 
            # self.rect.y = 0
            # self.pointVie = self.Max_pointVie 
            # self.jeu.joueur.vie = 1
            print('')
            print("Game Over !")
            print("Vous êtes contaminé !")
            print('')
            pygame.quit()


#---------------------------------------------------------#            
# définition de la classe pour les briques de niveaux 2 à 4
class Brique2(pygame.sprite.Sprite):  

    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.pointVie = l = random.randint(30, 60)
        self.Max_pointVie = l
        self.attaque = random.randint(20, 35)
        self.image = pygame.image.load('image/virus3.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 485)                # horizontal
        self.rect.y = 0                                     # vertical
        self.vitesse = 1

    def Suppr(self):
        #---------------------------------------#
        # fonction de suppression de(s) brique(s)
        self.jeu.briqueT.remove(self)

    def degats(self, nombre):
        self.pointVie -= nombre
        if self.pointVie <= 0 :
            self.rect.x = random.randint(0, 485) 
            self.vitesse = 1
            self.rect.y = 0
            self.pointVie = self.Max_pointVie
            
    def VieChange(self, place):
        (120,224,51)
        [self.rect.x, self.rect.y - 10, self.pointVie, 4]

    def Avance(self):
        if not self.jeu.collision(self, self.jeu.joueurs):
            self.rect.y += self.vitesse 
        else:
            self.jeu.joueur.degats(self.attaque, self.jeu)
        if self.rect.y > 730 :
            print('')
            print("Game Over !")
            print("Vous êtes contaminé !")
            print('')
            pygame.quit()
