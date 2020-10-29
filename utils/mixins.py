from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from tortoise.models import SiteUrls
from tortoise_api.models import Rules
from tortoise_web.models import News, Team, Slider, Events, Privacy, Changes


class ModelDataMixin(object):
    context = {}
    siteurls = SiteUrls # noqa
    news = News.objects.all()
    team = Team.objects.all()
    slider = Slider.objects.all()
    events = Events.objects.all()
    privacy = Privacy.objects.all()
    changes = Changes.objects.all()
    rules = Rules.objects.all().order_by('number')[1:]

    def get_main_context(self):
        self.context['slides'] = self.slider
        self.get_common_context()
        self.get_category_events()
        return self.context

    def get_events_context(self):
        self.context['events'] = self.events.filter(status__in=['Live', 'Ended']).order_by('-id')
        self.get_upcoming_context()
        self.get_common_context()
        return self.context

    def get_upcoming_context(self):
        self.context['upcoming'] = self.events.filter(status='Upcoming')[:2]
        return self.context

    def get_category_events(self):
        self.context['levents'] = self.events.filter(status='Live')[:2] # noqa
        self.context['revents'] = self.events.filter(status='Ended')[:3] # noqa
        self.get_upcoming_context()
        return self.context

    def get_common_context(self):
        self.context["team"] = self.team
        self.context["siteurls"] = self.siteurls
        self.context["news"] = self.news
        return self.context

    def get_blog_context(self):
        self.context["siteurls"] = self.siteurls
        return self.context

    def get_generic_context(self):
        self.context["privacy"] = self.privacy
        self.context['rules'] = self.rules
        self.context['changes'] = self.changes
        self.get_blog_context()


class ResponseMixin(object):

    @staticmethod
    def json_response_204():
        return JsonResponse({"response": "Not Content"}, status=204)

    @staticmethod
    def json_response_400():
        return JsonResponse({"response": "Bad Request"}, status=400)

    @staticmethod
    def json_response_401():
        return JsonResponse({"response": "Unauthorized"}, status=401)

    @staticmethod
    def json_response_404():
        return JsonResponse({"response": "Not Found"}, status=404)

    @staticmethod
    def json_response_405():
        return JsonResponse({"response": "Method Not Allowed"}, status=405)

    @staticmethod
    def json_response_500():
        return JsonResponse({"response": "Internal Server Error"}, status=500)

    @staticmethod
    def json_response_501():
        return JsonResponse({"response": "Not Implemented"}, status=501)

    @staticmethod
    def json_response_502():
        return JsonResponse({"response": "Bad Gateway"}, status=502)

    @staticmethod
    def json_response_503():
        return JsonResponse({"response": "Internal Server Error"}, status=503)

    @staticmethod
    def json_response_504():
        return JsonResponse({"response": "Gateway Timeout"}, status=504)

    @staticmethod
    def html_response_404(request):
        return render(request, "dashboard/page-404.html", status=404)

    @staticmethod
    def html_response_403(request):
        return render(request, "dashboard/page-403.html", status=403)

    @staticmethod
    def http_response_400():
        return HttpResponse("<h1>Bad Request (400)</h1>", status=400)

    @staticmethod
    def http_response_401():
        return HttpResponse("<h1>Unauthorized (401)</h1>", status=401)

    @staticmethod
    def http_response_403():
        return HttpResponse("<h1>Forbidden (403)</h1>", status=403)

    @staticmethod
    def http_response_404():
        return HttpResponse("<h1>Page not found (404)</h1>", status=404)

    @staticmethod
    def http_response_405():
        return HttpResponse("<h1>Method Not Allowed (405)", status=405)
