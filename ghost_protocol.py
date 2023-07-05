import RPi.GPIO as GPIO
import time
import random
import pygame
class GhostProtocol():
    def __init__(self):
        self.gpb = 31
        self.reset = 29
        self.yb1 = 37
        self.rb2 = 35
        self.yb3 = 33
        self.bzz = 13
        self.pir = 11
        self.egb = 23
        self.ghp_loop = False
        self.bind_loop = True
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.gpb, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.egb, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.yb1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.rb2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.yb3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.bzz, GPIO.OUT)
        GPIO.setup(self.pir, GPIO.IN)
        self.audio_mixer("start-beep.mp3", "play")
        print("Welcome")
        while pygame.mixer.music.get_busy():
                    continue
        
        
    def audio_mixer(self, track, function):
        pygame.mixer.init()
        pygame.mixer.music.load(track)
        if function == "play":
            pygame.mixer.music.play()
        elif function == "pause":
            pygame.mixer.music.pause()
        elif function == "unpause":
            pygame.mixer.music.unpause()
        elif function == "stop":
            pygame.mixer.music.stop()
    def ghost_shufler(self):
        gst = ["gs1.mp3", "gs2.mp3", "gs3.mp3"]
        gs = random.choice(gst)
        self.audio_mixer(gs, "play")
        while pygame.mixer.music.get_busy():
            stop_ghp = GPIO.input(self.gpb)
            if stop_ghp == GPIO.LOW:
                self.audio_mixer(gs, "stop")
                break
            else:
                continue
    def ghp(self):
            while True:
                pir_alert = GPIO.input(self.pir)
                gpb_check = GPIO.input(self.gpb)
                if gpb_check == GPIO.LOW:
                    self.audio_mixer("deact.mp3", "play")
                    print("Deactivating Ghost Protocol")
                    while pygame.mixer.music.get_busy():
                        continue
                    pir_alert = 0
                    yb1_alert = 0
                    break
                if pir_alert == 0:                 
                    print("No intruders", pir_alert)  
                    time.sleep(0.1)
                elif pir_alert == 1:               
                    print("Intruder detected", pir_alert)
                    self.ghost_shufler() 
                    time.sleep(0.1)
            
    def binder(self):
        while self.bind_loop:
            act_ghp = GPIO.input(self.gpb)
            bind_kill = GPIO.input(self.reset)
            yb1_alert = GPIO.input(self.yb1)
            rb2_alert = GPIO.input(self.rb2)
            yb3_alert = GPIO.input(self.yb3)
            if bind_kill == GPIO.HIGH:
                print("A project designed and developed by Habril Inc")
                print("Harish :)")
                self.audio_mixer("end.mp3", "play")
                while pygame.mixer.music.get_busy():
                    continue
                break
            elif act_ghp == GPIO.HIGH:
                print("Activating Ghost Protocol")
                self.audio_mixer("act.mp3", "play")
                while pygame.mixer.music.get_busy():
                    continue
                self.ghp()
            elif yb1_alert == GPIO.HIGH:
                self.audio_mixer("roll.mp3", "play")
                print("Roll")
                while True:
                    yb1_kill = GPIO.input(self.egb)
                    if yb1_kill == GPIO.HIGH:
                        self.audio_mixer("roll.mp3", "stop")
                        yb1_alert = GPIO.LOW
                        yb1_kill = GPIO.LOW
                        break
                    elif pygame.mixer.music.get_busy():
                        pass
                    else:
                        break
            elif yb3_alert == GPIO.HIGH:
                self.audio_mixer("teq.mp3", "play")
                print("Teq")
                while True:
                    yb3_kill = GPIO.input(self.egb)
                    if yb3_kill == GPIO.HIGH:
                        self.audio_mixer("teq.mp3", "stop")
                        yb3_alert = GPIO.LOW
                        yb3_kill = GPIO.LOW
                        break
                    elif pygame.mixer.music.get_busy():
                        pass
                    else:
                        break
            elif rb2_alert == GPIO.HIGH:
                rbgst = ["gs1.mp3", "gs2.mp3", "gs3.mp3"]
                rbgs = random.choice(rbgst)
                self.audio_mixer(rbgs, "play")
                print("Ghost Shuffle")
                while True:
                    rb2_kill = GPIO.input(self.egb)
                    if rb2_kill == GPIO.HIGH:
                        self.audio_mixer(rbgs, "stop")
                        rb2_alert = GPIO.LOW
                        rb2kill = GPIO.LOW
                        break
                    elif pygame.mixer.music.get_busy():
                        pass
                    else:
                        break
            
gh = GhostProtocol()
gh.binder()