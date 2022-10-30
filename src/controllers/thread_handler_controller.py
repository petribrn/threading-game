import threading


class ThreadHandlerController:
    stop_event = threading.Event()

    @staticmethod
    def create(function, window) -> threading.Thread:
        return threading.Thread(target=function, args=(window, ThreadHandlerController.stop_event), daemon=True)

    @staticmethod
    def stop_daemon_threads() -> None:
        ThreadHandlerController.stop_event.set()
