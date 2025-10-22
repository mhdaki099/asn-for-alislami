#!/usr/bin/env python3
"""
Installation script for PDF to Excel converter with OCR capabilities
This script helps install the required dependencies for image processing and OCR
"""

import subprocess
import sys
import os
import platform

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def install_tesseract_instructions():
    """Provide instructions for installing Tesseract OCR"""
    system = platform.system().lower()
    
    print("\n📋 Tesseract OCR Installation Instructions:")
    print("=" * 50)
    
    if system == "windows":
        print("Windows:")
        print("1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki")
        print("2. Install the .exe file")
        print("3. Add Tesseract to your PATH environment variable")
        print("   - Usually: C:\\Program Files\\Tesseract-OCR")
        print("4. Restart your terminal/command prompt")
        
    elif system == "darwin":  # macOS
        print("macOS:")
        print("1. Install using Homebrew:")
        print("   brew install tesseract")
        print("2. Or download from: https://github.com/tesseract-ocr/tesseract")
        
    elif system == "linux":
        print("Linux:")
        print("Ubuntu/Debian:")
        print("  sudo apt-get update")
        print("  sudo apt-get install tesseract-ocr")
        print("")
        print("CentOS/RHEL:")
        print("  sudo yum install tesseract")
        print("")
        print("Fedora:")
        print("  sudo dnf install tesseract")
    
    print("\n⚠️  Make sure Tesseract is accessible from command line:")
    print("   tesseract --version")

def main():
    print("🚀 Installing PDF to Excel Converter with OCR capabilities...")
    print("=" * 60)
    
    # Check if this is Windows
    if platform.system() == "Windows":
        print("🪟 Detected Windows system")
        print("💡 For Windows users, we recommend using GPT-4 Vision for OCR")
        print("   This avoids dependency conflicts and provides better accuracy")
        
        # Core packages (Windows-optimized)
        core_packages = [
            "streamlit",
            "pandas",
            "PyPDF2",
            "openpyxl",
            "PyMuPDF",
            "openai>=1.0.0",
            "python-dotenv",
            "numpy>=1.24.0",
            "Pillow>=10.0.0",
        ]
        
        # Image processing packages
        image_packages = [
            "opencv-python>=4.8.0",
            "scikit-image>=0.21.0",
            "imageio>=2.31.0",
            "matplotlib>=3.7.0",
        ]
        
        # OCR packages (minimal for Windows)
        ocr_packages = [
            "pytesseract>=0.3.10",
            "protobuf<=3.20.3",  # Fix protobuf conflicts
        ]
        
        print("\n📦 Installing core packages...")
        for package in core_packages:
            install_package(package)
        
        print("\n🖼️ Installing image processing packages...")
        for package in image_packages:
            install_package(package)
        
        print("\n🔍 Installing OCR packages...")
        for package in ocr_packages:
            install_package(package)
            
    else:
        # Non-Windows systems
        core_packages = [
            "streamlit",
            "pandas",
            "PyPDF2",
            "openpyxl",
            "PyMuPDF",
            "openai>=1.0.0",
            "python-dotenv",
            "numpy>=1.24.0",
            "Pillow>=10.0.0",
        ]
        
        ocr_packages = [
            "pytesseract>=0.3.10",
            "opencv-python>=4.8.0",
            "paddleocr>=2.7.0",
            "easyocr>=1.7.0",
            "scikit-image>=0.21.0",
            "imageio>=2.31.0",
            "matplotlib>=3.7.0",
        ]
        
        print("\n📦 Installing core packages...")
        for package in core_packages:
            install_package(package)
        
        print("\n🔍 Installing OCR packages...")
        for package in ocr_packages:
            install_package(package)
    
    # Check if Tesseract is available
    try:
        result = subprocess.run(["tesseract", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Tesseract OCR is already installed and accessible")
        else:
            print("⚠️  Tesseract OCR not found in PATH")
            install_tesseract_instructions()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("⚠️  Tesseract OCR not found in PATH")
        install_tesseract_instructions()
    
    print("\n🎉 Installation complete!")
    print("\n📝 Next steps:")
    print("1. Set up your OpenAI API key in a .env file:")
    print("   OPENAI_API_KEY=your_api_key_here")
    print("2. Run the application:")
    print("   streamlit run main.py")
    
    if platform.system() == "Windows":
        print("\n💡 Windows users - The application now uses:")
        print("   - GPT-4 Vision API for primary OCR (best accuracy)")
        print("   - Tesseract as fallback (if installed)")
        print("   - No complex dependency conflicts")
    else:
        print("\n💡 The application now supports:")
        print("   - Regular PDF text extraction")
        print("   - Scanned PDF OCR with multiple engines")
        print("   - Latest GPT-4o and GPT-4o-mini models")
        print("   - Automatic text file saving")

if __name__ == "__main__":
    main()
