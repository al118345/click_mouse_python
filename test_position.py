from pynput.mouse import Button, Controller
import time
mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

while True:
    mouse = Controller()

    print('Now we have moved it to {0}'.format(
        mouse.position))
    time.sleep(3)



