from service.cnbc.url_list import start as cnbc_start
from service.cnn.url_list import start as cnn_start

print("Starting scraping")
print("=====================================")
print("Selecting service")
print("1. CNBC Indonesia")
print("2. CNN Indonesia")
print("=====================================")
choice = input("Select service: ")
total_loop = int(input("Input total loop: "))
if choice == '1':
    cnbc_start(total_loop)
elif choice == '2':
    cnn_start(total_loop)
