import { Content } from '@/data/content';

export default function Portfolio({ content }: { content: Content['portfolio'] }) {
    return (
        <section id="portfolio" className="py-24 bg-black text-foreground">
            <div className="max-w-7xl mx-auto px-6">
                <div className="mb-16">
                    <h2 className="text-primary text-sm tracking-[0.2em] uppercase font-bold mb-4">{content.label}</h2>
                    <h3 className="text-3xl md:text-5xl font-bold">{content.title}</h3>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                    {content.cases.map((item) => (
                        <div key={item.id} className="group relative aspect-video rounded-xl overflow-hidden cursor-pointer">
                            {/* Fallback Gradient / Placeholder Image */}
                            <div className={`absolute inset-0 bg-gradient-to-br ${item.color} opacity-20 group-hover:opacity-30 transition-all duration-500`} />

                            <div className="absolute inset-0 flex flex-col justify-end p-8 bg-gradient-to-t from-black via-transparent to-transparent">
                                <div className="transform translate-y-4 group-hover:translate-y-0 transition-transform duration-300">
                                    <p className="text-xs font-bold text-primary uppercase tracking-wider mb-2">{item.type}</p>
                                    <h4 className="text-2xl font-bold text-white mb-2">{item.client}</h4>
                                    <p className="text-gray-300 text-sm opacity-0 group-hover:opacity-100 transition-opacity duration-300 delay-100">
                                        {item.description}
                                    </p>
                                </div>
                            </div>

                            {/* Play Button Overlay */}
                            <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                                <div className="w-16 h-16 rounded-full bg-white/10 backdrop-blur-sm flex items-center justify-center border border-white/20">
                                    <svg className="w-6 h-6 text-white ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" /></svg>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
