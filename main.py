from get_platform_info import platform_info as platform
from get_current_session_info import get_session_info


def main():
    platform()
    print("User time:",get_session_info()[0][0])
    print("System time:",get_session_info()[0][1])
    print("Idle time:",get_session_info()[0][2])
<<<<<<< HEAD
    print("Interruption time:", get_session_info()[0][3])
=======
>>>>>>> e5bd01d8184168ec05d4933dd377c17e717855e8


if __name__ == "__main__":
    main()