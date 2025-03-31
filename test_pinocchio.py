import pinocchio

model = pinocchio.buildModelFromUrdf("/home/irc306/yrProject/pinocchio/jaka_description/jaka_zu18.urdf")
print(f"model name: {model.name}")
print(type(model))
print(model)
data = model.createData()

# Sample a random configuration
q = pinocchio.randomConfiguration(model)
print(f"q: {q.T}")
pinocchio.forwardKinematics(model, data, q)
 
# data.oMi为SE3位姿，translation为位置部分
for name, oMi in zip(model.names, data.oMi):
    print("{:<24} : {: .2f} {: .2f} {: .2f}".format(name, *oMi.translation.T.flat))

print(*data.oMi)