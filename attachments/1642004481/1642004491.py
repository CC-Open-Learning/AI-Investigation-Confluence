import sys
import collections

User = collections.namedtuple('User', 'username forename middlename surname id')

def process_line(line, usernames):
    fields = line.rstrip().split(':')
    username = (fields[1][0] + fields[3]).lower()
    original_username = username
    count = 1
    while username in usernames:
        username = f'{original_username}{count}'
        count += 1
    usernames.add(username)
    return User(username, fields[1], fields[2], fields[3], fields[0])

def print_users(users):
    print(f"{'ID':<6} {'Username':<15} {'Full Name'}")
    print("=" * 40)
    for user in sorted(users, key=lambda x: x.username):
        full_name = f"{user.forename} {user.middlename} {user.surname}".strip()
        print(f"{user.id:<6} {user.username:<15} {full_name}")

if __name__ == '__main__':
    usernames = set()
    users = []
    for line in sys.stdin:
        users.append(process_line(line, usernames))
    print_users(users)
