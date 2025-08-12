from utils.image_utils import read_image, write_image

def run_q2():
    input_path = "input_images/cat.jpeg"
    output_path = "output_images/q2_written_image.jpg"

    img_array = read_image(input_path)
    write_image(img_array, output_path)

    print("Image successfully written to", output_path)
