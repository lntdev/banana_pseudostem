import matplotlib.pyplot as plt
import csv

class BananaPseudostemCoreCandy:
    def __init__(self, initial_weight, initial_moisture_content):
        self.initial_weight = initial_weight
        self.initial_moisture_content = initial_moisture_content
        self.current_weight = initial_weight
        self.current_moisture_content = initial_moisture_content
        self.total_time = 0
        self.history = []

    def apply_osmosis(self, solution_brix, time_hours):
        moisture_loss = 0.05 * solution_brix * (time_hours / 10)
        weight_loss = self.current_weight * (moisture_loss / 100)

        self.current_weight -= weight_loss
        self.current_moisture_content -= moisture_loss
        self.total_time += time_hours

        self._log("Osmosis", time_hours, solution_brix, weight_loss, moisture_loss)

    def apply_drying(self, temperature, time_hours):
        moisture_loss = (temperature / 100) * (time_hours / 5)
        weight_loss = self.current_weight * (moisture_loss / 100)

        self.current_weight -= weight_loss
        self.current_moisture_content -= moisture_loss
        self.total_time += time_hours

        self._log("Drying", time_hours, temperature, weight_loss, moisture_loss)

    def _log(self, process_type, time_hours, condition, weight_loss, moisture_loss):
        entry = {
            "Process": process_type,
            "Time (h)": self.total_time,
            "Condition": condition,
            "Weight (g)": round(self.current_weight, 2),
            "Moisture (%)": round(self.current_moisture_content, 2),
            "Weight Loss (g)": round(weight_loss, 2),
            "Moisture Loss (%)": round(moisture_loss, 2)
        }
        self.history.append(entry)
        print(f"[{process_type}] Time: {self.total_time}h, Weight: {entry['Weight (g)']}g, Moisture: {entry['Moisture (%)']}%")

    def export_log(self, filename):
        keys = self.history[0].keys()
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.history)
        print(f"\n📄 Process log saved to {filename}")

    def plot_results(self):
        times = [entry["Time (h)"] for entry in self.history]
        weights = [entry["Weight (g)"] for entry in self.history]
        moistures = [entry["Moisture (%)"] for entry in self.history]

        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(times, weights, marker='o', color='green')
        plt.title("Weight vs Time")
        plt.xlabel("Time (hours)")
        plt.ylabel("Weight (g)")
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.plot(times, moistures, marker='o', color='blue')
        plt.title("Moisture Content vs Time")
        plt.xlabel("Time (hours)")
        plt.ylabel("Moisture (%)")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

# Function to take float input safely
def get_float_input(prompt, default):
    try:
        return float(input(f"{prompt} (default: {default}): ") or default)
    except ValueError:
        print("Invalid input. Using default.")
        return default

# ----------------------
# Start of the demo
# ----------------------

print("\nWelcome to Osmo-Dehydrated Banana Pseudostem Core Candy Simulation 🍬")

# Step 1: Initial Input
initial_weight = get_float_input("Enter initial weight of banana pseudostem core (grams)", 100)
initial_moisture = get_float_input("Enter initial moisture content (%)", 90)

candy = BananaPseudostemCoreCandy(initial_weight, initial_moisture)

# Step 2: Osmosis
solution_brix = get_float_input("Enter Brix level of sugar solution", 50)
osmosis_time = get_float_input("Enter duration of osmosis (hours)", 6)
candy.apply_osmosis(solution_brix, osmosis_time)

# Step 3: Drying Stage 1
dry_temp1 = get_float_input("Enter drying temperature for Stage 1 (°C)", 60)
dry_time1 = get_float_input("Enter drying duration for Stage 1 (hours)", 5)
candy.apply_drying(dry_temp1, dry_time1)

# Optional: Drying Stage 2
add_stage = input("Do you want to add another drying stage? (yes/no): ").strip().lower()
if add_stage == 'yes':
    dry_temp2 = get_float_input("Enter drying temperature for Stage 2 (°C)", 70)
    dry_time2 = get_float_input("Enter drying duration for Stage 2 (hours)", 3)
    candy.apply_drying(dry_temp2, dry_time2)

# Export and visualize results
candy.export_log("banana_pseudostem_log.csv")
candy.plot_results()
