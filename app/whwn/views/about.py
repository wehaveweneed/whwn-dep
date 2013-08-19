import json
from django.views.generic import TemplateView
 
class AboutView(TemplateView):
	template_name="about.html"
	
	def get_context_data(self, **kwargs):
		context = super(AboutView, self).get_context_data(**kwargs)
		with open("about.json",'rb') as fp:
			data= json.load(fp)
			context["team"]=data["team"]
		return context


