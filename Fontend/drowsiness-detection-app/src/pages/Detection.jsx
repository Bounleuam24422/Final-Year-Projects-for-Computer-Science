import React, { useState, useRef, useEffect } from "react";

const DetectionBox = () => {
  const [isWebcamOn, setIsWebcamOn] = useState(false);
  const videoRef = useRef(null);

  const handleStart = async () => {
    try {
      const res = await fetch("http://localhost:8000/start", { method: "GET" });
      if (res.ok) {
        setIsWebcamOn(true);
      } else {
        console.error("Start failed with status:", res.status);
      }
    } catch (error) {
      console.error("Start failed:", error);
    }
  };

  const handleStop = async () => {
    try {
      await fetch("http://localhost:8000/stop", { method: "GET" });
    } catch (error) {
      console.error("Stop failed:", error);
    }
    setIsWebcamOn(false);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  // หยุด stream เมื่อ Component หายไป
  useEffect(() => {
    return () => {
      if (isWebcamOn) handleStop();
    };
  }, [isWebcamOn]);

  return (
    <div
      className={`absolute left-1/2 transform -translate-x-1/2
        w-[90%] max-w-2xl bg-[#EAE1CF] shadow-lg transition-all duration-300
        ${
          isWebcamOn
            ? "top-[15%] border-none"
            : "top-[35%] border-dotted border-4 border-black rounded-lg text-center flex flex-col items-center justify-center"
        }`}
    >
      {!isWebcamOn ? (
        <div className="flex flex-col items-center p-6">
          <h2 className="text-2xl font-bold text-blue-700">ການກວດຈັບ</h2>
          <p className="mt-4 text-lg text-center">
            ກົດປຸ່ມເພື່ອເລີ່ມການກວດຈັບຜ່ານກ້ອງ Webcam
          </p>
          <button
            className="mt-4 bg-blue-600 text-white px-6 py-3 text-lg font-bold rounded-full flex items-center justify-center gap-2 hover:bg-blue-800"
            onClick={handleStart}
          >
            📷 ເລີ່ມກວດຈັບ
          </button>
        </div>
      ) : (
        <div className="relative w-full h-full">
          {/* ✅ ดึง stream จาก backend */}
          <img
            ref={videoRef}
            src={`http://localhost:8000/video_feed?${Date.now()}`}
            alt="Webcam stream"
            className="w-full h-auto rounded-lg shadow-lg"
          />

          {/* ❌ ปุ่มปิด */}
          <button
            className="absolute top-2 right-2 bg-red-500 hover:bg-red-600 text-white font-bold px-5 py-2 rounded-full flex items-center gap-2 shadow-lg z-10"
            onClick={handleStop}
          >
            <img
              src="/camera-icon.png"
              alt="camera"
              className="w-5 h-5"
              onError={(e) => (e.target.style.display = "none")}
            />
            ປິດກ້ອງ
          </button>
        </div>
      )}
    </div>
  );
};

export default DetectionBox;
