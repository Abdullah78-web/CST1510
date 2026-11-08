import pandas as pd

inventory = pd.DataFrame({
    "item": ["laptop", "mouse", "keyboard", "monitor", "headphones"],
    "price": [1200.0, 25.5, 75.0, 300.0, 65],
    "stock": [15, 120, 50, 30, 25],
})
print(inventory)

grouped = inventory.groupby("item")
#print(grouped["stock"].max())

print(grouped["price"].agg(["mean", "max", "min"]))