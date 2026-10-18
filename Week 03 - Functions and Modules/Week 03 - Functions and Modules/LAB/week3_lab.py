"""
RECORD CHECK  -  my version
===========================

Name  : Abdullah Laghari
Lane  :  IT
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def border():
    return "=" * 34

def report_line(label, value):
    return f" {label:<12}: {value:>11}"

def check(value, limit):
    free = limit - value
    percent = (value / limit) * 100
    return free, percent

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

hostname = input("Hostname: ")
used = float(input("GB used: "))
total = float(input("GB total: "))

free, percent = check(used, total)
status = status_of(percent)

print(border())
print(f" RECORD CHECK  -  {hostname}")
print(border())
print(report_line("Used", f"{used:.2f}"))
print(report_line("Total", f"{total:.2f}"))
print(report_line("Free", f"{free:.2f}"))
print(report_line("Percent", f"{percent:.2f}") + " %")
print(report_line("Status", status))
print(border())