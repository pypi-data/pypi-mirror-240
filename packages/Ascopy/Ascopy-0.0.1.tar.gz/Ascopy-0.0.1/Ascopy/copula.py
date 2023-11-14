# version: 2023_09_12_11_27

from scipy import stats
import numpy as np
from scipy import special
from scipy.stats import multivariate_t
import warnings
warnings.filterwarnings('ignore')



def copula1(u,v,theta):
    C=(u**(-theta) + v**(-theta)-1)**(-1/theta)
    copula_1=(-(-1-1/theta))*theta*u**(-1-theta)*v**(-1-theta)*(-1+u**(-theta)+v**(-theta))**(-2-1/theta)
    judge = C>0
    for i in range(len(u)):
        if not judge[i]:
            copula_1[i]=0.0     
#    if C>0:
#        copula_1=(-(-1-1/theta))*theta*u**(-1-theta)*v**(-1-theta)*(-1+u**(-theta)+v**(-theta))**(-2-1/theta)
#    else:
#        copula_1=0
    return copula_1

def copula2(u,v,theta):
    C=1-((1-u)**theta+(1-v)**theta)**(1/theta)
    copula_2=(-1+theta)*(1-u)**(-1+theta)*((1-u)**theta+(1-v)**theta)**(-2+1/theta)*(1-v)**(-1+theta)
    judge = C>0
    for i in range(len(u)):
        if not judge[i]:
            copula_2[i]=0.0
#    if C>0:
#        copula_2=(-1+theta)*(1-u)**(-1+theta)*((1-u)**theta+(1-v)**theta)**(-2+1/theta)*(1-v)**(-1+theta)
#    else:
#        copula_2=0
    return copula_2

def copula3(u,v,theta):
    #C=u*v/(1-theta*(1-u)*(1-v))
    copula_3=((1-theta*(1-u)*(1-v))*(1-theta)+2*theta*u*v)/(1-theta*(1-u)*(1-v))**3
    return copula_3

def copula4(u,v,theta):
    #from math import*
    #C=np.exp(-((-np.log(u))**theta+(-np.log(v))**theta)**(1/theta))    
    copula_4=(1/(u*v))*(((-np.log(u))**(-1+theta)*(-1+theta+((-np.log(u))**theta+(-np.log(v))**theta)**(1/theta)) 
     * ((-np.log(u))**theta+(-np.log(v))**theta)**(-2+1/theta)*(-np.log(v))**(-1+theta))/np.exp((-np.log(u))**theta+(-np.log(v))**theta)**(1/theta))

    return copula_4

def copula5(u,v,theta):
    #from math import*
    #C=(-1/theta)*np.log(1+((np.exp(-theta*u)-1)*(np.exp(-theta*v)-1)/(np.exp(-theta)-1)))    
    copula_5=((np.exp(theta)-1)*theta*np.exp(theta*(u+v+1)))/(np.exp(theta*(u + v))-np.exp(theta*u+theta)-np.exp(theta*v+theta)+np.exp(theta))**2
    return copula_5

def copula6(u,v,theta):
    #C=1-((1-u)**theta+(1-v)**theta-(1-u)**theta*(1-v)**theta )**(1/theta)
    copula_6=(1-u)**(-1+theta)*(theta-(-1+(1-u)**theta)*(-1+(1-v)**theta))*((1-u)**theta+(1-v)**theta-(1-u)**theta*(1-v)**theta)**(-2+1/theta)*(1-v)**(-1+theta)
    return copula_6

def copula7(u,v,theta):
    C=theta*u*v+(1-theta)*(u+v-1)
    copula_7=u*0.0 + theta
    judge = C>0
    for i in range(len(u)):
        if not judge[i]:
            copula_7[i]=0.0 
    return copula_7

def copula8(u,v,theta):
    C=(theta*theta*u*v-(1-u)*(1-v))/(theta**2-(theta-1)**2*(1-u)*(1-v))
    copula_8=-((2*(-1+theta)*theta**3*(1+(-1+theta)*u)*(1+(-1+theta)*v))/(theta**2*(u*(-1+v)-v)+(-1+u)*(-1+v)+2*theta*(-1+u+v-u*v))**3)
    judge = C>0
    for i in range(len(u)):
        if not judge[i]:
            copula_8[i]=0.0 
#    if C>0:
#        copula_8=-((2*(-1+theta)*theta**3*(1+(-1+theta)*u)*(1+(-1+theta)*v))/(theta**2*(u*(-1+v)-v)+(-1+u)*(-1+v)+2*theta*(-1+u+v-u*v))**3)
#    else:
#        copula_8=0
    return copula_8

def copula9(u,v,theta):
    #from math import*
    #C=u*v*np.exp(-theta*np.log(u)*np.log(v))
    copula_9=(1-theta-theta*np.log(v)+theta*np.log(u)*(-1+theta*np.log(v)))/u**(theta*np.log(v))

    return copula_9

def copula10(u,v,theta):
    #C=u*v/(1+(1-u**theta)*(1-v**theta))**(1/theta)
    copula_10=(2-v**theta+u**theta*(-1+v**theta))**(-2-1/theta)*(4-2*v**theta+u**theta*(-2-(-1+theta)*v**theta))
    return copula_10

def copula11(u,v,theta):
    C=((u**theta)*(v**theta)-2*(1-u**theta)*(1-v**theta))**(1/theta)
    copula_11=(theta-1)*(2*theta*(u**(theta-1))*(v**(2*theta-2))-theta*(u**(2*theta-1))*(v**(2*theta-2)))*(((u**theta)*(v**theta)-2*(1-u**theta)*(1-v**theta)))**(1/theta-2)
    judge = C>0
    for i in range(len(u)):
        if not judge[i]:
            copula_11[i]=0.0
#    if C>0:
#        copula_11=(theta-1)*(2*theta*(u**(theta-1))*(v**(2*theta-2))-theta*(u**(2*theta-1))*(v**(2*theta-2)))*(((u**theta)*(v**theta)-2*(1-u**theta)*(1-v**theta)))**(1/theta-2)
#    else:
#        copula_11=0
    return copula_11

def copula12(u,v,theta):
    #C=(1+((1/u-1)**theta+(1/v-1)**theta)**(1/theta))**-1
    copula_12=((-1+1/u)**theta*(-1+theta+((-1+1/u)**theta+(-1+1/v)**theta)**(1/theta)+theta*((-1 + 1/u)**theta+(-1+1/v)**theta)**(1/theta))*((-1+1/u)**theta+(-1+1/v)**theta)**(-2+1/theta)*(-1+1/v)**theta)/((-1+u)*u*(1+((-1+1/u)**theta+(-1+1/v)**theta)**(1/theta))**3*(-1+v)*v)

    return copula_12

def copula13(u,v,theta):
    #from math import*
    #C=np.exp(1-((1-np.log(u))**theta+(1-np.log(v)**theta-1)**(1/theta)))
    copula_13=(1/(u*v))*(np.exp(1-(-1+(1-np.log(u))**theta+(1-np.log(v))**theta)**(1/theta))*(1-np.log(u))**(-1+theta)*(-1+theta+(-1+(1-np.log(u))**theta+(1-np.log(v))**theta)**(1/theta))*(-1+(1-np.log(u))**theta+(1-np.log(v))**theta)**(-2+1/theta)*(1-np.log(v))**(-1+theta))
    return copula_13

def copula14(u,v,theta):
    #C=(1+((u**(-1/theta)-1)**theta+(v**(-1/theta)-1)**theta)**(1/theta))**(-theta)
    copula_14=((-1+u**(-theta**(-1)))**theta*(-1+v**(-theta**(-1)))**theta*((-1+u**(-theta**(-1)))**theta+(-1+v**(-theta**(-1)))**theta)**(-2+1/theta)*(1+((-1+u**(-theta**(-1)))**theta+(-1+v**(-theta**(-1)))**theta)**(1/theta))**(-2-theta)*(-1+theta+2*theta*((-1+u**(-theta**(-1)))**theta+(-1+v**(-theta**(-1)))**theta)**(1/theta)))/(theta*u*(-1+u**(1/theta))*v*(-1+v**(1/theta)))

    return copula_14

def copula15(u,v,theta):
    C=(1-((1-u**(1/theta))**theta+(1-v**(1/theta))**theta))**theta
    copula_15=(-1+theta)*theta*u**(-1+1/theta)*(1-u**(1/theta))**(-1+theta)*v**(-1+1/theta)*(1-v**(1/theta))**(-1+theta)* (1-(1-u**(1/theta))**theta-(1-v**(1/theta))**theta)**(-2+theta)
    judge = C>0
    for i in range(len(u)):
        if not judge[i]:
            copula_15[i]=0.0
#    if C>0:
#        copula_15=(-1+theta)*theta*u**(-1+1/theta)*(1-u**(1/theta))**(-1+theta)*v**(-1+1/theta)*(1-v**(1/theta))**(-1+theta)* (1-(1-u**(1/theta))**theta-(1-v**(1/theta))**theta)**(-2+theta)
#    else:
#        copula_15=0
    return copula_15

#sqrt需要导入math或者numpy包才能用
def copula16(u,v,theta):
    #from math import*
    #C=((u+v-1-theta*(1/u+1/v-1))+((u+v-1-theta*(1/u+1/v-1))**2+4*theta)**(1/2))/2
    copula_16=(2*theta*(theta+u**2)*(theta+v**2))/(np.sqrt(4*theta+(-1+u-theta*(-1+1/u+1/v)+v)**2)*(u**2*v**2*(-1+u+v)**2+theta**2*(u+v-u*v)**2+2*theta*u*v*(u**2*(-1+v)-(-1+v)*v+u*(1-v+ v**2))))
    return copula_16


def copula17(u,v,theta):
    #C=(1+((1+u)**(-theta)-1)*((1-v)**(-theta)-1)/(2**(-theta)-1))**(-1/theta)-1
    copula_17=(2**theta*(2**theta*(-1+(1+u)**theta)*(-1+(1-v)**theta)+(-1+2**theta)*theta*(1+u)**theta*(1-v)**theta))/(1+((-1+(1+u)**(-theta))*(-1+(1-v)**(-theta)))/(-1+2**(-theta)))**theta**(-1)/((1+u)*(2**theta-2**theta*(1+u)**theta-(2-2*v)**theta+(1+u)**theta*(1-v)**theta)**2*(-1+v))
    return copula_17

def copula18(u,v,theta):
    #from math import*
    C=1+theta/np.log(np.exp(theta/(u-1))+np.exp(theta/(v-1)))
    copula_18=(np.exp(theta*(1/(-1+u)+1/(-1+v)))*theta**3*(2+np.log(np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))))/((np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))**2*(-1+u)**2*(-1+v)**2*np.log(np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))**3)
    judge = C>0
    for i in range(len(u)):
        if not judge[i]:
            copula_18[i]=0.0
#    if C>0:
#        copula_18=(np.exp(theta*(1/(-1+u)+1/(-1+v)))*theta**3*(2+np.log(np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))))/((np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))**2*(-1+u)**2*(-1+v)**2*np.log(np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))**3)
#    else:
#        copula_18=0
    return copula_18

def copula19(u,v,theta):
    #from math import*
    #C=theta/np.log(np.exp(theta/u)+np.exp(theta/v)-np.exp(theta))
    copula_19=(np.exp(theta*(1/u+1/v))*theta**3*(2+np.log(-np.exp(theta)+np.exp(theta/u)+np.exp(theta/v))))/((-np.exp(theta)+np.exp(theta/u)+np.exp(theta/v))**2*u**2*v**2*np.log(-np.exp(theta)+np.exp(theta/u)+np.exp(theta/v))**3)
    return copula_19

def copula20(u,v,theta):
    #from math import*
    #C=(np.log(np.exp(u**-theta)+np.exp(v**-theta)-np.exp(1)))**(-1/theta)
    copula_20=(np.exp(u**(-theta)+v**(-theta))*u**(-1-theta)*v**(-1-theta)*np.log(-np.exp(1)+np.exp(u)**(-theta)+np.exp(v)**(-theta))**(-2-1/theta)*(1+theta+theta*np.log(-np.exp(1.0)+np.exp(u)**(-theta)+np.exp(v)**(-theta))))/(-np.exp(1.0)+np.exp(u)**(-theta)+np.exp(v)**(-theta))**2
    return copula_20    
    
def copula21(u,v,theta):  
    #Copula21=gauss copula
    uu=stats.norm.ppf(q=u, loc=0.0, scale=1.0)
    vv=stats.norm.ppf(q=v, loc=0.0, scale=1.0)       
    copula_21 = 1/(np.sqrt(1-theta*theta))*np.exp( (2*theta*uu*vv-theta**2*(uu**2+vv**2))/(2-2*theta*theta))
    return copula_21 

#def copula22(u,v,theta):           # t-Copula    
#    rho,df=theta
#    s1=stats.t.ppf(u,df)
#    s2=stats.t.ppf(v,df)
#    ans=(  np.sqrt(1 - rho**2) * ( (df + s1**2 + s2**2 - 2*s1*s2*rho - df*rho**2)/(df-df*rho**2) )**(-1-df/2) * special.gamma((2 + df)/2)  )  /  ( np.pi*(df - df*rho**2)*special.gamma(df/2) )
#    f1=stats.t.pdf(s1,df)
#    f2=stats.t.pdf(s2,df)
#    copula_22 = ans/f1/f2
#    return copula_22
#    ans1 = rho**(-0.5)*special.gamma((nu+2)/2)*special.gamma(nu/2) / special.gamma((nu+1)/2) / special.gamma((nu+1)/2) 
#    ans2 =  (1 + (s1*s1 + s2*s2 - 2*rho*s1*s2)/(nu*(1-rho*rho)) )**((nu+2)/2)
#    ans3 = (1+s1*s1/nu)**(-(nu+1)/2) * (1+s2*s2/nu)**(-(nu+1)/2)
#    copula_22 = ans1*ans2/ans3
#    return copula_22


def copula22(u,v,theta):           # t-Copula    
    rho,df=theta
    s1=stats.t.ppf(u,df)
    s2=stats.t.ppf(v,df)
    rv = multivariate_t([0, 0], [[1, rho], [rho, 1]], df=df)
    f1=stats.t.pdf(s1,df)
    f2=stats.t.pdf(s2,df)
    pos=np.dstack((s1,s2))
    copula_22 =rv.pdf(pos)/f1/f2
    return copula_22


#def copula22(u,v,theta):           # t-Copula    
#    rho,df=theta
#    s1=stats.t.ppf(u,df)
#    s2=stats.t.ppf(v,df)
#    ga1=special.gamma(df/2)
#    ga2=special.gamma((df+1)/2)
#    if df<=197:
#        ans1=ga1**2 *df/2 / ga2 / ga2            ############??????????????????????
#    else:
#        ans1=df/2   
#    #ans1 = special.gamma((df+2)/2)*special.gamma(df/2) / special.gamma((df+1)/2) / special.gamma((df+1)/2) / np.sqrt(1-rho*rho)
#    ans2 =  (1 + (s1*s1 + s2*s2 - 2*rho*s1*s2)/(df*(1-rho*rho)) )**(-(df+2)/2)
#    ans3 = (1+s1*s1/df)**((df+1)/2) * (1+s2*s2/df)**((df+1)/2)
#    copula_22 = ans1*ans2*ans3
#    return copula_22





#####################################################################################################
#####################################################################################################

def copulas(u,v,theta):
    global num_nelsen
    
    if num_nelsen == 1:  
        ans=copula1(u,v,theta)
    elif num_nelsen == 2: 
        ans=copula2(u,v,theta)
    elif num_nelsen == 3:
        ans=copula3(u,v,theta)  		
    elif num_nelsen == 4: 
        ans=copula4(u,v,theta)  		
    elif num_nelsen == 5: 
        ans=copula5(u,v,theta)  			
    elif num_nelsen == 6: 
        ans=copula6(u,v,theta)
    elif num_nelsen == 7:
        ans=copula7(u,v,theta)
    elif num_nelsen == 8: 
        ans=copula8(u,v,theta)
    elif num_nelsen == 9: 
        ans=copula9(u,v,theta)  		
    elif num_nelsen == 10: 
        ans=copula10(u,v,theta)  		
    elif num_nelsen == 11: 
        ans=copula11(u,v,theta)
    elif num_nelsen == 12: 
        ans=copula12(u,v,theta)
    elif num_nelsen == 13: 
        ans=copula13(u,v,theta)  		
    elif num_nelsen == 14: 
        ans=copula14(u,v,theta)  		
    elif num_nelsen == 15: 
        ans=copula15(u,v,theta)  			
    elif num_nelsen == 16: 
        ans=copula16(u,v,theta)
    elif num_nelsen == 17: 
        ans=copula17(u,v,theta)
    elif num_nelsen == 18: 
        ans=copula18(u,v,theta)
    elif num_nelsen == 19: 
        ans=copula19(u,v,theta)  		
    elif num_nelsen == 20: 
        ans=copula20(u,v,theta) 
    elif num_nelsen == 21: 
        ans=copula21(u,v,theta) 
    elif num_nelsen == 22: 
        ans=copula22(u,v,theta)     
    else:
        print("illegal value for the argument 'num_nelsen'!")
        return
    return ans
        

def set_value (id):
    global num_nelsen
    num_nelsen=id
    
    if num_nelsen == 1:  
        theta_min= 1.0E-05
        theta_max= 1.0E+01         
    elif num_nelsen == 4: 
        theta_min= 2.0E-03
        theta_max= 3.0E+00  	   		
    elif any([num_nelsen==2, num_nelsen==6, num_nelsen==8, num_nelsen==12]):     
        theta_min= 1.0E+00
        theta_max= 5.0E+01  	 
    elif any([num_nelsen==14, num_nelsen==15]):
        theta_min= 1.0E+00
        theta_max= 4.0E+01  	 
    elif num_nelsen == 3: 
        theta_min=-1.0E+00
        theta_max= 0.999999999  	  		
    elif any([num_nelsen==5, num_nelsen==17]):
        theta_min=-1.0E+02
        theta_max= 1.0E+02   	 		
    elif any([num_nelsen==7, num_nelsen==9, num_nelsen==10]):	
        theta_min= 1.0E-05 
        theta_max= 1.0E+00  	 
    elif num_nelsen == 11: 
        theta_min= 1.0E-05 
        theta_max= 0.5E+00  	    		
    elif any([num_nelsen==13, num_nelsen==19, num_nelsen==20]): 
        theta_min= 1.0E-05 
        theta_max= 1.0E+02  	  
    elif num_nelsen == 16: 
        theta_min= 1.0E-05 
        theta_max= 1.0E+03  	  
    elif num_nelsen == 18:	 
        theta_min= 2.0E+00 
        theta_max= 1.0E+02  	 
    elif any([num_nelsen==21, num_nelsen==22]):
        theta_min= -0.9999 
        theta_max= 0.9999  	   		 
    else:
        return
    return np.array([theta_min,theta_max]) 


 
######################################################################################

def copula1a(u,v,theta):
    C=(u**(-theta) + v**(-theta)-1)**(-1/theta)   
    if C>0:
        copula_1=(-(-1-1/theta))*theta*u**(-1-theta)*v**(-1-theta)*(-1+u**(-theta)+v**(-theta))**(-2-1/theta)
    else:
        copula_1=0
    return copula_1

def copula2a(u,v,theta):
    C=1-((1-u)**theta+(1-v)**theta)**(1/theta)
    if C>0:
        copula_2=(-1+theta)*(1-u)**(-1+theta)*((1-u)**theta+(1-v)**theta)**(-2+1/theta)*(1-v)**(-1+theta)
    else:
        copula_2=0
    return copula_2

def copula7a(u,v,theta):
    C=theta*u*v+(1-theta)*(u+v-1)
    if C>0.0:
        copula_7=theta
    else:
        copula_7=0.0
    return copula_7

def copula8a(u,v,theta):
    C=(theta*theta*u*v-(1-u)*(1-v))/(theta**2-(theta-1)**2*(1-u)*(1-v))
    if C>0:
        copula_8=-((2*(-1+theta)*theta**3*(1+(-1+theta)*u)*(1+(-1+theta)*v))/(theta**2*(u*(-1+v)-v)+(-1+u)*(-1+v)+2*theta*(-1+u+v-u*v))**3)
    else:
        copula_8=0
    return copula_8


def copula11a(u,v,theta):
    C=((u**theta)*(v**theta)-2*(1-u**theta)*(1-v**theta))**(1/theta)
    if C>0:
        copula_11=(theta-1)*(2*theta*(u**(theta-1))*(v**(2*theta-2))-theta*(u**(2*theta-1))*(v**(2*theta-2)))*(((u**theta)*(v**theta)-2*(1-u**theta)*(1-v**theta)))**(1/theta-2)
    else:
        copula_11=0
    return copula_11


def copula15a(u,v,theta):
    C=(1-((1-u**(1/theta))**theta+(1-v**(1/theta))**theta))**theta
    if C>0:
        copula_15=(-1+theta)*theta*u**(-1+1/theta)*(1-u**(1/theta))**(-1+theta)*v**(-1+1/theta)*(1-v**(1/theta))**(-1+theta)* (1-(1-u**(1/theta))**theta-(1-v**(1/theta))**theta)**(-2+theta)
    else:
        copula_15=0
    return copula_15


def copula18a(u,v,theta):
    #from math import*
    C=1+theta/np.log(np.exp(theta/(u-1))+np.exp(theta/(v-1)))
    if C>0:
        copula_18=(np.exp(theta*(1/(-1+u)+1/(-1+v)))*theta**3*(2+np.log(np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))))/((np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))**2*(-1+u)**2*(-1+v)**2*np.log(np.exp(theta/(-1+u))+np.exp(theta/(-1+v)))**3)
    else:
        copula_18=0
    return copula_18

 
def copulae(u,v,theta):
    global num_nelsen
    
    if num_nelsen == 1:  
        ans=copula1a(u,v,theta)
    elif num_nelsen == 2: 
        ans=copula2a(u,v,theta)
    elif num_nelsen == 3:
        ans=copula3(u,v,theta)  		
    elif num_nelsen == 4: 
        ans=copula4(u,v,theta)  		
    elif num_nelsen == 5: 
        ans=copula5(u,v,theta)  			
    elif num_nelsen == 6:
        ans=copula6(u,v,theta)
    elif num_nelsen == 7:
        ans=copula7a(u,v,theta)
    elif num_nelsen == 8: 
        ans=copula8a(u,v,theta)
    elif num_nelsen == 9: 
        ans=copula9(u,v,theta)  		
    elif num_nelsen == 10: 
        ans=copula10(u,v,theta)  		
    elif num_nelsen == 11: 
        ans=copula11a(u,v,theta)
    elif num_nelsen == 12: 
        ans=copula12(u,v,theta)
    elif num_nelsen == 13: 
        ans=copula13(u,v,theta)  		
    elif num_nelsen == 14: 
        ans=copula14(u,v,theta)  		
    elif num_nelsen == 15: 
        ans=copula15a(u,v,theta)  			
    elif num_nelsen == 16: 
        ans=copula16(u,v,theta)
    elif num_nelsen == 17: 
        ans=copula17(u,v,theta)
    elif num_nelsen == 18: 
        ans=copula18a(u,v,theta)
    elif num_nelsen == 19: 
        ans=copula19(u,v,theta)  		
    elif num_nelsen == 20: 
        ans=copula20(u,v,theta) 
    elif num_nelsen == 21: 
        ans=copula21(u,v,theta) 
    elif num_nelsen == 22:
        ans=copula22(u,v,theta)
    else:
        print("illegal value for the argument 'num_nelsen'!")
        return
    return ans    
    
    
