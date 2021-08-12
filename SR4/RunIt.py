#Universidad del Valle de Guatemala
#Graficas por Computadora
#Laboratorio SR4
#Diego Crespo 19541
from Engine import Renderer, V3, _color

from obj import Texture

import random

width = 960
height = 540

rend = Renderer(width, height)

modelTexture = Texture("model_normal.bmp")


rend.glLoadModel("model.obj", modelTexture, V3(width/2, height/2, 0), V3(200,200,200))


rend.glFinish("salida.bmp")


