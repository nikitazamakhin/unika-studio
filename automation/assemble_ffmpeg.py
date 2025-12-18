import subprocess
import os
import sys

def assemble_with_ffmpeg():
    ffmpeg_exe = "/opt/anaconda3/bin/ffmpeg"
    if not os.path.exists(ffmpeg_exe):
        try:
            import imageio_ffmpeg
            ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        except:
             ffmpeg_exe = "ffmpeg"
    
    print(f"Using ffmpeg at: {ffmpeg_exe}")

    # Clips
    clips = [
        "reel2_clip_01_splash.mp4",
        "reel2_clip_03_luxury.mp4",
        "reel2_clip_02_lion.mp4"
    ]
    
    # Check existence
    valid_clips = []
    for c in clips:
        if os.path.exists(c):
            valid_clips.append(c)
        else:
            print(f"Missing file: {c}")
    
    if not valid_clips:
        print("No clips found.")
        return

    # Create a temporary list file for ffmpeg concat demuxer
    # Note: Concat demuxer requires same codecs/dimensions. Kling usually outputs same consistent format.
    # If dimensions differ (e.g. 16:9 vs 9:16), this fails.
    # We should use a complex filtergraph to be safe.
    
    # Detailed Filter:
    # 1. Scale/Crop each input to 1080x1920 (9:16)
    # 2. Concat
    
    # Construct input args
    input_args = []
    filter_parts = []
    
    for i, clip in enumerate(valid_clips):
        input_args.extend(["-i", clip])
        # Filter: scale to consistent height (1920), crop to width (1080)
        # Assuming input is landscape 1920x1080 or similar.
        # scale=-1:1920 -> height 1920, width auto (probably 3413 for 16:9 source)
        # crop=1080:1920 -> center crop
        filter_parts.append(f"[{i}:v]scale=-1:1920,crop=1080:1920,setsar=1[v{i}];")
    
    # Concat part
    concat_inputs = "".join([f"[v{i}]" for i in range(len(valid_clips))])
    concat_filter = f"{concat_inputs}concat=n={len(valid_clips)}:v=1:a=0[outv]"
    
    full_filter = "".join(filter_parts) + concat_filter
    
    output_file = "reel_2_trash_luxury_ffmpeg.mp4"
    
    cmd = [
        ffmpeg_exe,
        "-y", # Overwrite
    ] + input_args + [
        "-filter_complex", full_filter,
        "-map", "[outv]",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_file
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully created {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running ffmpeg: {e}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    assemble_with_ffmpeg()
