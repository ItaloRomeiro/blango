#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blango.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')
    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import django-configurations. Is it installed in your "
            "environment and activated?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
