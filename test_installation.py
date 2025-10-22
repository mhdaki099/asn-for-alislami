#!/usr/bin/env python3
"""
Test script to verify installation of PDF to Excel converter with OCR capabilities
"""

import sys
import importlib
import subprocess

def test_package(package_name, import_name=None):
    """Test if a package can be imported"""
    if import_name is None:
        import_name = package_name
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {package_name}")
        return True
    except ImportError as e:
        print(f"❌ {package_name}: {e}")
        return False

def test_tesseract():
    """Test if Tesseract OCR is available"""
    try:
        result = subprocess.run(["tesseract", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            version = result.stdout.split('\n')[0]
            print(f"✅ Tesseract OCR: {version}")
            return True
        else:
            print(f"❌ Tesseract OCR: Command failed")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("❌ Tesseract OCR: Not found in PATH")
        return False

def test_environment():
    """Test environment variables"""
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("✅ OpenAI API Key: Found")
        return True
    else:
        print("❌ OpenAI API Key: Not found in .env file")
        return False

def main():
    print("🧪 Testing PDF to Excel Converter Installation")
    print("=" * 50)
    
    # Core packages
    core_packages = [
        ("streamlit", "streamlit"),
        ("pandas", "pandas"),
        ("PyPDF2", "PyPDF2"),
        ("openpyxl", "openpyxl"),
        ("PyMuPDF", "fitz"),
        ("openai", "openai"),
        ("python-dotenv", "dotenv"),
        ("numpy", "numpy"),
        ("PIL", "PIL"),
    ]
    
    # OCR packages
    ocr_packages = [
        ("pytesseract", "pytesseract"),
        ("opencv-python", "cv2"),
        ("paddleocr", "paddleocr"),
        ("easyocr", "easyocr"),
        ("scikit-image", "skimage"),
        ("imageio", "imageio"),
        ("matplotlib", "matplotlib"),
    ]
    
    print("\n📦 Testing core packages...")
    core_results = []
    for package, import_name in core_packages:
        core_results.append(test_package(package, import_name))
    
    print("\n🔍 Testing OCR packages...")
    ocr_results = []
    for package, import_name in ocr_packages:
        ocr_results.append(test_package(package, import_name))
    
    print("\n🔧 Testing system dependencies...")
    tesseract_ok = test_tesseract()
    
    print("\n🔑 Testing environment...")
    env_ok = test_environment()
    
    # Summary
    print("\n📊 Installation Summary")
    print("=" * 30)
    
    core_ok = all(core_results)
    ocr_ok = all(ocr_results)
    
    print(f"Core packages: {'✅ All OK' if core_ok else '❌ Some missing'}")
    print(f"OCR packages: {'✅ All OK' if ocr_ok else '❌ Some missing'}")
    print(f"Tesseract OCR: {'✅ OK' if tesseract_ok else '❌ Missing'}")
    print(f"Environment: {'✅ OK' if env_ok else '❌ Missing API key'}")
    
    if core_ok and ocr_ok and tesseract_ok and env_ok:
        print("\n🎉 Installation is complete and ready to use!")
        print("\n🚀 Run the application with:")
        print("   streamlit run main.py")
    else:
        print("\n⚠️  Installation incomplete. Please fix the issues above.")
        
        if not core_ok or not ocr_ok:
            print("\n💡 Try running the installation script:")
            print("   python install_dependencies.py")
        
        if not tesseract_ok:
            print("\n💡 Install Tesseract OCR:")
            print("   Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
            print("   macOS: brew install tesseract")
            print("   Linux: sudo apt-get install tesseract-ocr")
        
        if not env_ok:
            print("\n💡 Create a .env file with your OpenAI API key:")
            print("   OPENAI_API_KEY=your_api_key_here")

if __name__ == "__main__":
    main()
