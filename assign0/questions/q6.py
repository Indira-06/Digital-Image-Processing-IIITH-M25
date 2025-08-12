from utils.image_utils import read_image, write_image, rgb_to_grayscale, grayscale_to_pseudocolor

def run_q6():
    input_path = "input_images/cat.jpeg"

    gray = rgb_to_grayscale(read_image(input_path))  # default = luminosity
    pseudo = grayscale_to_pseudocolor(gray)

    write_image(pseudo, "output_images/q6_pseudocolor.jpg")
    print("Pseudocolor image saved!")
