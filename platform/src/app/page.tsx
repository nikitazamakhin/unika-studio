"use client";

import { useState } from "react";
import ImageGenerator from "@/components/ImageGenerator";
import VideoAnimator from "@/components/VideoAnimator";

export default function Home() {
  const [generatedImage, setGeneratedImage] = useState<string | null>(null);

  return (
    <main className="min-h-screen bg-gray-950 text-gray-100 p-8">
      <header className="mb-12 border-b border-gray-800 pb-6 flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold bg-gradient-to-r from-yellow-400 to-yellow-600 bg-clip-text text-transparent">
            Unika/Platform
          </h1>
          <p className="text-gray-400 mt-2">Unified AI Production Studio</p>
        </div>
        <div className="text-xs font-mono text-gray-500">
          API Status: <span className="text-green-500">Connected</span>
        </div>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <section className="space-y-6">
          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6 h-full border-l-4 border-l-blue-500/50">
            <h2 className="text-2xl font-semibold mb-6 flex items-center gap-2 text-blue-400">
              <span>1️⃣</span> Generation
            </h2>
            <ImageGenerator onImageGenerated={setGeneratedImage} />
          </div>
        </section>

        <section className="space-y-6">
          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6 h-full border-l-4 border-l-purple-500/50">
            <h2 className="text-2xl font-semibold mb-6 flex items-center gap-2 text-purple-400">
              <span>2️⃣</span> Animation
            </h2>
            <VideoAnimator initialImage={generatedImage} />
          </div>
        </section>
      </div>
    </main>
  );
}
