from PIL import Image
import numpy as np
import imageio
import os

#to read an image and return it as a numpy array.
#this supports grayscale and rgb too.
#q1
def read_image(path):
    img = Image.open(path)
    img_array = np.array(img)
    return img_array

#to save the pixel values of an image array in a .txt file.
def save_pixel_array_to_txt(array, output_path):
    with open(output_path, 'w') as f:
        if len(array.shape) == 2:
            #grayscale
            for row in array:
                f.write(' '.join(str(val) for val in row) + '\n')
        elif len(array.shape) == 3:
            #color
            for row in array:
                row_str = ' '.join(' '.join(str(channel) for channel in pixel) for pixel in row)
                f.write(row_str + '\n')
        else:
            raise ValueError("Unsupported array shape")

# to write a numpy array into an image file
#again, supports grayscale(2D) and RGB color(3D) images too.
#q2
def write_image(array, output_path):
    if len(array.shape) == 2:
        mode = 'L'  #grayscale
    elif len(array.shape) == 3 and array.shape[2] == 3:
        mode = 'RGB'
    else:
        raise ValueError("Unsupported image array shape")

    img = Image.fromarray(np.uint8(array), mode=mode)
    img.save(output_path)

#to adjust brightness of image
#'value' if positive, we get a brighter imager. 
#if the 'value' is negative we get darker image
#q3
def change_brightness(img_array, value):
    #casting to int16 to avoid overflow/underflow cases
    img_int = img_array.astype(np.int16)
    #adding value, then clip to valid range
    brightened = np.clip(img_int + value, 0, 255)
    return brightened.astype(np.uint8)

#adjusting the contrast of image
#multiplying around a midpoint
#if faxtor>1 then more contrast, if 0<factor<1 then less contrast
#q4
def change_contrast(img_array, factor):
    img_float = img_array.astype(np.float32)
    contrasted = (img_float - 128) * factor + 128
    return np.clip(contrasted, 0, 255).astype(np.uint8)

#converts an RGB image to a grayscale image with different methods found on google
#default is luminosity method which is more accurate to human vision and looks more natural (due to its weighing of green)
#methods = 'average', 'luminosity', or 'lightness'
#Average: Equal weight to all channels. Simple but flat-looking.
#Luminosity: Weighted for human perception (green-heavy). Looks more balanced and realistic.
#Lightness: Based on max and min. Gives a contrasty, stylized feel.
#q5
def rgb_to_grayscale(img_array, method='luminosity'):
    if len(img_array.shape) != 3 or img_array.shape[2] != 3:
        raise ValueError("Input must be a color (RGB) image")

    img = img_array.astype(np.float32)
    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

    if method == 'average':
        gray = (R + G + B) / 3
    elif method == 'luminosity':
        gray = 0.299 * R + 0.587 * G + 0.114 * B
    elif method == 'lightness':
        gray = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
    else:
        raise ValueError("Unknown grayscale method")

    return gray.astype(np.uint8)

#converts a grayscale image to a pseudocolor using a basic colormap
#output is hopefully an RGB image 
#q6
def grayscale_to_pseudocolor(gray_img):
    if len(gray_img.shape) != 2:
        raise ValueError("Input must be a grayscale image")

    height, width = gray_img.shape
    pseudocolor = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            val = gray_img[i, j]
            if val < 128:
                #map 0 - 127: Blue to Red
                ratio = val / 128
                r = int(255 * ratio)
                g = 0
                b = int(255 * (1 - ratio))
            else:
                #map 128-255: Red to Yellow
                ratio = (val - 128) / 127
                r = 255
                g = int(255 * ratio)
                b = 0
            pseudocolor[i, j] = [r, g, b]

    return pseudocolor

#replacing green pixels in foreground with background pixels
#q7
def replace_green_screen(fg_img, bg_img, threshold=1.3):
    #removing alpha channel if present
    #alpha channel 
    if fg_img.shape[2] == 4:
        fg_img = fg_img[:, :, :3]
    if bg_img.shape[2] == 4:
        bg_img = bg_img[:, :, :3]
    
    if fg_img.shape != bg_img.shape:
        bg_img = Image.fromarray(bg_img)
        bg_img = bg_img.resize((fg_img.shape[1], fg_img.shape[0]))  #resizing to match (W, H)
        bg_img = np.array(bg_img)

        #print(fg_img.shape)
        #print(bg_img.shape)
        #raise ValueError("Foreground and background must be same shape")

    result = fg_img.copy()

    #extracting RGB channels
    r, g, b = fg_img[:,:,0], fg_img[:,:,1], fg_img[:,:,2]

    #creating a green mask
    green_mask = (g > r * threshold) & (g > b * threshold)

    #appling mask - replace green pixels with background
    result[green_mask] = bg_img[green_mask]

    return result

#q8
#reading a video file and save each frame as an image into an output_folder
def extract_frames_from_video(video_path, output_folder):
    reader = imageio.get_reader(video_path)
    os.makedirs(output_folder, exist_ok=True)

    for i, frame in enumerate(reader):
        frame_path = os.path.join(output_folder, f"frame_{i:03d}.jpg")
        imageio.imwrite(frame_path, frame)

    return i + 1  #total number of frames
#reading all frames in input folder and then writing them into a video
#assuming all the frames are names in order like frame_000.jpg,etc.
def frames_to_video(input_folder, output_video_path, fps=24):
    writer = imageio.get_writer(output_video_path, fps=fps)

    frame_files = sorted(
        [f for f in os.listdir(input_folder) if f.endswith('.jpg')]
    )

    for filename in frame_files:
        frame = imageio.imread(os.path.join(input_folder, filename))
        writer.append_data(frame)

    writer.close()

#q9
#creates a list of frames fading from img1 to img2
def create_fade_transition(img1, img2, num_frames=24):
    if img1.shape != img2.shape:
        img2 = Image.fromarray(img2)
        img2 = img2.resize((img1.shape[1], img1.shape[0]))
        img2 = np.array(img2)
    #if img1.shape != img2.shape:
    #    raise ValueError("Images must be the same shape for transition")

    img1 = img1.astype(np.float32)
    img2 = img2.astype(np.float32)
    frames = []

    for i in range(num_frames):
        alpha = i / (num_frames - 1)
        blended = (1 - alpha) * img1 + alpha * img2
        frames.append(blended.astype(np.uint8))

    return frames


