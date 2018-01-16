from rest_framework import viewsets
from .models import Rate, Run, Velocity, Analyzer, Decay, Pulse
from .serializers import *

# Create your views here.

class RunViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Run.objects.all().order_by('ts')
    serializer_class = RunSerializer


class AnalyzerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Analyzer.objects.all().order_by('name')
    serializer_class = AnalyzerSerializer


class RateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rate.objects.all().order_by('query_time')
    serializer_class = RateSerializer
    filter_fields = ('analyzer', 'run')


class VelocityViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Velocity.objects.all().order_by('event_time')
    serializer_class = VelocitySerializer
    filter_fields = ('analyzer', 'run')


class DecayViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Decay.objects.all().order_by('event_time')
    serializer_class = DecaySerializer
    filter_fields = ('analyzer', 'run')


class PulseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pulse.objects.all().order_by('event_time')
    serializer_class = PulseSerializer
    filter_fields = ('analyzer', 'run')