# {
#     "Records": [
#         {
#             "keywords": "apple",
#             "limit": 5,
#             "color": "green",
#             "print_urls": true
#         },
#         {
#             "keywords": "universe",
#             "limit": 15,
#             "size": "large",
#             "print_urls": true
#         }
#     ]
# }

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images