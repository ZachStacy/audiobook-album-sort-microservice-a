# Author: Zach Stacy
# GitHub username: Zachstacy
# Date: 11-13-24
# Description: Microservice server that categorizes audio folders and sends a confirmation back to the client.

import os
import zmq
from mutagen.mp3 import MP3
import time

# Wait for a brief period before processing the file
time.sleep(2)  # Delay for 2 seconds


def categorize_audio_folders(directory_path):
    results = {}
    duration_threshold = 600  # 10 minutes

    for folder_name in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, folder_name)

        if os.path.isdir(folder_path):
            category = "Album"          # default each to be album unless conditions below true

            if any("chapter" in subfolder.lower() for subfolder in os.listdir(folder_path)):
                category = "Audiobook"
            else:
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)

                    if file_name.lower().endswith(".mp3"):
                        try:
                            audio = MP3(file_path)
                            duration = audio.info.length

                            if duration > duration_threshold:
                                category = "Audiobook"          # if any mp3 > 10 minutes, assumed audiobook file
                                break
                        except Exception as e:
                            print(f"Error processing {file_path}: {e}")
            results[folder_name] = category

    # Write the results to output.txt
    with open("output.txt", "w") as f:
        for folder, category in results.items():
            f.write(f"{folder}: {category}\n")

    # Clear the input.txt file after processing
    with open("input.txt", "w") as f:
        f.write("")

    return "Processing complete, results written to output.txt"

# Set up ZeroMQ context and REP socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Server is waiting to receive directory paths from the client...")

# Infinite loop to keep the server running
while True:
    directory_path = socket.recv_string()
    print(f"Received directory path: {directory_path}")

    # Run the categorization function
    response_message = categorize_audio_folders(directory_path)

    # Send a confirmation back to the client
    socket.send_string(response_message)
    print(response_message)

# Clean up the ZeroMQ context
context.destroy()