import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Detection from "./pages/Detection";

const App = () => {
  return (
    <div className="min-h-screen flex flex-col bg-[#EAE1CF]">
      <Header />
      <main className="flex-grow flex justify-center items-center p-4">
        <Detection /> {/* ໃຊ້ Detection ທີ່ import ມາ */}
      </main>
      <Footer />
    </div>
  );
};

export default App;
