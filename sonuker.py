# -*- coding: utf-8 -*-

from pynput.mouse import Button, Controller
import time
mouse = Controller()
#EL OTRO ES SUBPALS
# Obtiene la posición actual
print('The current pointer position is {0}'.format(
    mouse.position))

while True:
    time.sleep(5)
    # mouse.position = ( 86, 45)
    # mouse.press(Button.left)
    # mouse.release(Button.left)
    # time.sleep(7)

    # presiona el boton de mostrar video Now we have moved it to (502.79296875, 734.0625)

    #mouse.position = (760, 697)
    mouse.position = ( 783, 676)

    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(9)

    # da a me gusta
    mouse.position = (135, 445)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

    # presiona el botón de subscribirse
    mouse.position = (426, 518)
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
    mouse.position = (784, 738)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(30)
