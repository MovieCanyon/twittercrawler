import csv

# Pass in dictionary from capture_users.py
# For each user, go through their mentions
# Print triad to console

# Example: If A mentions B, and B mentions C, then print:

# Triad 1:
# A->B; B->C
# A->B; B->C; C->A
# A<->B; B-> C; C->A
# A<->B; B<-> C; C->A
# A->B; B<-> C; C<->A
# A->B; B<-> C;

