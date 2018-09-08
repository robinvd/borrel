from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic.base import TemplateView


class ErrorView(TemplateView):
		template_name = 'error.html'
		error = None

		def get_context_data(self, **kwargs):
				context_data = super().get_context_data(**kwargs)
				context_data['error_code'] = self.error
				if self.error == 500:
						context_data['error_message'] = 'Oeps, er is iets fout gegaan!\n' \
						                                'Een team van getrainde aapjes is op de hoogte gebracht en  zullen deze fout zo snel mogelijk herstellen!\n'
				elif self.error == 404:
						context_data['error_message'] = 'De opgevraagde pagina of data vereist om deze pagina op te bouwen kon niet worden gevonden'
				elif self.error == 403:
						context_data['error_message'] = 'U heeft niet de correcte rechten om deze pagina te bekijken'
				elif self.error == 400:
						context_data['error_message'] = 'Het was niet mogelijk om uw verzoek af te handelen'

				return context_data

		@method_decorator(requires_csrf_token)
		def dispatch(self, request, *args, **kwargs):
				context = self.get_context_data(**kwargs)
				return render(request, self.template_name, context, status=self.error)
