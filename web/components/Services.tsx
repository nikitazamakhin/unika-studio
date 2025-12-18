import { Content } from '@/data/content';

export default function Services({ content }: { content: Content['services'] }) {
    return (
        <section className="py-24 bg-surface text-foreground relative overflow-hidden">
            <div className="max-w-7xl mx-auto px-6">
                <div className="mb-16 text-center space-y-4">
                    <h2 className="text-primary text-sm tracking-[0.2em] uppercase font-bold">{content.label}</h2>
                    <h3 className="text-3xl md:text-5xl font-bold">{content.title}</h3>
                    <p className="text-gray-400 max-w-2xl mx-auto">
                        {content.desc}
                    </p>
                </div>

                <div className="grid md:grid-cols-2 gap-8">
                    {/* Card 1: Commercial */}
                    <div id="commercial" className="group relative p-1 rounded-2xl bg-gradient-to-b from-gray-800 to-transparent hover:from-primary hover:to-primary/20 transition-all duration-500">
                        <div className="relative h-full bg-background rounded-xl p-8 md:p-12 border border-gray-800 flex flex-col items-start overflow-hidden">
                            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                                <svg className="w-32 h-32" fill="currentColor" viewBox="0 0 24 24"><path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h18v14zM8 15c0-1.66 1.34-3 3-3 .35 0 .69.07 1 .18V6h5v2h-3v7.03c-.02 1.64-1.35 2.97-3 2.97-1.66 0-3-1.34-3-3z" /></svg>
                            </div>

                            <h4 className="text-2xl font-bold mb-4 group-hover:text-primary transition-colors">{content.commercial.title}</h4>
                            <p className="text-gray-400 mb-8 flex-grow">
                                {content.commercial.desc}
                            </p>

                            <ul className="space-y-3 mb-8 text-sm text-gray-300">
                                {content.commercial.features.map((feature, i) => (
                                    <li key={i} className="flex items-center"><span className="w-1.5 h-1.5 bg-primary rounded-full mr-3" />{feature}</li>
                                ))}
                            </ul>

                            <button className="w-full py-4 border border-gray-700 rounded-lg group-hover:bg-primary group-hover:text-black group-hover:border-primary transition-all font-semibold">
                                {content.commercial.cta}
                            </button>
                        </div>
                    </div>

                    {/* Card 2: AI SMM */}
                    <div id="viral" className="group relative p-1 rounded-2xl bg-gradient-to-b from-gray-800 to-transparent hover:from-purple-500 hover:to-purple-900/20 transition-all duration-500">
                        {/* Note: Overriding hover color for distinction, or keep primary? Let's use Primary for brand consistency, or maybe a secondary 'Viral' color. Sticking to Primary for now for cohesive premium look, maybe vary slightly. */}
                        <div className="relative h-full bg-background rounded-xl p-8 md:p-12 border border-gray-800 flex flex-col items-start overflow-hidden">
                            <div className="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                                <svg className="w-32 h-32" fill="currentColor" viewBox="0 0 24 24"><path d="M17 10.5V7c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-3.5l4 4v-11l-4 4zM14 13h-3v3H9v-3H6v-2h3V8h2v3h3v2z" /></svg>
                            </div>

                            <h4 className="text-2xl font-bold mb-4 group-hover:text-primary transition-colors">{content.viral.title}</h4>
                            <p className="text-gray-400 mb-8 flex-grow">
                                {content.viral.desc}
                            </p>

                            <ul className="space-y-3 mb-8 text-sm text-gray-300">
                                {content.viral.features.map((feature, i) => (
                                    <li key={i} className="flex items-center"><span className="w-1.5 h-1.5 bg-primary rounded-full mr-3" />{feature}</li>
                                ))}
                            </ul>

                            <button className="w-full py-4 border border-gray-700 rounded-lg group-hover:bg-white group-hover:text-black group-hover:border-white transition-all font-semibold">
                                {content.viral.cta}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
