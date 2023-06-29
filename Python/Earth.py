from vpython import *

def sim(power: int = 2):
    # simulate the motion of the earth around the sun

    # define constants
    G = 6.67408e-11

    # mas of the sun
    m_sun = 1.9891e30

    # radius of the sun (not to scale)
    # r_sun = 6.9634e8
    r_sun = 5e10

    # mass of the earth
    m_earth = 5.9722e29 / 4

    # radius of the earth (not to scale)
    # r_earth = 6.367e6
    r_earth = 3e9

    # mass of the moon
    m_moon = 7.348e22

    # radius of the moon (not to scale)
    # r_moon = 1.737e6
    r_moon = 3e9

    # create the objects
    sun = sphere(pos=vector(0, 0, 0), radius=r_sun, color=color.yellow)

    earth = sphere(pos=vector(1.496e11, 0, 0), radius=r_earth, texture=textures.earth, make_trail=True)

    moon = sphere(pos=vector(1.496e11 + 1.19e10, 0, 0), radius=r_moon, color=color.red, make_trail=True)
    # moon = sphere(pos=vector(1.496e11 * 1.3, 0, 0), radius=r_moon, color=color.red, make_trail=True)

    # Calculate velocity needed to maintain a uniform circular orbit around the sun for the earth
    v = sqrt(G * m_sun / (mag(earth.pos) ** (power - 1)))
    # print(v)

    # Calculate velocity for the moon
    v_moon_earth = sqrt(G * m_earth / (mag(moon.pos - earth.pos) ** (power - 1)))
    v_moon_sun = sqrt(G * m_sun / (mag(moon.pos) ** (power - 1)))

    earth.velocity = vector(0, v, 0)
    moon.velocity = vector(0, v_moon_sun - v_moon_earth, 0)
    v_moon = vector(0, v_moon_earth, 0)

    # define initial time
    t = 0

    # define time interval
    dt = 3600

    while t < 1e10:
        rate(3000) 
        earth.pos = earth.pos + earth.velocity * dt
        r_vector = earth.pos - sun.pos
        F_grav = -(G * m_sun * m_earth) / (mag(r_vector) ** power) * (norm(r_vector))
        earth.velocity = earth.velocity + (F_grav / m_earth) * dt
        moon.pos = moon.pos + moon.velocity * dt
        r_vector_moon_sun = moon.pos - sun.pos
        F_grav_moon_sun = -(G * m_sun * m_moon) / (mag(r_vector_moon_sun) ** power) * (norm(r_vector_moon_sun))
        r_vector_moon_earth = moon.pos - earth.pos
        F_grav_moon_earth = -(G * m_earth * m_moon) / (mag(r_vector_moon_earth) ** power) * (norm(r_vector_moon_earth))
        moon.velocity = moon.velocity + (F_grav_moon_sun / m_moon + F_grav_moon_earth / m_moon) * dt
        t += dt

def main():
    sim()

if __name__ == "__main__":
    main()