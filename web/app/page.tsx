import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Services from "@/components/Services";
import Portfolio from "@/components/Portfolio";
import Process from "@/components/Process";
import Footer from "@/components/Footer";
import { content } from "@/data/content";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Unika Studio | AI Production & Viral Content Agency",
  description: "We combine cinematic storytelling with generative AI to create commercial masterpieces and viral sensations. Dubai-based AI Production Studio.",
  keywords: ["AI production", "generative AI", "viral marketing", "video production", "commercials", "Dubai"],
  openGraph: {
    title: "Unika Studio | AI Production & Viral Content",
    description: "Dominating the attention economy with generative AI.",
    siteName: "Unika Studio",
    locale: "en_US",
    type: "website",
  },
};

export default function Home() {
  const c = content.en;

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
