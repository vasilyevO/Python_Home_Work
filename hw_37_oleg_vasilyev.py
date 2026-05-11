print("\n 1. Воспроизведение мультимедиа")

class AudioFileMixin:
    """Mixin for playing audio tracks."""

    def play_audio(self) -> str:
        """Returns a string containing the tracks. Requires the `audio_tracks` field."""
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует поле audio_tracks")
        tracks = "\n".join(self.audio_tracks)
        return f"Воспроизведение аудио для {self.__class__.__name__}:\n{tracks}"

class VideoFileMixin:
    """Mixin for playing video files."""

    def play_video(self) -> str:
        """Returns a string containing the video. Requires the video_files field."""
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует поле video_files")
        videos = "\n".join(self.video_files)
        return f"Воспроизведение видео для {self.__class__.__name__}:\n{videos}"

class MediaPlayer(AudioFileMixin, VideoFileMixin):
    """A media player that supports audio and video."""

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
        """Returns a string containing the tracks. Requires the `audio_tracks` field."""
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует поле audio_tracks")
        tracks = "\n".join(self.audio_tracks)
        return f"Воспроизведение аудио для {self.__class__.__name__}:\n{tracks}"


class VideoFileMixin:
    """Mixin for playing video files."""

    def play_video(self) -> str:
        """Returns a string containing the video. Requires the video_files field."""
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует поле video_files")
        videos = "\n".join(self.video_files)
        return f"Воспроизведение видео для {self.__class__.__name__}:\n{videos}"

class MediaPlayer(AudioFileMixin):
    """A media player that supports audio only."""

    def __init__(self, tracks: list[str]) -> None:
        self.audio_tracks = tracks

class Laptop(AudioFileMixin, VideoFileMixin):
    """A laptop with audio and video support."""

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