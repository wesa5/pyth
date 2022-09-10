
PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt" ) as name_file:
    names = name_file.readlines()
    #print(names)

with open("./input/letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./output/Ready_to_send/invite_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
