import filetype
import os

files = os.listdir("./")

fc = 0
for i in range(len(files)):
    kind = filetype.guess(files[i])
    if kind is None:
        print("None")
    else:
        print(f"File Extension: {kind.extension}")
        print(f"File MIME Type: {kind.mime}")
    if kind is not None:
        ext = kind.extension 
        if ext == "pdf":
            os.rename(files[i], f"Document {fc}.pdf")
            fc += 1