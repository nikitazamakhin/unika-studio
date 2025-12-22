import type { Metadata } from "next";
import SmoothScroll from '@/components/SmoothScroll';
import { GoogleAnalytics } from '@next/third-parties/google';
// import { Geist, Geist_Mono } from "next/font/google"; // Disabled due to build error
import "./globals.css";

// const geistSans = Geist({
//   variable: "--font-geist-sans",
//   subsets: ["latin"],
// });

// const geistMono = Geist_Mono({
//   variable: "--font-geist-mono",
//   subsets: ["latin"],
// });

export const metadata: Metadata = {
  title: "Unika Studio | AI Production",
  description: "Next-generation AI, commercial, and viral content production studio.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className="antialiased font-sans"
      >
        <SmoothScroll>
          {children}
        </SmoothScroll>
        <GoogleAnalytics gaId="G-XXXXXXXXXX" /> {/* REPLACE WITH YOUR GA4 ID */}
      </body>
    </html>
  );
}
