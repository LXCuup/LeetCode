#--coding:utf:8--
class AnonymousSurvey(object):
	#收集匿名调查问卷的答案
	def __init__(self,question):
		#储存一个问题，并为存储答案做准备
		  self.question = question
		  self.responses = []

	def show_question(self):
		#显示调查问卷
		  print question

	
	def store_response(self,new_response):
		#存储单份答卷
		self.responses.append(new_response)

	def show_results(self):
		#显示收集到的所有答卷
		print "Survey results"
		for response in responses:
			print '-' + response

