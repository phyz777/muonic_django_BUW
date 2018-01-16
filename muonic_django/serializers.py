from rest_framework import serializers
from .models import Run, Analyzer, Velocity, Rate, Decay, Pulse


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ('run_id', 'user', 'active', 'simulation', 'ts')

    user = serializers.ReadOnlyField(source='user.username')


class AnalyzerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyzer
        fields = ('name',)


class VelocitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Velocity
        fields = ('run', 'analyzer', 'event_time', 'flight_time')


class DecaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Decay
        fields = ('run', 'analyzer', 'event_time', 'decay_time')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class PulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pulse
        fields = ('run', 'analyzer', 'event_time', 'pulse_width_ch0', 'pulse_width_ch1', 'pulse_width_ch2', 'pulse_width_ch3')