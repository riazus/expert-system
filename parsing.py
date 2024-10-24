def parse_input(file_path):
    rules = []
    facts = set()
    queries = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.split('#')[0].strip()

            if not line:
                continue

            if line.startswith('='):
                facts.update(set(line[1:]))
                continue

            if line.startswith('?'):
                queries = list(line[1:])
                continue

            rules.append(line)

    return rules, facts, queries
