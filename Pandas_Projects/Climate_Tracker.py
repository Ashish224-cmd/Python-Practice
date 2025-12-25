import pandas as pd 
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/hp/OneDrive/Documents/TEXT_FILES/CH_DECORATORS/climate.csv")
#df.info()
#convert Date column object type to datetime64 type
df["Date"] = pd.to_datetime(df["Date"])
df.info()
# Step 3: Plot temperature trends 
print(plt.figure(figsize=(10, 6)))
for country in df["Country"].unique():
    #print(country)
    country_data = df[df['Country']==country]
    print(country_data)
    plt.plot(country_data['Date'],country_data['AverageTemperature'], marker='o',label=country)
    
plt.title('Average Temperature Trends (1920–2020)')
plt.xlabel('Year')
plt.ylabel('Average Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()