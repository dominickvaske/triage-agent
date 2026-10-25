import anthropic 
import data
import json

TOOLS = [
    {
        "name": "get_incident_history",
        "description": "Get previous maintenance for an asset. Use this to see if a problem is recurring.",
        "input_schema": {
            "type": "object",
            "properties": {
                "asset_id": {"type":"string", "description":"Asset ID like GEN-04"}
            },
            "required": ["asset_id"],
        }
    },
    {
        "name": "asset_lookup",
        "description": "Get a list of assets with identifying information like location in a dictionary",
        "input_schema": {
            "type": "object",
            "properties": {},
        }
    }
]

def asset_lookup():
    return json.dumps(data.ASSETS)

def get_incident_history(asset_id):
    output = []
    for incident in data.PAST_INCIDENTS:
        if incident["asset_id"] == asset_id:
            output.append(incident)
    
    return json.dumps(output)

# switches on the correct tool to run
def run_tool(tool_name, tool_input):
    if tool_name == "get_incident_history":
        return get_incident_history(tool_input["asset_id"])
    elif tool_name == "asset_lookup":
        return asset_lookup()

# first message to send to claude as a user
messages =  [{
        "role": "user",
        "content": data.REPORTS[0],
    }]

client = anthropic.Anthropic()

# model loop to handle the back and forth of conversation
while True:
    # send new msg to claude and get response
    response = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1024,
        system="You are a concise dispatch reviewer. Review report and assign priority and procedure for investigation.",
        messages= messages,
        tools=TOOLS, # passes menu of tools
    )

    # append msg to messages/transcript list as an assistant
    messages.append({"role":"assistant", "content": response.content})

    # claude is done, print response and break from loop
    if response.stop_reason == "end_turn":
        break
    
    # claude wants to call a tool
    if response.stop_reason == "tool_use":
        tool_results = []

        # find the block of content and run correct tool
        for block in response.content:
            if block.type == "tool_use":
                print("CALL: ", block.name, block.input) # what Claude asked for

                # generic function to find correct tool to run
                output = run_tool(block.name, block.input)

                print("RESULT:", output)    # what I'm sending back to Claude

                # send result of tool run back to agent
                tool_results.append({"type":"tool_result",
                                     "tool_use_id": block.id,
                                     "content": output})

        messages.append({"role": "user", "content": tool_results})


# print response from model
for block in response.content:
    if block.type == "text":
        print(block.text)
