import math
import pyqtgraph
import numpy as np
import sys
import matplotlib.pyplot as plt

class GpsUtils:
	#WGS-84 geodetic constants
        a = 6378137           # WGS-84 Earth semimajor axis (m)
        b = 6356752.3142    # WGS-84 Earth semiminor axis (m)
        f = (a - b) / a       # Ellipsoid Flatness
        e_sq = f * (2 - f)    # Square of Eccentricity

        def __init__(self):
                self.x= []
                self.y = []
                self.z = []
                self.tm = []
                self.xEast = []
                self.yNorth = []
                self.zUp = []
                
        def GeodeticToENU(self,lat0,lon0,h0:
		# Convert to radians in notation consistent with the paper:
                #v = open('auto_bad.txt', 'rb')
                v = open('auto_bad','rb')
                v.read()
		#c = bytearray(v)
		#c.decode('ansi')
		#print(c)
                if "GPGGA" in v:
                        for i, line in enumerate(v):
			
				#if "*" in line:
					#line_str = str(line)
                                _id,time, lat, lat_h, lon, lon_h, mode, num_sat, hdop, alt, units_alt, el_geo, ak, asd, crc = line.split(',')					
                                deg_lat = float(lat[0:2])
                                minute_lat = float(lat[2:12])/60
                                degres_lat = deg_lat + minute_lat

                                if "S" in lat_h:
                                        degres_lat = - degres_lat

                                c = math.radians(degres_lat)

                                deg_lon = float(lon[0:3])
                                minute_lon = float(lon[3:13])/60
                                degres_lon = deg_lon + minute_lon

                                if "W" in lon_h:
                                        degres_lon = - degres_lon

                                phi = math.radians(float(degres_lon))
                                s = math.sin(c)
                                N = GpsUtils.a /math.sqrt(1 - GpsUtils.e_sq * s * s)
                                sin_lambda = math.sin(c)
                                cos_lambda = math.cos(c)
                                cos_phi = math.cos(phi)
                                sin_phi = math.sin(phi)
                                self.x=(((float(alt) + float(el_geo)) + N) * cos_lambda * cos_phi)
                                self.y=( ((float(alt) + float(el_geo)) + N) * cos_lambda * sin_phi)
                                self.z=(((float(alt) + float(el_geo)) + (1 - GpsUtils.e_sq) * N) * sin_lambda)
				#self.tm.append(float(time))
				#self.x.append(((float(alt) + float(el_geo)) + N) * cos_lambda * cos_phi)
				#self.y.append( ((float(alt) + float(el_geo)) + N) * cos_lambda * sin_phi)
				#self.z.append(((float(alt) + float(el_geo)) + (1 - GpsUtils.e_sq) * N) * sin_lambda)
                                self.tm.append(float(time))
				#print(self.x,self.y,self.z)				
				#self.lont.append(y)
				#self.altt.append(z)	
				#print(self.latt,self.lont,altt)
				#a = [0,1,2,3,4,5,6,7,8,9]		
                                
		
                                ca = math.radians(lat0)
                                phi_ = math.radians(lon0)
                                sa = math.sin(ca)
                                N1 = GpsUtils.a / math.sqrt(1 - GpsUtils.e_sq * sa * sa)

                                sin_l = math.sin(ca)
                                cos_l = math.cos(ca)
                                cos_phi_ = math.cos(phi_)
                                sin_phi_ = math.sin(phi_)
                                
                                x0 = (h0 + N1) * cos_l * cos_phi_
                                y0 = (h0 + N1) * cos_l * sin_phi_
                                z0 = (h0 + (1 - GpsUtils.e_sq) * N1) * sin_l

                                xd = self.x - 2829172.4960228447
                                yd = self.y -  2208069.078376276
                                zd = self.z - 5255182.548548596
				
				#This is the matrix multiplication
                                self.xEast.append(- sin_phi_ * xd + cos_phi_ * yd)
                                self.yNorth.append(-cos_phi_ * sin_l * xd - sin_l * sin_phi_ * yd + cos_l * zd)
                                self.zUp.append(cos_l * cos_phi_ * xd + cos_l * sin_phi_* yd + sin_l * zd)
				#print(self.xEast)
def main():
        obj = GpsUtils()
        obj.GeodeticToENU(55.849259,37.970779,153.817703)
        
       # plt.plot(obj.tm,obj.xEast)
       # plt.plot(obj.tm,obj.yNorth)
       # plt.plot(obj.tm,obj.zUp)
        
        plt.show()
       # pyqtgraph.plot(obj.tm, obj.zUp)
        #pg.plot(obj.tm, obj.yNorth)
        #pg.plot(obj.tm, obj.zUp)
        
if __name__ == '__main__':
        main()
	
