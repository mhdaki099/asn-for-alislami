#!/usr/bin/env python3
"""
Windows-specific installation script for PDF to Excel converter with OCR capabilities
"""

import subprocess
import sys
import os
import platform
import urllib.request
import zipfile
import tempfile

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def download_and_install_tesseract():
    """Download and install Tesseract for Windows"""
    try:
        print("\n🔍 Checking if Tesseract is already installed...")
        
        # Check if tesseract is already in PATH
        result = subprocess.run(["tesseract", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Tesseract is already installed and accessible")
            return True
    except:
        pass
    
    print("\n📥 Downloading Tesseract OCR for Windows...")
    
    # Tesseract download URL (latest stable version)
    tesseract_url = "https://github.com/UB-Mannheim/tesseract/releases/download/v5.3.3.20231005/tesseract-ocr-w64-setup-5.3.3.20231005.exe"
    download_path = os.path.join(tempfile.gettempdir(), "tesseract-installer.exe")
    
    try:
        print("Downloading Tesseract installer...")
        urllib.request.urlretrieve(tesseract_url, download_path)
        print("✅ Download complete")
        
        print("\n🚀 Starting Tesseract installation...")
        print("Please follow the installation wizard:")
        print("1. Accept the license agreement")
        print("2. Choose installation directory (default is fine)")
        print("3. Make sure 'Add Tesseract to PATH' is checked")
        print("4. Complete the installation")
        
        # Run the installer
        subprocess.run([download_path], check=True)
        
        # Clean up
        os.remove(download_path)
        
        print("\n✅ Tesseract installation completed!")
        print("Please restart your terminal/command prompt for PATH changes to take effect.")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to download/install Tesseract: {e}")
        print("\n💡 Manual installation:")
        print("1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki")
        print("2. Run the installer")
        print("3. Make sure to add Tesseract to PATH during installation")
        return False

def fix_protobuf_issues():
    """Fix protobuf version conflicts"""
    print("\n🔧 Fixing protobuf version conflicts...")
    
    try:
        # Uninstall problematic packages
        packages_to_remove = ["protobuf", "paddleocr", "easyocr"]
        
        for package in packages_to_remove:
            try:
                subprocess.run([sys.executable, "-m", "pip", "uninstall", package, "-y"], 
                             check=True, capture_output=True)
                print(f"✅ Removed {package}")
            except:
                pass
        
        # Install compatible protobuf version
        install_package("protobuf<=3.20.3")
        
        return True
    except Exception as e:
        print(f"⚠️  Protobuf fix failed: {e}")
        return False

def main():
    print("🚀 Windows Installation for PDF to Excel Converter with OCR")
    print("=" * 60)
    
    if platform.system() != "Windows":
        print("❌ This script is designed for Windows systems only.")
        return
    
    # Core packages
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
    
    # OCR packages
    ocr_packages = [
        "pytesseract>=0.3.10",
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
    
    # Fix protobuf issues
    fix_protobuf_issues()
    
    # Install Tesseract
    download_and_install_tesseract()
    
    print("\n🎉 Windows installation complete!")
    print("\n📝 Next steps:")
    print("1. Restart your terminal/command prompt")
    print("2. Set up your OpenAI API key in a .env file:")
    print("   OPENAI_API_KEY=your_api_key_here")
    print("3. Test the installation:")
    print("   python test_installation.py")
    print("4. Run the application:")
    print("   streamlit run main.py")
    print("\n💡 The application now uses GPT-4 Vision for OCR!")
    print("   - No need for complex OCR dependencies")
    print("   - Better accuracy for complex documents")
    print("   - Handles various image qualities")

if __name__ == "__main__":
    main()
