import numpy as np
import matplotlib.pyplot as plt

class AtterbergLimitsAnalyzer:
    def __init__(self, data):
        self.data = data
        self.moisture_content = data[:, 0]
        self.impact_count = data[:, 1]
        self.liquid_limit_slope = None
        self.liquid_limit_intercept = None

    def analyze_liquid_limit(self):
        # Fit a line to the data points using numpy's polyfit
        liquid_limit_line = np.polyfit(self.impact_count, self.moisture_content, 1)
        self.liquid_limit_slope = liquid_limit_line[0]
        self.liquid_limit_intercept = liquid_limit_line[1]
        liquid_limit_fit = self.liquid_limit_slope * self.impact_count + self.liquid_limit_intercept

        print("Liquid Limit Analysis:")
        print(f"Slope: {self.liquid_limit_slope}")
        print(f"Intercept: {self.liquid_limit_intercept}")

        plt.scatter(self.impact_count, self.moisture_content, label="Data Points")
        plt.plot(self.impact_count, liquid_limit_fit, label="Best Fit Line")
        plt.xlabel("Impact Count")
        plt.ylabel("Moisture Content")
        plt.title("Atterberg Limits Analysis")
        plt.legend()
        plt.show()

    def estimate_moisture_content(self, impact_count):
        if self.liquid_limit_slope is not None and self.liquid_limit_intercept is not None:
            return self.liquid_limit_slope * impact_count + self.liquid_limit_intercept
        else:
            print("Liquid limit analysis must be performed first.")

# Data
data = np.array([
    [68.63, 49],
    [66.41, 20],
    [62.6, 19],
    [59.85, 11],
])

# Create an instance of AtterbergLimitsAnalyzer
analyzer = AtterbergLimitsAnalyzer(data)

# Analyze the liquid limit and plot the relationship
analyzer.analyze_liquid_limit()

# Estimate the moisture content at 25 impacts
estimated_moisture_content = analyzer.estimate_moisture_content(25)
print(f"Estimated moisture content at 25 impacts: {estimated_moisture_content}")

