#criar arquivo para cache
#criar função para armazenar comentários


class Data:
	def __init__(self):
		self.index = 0
	
	def comment(self):
		opcao = self.get_choice()
		
		while opcao != '1':
			id = self.get_cache()
			textfile = f'comment{id}.txt'
			with open(textfile, 'wt') as text:
				text.write(opcao)
		self.comment()
			
			#if self.get_choice() == '1':
			#break
	
	
	def get_cache(self):
		self.rec = open('cache.txt', 'r')
		for index in self.rec:
			self.index = 0
			self.index = int(index)+1
			self.rec_w = open('cache.txt', 'wt')
			self.string = str(self.index)
			self.rec_w.write(self.string)
		return self.index
			
			
	def get_choice(self):
		self.option = input("digite um comentário ou 1 para sair:  ")
		return self.option
		
if __name__=='__main__':
	com = Data()
	com.comment()
	
		
		
			
		