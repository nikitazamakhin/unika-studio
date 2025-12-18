"use client";

import { useState } from 'react';
import Link from 'next/link';
import { Content } from '@/data/content';

export default function Navbar({ content }: { content: Content['navbar'] }) {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="fixed top-0 w-full z-50 transition-all duration-300 glass border-b border-white/5 bg-black/50 backdrop-blur-md">
            <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
                <Link href={content.toggleLink === "/" ? "/ru" : "/"} className="text-xl font-bold tracking-widest text-white relative z-50">
                    UNIKA <span className="text-primary">STUDIO</span>
                </Link>

                {/* Desktop Menu */}
                <div className="hidden md:flex gap-8 items-center">
                    <Link href="#commercial" className="text-sm font-medium text-gray-300 hover:text-white transition-colors">
                        {content.commercial}
                    </Link>
                    <Link href="#viral" className="text-sm font-medium text-gray-300 hover:text-white transition-colors">
                        {content.viral}
                    </Link>
                    <button className="px-6 py-2 border border-primary text-primary hover:bg-primary hover:text-black transition-all duration-300 text-sm font-semibold tracking-wide">
                        {content.start}
                    </button>

                    <Link href={content.toggleLink} className="ml-4 text-xs font-bold text-gray-500 hover:text-white transition-colors border border-gray-700 rounded px-2 py-1">
                        {content.toggleText}
                    </Link>
                </div>

                {/* Mobile Hamburger */}
                <button
                    className="md:hidden text-white z-50 focus:outline-none"
                    onClick={() => setIsOpen(!isOpen)}
                >
                    {isOpen ? (
                        <span className="text-2xl">✕</span>
                    ) : (
                        <span className="text-2xl">☰</span>
                    )}
                </button>

                {/* Mobile Menu Overlay */}
                {isOpen && (
                    <div className="fixed inset-0 bg-black/95 backdrop-blur-xl z-40 flex flex-col items-center justify-center space-y-8 animate-fade-in">
                        <Link
                            href="#commercial"
                            className="text-2xl font-bold text-white hover:text-primary transition-colors"
                            onClick={() => setIsOpen(false)}
                        >
                            {content.commercial}
                        </Link>
                        <Link
                            href="#viral"
                            className="text-2xl font-bold text-white hover:text-primary transition-colors"
                            onClick={() => setIsOpen(false)}
                        >
                            {content.viral}
                        </Link>
                        <button className="px-8 py-3 bg-primary text-black text-lg font-bold tracking-widest rounded-full">
                            {content.start}
                        </button>
                        <Link
                            href={content.toggleLink}
                            className="mt-8 text-sm font-mono text-gray-400 border border-gray-700 rounded px-4 py-2 hover:bg-white/10"
                        >
                            Change Language: {content.toggleText}
                        </Link>
                    </div>
                )}
            </div>
        </nav>
    );
}
