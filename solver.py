# shooter and target come with Position objects
def calculate_linear_slope(shooter, target):
    # get the shooter coordinates
    shooter_x = shooter.x
    shooter_y = shooter.y

    # get the target coordinates
    target_x = target.x
    target_y = target.y

    if shooter_x == target_x:
        return None  # vertical line, slope is undefined

    # calculate the slope
    # formula: slope = y1 - y2 / x1 - x2
    slope = (target_y - shooter_y) / (target_x - shooter_x)
    return slope