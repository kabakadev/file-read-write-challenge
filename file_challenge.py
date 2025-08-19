"""
File Read & Write Challenge
Reads a file and writes a modified version to a new file
"""

def process_file(input_filename, output_filename):
    """Read file and write modified version"""
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Modify content (example: add line numbers and timestamp)
        lines = content.split('\n')
        modified_lines = []
        
        modified_lines.append(f"# File processed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        modified_lines.append(f"# Original file: {input_filename}")
        modified_lines.append("# Modified content below:")
        modified_lines.append("")
        
        for i, line in enumerate(lines, 1):
            modified_lines.append(f"{i:3d}: {line}")
        
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(modified_lines))
        
        print(f"✅ File processed successfully: {input_filename} -> {output_filename}")
        
    except FileNotFoundError:
        print(f"❌ Error: File '{input_filename}' not found")
    except PermissionError:
        print(f"❌ Error: Permission denied accessing '{input_filename}'")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    # Create sample input file for demonstration
    sample_content = """This is a sample file for the challenge.
It contains multiple lines.
Each line will be numbered in the output.
This demonstrates file reading and writing."""
    
    with open("sample_input.txt", "w") as f:
        f.write(sample_content)
    
    # Process the file
    process_file("sample_input.txt", "processed_output.txt")
