from utils.image_utils import read_image, write_image, change_brightness

def run_q3():
    input_path = "input_images/cat.jpeg"
    output_brighter = "output_images/q3_brighter.jpg"
    output_darker = "output_images/q3_darker.jpg"

    img = read_image(input_path)

    brighter = change_brightness(img, 50)  #increase brightness
    darker = change_brightness(img, -50)   #decrease brightness

    write_image(brighter, output_brighter)
    write_image(darker, output_darker)

    print("Saved bright and dark versions!")
