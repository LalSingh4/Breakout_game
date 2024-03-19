def create_ball(width, height, radius):
    ball_pos = [width // 2, height // 2]
    ball_x_change = 2
    ball_y_change = -2  # Negative for downward movement
    return {
        "pos": ball_pos,
        "x_change": ball_x_change,
        "y_change": ball_y_change,
        "radius": radius
    }


def update_ball(ball, width, height):
    ball["pos"][0] += ball["x_change"]
    ball["pos"][1] += ball["y_change"]

    # Check for wall collisions
    if ball["pos"][0] <= 0 or ball["pos"][0] >= width:
        ball["x_change"] *= -1

    if ball["pos"][1] <= 0:
        ball["y_change"] *= -1

    return ball
