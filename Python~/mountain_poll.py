# --coding:utf-8--
responses = {}
#设置一个标志，指出调查是否继续
polling_avtive = True

while polling_avtive:
	#提示输入被调查者的名字和回答
	name = raw_input("\nWhat is your name? ")
	response = raw_input("which mountain would you like to climb someday? ")

	#将答案存储在字典中
	responses[name] = response

	#看看是否还有人要参与调查
	repeat = raw_input("would you like to let another person respond?(yes/no) ")
	if repeat == 'no':
		polling_avtive = False

#调查结束，显示结果
print "\n ---Poll Results---"
for name,response in responses.items():
	print name + " would like to climb " + response + "."