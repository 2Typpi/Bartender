import time
from _thread import start_new_thread
import RPi.GPIO as GPIO


def pour_drink(ingredients):
    for ingredient in ingredients:
        start_new_thread(pour_ingredient, (ingredient,))


def pour_ingredient(ingredient):
    RELAIS_1_GPIO = ingredient["name"]
    wait_pour = ingredient["wait_before_pour"]

    # Wait for other ingredients
    print("{}: wait for pour".format(wait_pour))
    time.sleep(wait_pour)

    GPIO.setmode(GPIO.BCM)  # GPIO Nummern statt Board Nummern
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)  # GPIO Modus zuweisen
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)  # an
    print("{}: on for {}".format(RELAIS_1_GPIO, ingredient["pour_time"]))

    time.sleep(ingredient["pour_time"])

    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)  # aus
    print("{}: off".format(RELAIS_1_GPIO))
