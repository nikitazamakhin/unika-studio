import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Services from "@/components/Services";
import Portfolio from "@/components/Portfolio";
import Process from "@/components/Process";
import Footer from "@/components/Footer";
import { content } from "@/data/content";
import { Metadata } from "next";

export const metadata: Metadata = {
    title: "Unika Studio | AI Продакшен и Вирусный Маркетинг",
    description: "Студия генеративного ИИ в Дубае. Создаем кинематографическую рекламу и вирусные Reels для захвата внимания.",
    keywords: ["AI продакшен", "генеративный ИИ", "вирусный маркетинг", "видео продакшен", "реклама", "Дубай", "SMM"],
    openGraph: {
        title: "Unika Studio | AI Продакшен и Вирусный Контент",
        description: "Захватываем алгоритмы с помощью генеративного ИИ.",
        siteName: "Unika Studio",
        locale: "ru_RU",
        type: "website",
    },
};

export default function HomeRU() {
    const c = content.ru;

    return (
        <main className="min-h-screen">
            <Navbar content={c.navbar} />
            <Hero content={c.hero} />

            <Services content={c.services} />
            <Portfolio content={c.portfolio} />
            <Process content={c.process} />

            <Footer content={c.footer} />
        </main>
    );
}
