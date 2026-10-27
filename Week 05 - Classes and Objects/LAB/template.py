"""
RECORD CHECK  -  my version
===========================

Name  :Abdullah Laghari
Lane  :IT  
Date  :24-10-26
"""

# ====================================================================== CLASS
class Record:
    def __init__(self, label,value,limit):
        self.label = label
        self.value= value
        self.limit = limit

    def status(self):
        ratio = self.value/ self.limit
        if ratio >= 1.0:
            return "OVER LIMIT"
        if ratio >= 0.9:
            return "WARNING"
        return "OK"


# ==================================================================== OUTPUT
with open("my_data.txt", "w") as f:
    f.write("R-001,87,100\n")
    f.write("R-002,120,100\n")
    f.write("R-003,95,100\n")
    f.write("R-004,40,100\n")

def load_records(path):
    loaded = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            loaded.append(Record(label, float(value), float(limit)))
    return loaded

records= load_records("my_data.txt")
over_limit_total= 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print("Label :", record.label)
    print("Value :", record.value)
    print("Limit :", record.limit)
    print("Status:", record.status())

    if record.status() == "OVER LIMIT":
        over_limit_total += 1

    print("=" * 34)
    
print()
print("Records over limit:", over_limit_total)


# ==========================================================================

