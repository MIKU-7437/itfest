import React from 'react';
import {Link} from "react-router-dom";



const Nav = () => {
    return (
        <React.Fragment>
            <div className={'max-w-[1440px] mx-auto h-[60px] bg-[#FF4900] rounded-[10px] flex justify-center items-center'}>
                <div className={'flex justify-center items-center text-center gap-24 font-bold text-white tracking-[-0.5px] leading-[14px]'}>
                    <Link to="/">О нас</Link>
                    <Link to="/">Каталог</Link>
                    <Link to="/">Прайс</Link>
                    <Link to="/">Как купить</Link>
                    <Link to="/">Контакты</Link>
                </div>
            </div>
        </React.Fragment>
    );
};

export default Nav;