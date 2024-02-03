import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("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")
)
file = client.files.create(
    file = open("data.pdf", "rb"),
    purpose="assistants"
)
assistant = client.beta.assistants.create(
  name = "Heal.io - BellHacks",
  description = "You are a helpful assistant who will give a diagnosis based on a user's symptoms given and also return possible drugs needed with a total itemized price for the drugs from the data.pdf by taking into consideration on average units per package and using that information to return an accurate price. Only return a diagnosis based on the symptoms within 15 words and only return the drugs included in the total cost and total cost itself. Omit all calculations only including the actual end result of the calculation. Include the total calculations for the cost of the drugs and the diagnosis all in one answer instead of dividing the it into 2 parts. Omit the cost per tablet and instead only return the total cost and include how many tablets come in the pack of the total cost. Make sure the total number of words is under 35 words.",
  model = "gpt-4-turbo-preview",
  tools = [{"type": "retrieval"}],
  file_ids = [file.id]
)
thread = client.beta.threads.create(
  messages = [
    {
      "role": "user",
      "content": "I feel tired, I have a cough, and I have a loss of apetite. What disease do I have and what drugs do I need and how much do they cost?",
      "file_ids": [file.id]
    }
  ]
)