from datetime import datetime

import dotenv

from builder.builder_processor import build_input
from gpt_client.GPTClient import GPTClient
from reader.reader_processor import read_instructions, read_code_repository
import tiktoken

# load the .env file
dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


if __name__ == "__main__":

    print("\n\n========================================")
    print("    CROSSOVER - RAG ASSISTANT EMULATOR  ")
    print("========================================")
    print("")
    print("This is a simple emulator for the Crossover RAG Assistant.")
    print("It is intended to be used for testing and development purposes.")
    print("")
    print("========================================")
    print("")
    print("Please provide the file name for the instructions, in .txt format "
          "(You need to paste the instruction file inside /instruction_files path): ")
    instruction_path = input()
    print("Please provide the main directory for the code repository that will be Q/A'd "
          "(You need to paste the code repository inside /code_repositories path): ")
    code_repository_path = input()
    print("Please provide the file name for the requirement specification file, in .txt format "
          "(You need to paste the requirement specification file inside /requirement_specifications path): ")
    requirement_specification_path = input()
    print("")
    print("========================================")
    print("")
    print("* The emulator will now run the RAG Assistant.")
    print("* Please wait until the process is finished.")
    print("* The output file will be generated inside /generated_reports path.")
    print("   --- The default name for the output file will be 'report_YYYY-MM-DD_HH-MM-SS.txt', where "
          "YYYY-MM-DD_HH-MM-SS is the current date and time.")
    print("")
    print("========================================")

    # read the instructions
    instructions = read_instructions(instruction_path)

    # read the code repository
    code_repository = read_code_repository(code_repository_path)

    # read the requirement specification
    requirement_specification = read_instructions(requirement_specification_path)

    # build the input
    input_query = build_input(instructions, code_repository, requirement_specification)

    # print the input
    print("========================================")
    print(input_query)
    print("========================================")

    # calculate the token
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(input_query))
    print("========================================")
    print(f"Number of tokens: {(num_tokens // 1000) + 4}K tokens.")
    print(f"Approximate Cost: ${((num_tokens // 1000) * 0.01) + (4.096 * 0.03)}.")
    print("========================================")

    # send the query to the client
    client = GPTClient(api_key=config["OPENAI_API_KEY"])
    result = client.get_response(input_query, "N/A")

    print("==============00100==========================")
    print("The RAG Assistant has finished processing the input.")
    print("========================================")

    # print the result
    print("========================================\n\n")
    print(result)
    print("\n\n========================================")

    # write the result to a file
    try:
        current_date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"generated_reports/report_{current_date_time}.txt", "w") as f:
            f.write(result)
    except Exception as e:
        print("========================================")
        print("The RAG Assistant has failed to write the output to a file.")
        print("========================================")
        print(e)
        print("========================================")

