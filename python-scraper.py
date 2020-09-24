# =============================================================================
# Name:         Peter Kim
# Description:  Playbook for how to incorporate CLI arguments in Python app.
# =============================================================================
'''
Sample CLI commands
$ python3 python-scraper.py -t daily_update
$ python3 python-scraper.py -t six_week_rolling_window
'''

import argparse, sys
from argparse import RawTextHelpFormatter

def run_sample_function(input_time_period='six_week_rolling_window'):
  '''
  Sample application with a single input parameter, comes from CLI argument.
  
  Inputs:
    * input_time_period - str, argument for time period.
        - Example: 'six_week_rolling_window', also default parameter
  '''
  # branching logic based in input parameter
  if input_time_period='six_week_rolling_window':
    print("Run the application using the six week rolling window.")
  elif input_time_period='daily_update':
    print("Run the application using the daily update window.")
    
  # ========== SAMPLE CODE ==========
  # put sample application code that incorporate the parameters.
  # =================================
  
  return None

def main():

  # parse command line interface arguments
  parser = argparse.ArgumentParser(description='''Run this Python application using flags.''',
                                    formatter_class=RawTextHelpFormatter)
  parser.add_argument('-t', '--time_period',
                        help='''Enter time period description''',
                        required=True)
  args = parser.parse_args()
  
  # save CLI arguments as variables
  if args.time_period:
    str_time_period = args.time_period
    
  # run function using argument
  run_sample_function(str_time_period)
  

if __name__ == "__main__":
  main()
