from websitedata.models import (News, Team, Slider, Events, Privacy, Changes)
from userdata.models import Rules
from Tortoise.models import SiteUrls


class UtilityMixin(object):
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
        self.context["siteurls"] = self.siteurls # noqa
        self.context["news"] = self.news
        return self.context

    def get_blog_context(self):
        self.context["siteurls"] = self.siteurls  # noqa
        return self.context

    def get_generic_context(self):
        self.context["privacy"] = self.privacy
        self.context['rules'] = self.rules
        self.context['changes'] = self.changes
        self.get_blog_context()
