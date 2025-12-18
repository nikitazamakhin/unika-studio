export type Content = typeof content.en;

export const content = {
    en: {
        lang: "en",
        navbar: {
            commercial: "COMMERCIAL",
            viral: "VIRAL",
            start: "START PROJECT",
            toggleLink: "/ru",
            toggleText: "RU"
        },
        hero: {
            label: "AI Production Studio",
            title_1: "CAPTIVATE",
            title_2: "THE ALGORITHM",
            desc: "We combine cinematic storytelling with generative AI to create commercial masterpieces and viral sensations that dominate the feed.",
            cta_commercial: "COMMERCIAL",
            cta_viral: "VIRAL PRODUCTION"
        },
        services: {
            label: "Our Products",
            title: "Dominate the Attention Economy",
            desc: "We deliver two distinct tiers of AI production. Choose the one that fits your brand's growth strategy.",
            commercial: {
                title: "Commercial Video",
                desc: "High-end, bespoke AI cinematography for TV commercials, brand movies, and music videos. Impossible visuals, produced at a fraction of the cost of traditional VFX.",
                features: ["Cinematic 4K Quality", "Custom Storyboarding", "Broadcast Rights Included"],
                cta: "Request Quote"
            },
            viral: {
                title: "AI SMM Packages",
                desc: "\"Content as a Service\". A steady stream of viral-ready vertical videos (Reels/Shorts) designed to hijack algorithms and grow your audience.",
                features: ["Monthly Content Deliveries", "Trend-Jacking Formats", "Optimized for Retention"],
                cta: "View Packages"
            }
        },
        portfolio: {
            label: "Selected Works",
            title: "Impossible Made Real",
            cases: [
                {
                    id: 1,
                    client: "Neon Energy",
                    type: "Commercial Spot",
                    description: "Cyberpunk aesthetic energy drink commercial generated 100% with AI.",
                    color: "from-purple-600 to-blue-600"
                },
                {
                    id: 2,
                    client: "Vogue Tech",
                    type: "Fashion Editorial",
                    description: "Surreal fashion showcase for wearble technology accessories.",
                    color: "from-pink-500 to-rose-500"
                },
                {
                    id: 3,
                    client: "Future Motors",
                    type: "Product Reveal",
                    description: "Concept car anticipation video using generative 3D visualization.",
                    color: "from-amber-500 to-orange-600"
                },
                {
                    id: 4,
                    client: "Zenith Real Estate",
                    type: "Architectural Viz",
                    description: "Dreamscape luxury property tours that defy physics.",
                    color: "from-emerald-500 to-teal-600"
                }
            ]
        },
        process: {
            label: "The Process",
            title: "From Abstract to Asset",
            steps: [
                {
                    num: "01",
                    title: "Vision & Briefing",
                    desc: "We decode your brand DNA. You provide the goals, we define the aesthetic territory and narrative arc."
                },
                {
                    num: "02",
                    title: "AI Concepting",
                    desc: "Rapid iteration of styleframes. We generate dozens of visual directions in 24 hours to find the perfect look."
                },
                {
                    num: "03",
                    title: "Production & Synthesis",
                    desc: "The magic happens. Video generation, consistent character training, and motion coherence pipelines run full throttle."
                },
                {
                    num: "04",
                    title: "Polish & Delivery",
                    desc: "Human touch meets machine power. Upscaling to 4K, color grading, sound design, and final edit."
                }
            ]
        },
        footer: {
            title: "Let's Talk",
            cta: "START PROJECT",
            email: "hello@unika.studio",
            address: "Dubai, UAE",
            socials: [
                { label: "Instagram", link: "#" },
                { label: "LinkedIn", link: "#" },
                { label: "YouTube", link: "#" }
            ],
            links: [
                { label: "Commercial", link: "#commercial" },
                { label: "Viral", link: "#viral" }
            ],
            copyright: "© 2025 Unika Studio. All rights reserved."
        }
    },
    ru: {
        lang: "ru",
        navbar: {
            commercial: "РЕКЛАМА",
            viral: "ВИРУСНЫЙ КОНТЕНТ",
            start: "ОБСУДИТЬ ПРОЕКТ",
            toggleLink: "/",
            toggleText: "EN"
        },
        hero: {
            label: "Агентство AI Продакшена",
            title_1: "ЗАХВАТЫВАЕМ",
            title_2: "АЛГОРИТМЫ",
            desc: "Мы объединяем кинематографический сторителлинг и генеративный ИИ, создавая рекламные шедевры и вирусный контент.",
            cta_commercial: "РЕКЛАМА",
            cta_viral: "ВИРУСНЫЙ КОНТЕНТ"
        },
        services: {
            label: "Наши Продукты",
            title: "Внимание — новая валюта",
            desc: "Мы предлагаем два уровня AI-продакшена. Выберите тот, который подходит для стратегии роста вашего бренда.",
            commercial: {
                title: "Коммерческое Видео",
                desc: "Премиальная AI-кинематография для ТВ-рекламы, бренд-фильмов и клипов. Невозможный визуал за долю стоимости традиционного VFX.",
                features: ["Кинематографическое 4K качество", "Уникальная раскадровка", "Права на трансляцию"],
                cta: "Запросить смету"
            },
            viral: {
                title: "AI SMM Пакеты",
                desc: "\"Контент как сервис\". Поток вирусных вертикальных видео (Reels/Shorts), созданных для захвата алгоритмов и роста аудитории.",
                features: ["Ежемесячные поставки контента", "Трендовые форматы", "Оптимизация под удержание"],
                cta: "Смотреть пакеты"
            }
        },
        portfolio: {
            label: "Избранные работы",
            title: "Невозможное стало реальным",
            cases: [
                {
                    id: 1,
                    client: "Neon Energy",
                    type: "Рекламный ролик",
                    description: "Киберпанк-эстетика для энергетика, созданная на 100% с помощью ИИ.",
                    color: "from-purple-600 to-blue-600"
                },
                {
                    id: 2,
                    client: "Vogue Tech",
                    type: "Fashion Эдиториал",
                    description: "Сюрреалистичный показ модных технологических аксессуаров.",
                    color: "from-pink-500 to-rose-500"
                },
                {
                    id: 3,
                    client: "Future Motors",
                    type: "Презентация продукта",
                    description: "Тизер концепт-кара с использованием генеративной 3D-визуализации.",
                    color: "from-amber-500 to-orange-600"
                },
                {
                    id: 4,
                    client: "Zenith Real Estate",
                    type: "Архитектурная виз.",
                    description: "Туры по элитной недвижимости мечты, бросающие вызов физике.",
                    color: "from-emerald-500 to-teal-600"
                }
            ]
        },
        process: {
            label: "Процесс",
            title: "От Идеи до Результата",
            steps: [
                {
                    num: "01",
                    title: "Видение и Бриф",
                    desc: "Мы расшифровываем ДНК вашего бренда. Вы ставите цели, мы определяем эстетическую территорию и нарратив."
                },
                {
                    num: "02",
                    title: "AI Концепт",
                    desc: "Быстрая итерация стиль-фреймов. Мы генерируем десятки визуальных направлений за 24 часа."
                },
                {
                    num: "03",
                    title: "Синтез и Продакшен",
                    desc: "Магия в действии. Генерация видео, консистентность персонажей и моушн-дизайн на полных оборотах."
                },
                {
                    num: "04",
                    title: "Полиш и Сдача",
                    desc: "Человеческий тач и мощь машин. Апскейл до 4K, цветокоррекция, саунд-дизайн и финальный монтаж."
                }
            ]
        },
        footer: {
            title: "Обсудить проект",
            cta: "НАЧАТЬ",
            email: "hello@unika.studio",
            address: "Dubai, UAE",
            socials: [
                { label: "Instagram", link: "#" },
                { label: "LinkedIn", link: "#" },
                { label: "YouTube", link: "#" }
            ],
            links: [
                { label: "Реклама", link: "#commercial" },
                { label: "Вирусный контент", link: "#viral" }
            ],
            copyright: "© 2025 Unika Studio. Все права защищены."
        }
    }
};
