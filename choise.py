#!/usr/bin/env python3
#juego echo para matar el aburrimiento
from time import sleep 
from random import choice as ch

player_name = input("ingresa tu nombre $")

Options_cpu = ['piedra', 'papel', 'tijera']

cpu = ch(Options_cpu)

Options_player = input("Elige piedra, papel o tijera $")

print("la cpu esta eligiendo...")
sleep(2)

if Options_player == "piedra" and cpu == "papel":
    print("el jugador eligio PIEDRA")
    print("gana la cpu usando", cpu)

elif Options_player == "piedra" and cpu == "tijera":
    print("gana el jugador usando piedra")
    print("la cpu eligio tijera")

elif Options_player == "piedra" and cpu == "piedra":
    print("empate ambos eligieron piedra")

elif Options_player == "papel" and cpu == "piedra":
    print("tu ganas")
    print ("tu elegiste", Options_player)
    print("la cpu eligio", cpu)
    
elif Options_player == "papel" and cpu == "tijera":
    print("gana la cpu")
    
elif Options_player == "papel" and cpu == "papel":
    print("empate")
    
elif Options_player == "tijera" and cpu == "papel":
    print("tu ganas")
    
elif Options_player == "tijera" and cpu == "piedra":
    print("tu pierdes")
    
elif Options_player == "tijera" and cpu == "tijera":
    print("empate")