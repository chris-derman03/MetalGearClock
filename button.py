# Class for a button
# Has a method the show the button screen and to determine if it collided with some given cursor position.
class Button():

    # Set the position and image for a button
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    # Draw button
    def draw(self, screen):

        # blit the button image onto the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # This should be called if a click is detected
    # If the cursor collided with the button's hitbox, return true
    def is_clicked(self, cursor_position):

        return self.rect.collidepoint(cursor_position)



# Type of button that inherets from our normal button
# This type of button will only be able to clicked once after it is drawn to the screen
class ManagedButton(Button):

    did_draw = False

    # Set the position and image for a button
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    # Only when we draw the button to the screen should it be allowed to be clicked
    def draw(self, screen):
        super().draw(screen)
        self.did_draw = True

    # Same as the detecting a click on the regular button
    # but this time only detect a click if the button was drawn to the frame
    def is_clicked(self, cursor_position):
        return self.did_draw and super().is_clicked(cursor_position)



        

# Framework to keep track of all of our buttons
# As of now, only ManagedButton instances will go into this
class ButtonManager():

    # List of buttons on constructor
    def __init__(self):
        self.buttons = []

    # Prevent all buttons from being able to be clicked
    # This should be called at the beginning of every frame/gameloop tick
    def reset(self):
        for button in self.buttons:
            button.did_draw = False

    def add_button(self, x, y, image):
        button = ManagedButton(x , y, image)
        self.buttons += [button]
        return button
