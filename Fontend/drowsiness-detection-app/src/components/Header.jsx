import React from "react";
import logo from "../assets/logo.png";

const Header = () => {
  return (
    <header className="flex items-center justify-between px-6 py-2 bg-gradient-to-r from-black to-blue-700 h-[20vh] relative">
      <img
        src={logo}
        alt="Logo"
        className="h-[180px] w-auto absolute bottom-[-35px] left-6"
      />
      <div className="text-center text-white flex-1">
        <h1 className="text-2xl font-bold">
          ບົດໂຄງການຈົບຊັ້ນລະດັບປະລິນຍາຕີວິທະຍາສາດ
        </h1>
        <h2 className="text-lg">ສາຂາ ວິທະຍາສາດຄອມພິວເຕີ</h2>
        <p className="font-bold">
          ການແຈ້ງເຕືອນອາການເຫງົານອນຂອງຜູ້ຂັບຂີ່ແບບອັດຕະໂນມັດ
          ໂດຍນຳໃຊ້ເຕັກນິກການຮຽນຮູ້ເລິກເຊິງ
        </p>
        <p className="italic">
          Automatic Driver Drowsiness Warning Using Deep Learning
        </p>
      </div>
      <div className="w-[80px]"></div>{" "}
      {/* เว้นช่องว่างขวาให้โลโก้อยู่ด้านซ้าย */}
    </header>
  );
};

export default Header;
