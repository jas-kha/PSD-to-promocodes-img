import os
import zipfile
from datetime import datetime

OUTPUT_DIRECTORY = "output"
ZIP_FILE_NAME = f"promo_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"

def zip_output_folder(output_dir, zip_file_name):
    """Create a ZIP archive with progress display."""
    if not os.path.exists(output_dir):
        print(f"❌ Output folder '{output_dir}' does not exist.")
        return

    files = []
    for root, _, file_names in os.walk(output_dir):
        for file in file_names:
            files.append(os.path.join(root, file))

    total_files = len(files)
    if total_files == 0:
        print(f"⚠️ Output folder '{output_dir}' is empty.")
        return

    print(f"📦 Creating ZIP: {zip_file_name}")
    with zipfile.ZipFile(zip_file_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for index, file_path in enumerate(files, start=1):
            arcname = os.path.relpath(file_path, output_dir)
            zipf.write(file_path, arcname)

            # Show progress
            percent = (index / total_files) * 100
            print(f"[{index}/{total_files}] {percent:.1f}% - {arcname}")

    print(f"✅ ZIP file created successfully: {zip_file_name}")

if __name__ == "__main__":
    zip_output_folder(OUTPUT_DIRECTORY, ZIP_FILE_NAME)
