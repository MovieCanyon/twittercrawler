import capture_users

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

triad_number = 1
user_dict = capture_users.user_dict


print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TRIAD BUILDING HAS NOW BEGUN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")
for user in user_dict:
    for mentioned_user in user_dict[user]:
        mentioned_user = mentioned_user[1:]
        if mentioned_user in user_dict:
            for third_user in user_dict[mentioned_user]:
                print("Triad ", triad_number)
                print(user + '->' + mentioned_user + '; ' + mentioned_user + '->' + third_user)
                print(user + '->' + mentioned_user + '; ' + mentioned_user + '->' + third_user + '; ' + third_user + '->' + user)
                print(user + '<->' + mentioned_user + '; ' + mentioned_user + '->' + third_user + '; ' + third_user + '->' + user)
                print(user + '<->' + mentioned_user + '; ' + mentioned_user + '<->' + third_user + '; ' + third_user + '->' + user)
                print(user + '->' + mentioned_user + '; ' + mentioned_user + '<->' + third_user + '; ' + third_user + '<->' + user)
                print(user + '->' + mentioned_user + '; ' + mentioned_user + '<->' + third_user + '; ')
                print("")
                triad_number += 1
