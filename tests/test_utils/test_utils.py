def log_output(test, errors, sort=False):
  log_path = 'log.txt'

  with open(log_path, 'a') as logfile:
    logfile.write('{0}\n'.format(test))
    if sort:
      errors = sorted(errors)
    for error in errors:
      logfile.write("  {0}\n".format(error))