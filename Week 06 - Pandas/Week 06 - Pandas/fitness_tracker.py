import pandas as pd

gym = pd.DataFrame({
    "Member_Name": ["Abdullah", "Ismail", "Parham", "Ali"],
    "Workout_Type": ["Cardio", "Strength", "Yoga", "Cardio"],
    "Calories_Burned": [2200, 1800, 600, 1500],
    "Heart_Rate": [151.2, 135.6, 49.3, 92.0],
    "Duration_Mins": [32, 52, 130, 21],
})

#print(gym)

gym["Burn_Rate_Per_Min"] = gym["Calories_Burned"]/ gym["Duration_Mins"]

#print(gym)

#print(gym[["Member_Name", "Burn_Rate_Per_Min"]])

#print(gym.iloc[0])
#print(gym.loc[1, "Member_Name"])