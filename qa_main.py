from datetime import datetime

import dotenv
import tiktoken

from builder.builder_processor import build_qa
from gpt_client.GPTClient import GPTClient
from reader.reader_processor import read_code_repository, read_report

# load the .env file
dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


if __name__ == "__main__":

    print("\n\n========================================")
    print("    CROSSOVER - RAG ASSISTANT Q/A EMULATOR ")
    print("========================================")
    print("")
    print("This is a simple Q/A emulator for the Crossover RAG Assistant.")
    print("It is intended to be used for testing and development purposes.")
    print("")
    print("========================================")
    print("")
    print("Please provide the file name for the report, in .txt format "
          "(You need to paste the instruction file inside /generated_reports path): ")
    report_path = input()
    print("Please provide the main directory for the code repository that will be Q/A'd "
          "(You need to paste the code repository inside /code_repositories path): ")
    code_repository_path = input()

    print("")
    print("========================================")
    print("")
    print("* The emulator will now run the Q/A assistant.")
    print("* Please wait until the process is finished.")
    print("* The output file will be generated inside /improved_reports path.")
    print("   --- The default name for the output file will be 'improved_report_YYYY-MM-DD_HH-MM-SS.txt', where "
          "YYYY-MM-DD_HH-MM-SS is the current date and time.")
    print("")
    print("========================================")

    # read the report
    report_data = read_report(report_path)

    # read the code repository
    code_repository = read_code_repository(code_repository_path)

    # build the input
    input_query = build_qa(report_data, code_repository)

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

    # basic improvements
    whole_report = ""
    for i in range(2):
        input_query += f"\n *** ENHANCE, IMPROVE, AND ELABORATE ON THE PROBLEM-{i+1}'s SOLUTION, AND PROVIDE " \
                       f"MUCH MORE DETAIL AND IMMENSE DEPTH WHILE" \
                       "PROVIDING THE ANSWER. DO NOT TRY TO PROVIDE A SHORT ANSWER, AS LONG AS YOU ARE GIVING" \
                       "IMPORTANT OR POTENTIALLY IMPORTANT INFORMATION, YOU MUST INCLUDE IT IN YOUR RESPONSE ***\n"

        # send the query to the client
        improvement = client.get_response(input_query, "")
        whole_report += improvement + "\n\n"

    # print the result
    print("========================================\n\n")
    print(whole_report)
    print("\n\n========================================")

    # save the result
    try:
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with open(f"improved_reports/improved_report_{current_time}.txt", "w") as file:
            file.write(whole_report)
    except Exception as e:
        print("========================================")
        print("The RAG Assistant has failed to write the output to a file.")
        print("========================================")
        print(e)


