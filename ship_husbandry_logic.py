# ---------------------------------------------------------
# PROJECT: Ship Husbandry Maintenance & Analytics Logic
# PURPOSE: Technical decision-making simulation for underwater 
#          inspections and maritime logistics.
# ---------------------------------------------------------

def check_hull_status(fouling_type: str) -> str:
    """Simulates the decision to deploy a Brush Kart based on fouling."""
    # Actionable categories for maintenance
    heavy_fouling = ["Barnacles", "Heavy Slime", "Tubeworms"]
    
    if fouling_type in heavy_fouling:
        return f"ACTION: Deploy Hydraulic Brush Kart. Priority: HIGH. (Type: {fouling_type})"
    return "STATUS: Hull is within hydrodynamic tolerance. No cleaning required."

def calculate_shaft_wear(current_poker: float, baseline: float) -> str:
    """Logic for Poker Gauge measurement and wear-down analysis."""
    # abs() handles potential reading order errors; round(x, 2) ensures clean data
    wear_down = round(abs(current_poker - baseline), 2)
    MAX_LIMIT = 2.0  # mm
    
    if wear_down >= MAX_LIMIT:
        return f"ALERT: Wear is {wear_down}mm. CRITICAL (Exceeds {MAX_LIMIT}mm limit). Schedule replacement."
    return f"STATUS: Wear is {wear_down}mm. Shaft alignment is STABLE."

def verify_sensor_seal(knocks_heard: int) -> str:
    """Simulates the 'handshake' protocol for sensor replacement."""
    signals = {
        2: "COMMUNICATION: Handshake confirmed (2 Knocks). Area is dry. Begin swap.",
        3: "COMMUNICATION: ABORT (3 Knocks). Seal compromised or Engine Room intervention."
    }
    return signals.get(knocks_heard, "STATUS: Waiting for acoustic signal from Engine Room...")

# --- SIMULATION OF A TECHNICAL INSPECTION ---

def run_inspection_report():
    print("="*40)
    print("   MARITIME TECHNICAL INSPECTION LOG   ")
    print("="*40)

    # 1. Hull Observation
    print(f"\n[1/3] HULL INSPECTION:")
    print(check_hull_status("Barnacles"))

    # 2. Poker Gauge Reading (Simulation: 12.5mm vs 10.8mm)
    print(f"\n[2/3] SHAFT WEAR ANALYSIS:")
    print(calculate_shaft_wear(12.5, 10.8))

    # 3. Sensor Replacement (Received 2 knocks)
    print(f"\n[3/3] SENSOR SWAP PROTOCOL:")
    print(verify_sensor_seal(2))

    print("\n" + "="*40)
    print("        INSPECTION COMPLETED          ")
    print("="*40)

if __name__ == "__main__":
    run_inspection_report()
