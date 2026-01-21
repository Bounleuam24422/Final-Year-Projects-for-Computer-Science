const Footer = () => {
  return (
    <footer className="fixed bottom-0 w-full bg-black text-white py-4 text-center">
      <div className="flex justify-around">
        <div>
          <strong>ພັດທະນາໂດຍ:</strong>
          <p>ທ ບຸນເຫຼື່ອມ ແສງຄຳຢອງ ຫ້ອງ 4CS2</p>
          <p>ທ ຈ້າປໍເຮີ່ ເຊົາເກຍເຮີ່ ຫ້ອງ 4CS2</p>
        </div>
        <div>
          <strong>ນຳພາໂດຍ:</strong>
          <p>ອຈ.ປອ ພູທອນ ວົງປະສິດ</p>
        </div>
        <div>
          <strong>ຊ່ວຍນຳພາໂດຍ:</strong>
          <p>ຊອ.ປທ. ອໍລະດີ ຄຳມະນີວົງ</p>
        </div>
      </div>
      <p className="mt-2">ສົກສຶກສາ 2024-2025</p>
    </footer>
  );
};

export default Footer;
