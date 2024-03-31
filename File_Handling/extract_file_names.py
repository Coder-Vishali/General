import os

def generate_annoate(folder):
    for root, dirs, files in os.walk(folder, topdown=False):
        total_context_text = os.path.splitext(os.path.join(root, 'output'))[0] + ".txt"
        output_file = open(total_context_text, 'a')
        for name in files:
            print("file name", name)
            output_file.write(name)
            output_file.write("\n")
    output_file.close()

if __name__ == '__main__':
    generate_annoate(r'<Path_to_that_folder>')
