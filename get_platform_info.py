import platform


def platform_info():
    print(f"Operating system: {platform.system()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"OS version: {platform.version()}")
    print(f"Processor name: {platform.processor()}")

def main():
    platform_info()


if __name__ == "__main__":
    main()