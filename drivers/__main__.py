import sys
import time

URL = "https://localhost:3000"

if __name__ == '__main__':
    argv = sys.argv[1:]

    if len(argv) == 0:
        print(f"Usage: {sys.executable} {sys.argv[0]} [firefox|chrome]")
        sys.exit(1)

    match argv[0]:
        case 'firefox':
            from .firefox import driver
        case 'chrome':
            from .chrome import driver
        case _:
            print(f"Unknown driver: {argv[0]}")
            sys.exit(1)
    
    print(f"Running {argv[0]} driver")
    driver.get(URL)

    # Check if the page contains expected content (e.g., "Hello world!")
    assert "Hello world!" in driver.page_source

    print("Request finished waiting 10 seconds before closing the browser")
    # Allow the issue to occur
    time.sleep(10)

    print("Closing the browser")

    driver.quit()