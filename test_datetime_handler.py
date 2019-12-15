"""Tests for the datetime handler."""
import datetime as dt
import pytest

from datetime_handler import DateTimeHandler as dth


def test_dt_handling_with_format():
	date = dth.parse(dt_in="3 del 2 del 2019",
					 dt_format="%d del %m del %Y")
	assert date == dt.datetime(2019,2,3)


def test_dt_handling_with_format_raises_TypeError():
	with pytest.raises(TypeError):
		dth.parse(dt_in=123456789,
			      dt_format="%d del %m del %Y")


def test_dt_handling_timestamp_secs():
	date = dth.parse(dt_in=1565805808)
	assert date == dt.datetime(2019, 8, 14, 15, 3, 28)


def test_dt_handling_timestamp_millisecs():
	date = dth.parse(dt_in=1565805808000)
	assert date == dt.datetime(2019, 8, 14, 15, 3, 28)


def test_dt_handling_str_1():
	date = dth.parse(dt_in="2019-05-04T15:00:00")
	assert date == dt.datetime(2019, 5, 4, 15, 00, 00)


def test_dt_handling_str_2():
	date = dth.parse(dt_in="2019-05-04T15:00:00.112000")
	assert date == dt.datetime(2019, 5, 4, 15, 0, 0 ,112000)


def test_dt_handling_str_3():
	date = dth.parse(dt_in="04/05/2019")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_str_4():
	date = dth.parse(dt_in="5-4-2019")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_str_5():
	date = dth.parse(dt_in="20190504")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_str_6():
	date = dth.parse(dt_in="2019-5-4")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_str_7():
	date = dth.parse(dt_in="2019/5/4")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_str_8():
	date = dth.parse(dt_in="04/05/19")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_str_9():
	date = dth.parse(dt_in="04-05-19")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_str_10():
	date = dth.parse(dt_in="04/05/19")
	assert date == dt.datetime(2019, 5, 4)


def test_dt_handling_with_dt():
	date = dth.parse(dt.datetime(2019, 5, 4, 15))
	assert date == dt.datetime(2019, 5, 4, 15)


def test_dt_handling_with_time():
	date = dth.parse(dt.time(20, 5, 4))
	assert date == dt.time(20, 5, 4)


def test_dt_handling_with_date():
	date = dth.parse(dt.date(2018, 5, 4))
	assert date == dt.datetime(2018, 5, 4)


def test_dt_handling_raises_TypeError():	
	with pytest.raises(TypeError,
					   match="objects are not supported"):
		dth.parse({"date": "2019-05-04"})
