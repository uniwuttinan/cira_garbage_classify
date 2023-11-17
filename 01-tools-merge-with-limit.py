import os
import shutil
import random

LIMIT = 50

def rename_and_copy_images(source_folder, output_folder, material_type):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Filter files based on allowed extensions (jpg and png)
    allowed_extensions = {'.jpg', '.jpeg', '.png'}
    files = [f for f in files if os.path.splitext(f)[1].lower() in allowed_extensions]

    # Rename and move files
    for i, file_name in enumerate(files):
        if i >= LIMIT:
            return
        file_extension = os.path.splitext(file_name)[1].lower()
        new_file_name = f"{material_type}_{str(i + 1).zfill(3)}{file_extension}"
        source_path = os.path.join(source_folder, file_name)
        output_path = os.path.join(output_folder, new_file_name)

        # Rename and move the file
        shutil.copy(source_path, output_path)

if __name__ == "__main__":
    # Set the source folder, output folder, and material types
    source_folder = "01-source-grouping"
    output_folder = "02-source-merged-limit"
    material_types = ["HDPE", "LDPE", "OTHER", "PET", "PP", "PS", "PVC",]

    os.makedirs(output_folder, exist_ok=True)

    # Process images for each material type
    for material_type in material_types:
        material_source_folder = os.path.join(source_folder, material_type)
        rename_and_copy_images(material_source_folder, output_folder, material_type)
