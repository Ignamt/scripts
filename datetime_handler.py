"""Contains the DateTimeHandler, used to parse any input and convert it to
a  datetime object in order to unify date info management.

"""
import datetime as dt


class DateTimeHandler(dt.datetime):
    """Handles incoming date info and returns a datetime object.
    
    This class inherits from the datetime class, so that it has all
    the same attributes and methods, but adds the parse() method.
        
    """

    @classmethod
    def parse(cls, dt_in, dt_format=None):
        """Convert input datetime info to datetime object.

        IMPORTANT: This method uses Argentine date formatting (eg: DD/MM/YYYY),
        not the USA formatting (MM/DD/YYYY) -> So weird!

        Also, this method
        
        ARGS:
        - input: The input information to parse and turn into a datetime.
        - format: (Optional) string of datetime formatting to specify.
                   This speeds up the conversion.

        RETURNS: A datetime() object from the info that was input, or a 
                datetime.time() object if that was the input
        
        RAISES:
            - TypeError: If a format was given and the input is not a str
                          (or unicode)
                         If dt_in is not of a supported type
                   
        """
        print("DateTimeHandler input: ", str(dt_in), ". Type: ", type(dt_in))
        if dt_format:
            return cls._parse_format(dt_in, dt_format)

        # Parse timestamp info
        if isinstance(dt_in, int):
            return cls._parse_timestamp(dt_in)

        # Parse string info
        elif isinstance(dt_in, str):
            return cls._parse_str(dt_in)

        elif isinstance(dt_in, (dt.datetime, dt.time)):
            print("Datetime object detected, returning.")
            return dt_in

        elif isinstance(dt_in, dt.date):
            dt.datetime.combine(dt_in, dt.time())

        else:
            raise TypeError("{} objects are not supported".format(type(dt_in)))

    
    @classmethod
    def _parse_format(cls, dt_in, dt_format):
        print("Format detected, parsing.")
        if not isinstance(dt_in, (str, unicode)):
            raise TypeError("The datetime info is not a string. "
                            "Please remove the formatting or"
                            " supply string-based information.")
        return cls.strptime(dt_in, dt_format)


    @classmethod
    def _parse_timestamp(dt_in):
        print("Numerical value detected, parsing.")
        # If Seconds
        try:
            print("Parsed timestamp in seconds.")
            return cls.fromtimestamp(dt_in)

        # If Miliseconds
        except (ValueError, OSError):
            print("Parsed timestamp in miliseconds.")
            return cls.fromtimestamp(dt_in/1000)

    @classmethod
    def _parse_str(dt_in):
        print("String detected, parsing.")
        formats = [
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%dT%H:%M:%S.%f",
            "%d/%m/%Y",
            "%d-%m-%Y",
            "%Y%m%d",
            "%Y-%m-%d",
            "%Y/%m/%d",
            "%d/%m/%y",
            "%d-%m-%y",
            "%d/%m/%y",
        ]

        for f in formats:
            try:
                print("Parsing with format: ", f)
                return cls.strptime(dt_in, f)
            except Exception as ex:
                print(ex)
                continue
