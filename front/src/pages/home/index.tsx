import CatalogCard from "@/widgets/Catalog/CatalogCard.tsx";
import CarouselCard from "@/shared/ui/Carousel/CarouselCard.tsx";
import {useEffect, useState} from "react";
import axiosInstance from "@/shared/libs/axios.ts";

const Home = () => {
    const [categories, setCategories] = useState<[]>([]);
    const fetchCategories = async () => {
        const response = await axiosInstance.get('v1/store/category/get-all/')
        setCategories(response.data)
        console.log(response.data);

    }

    useEffect(() => {
        fetchCategories()
    }, []);
    return (
        <div>
            <div className="h-56 sm:h-64 xl:h-80 2xl:h-96">
                <div className="">
                    <CarouselCard/>
                </div>
                <div className={'text-center text-[40px] leading-[14px] font-bold mt-[57px]'}>Категорий</div>
                <div className={'mt-[73px]'}>
                    <CatalogCard cards={categories}/>
                </div>
            </div>
        </div>
    );
};

export default Home;