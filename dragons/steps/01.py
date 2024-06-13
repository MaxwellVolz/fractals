# 1st iteration: R
# 2nd iteration: R R L
# 3rd iteration: R R L R R L L
# 4th iteration: R R L R R L L R R R L L R L L.

# Each iteration can be found by
# 1. copying the previous iteration
# 2. an R
# 3. a second copy of the previous iteration in reverse order with the
#   L and R letters swapped.


s = "R"

translation_table = str.maketrans("RL", "LR")

print(
    f"""

Testing string translations:

'RL'       ->      {"RL".translate(translation_table)}
'LR'       ->      {"LR".translate(translation_table)}
'RRRR'     ->      {"RRRR".translate(translation_table)}
'RRL'      ->      {"RRL".translate(translation_table)}
"""
)


def dragon_tailwhip(dragon):
    # print(dragon)

    antidragon = dragon[::-1].translate(translation_table)

    return dragon + "R" + antidragon


print(
    f"""
Dragon training:

'R'        ->      {dragon_tailwhip('R')}
'RRL'      ->      {dragon_tailwhip('RRL')}
'RRLRRLL'  ->      {dragon_tailwhip('RRLRRLL')}

"""
)
