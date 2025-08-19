# File Operations Assignment

Automated submission for file read/write challenge and error handling lab.

## 📋 Assignment Components

### 1. File Read & Write Challenge 🖋️
**File**: `file_challenge.py`

Reads a file and creates a modified version with:
- Timestamp header
- Line numbers
- Original filename reference

### 2. Error Handling Lab 🧪  
**File**: `error_handling_lab.py`

Interactive program that:
- Prompts for filename input
- Handles file not found errors
- Handles permission errors  
- Provides helpful error messages
- Suggests similar filenames

## 🚀 Usage

### Quick Demo
```bash
python demo.py
```

### File Processing
```bash
python file_challenge.py
```

### Interactive Error Handling
```bash
python error_handling_lab.py
```

## 📁 Files Generated

- `sample_input.txt` - Demo input file
- `processed_output.txt` - Modified output file  
- `test1.txt`, `test2.txt`, `empty.txt`, `numbers.txt` - Test files

## ✨ Features

- ✅ Comprehensive error handling
- ✅ User-friendly error messages
- ✅ File suggestions for typos
- ✅ File statistics display
- ✅ Automated test file creation
- ✅ Cross-platform compatibility

## 📊 Error Handling Coverage

- `FileNotFoundError` - File doesn't exist
- `PermissionError` - No read/write access
- `IsADirectoryError` - Target is directory
- `UnicodeDecodeError` - Binary file handling
- `KeyboardInterrupt` - Graceful exit
- Generic `Exception` - Catch-all handler

---
*Generated on 2025-08-19 21:40:32*
