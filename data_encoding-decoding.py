import base64

def encode_text():
    text = input("Enter text to encode: ")
    encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    print("Encoded:", encoded)

def decode_text():
    encoded = input("Enter Base64 to decode: ")
    
    try:
        # Fix padding if missing
        encoded += '=' * (-len(encoded) % 4)
        
        decoded = base64.b64decode(encoded).decode('utf-8')
        print("Decoded:", decoded)
        
    except Exception:
        print("Invalid Base64 input!")

def main():
    while True:
        print("\n===== Base64 Tool =====")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == '1':
            encode_text()
        elif choice == '2':
            decode_text()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()