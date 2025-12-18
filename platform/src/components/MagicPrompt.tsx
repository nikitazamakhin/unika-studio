"use client";

import { useState } from "react";
import { fal } from "@fal-ai/client";

export default function MagicPrompt({ onPromptGenerated }: { onPromptGenerated: (prompt: string) => void }) {
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);

    const enhancePrompt = async () => {
        if (!input) return;
        setLoading(true);
        try {
            // Use a simple LLM model via Fal (e.g. Llama 3 or similar if available/mapped, or just mock it if we don't have a direct LLM endpoint handy?)
            // Actually Fal has LLM endpoints. "fal-ai/any-llm" or "fal-ai/clarity-upscaler" (not exactly).
            // Let's use OpenAI directly if we have the key, BUT client-side exposure is risky.
            // Better: Create a server action or API route.
            // For now, let's use a Fal text-to-text model if one exists.
            // Search results didn't explicitly list LLMs on Fal. 
            // User has OPENAI_KEY in .env. Let's use a server API route for safety.

            const res = await fetch("/api/magic-prompt", {
                method: "POST",
                body: JSON.stringify({ prompt: input }),
            });
            const data = await res.json();
            if (data.prompt) {
                onPromptGenerated(data.prompt);
            }
        } catch (e) {
            console.error(e);
            alert("Failed to enhance prompt");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-gray-800 p-4 rounded-xl border border-gray-700 mb-6">
            <h3 className="text-yellow-500 font-bold mb-2 text-sm flex items-center gap-2">
                ✨ Magic Prompt (Neuronet Idea Generator)
            </h3>
            <div className="flex gap-2">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="E.g. 'Cyberpunk girl on bike'..."
                    className="flex-1 bg-gray-900 border border-gray-600 rounded-lg px-3 py-2 text-white text-sm focus:ring-1 focus:ring-yellow-500 outline-none"
                    onKeyDown={(e) => e.key === "Enter" && enhancePrompt()}
                />
                <button
                    onClick={enhancePrompt}
                    disabled={loading}
                    className="bg-yellow-500/10 text-yellow-500 hover:bg-yellow-500/20 px-4 py-2 rounded-lg text-sm font-bold transition-colors disabled:opacity-50"
                >
                    {loading ? "Thinking..." : "Enhance"}
                </button>
            </div>
        </div>
    );
}
