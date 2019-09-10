import numpy as np
import matplotlib.pyplot as plt

#Function defining the initial and analytic solution
def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2),0)
    
#Put everything inside a main fucntion to avoid global variables
def main():
    #setup space, initial phi profile and Courant number
    nx = 40 #number of points in space
    nt = 400 #number of time steps - MODIFIED
    c = 0.20 # The Courant number
    #spatial variable going from zero to one inclusive
    x = np.linspace(0.0,1.0,nx+1)
    #Three time levels of the dependent variable, phi
    phi_ftcs = initialBell(x)
    phi_ftbs = initialBell(x)
    phi_ctcs = initialBell(x)
    #phiNew = phi.copy()
    phiOld_ftcs = phi_ftcs.copy()
    phiOld_ftbs = phi_ftbs.copy()
    phiOld_ctcs = phi_ctcs.copy()
    
    #FTCS for all time steps looping over space
    for i in range(1,nt):
        for j in  range(1,nx):
            phi_ftcs[j] = phiOld_ftcs[j] - 0.5*c*(phiOld_ftcs[j+1] - phiOld_ftcs[j-1])
        #apply periodic boundary conditions
        phi_ftcs[0] = phiOld_ftcs[0] - 0.5*c*(phiOld_ftcs[1] - phiOld_ftcs[nx-1])
        phi_ftcs[nx] = phi_ftcs[0]
        #update phi for the next time-step
        phiOld_ftcs = phi_ftcs.copy()
        
        
    #FTBS for all time steps, looping over space
    for i in range(1,nt):
        for j in  range(1,nx):
            phi_ftbs[j] = phiOld_ftcs[j] -c*(phiOld_ftcs[j+1] - phiOld[j-1])
        #apply periodic boundary conditions
        phi_ftcs[0] = phiOld_ftcs[0] - c*(phiOld_ftcs[1] - phiOld_ftcs[nx-1])
        phi_ftcs[nx] = phi_ftcs[0]
        #update phi for the next time-step
        phiOld_ftcs = phi_ftcs.copy()
        
        
        

    #Loop over remaining time steps (nt) using CTCS
    
    #nt = 40
    #for n in range (1,nt):
        #loop over space
        #for j in range (1,nx):
            #phiNew[j] = phiOld[j] - 0.5*c*(phi[j+1] - phiOld[j-1])
        #apply periodic boundary conditions
        #phiNew[0] = phiOld[0] - c*(phi[1] - phi[nx-1])
        #phiNew[nx] = phiNew[0]
        #update phi for the next time-step
        #phiOld = phi.copy()
        #phi = phiNew.copy()
        
    #derived quantities
    u = 1
    dx = 1./nx
    dt = c*dx/u
    t = nt*dt
    
    
    #Plot the solution in comparison to the analyic solution
    plt. plot(x, initialBell(x-u*t), 'k', label = 'analytic')
    plt. plot(x, phi, 'b', label='CTCS')
    plt.legend(loc='best')
    plt.ylabel('$\phi$')
    plt.axhline(0, linestyle=':', color='black')
    plt.show()
    
#Execute the code
main()

