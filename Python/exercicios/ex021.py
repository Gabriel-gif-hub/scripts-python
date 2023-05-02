print('======Desafio 021======')
'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
'''
# import playsound
# tocar = playsound.playsound('ex021.mp3')
# print('Playing sound with playsound ')

# import pygame
# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load('ex021.mp3')
# pygame.mixer_music.play()
# pygame.event.wait()
# print()

# import soundfile as sf

# audio = sf.read('ex021.wav')
# print(audio)
# print('----------')
# print('Sample rate ir', audio)
# print('----------')
# print('Done')

# import soundfile as sf 
# data, samplerate = sf.read('ex021.wav') 
# print(data) 
# print("---------------------") 
# print("Sample Rate is ", samplerate) 
# print("---------------------") 
# print("Done")

# from playsound import playsound

# playsound("ex021_audio.mp3")

import winsound 
winsound.PlaySound('rapteste.wav', winsound.SND_FILENAME)
