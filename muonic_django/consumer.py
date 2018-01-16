import datetime
from importlib import import_module
from muonic.lib.consumers import AbstractMuonicConsumer


class Consumer(AbstractMuonicConsumer):

    def __init__(self, app_settings=None, username=None, simulation=False, logger=None):
        super().__init__(logger=logger)

        models = import_module('.'.join(__name__.split('.')[:-1]) + '.models')  # models have to be imported after the settings conf
        self.User = getattr(import_module('django.contrib.auth.models'), 'User')
        self.Run = getattr(models, 'Run')
        self.Analyzer = getattr(models, 'Analyzer')
        self.Rate = getattr(models, 'Rate')
        self.Velocity = getattr(models, 'Velocity')
        self.Decay = getattr(models, 'Decay')
        self.Pulse = getattr(models, 'Pulse')

        self.analyzers = {}
        self.run = None
        self.simulation = simulation
        self.user = self.User.objects.get(username=username) if username is not None else None

    def start(self, run_id, analyzer_id='', expected_data_types=[]):
        if self.run is not None:
            if run_id != self.run.run_id:
                raise Exception("Cannot record data from different runs simultaneously")
        else:
            self.run, created = self.Run.objects.get_or_create(run_id=run_id, user=self.user, simulation=self.simulation)
        self.analyzers[analyzer_id], created = self.Analyzer.objects.get_or_create(name=analyzer_id)

    def stop(self, run_id, analyzer_id=''):
        if run_id != self.run.run_id:
            self.logger.warning("Stop called with non-existent run-id")
            return
        self.analyzers.pop(analyzer_id)
        if not self.analyzers:
            self.run.active = False
            self.run.save()
            self.run = None     # all analyzers stopped - run stopped

    def push_velocity(self, flight_time, event_time, meta):
        aid = meta.get('analyzer_id')
        if aid not in self.analyzers:  # push called after stop for aid - ignore silently
            return
        v = self.Velocity(flight_time=flight_time,
                          event_time=event_time.replace(tzinfo=datetime.timezone.utc),
                          analyzer=self.analyzers.get(aid),
                          run=self.run)
        v.save()

    def push_decay(self, decay_time, event_time, meta):
        aid = meta.get('analyzer_id')
        if aid not in self.analyzers:  # push called after stop for aid - ignore silently
            return
        d = self.Decay(decay_time=decay_time,
                       event_time=event_time.replace(tzinfo=datetime.timezone.utc),
                       analyzer=self.analyzers.get(aid),
                       run=self.run)
        d.save()

    def push_rate(self, rates, counts, time_window, query_time, meta):
        aid = meta.get('analyzer_id')
        if aid not in self.analyzers:  # push called after stop for aid - ignore silently
            return
        r = self.Rate(rate_ch0=rates[0],
                      rate_ch1=rates[1],
                      rate_ch2=rates[2],
                      rate_ch3=rates[3],
                      rate_cht=rates[4],
                      count_ch0=counts[0],
                      count_ch1=counts[1],
                      count_ch2=counts[2],
                      count_ch3=counts[3],
                      count_cht=counts[4],
                      time_window=time_window,
                      query_time=query_time.replace(tzinfo=datetime.timezone.utc),
                      run=self.run,
                      analyzer=self.analyzers.get(aid))
        r.save()

    def push_raw(self, data, meta):
        pass

    def push_pulse(self, pulse_widths, event_time, meta):
        aid = meta.get('analyzer_id')
        if aid not in self.analyzers:  # push called after stop for aid - ignore silently
            return
        pw = {}
        for i in range(4):
            pw[i] = pulse_widths.get(i)[0] if len(pulse_widths.get(i)) >= 1 else None
        p = self.Pulse(pulse_width_ch0=pw.get(0),
                       pulse_width_ch1=pw.get(1),
                       pulse_width_ch2=pw.get(2),
                       pulse_width_ch3=pw.get(3),
                       event_time=event_time.replace(tzinfo=datetime.timezone.utc),
                       run=self.run,
                       analyzer=self.analyzers.get(aid))
        p.save()