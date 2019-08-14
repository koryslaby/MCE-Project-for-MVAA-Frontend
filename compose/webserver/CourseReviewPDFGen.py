from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.platypus import Table


class CourseReviewPDFGen:


	def __init__(self):
		self.c = canvas.Canvas('MilitaryCreditEquivalencyCourseEvaluationForm.pdf')
		self.form = self.c.acroForm

	def create_table(self):
       data=  [['00', '01', '02', '03', '04'],
               ['10', '11', '12', '13', '14'],
               ['20', '21', '22', '23', '24'],
               ['30', '31', '32', '33', '34']]

	def save_form(self):
		self.c.save()



		