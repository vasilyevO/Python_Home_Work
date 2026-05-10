print("\n 1. Воспроизведение мультимедиа")

class AudioFileMixin:
    """Mixin for playing audio tracks."""

    def play_audio(self) -> None:
        """Displays a list of audio tracks. Requires the `audio_tracks` field."""
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует поле audio_tracks")
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(track)

class VideoFileMixin:
    """Mixin for playing video files."""

    def play_video(self) -> None:
        """Displays a list of video files. Requires the video_files field."""
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует поле video_files")
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in self.video_files:
            print(video)

class MediaPlayer(AudioFileMixin, VideoFileMixin):
    """A media player that supports audio and video."""

    def __init__(self) -> None:
        self.audio_tracks = ["Track 1", "Track 2"]
        self.video_files = ["Video 1", "Video 2"]

player = MediaPlayer()
player.play_audio()
player.play_video()


print("\n 2. Устройства")
class AudioFileMixin:
    """Mixin for playing audio tracks."""

    def play_audio(self) -> None:
        """Displays a list of audio tracks. Requires the `audio_tracks` field."""
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Отсутствует поле audio_tracks")
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(track)


class VideoFileMixin:
    """Mixin for playing video files."""

    def play_video(self) -> None:
        """Displays a list of video files. Requires the video_files field."""
        if not hasattr(self, "video_files"):
            raise AttributeError("Отсутствует поле video_files")
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in self.video_files:
            print(video)


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

player.play_audio()
laptop.play_audio()
laptop.play_video()