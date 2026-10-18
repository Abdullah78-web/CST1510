"""
RECORD CHECK  -  my version
===========================

Name  :Abdullah Laghari
Lane  :IT
Date  :17-10-26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
with open("servers.txt", "w") as f:
    f.write("srv-01,87,120\nsrv-02,110,120\nsrv-03,130,120\n")

def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records

def check_record(record):
    if record["value"] > record["limit"]:
        return "OVER LIMIT"
    elif record["value"] >= record["limit"] * 0.8:
        return "WARNING"
    return "OK"

try:
    records = load_records("servers.txt")
except FileNotFoundError:
    print("File not found")
    records = []

over = 0
with open("results.txt", "w") as out:
    for record in records:
        status = check_record(record)
        print(record["label"], status)
        out.write(record["label"] + "," + status + "\n")
        if status == "OVER LIMIT":
            over = over + 1

print(over, "of", len(records), "were over limit")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
