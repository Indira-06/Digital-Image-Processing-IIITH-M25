from utils.image_utils import read_image, write_image, change_contrast

def run_q4():
    input_path = "input_images/cat.jpeg"
    output_high = "output_images/q4_high_contrast.jpg"
    output_low = "output_images/q4_low_contrast.jpg"

    img = read_image(input_path)

    high_contrast = change_contrast(img, 1.5)  # more punch
    low_contrast = change_contrast(img, 0.5)   # flatter

    write_image(high_contrast, output_high)
    write_image(low_contrast, output_low)

    print("Saved high and low contrast images!")
