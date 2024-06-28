def main():
    result = 'github.com/Angel21-ctrl-Z/bookbot/output.txt'
    output = run_rea(result)
    print(output)

def run_rea(result):
    with open(result) as f:
        return f.read()

main()