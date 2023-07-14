import psutil


def get_session_info():
    return psutil.cpu_times(), 1


def main():
    print("User time:",get_session_info()[0][0])
    print("System time:",get_session_info()[0][1])
    print("Idle time:",get_session_info()[0][2])


if __name__ == "__main__":
    main()