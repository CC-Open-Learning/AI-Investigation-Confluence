import sys

print('<table border="1">')
count = 0
for line in sys.stdin:
    color = 'lightgreen' if count == 0 else 'white' if count % 2 else 'lightyellow'
    print(f'<tr bgcolor="{color}">')
    fields = line.strip().split(',')
    for field in fields:
        if field.isdigit():
            print(f'<td align="right">{field}</td>')
        else:
            print(f'<td>{field}</td>')
    print('</tr>')
    count += 1
print('</table>')
