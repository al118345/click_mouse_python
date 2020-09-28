from pynput.mouse import Button, Controller
import time
mouse = Controller()
#EL OTRO ES SUBPALS
# Obtiene la posición actual
print('The current pointer position is {0}'.format(
    mouse.position))

while True:
    time.sleep(5)

    #presiona el boton de mostrar video
    mouse.position = ( 532.49609375, 688.70703125)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(9)


    #da a me gusta
    mouse.position = (651.2890625, 773.90234375)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

    # presiona el botón de subscribirse
    mouse.position = (918.9453125, 830.796875)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)


    # cambio de pestaña
    mouse.position = (70.65625, 21.19140625)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(13)


    # confirmo la subcripción
    mouse.position = (492.33984375, 750.921875)
    print('Now we have moved it to {0}'.format(
        mouse.position))
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(30)


