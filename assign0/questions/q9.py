from utils.image_utils import read_image, create_fade_transition
import imageio
import numpy as np
from PIL import Image

def run_q9():
    img1 = read_image("input_images/transition_start.jpg")
    img2 = read_image("input_images/transition_end.jpg")

    # Resize img2 to match img1 if needed
    if img1.shape != img2.shape:
        
        img2 = Image.fromarray(img2).resize((img1.shape[1], img1.shape[0]))
        img2 = np.array(img2)

    frames = create_fade_transition(img1, img2, num_frames=72) #3 sec at 24fps
    output_path = "videos/q9_transition_video.mp4"
    writer = imageio.get_writer(output_path, fps=24)

    for frame in frames:
        writer.append_data(frame)
    writer.close()

    print(f"Transition video saved to {output_path}")
