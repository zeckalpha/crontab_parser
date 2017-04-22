import calendar


class CronLine(object):
    def __init__(self, line: str) -> None:
        split_line = line.split()
        minute, hour, day_of_month, month, day_of_week, *command = split_line
        self.minute = minute
        self.hour = hour
        self.day_of_month = day_of_month
        self.month = month
        self.day_of_week = day_of_week
        self.command = command

    def describe_command(self) -> str:
        return ' '.join(self.command)

    time_descriptions = {
        '*': 'every',
        '1': 'the first',
        '45': 'not a good approach',
        '23': 'not at all',
        '0': 'zero points'
    }

    def describe_time(self, field, unit) -> str:
        return f"{self.time_descriptions[field]} {unit}"

    def describe_minute(self) -> str:
        return self.describe_time(self.minute, 'minute')

    def describe_hour(self) -> str:
        return self.describe_time(self.hour, 'hour')

    def describe_day_of_month(self) -> str:
        return self.describe_time(self.day_of_month, 'day')

    def describe_month(self) -> str:
        try:
            month_int = int(self.month)
            return calendar.month_name[month_int]
        except ValueError:
            return 'every month'

    def describe_day_of_week(self) -> str:
        try:
            day_of_week_int = int(self.day_of_week) % 7
            return calendar.day_name[day_of_week_int - 1] + 's'
        except ValueError:
            return 'any day of the week'

    def describe(self) -> str:
        return ''.join([
            "Run `",
            self.describe_command(),
            "` on ",
            self.describe_minute(),
            " of ",
            self.describe_hour(),
            " of ",
            self.describe_day_of_month(),
            " of ",
            self.describe_month(),
            " on ",
            self.describe_day_of_week()
        ])
