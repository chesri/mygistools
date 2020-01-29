#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Chris
#
# Created:     06/09/2018
# Copyright:   (c) Chris 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def getMaidenhead(coord, axis):
    # ai is interval for field
    # bi is interval for subgrid
    # ci is interval for sub-subgrid
    if axis == 'lon':
        low = -180
        high = 180
        ai = 20
        bi = 2
        ci = 0.08333333333333333
    if axis == 'lat':
        low = -90
        high = 90
        ai = 10
        bi = 1
        ci = 0.041666666666666664

    a_index = 0
    for a in range(low,high,ai):
        if coord >= a and coord < (a+ai):
            string = '{}/{}:{}'.format(a,a+ai,'ABCDEFGHIJKLMNOPQR'[a_index])
            ra = 'ABCDEFGHIJKLMNOPQR'[a_index]
            ##print(string)

            b_index = 0
            for b in range(a,a+ai,bi):
                if coord >= b and coord < (b+2):
                    string = '{}/{}:{}'.format(b,b+2,'0123456789'[b_index])
                    rb = '0123456789'[b_index]
                    ##print(string)

                    gap = ci
                    c_index = 0
                    # create variable "d" to do math on/walk across grid
                    d = b
                    for c in range(0,23):
                        if coord >= d and coord < (d+gap):
                            string = '{}/{}:{}'.format(d,d+gap,'abcdefghijklmnopqrstuvwxyz'[c_index])
                            rc = 'abcdefghijklmnopqrstuvwxyz'[c_index]
                            ##print(string)
                        d = d + gap
                        c_index += 1

                b_index += 1
        a_index += 1
    return ra,rb,rc

a,c,e = getMaidenhead(-80.817,'lon')
b,d,f = getMaidenhead(35.048,'lat')
print(a+b+c+d+e+f)