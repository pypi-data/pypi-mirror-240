import datetime
import ipaddress
import math

from flask import request
from flask_babel import gettext as _
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.hybrid import hybrid_property

from uffd.tasks import cleanup_task
from uffd.database import db

@cleanup_task.delete_by_attribute('expired')
class RatelimitEvent(db.Model):
	__tablename__ = 'ratelimit_event'
	id = Column(Integer(), primary_key=True, autoincrement=True)
	timestamp = Column(DateTime(), default=datetime.datetime.utcnow, nullable=False)
	expires = Column(DateTime(), nullable=False)
	name = Column(String(128), nullable=False)
	key = Column(String(128))

	@hybrid_property
	def expired(self):
		return self.expires < datetime.datetime.utcnow()

class Ratelimit:
	def __init__(self, name, interval, limit):
		self.name = name
		self.interval = interval
		self.limit = limit
		self.base = interval**(1/limit)

	def log(self, key=None):
		db.session.add(RatelimitEvent(name=self.name, key=key, expires=datetime.datetime.utcnow() + datetime.timedelta(seconds=self.interval)))
		db.session.commit()

	def get_delay(self, key=None):
		events = RatelimitEvent.query\
				.filter(db.not_(RatelimitEvent.expired))\
				.filter_by(name=self.name, key=key)\
				.order_by(RatelimitEvent.timestamp)\
				.all()
		if not events:
			return 0
		delay = math.ceil(self.base**len(events))
		if delay < 5:
			delay = 0
		delay = min(delay, 365*24*60*60) # prevent overflow of datetime objects
		remaining = events[0].timestamp + datetime.timedelta(seconds=delay) - datetime.datetime.utcnow()
		return max(0, math.ceil(remaining.total_seconds()))

def get_addrkey(addr=None):
	if addr is None:
		addr = request.remote_addr
	try:
		addr = ipaddress.ip_address(addr)
	except ValueError:
		return '"'+addr+'"'
	if isinstance(addr, ipaddress.IPv4Address):
		net = ipaddress.IPv4Network((addr, '24'), strict=False)
	elif isinstance(addr, ipaddress.IPv6Address):
		net = ipaddress.IPv6Network((addr, '48'), strict=False)
	else:
		net = ipaddress.ip_network(addr)
	return net.network_address.compressed

class HostRatelimit(Ratelimit):
	def log(self, key=None):
		super().log(get_addrkey(key))

	def get_delay(self, key=None):
		return super().get_delay(get_addrkey(key))

def format_delay(seconds):
	if seconds <= 15:
		return _('a few seconds')
	if seconds <= 30:
		return _('30 seconds')
	if seconds <= 60:
		return _('one minute')
	if seconds < 3000:
		return _('%(minutes)d minutes', minutes=(math.ceil(seconds/60)+1))
	if seconds <= 3600:
		return _('one hour')
	return _('%(hours)d hours', hours=math.ceil(seconds/3600))

# Global host-based ratelimit
host_ratelimit = HostRatelimit('host', 1*60*60, 25)
