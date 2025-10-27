"use client";
import { useState, useRef, useEffect, useMemo } from "react";
import { SendHorizontal } from "lucide-react";
import { motion } from "framer-motion";
import dynamic from "next/dynamic";


const LiquidEther = dynamic(() => import("../utils/LiquidEther"), {
  ssr: false,
});


const acneInfo = `Test`;


export default function MedicalChatUI() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "👋 Hello! I’m CareSphere, your AI medical assistant. How can I help you today?",
    },
  ]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef<HTMLDivElement | null>(null);


  const sendMessage = () => {
    if (!input.trim()) return;
    const newMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, newMsg, { sender: "bot", text: acneInfo }]);
    setInput("");
  };


  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  
  const etherProps = useMemo(
    () => ({
      colors: ["#5227FF", "#FF9FFC", "#B19EEF"],
      mouseForce: 20,
      cursorSize: 100,
      isViscous: false,
      viscous: 30,
      iterationsViscous: 32,
      iterationsPoisson: 32,
      resolution: 0.5,
      isBounce: false,
      autoDemo: true,
      autoSpeed: 0.5,
      autoIntensity: 2.2,
      takeoverDuration: 0.25,
      autoResumeDelay: 3000,
      autoRampDuration: 0.6,
    }),
    []
  );

  return (
    <div className="relative flex flex-col h-[calc(100vh-4.3rem)] bg-gradient-to-br from-black to-teal-900 overflow-hidden">
      
      {/* Background */}
      <div className="absolute inset-0 z-0 pointer-events-none">
        <LiquidEther {...etherProps} />
      </div>

      {/* Chat UI */}
      <div className="flex-1 overflow-y-auto pt-10 px-6 md:px-36 space-y-8 relative z-10">
        {messages.map((msg, idx) => (
          <motion.div
            key={idx}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[70%] p-6 rounded-3xl shadow-lg text-sm break-words ${
                msg.sender === "user"
                  ? "text-white border bg-black/50 rounded-br-none"
                  : "text-white border bg-black/50 rounded-bl-none"
              }`}
            >
              {msg.text}
            </div>
          </motion.div>
        ))}
        <div ref={chatEndRef} />
      </div>

      {/* Input Section */}
      <div className="p-4 px-6 sm:px-8 relative z-10">
        <div className="flex border border-gray-500 items-center max-w-2xl mx-auto rounded-full shadow-inner px-8 py-2 hover:border hover:border-white">
          <input
            type="text"
            placeholder="Type your symptoms or questions ..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 outline-none bg-transparent text-white pr-4"
          />
          <button
            onClick={sendMessage}
            className="font-bold border border-transparent hover:border hover:border-white text-white rounded-full p-2 transition"
          >
            <SendHorizontal className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
}
