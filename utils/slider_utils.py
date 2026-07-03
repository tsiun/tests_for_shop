from random import randint


def get_random_slider_value(min_val: float, max_val: float, step: float) -> float:
    total_steps = round((max_val - min_val) / step)
    n_steps = randint(1, total_steps - 1)
    value_of_slider = round(min_val + n_steps * step, 10)

    return value_of_slider
