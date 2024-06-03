import pygame as pg
import sys
import math

pg.init()


WIDTH, HEIGHT = 700, 600
GOLD = (255, 215, 0)
WHITE = (0, 0, 0)


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Solar System Simulation")


def draw_orbit(xc, yc, rx, ry, color):
    pg.draw.ellipse(screen, color, [xc-rx, yc-ry, 2*rx, 2*ry], 1)


def main():
    orbit_radius_x = 200  
    orbit_radius_y = 100  
    orbit_speed = 0.001   
    orbit_angle = 0       

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

       
        screen.fill(WHITE)

        # Draw the sun at the center
        pg.draw.circle(screen, "yellow", (WIDTH//2, HEIGHT//2), 50)

        # Draw the elliptical orbits
        draw_orbit(WIDTH//2, HEIGHT//2, 200, 100, GOLD)
        draw_orbit(WIDTH//2, HEIGHT//2, 300, 150, GOLD)
        draw_orbit(WIDTH//2, HEIGHT//2, 350, 200, GOLD)
        draw_orbit(WIDTH//2, HEIGHT//2, 400, 250, GOLD)

        # Calculate the positions of orbiting planets
        planet1_x = WIDTH//2 + orbit_radius_x * math.cos(orbit_angle)
        planet1_y = HEIGHT//2 + orbit_radius_y * math.sin(orbit_angle)
        planet2_x = WIDTH//2 + orbit_radius_x * 1.5 * math.cos(orbit_angle * 0.7)
        planet2_y = HEIGHT//2 + orbit_radius_y * 1.5 * math.sin(orbit_angle * 0.7)
        planet3_x = WIDTH//2 + orbit_radius_x * 1.75 * math.cos(orbit_angle * 0.6)
        planet3_y = HEIGHT//2 + orbit_radius_y * 2 * math.sin(orbit_angle * 0.6)
        planet4_x = WIDTH//2 + orbit_radius_x * 1.75 * math.cos(orbit_angle * 0.8)
        planet4_y = HEIGHT//2 + orbit_radius_y * 2 * math.sin(orbit_angle * 0.8)
        planet5_x = WIDTH//2 + orbit_radius_x * 2 * math.cos(orbit_angle * 1)
        planet5_y = HEIGHT//2 + orbit_radius_y *2.25 * math.sin(orbit_angle * 1)

        # Draw the orbiting planets
        pg.draw.circle(screen, "red", (int(planet1_x), int(planet1_y)), 20)
        pg.draw.circle(screen, "green", (int(planet2_x), int(planet2_y)), 15)
        pg.draw.circle(screen, "pink", (int(planet3_x), int(planet3_y)), 17)
        pg.draw.circle(screen, "blue", (int(planet4_x), int(planet4_y)), 20)
        pg.draw.circle(screen, "orange", (int(planet5_x), int(planet5_y)), 22)

        # Update the orbit angle for the next frame
        orbit_angle += orbit_speed

        # Update the display
        pg.display.flip()

# Run the main function
if __name__ == "__main__":
    main()
