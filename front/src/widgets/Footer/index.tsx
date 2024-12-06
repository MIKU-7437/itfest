import React from "react";
import Instagram from "@/shared/assets/icons/instagram";
import Facebook from "@/shared/assets/icons/facebook";
import IconX from "@/shared/assets/icons/iconX";
import Youtube from "@/shared/assets/icons/youtube";

const Footer = () => {
   return (
     <React.Fragment>
       <div className="w-full h-auto bg-[#969696] text-[#FFFF]">
         <div className="flex items-center justify-between pl-[400px] pr-[400px] pt-[55px] gap-[20px] text-[16px] font-semibold ">
           <div>О нас</div>
           <div>Каталог</div>
           <div>Прайс</div>
           <div>Как купить</div>
           <div>Контакты</div>
         </div>
         <div className="border-[1px] mt-[30px] w-full max-w-[1440px] mx-auto ">
           <hr />
         </div>

         <div className="flex items-center justify-between pt-[20px]">
           <div className="flex items-center ">
             <div className="text-[20px] ">Будьте в курсе новостей</div>
             <div></div>
             <div></div>
           </div>

           <div className="flex items-center ">
             <div className="text-[20px]">Телефоны для связи</div>
             <div className="flex items-center">
               <div className="font-bold">+7(747)9999999</div>
               <div className="font-bold">+7(707)9999999</div>
             </div>
           </div>

           <div className="flex items-center justify-between gap-[35px]">
             <Instagram />
             <Facebook />
             <IconX />
             <Youtube />
           </div>
         </div>
         
         <div className="text-center text-[16px] font-semibold pt-[15px]">©2024 Hackaton</div>

       </div>
     </React.Fragment>
   );
   };

export default Footer;