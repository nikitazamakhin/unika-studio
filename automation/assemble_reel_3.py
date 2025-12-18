from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, ColorClip
import moviepy.video.fx.all as vfx
import os

def assemble_reel_3_hook():
    print("Assembling Reel 3 (Style Switch Hook)...")
    
    clips_files = [
        "reel3_clip_01_renaissance.mp4",
        "reel3_clip_02_anime.mp4",
        "reel3_clip_03_claymation.mp4"
    ]
    
    loaded_clips = []
    
    # Target: 3.3s per clip = 10s total (approx)
    
    for fname in clips_files:
        if os.path.exists(fname):
            clip = VideoFileClip(fname)
            # Resize/Crop to 9:16 Vertical
            
            w, h = clip.size
            target_ratio = 9/16
            
            if w/h > target_ratio:
                new_w = h * target_ratio
                clip = clip.crop(x1=(w/2 - new_w/2), y1=0, width=new_w, height=h)
            else:
                new_h = w / target_ratio
                clip = clip.crop(x1=0, y1=(h/2 - new_h/2), width=w, height=new_h)
            
            clip = clip.resize(newsize=(1080, 1920))
            
            # Trim to EXACTLY 3.33 seconds
            if clip.duration > 3.33:
                clip = clip.subclip(0, 3.33)
                
            loaded_clips.append(clip)
        else:
            print(f"Missing {fname}")

    if not loaded_clips:
        return

    final = concatenate_videoclips(loaded_clips, method="compose")
    
    print(f"Exporting reel_3_hook.mp4 ({final.duration}s)...")
    final.write_videofile("reel_3_hook.mp4", fps=30, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    assemble_reel_3_hook()
