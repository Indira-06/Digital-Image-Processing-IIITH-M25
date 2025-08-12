from utils.image_utils import extract_frames_from_video, frames_to_video

def run_q8():
    video_path = "videos/sample_video.mp4"
    frame_folder = "output_images/q8_frames"
    output_video = "videos/q8_output_video.mp4"

    num_frames = extract_frames_from_video(video_path, frame_folder)
    print(f"Extracted {num_frames} frames.")

    frames_to_video(frame_folder, output_video)
    print(f"Reconstructed video saved to {output_video}")
