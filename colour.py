import tkinter as tk
from tkinter import ttk
import random

# Define possible parent genotypes
parent_colors = {
    'Yellow': ('Y', 'y', 'Y', 'y'),  
    'Blue': ('B', 'b', 'b', 'b'),    # Hypothetical genotype for blue
    'Red': ('r', 'r', 'R', 'r'),     # Hypothetical genotype for red
    'Green': ('G', 'g', 'g', 'g'),
    'Orange': ('O', 'o', 'o', 'o'),
    'Grey': ('G', 'g', 'G', 'g'),
    'White': ('W', 'w', 'w', 'w'),
    'Pink': ('P', 'p', 'p', 'p'),
    'Black': ('B', 'b', 'B', 'b'),
    'Brown': ('O', 'o', 'b', 'b')
}

# Hypothetical target genotype for purple color
target_genotype = {'B': 1, 'b': 1, 'R': 1, 'r': 1}

# Revised function to check if offspring genotype is purple
def is_purple(genotype):
    count = {'B': 0, 'b': 0, 'R': 0, 'r': 0}
    for allele in genotype:
        if allele in count:
            count[allele] += 1
    return all(count[key] >= value for key, value in target_genotype.items())

# Function to simulate crossing two parents
def simulate_crossing(parent1, parent2):
    return [random.choice([parent1[i], parent2[i]]) for i in range(len(parent1))]

# Create GUI
class BreedingSimulatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Corn Kernel Breeding Simulator")
        self.geometry("400x300")

        self.selected_parents = []

        # Dropdowns for parent selection
        self.parent1_var = tk.StringVar()
        self.parent2_var = tk.StringVar()
        self.create_dropdowns()

        # Button to simulate cross
        ttk.Button(self, text="Simulate Cross", command=self.simulate_cross).pack(pady=20)
        
        # Label to display results
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()

    def create_dropdowns(self):
        ttk.Label(self, text="Select Parent 1").pack()
        parent1_dropdown = ttk.OptionMenu(self, self.parent1_var, *parent_colors.keys())
        parent1_dropdown.pack()

        ttk.Label(self, text="Select Parent 2").pack()
        parent2_dropdown = ttk.OptionMenu(self, self.parent2_var, *parent_colors.keys())
        parent2_dropdown.pack()

    def simulate_cross(self):
        parent1 = parent_colors[self.parent1_var.get()]
        parent2 = parent_colors[self.parent2_var.get()]

        offspring = simulate_crossing(parent1, parent2)
        result_text = f"Offspring Genotype: {offspring}\n"

        if is_purple(offspring):
            result_text += "Produces Purple Kernels."
        else:
            result_text += "Does not produce Purple Kernels."

        self.result_label.config(text=result_text)

# Run the GUI application
if __name__ == "__main__":
    app = BreedingSimulatorGUI()
    app.mainloop()
