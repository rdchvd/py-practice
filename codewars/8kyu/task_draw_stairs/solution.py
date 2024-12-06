def draw_stairs_recursive(n, drawing=""):
    """
    Create a drawing of stairs with n steps using recursion.
    :param n: number of steps and width of the stairs
    :param drawing: the drawing of the stairs being created
    :return: the drawing of the stairs with new step
    """
    drawing = " " * (n - 1) + "I" + drawing
    if n == 1:
        return drawing
    return draw_stairs_recursive(n - 1, "\n" + drawing)


def draw_stairs(n):
    """
    Create a drawing of stairs with n steps.
    :param n: number of steps and width of the stairs
    :return: the drawing of the stairs
    """
    return "\n".join(" " * i + "I" for i in range(n))
