# Class for buttons
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
    
class ManagedButton(Button):

    did_draw = False

    # Set the position and image for a button
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    def draw(self, screen):
        super().draw(screen)
        self.did_draw = True

    # If it drew the frame and is clicked
    def is_clicked(self, cursor_position):
        return self.did_draw and super().is_clicked(cursor_position)
        
        
class ButtonManager():

    # List of buttons
    def __init__(self):
        self.buttons = []

    def reset(self):
        for button in self.buttons:
            button.did_draw = False

    def add_button(self, x, y, image):
        button = ManagedButton(x , y, image)
        self.buttons += [button]
        return button