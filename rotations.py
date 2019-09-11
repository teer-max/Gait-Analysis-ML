import numpy as np

def rotation_3d(vector,angle,str):
    c, s = np.cos(angle), np.sin(angle)

    if str == 'x':
        R = np.array([(1,0,0),(0,c,-s),(0,s,c)])
    elif str == 'y':
        R = np.array([(c,0,s),(0,1,0),(-s,0,c)])
    elif str == 'z':
        R = np.array([(c,-s,0),(s,c,0),(0,0,1)])
    else:
        print("improper choice for axis")

    return np.matmul(vector, R)

def getangle(a,b):
    theta = np.arctan(a/b)
    return theta
def reorient(data, restingmean,**kwargs):
    #Get angle between x,z

    theta = getangle(restingmean[0],restingmean[2])
    #rotate that angle by theta to eliminate x
    oriented_data = rotation_3d(data,theta,'y')
    oriented_rest = rotation_3d(restingmean,theta,'y')

    #repeat that again but for angle between y and z
    theta2 = getangle(oriented_rest[1],oriented_rest[2])
    reoriented_data = rotation_3d(oriented_data,-theta2,'x')
    reoriented_rest = rotation_3d(oriented_rest,-theta2,'x')

    if('bentmean' in kwargs):
        oriented_bent = rotation_3d(kwargs['bentmean'], theta, 'y')
        #print("Oriented Bent Vector is:", oriented_bent)
        reoriented_bent = rotation_3d(oriented_bent,-theta2,'x')
        #print("Reoriented Bent Vector is:", reoriented_bent)

        theta3 = getangle(oriented_bent[1], oriented_bent[0])

        final_bent = rotation_3d(reoriented_bent,theta3,'z')
        #print("Final Bent vector should be of form [x,0,z]:",final_bent)

        d = rotation_3d(reoriented_data, theta3, 'z')

        return d
    else:
        #Check
        #print("Reoriented Rest vector is:", str(reoriented_rest))

        return reoriented_data

