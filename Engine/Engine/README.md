# Monte Carlo Engine for European Options

## Overview
This python project is a modular Monte Carlo simulation engine for pricing European options and computing Greeks (Delta, Gamma) using Geometric Brownian Motion (GBM). It is designed for extensibility, performance, and clarity, making it suitable for both software engineering and quantitative finance applications.

## Features
- Modular design: Easily extend with new models (e.g., Heston)
- Simulate asset price paths using stochastic models
- Price European call and put options
- Compute Greeks (Delta, Gamma) - two of which I find most interesting 
- Input validation and output checks
- Visualization of price paths, payoff distributions, and Greeks
- Fetch real market data via API (yfinance)

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-directory>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Example
```python
from models import GBMModel
from simulation_engine import SimulationEngine
from pricing import Pricing
from visualization import plot_price_paths, plot_payoff_distribution

# Parameters
S0, r, sigma, T, n_steps, n_paths = 100, 0.05, 0.2, 1.0, 252, 1000
K = 100

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
print(f"Call Price: {price:.4f}, Delta: {delta:.4f}, Gamma: {gamma:.4f}")
```

## Module Descriptions
- `models.py`: Asset price models (GBM, Heston stub)
- `simulation_engine.py`: Path simulation and payoff calculation
- `pricing.py`: Option pricing and Greeks
- `validation.py`: Input/output validation
- `visualization.py`: Plotting functions (Matplotlib)
- `data_loader.py`: Fetches real market data via yfinance

## License
MIT 
