# Al-ISLAMI Food Group - PDF to Excel Converter

A powerful Streamlit application for Al-ISLAMI Food Group that extracts data from PDF invoices and converts them to Excel format. Now enhanced with comprehensive OCR capabilities for scanned PDFs and secure login system!

## 🌟 Features

### 📄 PDF Processing
- **Regular PDFs**: Direct text extraction from machine-readable PDFs
- **Scanned PDFs**: Advanced OCR processing with multiple engines
- **Batch Processing**: Handle multiple PDFs simultaneously

### 🔍 OCR Capabilities
- **GPT-4 Vision API**: Primary OCR using latest AI vision models (best accuracy)
- **Multiple Fallback Engines**: Tesseract OCR as backup option
- **Image Enhancement**: Automatic preprocessing for better OCR accuracy
- **Progress Tracking**: Real-time progress updates during processing
- **Text File Export**: Save extracted text to downloadable files

### 🤖 AI Integration
- **Latest GPT Models**: GPT-4o and GPT-4o-mini support
- **Smart Error Correction**: Handles OCR artifacts and formatting issues
- **Intelligent Data Extraction**: Extracts structured data from unstructured text

### 📊 Excel Output
- **Structured Tables**: Clean, organized Excel files with standardized columns
- **Editable Interface**: Streamlit data editor for manual corrections
- **Search & Filter**: Built-in search functionality
- **Download Options**: Multiple download formats
- **File Separators**: Clear separation between multiple uploaded files

### 🔐 Security & Access
- **Secure Login**: Password-protected access system
- **User Authentication**: Dedicated login credentials
- **Session Management**: Secure user sessions
- **Branded Interface**: Al-ISLAMI Food Group branding throughout

## 🚀 Installation

### Quick Setup
```bash
# Clone the repository
git clone <repository-url>
cd kareem-pdf-to-excel-main

# Run the installation script
python install_dependencies.py

# Set up environment variables
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run the application
streamlit run main.py
```

### Manual Installation
```bash
# Install core dependencies
pip install streamlit pandas PyPDF2 openpyxl PyMuPDF openai python-dotenv

# Install OCR dependencies
pip install pytesseract opencv-python paddleocr easyocr scikit-image imageio matplotlib

# Install Tesseract OCR (system-dependent)
# Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
# macOS: brew install tesseract
# Linux: sudo apt-get install tesseract-ocr
```

## 📋 Requirements

### System Requirements
- Python 3.8+
- Tesseract OCR installed and accessible
- OpenAI API key

### Python Packages
- streamlit
- pandas
- PyMuPDF (fitz)
- openai>=1.0.0
- pytesseract>=0.3.10
- opencv-python>=4.8.0
- paddleocr>=2.7.0
- easyocr>=1.7.0
- scikit-image>=0.21.0
- And more (see requirements.txt)

## 🔐 Login Credentials

**Default Login:**
- Username: `mohamad`
- Password: `12345`

## 🔧 Usage

### 1. Login
- Enter your credentials on the login page
- Access will be granted upon successful authentication

### 2. Upload PDFs
- Drag and drop PDF files or use the file uploader
- Supports both regular and scanned PDFs
- Multiple file selection supported

### 3. Automatic Processing
- **Regular PDFs**: Direct text extraction
- **Scanned PDFs**: Automatic OCR detection and processing
- Progress tracking with real-time updates

### 4. AI Data Extraction
- Uses latest GPT models for intelligent data extraction
- Handles OCR errors and formatting issues
- Extracts structured invoice data

### 5. Review & Edit
- View extracted data in an editable table
- Search and filter functionality
- Manual corrections as needed

### 6. Export Results
- Download Excel files
- Download extracted text files
- Save processed data

## 🎯 OCR Engine Details

### GPT-4 Vision (Primary)
- **Best-in-class accuracy** for document text recognition
- Handles complex layouts, tables, and formatting
- Intelligent text extraction with context understanding
- No dependency conflicts or installation issues
- Works with various image qualities and formats

### Tesseract (Fallback)
- Industry-standard OCR engine
- Excellent for clear, high-contrast text
- Customizable configuration options
- Available when GPT Vision is not accessible

## 📝 Supported Data Fields

The application extracts the following standardized fields:
- PO Number
- Item Code
- Description
- UOM (Unit of Measure)
- Quantity
- Lot Number
- Expiry Date
- Manufacturing Date
- Promised Date
- Need by Date
- Invoice Number
- Unit Price
- Total Price
- Country
- HS Code
- Invoice Date
- Customer Number
- Payer Name
- Currency
- Supplier
- Invoice Total
- VAT
- Payment Terms
- Freight Terms

## 🔗 Links

- **Live Application**: https://inst-lpo.streamlit.app/
- **Documentation**: See this README
- **Issues**: Report bugs and feature requests

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Protobuf version conflicts (PaddleOCR/EasyOCR)**
   ```bash
   # Quick fix - run this script
   python quick_fix.py
   
   # Or manually fix
   pip uninstall protobuf paddleocr easyocr -y
   pip install protobuf<=3.20.3
   ```

2. **Tesseract not found**
   - Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
   - macOS: `brew install tesseract`
   - Linux: `sudo apt-get install tesseract-ocr`
   - Run `tesseract --version` to verify

3. **PyTorch/EasyOCR dependency issues**
   - Use GPT-4 Vision instead (recommended)
   - Run `python quick_fix.py` to switch to GPT Vision

4. **OpenAI API errors**
   - Verify your API key in the .env file
   - Check API quota and billing
   - Ensure you have access to GPT-4 Vision API

5. **All OCR engines failing**
   - Make sure your OpenAI API key is valid
   - Check internet connection
   - GPT-4 Vision should work as primary OCR

6. **Memory issues with large PDFs**
   - Process fewer files at once
   - Increase system memory if possible

### Getting Help
- Check the troubleshooting section above
- Review error messages in the application
- Ensure all dependencies are properly installed

