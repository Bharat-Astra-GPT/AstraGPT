import React, { useState } from 'react';
import { Plus, Sliders, Mic, Sparkles, Camera, Image, FileText, HardDrive } from 'lucide-react';

const CustomAIInterface = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Leonardo AI Style Dark Theme Colors
  const bgColor = "bg-[#0d0d0f]"; // Deep dark background
  const cardColor = "bg-[#1a1a1c]"; // Slightly lighter for the bottom bar
  const accentColor = "text-white";
  const iconBg = "hover:bg-[#2a2a2c] transition-all duration-200";

  return (
    <div className={`flex flex-col justify-end h-screen ${bgColor} p-4 font-sans text-white`}>
      
      {/* Bottom Rectangular Board */}
      <div className={`${cardColor} rounded-3xl p-4 shadow-2xl relative`}>
        
        {/* Attachment Pop-up Menu */}
        {isMenuOpen && (
          <div className="absolute bottom-20 left-4 bg-[#1a1a1c] border border-[#2d2d2f] rounded-2xl p-2 flex flex-col gap-2 shadow-xl animate-in fade-in slide-in-from-bottom-4 duration-200">
            <button className="flex items-center gap-3 p-3 hover:bg-[#2d2d2f] rounded-xl"><Camera size={20}/> Camera</button>
            <button className="flex items-center gap-3 p-3 hover:bg-[#2d2d2f] rounded-xl"><Image size={20}/> Gallery</button>
            <button className="flex items-center gap-3 p-3 hover:bg-[#2d2d2f] rounded-xl"><FileText size={20}/> File</button>
            <button className="flex items-center gap-3 p-3 hover:bg-[#2d2d2f] rounded-xl"><HardDrive size={20}/> Drive</button>
          </div>
        )}

        {/* Input Bar Section */}
        <div className="flex items-center justify-between gap-2">
          
          {/* Left Icons (Tick Marked) */}
          <div className="flex items-center gap-4">
            <button 
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className={`p-2 rounded-full ${iconBg}`}
            >
              <Plus size={28} />
            </button>
            
            <button className={`p-2 rounded-full ${iconBg}`}>
              <Sliders size={24} className="opacity-70" />
            </button>
          </div>

          {/* Right Icons (Tick Marked) */}
          <div className="flex items-center gap-3">
            {/* Fast Mode Indicator */}
            <div className="bg-[#2a2a2c] px-4 py-2 rounded-full text-sm font-medium border border-[#3d3d3f]">
              Fast
            </div>

            <button className={`p-3 rounded-full ${iconBg} border border-[#2d2d2f]`}>
              <Mic size={24} />
            </button>

            <button className="p-3 bg-gradient-to-tr from-gray-700 to-gray-500 rounded-full shadow-lg">
              <Sparkles size={24} fill="white" />
            </button>
          </div>

        </div>

        {/* Placeholder for "Ask Gemini" type text */}
        <div className="mt-2 ml-2 text-gray-500 text-lg">
          Ask AI...
        </div>
      </div>
    </div>
  );
};                                     
