import numpy as np
import pandas as pd

path="AQI_Data.csv"
df = pd.read_csv(path)
print(df)

print("First 5 rows \n")
print(df.head(5))
print("\n")

print("last 6 rows \n")
print(df.tail(6))
print("\n")

print("Summary of data \n")
print(df.describe())
print("\n")

print("Mean for each city \n")
print(df.groupby("City")[["AQI","PM2.5","PM10"]].mean())
print("\n")

print("missing values")
miss=df.isnull().sum()
print(miss)

df["AQI"]=df["AQI"].fillna(df["AQI"].mean())
df["PM2.5"]=df["PM2.5"].fillna(df["PM2.5"].mean())
df["PM10"]=df["PM10"].fillna(df["PM10"].mean())
df["NO2"]=df["NO2"].fillna(df["NO2"].mean())
df["CO"]=df["CO"].fillna(df["CO"].mean())
df["O3"]=df["O3"].fillna(df["O3"].mean())
df["SO2"]=df["SO2"].fillna(df["SO2"].mean())

print(df)
print("\n")

print("Mean of AQI:",df["AQI"].mean())
print("Median of AQI:",df["AQI"].median())
print("Standard Deviation of AQI:",df["AQI"].std())