import os
import pygame
from pygame import mixer

# Initialize pygame and mixer
pygame.init()
mixer.init()

# Function to list all MP3 files in a directory
def list_mp3_files(directory):
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

# Function to create a playlist
def create_playlist():
    playlist = []
    while True:
        print("Add MP3 files to your playlist:")
        mp3_files = list_mp3_files('.')
        for i, file in enumerate(mp3_files):
            print(f"{i + 1}. {os.path.basename(file)}")
        print("0. Done")
        choice = input("Enter the number of the MP3 file to add (0 to finish): ")
        if choice == '0':
            break
        elif choice.isdigit() and 0 < int(choice) <= len(mp3_files):
            playlist.append(mp3_files[int(choice) - 1])
        else:
            print("Invalid choice. Please select a valid number.")
    return playlist

# Function to play a playlist
def play_playlist(playlist):
    mixer.music.stop()
    for song in playlist:
        mixer.music.load(song)
        mixer.music.play()
        print(f"Now playing: {os.path.basename(song)}")
        while pygame.mixer.music.get_busy():
            pass

# Main loop
while True:
    print("\nMusic Player Menu:")
    print("1. Create Playlist")
    print("2. Play Playlist")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        playlist = create_playlist()
    elif choice == '2':
        if 'playlist' in locals():
            play_playlist(playlist)
        else:
            print("Please create a playlist first.")
    elif choice == '3':
        mixer.quit()
        pygame.quit()
        print("Thanks Namasthe!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
