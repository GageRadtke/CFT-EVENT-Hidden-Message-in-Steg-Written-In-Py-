# written by Gage
import os

def find_secret():
Get the image to scan
    target_image = input("Enter the image to scan (jpg): ")

    if not os.path.exists(target_image):
        print(f"[-] File '{target_image}' not found.")
        return

    #Define markers 
    START_MARKER = b"---SECRET_START---"
    END_MARKER = b"---SECRET_END---"

    # Read the image as binary
    with open(target_image, "rb") as f:
        data = f.read()

    # Search for the markers
    start_index = data.find(START_MARKER)
    end_index = data.find(END_MARKER)

    # Extract and display
    if start_index != -1 and end_index != -1:
        secret_data = data[start_index + len(START_MARKER) : end_index]
        message = secret_data.decode()
        print(f"\n[+] Found Secret Message: {message}")
    else:
        print("\n[-] No hidden message found with those markers.")

if __name__ == "__main__":
    find_secret()