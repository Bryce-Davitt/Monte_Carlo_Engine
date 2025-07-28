import numpy as np

class Pricing:
    def __init__(self, simulation_engine):
        self.engine = simulation_engine

    def price_european_option(self, K, option_type='call'):
        paths = self.engine.simulate()
        payoffs = self.engine.calculate_payoff(paths, K, option_type)
        price = np.exp(-self.engine.r * self.engine.T) * np.mean(payoffs)
        return price

    def compute_delta(self, K, option_type='call', dS=1e-4):
        S0 = self.engine.S0
        self.engine.S0 = S0 + dS
        price_up = self.price_european_option(K, option_type)
        self.engine.S0 = S0 - dS
        price_down = self.price_european_option(K, option_type)
        self.engine.S0 = S0  # reset
        delta = (price_up - price_down) / (2 * dS)
        return delta

    def compute_gamma(self, K, option_type='call', dS=1e-4):
        S0 = self.engine.S0
        self.engine.S0 = S0 + dS
        price_up = self.price_european_option(K, option_type)
        self.engine.S0 = S0
        price_mid = self.price_european_option(K, option_type)
        self.engine.S0 = S0 - dS
        price_down = self.price_european_option(K, option_type)
        self.engine.S0 = S0  # reset
        gamma = (price_up - 2 * price_mid + price_down) / (dS ** 2)
        return gamma 