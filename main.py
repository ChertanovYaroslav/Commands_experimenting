from get_platform_info import platform_info as platform
from get_current_session_info import get_session_info


def main():
    platform()
    print("User time:",get_session_info()[0][0])
    print("System time:",get_session_info()[0][1])
    print("Idle time:",get_session_info()[0][2])


if __name__ == "__main__":
    main()