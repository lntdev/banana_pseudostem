import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time


# ---------- Nutritional Composition ----------
nutritional_data = {
    "Nutrient": [
        "Dietary Fiber (g/100g)",
        "Potassium (mg/100g)",
        "Calcium (mg/100g)",
        "Magnesium (mg/100g)",
        "Iron (mg/100g)",
        "Phenolic Compounds (mg GAE/g)",
        "Antioxidants (% activity)"
    ],
    "Amount": [3.5, 400, 65, 40, 2.5, 1.35, 22.5]
}

nutritional_df = pd.DataFrame(nutritional_data)

# ---------- Sensory Evaluation ----------
sensory_data = {
    "Treatment": ["Tc", "T1", "T2", "T3", "T4", "T5", "T6"],
    "Texture": [7.5, 8.0, 8.28, 8.0, 7.6, 8.32, 7.83],
    "Colour": [7.6, 7.71, 8.65, 7.85, 7.82, 8.01, 7.8],
    "Taste": [7.6, 7.85, 8.15, 7.71, 7.3, 8.2, 8.1],
    "Flavour": [5.0, 7.71, 8.15, 7.9, 7.6, 8.0, 7.78],
    "Overall": [7.0, 7.85, 8.6, 8.0, 7.8, 8.4, 7.8]
}

sensory_df = pd.DataFrame(sensory_data)

# ---------- Moisture Content ----------
moisture_data = {
    "Treatment": ["Tc", "T2", "T5"],
    "Initial MC%": [6.28, 6.28, 6.31],
    "After 15 days MC%": [8.91, 8.90, 8.82],
    "After 30 days MC%": [12.40, 12.36, 12.33]
}

moisture_df = pd.DataFrame(moisture_data)

# ---------- Microbial Data ----------
microbial_data = {
    "Treatment": ["T2"] * 4 + ["T5"] * 4,
    "Storage Days": [0, 5, 15, 30] * 2,
    "Bacterial Count (x10⁴ CFU/g)": [0, 2, 6, 10, 0, 6, 11, 27],
    "Fungal Count (x10² CFU/g)": [0, 0, 6, 11, 0, 2, 9, 13]
}

microbial_df = pd.DataFrame(microbial_data)

# ---------- Plot 1: Nutritional Composition ----------
plt.figure(figsize=(10, 6))
sns.barplot(x="Amount", y="Nutrient", data=nutritional_df, palette="YlGnBu")
plt.title("Nutritional Composition of Banana Pseudostem")
plt.xlabel("Amount")
plt.ylabel("Nutrient")
plt.tight_layout()
plt.show(block=False)

# ---------- Plot 2: Sensory Evaluation ----------
sensory_melt = sensory_df.melt(id_vars="Treatment", var_name="Attribute", value_name="Score")

plt.figure(figsize=(12, 6))
sns.boxplot(x="Attribute", y="Score", data=sensory_melt, palette="pastel")
plt.title("Sensory Evaluation of Banana Pseudostem Core Candy")
plt.tight_layout()
plt.show(block=False)

# ---------- Plot 3: Moisture Content ----------
moisture_melt = moisture_df.melt(id_vars="Treatment", var_name="Day", value_name="Moisture %")

plt.figure(figsize=(10, 6))
sns.barplot(x="Day", y="Moisture %", hue="Treatment", data=moisture_melt)
plt.title("Moisture Content Changes During Storage")
plt.tight_layout()
plt.show(block=False)

# ---------- Plot 4: Microbial Load ----------
plt.figure(figsize=(10, 6))
sns.lineplot(x="Storage Days", y="Bacterial Count (x10⁴ CFU/g)", hue="Treatment", data=microbial_df, marker='o')
plt.title("Bacterial Growth During Storage")
plt.tight_layout()
plt.show(block=False)

plt.figure(figsize=(10, 6))
sns.lineplot(x="Storage Days", y="Fungal Count (x10² CFU/g)", hue="Treatment", data=microbial_df, marker='o')
plt.title("Fungal Growth During Storage")
plt.tight_layout()
plt.show(block=False)

# ---------- Simulate Real-time Sensor Data ----------
def simulate_realtime_sensor_input():
    print("\n📡 Real-time simulation started! New treatment entries will be added every 5 seconds.")
    print("Press Ctrl+C to stop.\n")
    treatment_counter = len(sensory_df) + 1

    try:
        while True:
            t = f"T{treatment_counter}"
            tex = round(random.uniform(7.0, 9.0), 2)
            col = round(random.uniform(7.0, 9.0), 2)
            tas = round(random.uniform(7.0, 9.0), 2)
            fla = round(random.uniform(7.0, 9.0), 2)
            ova = round((tex + col + tas + fla) / 4, 2)
            mc_init = round(random.uniform(6.0, 6.5), 2)
            mc_15 = round(mc_init + random.uniform(2.5, 3.0), 2)
            mc_30 = round(mc_15 + random.uniform(3.0, 4.0), 2)

            sensory_df.loc[len(sensory_df.index)] = [t, tex, col, tas, fla, ova]
            moisture_df.loc[len(moisture_df.index)] = [t, mc_init, mc_15, mc_30]

            print(f"✅ Added {t} | Texture: {tex}, Colour: {col}, Taste: {tas}, Moisture Day 0: {mc_init}%")

            treatment_counter += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
# ---------- Interactive Example ----------
def interactive_summary():
    print("\nWelcome to Banana Pseudostem Candy Data Viewer!")
    print("Choose a section to display:")
    print("1. Nutritional Composition")
    print("2. Sensory Evaluation")
    print("3. Moisture Content")
    print("4. Microbial Evaluation")
    print("5. Simulate Real-Time Sensor Input")
    print("6. Exit")


    while True:
        choice = input("\nEnter your choice (1–6): ").strip()
        if choice == "1":
            print("\nNutritional Composition:\n", nutritional_df)
        elif choice == "2":
            print("\nSensory Evaluation Scores:\n", sensory_df)
        elif choice == "3":
            print("\nMoisture Content During Storage:\n", moisture_df)
        elif choice == "4":
            print("\nMicrobial Evaluation:\n", microbial_df)
        elif choice == "5":
            simulate_realtime_sensor_input()
        elif choice == "6":
            print("👋 Exiting. Thanks for using the dashboard!")
            break

interactive_summary()
