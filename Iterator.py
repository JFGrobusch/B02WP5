### Iteration magic###
## Evolving a fuel tank##

MS = [5,2,4]

def natural_selection(tank,MS):
    # check if any margin is not satisfied to fix this first
    safe = True
    for margin in MS:
        if margin < 0:
            safe = False
    # Set positve or negative
    if safe:
        finder = 1
    else:
        finder = -1
    # Find what to change
    old_margin = finder * 10000
    index = 0
    for margin in MS:
        new_margin = margin
        if new_margin < old_margin:
            old_margin = new_margin
            best = index
        index += 1