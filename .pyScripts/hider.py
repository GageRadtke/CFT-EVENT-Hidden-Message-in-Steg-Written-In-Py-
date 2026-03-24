# created by Gage
import os

print("--- DEBUG: SCRIPT IS STARTING ---") # Add this line

def hide_secret():
    # Get the image name
    original_image = input("Enter the name of your source image (photo.jpg): ")

    # Run A check
    if not os.path.exists(original_image):
        print(f"[-] Image Not Found '{original_image}'. Please verify it's in this folder!")
        return # stop if needed

    # Get the secret message
    secret_message = input("Type the secret message you want to hide: ")
    output_image = "evidence.jpg"

    # 4. Perform the "hiding"
    with open(original_image, "rb") as f:
        data = f.read()

    with open(output_image, "wb") as f:
        f.write(data)
        f.write(b"---SECRET_START---") # marker
        f.write(secret_message.encode())
        f.write(b"---SECRET_END---") #marker

    print(f"\n[+] Success! '{output_image}' created with a hidden message.")
    print(f"[+] Your secret is now buried at the end of the file.")

if __name__ == "__main__":
    hide_secret()
