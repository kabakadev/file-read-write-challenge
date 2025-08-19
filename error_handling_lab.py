"""
Error Handling Lab
Asks user for filename and handles various error conditions
"""

import os
from pathlib import Path

def safe_file_reader():
    """Interactive file reader with comprehensive error handling"""
    
    while True:
        try:
            filename = input("Enter filename to read (or 'quit' to exit): ").strip()
            
            if filename.lower() == 'quit':
                print("👋 Goodbye!")
                break
            
            if not filename:
                print("⚠️ Please enter a valid filename")
                continue
            
            # Check if file exists
            if not os.path.exists(filename):
                print(f"❌ Error: File '{filename}' does not exist")
                
                # Suggest similar files in current directory
                current_files = [f for f in os.listdir('.') if os.path.isfile(f)]
                similar_files = [f for f in current_files if filename.lower() in f.lower()]
                
                if similar_files:
                    print("💡 Did you mean one of these?")
                    for f in similar_files[:3]:  # Show max 3 suggestions
                        print(f"   - {f}")
                continue
            
            # Check if it's actually a file (not directory)
            if os.path.isdir(filename):
                print(f"❌ Error: '{filename}' is a directory, not a file")
                continue
            
            # Try to read the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                
            print(f"\n✅ Successfully read '{filename}'")
            print(f"📊 File stats:")
            print(f"   - Size: {len(content)} characters")
            print(f"   - Lines: {len(content.splitlines())}")
            print(f"   - Words: {len(content.split())}")
            
            # Show first few lines
            lines = content.splitlines()
            print(f"\n📖 First {min(5, len(lines))} lines:")
            for i, line in enumerate(lines[:5], 1):
                print(f"   {i}: {line}")
            
            if len(lines) > 5:
                print(f"   ... and {len(lines) - 5} more lines")
                
        except PermissionError:
            print(f"❌ Error: Permission denied - cannot read '{filename}'")
        except UnicodeDecodeError:
            print(f"❌ Error: Cannot decode '{filename}' as text file (might be binary)")
        except IsADirectoryError:
            print(f"❌ Error: '{filename}' is a directory")
        except OSError as e:
            print(f"❌ System error reading '{filename}': {e}")
        except KeyboardInterrupt:
            print("\n\n⏹️ Operation cancelled by user")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        print()  # Empty line for readability

def create_test_files():
    """Create some test files for demonstration"""
    test_files = {
        "test1.txt": "Hello World!\nThis is a test file.",
        "test2.txt": "Another test file\nwith multiple lines\nfor testing purposes.",
        "empty.txt": "",
        "numbers.txt": "\n".join([f"Line {i}" for i in range(1, 11)])
    }
    
    for filename, content in test_files.items():
        with open(filename, "w") as f:
            f.write(content)
    
    print("📁 Created test files: " + ", ".join(test_files.keys()))

if __name__ == "__main__":
    print("🧪 Error Handling Lab")
    print("=" * 50)
    
    # Create test files
    create_test_files()
    print()
    
    # Run the interactive file reader
    safe_file_reader()
