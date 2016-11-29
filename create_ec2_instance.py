import boto3

ec2 = boto3.resource('ec2')
new_instance = ec2.create_instances(ImageId='ami-16d4eb01', MinCount=1, MaxCount=2, InstanceType='t2.micro')

instances = ec2.instances.all()
for instance in instances:
	print(instance.id, instance.instance_type)
