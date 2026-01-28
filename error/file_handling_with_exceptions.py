# file = open("order.txt", "w")
# file.write("Masala chai - 2 cups")
# # files take resources like memory
# # file is loaded in memory
# # it is sensitive file handling
# try:
#     file.write("MASALA CHAI -2 CUPS")
# finally:
#     file.close()
with open("./new_order.txt", "w") as file:
    file.write("Ginger tea -2 cups")
# as soon we take refernce of file
# file.__enter__() for loading in memory
# as we close
# file.__exit__() removes from memory
# with automatically handles it
