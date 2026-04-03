# clean_ship_ops.py
class SubseaMission:
    def __init__(self):
        self.loto_complete = False
        self.hull_status = "Fouled"
        self.prop_grade = "D"
        self.efficiency = 80

    def safety_check(self):
        print("Safety: Performing LOTO... Engines Locked.")
        self.loto_complete = True

    def run_brush_kart(self):
        if not self.loto_complete:
            print("Error: Safety LOTO not complete!")
            return
        
        print("Operation: Running Brush Kart...")
        self.hull_status = "Clean"
        print("Hull is now clean.")

    def polish_propeller(self):
        print("Operation: Polishing Propeller...")
        # Move from Grade D to Grade A
        for grade in ["C", "B", "A"]:
            self.prop_grade = grade
            print("Surface Grade now: " + self.prop_grade)

    def show_report(self):
        print("--- FINAL REPORT ---")
        print("Hull: " + self.hull_status)
        print("Propeller Grade: " + self.prop_grade)
        if self.prop_grade == "A" and self.hull_status == "Clean":
            print("Vessel Efficiency: 100%")

# Run it
mission = SubseaMission()
mission.safety_check()
mission.run_brush_kart()
mission.polish_propeller()
mission.show_report()
