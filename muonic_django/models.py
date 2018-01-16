from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Run(models.Model):
    run_id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True)
    simulation = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.run_id) + ' - ' + str(self.user) + ' - ' + str(self.ts)


class Analyzer(models.Model):
    name = models.CharField(null=False, verbose_name='Analyzer name', max_length=50)

    def __str__(self):
        return self.name


class Decay(models.Model):
    decay_time = models.FloatField()
    event_time = models.DateTimeField()
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    analyzer = models.ForeignKey(Analyzer)

    def __str__(self):
        return 'Decay time: %s, timestamp: %s' % (str(self.decay_time), str(self.event_time))


class Pulse(models.Model):
    pulse_width_ch0 = models.FloatField(null=True)
    pulse_width_ch1 = models.FloatField(null=True)
    pulse_width_ch2 = models.FloatField(null=True)
    pulse_width_ch3 = models.FloatField(null=True)
    event_time = models.DateTimeField()
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    analyzer = models.ForeignKey(Analyzer)

    def __str__(self):
        return 'Ch1: %s, Ch2: %s, Ch3: %s, Ch4: %s, timestamp: %s' %\
               (str(self.pulse_width_ch0),
                str(self.pulse_width_ch1),
                str(self.pulse_width_ch2),
                str(self.pulse_width_ch3),
                str(self.event_time))


class Rate(models.Model):
    rate_ch0 = models.FloatField()
    rate_ch1 = models.FloatField()
    rate_ch2 = models.FloatField()
    rate_ch3 = models.FloatField()
    rate_cht = models.FloatField()  # Trigger
    count_ch0 = models.FloatField()
    count_ch1 = models.FloatField()
    count_ch2 = models.FloatField()
    count_ch3 = models.FloatField()
    count_cht = models.FloatField()  # Trigger
    time_window = models.FloatField()
    query_time = models.DateTimeField()
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    analyzer = models.ForeignKey(Analyzer)

    def __str__(self):
        return 'Ch1: %s, Ch2: %s, Ch3: %s, Ch4: %s, timestamp: %s' %\
               (str(self.rate_ch0), str(self.rate_ch1), str(self.rate_ch2), str(self.rate_ch3), str(self.query_time))


class Velocity(models.Model):
    flight_time = models.FloatField()
    event_time = models.DateTimeField()
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    analyzer = models.ForeignKey(Analyzer)

    def __str__(self):
        return 'flight time: %s, timestamp: %s' % (str(self.flight_time), str(self.event_time))