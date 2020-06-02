import pygame
from Tir import Tir 

#----------------------------------------------------------------#
# définition de la classe pour le joueur (et ses caractéristiques)
class Joueur(pygame.sprite.Sprite): 
  
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu 
        self.vie = 100
        self.max_vie = 100
        self.attaque = 20
        self.vitesse = 20
        self.image = pygame.image.load("image/joueur.png")
        self.rect = self.image.get_rect()
        self.tirT = pygame.sprite.Group()
        self.rect.x = 240
        self.rect.y = 570

    def Tirs(self):
        self.tirT.add(Tir(self))

    def Dep_Droite(self):
        if not self.jeu.collision(self, self.jeu.briqueT): 
            self.rect.x += self.vitesse

    def Dep_Gauche(self):
        if not self.jeu.collision(self, self.jeu.briqueT): 
            self.rect.x -= self.vitesse 
    
    def VieChange(self, place):
        pygame.draw.rect(place, (120,210,47), [self.rect.x - 15 , self.rect.y - 20, self.vie, 4])

    def degats(self, nombre, jeu):
        if self.vie - nombre >= 0:
            self.vie -= nombre
        elif self.vie - nombre <= 0:

            print('')
            print("Game Over !")
            print("Vous avez été touché !")
            print('')
            pygame.quit()
            
