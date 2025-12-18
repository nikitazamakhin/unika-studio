from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, ColorClip
import moviepy.video.fx.all as vfx
import os

def assemble_reel_2():
    print("Assembling Reel 2 (Renovation Drink)...")
    
    clips_files = [
        "reel2_clip_01_splash.mp4",
        "reel2_clip_03_luxury.mp4", # Glitch to luxury immediately
        "reel2_clip_02_lion.mp4" # Lion staring
    ]
    
    loaded_clips = []
    
    for fname in clips_files:
        if os.path.exists(fname):
            clip = VideoFileClip(fname)
            # Resize/Crop to 9:16 Vertical
            # Input Kling is likely 16:9 Landscape (1920x1080) or similar.
            # We want 1080x1920. CENTER CROP.
            
            w, h = clip.size
            target_ratio = 9/16
            
            if w/h > target_ratio:
                # Too wide
                new_w = h * target_ratio
                clip = clip.crop(x1=(w/2 - new_w/2), y1=0, width=new_w, height=h)
            else:
                # Too tall
                new_h = w / target_ratio
                clip = clip.crop(x1=0, y1=(h/2 - new_h/2), width=w, height=new_h)
            
            clip = clip.resize(newsize=(1080, 1920))
            loaded_clips.append(clip)
        else:
            print(f"Missing {fname}")

    if not loaded_clips:
        return

    # Trim clips for pacing
    # 1. Splash: 0s to 3s (Action)
    clip1 = loaded_clips[0].subclip(0, 3)
    
    # 2. Luxury: 0s to 3s
    clip2 = loaded_clips[1].subclip(0, 3) 
    
    # 3. Lion: 0s to 4s
    clip3 = loaded_clips[2].subclip(0, 4)
    
    final = concatenate_videoclips([clip1, clip2, clip3], method="compose")
    
    print(f"Exporting reel_2_trash_luxury.mp4 ({final.duration}s)...")
    final.write_videofile("reel_2_trash_luxury.mp4", fps=30, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    assemble_reel_2()
