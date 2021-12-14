import argparse, sys

# Function to print an error message to the STDERR, then exits
def error(msg):
    sys.stderr.write(f"\nERROR: {msg}")
    sys.exit(1)

# Create CLI Parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "file",
    help="File to run as Reflect program"
)
args = parser.parse_args()

# Open Reflect file
with open(args.program, encoding="utf8") as f:
    # TODO
    pass

# Initializations
memory = bytearray(30000) # Program memory. Max or 30,000
pointer = 0               # Cell pointer
direction = True          # Direction, True if right, False if left. Inits to Right
eof = False               # Has reached end of file