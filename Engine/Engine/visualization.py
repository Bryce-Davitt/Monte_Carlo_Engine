import matplotlib.pyplot as plt
import numpy as np

def plot_price_paths(paths, n_paths_to_plot=20):
    plt.figure(figsize=(10, 6))
    for i in range(min(n_paths_to_plot, paths.shape[0])):
        plt.plot(paths[i], lw=0.7)
    plt.title('Simulated Asset Price Paths')
    plt.xlabel('Time Step')
    plt.ylabel('Asset Price')
    plt.grid(True)
    plt.show()

def plot_payoff_distribution(payoffs):
    plt.figure(figsize=(8, 5))
    plt.hist(payoffs, bins=50, alpha=0.7)
    plt.title('Payoff Distribution at Maturity')
    plt.xlabel('Payoff')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_greeks(strikes, values, greek_name='Delta'):
    plt.figure(figsize=(8, 5))
    plt.plot(strikes, values, marker='o')
    plt.title(f'{greek_name} vs. Strike Price')
    plt.xlabel('Strike Price')
    plt.ylabel(greek_name)
    plt.grid(True)
    plt.show() 