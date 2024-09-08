import pygame
import sys

def draw_png_pixel_by_pixel(image_path, pixel_size=5, delay=10):
    # Initialize Pygame
    pygame.init()

    # Load the image
    image = pygame.image.load(image_path)

    # Set up the display with the correct size
    width, height = image.get_size()
    screen = pygame.display.set_mode((width * pixel_size, height * pixel_size))
    pygame.display.set_caption('Draw Image Pixel by Pixel')

    # Convert the image for faster pixel access
    image = image.convert()

    # Main loop
    running = True
    for y in range(height):
        for x in range(width):
            # Get the color of the pixel
            color = image.get_at((x, y))
            # Fill a rectangle with the color
            pygame.draw.rect(screen, color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

            # Control the speed of drawing
            pygame.time.delay(delay)  # Delay in milliseconds

        # Update the display after each row
        pygame.display.flip()

        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    # Final update to display the last pixels
    pygame.display.flip()

    # Wait for the user to close
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

# Example usage
draw_png_pixel_by_pixel('sudasi.jpg', pixel_size=2, delay=0)  # Adjust delay as needed