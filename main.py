import os
from psd_tools import PSDImage
from PIL import Image, ImageDraw, ImageFont

# === Configuration ===
PSD_FILE_PATH = "max_design.psd"
PROMO_CODES_FILE_PATH = "promocodes.txt"
OUTPUT_DIRECTORY = "output"
FONT_PATH = "font/arial.ttf"  # Change to your font path
FONT_SIZE = 75
TEXT_POSITION = (505, 310)  # Coordinates (x, y)
TEXT_COLOR = "white"

def load_promo_codes(file_path):
    """Read promo codes from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def prepare_output_directory(directory_path):
    """Create output directory if it doesn't exist."""
    os.makedirs(directory_path, exist_ok=True)

def generate_promo_images(psd_file, promo_codes, font_path, font_size, text_position, text_color):
    """Generate PNG images with promo codes placed on a PSD template."""
    psd = PSDImage.open(psd_file)
    font = ImageFont.truetype(font_path, font_size)

    for index, code in enumerate(promo_codes, start=1):
        # Convert PSD to PNG
        composite_image = psd.composite().convert("RGBA")

        # Draw promo code on image
        draw = ImageDraw.Draw(composite_image)
        draw.text(text_position, code, font=font, fill=text_color)

        # Save output
        output_path = os.path.join(OUTPUT_DIRECTORY, f"promo_code_{index}.png")
        composite_image.save(output_path)

        print(f"✅ Saved: {output_path}")

def main():
    prepare_output_directory(OUTPUT_DIRECTORY)
    promo_codes = load_promo_codes(PROMO_CODES_FILE_PATH)
    generate_promo_images(
        psd_file=PSD_FILE_PATH,
        promo_codes=promo_codes,
        font_path=FONT_PATH,
        font_size=FONT_SIZE,
        text_position=TEXT_POSITION,
        text_color=TEXT_COLOR
    )
    print("🎉 All promo code images generated successfully!")

if __name__ == "__main__":
    main()
