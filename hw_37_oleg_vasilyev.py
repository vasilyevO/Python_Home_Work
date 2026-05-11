print("\n 1. Воспроизведение мультимедиа")

class AudioFileMixin:
    """Миксин для воспроизведения аудио треков."""

    def play_audio(self) -> str:
        """Возвращает строку с треками. Требует поле audio_tracks."""
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует поле audio_tracks")
        tracks = "\n".join(self.audio_tracks)
        return f"Воспроизведение аудио для {self.__class__.__name__}:\n{tracks}"

class VideoFileMixin:
    """Миксин для воспроизведения видео файлов."""

    def play_video(self) -> str:
        """Возвращает строку с видео. Требует поле video_files."""
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует поле video_files")
        videos = "\n".join(self.video_files)
        return f"Воспроизведение видео для {self.__class__.__name__}:\n{videos}"

class MediaPlayer(AudioFileMixin, VideoFileMixin):
    """Медиаплеер с поддержкой аудио и видео."""

    def __init__(self) -> None:
        self.audio_tracks = ["Track 1", "Track 2"]
        self.video_files = ["Video 1", "Video 2"]

player = MediaPlayer()
print(player.play_audio())
print(player.play_video())


print("\n 2. Устройства")
class AudioFileMixin:
    """Mixin for playing audio tracks."""

    def play_audio(self) -> str:
        """Возвращает строку с треками. Требует поле audio_tracks."""
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует поле audio_tracks")
        tracks = "\n".join(self.audio_tracks)
        return f"Воспроизведение аудио для {self.__class__.__name__}:\n{tracks}"


class VideoFileMixin:
    """Миксин для воспроизведения видео файлов."""

    def play_video(self) -> str:
        """Возвращает строку с видео. Требует поле video_files."""
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует поле video_files")
        videos = "\n".join(self.video_files)
        return f"Воспроизведение видео для {self.__class__.__name__}:\n{videos}"

class MediaPlayer(AudioFileMixin):
    """Медиаплеер с поддержкой только аудио."""

    def __init__(self, tracks: list[str]) -> None:
        self.audio_tracks = tracks

class Laptop(AudioFileMixin, VideoFileMixin):
    """Ноутбук с поддержкой аудио и видео."""

    def __init__(self, audio_tracks: list[str], video_files: list[str]) -> None:
        self.audio_tracks = audio_tracks
        self.video_files = video_files

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

player = MediaPlayer(tracks)
laptop = Laptop(tracks, movies)

print(player.play_audio())
print(laptop.play_audio())
print(laptop.play_video())