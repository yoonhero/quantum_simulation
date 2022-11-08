from vpython import *

# Defining Display

scene2 = canvas(width=500,height=500,background = vector(1,1,1))

# Defining Constants
e = 1.6021765e-19 # Charge of Electron
a0 = 0.529177e-10 # Radius of first orbit
m_p = 1.6726219e-27 # Mass of Proton

#Defining 3D Objects
nucleus = sphere(pos = vector(0,0,0), radius = 0.1*a0, velocity = vector(0,0,0), mass = m_p, charge = e, color = color.yellow)

# Electron 3d object
class Electron():
    m_e = 9.10938356e-31 # Mass of Electron
    e = 1.6021765e-19 # Charge of Electron
    a0 = 0.529177e-10 # Radius of first orbit
    epsilon = 8.854187e-12 # Permittivity of free space

    def __init__(self, init_pos):
        self.pi = 2*asin(1.0) # Defining value of pi using sin(pi/2) = 1
        self.a0 = Electron.a0
        self.m_e = Electron.m_e
        self.e = Electron.e
        self.epsilon = Electron.epsilon

        self.init_pos = init_pos
        self.v_e = self.e/sqrt(4*self.pi*self.epsilon*self.a0*self.m_e) # Using Classical Physics: mv^2/r = e^2/(4*pi*epsilon*r^2)

        self.electron = sphere(pos = vector(self.init_pos,0,0), radius = 0.02*self.a0, velocity = vector(0,self.v_e,0), mass = self.m_e, charge = -self.e, color = color.red)
        self.electron.trail = curve(color=self.electron.color)

        self.T_orbit = 2.*self.pi*self.a0/self.v_e
        self.dt = self.T_orbit/1000.


    #Defining function for Calculating Acceleration
    def acc(self, pos, charge):
        dr=( self.electron.pos - pos)
        Force = 1./(4.*self.pi*self.epsilon)*charge*self.electron.charge/(mag(dr)**2) * norm(dr)
        m1 = self.electron.mass
        return Force/m1

    # update electon's position
    def update(self, pos, charge):
        
        self.electron.velocity = self.electron.velocity + self.acc(pos, charge)*self.dt
        self.electron.pos = self.electron.pos + self.electron.velocity*self.dt 
        # self.electron.trail.append(pos = self.electron.pos)


# class Atom():
#     def __init__(self, shells, electrons):
#         self.max_electrons = [2, 8, 18, 32]
#         self.shells = [[]] * shells

#         t = 0
#         for i in range(electrons):
#             if sum(self.max_electrons[0:t+1]) > i+1:
#                 t += 1
#             shells[i] = Electron(a0)


# class Hydrogen(Atom):



electron1 = Electron(a0)
electron2 = Electron(a0)

t = 0
t_end = 1000*electron1.T_orbit

#Updating Position of Electron in loop
while (t<t_end):
    rate(100)

    t = t+electron1.dt

    electron1.update(nucleus.pos, nucleus.charge)
    if t>7.963903871003342e-17:
        electron2.update(nucleus.pos, nucleus.charge)

  