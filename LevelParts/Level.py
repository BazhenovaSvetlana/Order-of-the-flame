from Draws.LevelDraws import *
from LevelParts.City.City import *
from LevelParts.Map import *
import pygame


class Level:
    # TODO Создать класс уровня который будет мониторить ситуацию происходящюю во время игры, инициализируетс я в
    #  главном меню
    """

    Class of game level
    :field map: Map
    :field first_city: City of first player
    :field second_city: Сity of second player

    """

    def __init__(self, map_file):
        """

        Initialise of level
        :param map_file: File with information about map

        """
        self.map = Map(map_file, LevelXSize / 2 - MapXSize / 2, LevelYSize / 2 - MapYSize / 2, MapXSize, MapYSize)
        self.first_city = City(("order", "left"), LevelXSize / 2 - MapXSize / 2 - CityXSize,
                                    LevelYSize / 2 - CityYSize / 2)
        self.second_city = City(("union", "right"), LevelXSize / 2 + MapXSize / 2, LevelYSize / 2 - CityYSize / 2)

    def update(self, screen):
        """

        Update level
        :param screen:
        :return:
        """
        level_draw(self, screen)
        map_draw(self.map, screen)
        self.first_city.update(screen, self)
        self.second_city.update(screen, self)

    def game_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.first_city.add_unit(SwordsmanType)
            elif event.key == pygame.K_RIGHT:
                self.second_city.add_unit(SwordsmanType)


if __name__ == "__main__":
    print("This module is not for direct call!")
