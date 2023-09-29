import os
os.system("pip install bs4")

from ThornImage_Remast import ImageThorn

image_thorn = ImageThorn()

url = "https://legends.dbz.space/characters/"  # Replace with the URL of your choice

output_folder = "./dbz"

image_thorn.scrape_images(url, output_folder)

print(f"Images scraped and saved to {output_folder}")
