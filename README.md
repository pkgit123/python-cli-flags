# python-cli-flags
Playbook to use Python command-line-interface (CLI) flags.

Use argparse library to enable CLI flags.  Benefit to CLI flags includes code re-use for similar (but not exactly same) use cases, especially when executing Python application from command-line-interface (CLI).  Example: running cron jobs (or Windows Scheduled Tasks) with different flags at different times for different jobs.  

***Example CLI:***
```Python
python3 python-scraper.py -t daily_update
```

***Reference:***
* https://www.askpython.com/python/python-command-line-arguments
