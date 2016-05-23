import numpy as np
import matplotlib.pyplot as plt
import glob
import os

cell='4'
measno='4'

filename='N:/data/emily/magnetometer_test/cell{1:s}/remote/meas{0:s}'.format(str(measno), str(cell))
files=glob.glob(filename+"/*0.csv")
files=sorted(files)

start=50


a=np.loadtxt(files[0], delimiter=',')
b=np.sum(a[start:,:], axis=0)




datanew=np.zeros([len(b), len(files)])

for i in range(len(files)):
	data=np.loadtxt(files[i], delimiter=',')
	datanew[:,i]=np.mean(data[start:,:], axis=0)

plt.plot(datanew[:,1])

# # limmax=15
# # limmin = 0.5
# # cs=plt.contourf(datanew, levels=np.linspace(limmin, limmax, limmax*10), cmap=plt.cm.jet, extend="both")
# # cs.cmap.set_under('k')
# # cs.set_clim(limmin, limmax)
# # cb=plt.colorbar(cs)
# # plt.xlabel("B0 Offset")
# # plt.ylabel("Frequency (Hz)")
# # plt.show()
# # plt.savefig(filename+"/all_together{0:s}.png".format(measno) )
X,Y = np.meshgrid(np.arange(0,datanew.shape[1],1), np.arange(100, 4100,100))
z_min=2
z_max=12
plt.pcolor(X,Y, datanew, cmap="gnuplot")
plt.axis([X.min(), X.max(), Y.min(), Y.max()])
plt.xlabel('R3 Offset (mV)')
plt.ylabel('B1 Frequency (Hz)')
plt.colorbar()
plt.show()
plt.savefig(filename+"/all_together{0:s}.png".format(measno))

# cell='4'
# measurement = '44'
# folder = 'N:\\data\\emily\\magnetometer\\cell{1:s}\\remote\\meas{0:s}'.format(str(measurement), str(cell))

# files = glob.glob(os.path.join(folder, 'b0offset0.089V_fft.csv'))
# #files=glob.glob(folder+"/*sweep0.500V_B1amp.csv")
# data=np.loadtxt(files, delimiter=',')
# plt.plot(data)
# plt.show()
# # files=sorted(files)
# shape = [len(files), 10001, 96]
# data = np.zeros(shape)
# for i, f in enumerate(files):
#     c_data = np.loadtxt(f, delimiter=',')
#     data[i,:,:] = c_data


# cum_data = np.sum(data, axis=2)
# cum_data_shape = cum_data.shape

# # X, Y = np.meshgrid(
# #     np.arange(0, cum_data_shape[1], 1),
# #     np.arange(0, cum_data_shape[0], 1)
# # )

# # z_min=1
# # z_max=6
# # plt.axis([X.min(), X.max(), Y.min(), Y.max()])
# # plt.pcolor(X, Y, cum_data,  cmap="hsv", vmin=z_min, vmax=z_max)
# # plt.colorbar()
# # plt.show()

# plt.matshow(cum_data, aspect='auto')

# plt.show()