class Television:
    """
    A class representing a basic television.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a new instance of the Television class.

        The TV is initially turned off, with the channel set to the minimum channel and the volume set to the minimum volume.
        """
        self.__status: bool = False
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__muted: bool = False

    def power(self) -> None:
        """
        Toggle the power state of the TV.

        If the TV is currently on, it will be turned off. If the TV is currently off, it will be turned on.
        """
        self.__status = not self.__status

    def channel_up(self) -> None:
        """
        Increment the channel of the TV.

        If the TV is powered on and the current channel is less than the maximum channel, the channel will be incremented by 1.
        If the current channel is the maximum channel, the channel will be set to the minimum channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrement the channel of the TV.

        If the TV is powered on and the current channel is greater than the minimum channel, the channel will be decremented by 1.
        If the current channel is the minimum channel, the channel will be set to the maximum channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume of the TV.

        If the TV is powered on and the current volume is less than the maximum volume, the volume will be incremented by 1.
        The mute state will be set to False.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume of the TV.

        If the TV is powered on and the current volume is greater than the minimum volume, the volume will be decremented by 1.
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def mute(self) -> None:
        """
        Toggle the mute state of the TV.

        If the TV is powered on, the mute state will be switched from True to False, or from False to True.
        """
        if self.__status:
            self.__muted = not self.__muted

    def __str__(self) -> str:
        """
        Return a string representation of the TV's current state.

        If the TV is muted, the volume will be displayed as the minimum volume.
        Otherwise, the actual volume level will be displayed.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'