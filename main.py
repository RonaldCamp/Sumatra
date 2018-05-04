# test.py
import sys
from sumatra.parameters import build_parameters
from sumatra.decorators import capture

@capture
def main(parameters):
    print "Hi"

parameter_file = sys.argv[1]
parameters = build_parameters(parameter_file)
main(parameters)

