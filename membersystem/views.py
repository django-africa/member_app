from django.views.generic import View


class HomeView(View):
        template_name = 'templates/index.html'