from data_loader import get_underlying_price, get_option_expiries, get_option_chain
from models import GBMModel
from simulation_engine import SimulationEngine
from pricing import Pricing
from visualization import plot_price_paths, plot_payoff_distribution
import pandas as pd

# Prompt user for ticker
try:
    ticker = input("Enter ticker symbol (e.g., AAPL): ").strip().upper()
except Exception:
    ticker = 'AAPL'
    print('Defaulting to AAPL')

# Fetch underlying price
S0 = get_underlying_price(ticker)
print(f"Current price of {ticker}: {S0}")

# Fetch available expiries
expiries = get_option_expiries(ticker)
print("Available expiries:")
for i, exp in enumerate(expiries):
    print(f"{i}: {exp}")

# Prompt user for expiry
try:
    expiry_idx = int(input(f"Select expiry by index (0-{len(expiries)-1}): "))
    expiry = expiries[expiry_idx]
except Exception:
    expiry = expiries[0]
    print(f'Defaulting to first expiry: {expiry}')

# Fetch option chain
chain = get_option_chain(ticker, expiry)
calls = chain['calls']
puts = chain['puts']

# Show available strikes
print("Available strikes:")
print(calls[['strike', 'lastPrice']].head(10))

# Prompt user for strike
try:
    K = float(input("Enter strike price (e.g., 100): "))
except Exception:
    K = float(calls['strike'].iloc[0])
    print(f'Defaulting to first strike: {K}')

# Set other parameters
today = pd.Timestamp.today()
expiry_date = pd.Timestamp(expiry)
T = (expiry_date - today).days / 365.0
T = max(T, 1/365)  # Avoid zero or negative
r = 0.01  # Assume 1% risk-free rate
sigma = 0.2  # Assume 20% volatility (or estimate from data)
n_steps = 252
n_paths = 5000

# Initialize model and engine
model = GBMModel()
engine = SimulationEngine(model, S0, r, sigma, T, n_steps, n_paths)
pricing = Pricing(engine)

# Simulate paths and plot
paths = engine.simulate()
plot_price_paths(paths)

# Calculate and plot payoff distribution
payoffs = engine.calculate_payoff(paths, K, option_type='call')
plot_payoff_distribution(payoffs)

# Price option and compute Greeks
price = pricing.price_european_option(K, option_type='call')
delta = pricing.compute_delta(K, option_type='call')
gamma = pricing.compute_gamma(K, option_type='call')
print(f"\nSimulated European Call Option Price: {price:.4f}")
print(f"Delta: {delta:.4f}")
print(f"Gamma: {gamma:.4f}") 