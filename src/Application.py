import Table
from VideoRecognotion import VideoRecognition


class Application:
    _obj = None
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = super().__new__(cls, *args, **kwargs)
        return cls._obj
    

    def process(self):
        pass

    def show(self) -> None:
        pass

if __name__ == "__main__":
    app = Application()
    app.process()