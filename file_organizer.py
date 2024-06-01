import os
import shutil
import argparse
import logging
from PIL import Image
import PyPDF2
from mutagen.mp3 import MP3

logging.basicConfig(filename='file_organizer.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to extract metadata from images
def extract_image_metadata(file_path):
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                date_taken = exif_data.get(36867)  # Tag for date taken
                if date_taken:
                    return date_taken[:10]  # Extracting date in 'YYYY-MM-DD' format
    except Exception as e:
        logging.error(f"Error extracting metadata from image: {e}")

# Function to extract metadata from PDFs
def extract_pdf_metadata(file_path):
    try:
        with open(file_path, 'rb') as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            if '/CreationDate' in info:  # Tag for creation date
                return info['/CreationDate'][:10]  # Extracting date in 'YYYY-MM-DD' format
    except Exception as e:
        logging.error(f"Error extracting metadata from PDF: {e}")

# Function to extract metadata from audio files
def extract_audio_metadata(file_path):
    try:
        audio = MP3(file_path)
        if 'TPE1' in audio:  # Tag for artist
            return audio['TPE1'].text[0]  # Extracting artist name
    except Exception as e:
        logging.error(f"Error extracting metadata from audio file: {e}")

# Function to organize files based on metadata
def organize_files(source_dir, destination_structure):
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file_path)
            metadata = None
            if ext.lower() == '.jpg' or ext.lower() == '.jpeg' or ext.lower() == '.png':
                metadata = extract_image_metadata(file_path)
            elif ext.lower() == '.pdf':
                metadata = extract_pdf_metadata(file_path)
            elif ext.lower() == '.mp3':
                metadata = extract_audio_metadata(file_path)
            # Add support for more file types and metadata extraction here
            
            if metadata:
                destination_dir = os.path.join(destination_structure, metadata)
                os.makedirs(destination_dir, exist_ok=True)
                shutil.move(file_path, destination_dir)
                logging.info(f"Moved {file} to {destination_dir}")

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Organize files based on metadata")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("--destination_structure", help="Custom destination structure (e.g., 'Year/Month')")
    args = parser.parse_args()

    # Check if the source directory exists
    if not os.path.isdir(args.source_dir):
        print("Error: Source directory not found.")
        return

    # If custom destination structure is provided, use it; otherwise, prompt the user
    if args.destination_structure:
        destination_structure = args.destination_structure
    else:
        destination_structure = input("Enter the destination structure (e.g., 'Year/Month'): ")

    # Organize files in the source directory based on metadata
    organize_files(args.source_dir, destination_structure)

if __name__ == "__main__":
    main()
