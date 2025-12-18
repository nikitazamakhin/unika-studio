import { Content } from '@/data/content';

export default function Process({ content }: { content: Content['process'] }) {
    return (
        <section className="py-24 bg-surface relative overflow-hidden">
            {/* Background Line */}
            <div className="absolute left-[50%] top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-primary/20 to-transparent hidden md:block" />

            <div className="max-w-6xl mx-auto px-6 relative z-10">
                <div className="text-center mb-20 space-y-4">
                    <h2 className="text-primary text-sm tracking-[0.2em] uppercase font-bold">{content.label}</h2>
                    <h3 className="text-3xl md:text-5xl font-bold text-white">{content.title}</h3>
                </div>

                <div className="space-y-12 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-24 md:gap-y-12">
                    {content.steps.map((step, idx) => (
                        <div key={idx} className={`relative flex gap-6 ${idx % 2 === 0 ? 'md:text-right md:flex-row-reverse' : 'md:text-left'} group`}>

                            {/* Number Bubble (Center for desktop) */}
                            <div className={`hidden md:flex absolute top-0 ${idx % 2 === 0 ? '-right-[60px]' : '-left-[60px]'} w-8 h-8 rounded-full bg-surface border border-primary/50 items-center justify-center text-xs text-primary font-bold z-20 group-hover:bg-primary group-hover:text-black transition-colors duration-300`}>
                                {step.num}
                            </div>

                            {/* Mobile Number */}
                            <div className="md:hidden text-primary font-bold text-xl">{step.num}</div>

                            <div>
                                <h4 className="text-xl font-bold text-white mb-2 group-hover:text-primary transition-colors">{step.title}</h4>
                                <p className="text-gray-400 text-sm leading-relaxed">{step.desc}</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
