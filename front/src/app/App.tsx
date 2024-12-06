import {Suspense} from "react";
import {Route, Routes} from "react-router-dom";
import DefaultLayout from "@/app/layout/default.tsx";
import Loader from "@/shared/ui/Loader/Loader.tsx";
import Home from "@/pages/home";


const App = () => {
    return (
        <Suspense fallback={<Loader/>}>
            <DefaultLayout>
                <Routes>
                    <Route path="/" element={<Home />} />
                </Routes>
            </DefaultLayout>
        </Suspense>
    );
};

export default App;