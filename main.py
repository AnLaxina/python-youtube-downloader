# Importing the customtkinter library
# Using this one instead because it provides a more sleek UI
import customtkinter

# Importing the pytube library
# I import the YouTube class because I am trying to download videos.
# pytube also offers to import other classes such as Channel and Playlist.
# However, they are not needed in this case.
from pytube import YouTube

main = customtkinter.CTk()

main.mainloop()