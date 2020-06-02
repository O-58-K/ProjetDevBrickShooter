# -*- coding: utf-8 -*-
import pygame
import time
from Jeu import Jeu
from Joueur import Joueur

pygame.init()
pygame.display.set_caption("Brick Shooter")                       # définition du nom de la fenêtre
fenetre = pygame.display.set_mode((549,700))                      # définition des dimensions de la fenêtre de jeu
Fond = pygame.image.load("image/image.jpg").convert()             # affichage du fond de l'écran de jeu
accueil = pygame.image.load("image/image3.jpg")
logo = pygame.image.load("image/logo.png")

#---------------------------------------------------#
# bouton start
bouton = pygame.image.load("image/startbouton.png")
bouton = pygame.transform.scale(bouton, (90, 40))
boutonPos = bouton.get_rect() 
boutonPos.x = 30
boutonPos.y = 350
#---------------------------------------------------#
# bouton quitter
bouton2 = pygame.image.load("image/quittebouton.png")
bouton2 = pygame.transform.scale(bouton2, (40, 40))
boutonPos2 = bouton2.get_rect() 
boutonPos2.x = 480
boutonPos2.y = 352
#---------------------------------------------------#
# bouton info
bouton3 = pygame.image.load("image/infobouton.png")
bouton3 = pygame.transform.scale(bouton3, (40, 40))
boutonPos3 = bouton3.get_rect() 
boutonPos3.x = 420
boutonPos3.y = 352
#---------------------------------------------------#
# # bouton retour
# retour = pygame.image.load("image/retour.png")
# retour = pygame.transform.scale(retour, (40, 40))
# retourPos = retour.get_rect() 
# retourPos.x = 480
# retourPos.y = 352

jeu = Jeu()
run = True
Info = False
# Retour = False

while run:                                                        # la boucle du jeu (tant que 'run' est vrai, la boucle tourne sans cesse)

  fenetre.blit(Fond, (0, 0))
    
  if jeu.start:
    jeu.startGame(fenetre)
  elif Info:
    fenetre = pygame.display.set_mode((1500, 400))
      
    Fond = pygame.font.Font(None, 24)
    text = Fond.render("Instructions du jeu :",1,(0,255,255))
    text2 = Fond.render("Le jeu 'Brick Shooter' est un jeu dans lequel nous devons détruire des briques arrivant depuis le haut de la fenêtre",1,(255,255,255))
    text3 = Fond.render("TOUCHES : Flèche-GAUCHE | Flèche-DROITE | ESPACE",1,(255,255,255))

    fenetre.blit(text, (80, 100))
    fenetre.blit(text2, (80, 140))
    fenetre.blit(text3, (80, 160))

    if jeu.touche.get(pygame.K_ESCAPE):
      Info = False
    # fenetre.blit(retour, (480, 352))
  # elif jeu.fin:
  #    jeu.perdu(fenetre)
  #    # jeu.start = False
  else:
    jeu.start = False
    fenetre.blit(logo,(150, 50)) 
    fenetre.blit(accueil,(150, 400))
    fenetre.blit(bouton, (30, 350))                               # affiche la position du bouton de commencement dans la fenetre du jeu                                    
    fenetre.blit(bouton2, (480, 352))
    fenetre.blit(bouton3, (400, 352)) 

  pygame.display.flip()    

  while Info:
    fenetre = pygame.display.set_mode((1500, 400))
      
    Fond = pygame.font.Font(None, 20)
    text = Fond.render("Instructions du jeu :",1,(0,255,255))
    text2 = Fond.render("Le jeu 'Brick Shooter' est un jeu dans lequel nous devons détruire des briques arrivant depuis le haut de la fenêtre, TOUCHES : Flèche-GAUCHE | Flèche-DROITE | ESPACE",1,(255,255,255))

    fenetre.blit(text, (680, 100))
    fenetre.blit(text2, (80, 140))
    # fenetre.blit(retour, (480, 352))

    if jeu.touche.get(pygame.K_ESCAPE):
      Info = False

    for event in pygame.event.get():                        
      if event.type == pygame.QUIT:                         
        run = False 
        pygame.quit()

  for event in pygame.event.get():                        
    if event.type == pygame.QUIT:                         
      run = False                                                 # la boucle 'run' s'arrête
      pygame.quit()                                               # fermeture
    elif event.type == pygame.KEYDOWN:                            # si la touche actionnée en question est appuyée, la valeur passe à vraie
      jeu.touche[event.key] = True
      if event.key == pygame.K_SPACE:                             # active le tir lorsque le joueur actionne la touche 'espace'
        jeu.joueur.Tirs()
    elif event.type == pygame.KEYUP:                              # si la touche actionnée en question n'est plus appuyée, la valeur passe à faux
      jeu.touche[event.key] = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if boutonPos.collidepoint(event.pos):
          jeu.start = True
      elif boutonPos2.collidepoint(event.pos):
          pygame.quit()
      elif boutonPos3.collidepoint(event.pos):
          Info = True
      # elif retourPos.collidepoint(event.pos):
      #     pygame.quit()

          