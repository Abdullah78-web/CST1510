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

import pandas as pd
import matplotlib.pyplot as plt

#first read my own csv file into a table
df= pd.read_csv("my_servers.csv")

#work out how full each server is, as a percent of its total
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

#then give each server a status using a lambda inside apply
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print(df)

#print only the servers that are not ok using a filter and no loop
print(df[df["status"] != "OK"])

# group by status and count how many servers are in each group
counts = df.groupby("status").size()
print(counts)
df.to_csv("my_servers_report.csv", index=False)

#bar chart
counts.plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.savefig("my_status_counts.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case