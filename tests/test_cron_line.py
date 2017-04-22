import unittest

from crontab_parser.cron_line import CronLine


class TestCronLine(unittest.TestCase):
    def test_splits_into_fields(self) -> None:
        line = "* * * * * command to run"
        split_line = line.split(" ")
        minute, hour, day_of_month, month, day_of_week, *command = split_line
        cl = CronLine(line)
        self.assertEqual(minute, cl.minute)
        self.assertEqual(hour, cl.hour)
        self.assertEqual(day_of_month, cl.day_of_month)
        self.assertEqual(month, cl.month)
        self.assertEqual(day_of_week, cl.day_of_week)
        self.assertEqual(command, cl.command)


if __name__ == '__main__':
    unittest.main()
