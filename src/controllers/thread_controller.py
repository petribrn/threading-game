import threading
from src.entities.ball_thread import BallThread
from src.entities.countdown_thread import CountdownThread
from src.entities.game_thread import GameThread


class ThreadController:
    stop_event = threading.Event()
    mutex = threading.Lock()

    @staticmethod
    def create(target_function, window, type_of_thread: str) -> GameThread:
        if type_of_thread == 'countdown':
            return CountdownThread(target_function, ThreadController.stop_event, window, ThreadController.mutex)
        if type_of_thread == 'ball':
            return BallThread(target_function, ThreadController.stop_event, window, ThreadController.mutex)

    @staticmethod
    def stop_daemon_threads() -> None:
        ThreadController.stop_event.set()
