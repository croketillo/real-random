from real_random import (
    real_random,
    real_random_int,
    real_random_float,
    real_random_choice,
    real_random_string,
)

print(real_random())                          # → 0.72623...
print(real_random_int(1, 10))                 # → 7
print(real_random_float(0.5, 2.5))            # → 1.934...
print(real_random_choice(["red", "blue"]))    # → "blue"
print(real_random_string(8))                  # → "aG9xB2dZ"
