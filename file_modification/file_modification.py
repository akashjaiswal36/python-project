

def file_modification(file_path, key, value):
    with open("deployment.yaml", "r") as file:
        lines = file.readlines()

    with open("deployment.yaml", "w") as file:
        for line in lines:
            if key in line:
                file.write("        " + key + ":" + " " + "ajs3ra8/python" + ":" + value + "\n")
            else:
                file.write(line)



file_modification("deployment.yaml", "image", "10")

