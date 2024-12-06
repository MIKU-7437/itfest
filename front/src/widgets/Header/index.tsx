import Input from '@/shared/ui/Input/Input';
import React from 'react';
import Basket from "@/shared/assets/icons/basket.tsx";
import Search from "@/shared/assets/icons/Search.tsx";

const Index = () => {
    return (
        <React.Fragment>
            <div className="flex items-center justify-between pt-[39px]">
                <div className={'flex  items-center gap-[82px]'}>
                    <div className="text-[40px] text-[#FF7640] font-bold">Nacho</div>
                    <div className={'relative'}>
                        <div className={'absolute right-[10px] bottom-[10px] z-[1]'}>
                            <Search />
                        </div>
                        <Input className={'w-[300px] rounded-[10px]'} placeholder={'Search...'} type="text"/>
                    </div>
                </div>

                <div className={'flex items-center gap-[20px] text-[16px]'}>

                    <div className={'flex gap-[5px] items-center'}>
                        <Basket/>
                        <div>Корзина</div>
                    </div>


                    <div className={'flex gap-[30px] items-center'}>
                        <div>Войти</div>
                        <div>|</div>
                        <div>Регистрация</div>
                    </div>


                </div>


            </div>

        </React.Fragment>
    );
};

export default Index;