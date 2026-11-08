import pandas as pd

inventory = pd.DataFrame({
    "item": ["laptop", "mouse", "keyboard", "monitor", "headphones"],
    "category": ["technology", "technology", "technology", "audio"]
    "price": [1200.0, 25.5, 75.0, 300.0, 65],
    "stock": [15, 120, 50, 30, 25],
})
print(inventory)

lambda p: (
    "Too expensive" if p >= 200
    else "acceptable" if p >= 100
    else "cheap"
)

#inventory["status"] = inventory["percent"].apply(classify)
print(inventory)