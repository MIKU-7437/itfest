import React, {ReactNode} from 'react';
import Footer from "@/widgets/Footer";
import AboutUs from "@/widgets/AboutUs/AboutUs.tsx";
import Header from "@/widgets/Header";
import Nav from "@/widgets/Nav/Nav.tsx";

interface LayoutProps {
    children: ReactNode
}

const DefaultLayout: React.FC<LayoutProps> = ({children}) => {
    return (
        <React.Fragment>
            <div className='w-full max-w-[1440px] mx-auto'>
                <Header/>
                <div className={'mt-[53px]'}>
                    <Nav/>
                </div>
                <div>
                    {children}
                </div>
            </div>
            <AboutUs/>
            <Footer/>
        </React.Fragment>

    );
};

export default DefaultLayout;