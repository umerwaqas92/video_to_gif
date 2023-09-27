from moviepy.editor import VideoFileClip
import moviepy.editor as mp

# Input video file name
input_video_file = "202309271028.mp4"

# Output GIF file name
output_gif_file = "output.gif"

# Speed factor (2x speed)
speed_factor = 2

try:
    # Load the video clip
    video_clip = VideoFileClip(input_video_file)

    # Speed up the video by a factor of 2
    sped_up_clip = video_clip.speedx(factor=speed_factor)

    # Write the sped-up video as a GIF
    sped_up_clip.write_gif(output_gif_file, fps=10)  # Adjust the FPS as needed

    print(f"Video converted to GIF (2x speed): {output_gif_file}")
except Exception as e:
    print(f"Error converting video to GIF: {e}")
