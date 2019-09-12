#!/usr/bin/env python
# coding=utf-8

'''
@author: Yingchun Zhang  modified by Xiaoyu Zhang
@e-mail: yczhang@smail.nju.edu.cn
@time: 2019/6/5 11:36
@org: Nanjing University
'''

# units real in lammps: kcal/mol for energy; kcal/mol/A for force; A for length
# units in ASE: eV for energy; A for length;


#dirName = r'D:\simulationBackup\amp\reaxff-as-training-data\water\md-1/'
dirName = r'./'
lmpTrajFileName = 'XDATCAR'
lmpForceFileName = 'PosAndForce'
lmpOutFileName = 'pot_en'
energyName = 'energy.raw'
forceName = 'force.raw'
coordName = 'coord.raw'
typeName = 'type.raw'
boxName = 'box.raw'

lmpTraj = open(dirName + lmpTrajFileName, 'r')
traj = lmpTraj.read().split('Direct configuration=')[0:1]    #divide the diffenrent part
lmpTraj.close()

lmpTrajAndForce = open(dirName + lmpForceFileName, 'r')
ForceAndTraj = lmpTrajAndForce.read().split('POSITION')[0:]    #divide the diffenrent part
ForceAndTraj = ForceAndTraj[1:]
print(ForceAndTraj[1])
lmpTraj.close()

infor = traj[0]
hhh = infor.split('\n')
print(len(hhh))
print(hhh[3])
ax, bx, by, cz = float(hhh[2].split(  )[0]), float(hhh[3].split(  )[0]), float(hhh[3].split(  )[1]), float(hhh[4].split(  )[2])
print(ax, bx, by, cz)
ele1 = hhh[5].split(  )[0]
ele2 = hhh[5].split(  )[1]
print(ele1, ele2)
num_ele1 = int(hhh[6].split(  )[0])
num_ele2 = int(hhh[6].split(  )[1])
print(num_ele1, num_ele2)

outFile = open(dirName + lmpOutFileName, 'r')
out = outFile.readlines()
outFile.close()

type_ = open(dirName + typeName, 'w')
coord_ = open(dirName + coordName, 'w')
force_ = open(dirName + forceName, 'w')
energy_ = open(dirName + energyName, 'w')
box_ = open(dirName + boxName, 'w')
nAtoms = num_ele1 + num_ele2
for iframe, xtraj in enumerate(ForceAndTraj):
    print(iframe)
    print(xtraj)
    while iframe < 2000 and iframe % 20 == 0:
        lines = xtraj.split('\n')

        print('%8.6f 0.0 0.0 %8.6f %8.6f 0.0 0.0 0.0 %8.6f' % (ax, bx, by, cz), file=box_)
        print('%15.8f' % (float(out[iframe])), file=energy_)
        for i in range(nAtoms):
            tmp = lines[i + 2].split()
            if i < num_ele1:
                coord_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[0]), float(tmp[1]), float(tmp[2])))
                force_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[3]), float(tmp[4]), float(tmp[5])))
            else:
                coord_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[0]), float(tmp[1]), float(tmp[2])))
                force_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[3]), float(tmp[4]), float(tmp[5])))

        coord_.write("\n")
        force_.write('\n')
        break

    while iframe >= 2000 and iframe % 20 == 0:
        lines = xtraj.split('\n')

        print('%8.6f 0.0 0.0 %8.6f %8.6f 0.0 0.0 0.0 %8.6f' % (ax, bx, by, cz), file=box_)
        print('%15.8f' % (float(out[iframe])), file=energy_)
        for i in range(nAtoms):
            tmp = lines[i + 2].split()
            if i < num_ele1:
                coord_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[0]), float(tmp[1]), float(tmp[2])))
                force_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[3]), float(tmp[4]), float(tmp[5])))
            else:
                coord_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[0]), float(tmp[1]), float(tmp[2])))
                force_.write('%12.9f  %12.9f  %12.9f  ' % (float(tmp[3]), float(tmp[4]), float(tmp[5])))

        coord_.write("\n")
        force_.write('\n')
        break

for ii in range(nAtoms):
    if ii < num_ele1:
        type_.write('0 ')
    else:
        type_.write('1 ')

energy_.close()
coord_.close()
force_.close()
box_.close()
type_.close()



