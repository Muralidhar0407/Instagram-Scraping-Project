import instaloader

username = input("Enter the Instagram username: ")

loader = instaloader.Instaloader()

try:
    profile = instaloader.Profile.from_username(loader.context, username)
    
    print("Username:", profile.username)
    print("Full Name:", profile.full_name)
    print("Bio:", profile.biography)
    print("Followers:", profile.followers)
    print("Following:", profile.followees)
    print("Posts Count:", profile.mediacount)
except instaloader.exceptions.ProfileNotExistsException:
    print("The given username does not exist.")