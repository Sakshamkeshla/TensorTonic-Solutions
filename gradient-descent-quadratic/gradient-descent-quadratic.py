import numpy
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    fx = numpy.poly1d([a,b,c])
    dfx = fx.deriv()
    for i in range(steps):
        gradient = dfx(x0)
        x0 = x0 - (lr * gradient)
    return x0
    pass