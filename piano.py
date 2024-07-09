import pygame

from typing import Final

class Note:
    def __init__(self, note: str, octave: int, audio_src: str) -> None:
        self.audio = pygame.mixer.Sound(audio_src)
        self.note = note
        self.octave = octave



class PianoKey(pygame.Surface):

    def __init__(self, note: Note, texture_data: tuple[pygame.Surface, pygame.Surface], size: tuple[int, int]) -> None:
        super().__init__(size)

        self.note = note
        self.size = size
        self.rect = self.get_rect()
        self.rect.topleft = (0, 0)

        self.textures = texture_data

        self.fill(self.textures[0], (0, 0))

        self.__pressed = False

    def clicked(self) -> bool:
        player_mouse = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(player_mouse) and not self.__pressed:
                self.__pressed = True

                return True
        
        if not pygame.mouse.get_pressed()[0]:
            self.__pressed = False

            return False



class PianoKeyGroup(pygame.Surface):

    def __init__(self, keys: list[PianoKey]) -> None:
        super().__init__((keys[0].get_width() * 7, keys[0].get_height()))
        self.fill((0, 0, 0))

        self.piano_keys = keys

    def update(self) -> None:
        self.fill((0, 0, 0))
        
        for index, key in enumerate(self.piano_keys, 0):
            if index not in [2, 4, 7, 9, 11]:
                self.blit(key, (index * key.get_width(), 0))
                continue

            self.blit(key.textures[0], ((index - 1) * self.piano_keys[index - 1].get_width() - (key.get_width() // 2), 0))

            if key.clicked():
                key.blit(key.textures[1], (0, 0))
            


class Piano:

    def __init__(self, whitekey_data: tuple[pygame.Surface, pygame.Surface], blackkey_data: tuple[pygame.Surface, pygame.Surface]) -> None:
        self.notes: Final[list[str]] = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
        self.keys_count: Final[int] = 12
        self.keys_group: list[PianoKeyGroup] = []

        self.black_keys = blackkey_data
        self.white_keys = whitekey_data

    
    def generate_keys(self) -> None:
        for octave in range(0, self.keys_count % 12, 1):
            keys: list[PianoKey] = []

            for i in range(0, 12, 1):
                current_note = Note(self.notes[i], octave, 'sounds\\%i%s.mp3' % (octave, self.notes[i].lower()))

                if i in [2, 4, 7, 9, 11]:
                    piano_key = PianoKey(self.notes[i], self.black_keys, self.black_keys[0].get_size())
                else:
                    piano_key = PianoKey(self.notes[i], self.white_keys, self.white_keys[0].get_size())
            
                keys.append(piano_key)
            
            group = PianoKeyGroup(keys)
            self.keys_group.append(group)

    def update(self) -> None:
        for group in self.keys_group:
            group.update()