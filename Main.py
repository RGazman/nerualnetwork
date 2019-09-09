from numpy import exp, array, random, dot

#A+B*C=X

training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 1]]).T
random.seed(1)
synaptic_weights = 2 * random.random((3, 1)) - 1
file_result = open('result.txt','w+')

#situation = array([int(input ()),int(input ()),int(input ())])
# 1,1,0 - 23563 itetation
situation = array([1,0,0])
print ("Start set: " + str(situation))


for iteration in range(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
   # result = 1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights))))
    result = 1 / (1 + exp(-(dot(situation, synaptic_weights))))
    file_result.write ("Output:"+'\n'+ str(output)+'\n'+ "Synaptic_weights:"+'\n'+ str(synaptic_weights)+'\n'+ "Result "+str(result)+'\n'+'\n')

#file_result.write ("result"+ str(result)+'\n')
print ("Result: " + str(result))
file_result.close()

input ("Press Enter to close")