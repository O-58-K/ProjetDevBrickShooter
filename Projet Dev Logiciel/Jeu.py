import pygame
from Joueur import Joueur
from Brique import Brique, Brique2
import time

class Jeu:
  def __init__(self):
    self.start = False
    self.joueurs = pygame.sprite.Group()        
    self.joueur = Joueur(self)                  
    self.joueurs.add(self.joueur)               
    self.briqueT = pygame.sprite.Group()
    self.touche = {}
    self.apparitionBrique()
    self.apparitionBrique()
    self.apparitionBrique()
    self.apparitionBrique()

  def apparitionBrique(self):
    brique = Brique(self)
    brique2 = Brique2(self)
    self.briqueT.add(brique, brique2)

  def collision(self, sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

  def startGame(self, fenetre):

    fenetre.blit(self.joueur.image, self.joueur.rect) 

    for Tirs in self.joueur.tirT:
      Tirs.Depl()
    for brique in self.briqueT:
      time.sleep(0.003)                                              # pause
      brique.Avance()
      brique.VieChange(fenetre)
    for brique2 in self.briqueT:
      time.sleep(0.003)                                              # pause
      brique2.Avance()
      brique2.VieChange(fenetre)

    self.joueur.VieChange(fenetre)                                   # affiche la jauge de vie du joueur
    self.joueur.tirT.draw(fenetre)                                   # affiche le tir du joueur 
    self.briqueT.draw(fenetre)                                       # affiche les briques 

    if self.touche.get(pygame.K_RIGHT) and self.joueur.rect.x < 485:  # définie la distance sur laquelle le joueur peut se déplacer (limite de la partie droite de la fenêtre)
      self.joueur.Dep_Droite()                                       # déplacement à droite
    elif self.touche.get(pygame.K_LEFT) and self.joueur.rect.x > 0:   # définie la distance sur laquelle le joueur peut se déplacer (limite de la partie gauche de la fenêtre)
      self.joueur.Dep_Gauche()                         
    elif self.touche.get(pygame.K_ESCAPE):
      self.start = False

  # def info(self, fenetre, jeu):
      
  #     fenetre = pygame.display.set_mode((1500, 400))
      
  #     Fond = pygame.font.Font(None, 24)
  #     text = Fond.render("Instructions du jeu :",1,(0,255,255))
  #     text2 = Fond.render("Le jeu 'Brick Shooter' est un jeu dans lequel nous devons détruire des briques arrivant depuis le haut de la fenêtre, TOUCHES : Flèche-GAUCHE | Flèche-DROITE | ESPACE",1,(255,255,255))

  #     fenetre.blit(text, (680, 100))
  #     fenetre.blit(text2, (80, 140))

  # def perdu(self, fenetre):
  #   fenetre = pygame.display.set_mode((1317,568))
  #   Fond = pygame.image.load("image/image2.png").convert()
  #   fenetre.blit(Fond, (0, 0))

