import requests
import pandas as pd

# Fetch data from the Fake Store API
response = requests.get("https://fakestoreapi.com/products")
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
driveFile = "https://www.dropbox.com/scl/fi/obuvrc4ky4jjcttfhu6uw/products.csv?rlkey=lalz1ze115qgwhqyoxwfmn4vx&st=ekwiktwg&dl=0"
df.to_csv(driveFile, index=False)
