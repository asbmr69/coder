from agency_swarm import Agency
from Bunty import Bunty

# from dotenv import load_dotenv
# load_dotenv()
from agency_swarm import set_openai_key
set_openai_key("null")

bunty = Bunty()
#browsingAgent = BrowsingAgent()
agency = Agency([bunty],
            shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio(server_name="0.0.0.0")
    agency.run_demo()