import numpy as np
import matplotlib.pyplot as plt

def alcubierre_metric(x, y, z, t, v=1.0, R=1.0, sigma=1.0):
    """
    Simplified Alcubierre warp drive metric function.
    x, y, z: spatial coordinates
    t: time coordinate
    v: warp bubble velocity (fraction of speed of light)
    R: radius of the warp bubble
    sigma: thickness of the warp bubble wall
    Returns the warp factor at the given coordinates.
    """
    r = np.sqrt((x - v*t)**2 + y**2 + z**2)
    warp_factor = 1 - np.exp(-(r - R)**2 / (2 * sigma**2))
    return warp_factor

def simulate_warp_bubble_motion():
    """
    Simulate the warp bubble motion over time and plot the warp factor along x-axis.
    """
    t_values = np.linspace(0, 10, 100)
    x_values = np.linspace(-5, 15, 200)
    y = 0
    z = 0

    plt.figure(figsize=(10, 6))
    for t in t_values[::10]:
        warp_factors = [alcubierre_metric(x, y, z, t) for x in x_values]
        plt.plot(x_values, warp_factors, label=f't={t:.1f}')

    plt.title('Warp Drive Bubble Simulation (Alcubierre Metric)')
    plt.xlabel('x coordinate')
    plt.ylabel('Warp Factor')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_warp_bubble_motion()
