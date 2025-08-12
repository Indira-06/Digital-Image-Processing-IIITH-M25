from utils.image_utils import read_image, save_pixel_array_to_txt

def run_q1():
    path = "input_images/cat.jpeg"
    img_array = read_image(path)

    print("Image shape:", img_array.shape)
    save_pixel_array_to_txt(img_array, "output_images/q1_output_pixels.txt")
