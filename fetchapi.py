import requests
import csv

# Fetch product data from Fake Store API
response = requests.get("https://fakestoreapi.com/products")
products = response.json()

# Save data to CSV
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Title", "Price", "Description", "Category", "Image URL"])  # Headers
    for product in products:
        writer.writerow([product["id"], product["title"], product["price"], product["description"], product["category"], product["image"]])

print("Product data saved to products.csv!")
