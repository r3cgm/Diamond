import diamond.collector
import os
import socket
from socket import error as socket_error
import time

"""
Collect tcp or udp port opening times.

##### Configuration

Create a file called PortLatency.conf in the collectors_config_path
directory.

 * enabled = true
 * interval = 60
 * target_1 = www.yahoo.com:80:tcp
 * target_2 = www.google.com:443:tcp
 * target_3 = 8.8.8.8:53:udp

Test your configuration using the following command:

diamond-setup --print -C PortLatency

You should get a reponse back that indicates 'enabled': True and see entries
for your targets in pairs like:

'target_1': 'www.yahoo.com:80:tcp'

Where www.yahoo.com is the host, 80 is the port, and either tcp or udp is
specified, all separated by colons.

We embed the name of the host in the metric string.

"""


class PortLatency(diamond.collector.Collector):

    def get_default_config_help(self):
        config_help = super(PortLacency, self).get_default_config_help()
        config.update({
            'path': 'portlatency',
        })
        return config_help

    def get_default_config(self):
        """
        Returns the default collector settings.
        """
        config = super(PortLatency, self).get_default_config()
        return config

    def collect(self):
        for key in self.config.keys():
            if key[:7] == "target_":
                host, port, proto = self.config[key].split(':')
                metric_name = host.replace('.', '_') + '.' + port + '.' + proto

                if proto == 'tcp':
                    sock = socket.socket()
                elif proto == 'udp':
                    sock = socket.socket(socket.SOCK_DGRAM)

                port_failed = 0

                time_start = time.time()
                try:
                    sock.connect((host, int(port)))
                except socket_error as serr:
                    port_failed = 1
                time_end = time.time()

                if port_failed:
                    self.publish(metric_name, -1)
                else:
                    self.publish(metric_name, (time_end - time_start) * 1000)
