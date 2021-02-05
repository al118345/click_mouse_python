# -*- coding: utf-8 -*-
from pynput.mouse import Button, Controller

import time
mouse = Controller()
#EL OTRO ES SUBPALS
# Obtiene la posición actual
print('The current pointer position is {0}'.format(
    mouse.position))
cont=0
while True:
    time.sleep(5)

    #mouse.position = ( 86, 45)
    #mouse.press(Button.left)
    #mouse.release(Button.left)
    cont = -1
    time.sleep(10)
    cont = cont + 1


    #presiona el boton de mostrar video Now we have moved it to (502.79296875, 734.0625)

    #mouse.position = (795, 755)
    mouse.position = (754, 670)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(9)


    #da a me gusta
    mouse.position = (139, 491)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

    # presiona el botón de subscribirse
    mouse.position = (397, 538)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)


    # cambio de pestaña
    mouse.position = (1353, 669)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(13)


    # confirmo la subcripción
    #mouse.position = (752, 826)
    mouse.position = (764, 725)


    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(30)


