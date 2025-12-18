import { NextResponse } from "next/server";
import OpenAI from "openai";

export async function POST(req: Request) {
    try {
        const { prompt } = await req.json();
        const apiKey = process.env.OPENAI_API_KEY;

        if (!apiKey) {
            return NextResponse.json({ error: "No OpenAI Key" }, { status: 500 });
        }

        const openai = new OpenAI({ apiKey });
        const completion = await openai.chat.completions.create({
            model: "gpt-4o-mini", // Cost effective
            messages: [
                {
                    role: "system",
                    content: "You are an expert AI art director. Your task is to take a simple idea and convert it into a highly detailed, photorealistic image generation prompt optimized for Flux/Imagen 3. Include details about lighting, camera angle, texture, diversity, and style. Keep it under 50 words. Output ONLY the raw prompt."
                },
                {
                    role: "user",
                    content: prompt
                }
            ],
            temperature: 0.7,
        });

        const enhancedPrompt = completion.choices[0].message.content;

        return NextResponse.json({ prompt: enhancedPrompt });
    } catch (error) {
        return NextResponse.json({ error: "Failed to generate" }, { status: 500 });
    }
}
