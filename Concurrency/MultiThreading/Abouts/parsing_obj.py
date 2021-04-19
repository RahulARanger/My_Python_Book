import threading


def parse_obj():
    # Returns the current thread object
    thread_obj = threading.current_thread()
    # Thread object
    print(thread_obj)
    print(
        f"""
Name: {thread_obj.name}
More: {dir(thread_obj)}
Alive ?: {thread_obj.is_alive()}
"""
    )


parse_obj()
