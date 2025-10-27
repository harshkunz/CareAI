"use client";
import { Stethoscope } from "lucide-react";
import { motion } from "framer-motion";

export default function Navbar() {
  return (
    <nav className="w-full bg-gradient-to-br from-black to-teal-800 shadow-lg sticky top-0 z-50 border-b border-teal-900">
      <div className="flex justify-center items-center py-4">
        <motion.div
          whileHover={{
            scale: 1.05,
            color: "#5eead4",
            textShadow: "0 0 12px #5eead4",
          }}
          transition={{ duration: 0.3 }}
          className="flex items-center justify-center cursor-pointer"
        >
          <Stethoscope className="w-9 h-9 mr-2 text-teal-400" />
          <h1 className="text-2xl font-semibold text-teal-400">CareAI</h1>
        </motion.div>
      </div>
    </nav>
  );
}
