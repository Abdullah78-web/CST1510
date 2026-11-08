import pandas as pd

values = pd.Series([87, 120, 45])
print(values)
inventory = pd.DataFrame(
    {
    "item": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [1200.0, 25.5, 75.0, 300.0],
    "stock": [15, 120, 50, 30],
})
print(inventory)
servers = pd.read_csv("servers.csv")
print(servers)
print(servers.dtypes)
servers["percent"] = (servers["used"] / servers["total"]) * 100
print(servers)