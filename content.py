# -*- coding: utf-8 -*-


import re, csv


class Open():

	def compile_content(self):
	
		# Vida content cards
		f = open('content_cards_v1.csv', 'rU')

		csv_f = csv.reader(f, dialect=csv.excel)

		contentList = []
		csv_f.next()

		for row in csv_f:

			# content array holds one row from CSV and clears each time through the loop to hold new row
			content = []

			for item in row:
				content.append(item)

			contentList.append(content)

		f.close()

		return contentList



class Classifier():

	def match(self, content_data):

		row_list = [[1711,"How to find a new fitness fitness fitness fitness gym that will work for you","<p>In general, I like fitness and new things.</p>","https://www.vida.com/content/how-to-find-a-gym-that-will-work-for-you","fitness","new","gym"],[1711,"How to find a gym that will work for you","<p>Finding a gym is a fun and an exciting part of your health journey. When looking for a gym consider what is important to you. There are many gyms out there from the bare bones gym to the full service athletic club. For example you may want access to a pool and jacuzzi, classes that are included in your membership, specific exercise equipment or child care services.</p>","https://www.vida.com/content/how-to-find-a-gym-that-will-work-for-you","General fitness","new","gym"]]	
	
		
		keywords_per_article = []

		for row in content_data:
			content = [row[1],row[2],row[3]]
			keywords = [row[4],row[5],row[6]]
			result_list = []
			
			for keyword in keywords:
				keyword = keyword.strip().lower().replace('new/', '').replace('new\\', '')
				
				keyword_total = 0
				
				for content_item in content:
					content_item = content_item.lower()
					if not keyword:
						keyword_total += 0
					else:
					  keywords_found = re.findall(keyword, content_item)
					  keyword_total += len(keywords_found)
					  
				row.append(keyword_total)  
				
		#Returns as follows [article number, title, content, permalink, cat1, cat2, cat3, cat1 #, cat2 #, cat3 #]
		print content_data
				
#class Writer():



open_file = Open()
compile_content = open_file.compile_content()


classify_file = Classifier()
result = classify_file.match(compile_content)