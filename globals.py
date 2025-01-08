import pygame as pg

pg.init()

SCREEN_INFO = pg.display.Info()
SCREEN_WIDTH = SCREEN_INFO.current_w
SCREEN_HEIGHT = SCREEN_INFO.current_h - 96

CONTROL_PANEL_WIDTH = 0.25 * SCREEN_WIDTH
CONTROL_PANEL_HEIGHT = SCREEN_HEIGHT

FONT = pg.font.SysFont(None, 24)
