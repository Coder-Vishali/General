import pathlib
initial_count = 0
for path in pathlib.Path(r"<enter your path here>").iterdir():
    if path.is_file():
        initial_count += 1

print(initial_count)
