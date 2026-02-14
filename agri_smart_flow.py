import random

def get_agri_decision(moisture, weather):
....if moisture < 30 and weather != "Heavy Rain":
........return "LOW MOISTURE. Decision: Turn the water irrigation ON."
....elif weather == "Heavy Rain":
........return "RAIN DETECTED. Decision: Keep the water irrigation OFF."
....else:
........return "MOISTURE SUFFICIENT. Decision: Keep the water irrigation OFF."

current_moisture = random.randint(10, 60)
upcoming_weather = random.choice(["Sunny", "Heavy Rain", "Cloudy"])

print("\n--- AgriSmart Monitoring System ---")
print(f"Current Soil Moisture: {current_moisture}%")
print(f"Weather Forecast: {upcoming_weather}")

ai_output = get_agri_decision(current_moisture, upcoming_weather)
print(f"AI Recommendation: {ai_output}")

if "ON" in ai_output.upper():
....print("STATUS: Water Valve OPENED.")
else:
....print("STATUS: Water Valve CLOSED.")
