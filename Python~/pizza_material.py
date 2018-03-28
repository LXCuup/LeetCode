prompt = "Please add materials of your pizza:"
prompt += "\n Enter 'quit' when you are finishend. "

materials_list = []
active = True
while active:
	material = raw_input(prompt)
	
	if material == 'quit':
		active = False
	else:
		materials_list.append(material)
		for ma in materials_list:
		    print ma