import sys

def hanoi(n, source, target, auxiliary, towers):
    if n == 1:
        move_disk(source, target, towers)
        return
    hanoi(n - 1, source, auxiliary, target, towers)
    move_disk(source, target, towers)
    hanoi(n - 1, auxiliary, target, source, towers)

def move_disk(source, target, towers):
    disk = towers[source].pop()
    towers[target].append(disk)
    print(f"Перемістити диск з {source} на {target}: {disk}")
    print(f"Проміжний стан: {towers}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python hanoi.py <number_of_disks>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 0:
            raise ValueError("The number of disks must be a positive integer.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    towers = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    print(f"Початковий стан: {towers}")
    
    hanoi(n, 'A', 'C', 'B', towers)
    
    print(f"Кінцевий стан: {towers}")

if __name__ == "__main__":
    main()
