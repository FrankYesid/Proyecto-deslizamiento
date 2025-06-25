import requests
from pathlib import Path
from typing import List
import os

def download_sample_images(output_dir: str = "samples") -> None:
    """Download sample satellite images for testing"""
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # List of sample satellite images
    sample_urls = [
        "https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x5400x2700.jpg",
        "https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x5400x2700.png",
        "https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x5400x2700.tiff"
    ]

    for url in sample_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            # Extract filename from URL
            filename = os.path.basename(url)
            filepath = output_path / filename
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded: {filename}")
            
        except Exception as e:
            print(f"Failed to download {url}: {str(e)}")

if __name__ == "__main__":
    download_sample_images()
