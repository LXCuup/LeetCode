#--coding:utf:8--
responses = {}
i = 1
while i < 3:
	def show_question():
		#显示调查问卷
		question = raw_input("question: ")

		
	def store_response():
		#存储单份答卷
		response = raw_input("answer: ")


	responses['question'] = 'response'

	i = i + 1

def show_results():
	#显示收集到的所有答卷
	for q,a in responses.items():
		print "%r\n%r" %(q,a)

show_question()
store_response()
show_results()