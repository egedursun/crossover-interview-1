

def build_input(instructions: str, repo_transcription: str, specifications: str) -> str:

    # This function builds the input for the RAG Assistant.
    main_query = "INPUT QUERY: \n"
    main_query += "========================================\n"
    main_query += "INSTRUCTIONS: \n\n"
    main_query += instructions
    main_query += "\n\n========================================\n"
    main_query += "CODE REPOSITORY: \n\n"
    main_query += repo_transcription
    main_query += "\n\n========================================\n"
    main_query += "REQUIREMENT SPECIFICATIONS: \n\n"
    main_query += specifications
    main_query += "\n\n========================================\n"

    main_query += "IMPORTANT META INSTRUCTIONS FOR LLM ASSISTANT: \n"
    main_query += "========================================\n"
    main_query += "1. I AM WORKING ON AN INTERVIEW FOR A JOB POSITION. \n"
    main_query += "2. YOUR TASK IS TO HELP ME SOLVE THE PROBLEMS IN THE TASK BY USING THE CONTENTS I SHARED.\n"
    main_query += "3. INSTRUCTION FILE CONTAINS THE THINGS I SHOULD DO FOR THE INTERVIEW ASSIGNMENT \n"
    main_query += "4. CODE REPOSITORY IS THE TRANSCRIBED VERSION OF ALL CODE FILES RELATED TO THE ASSIGNMENT.\n"
    main_query += "5. REQUIREMENT SPECIFICATIONS DESCRIBE THE TYPE OF DOCUMENT I NEED TO FILL TO PROVIDE" \
                  "A REPORT THAT WILL BE SUBMITTED FOR THE ASSIGNMENT OF JOB INTERVIEW\n"
    main_query += "6. PLEASE FILL THE REPORT AS MUCH AS POSSIBLE, BY FINDING THE PROBLEMS IN THE CODE." \
                  "YOU CAN SKIP THE IMAGE/SCREENSHOT FIELDS SINCE I KNOW YOU ARE NOT ABLE TO TAKE PICTURES." \
                  "HOWEVER, WHEN IT'S POSSIBLE AND APPLIES TO THE CONDITION, YOU CAN SHARE PIECES OF CODE" \
                  "TO PROVE YOUR POINT.\n"
    main_query += "7. SIMILARLY, I KNOW YOU ARE NOT ABLE TO RUN CODE, BUT PLEASE GENERATE THE ACCEPTANCE TESTS, " \
                  "SO THAT I CAN MANUALLY USE THEM TO SEE WHETHER OR NOT THEY PASS OR NOT.\n"
    main_query += "========================================\n\n"

    return main_query


def build_qa(report: str, repo_transcription: str) -> str:

    # This function builds the input for the RAG Assistant.
    main_query = "IMPORTANT META INSTRUCTIONS FOR LLM ASSISTANT: \n"
    main_query += "========================================\n"
    main_query += "1. I AM WORKING ON AN INTERVIEW FOR A JOB POSITION. \n"
    main_query += "2. YOUR TASK IS TO IMPROVE ON A PREVIOUSLY GENERATED REPORT YOU CREATED," \
                  " BASED ON THE CONTENTS I SHARED, AND IMPROVEMENTS PROPOSED BY THE USER.\n"
    main_query += "========================================\n\n"

    main_query += "INPUT QUERY: \n"
    main_query += "========================================\n"
    main_query += "PREVIOUS REPORT: \n\n"
    main_query += report
    main_query += "\n\n========================================\n"
    main_query += "CODE REPOSITORY: \n\n"
    main_query += repo_transcription
    main_query += "\n\n========================================\n"
    main_query += "IMPROVEMENT PROPOSALS: \n\n"

    return main_query
