import time
from _thread import start_new_thread
# import gpiozero


def pour_drink(ingredients):
    for ingredient in ingredients:
        start_new_thread(pour_ingredient, (ingredient,))


def pour_ingredient(ingredient):
    name = ingredient["name"]
    wait_pour = ingredient["wait_before_pour"]
    print("{}: wait for pour".format(wait_pour))
    time.sleep(wait_pour)
    # relay = gpiozero.OutputDevice(ingredient["name"], active_high=True, initial_value=False)  # noqa: E501
    # relay.on()
    print("{}: on for {}".format(int(name), ingredient["pour_time"]))
    time.sleep(ingredient["pour_time"])
    print("{}: off".format(int(name)))
    # relay.off()
