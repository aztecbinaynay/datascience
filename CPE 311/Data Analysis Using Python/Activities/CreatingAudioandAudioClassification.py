"""
Instructions are given to the users so the user would be able to decide whether the person being
recorded is a male or female. Another inquiry asks the user what type of family memeber is being 
recorded. The family member type shall be the name of the .wav audio file. The files are automatically
sorted to their respective folders, depending on the gender of the one being recorded.

#! path(s) should lead to a folder directory that already exists!
#? Improvement of program include: (1) automating directory creation if the folders to store the 
#? the audio files in don't exist yet.
"""

# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os

male_members = {
    "s": "son",
    "b": "brother",
    "u": "uncle",
    "f": "father",
    "n": "nephew",
    "mc": "male cousin",
    "o": "other",
}
female_members = {
    "d": "daughter",
    "s": "sister",
    "a": "aunt",
    "m": "mother",
    "n": "niece",
    "fc": "female cousin",
    "o": "other",
}
# Sampling frequency
freq = 44100

# Recording duration
duration = 60

while True:
    user = str(
        input("Do you want to record a female [f] or male [m] voice or exit[e]? ")
    )
    if user.lower() == "m":
        path = r"C:\Users\core i5\Desktop\GitHub\DataSci\Data Analysis and Tools\Dataset\male_voices"
        male = str(
            input(
                "Are you recording your son[s], brother[b], uncle[u], father[f], nephew[n], male cousin[mc], or other[o]? "
            )
        )
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait(60)
        sound_name = f"{male_members[f'{male}']}.wav"
        wv.write(os.path.join(path, sound_name), recording, freq, sampwidth=2)

    elif user.lower() == "f":
        path = r"C:\Users\core i5\Desktop\GitHub\DataSci\Data Analysis and Tools\Dataset\female_voices"
        female = str(
            input(
                "Are you recording your daughter[d], sister[s], aunt[a], mother[m], niece[n], female cousin[fc], or other[o]? "
            )
        )
        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait(60)
        sound_name = f"{female_members[f'{female}']}.wav"
        wv.write(os.path.join(path, sound_name), recording, freq, sampwidth=2)

    elif user.lower() == "e":
        print("exiting program....")
        break

    else:
        print("Unrecognized command. Try again\n")
        continue
