from transcriber.transcriber_processor import transcribe_code_repository


def read_instructions(filename: str) -> str or None:
    # This function reads the instructions from the file and returns a list of instructions.
    # Each instruction is a string.
    complete_filename = "instruction_files/" + filename
    instructions = None
    try:
        with open(complete_filename, "r") as file:
            instructions = file.read()
    except FileNotFoundError as e:
        print(f"Instruction file ({complete_filename}) is not found. "
              f"Please check the file name and try again.")

    return instructions


def read_code_repository(filename: str) -> str or None:
    complete_filename = "code_repositories/" + filename
    content = transcribe_code_repository(complete_filename)
    return content


def read_requirement_specifications(filename: str) -> str or None:
    # This function reads the requirement specifications from the file and returns a list of requirements.
    # Each requirement is a string.
    complete_filename = "requirement_specifications/" + filename
    requirements = None
    try:
        with open(complete_filename, "r") as file:
            requirements = file.read()
    except FileNotFoundError as e:
        print(f"Requirement specification file ({complete_filename}) is not found. "
              f"Please check the file name and try again.")

    return requirements


def read_report(filename: str) -> str or None:
    # This function reads the report from the file and returns a list of reports.
    # Each report is a string.
    complete_filename = "generated_reports/" + filename
    reports = None
    try:
        with open(complete_filename, "r") as file:
            reports = file.read()
    except FileNotFoundError as e:
        print(f"Report file ({complete_filename}) is not found. "
              f"Please check the file name and try again.")

    return reports


if __name__ == "__main__":
    test_instructions = read_instructions("001.txt")
    test_code_repository = read_code_repository("001")
    test_requirement_specifications = read_requirement_specifications("001.txt")
    # print(test_instructions)
    # print(test_code_repository)
    # print(test_requirement_specifications)
