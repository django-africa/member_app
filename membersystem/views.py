from django.views.generic import View


class HomeView(View):
        template_name = 'index.html'