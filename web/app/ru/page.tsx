import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Services from "@/components/Services";
import Portfolio from "@/components/Portfolio";
import Process from "@/components/Process";
import Footer from "@/components/Footer";
import VideoSection from "@/components/VideoSection";
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

            {/* Showreel Block */}
            <VideoSection
                videoUrl={c.showreel.video}
                posterUrl={c.showreel.poster}
                title={c.showreel.title}
                subtitle={c.showreel.subtitle}
            />

            <Services content={c.services} />
            <Portfolio content={c.portfolio} />
            <Process content={c.process} />

            {/* Vision Block */}
            <VideoSection
                videoUrl={c.vision.video}
                posterUrl={c.vision.poster}
                title={c.vision.title}
                subtitle={c.vision.subtitle}
                overlayColor="bg-primary/20"
            />

            <Footer content={c.footer} />
        </main>
    );
}
