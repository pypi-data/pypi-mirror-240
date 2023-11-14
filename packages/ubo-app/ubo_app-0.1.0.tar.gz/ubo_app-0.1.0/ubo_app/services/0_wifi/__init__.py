# ruff: noqa: D100, D101, D102, D103, D104, D107, N999
from kivy import app


def init() -> None:
    print(app)

    # def on_keyboard(
    #     self: MenuApp,
    #     _: WindowBase,
    #     key: int,
    #     _scancode: int,
    #     _codepoint: str,
    #     modifier: list[Modifier],
    # ) -> None:
    #     """Handle keyboard events."""
    #     if modifier == []:
    #         if key == Keyboard.keycodes['up']:
    #             self.menu_widget.go_up()
    #         elif key == Keyboard.keycodes['down']:
    #             self.menu_widget.go_down()
    #         elif key == Keyboard.keycodes['1']:
    #             self.menu_widget.select(0)
    #         elif key == Keyboard.keycodes['2']:
    #             self.menu_widget.select(1)
    #         elif key == Keyboard.keycodes['3']:
    #             self.menu_widget.select(2)
    #         elif key == Keyboard.keycodes['left']:
    #             self.menu_widget.go_back()
