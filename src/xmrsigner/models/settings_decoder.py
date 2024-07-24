class SettingsQrDecoder(BaseSingleFrameQrDecoder):

    def __init__(self):
        super().__init__()
        self.data = None

    def add(self, segment, qr_type=QRType.SETTINGS):
        """
            * Ignores unrecognized settings options.
            * Raises an Exception if a settings value is invalid.

            See `Settings.update()` for info on settings validation, especially for
            missing settings.
        """
        if not segment.startswith("settings::"):
            raise Exception("Invalid SettingsQR data")
        
        # Leave any other parsing or validation up to the Settings class itself.
        # SettingsQR are just ascii data to hand it over as-is.
        self.data = segment

        self.complete = True
        self.collected_segments = 1
        return DecodeQRStatus.COMPLETE
