# Troposphere code to generate the ssm cloudformation template

## Cloudformation Deploy
```
aws cloudformation deploy --template-file ./ssm.yaml  --stack-name ssmparameter --parameter-overrides Name=param1 value=Value1 
```
