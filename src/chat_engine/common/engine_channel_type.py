from enum import Enum


class EngineChannelType(str, Enum):
    NONE = "none"
    TEXT = "text"
    AUDIO = "audio"
    VIDEO = "video"
    EVENT = "event"
