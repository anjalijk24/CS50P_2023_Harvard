filename = input("File name: ").strip().casefold()

suffix = filename.rsplit('.', maxsplit=1)

if filename.endswith(("gif", "jpg", "jpeg", "png")):
   print("image/",suffix[1], sep='')
elif filename.endswith(("pdf", "zip")):
   print("application/",suffix[1], sep='')
elif filename.endswith("txt"):
   print("text/",suffix[0], sep='')
else:
    print("application/octet-stream")

#NOTE:
#I ran check50 which returned the following errors:
#:( input of happy.jpg yields output of image/jpeg
#:( input of zipper.jpg, with another extension name, yields output of image/jpeg
#I don't know what's wrong here because I get the expected answers when I execute 'python extensions.py'
#If someone is checking this assignment, it would be nice to get feedback