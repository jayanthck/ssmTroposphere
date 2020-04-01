# Troposphere code to generate the ssm cloudformation template

## Cloudformation Deploy
```
python3 ssm.py
aws cloudformation deploy --template-file ./ssm.yaml  --stack-name ssmparameter --parameter-overrides Name=param1 Value=Value1 --no-fail-on-empty-changeset 
```
