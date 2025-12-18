import { Content } from '@/data/content';

export default function Hero({ content }: { content: Content['hero'] }) {
    return (
        <section className="relative h-screen flex flex-col items-center justify-center overflow-hidden">
            {/* Background Gradient Blob */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-primary opacity-20 blur-[120px] rounded-full pointer-events-none" />

            <div className="z-10 text-center px-4 max-w-4xl mx-auto space-y-8">
                <h2 className="text-primary text-sm md:text-base tracking-[0.3em] uppercase opacity-0 animate-[fade-in_1s_ease-out_forwards]">
                    {content.label}
                </h2>

                <h1 className="text-5xl md:text-7xl font-bold tracking-tighter opacity-0 animate-[slide-up_1s_ease-out_0.3s_forwards]">
                    <span className="block text-white">{content.title_1}</span>
                    <span className="text-gradient">{content.title_2}</span>
                </h1>

                <p className="text-gray-400 text-lg md:text-xl max-w-2xl mx-auto opacity-0 animate-[slide-up_1s_ease-out_0.6s_forwards]">
                    {content.desc}
                </p>

                <div className="flex flex-col md:flex-row gap-6 justify-center pt-8 opacity-0 animate-[slide-up_1s_ease-out_0.9s_forwards]">
                    <a href="#commercial" className="group relative px-8 py-3 bg-surface border border-gray-800 hover:border-primary transition-colors duration-300">
                        <span className="text-white font-medium group-hover:text-primary transition-colors">{content.cta_commercial}</span>
                        <div className="absolute inset-0 bg-primary opacity-0 group-hover:opacity-5 transition-opacity duration-300" />
                    </a>

                    <a href="#viral" className="group relative px-8 py-3 bg-primary text-black font-semibold hover:bg-white transition-colors duration-300">
                        {content.cta_viral}
                    </a>
                </div>
            </div>
        </section>
    );
}
