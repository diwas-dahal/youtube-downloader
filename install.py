import subprocess
try:
    import pytube
except:
    subprocess.check_call([sys.executable, "-m", "pip",
                           "install", "git+https://github.com/nficano/pytube"])
import pytube
import os


def is_user():
    user = os.getlogin()
    location = f'C:/Users/{user}/Desktop/Modified_Downloads'
    is_dir = os.path.isdir(location)
    if is_dir:
        return True
    else:
        return False


def download_video(url, classification):
    user = os.getlogin()
    location = ''
    youtube = ""
    while True:
        try:
            youtube = pytube.YouTube(url)
            break
        except pytube.exceptions.RegexMatchError:
            url = input("Invalid url. Please try again : ")

    if classification == "music":
        location = f'C:/Users/{user}/Desktop/Modified_Downloads/music'
    elif classification == "tutorial":
        location = f'C:/Users/{user}/Desktop/Modified_Downloads/tutorial'
    else:
        location = f'C:/Users/{user}/Desktop/Modified_Downloads/normal'

    video = youtube.streams.get_highest_resolution()
    video.download(location)
    print(f"Successfully downloaded '{video.title}' at {location}")


def create_dir():
    user = os.getlogin()
    os.mkdir(f'C:/Users/{user}/Desktop/Modified_Downloads')
    print("[Modified_Downloads] : created")
    os.mkdir(f'C:/Users/{user}/Desktop/Modified_Downloads/music')
    print("[Music]: created")
    os.mkdir(f'C:/Users/{user}/Desktop/Modified_Downloads/tutorial')
    print("[Tutorials]: created")
    os.mkdir(f'C:/Users/{user}/Desktop/Modified_Downloads/normal')
    print("[Normal]: created")


def proccess():
    url = input("Please enter the url : ")
    while True:
        classification = input("Type : ").lower()
        if classification == "tutorial":
            break
        if classification == "normal":
            break
        if classification == "music":
            break
        else:
            print("Invalid type")
    download_video(url, classification)


def main():
    is_installed = is_user()
    if is_installed:
        print("Directory verified")
        proccess()
    else:
        print("Directory not found.")
        print("Creating directory.")
        create_dir()
        print("Verified.")
        proccess()


main()
