"""
Testing code for the math quiz

"""
import requests

# Example file for testing
url = "https://raw.githubusercontent.com/AltraMage/NineLetterWordPoints/main/background.js"


def steal_file(url, filename):
    try:
        data = requests.get(url)  # Probably should have something to wait for this to finish, but idk async
    except requests.ConnectionError:
        print("Check your network, proceding without connection. Please note, certain functionality may not work")
    if data.status_code == 200:  # 200? Oll Korrect!
        with open(filename, "wb") as file:
            # write to the file in binary, so you can do images and such
            file.write(data.content)
    else:
        print("Failed. Please check ur internets")
        code = data.status_code
        print(f"Error code is {code}, if you care that is")
        # Give user to option to get more info of error code
        print(f"https://en.wikipedia.org/wiki/HTTP_{code}")


if __name__ == "__main__":
    steal_file(url)