"use client";

import { useState, useEffect } from "react";
import { fal } from "@fal-ai/client";

// config is already global if configured in parent or another component, 
// but re-setting it here is safe.
fal.config({
    proxyUrl: "/api/fal/proxy",
});

export default function VideoAnimator({ initialImage }: { initialImage?: string | null }) {
    const [imageUrl, setImageUrl] = useState("");

    useEffect(() => {
        if (initialImage) setImageUrl(initialImage);
    }, [initialImage]);

    const [model, setModel] = useState("fal-ai/fast-svd");
    const [video, setVideo] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);
    const [logs, setLogs] = useState<string[]>([]);
    const [prompt, setPrompt] = useState("Dismounting motorcycle, adjusting skirt, slow motion");
    const [duration, setDuration] = useState("5"); // "5" or "10"

    const generate = async () => {
        if (!imageUrl) return;

        setLoading(true);
        setLogs((prev) => [...prev, `Starting animation with ${model} (${duration}s)...`]);
        try {
            let input: any = {
                image_url: imageUrl,
            };

            // Parameters differ by model
            if (model.includes("svd")) {
                input = {
                    ...input,
                    motion_bucket_id: 127,
                    cond_aug: 0.02
                };
            } else if (model.includes("kling")) {
                input = {
                    ...input,
                    prompt: prompt, // Kling needs prompt
                    duration: duration,
                    aspect_ratio: "9:16"
                };
            }

            const result: any = await fal.subscribe(model, {
                input,
                pollInterval: 2000, // slower poll for video
                logs: true,
            });

            const url = result.video?.url || result.url;
            setVideo(url);
            setLogs((prev) => [...prev, "✅ Animation complete!"]);
        } catch (error: any) {
            setLogs((prev) => [...prev, `❌ Error: ${error.message}`]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="space-y-4">
            <div className="flex flex-col gap-2">
                <label className="text-sm text-gray-400 font-medium">Model</label>
                <select
                    value={model}
                    onChange={(e) => setModel(e.target.value)}
                    className="bg-gray-800 border border-gray-700 rounded-lg p-3 text-white focus:ring-2 focus:ring-yellow-500 outline-none"
                >
                    <option value="fal-ai/fast-svd">Stable Video Diffusion (Fast & Cheap)</option>
                    <option value="fal-ai/kling-video/v1.6/pro/image-to-video">Kling 1.6 Pro (High Quality)</option>
                </select>
            </div>

            <div className="flex flex-col gap-2">
                <label className="text-sm text-gray-400 font-medium">Source Image URL</label>
                <div className="flex gap-2">
                    <input
                        type="text"
                        value={imageUrl}
                        onChange={(e) => setImageUrl(e.target.value)}
                        placeholder="https://..."
                        className="flex-1 bg-gray-800 border border-gray-700 rounded-lg p-3 text-white focus:ring-2 focus:ring-yellow-500 outline-none text-xs font-mono"
                    />
                    <button
                        onClick={async () => {
                            const text = await navigator.clipboard.readText();
                            setImageUrl(text);
                        }}
                        className="bg-gray-700 hover:bg-gray-600 px-3 rounded-lg text-sm"
                    >
                        Paste
                    </button>
                </div>
            </div>

            {model.includes("kling") && (
                <div className="space-y-4 animate-fade-in bg-gray-900/50 p-4 rounded-lg border border-gray-800">
                    <div className="flex flex-col gap-2">
                        <label className="text-sm text-gray-400 font-medium">Duration (Reels Mode)</label>
                        <div className="flex gap-4">
                            <label className="flex items-center gap-2 cursor-pointer">
                                <input type="radio" name="duration" value="5" checked={duration === "5"} onChange={(e) => setDuration(e.target.value)} />
                                <span>5 Seconds (Standard)</span>
                            </label>
                            <label className="flex items-center gap-2 cursor-pointer">
                                <input type="radio" name="duration" value="10" checked={duration === "10"} onChange={(e) => setDuration(e.target.value)} />
                                <span>10 Seconds (Pro)</span>
                            </label>
                        </div>
                    </div>

                    <div className="flex flex-col gap-2">
                        <label className="text-sm text-gray-400 font-medium">Motion Prompt</label>
                        <textarea
                            value={prompt}
                            onChange={(e) => setPrompt(e.target.value)}
                            rows={2}
                            className="bg-gray-800 border border-gray-700 rounded-lg p-3 text-white focus:ring-2 focus:ring-yellow-500 outline-none resize-none"
                        />
                    </div>
                </div>
            )}
            <button
                onClick={generate}
                disabled={loading || !imageUrl}
                className="w-full bg-yellow-500 hover:bg-yellow-400 text-black font-bold py-3 rounded-lg transition-colors flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
                {loading ? (
                    <>
                        <span className="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin"></span>
                        Animating... {model.includes("kling") && "(takes ~2-5m)"}
                    </>
                ) : (
                    "Generate Video"
                )}
            </button>

            {/* Logs Area */}
            {logs.length > 0 && (
                <div className="bg-black/50 rounded-lg p-3 max-h-32 overflow-y-auto text-xs font-mono text-gray-500">
                    {logs.map((log, i) => (
                        <div key={i}>{log}</div>
                    ))}
                </div>
            )}

            {/* Preview Area */}
            {video && (
                <div className="mt-6 rounded-xl overflow-hidden border border-gray-700 bg-black">
                    <video src={video} controls className="w-full" autoPlay loop />
                    <div className="p-4 flex justify-center">
                        <a href={video} download className="text-sm text-yellow-500 hover:text-yellow-400 underline">Download Video</a>
                    </div>
                </div>
            )}
        </div>
    );
}
