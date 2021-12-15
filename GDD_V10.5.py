# GDD - JOGO - MEGAMI: FINAL BATTLE
#
# ------------------------------------------------------------------

# para usar números aleatórios

# para usar PyGame
import pygame
from pygame.locals import *

# início do programa
# ( (int(input("Valor de R: "))) , (int(input("Valor de G: "))) , ( int(input("Valor de B: "))) )

CorStart = (0, 0, 0)
CorSelect = (0, 68, 85)
CorFundo = (135, 108, 47)
CorCirculo = (255, 0, 0)
CorLinha = (128, 0, 0)
CorRetangulo = (0, 0, 0)

# ---------------------------------------
# Tamanho tela.
Tela_X = 900
Tela_Y = 600

# ---------------------------------------

# ---------------------------------------
# Tamanho Figura
Tamanho_Figura = 48
# ---------------------------------------

# ---------------------------------------
# Tiro Tanque
X_Tiro1_A = 50
Y_Tiro1_A = 150
Set_X_Tiro1_A = 0
TankTiro1_A = 0
Tiro1_A = []
# ---------------------------------------

# Tiro Tanque 2 B
X_Tiro2_B = 850
Y_Tiro2_B = 400
Set_X_Tiro2_B = 0
TankTiro2_B = 0
Tiro2_B = []

# ---------------------------------------
# Tanques

TankPos1_A = 2

# Tanque 1 A
X_tank1_A = X_Tiro1_A
Y_tank1_A = Y_Tiro1_A

# Tanque 2 B

X_tank2_B = 800
Y_tank2_B = 500

TankPos2_B = 6

Select_inicial_Tanque = []
# ---------------------------------------
# Tanques Cores
#########################
# Tanque Vermelho

Tank1_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank1.png")
Tank2_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank2.png")
Tank3_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank3.png")
Tank4_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank4.png")
Tank5_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank5.png")
Tank6_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank6.png")
Tank7_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank7.png")
Tank8_Vermelho = pygame.image.load("Imagem_tanque_vermelho/tank8.png")
Tank_Vermelho = [Tank1_Vermelho, Tank2_Vermelho, Tank3_Vermelho, Tank4_Vermelho, Tank5_Vermelho, Tank6_Vermelho,
                 Tank7_Vermelho, Tank8_Vermelho]

# Tanque Verde
Tank1_verde = pygame.image.load("Imagem_tanque_verde/tank1.png")
Tank2_verde = pygame.image.load("Imagem_tanque_verde/tank2.png")
Tank3_verde = pygame.image.load("Imagem_tanque_verde/tank3.png")
Tank4_verde = pygame.image.load("Imagem_tanque_verde/tank4.png")
Tank5_verde = pygame.image.load("Imagem_tanque_verde/tank5.png")
Tank6_verde = pygame.image.load("Imagem_tanque_verde/tank6.png")
Tank7_verde = pygame.image.load("Imagem_tanque_verde/tank7.png")
Tank8_verde = pygame.image.load("Imagem_tanque_verde/tank8.png")
Tank_Verde = [Tank1_verde, Tank2_verde, Tank3_verde, Tank4_verde, Tank5_verde, Tank6_verde, Tank7_verde, Tank8_verde]

# Tanque Amarelo
Tank1_azul = pygame.image.load("Imagem_tanque_azul/tank1.png")
Tank2_azul = pygame.image.load("Imagem_tanque_azul/tank2.png")
Tank3_azul = pygame.image.load("Imagem_tanque_azul/tank3.png")
Tank4_azul = pygame.image.load("Imagem_tanque_azul/tank4.png")
Tank5_azul = pygame.image.load("Imagem_tanque_azul/tank5.png")
Tank6_azul = pygame.image.load("Imagem_tanque_azul/tank6.png")
Tank7_azul = pygame.image.load("Imagem_tanque_azul/tank7.png")
Tank8_azul = pygame.image.load("Imagem_tanque_azul/tank8.png")
Tank_azul = [Tank1_azul, Tank2_azul, Tank3_azul, Tank4_azul, Tank5_azul, Tank6_azul, Tank7_azul,
             Tank8_azul]

# Tanque cor
Tank_Cor = [Tank1_Vermelho, Tank1_verde, Tank1_azul]
Selecao_cor = 0

Tank_A = Tank_Vermelho
Tank_B = Tank_Verde

# --------------------------------------


# ---------------------------------------
# Tempo do tanque
TankTemp = 3
Tempo1_A = 0
Tempo2_B = 0

# ---------------------------------------
# Placar


Placar_A = []
PlacarATotal = pygame.image.load("Imagem_Placar/numero.png")  # lê o arquivo de sprite com

i = 0
while i < 7:  # executa o clipping da imagem que possuem largura = xx e altura = xx
    placar_parte = PlacarATotal.subsurface([i * 37, 0, 37, 38])  # subsurface executa o clipping
    Placar_A.append(placar_parte)  # inclue a superfície clipada na lista
    i = i + 1

Placar_B = Placar_A

Placar_A_Soma = 0
Placar_B_Soma = 0

Logo1 = pygame.image.load("Imagem_Placar/megami.png")
Logo2 = pygame.image.load("Imagem_Placar/megami1.png")

#deltaX= 113
#deltaY = 35

deltaX= 75
deltaY = 23

Player1_A  = pygame.image.load("Imagem_Placar/Player1.png")
#Player1_A  = pygame.transform.scale(Player1_A_default, (deltaX, deltaY))
Player2_B = pygame.image.load("Imagem_Placar/Player2.png")
Barra_cheia= pygame.image.load("Imagem_Placar/barra cheia.png")


Barra_vaziaA = []
Barra_vazia = pygame.image.load("Imagem_Placar/barra vazia.png")  # lê o arquivo de sprite com

i = 0
while i < 5:  # executa o clipping da imagem que possuem largura = xx e altura = xx
    barra_parte = Barra_vazia.subsurface([i * 23, 0, 23, 35])  # subsurface executa o clipping
    Barra_vaziaA.append(barra_parte)  # inclue a superfície clipada na lista

    i = i + 1
vaziaA=0
vaziaB=0

Barra_vaziaB=Barra_vaziaA
Logo = Logo1
Tempo_logo = 0

# ---------------------------------------
# Start
Select_inicial = []
Hud_start = pygame.image.load("Imagem_Inicio/hud_start.png")
Press_enter = pygame.image.load("Imagem_Inicio/press_enter.png")
Press_enter1 = pygame.image.load("Imagem_Inicio/press_enter1.png")
Enter = [Press_enter, Press_enter1]
# ------------------------------------------------


# ---------------------------------------
# Select figuras
selecao_fig_Tri_1 = pygame.image.load("Imagem_select/selecao_cor1.png")
selecao_fig_Tri_2 = pygame.image.load("Imagem_select/selecao_cor2.png")
player1_sel = pygame.image.load("Imagem_select/player1_sel.png")
player2_sel = pygame.image.load("Imagem_select/player2_sel.png")
Comando1 = pygame.image.load("Imagem_select/comando1.png")
Comando2 = pygame.image.load("Imagem_select/comando2.png")
sele_enter = pygame.image.load("Imagem_select/sele_enter.png")
tela_select_triangulox = 0
tela_select_trianguloy = 0
# ---------------------------------------
# Restart
Restart = []

Restart_winP1 = pygame.image.load("Imagem_Restart/restart_p1.png")
Restart_winP2 = pygame.image.load("Imagem_Restart/restart_p2.png")
reiniciar = pygame.image.load("Imagem_Restart/reiniciar.png")
Restart_Menu = [Restart_winP1, Restart_winP2, reiniciar]
Player = 0

# ---------------------------------------
# Timer selecao
timer_selecao = 30
Sele_Temp = 0  # contador

# ---------------------------------------
# Volume som
volume = 0.2

barra_modeA=0
barra_modeB =0
# -------------------------------------------------------------------
# Funções


def fundo_main():
    tela.fill(CorFundo)  # Preenche o fundo de tela

    pygame.draw.rect(tela, CorLinha, (1, 100, 898, 498), 4)
    pygame.draw.rect(tela, CorLinha, (0, 0, 900, 100), 0)
    tela.blit(Placar_A[Placar_A_Soma], (150, 50))
    tela.blit(Placar_B[Placar_B_Soma], (Tela_X - 187, 50))
    tela.blit(Barra_cheia, (20, 60))
    tela.blit(Barra_cheia, (Tela_X - 134, 60))
    tela.blit(Player1_A, (37.5, 5))
    tela.blit(Player2_B, (Tela_X - 154, 5))
    tela.blit(Logo, ((Tela_X / 2) - 179, 30))
def barraA(vaziaA):
    ##########################################################################################
    # Barra A
    if vaziaA == 1:
        tela.blit(Barra_vaziaA[vaziaA - 1], (20, 60))
    elif vaziaA == 2:
        tela.blit(Barra_vaziaA[vaziaA - 2], (20, 60))
        tela.blit(Barra_vaziaA[vaziaA - 1], (20 + 23, 60))
    elif vaziaA == 3:
        tela.blit(Barra_vaziaA[vaziaA - 3], (20, 60))
        tela.blit(Barra_vaziaA[vaziaA - 2], (20 + 23, 60))
        tela.blit(Barra_vaziaA[vaziaA - 1], (20 + (23 * 2), 60))
    elif vaziaA == 4:
        tela.blit(Barra_vaziaA[vaziaA - 4], (20, 60))
        tela.blit(Barra_vaziaA[vaziaA - 3], (20 + 23, 60))
        tela.blit(Barra_vaziaA[vaziaA - 2], (20 + (23 * 2), 60))
        tela.blit(Barra_vaziaA[vaziaA - 1], (20 + (23 * 3), 60))
    elif vaziaA == 5:
        tela.blit(Barra_vaziaA[vaziaA - 4], (20, 60))
        tela.blit(Barra_vaziaA[vaziaA - 3], (20 + 23, 60))
        tela.blit(Barra_vaziaA[vaziaA - 2], (20 + (23 * 2), 60))
        tela.blit(Barra_vaziaA[vaziaA - 1], (20 + (23 * 3), 60))
        tela.blit(Barra_vaziaA[vaziaA - 1], (20 + (23 * 4), 60))
    ##########################################################################################
    # Barra B
def barraB(vaziaB):
    if vaziaB == 1:
        tela.blit(Barra_vaziaB[vaziaB - 1], (Tela_X - 134, 60))
    elif vaziaB == 2:
        tela.blit(Barra_vaziaB[vaziaB - 2], (Tela_X - 134, 60))
        tela.blit(Barra_vaziaB[vaziaB - 1], (Tela_X - 134 + 23, 60))
    elif vaziaB == 3:
        tela.blit(Barra_vaziaB[vaziaB - 3], (Tela_X - 134, 60))
        tela.blit(Barra_vaziaB[vaziaB - 2], (Tela_X - 134 + 23, 60))
        tela.blit(Barra_vaziaB[vaziaB - 1], (Tela_X - 134 + (23 * 2), 60))
    elif vaziaB == 4:
        tela.blit(Barra_vaziaB[vaziaB - 4], (Tela_X - 134, 60))
        tela.blit(Barra_vaziaB[vaziaB - 3], (Tela_X - 134 + 23, 60))
        tela.blit(Barra_vaziaB[vaziaB - 2], (Tela_X - 134 + (23 * 2), 60))
        tela.blit(Barra_vaziaB[vaziaB - 1], (Tela_X - 134 + (23 * 3), 60))
    elif vaziaB == 5:
        tela.blit(Barra_vaziaB[vaziaB - 4], (Tela_X - 134, 60))
        tela.blit(Barra_vaziaB[vaziaB - 3], (Tela_X - 134 + 23, 60))
        tela.blit(Barra_vaziaB[vaziaB - 2], (Tela_X - 134 + (23 * 2), 60))
        tela.blit(Barra_vaziaB[vaziaB - 1], (Tela_X - 134 + (23 * 3), 60))
        tela.blit(Barra_vaziaB[vaziaB - 1], (Tela_X - 134 + (23 * 4), 60))


def som_tiro():
    pygame.mixer.music.set_volume(volume)
    Som_tiro = pygame.mixer.Sound("Sons/MP3_gunshot.mp3")
    Som_tiro.play()


def colisao():
    pygame.mixer.music.set_volume(volume)
    Som_tiro1 = pygame.mixer.Sound("Sons/MP3_gunshot1.mp3")
    Som_tiro1.play()


def som_select():
    pygame.mixer.music.set_volume(volume)
    Som_select = pygame.mixer.music.load("Sons/MP3_select.mp3")
    pygame.mixer.music.play(1, 0.0)


def som_confirm():
    pygame.mixer.music.set_volume(volume)
    Som_confirm = pygame.mixer.music.load("Sons/MP3_start.mp3")
    pygame.mixer.music.play(1, 0.0)


def som_inicio():
    pygame.mixer.music.set_volume(0.4)
    Som_confirm = pygame.mixer.music.load("Sons/MP3_jogo.mp3")
    pygame.mixer.music.play(-1)


def som_jogo():
    pygame.mixer.music.set_volume(0.4)
    Som_confirm = pygame.mixer.music.load("Sons/MP3_jogo_1.mp3")
    pygame.mixer.music.play(-1)


# Começando a usar o PyGame
pygame.init()  # |
tela = pygame.display.set_mode((Tela_X, Tela_Y), 0, 32)  # |- Inicialização do PyGame
pygame.display.set_caption('GDD - JOGO - MEGAMI: FINAL BATTLE')  # |

############################################################################################
# Pagina Inicial
som_inicio()
start = False
fim = False
selecao_player1 = False
selecao_player2 = False
restart = False
programa = False

while not programa:
    while not start:

        tela.fill(CorStart)  # Preenche o fundo de tela

        tela.blit(Hud_start, ((Tela_X / 2) - 250, 100))
        tela.blit(Enter[0], ((Tela_X / 2) - 125, 350))
        Select_inicial_Tanque = 0
        pygame.display.update()  # Atualiza tela - sem este update não haverá desenho

        Start_inicial = pygame.key.get_pressed()
        if Start_inicial[K_RETURN]:
            tela.blit(Enter[1], ((Tela_X / 2) - 125, 350))
            pygame.display.update()
            som_confirm()
            start = True
            Select_inicial_Tanque = 0
            pygame.time.delay(1000)

        for event in pygame.event.get():  # |
            if event.type == QUIT:  # |Detecta o clique para sair do pgm
                start = True  # |
                selecao_player1 = True
                selecao_player2 = True
                fim = True
                programa = True
                restart = True
                pygame.mixer.music.stop()
    ############################################################################################
    # Seleção Tanque

    while not selecao_player1:
        restart = False
        tela.fill(CorSelect)  # Preenche o fundo de tela

        tela_selectX = 200
        tela_selectY = 150
        tela.blit(Comando1, (500, 101))
        tela.blit(player1_sel, (75, 20))
        tela.blit(sele_enter, ((Tela_X / 2) - 242, 500))
        tela.blit(Tank_Cor[0], (tela_selectX, tela_selectY))
        tela.blit(Tank_Cor[1], (tela_selectX, tela_selectY + 25 + 50))
        tela.blit(Tank_Cor[2], (tela_selectX, tela_selectY + 25 + 125))
        tela.blit(selecao_fig_Tri_1, (tela_select_triangulox, tela_select_trianguloy))
        if Selecao_cor == 0:
            tela_select_triangulox = tela_selectX - 35
            tela_select_trianguloy = tela_selectY + 15
            Tank_A = Tank_Vermelho

        elif Selecao_cor == 1:
            tela_select_triangulox = tela_selectX - 35
            tela_select_trianguloy = tela_selectY + 15 + 25 + 50
            Tank_A = Tank_Verde

        elif Selecao_cor == 2:
            tela_select_triangulox = tela_selectX - 35
            tela_select_trianguloy = tela_selectY + 15 + 25 + 125
            Tank_A = Tank_azul

        pygame.display.update()  # Atualiza tela - sem este update não haverá desenho
        Select_inicial_Tanque = 0
        Select_inicial_Tanque = pygame.key.get_pressed()

        if Select_inicial_Tanque[K_RETURN]:
            tela.blit(selecao_fig_Tri_2, (tela_select_triangulox, tela_select_trianguloy))
            pygame.display.update()
            som_confirm()
            selecao_player1 = True
            pygame.time.delay(1000)

        if Selecao_cor > 2:
            Selecao_cor = 0

        elif Selecao_cor < 0:
            Selecao_cor = 2

        for event in pygame.event.get():  # |
            if event.type == QUIT:  # |Detecta o clique para sair do pgm
                start = True  # |
                selecao_player1 = True
                selecao_player2 = True
                fim = True
                programa = True
                restart = True
            elif event.type == KEYDOWN:
                if event.key == K_s:
                    Selecao_cor = Selecao_cor + 1
                    pygame.display.update()
                    som_select()

                elif event.key == K_w:
                    Selecao_cor = Selecao_cor - 1
                    pygame.display.update()
                    som_select()

    ############################################################################################
    # Player2
    Selecao_cor = 0
    while not selecao_player2:
        tela.fill(CorSelect)  # Preenche o fundo de tela

        tela_selectX = 200
        tela_selectY = 150
        tela.blit(Comando2, (500, 100))
        tela.blit(player2_sel, (75, 20))
        tela.blit(sele_enter, ((Tela_X / 2) - 242, 500))
        tela.blit(Tank_Cor[0], (tela_selectX, tela_selectY))
        tela.blit(Tank_Cor[1], (tela_selectX, tela_selectY + 25 + 50))
        tela.blit(Tank_Cor[2], (tela_selectX, tela_selectY + 25 + 125))
        tela.blit(selecao_fig_Tri_1, (tela_select_triangulox, tela_select_trianguloy))

        if Selecao_cor == 0:
            tela_select_triangulox = tela_selectX - 35
            tela_select_trianguloy = tela_selectY + 15
            Tank_B = Tank_Vermelho

        elif Selecao_cor == 1:
            tela_select_triangulox = tela_selectX - 35
            tela_select_trianguloy = tela_selectY + 15 + 25 + 50
            Tank_B = Tank_Verde

        elif Selecao_cor == 2:
            tela_select_triangulox = tela_selectX - 35
            tela_select_trianguloy = tela_selectY + 15 + 25 + 125
            Tank_B = Tank_azul

        pygame.display.update()  # Atualiza tela - sem este update não haverá desenho
        Select_inicial_Tanque = 0
        Select_inicial_Tanque = pygame.key.get_pressed()

        if Selecao_cor > 2:
            Selecao_cor = 0

        elif Selecao_cor < 0:
            Selecao_cor = 2

        if Select_inicial_Tanque[K_RETURN]:
            tela.blit(selecao_fig_Tri_2, (tela_select_triangulox, tela_select_trianguloy))
            pygame.display.update()
            som_confirm()
            selecao_player2 = True
            pygame.time.delay(1000)

        for event in pygame.event.get():  # |
            if event.type == QUIT:  # |Detecta o clique para sair do pgm
                start = True  # |
                selecao_player1 = True
                selecao_player2 = True
                fim = True
                programa = True
                restart = True

            elif event.type == KEYDOWN:
                if event.key == K_k:
                    Selecao_cor = Selecao_cor + 1
                    pygame.display.update()
                    som_select()

                elif event.key == K_i:
                    Selecao_cor = Selecao_cor - 1
                    pygame.display.update()
                    som_select()

    ############################################################################################
    # Laço principal
    som_jogo()
    while not fim:  # Laço principal

        fundo_main()
        barraA(vaziaA)
        barraB(vaziaB)

        # Tiro Tank 1
        Tiro_Colisao1_A = pygame.Rect(X_Tiro1_A + ((Tamanho_Figura / 2) - 2), Y_Tiro1_A + ((Tamanho_Figura / 2) - 2), 5,
                                      5)
        pygame.draw.rect(tela, CorRetangulo, Tiro_Colisao1_A, 0)
        # Tiro Tank 2
        Tiro_Colisao2_B = pygame.Rect(X_Tiro2_B + ((Tamanho_Figura / 2) - 2), Y_Tiro2_B + ((Tamanho_Figura / 2) - 2), 5,
                                      5)
        pygame.draw.rect(tela, CorRetangulo, Tiro_Colisao2_B, 0)

        # Figura
        tela.blit(Tank_A[TankPos1_A], (X_tank1_A, Y_tank1_A))
        tela.blit(Tank_B[TankPos2_B], (X_tank2_B, Y_tank2_B))


        pygame.display.update()  # Atualiza tela - sem este update não haverá desenho

        # ---------------------------------------

        if Tempo_logo <= 100:
            Logo = Logo1
            Tempo_logo = Tempo_logo + 1
        elif Tempo_logo >= 100 and Tempo_logo <= 200:
            Logo = Logo2
            Tempo_logo = Tempo_logo + 1
        else:
            Tempo_logo = 0

        # Movimentos

        # Tank 1 A

        if Tempo1_A == TankTemp:
            MovTank1_A = pygame.key.get_pressed()

            if MovTank1_A[K_d] and MovTank1_A[K_w] == 1:  # Movimentos Posição 2
                X_tank1_A = X_tank1_A + 1
                Y_tank1_A = Y_tank1_A - 1
                TankPos1_A = 2 - 1
            elif MovTank1_A[K_a] and MovTank1_A[K_w] == 1:  # Movimentos Posição 8
                X_tank1_A = X_tank1_A - 1
                Y_tank1_A = Y_tank1_A - 1
                TankPos1_A = 8 - 1
            elif MovTank1_A[K_d] and MovTank1_A[K_s] == 1:  # Movimentos Posição 4
                X_tank1_A = X_tank1_A + 1
                Y_tank1_A = Y_tank1_A + 1
                TankPos1_A = 4 - 1
            elif MovTank1_A[K_a] and MovTank1_A[K_s] == 1:  # Movimentos Posição 6
                X_tank1_A = X_tank1_A - 1
                Y_tank1_A = Y_tank1_A + 1
                TankPos1_A = 6 - 1
            elif MovTank1_A[K_d] == 1:  # Movimentos Posição 3
                X_tank1_A = X_tank1_A + 1
                TankPos1_A = 3 - 1
            elif MovTank1_A[K_a] == 1:  # Movimentos Posição 7
                X_tank1_A = X_tank1_A - 1
                TankPos1_A = 7 - 1
            elif MovTank1_A[K_w] == 1:  # Movimentos Posição 1
                Y_tank1_A = Y_tank1_A - 1
                TankPos1_A = 1 - 1
            elif MovTank1_A[K_s] == 1:  # Movimentos Posição 5
                Y_tank1_A = Y_tank1_A + 1
                TankPos1_A = 5 - 1
            Tempo1_A = 0

        Tempo1_A = Tempo1_A + 1

        # ---------------------------------------
        # Tank 2 B

        if Tempo2_B == TankTemp:
            MovTank2_B = pygame.key.get_pressed()

            if MovTank2_B[K_l] and MovTank2_B[K_i] == 1:  # Movimentos Posição 2
                X_tank2_B = X_tank2_B + 1
                Y_tank2_B = Y_tank2_B - 1
                TankPos2_B = 2 - 1
            elif MovTank2_B[K_j] and MovTank2_B[K_i] == 1:  # Movimentos Posição 8
                X_tank2_B = X_tank2_B - 1
                Y_tank2_B = Y_tank2_B - 1
                TankPos2_B = 8 - 1

            elif MovTank2_B[K_l] and MovTank2_B[K_k] == 1:  # Movimentos Posição 4
                X_tank2_B = X_tank2_B + 1
                Y_tank2_B = Y_tank2_B + 1
                TankPos2_B = 4 - 1
            elif MovTank2_B[K_j] and MovTank2_B[K_k] == 1:  # Movimentos Posição 6
                X_tank2_B = X_tank2_B - 1
                Y_tank2_B = Y_tank2_B + 1
                TankPos2_B = 6 - 1
            elif MovTank2_B[K_l] == 1:  # Movimentos Posição 3
                X_tank2_B = X_tank2_B + 1
                TankPos2_B = 3 - 1
            elif MovTank2_B[K_j] == 1:  # Movimentos Posição 7
                X_tank2_B = X_tank2_B - 1
                TankPos2_B = 7 - 1
            elif MovTank2_B[K_i] == 1:  # Movimentos Posição 1
                Y_tank2_B = Y_tank2_B - 1
                TankPos2_B = 1 - 1
            elif MovTank2_B[K_k] == 1:  # Movimentos Posição 5
                Y_tank2_B = Y_tank2_B + 1
                TankPos2_B = 5 - 1
            Tempo2_B = 0

        Tempo2_B = Tempo2_B + 1

        # ------------------------------------------------------
        # Limites Posição Tanques
        if X_tank1_A <= 0:
            X_tank1_A = 0
        elif X_tank1_A >= (Tela_X - Tamanho_Figura):
            X_tank1_A = Tela_X - Tamanho_Figura
        if Y_tank1_A <= 100:
            Y_tank1_A = 100
        elif Y_tank1_A >= (Tela_Y - Tamanho_Figura):
            Y_tank1_A = Tela_Y - Tamanho_Figura

        # Limites Posição Tanques
        if X_tank2_B <= 0:
            X_tank2_B = 0
        elif X_tank2_B >= (Tela_X - Tamanho_Figura):
            X_tank2_B = Tela_X - Tamanho_Figura
        if Y_tank2_B <= 100:
            Y_tank2_B = 100
        elif Y_tank2_B >= (Tela_Y - Tamanho_Figura):
            Y_tank2_B = Tela_Y - Tamanho_Figura

        # ------------------------------------------------------

        Tiro1_A = pygame.key.get_pressed()

        if (Tiro1_A[K_r] == 1 and X_Tiro1_A >= -14 and Y_Tiro1_A >= 86 and X_Tiro1_A <= Tela_X and Y_Tiro1_A <= Tela_Y) or (
                Set_X_Tiro1_A == 1 and X_Tiro1_A >= -14 and Y_Tiro1_A >= 86 and X_Tiro1_A <= Tela_X and Y_Tiro1_A <= Tela_Y):

            if Tiro1_A[K_r] == 1 and Set_X_Tiro1_A == 0:
                som_tiro()

            if TankTiro1_A == 0:
                Y_Tiro1_A = Y_Tiro1_A - 1

            elif TankTiro1_A == 1:
                X_Tiro1_A = X_Tiro1_A + 1
                Y_Tiro1_A = Y_Tiro1_A - 1

            elif TankTiro1_A == 2:
                X_Tiro1_A = X_Tiro1_A + 1

            elif TankTiro1_A == 3:
                X_Tiro1_A = X_Tiro1_A + 1
                Y_Tiro1_A = Y_Tiro1_A + 1

            elif TankTiro1_A == 4:
                Y_Tiro1_A = Y_Tiro1_A + 1

            elif TankTiro1_A == 5:
                X_Tiro1_A = X_Tiro1_A - 1
                Y_Tiro1_A = Y_Tiro1_A + 1

            elif TankTiro1_A == 6:
                X_Tiro1_A = X_Tiro1_A - 1

            elif TankTiro1_A == 7:
                X_Tiro1_A = X_Tiro1_A - 1
                Y_Tiro1_A = Y_Tiro1_A - 1

            Set_X_Tiro1_A = 1

        else:
            TankTiro1_A = TankPos1_A
            X_Tiro1_A = X_tank1_A
            Y_Tiro1_A = Y_tank1_A
            Set_X_Tiro1_A = 0

        # ------------------------------------------------------------------------

        Tiro2_B = pygame.key.get_pressed()
        if (Tiro2_B[K_p] == 1 and X_Tiro2_B >= -14 and Y_Tiro2_B >= 86 and X_Tiro2_B <= Tela_X and Y_Tiro2_B <= Tela_Y) or (
                Set_X_Tiro2_B == 1 and X_Tiro2_B >= -14 and Y_Tiro2_B >= 86 and X_Tiro2_B <= Tela_X and Y_Tiro2_B <= Tela_Y):

            if Tiro2_B[K_p] == 1 and Set_X_Tiro2_B == 0:
                som_tiro()

            if TankTiro2_B == 0:
                Y_Tiro2_B = Y_Tiro2_B - 1

            elif TankTiro2_B == 1:
                X_Tiro2_B = X_Tiro2_B + 1
                Y_Tiro2_B = Y_Tiro2_B - 1

            elif TankTiro2_B == 2:
                X_Tiro2_B = X_Tiro2_B + 1

            elif TankTiro2_B == 3:
                X_Tiro2_B = X_Tiro2_B + 1
                Y_Tiro2_B = Y_Tiro2_B + 1

            elif TankTiro2_B == 4:
                Y_Tiro2_B = Y_Tiro2_B + 1

            elif TankTiro2_B == 5:
                X_Tiro2_B = X_Tiro2_B - 1
                Y_Tiro2_B = Y_Tiro2_B + 1

            elif TankTiro2_B == 6:
                X_Tiro2_B = X_Tiro2_B - 1

            elif TankTiro2_B == 7:
                X_Tiro2_B = X_Tiro2_B - 1
                Y_Tiro2_B = Y_Tiro2_B - 1

            Set_X_Tiro2_B = 1

        else:
            TankTiro2_B = TankPos2_B
            X_Tiro2_B = X_tank2_B
            Y_Tiro2_B = Y_tank2_B
            Set_X_Tiro2_B = 0
        # ------------------------------------------------------------------------

        Colisao1_A_para_B = ((X_Tiro1_A - X_tank2_B) ** 2 + (Y_Tiro1_A - Y_tank2_B) ** 2) ** 0.5
        Tank_Prox = ((X_tank1_A - X_tank2_B) ** 2 + (Y_tank1_A - Y_tank2_B) ** 2) ** 0.5
        if Tank_Prox > Tamanho_Figura / 2:
            if Colisao1_A_para_B <= Tamanho_Figura / 2:
                Placar_A_Soma = Placar_A_Soma + 1
                X_Tiro1_A = X_tank1_A
                vaziaB = vaziaB + 1
                Y_Tiro1_A = Y_tank1_A
                Set_X_Tiro1_A = 0
                colisao()

        Colisao2_B_para_A = ((X_Tiro2_B - X_tank1_A) ** 2 + (Y_Tiro2_B - Y_tank1_A) ** 2) ** 0.5
        if Tank_Prox > Tamanho_Figura / 2:
            if Colisao2_B_para_A <= Tamanho_Figura / 2:
                Placar_B_Soma = Placar_B_Soma + 1
                vaziaA = vaziaA + 1
                X_Tiro2_B = X_tank2_B
                Y_Tiro2_B = Y_tank2_B
                Set_X_Tiro2_B = 0
                colisao()

        # ------------------------------------------------------

        if Placar_A_Soma >= 5:
            fim = True
            fundo_main()
            barraA(vaziaA)
            tela.blit(Barra_vazia, (Tela_X - 134, 60))
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.mixer.music.stop()

        if Placar_B_Soma >= 5:
            fim = True
            fundo_main()
            barraB(vaziaB)
            tela.blit(Barra_vazia, (20, 60))
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.mixer.music.stop()

        for event in pygame.event.get():  # |
            if event.type == QUIT:  # |Detecta o clique para sair do pgm
                start = True  # |
                selecao_player1 = True
                selecao_player2 = True
                fim = True
                programa = True
                restart = True
                pygame.mixer.music.stop()

    # ------------------------------------------------------------------

    # Restart comando para reiniciar
    # Prototipo

    while not restart:

        if Placar_A_Soma == 5:
            Player = 0
        elif Placar_B_Soma == 5:
            Player = 1

        tela.fill(CorSelect)  # Preenche o fundo de tela
        tela.blit(Restart_Menu[Player], ((Tela_X / 2) - 121.5, (40)))
        tela.blit(Restart_Menu[2], ((Tela_X / 2) - 208, 250))
        Restart = pygame.key.get_pressed()
        if Restart[K_RETURN]:
            som_confirm()
            fim = False
            selecao_player1 = False
            selecao_player2 = False
            restart = False
            programa = False
            restart = True
            Placar_A_Soma = 0
            Placar_B_Soma = 0

            # Tiro Tanque
            X_Tiro1_A = 50
            Y_Tiro1_A = 150
            Set_X_Tiro1_A = 0
            TankTiro1_A = 0
            Tiro1_A = []
            # ---------------------------------------

            # Tiro Tanque 2 B
            X_Tiro2_B = 850
            Y_Tiro2_B = 400
            Set_X_Tiro2_B = 0
            TankTiro2_B = 0
            Tiro2_B = []

            # ---------------------------------------
            # Tanques

            TankPos1_A = 2

            # Tanque 1 A
            X_tank1_A = X_Tiro1_A
            Y_tank1_A = Y_Tiro1_A

            # Tanque 2 B

            X_tank2_B = 800
            Y_tank2_B = 500

            TankPos2_B = 6
            Player = 0
            Selecao_cor = 0
            vaziaA=0
            vaziaB=0
            pygame.time.delay(1000)

        if Restart[K_ESCAPE]:
            restart = True
            fim = True
            programa = True

        pygame.display.update()  # Atualiza tela - sem este update não haverá desenho

        for event in pygame.event.get():  # |
            if event.type == QUIT:  # |Detecta o clique para sair do pgm
                start = True  # |
                selecao_player1 = True
                selecao_player2 = True
                fim = True
                programa = True
                restart = True

pygame.mixer.music.stop()

pygame.display.quit()  # Após o término do laço finaliza a tela de modo gráfico

print("\n\nFim do programa")
