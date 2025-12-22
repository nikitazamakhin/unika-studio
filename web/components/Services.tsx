"use client";

import { Content } from '@/data/content';
import { useState } from 'react';
import Modal from './Modal';

export default function Services({ content }: { content: Content['services'] }) {
    const [activeModal, setActiveModal] = useState<'commercial' | 'viral' | null>(null);

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

                            <button
                                onClick={() => setActiveModal('commercial')}
                                className="w-full py-4 border border-gray-700 rounded-lg group-hover:bg-primary group-hover:text-black group-hover:border-primary transition-all font-semibold"
                            >
                                {content.commercial.cta}
                            </button>
                        </div>
                    </div>

                    {/* Card 2: AI SMM */}
                    <div id="viral" className="group relative p-1 rounded-2xl bg-gradient-to-b from-gray-800 to-transparent hover:from-purple-500 hover:to-purple-900/20 transition-all duration-500">
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

                            <button
                                onClick={() => setActiveModal('viral')}
                                className="w-full py-4 border border-gray-700 rounded-lg group-hover:bg-white group-hover:text-black group-hover:border-white transition-all font-semibold"
                            >
                                {content.viral.cta}
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            {/* Modals */}
            <Modal
                isOpen={!!activeModal}
                onClose={() => setActiveModal(null)}
                title={activeModal === 'commercial' ? (content.commercial.form!.title) : (content.viral.pricing!.title)}
            >
                {activeModal === 'commercial' && (
                    <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
                        <div>
                            <label className="block text-sm text-gray-400 mb-1">{content.commercial.form?.fields.name}</label>
                            <input type="text" className="w-full bg-black/50 border border-gray-700 rounded-lg p-3 text-white focus:border-primary outline-none" />
                        </div>
                        <div>
                            <label className="block text-sm text-gray-400 mb-1">{content.commercial.form?.fields.email}</label>
                            <input type="email" className="w-full bg-black/50 border border-gray-700 rounded-lg p-3 text-white focus:border-primary outline-none" />
                        </div>
                        <div>
                            <label className="block text-sm text-gray-400 mb-1">{content.commercial.form?.fields.budget}</label>
                            <select className="w-full bg-black/50 border border-gray-700 rounded-lg p-3 text-white focus:border-primary outline-none">
                                <option>$5k - $10k</option>
                                <option>$10k - $25k</option>
                                <option>$25k+</option>
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm text-gray-400 mb-1">{content.commercial.form?.fields.desc}</label>
                            <textarea rows={3} className="w-full bg-black/50 border border-gray-700 rounded-lg p-3 text-white focus:border-primary outline-none"></textarea>
                        </div>
                        <button className="w-full bg-primary text-black font-bold py-3 rounded-lg hover:bg-yellow-400 transition-colors">
                            {content.commercial.form?.submit}
                        </button>
                    </form>
                )}

                {activeModal === 'viral' && (
                    <div className="space-y-4">
                        <div className="grid gap-4">
                            {content.viral.pricing?.plans.map((plan, i) => (
                                <div key={i} className={`p-4 rounded-xl border ${plan.recommended ? 'border-primary bg-primary/10' : 'border-gray-800 bg-black/40'} flex justify-between items-center group cursor-pointer hover:border-gray-600`}>
                                    <div>
                                        <div className="flex items-center gap-2">
                                            <h4 className="font-bold text-white">{plan.name}</h4>
                                            {plan.recommended && <span className="text-[10px] bg-primary text-black px-2 py-0.5 rounded-full font-bold">POPULAR</span>}
                                        </div>
                                        <div className="text-gray-400 text-sm mt-1">
                                            {plan.features.join(" • ")}
                                        </div>
                                    </div>
                                    <div className="text-right">
                                        <div className="text-lg font-bold text-primary">{plan.price}</div>
                                        <button className="text-xs text-white underline mt-1 opacity-0 group-hover:opacity-100 transition-opacity">
                                            {content.viral.pricing?.action}
                                        </button>
                                    </div>
                                </div>
                            ))}
                        </div>
                        <p className="text-center text-xs text-gray-500 mt-4">
                            Need a custom package? <a href="#" className="underline text-gray-400 hover:text-white">Contact Sales</a>
                        </p>
                    </div>
                )}
            </Modal>
        </section>
    );
}
