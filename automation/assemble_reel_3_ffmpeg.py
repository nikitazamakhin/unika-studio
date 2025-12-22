import subprocess
import os
import sys

def assemble_reel_3_ffmpeg():
    print("Locating ffmpeg for Reel 3...")
    
    # Try to find ffmpeg
    ffmpeg_exe = "ffmpeg"
    try:
        import imageio_ffmpeg
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    except:
        pass
        
    print(f"Using ffmpeg at: {ffmpeg_exe}")

    clips = [
        "reel3_clip_01_renaissance.mp4",
        "reel3_clip_02_anime.mp4",
        "reel3_clip_03_claymation.mp4"
    ]
    
    valid_clips = []
    for c in clips:
        if os.path.exists(c):
            valid_clips.append(c)
        else:
            print(f"Missing file: {c}")
    
    if not valid_clips:
        print("No clips found.")
        return

    # Filter Strategy:
    # 1. Trim to 3.33s
    # 2. Scale/Crop to 1080x1920
    # 3. Reset PTS
    
    input_args = []
    filter_parts = []
    
    for i, clip in enumerate(valid_clips):
        input_args.extend(["-i", clip])
        # [i:v] -> trim=duration=3.33 -> setpts=PTS-STARTPTS -> scale=-1:1920 -> crop=1080:1920 -> setsar=1 [vi]
        # We use 'trim=0:3.33' which implies start at 0, end at 3.33 (duration).
        filter_parts.append(f"[{i}:v]trim=duration=3.33,setpts=PTS-STARTPTS,scale=-1:1920,crop=1080:1920,setsar=1[v{i}];")
    
    concat_inputs = "".join([f"[v{i}]" for i in range(len(valid_clips))])
    concat_filter = f"{concat_inputs}concat=n={len(valid_clips)}:v=1:a=0[outv]"
    
    full_filter = "".join(filter_parts) + concat_filter
    
    output_file = "reel_3_hook_ffmpeg.mp4"
    
    cmd = [
        ffmpeg_exe,
        "-y", 
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

if __name__ == "__main__":
    assemble_reel_3_ffmpeg()
