"use client";

import { useRef, useState } from "react";

interface VideoSectionProps {
    videoUrl: string;
    posterUrl?: string; // Image to show while loading
    title: string;
    subtitle: string;
    overlayColor?: string; // e.g., "bg-black/50"
}

export default function VideoSection({ videoUrl, posterUrl, title, subtitle, overlayColor = "bg-black/40" }: VideoSectionProps) {
    const videoRef = useRef<HTMLVideoElement>(null);
    const [isMuted, setIsMuted] = useState(true);

    const toggleMute = () => {
        if (videoRef.current) {
            videoRef.current.muted = !isMuted;
            setIsMuted(!isMuted);
        }
    };

    return (
        <section className="relative w-full h-[80vh] min-h-[600px] overflow-hidden bg-black flex items-center justify-center">
            {/* Video Background */}
            <video
                ref={videoRef}
                className="absolute inset-0 w-full h-full object-cover opacity-80"
                src={videoUrl}
                poster={posterUrl}
                autoPlay
                loop
                muted={isMuted}
                playsInline
            />

            {/* Overlay Gradient */}
            <div className={`absolute inset-0 ${overlayColor} backdrop-blur-[2px]`} />
            <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-black opacity-80" />

            {/* Content */}
            <div className="relative z-10 text-center max-w-4xl px-6 animate-fade-in-up">
                <h2 className="text-sm font-bold tracking-[0.3em] text-primary uppercase mb-6 drop-shadow-lg">
                    {subtitle}
                </h2>
                <h3 className="text-4xl md:text-7xl font-bold text-white mb-8 tracking-tight drop-shadow-xl">
                    {title}
                </h3>
            </div>

            {/* Sound Control UI */}
            <button
                onClick={toggleMute}
                className="absolute bottom-8 right-8 z-20 w-12 h-12 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center hover:bg-white/20 transition-all text-white"
            >
                {isMuted ? (
                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" /><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2" /></svg>
                ) : (
                    <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" /></svg>
                )}
            </button>
        </section>
    );
}
