"""
Your module description
"""
def open_file(filename):

  try:

    f=open("files/"+filename,"r")

    print("Filename:",f.name)

    print("Contents of File")

    lines=f.readlines()

    for line in lines:

      print(line, end=" ")

    f.close()

  except FileNotFoundError as e:

      print(f"FileNotFoundError successfully handled\n"

            f"{e}")

  except IOError as ioe:

      print(f"IOError successfully handled\n"

            f"{ioe}")

  else:

    print("No exception occurred")

  

  finally:

    print("Finally always executed")