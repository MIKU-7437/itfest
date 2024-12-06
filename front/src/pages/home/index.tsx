import CatalogCard from "@/widgets/Catalog/CatalogCard.tsx";
import CarouselCard from "@/shared/ui/Carousel/CarouselCard.tsx";

const Home = () => {
    const cardData = [
        {
            id: 1,
            href: "#",
            imgAlt: "Image 1 alt text",
            imgSrc: "/image-1.jpg",
            title: "Noteworthy technology acquisitions 2021",
            description: "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."
        },
        {
            id: 2,
            href: "#",
            imgAlt: "Image 1 alt text",
            imgSrc: "/image-1.jpg",
            title: "Noteworthy technology acquisitions 2021",
            description: "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."
        },
        {
            id: 3,
            href: "#",
            imgAlt: "Image 1 alt text",
            imgSrc: "/image-1.jpg",
            title: "Noteworthy technology acquisitions 2021",
            description: "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."
        },
        {
            id: 4,
            href: "#",
            imgAlt: "Image 1 alt text",
            imgSrc: "/image-1.jpg",
            title: "Noteworthy technology acquisitions 2021",
            description: "Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order."
        },
    ]
    return (
        <div>
            <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
                <div className="">
                    <CarouselCard/>
                </div>
                <div className={'mt-[73px]'}>
                    <CatalogCard cards={cardData}/>
                </div>
            </div>
        </div>
    );
};

export default Home;