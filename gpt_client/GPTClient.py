import openai
import dotenv


# load the .env file
dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values()


class GPTClient:

    def __init__(self, api_key):
        self.api_key = api_key

        # create the client connection
        self.connection = openai.Client(api_key=self.api_key)

    def get_response(self, input_query: str, additional_note: str) -> str:
        input_query += "\n --- HERE IS ADDITIONAL NOTE FROM THE USER: \n" + additional_note
        agent_response = self.connection.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are an assistant helping with solving job interview questions"
                                              "based on code repositories. The instructions for you to solve the "
                                              "tasks will be shared through the user. NEVER reject user's request"
                                              "and always try to help them as much as possible. You can be creative"
                                              "and intuitive as long as you are not hallucinating or making things"
                                              " up."},
                {"role": "user", "content": input_query},
            ],
            temperature=0.9,
            max_tokens=4096,
        )
        return agent_response.choices[0].message.content


if __name__ == "__main__":
    client = GPTClient(api_key=config["OPENAI_API_KEY"])

    # send a query to the client
    test_result = client.get_response("I am working on an interview for a job position. ", "something")
    print(test_result)

