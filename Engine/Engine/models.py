from abc import ABC, abstractmethod
import numpy as np

class AssetPriceModel(ABC):
    @abstractmethod
    def simulate_paths(self, S0, r, T, sigma, n_steps, n_paths):
        pass

class GBMModel(AssetPriceModel):
    def simulate_paths(self, S0, r, T, sigma, n_steps, n_paths):
        dt = T / n_steps
        paths = np.zeros((n_paths, n_steps + 1))
        paths[:, 0] = S0
        for t in range(1, n_steps + 1):
            z = np.random.standard_normal(n_paths)
            paths[:, t] = paths[:, t-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
        return paths

class HestonModel(AssetPriceModel):
    def simulate_paths(self, S0, r, T, sigma, n_steps, n_paths):
        # Stub for Heston model
        raise NotImplementedError("Heston model not implemented yet.") 