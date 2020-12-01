### Iteration magic###
## Evolving a fuel tank##

MS = [5,2,4]

def natural_selection(tank,MS):
    # check if any margin is not satisfied to fix this first
    safe = True
    for margin in MS:
        if margin < 0:
            safe = False
    # Set positve or negative and find what to change.
    if safe:
        adjuster = 1
        margin is max(MS)
        index_margin = MS.index(max(MS))
    else:
        adjuster = -1
        margin is min(MS)
        index_margin = MS.index(min(MS))
    # Get variables

    # Change the variable(s)

def evolver(tanks):
    # Find best for species
    # Apply normal change
    # copy once
    # multiply and mutate
    # return back to start