from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, ColorClip
import moviepy.video.fx.all as vfx

def assemble_reel():
    print("Starting Reel Assembly...")
    
    clips_files = [
        "v2_clip_01_mountain.mp4",
        "v2_clip_02_ocean.mp4",
        "v2_clip_03_safari.mp4",
        "v2_clip_04_nyc.mp4",
        "v2_clip_05_smoke.mp4"
    ]
    
    processed_clips = []
    
    # Text/Intro settings
    w, h = 1080, 1920 # 9:16 aspect ratio (target)
    # Actually Kling Standard gives 16:9 usually (landscape). We need to verify input.
    # If input is 16:9, and we want Reel (9:16), we must crop.
    # My prompts were for "cinematic" which usually implies wide. The images were generated as "portrait_16_9" in FLUX (which is 9:16).
    # Wait, Flux "portrait_16_9" is 9:16 vertical? Yes usually.
    # Check `generate_reel_1_v2.py`: "image_size": "portrait_16_9" -> This produces 9:16 images vertical.
    # Kling script `animate_reel_1_v2.py`: "aspect_ratio": "16:9". 
    # Mismatch risk! Kling might force 16:9 landscape if I asked for it.
    # I should have asked for "9:16" in Kling for viral reels.
    # Let's assess the damage later. If they come out 16:9, I will center crop them to 9:16 in assembly.
    
    for filename in clips_files:
        if not os.path.exists(filename):
            print(f"File not found: {filename}")
            continue
            
        print(f"Processing {filename}...")
        clip = VideoFileClip(filename)
        
        # 1. Slow Motion (0.5x speed -> 2x duration)
        # We use speedx=0.5. Note: smooth motion requires interpolation which MoviePy doesn't do natively well without ffmpeg flags.
        # But simply slowing down plays frames slower. 30fps -> 15fps visual.
        # To keep it smooth, ideally we'd use 'minterpolate'. MoviePy isn't great at calling filters for this.
        # Simple slow mo for now:
        clip_slow = clip.fx(vfx.speedx, 0.5)
        
        # 2. Resize/Crop to 9:16 Vertical if needed.
        # Target: 1080x1920
        # If clip is landscape (e.g. 1920x1080), we crop the center.
        if clip.w > clip.h:
            clip_slow = clip_slow.crop(width=clip_slow.h * (9/16), height=clip_slow.h, x_center=clip_slow.w/2, y_center=clip_slow.h/2)
            clip_slow = clip_slow.resize(height=1920)
        else:
            # Assumed vertical or close. Resize to fit height/width.
            # Best: resize to cover.
            ratio = 9/16
            current_ratio = clip.w / clip.h
            if current_ratio > ratio:
                 # too wide, crop width
                 new_w = clip.h * ratio
                 clip_slow = clip_slow.crop(width=new_w, height=clip.h, x_center=clip.w/2, y_center=clip.h/2)
            else:
                 # too tall (rare), crop height
                 new_h = clip.w / ratio
                 clip_slow = clip_slow.crop(width=clip.w, height=new_h, x_center=clip.w/2, y_center=clip.h/2)
            
            clip_slow = clip_slow.resize(newsize=(1080, 1920))

        processed_clips.append(clip_slow)

    if not processed_clips:
        print("No clips loaded.")
        return

    # 3. Concatenate with Crossfade
    # MoviePy's concatenate_videoclips with `method='compose'` handles fades if applied.
    # Adding padding for transition.
    final_clips = []
    for i, clip in enumerate(processed_clips):
        # Add fade in/out
        # Simple concat for now to ensure stability, or dissolve.
        # Dissolve is complex in simple concat lists.
        # We will just append them.
        final_clips.append(clip)

    final_video = concatenate_videoclips(final_clips, method="compose")
    
    # 4. Intro Card
    # Simple black screen with text "THE JOURNEY"
    # To keep it simple, we skip complex text for now or verify ImageMagick is installed for TextClip.
    # Assuming no ImageMagick:
    # Use ColorClip as base.
    
    print(f"Writing output to reel_1_final.mp4 (Duration: {final_video.duration}s)...")
    final_video.write_videofile("reel_1_final.mp4", fps=30, codec="libx264", audio_codec="aac")
    print("Done!")

if __name__ == "__main__":
    assemble_reel()
