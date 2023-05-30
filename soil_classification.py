class Soil:
    def __init__(self, liquid_limit, plasticity_index):
        self.liquid_limit = liquid_limit
        self.plasticity_index = plasticity_index
        self.classification = ""

    def classify(self):
        if self.liquid_limit < 50 and self.plasticity_index < 12:
            self.classification = "Low Plasticity (CL)"
        elif self.liquid_limit < 50 and 12 <= self.plasticity_index <= 20:
            self.classification = "Low to Medium Plasticity (CL-ML)"
        elif self.liquid_limit < 50 and self.plasticity_index > 20:
            self.classification = "Medium Plasticity (ML)"
        elif self.liquid_limit >= 50 and self.plasticity_index < 10:
            self.classification = "High Plasticity (CH)"
        elif self.liquid_limit >= 50 and 10 <= self.plasticity_index <= 20:
            self.classification = "High to Medium Plasticity (CH-MH)"
        elif self.liquid_limit >= 50 and self.plasticity_index > 20:
            self.classification = "Medium Plasticity (MH)"
        else:
            self.classification = "Invalid data"

    def get_classification(self):
        return self.classification

# Example usage
liquid_limit = 40
plasticity_index = 15

soil = Soil(liquid_limit, plasticity_index)
soil.classify()
classification = soil.get_classification()

print(f"Soil Classification: {classification}")
