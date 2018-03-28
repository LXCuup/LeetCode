prompt = "Please add materials of your pizza:"
prompt += "\n Enter 'quit' when you are finishend. "

materials = " "
while materials != 'quit':
	materials = raw_input(prompt)
	
	if materials != 'quit':
		print materials