import sys
import os

if __name__ == '__main__':

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hands_on.settings.main")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)