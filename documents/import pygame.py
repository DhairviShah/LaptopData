import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line Following Robot Simulation")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
purple = (128, 0, 128)

# Robot parameters
robot_width = 50
robot_height = 30

# Generate a straight road pattern
def generate_straight_road():
    road_segments = [height // 2] * (width // 100)
    return road_segments

road_segments = generate_straight_road()

# Robot starts at the end of the straight line
robot_x = (len(road_segments) - 1) * 100 - robot_width
robot_y = road_segments[-1] - robot_height // 2

# Set up clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update robot position based on straight road
    closest_segment_index = min(range(len(road_segments)), key=lambda i: abs(road_segments[i] - robot_y))
    closest_segment = road_segments[closest_segment_index]

    # Center the robot on the road vertically
    if robot_y > closest_segment:
        robot_y -= 1
    elif robot_y < closest_segment:
        robot_y += 1

    # Move the robot horizontally along the straight road
    if robot_x > 0:
        robot_x -= 1

    # Draw the background
    screen.fill(white)

    # Draw the thicker road
    pygame.draw.lines(screen, red, False, [(i * 100, h) for i, h in enumerate(road_segments)])

    # Draw the robot
    pygame.draw.rect(screen, purple, (robot_x, robot_y, robot_width, robot_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
