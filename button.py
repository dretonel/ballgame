import pygame


class Button():

    def __init__(
        self,
        bstats_settings,
        screen,
        msg,
        index=0,
        row=0,
        offset=0
    ):
        """Initialize the button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        if len(msg) <= 2:
            self.width, self.height = (3 * 15), 36
        else:
            self.width, self.height = len(msg * 15), 36

        self.button_color = bstats_settings.colorPlay
        self.text_color = bstats_settings.colorText
        self.font = pygame.font.SysFont('FreeMono', 24, bold=True)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Is the button Play ? center the button
        if msg is 'Play':
            self.rect.center = self.screen_rect.center

        # Is the button Player/Number ? hug the left
        # Inner if-else for team color
        elif index is 0:
            if offset is 0:
                self.button_color = bstats_settings.colorHome
            else:
                self.button_color = bstats_settings.colorAway
            self.rect.midleft = (index + offset, (row + 1) * 40)

        # Is the button Player/Number ? hug the
        #    offset (currently mid of screen)
        # Inner if-else for team color
        else:
            if offset is 0:
                self.button_color = bstats_settings.colorHome
            else:
                self.button_color = bstats_settings.colorAway
            self.rect.midleft = (
                index * (self.width + 10) + 90 + offset,
                (row + 1) * 40
            )
        # self.rect.bottomleft = self.screen_rect.bottomleft

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on button"""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
