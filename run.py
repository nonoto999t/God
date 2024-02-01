import subprocess
import random
import time

def generate_traffic():
    while True:
        n = random.randint(1, 100)
        print(f"Making {n} random requests")

        with open("urls.txt", "r") as file:
            urls = file.read().splitlines()

        random_urls = random.sample(urls, n)

        for url in random_urls:
            subprocess.run(["curl", url, "-o", "/dev/null"])
            time.sleep(1)

        time.sleep(5)

if __name__ == "__main__":
    generate_traffic()
