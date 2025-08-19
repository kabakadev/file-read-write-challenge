"""
Combined Demo Script
Demonstrates both file processing and error handling
"""

from file_challenge import process_file
from error_handling_lab import safe_file_reader, create_test_files
import os

def main():
    print("🚀 File Operations Assignment Demo")
    print("=" * 50)
    
    # Create test environment
    create_test_files()
    
    # Demonstrate file processing
    print("\n📝 File Read & Write Challenge Demo:")
    process_file("test1.txt", "modified_test1.txt")
    
    print("\n🧪 Error Handling Lab Demo:")
    print("(Test files created for interactive testing)")
    
    # Show what files were created
    created_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    print(f"\n📂 Files available for testing: {', '.join(created_files)}")
    
    print("\n💡 Run 'python error_handling_lab.py' for interactive demo")

if __name__ == "__main__":
    main()
