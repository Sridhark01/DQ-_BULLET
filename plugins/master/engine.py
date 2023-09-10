import openai

async def ai(query):
    openai.api_key = "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" #Your openai api key
    response = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=100, n=1, stop=None, temperature=0.9, timeout=5)
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f"ᴀsᴋᴇᴅ ʙʏ📫: {message.from_user.mention}\nǫᴜᴇʀʏ🔖: {question}\n\n{response}")
    except Exception as e:
        # Handle other errors
        error_message = f"An error occurred: {e}"
        await m.edit(error_message)
