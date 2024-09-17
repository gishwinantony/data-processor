#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataProcessor.settings')


    # Automatically run the development server if no arguments are provided
    if len(sys.argv) == 1:
        sys.argv.append('runserver')
        sys.argv.append('8080')
    elif len(sys.argv) == 2 and sys.argv[1] == 'runserver':
        # If only 'runserver' is provided, append default port
        sys.argv.append('8080')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    
