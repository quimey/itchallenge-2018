from bs4 import BeautifulSoup
import os
folder = 'inputs'
result = []


def process_file(filename):
    content = []
    queries = []
    with open(filename, 'r') as f:
        n, m = map(int, f.readline().split())
        for i in range(n):
            content.append(f.readline())
        for i in range(m):
            queries.append(f.readline())
    content = ''.join(content)
    soup = BeautifulSoup(content, 'html.parser')

    # print(soup.prettify())

    for q in queries:
        try:
            path, name = q.strip().split('~')
            path = path.split('.')
            u = soup
            for p in path:
                if p not in [x.name for x in u.contents]:
                    raise ValueError
                u = u.__getattr__(p)
            result.append(u[name])
        except (ValueError, KeyError, TypeError, AttributeError):
            result.append("Not Found!")
        # print(q.strip(), result[-1])
    # print()


for filename in sorted(os.listdir(folder)):
    # print(filename)
    process_file(os.path.join(folder, filename))


# process_file('data.html')

print("\n".join(result))
