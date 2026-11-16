"""
RECORD CHECK  -  my version
===========================

Name  : Abdullah Laghari
Lane  : IT
Date  : 14 - 11 - 2006

Run it:   python template.py"""

def parse_line(raw_line):
    # Clean one messy line and return it as a dictionary:
    # make everything small letters and remove spaces at the two ends
    line= raw_line.strip().lower()

    # cut off the hostname at the first comma,
    hostname, rest = line.split(",", 1)
    record = {"hostname": hostname.strip()}

    # go through each key=value piece and save it as a number
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())

    return record


def status_of(used, total):
    #give back OVER LIMIT, WARNING or OK
    # work out how full the server is
    percent= used / total * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# five messy lines with different spaces and different capital letters
lines= [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    " srv-03   ,   Used = 95 ,  Total = 100",
    "Srv-04,used=45,total=100",
    "   SRV-05 ,used=100,total=100   ",
]

# clean each line and print it with its status
for raw_line in lines:
    record = parse_line(raw_line)
    print(record, status_of(record["used"], record["total"]))
