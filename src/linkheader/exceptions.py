"""Custom exceptions for linkheader."""


class LinkheaderError(Exception):
    """Base exception for linkheader."""


class InvalidColorError(LinkheaderError):
    """Raised when a color value is invalid."""


class FontLoadError(LinkheaderError):
    """Raised when a font cannot be loaded."""


class QRGenerationError(LinkheaderError):
    """Raised when QR code generation fails."""


class BannerGenerationError(LinkheaderError):
    """Raised when banner generation fails."""


class FaviconFetchError(LinkheaderError):
    """Raised when a favicon cannot be fetched."""
