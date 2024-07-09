import os
import subprocess

def run_script(script_name, *args):
    try:
        subprocess.run(['python', script_name, *args], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")

def create_random_files():
    print("Creating random files...")
    run_script('create_random_files.py')

def sort_files(source_dir, destination_dir):
    print("Sorting files...")
    run_script('copy_files.py', source_dir, destination_dir)

def create_koch_snowflake():
    while True:
        try:
            order = int(input("Enter the recursion level (1-5): "))
            if 1 <= order <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 5.")
    
    run_script('koch_snowflake.py', str(order))

def hanoi_towers():
    while True:
        try:
            n = int(input("Enter the number of disks: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    run_script('hanoi.py', str(n))

def main():
    while True:
        print("\nMenu:")
        print("1. Create random files")
        print("2. Sort files")
        print("3. Create Koch snowflake")
        print("4. Solve Hanoi Towers")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            create_random_files()
        elif choice == '2':
            source_dir = input("Enter the path to the source directory: ")
            destination_dir = input("Enter the path to the destination directory: ")
            if not os.path.exists(source_dir):
                print(f"The source directory '{source_dir}' does not exist.")
            else:
                sort_files(source_dir, destination_dir)
        elif choice == '3':
            create_koch_snowflake()
        elif choice == '4':
            hanoi_towers()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
4