#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy
from math import pi, cos, sin


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def render(time, tabl):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180/3.1415)

    axes()

    analize(tabl)

    glFlush()


def spin(angle):
    glRotate(angle,1.0,0.0,0.0)
    glRotate(angle,0.0,1.0,0.0)
    glRotate(angle,0.0,0.0,1.0)

def initializeTab(size: int):
    tablica=numpy.zeros((size,size,3))

    for i in range(size):
        for j in range(size):
            #generowanie wartości od 0 do 1.0
            u=i/size
            v=j/size
            #żeby nie liczyć potęg bezsensownie
            u2=u*u
            u3=u2*u
            u4=u3*u
            u5=u4*u

            tablica[i][j][0]=(-90 * u5 + 225 * u4 - 270 * u3 + 180 * u2 - 45 * u) * cos(pi * v)
            tablica[i][j][1]=160 * u4 - 320 * u3 + 160 * u2 - 5
            tablica[i][j][2]=(-90 * u5 + 225 * u4 - 270 * u3 + 180 * u2 - 45 * u) * sin(pi * v)


    return tablica

def analize(tablica):
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POINTS)

    for i in range(len(tablica)):
        for j in range(len(tablica)):
            glVertex3f(tablica[i][j][0], tablica[i][j][1], tablica[i][j][2])
    glEnd()



def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main(rozmiar):
    #inicjowanie tablicy
    tab=initializeTab(rozmiar)





    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), tab)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    rozmiar:int = 50
    main(rozmiar)
