import itertools

def gather_info():
    print("=== Wordlist Generator ===")
    print("Provide details below (leave blank to skip any field):")
    
    # Collect basic information
    name = input("Person's name: ").strip()
    birthday = input("Birthday (DDMMYYYY or MMDDYYYY): ").strip()
    address = input("Address/City/Location: ").strip()
    related_names = input("Related people's names (comma-separated): ").strip()
    extra_words = input("Any extra words (comma-separated): ").strip()
    
    # Collect all inputs into a single list
    base_words = [name, birthday, address]
    if related_names:
        base_words.extend(related_names.split(","))
    if extra_words:
        base_words.extend(extra_words.split(","))
    
    # Remove duplicates, empty strings, and clean up spaces
    base_words = list(set(word.strip() for word in base_words if word.strip()))
    
    return base_words

def generate_combinations(base_words, min_length=6, max_length=12):
    print("\nGenerating combinations... This might take a while for larger wordlists.")
    wordlist = set()
    
    # Generate permutations and append numbers for variations
    for length in range(1, len(base_words) + 1):
        for combination in itertools.permutations(base_words, length):
            combined = ''.join(combination)
            if min_length <= len(combined) <= max_length:
                wordlist.add(combined)
    
    # Add variations with numbers appended (e.g., "name123")
    for word in base_words:
        for number in range(0, 100):
            variation = f"{word}{number}"
            if min_length <= len(variation) <= max_length:
                wordlist.add(variation)
    
    return wordlist

def save_wordlist(wordlist, filename="wordlist.txt"):
    print(f"\nSaving wordlist to {filename}...")
    with open(filename, "w") as file:
        for word in sorted(wordlist):
            file.write(word + "\n")
    print(f"Wordlist saved successfully! Total words: {len(wordlist)}")

def main():
    base_words = gather_info()
    if not base_words:
        print("No information provided. Exiting.")
        return
    
    # Prompt user for wordlist length preferences
    try:
        min_length = int(input("Minimum password length (default 6): ") or 6)
        max_length = int(input("Maximum password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input for lengths. Using default values (6-12).")
        min_length, max_length = 6, 12
    
    wordlist = generate_combinations(base_words, min_length, max_length)
    save_wordlist(wordlist)
    print("\nProcess complete!")

if __name__ == "__main__":
    main()
