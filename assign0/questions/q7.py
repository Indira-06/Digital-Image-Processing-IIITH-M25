from utils.image_utils import read_image, write_image, replace_green_screen

def run_q7():
    fg_path = "input_images/foreground.png"
    bg_path = "input_images/background.jpg"

    fg = read_image(fg_path)
    bg = read_image(bg_path)

    output = replace_green_screen(fg, bg)
    write_image(output, "output_images/q7_minions_in_the_sky.jpg")

    print("Green screen replaced and saved!")
