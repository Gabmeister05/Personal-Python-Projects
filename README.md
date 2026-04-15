# URL Decoder
This repository contains a Python program for decoding and gridding ascii via google docs url and the cartesian coordinate system.

## How to run

Simple and straightforward, when the program is run it'll ask for a url

If you're going to run this program, I suggest to install the following libraries: requests and BeautifulSoup

E.g. `pip install requests beautifulsoup4`

Here's how the program works

1) It'll ask you for a url
- Ex: "Enter the URL containing the secret message table: "
- Here, you can either type out the url or the fast is to copy that url and paste it
- **NOTE**: The url should be a google doc that contains a table with x and y coordinates
- I.e. 'https://docs.google.com/document/d/[Document_ID]/edit'

2)
That's all! After you enter in your desired google doc url, the program will parse the data and will decode the message in upper case letters

Have fun :)
