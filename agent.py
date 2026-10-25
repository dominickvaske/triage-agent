import anthropic
from data import REPORTS

client = anthropic.Anthropic()

msg = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    system="You are a concise dispatch reviewer. Review report and assign priority and procedure for investigation.",
    messages=[{
        "role": "user",
        "content": REPORTS[0],
    }]
)

for block in msg.content:
    if block.type == "text":
        print(block.text)
