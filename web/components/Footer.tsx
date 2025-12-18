import { Content } from "@/data/content";

export default function Footer({ content }: { content: Content["footer"] }) {
    return (
        <footer className="bg-black text-white pt-24 pb-12 border-t border-white/10">
            <div className="container mx-auto px-6">
                {/* Main CTA Section */}
                <div className="flex flex-col md:flex-row justify-between items-start mb-24 gap-12">
                    <div className="max-w-2xl">
                        <h2 className="text-6xl md:text-8xl font-bold tracking-tighter leading-[0.9] mb-8 bg-gradient-to-br from-white to-gray-500 bg-clip-text text-transparent">
                            {content.title}
                        </h2>
                    </div>
                    <div className="flex flex-col items-start gap-6">
                        <button className="px-10 py-5 bg-primary text-black text-xl font-bold tracking-widest hover:bg-white hover:scale-105 transition-all duration-300 rounded-full">
                            {content.cta}
                        </button>
                        <a href={`mailto:${content.email}`} className="text-xl text-gray-400 hover:text-white transition-colors">
                            {content.email}
                        </a>
                    </div>
                </div>

                {/* Links Grid */}
                <div className="grid grid-cols-1 md:grid-cols-4 gap-12 border-t border-white/10 pt-12 text-sm text-gray-400">

                    {/* Address */}
                    <div className="space-y-4">
                        <h3 className="text-white font-bold uppercase tracking-widest">Office</h3>
                        <p>{content.address}</p>
                    </div>

                    {/* Socials */}
                    <div className="space-y-4">
                        <h3 className="text-white font-bold uppercase tracking-widest">Socials</h3>
                        <ul className="space-y-2">
                            {content.socials.map((social, idx) => (
                                <li key={idx}>
                                    <a href={social.link} className="hover:text-primary transition-colors flex items-center gap-2 group">
                                        {social.label}
                                        <span className="opacity-0 group-hover:opacity-100 transition-opacity">↗</span>
                                    </a>
                                </li>
                            ))}
                        </ul>
                    </div>

                    {/* Sitemap */}
                    <div className="space-y-4">
                        <h3 className="text-white font-bold uppercase tracking-widest">Menu</h3>
                        <ul className="space-y-2">
                            {content.links.map((link, idx) => (
                                <li key={idx}>
                                    <a href={link.link} className="hover:text-white transition-colors">
                                        {link.label}
                                    </a>
                                </li>
                            ))}
                        </ul>
                    </div>

                    {/* Copyright */}
                    <div className="md:text-right flex flex-col justify-end">
                        <p>{content.copyright}</p>
                    </div>
                </div>
            </div>
        </footer>
    );
}
