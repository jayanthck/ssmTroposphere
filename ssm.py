from troposphere import Parameter, Output, Ref, Template
import troposphere.ssm as ssm
t = Template()
name_param = t.add_parameter(Parameter(
    "Name",
    Description="Name of the ssm parameter",
    Type="String", 
))
value_param =t.add_parameter(Parameter(
    "Value",
    Description="Value of the ssm parameter",
    Type="String", 
))
ssmParameter = ssm.Parameter(title='ssmparameter',Name=Ref(name_param),Value=Ref(value_param),Type='String',)
t.add_resource(ssmParameter)
f= open("ssm.yaml","w+")
f.write(t.to_yaml())
f.close()
print(t.to_yaml()) 