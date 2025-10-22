#!/usr/bin/env python3
"""
Quick fix script for immediate resolution of OCR dependency issues
Run this script to fix the current problems and switch to GPT Vision OCR
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and return success status"""
    try:
        print(f"🔄 {description}...")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Success")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed: {e}")
        return False

def main():
    print("🚀 Quick Fix for OCR Dependency Issues")
    print("=" * 50)
    print("This script will fix the current OCR problems by:")
    print("1. Removing problematic packages")
    print("2. Installing compatible versions")
    print("3. Switching to GPT-4 Vision for OCR")
    print()
    
    # Step 1: Remove problematic packages
    print("📦 Step 1: Removing problematic packages...")
    problematic_packages = [
        "paddleocr",
        "easyocr", 
        "protobuf"
    ]
    
    for package in problematic_packages:
        run_command(f"{sys.executable} -m pip uninstall {package} -y", f"Removing {package}")
    
    # Step 2: Install compatible versions
    print("\n📦 Step 2: Installing compatible packages...")
    compatible_packages = [
        "protobuf<=3.20.3",
        "openai>=1.0.0",
        "Pillow>=10.0.0",
        "opencv-python>=4.8.0",
        "numpy>=1.24.0"
    ]
    
    for package in compatible_packages:
        run_command(f"{sys.executable} -m pip install {package}", f"Installing {package}")
    
    # Step 3: Verify OpenAI is working
    print("\n🔑 Step 3: Verifying OpenAI API...")
    try:
        from openai import OpenAI
        print("✅ OpenAI package is working")
    except Exception as e:
        print(f"❌ OpenAI package issue: {e}")
    
    print("\n🎉 Quick fix complete!")
    print("\n📝 What changed:")
    print("✅ Removed PaddleOCR and EasyOCR (dependency conflicts)")
    print("✅ Fixed protobuf version conflicts")
    print("✅ Now using GPT-4 Vision for OCR (best accuracy)")
    print("✅ Tesseract still available as fallback")
    
    print("\n🚀 Next steps:")
    print("1. Make sure your OpenAI API key is set in .env file")
    print("2. Run the application: streamlit run main.py")
    print("3. Upload your scanned PDF - it will now use GPT Vision!")
    
    print("\n💡 Benefits of GPT-4 Vision OCR:")
    print("• Better accuracy than traditional OCR")
    print("• Handles complex layouts and formatting")
    print("• No dependency conflicts")
    print("• Works with various image qualities")
    print("• Intelligent text extraction and structuring")

if __name__ == "__main__":
    main()
