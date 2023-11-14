# ruff: noqa: D100, D101, D102, D103, D104, D107
import os

from kivy.clock import Clock

from ubo_app.menu import MenuApp
from ubo_app.store import dispatch
from ubo_app.store.status_icons import (
    IconRegistrationAction,
    IconRegistrationActionPayload,
)


def main() -> None:
    """Instantiate the `MenuApp` and run it."""
    app = MenuApp()

    Clock.schedule_interval(
        lambda *_: dispatch(
            [
                IconRegistrationAction(
                    type='REGISTER_ICON',
                    payload=IconRegistrationActionPayload(icon='wifi', priority=-1),
                )
                for _ in range(2)
            ],
        ),
        3,
    )

    for services_directory_path in [
        './services',
        *os.environ.get('UBO_SERVICES', '').split(' '),
    ]:
        if os.path.isdir(services_directory_path):
            print(os.listdir(services_directory_path))

    app.run()


if __name__ == '__main__':
    main()
