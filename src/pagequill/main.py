"""Application entry point."""

from pagequill.ui.main_window import MainWindow


def main() -> None:
    """Start PageQuill."""
    window = MainWindow()
    window.run()


if __name__ == "__main__":
    main()

