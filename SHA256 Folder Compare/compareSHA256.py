import os
import hashlib

def calculate_sha256(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def get_files_with_hashes(folder):
    """Return a dictionary of file names and their SHA-256 hashes."""
    files_hashes = {}
    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        return files_hashes
    
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, folder)  # Normalize relative path
            files_hashes[relative_path] = calculate_sha256(file_path)
    return files_hashes

def compare_folders(folder1, folder2):
    """Compare SHA-256 hashes of all files in two folders."""
    hashes1 = get_files_with_hashes(folder1)
    hashes2 = get_files_with_hashes(folder2)
    
    all_files = set(hashes1.keys()).union(set(hashes2.keys()))
    
    different_files = []
    only_in_folder1 = []
    only_in_folder2 = []
    
    for file in all_files:
        hash1 = hashes1.get(file)
        hash2 = hashes2.get(file)
        
        if hash1 is None:
            only_in_folder2.append(file)
        elif hash2 is None:
            only_in_folder1.append(file)
        elif hash1 != hash2:
            different_files.append(file)
    
    print("Comparison Results:")
    print("==================")
    if different_files:
        print("Files with different content:")
        for file in different_files:
            print(f"  {file}")
    else:
        print("No differing files found.")
    
    if only_in_folder1:
        print("\nFiles only in", folder1, ":")
        for file in only_in_folder1:
            print(f"  {file}")
    if only_in_folder2:
        print("\nFiles only in", folder2, ":")
        for file in only_in_folder2:
            print(f"  {file}")

if __name__ == "__main__":
    folder1 = input("Enter the first folder path: ").strip()
    folder2 = input("Enter the second folder path: ").strip()
    compare_folders(folder1, folder2)
