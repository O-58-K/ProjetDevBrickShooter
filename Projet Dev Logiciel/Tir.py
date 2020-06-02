import pygame

#---------------------------------------------#
# définition de la classe pour le tir du joueur
class Tir(pygame.sprite.Sprite):                
    def __init__(self, joueur):
        super().__init__()
        self.vitesse = 10
        self.image = pygame.image.load("image/tir.png")
        self.joueur = joueur
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 20
        self.rect.y = joueur.rect.y + 20

    def Suppr(self):
        #------------------------------#
        # fonction de suppression du tir
        self.joueur.tirT.remove(self)

    def Depl(self):
        self.rect.y -= self.vitesse
        #----------------------------------------------#
        # le tir se supprime lorsqu'il touche une brique
        for brique in self.joueur.jeu.collision(self, self.joueur.jeu.briqueT): 
            self.Suppr()
            brique.degats(self.joueur.attaque)
        #---------------------------------------------------------------------------------------------------------#
        # supprime les briques ne se trouvant plus dans la zone visible par le joueur (en dehors de la zone de jeu)
        if self.rect.y < 0 :
            self.Suppr()
