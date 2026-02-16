import os
import pygame

class SoundHandler:
    def __init__(self):
        pygame.mixer.init()

        self.sounds = {}
        self.musicVolume = 0.4
        self.sfxVolume = 0.1

    def loadFolder(self, rootFolder: str):
        """
        Loads all audio files inside folder and subfolders.
        Key = filename without extension
        """

        supported = (".wav", ".ogg", ".mp3")

        for folder, _, files in os.walk(rootFolder):
            for file in files:
                if file.lower().endswith(supported):
                    fullpath = os.path.join(folder, file)

                    # name = file without extension
                    relative = os.path.relpath(fullpath, rootFolder)
                    name = os.path.splitext(relative.replace("\\", "/"))[0]
                    #name = os.path.splitext(file)[0]

                    sound = pygame.mixer.Sound(fullpath)
                    sound.set_volume(self.sfxVolume)

                    self.sounds[name] = sound
                    #print("Loaded sound:", name)

    # ---------- PLAY SFX ----------
    def play(self, name: str):
        """Play a sound effect"""
        sound = self.sounds.get(name)
        if sound:
            sound.play()

    def stop(self, name: str):
        sound = self.sounds.get(name)
        if sound:
            sound.stop()

    # ---------- MUSIC ----------
    def playMusic(self, path: str, loop: bool = True):
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.musicVolume)
        pygame.mixer.music.play(-1 if loop else 0)

    def stopMusic(self):
        pygame.mixer.music.stop()

    # ---------- VOLUME ----------
    def setSFXVolume(self, volume: float):
        self.sfxVolume = max(0, min(1, volume))
        for s in self.sounds.values():
            s.set_volume(self.sfxVolume)

    def setMusicVolume(self, volume: float):
        self.musicVolume = max(0, min(1, volume))
        pygame.mixer.music.set_volume(self.musicVolume)
