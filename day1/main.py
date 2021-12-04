
depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def changed_depth(depths):
    changes = len(depths)
    for i in range(0, changes):
        current_value = depths[i]
        if i == 0:
            print(str(current_value) + " (N/A - no previous measurement)")
            continue
        previous_value = depths[i - 1]
        if current_value > previous_value:
            print(str(current_value) + " (Increased)")
            continue
        else:
            print(str(current_value) + " (decreased)")
            continue


changed_depth(depths)