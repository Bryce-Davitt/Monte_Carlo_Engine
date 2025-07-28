from monte_carlo_engine import MonteCarloEngine

# Parameters
S0 = 100      # Initial asset price
r = 0.05      # Risk-free rate
sigma = 0.2   # Volatility
T = 1.0       # Time to maturity (1 year)
n_steps = 252 # Daily steps
n_paths = 10000 # Number of Monte Carlo paths
K = 100       # Strike price

# Initialize engine
engine = MonteCarloEngine(S0, r, sigma, T, n_steps, n_paths)

# Price European call and put options
call_price = engine.price_european_option(K, option_type='call')
put_price = engine.price_european_option(K, option_type='put')

# Compute Greeks
call_delta = engine.compute_delta(K, option_type='call')
call_gamma = engine.compute_gamma(K, option_type='call')
put_delta = engine.compute_delta(K, option_type='put')
put_gamma = engine.compute_gamma(K, option_type='put')

# Print results
print(f"European Call Option Price: {call_price:.4f}")
print(f"European Put Option Price: {put_price:.4f}")
print(f"Call Delta: {call_delta:.4f}")
print(f"Call Gamma: {call_gamma:.4f}")
print(f"Put Delta: {put_delta:.4f}")
print(f"Put Gamma: {put_gamma:.4f}") 