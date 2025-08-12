from utils.image_utils import read_image, write_image, rgb_to_grayscale

def run_q5():
    input_path = "input_images/cat.jpeg"

    avg = rgb_to_grayscale(read_image(input_path), method='average')
    lum = rgb_to_grayscale(read_image(input_path), method='luminosity')
    light = rgb_to_grayscale(read_image(input_path), method='lightness')

    write_image(avg, "output_images/q5_grayscale_average.jpg")
    write_image(lum, "output_images/q5_grayscale_luminosity.jpg")
    write_image(light, "output_images/q5_grayscale_lightness.jpg")

    print("Saved all grayscale versions!")
