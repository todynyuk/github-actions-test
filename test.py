import logging


logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)

def logs_artifact_test():
  logging.info('Test logger-1: test start')
  assert "Test"=="Test"
  logging.info('Test logger-1: test finish')
  
