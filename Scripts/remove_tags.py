with open('/media/6A2CC16C2CC1343B/Projects/NLP/categorized_txt_files/609-AH/fileappend.txt') as oldfile, open('/media/6A2CC16C2CC1343B/Projects/NLP/categorized_txt_files/609-AH/newfile.txt', 'w') as newfile:
	for line in oldfile:
		if not any(bad_word in line for bad_word in bad_words):
			newfile.write(line)
