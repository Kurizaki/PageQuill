"""Application-specific exceptions."""


class PageQuillError(Exception):
    """Base exception for PageQuill."""


class GitHubAuthError(PageQuillError):
    """Raised when GitHub authentication fails."""


class PublishError(PageQuillError):
    """Raised when publishing fails."""

