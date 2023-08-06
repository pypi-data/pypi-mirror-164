## Xby2 AWS Cloud Practice Library
#### VPC:
Here are the fields you can customize in KWARGS and the (defaults):  
* availability_zones (2)  
* cidr_block:  
    * partial: 192.168.0.0/16  
    * full: 10.0.0.0/16 (default)  
    * else: 172.31.0.0/16
* private_subnets (1)  
* public_subnets (1)  
* nat_gateways:  
    * ONE_PER_AZ (default)  
    * SINGLE: one nat gateway total  
    * else/NONE: no nat gateways 
* private_cidr_mask (22)  
* public_cidr_mask (20)  
* resource_name (test-vpc)

#### Security Group:
Here are the fields you can customize in KWARGS and the (defaults):  
* protocol (tcp)  
* i_from_port (0)  
* i_to_port (65535)  
* e_from_port (0)  
* e_to_port (65535)  
* i_cidr (10.0.0.0/16)  
* e_cidr (10.0.0.0/16)  
* resource_name (test-sec-group)  

#### ELB:
Here are the fields you can customize in KWARGS and the (defaults):  
* resource_name (test-lb)

#### EC2:
Here are the fields you can customize in KWARGS and the (defaults):  
* resource_name (test-ec2)  
* instance_type (t3a.micro)

#### RDS:
Here are the fields you can customize in KWARGS and the (defaults):  
* rds_instance_class (db.t4g.micro)  
* allocated_storage (8)  
* engine (PostgreSQL)  
* password (password)  
* username (username)  
* resource_name (test-rds)

#### AMI:
Here are the fields you can customize in KWARGS and the (defaults):    
* most_recent (True)  
* owners (["amazon"])  
* filters ([{"name": "description", "values": ["Amazon Linux 2 *]}])

#### Adding Resources:
Keep the order of declaration in mind. For example, the VPC should likely be the first thing declared. When using the options above, the resource will use require a "module", which will refer to a file within the Xby2AWS folder, a "resource_name", which will be the name of one of our custom classes, "overrides", which will be a list of any parameters that we want changed from the default values, and two booleans: "req_vpc" and "req_ami". These will indicate whether a particular resource will need us to pass in a vpc or an ami, respectively. Additionally, we can create resources that we haven't customized. This will require a "module", which will probably begin with either "pulumi_aws." or "pulumi_awsx.", the "resource_name", which will be a class within said module, "overrides", which will consist of **all** of the parameters needed for this resource, and the aforementioned booleans. For example:  
```json
{
    "module": "Xby2AWS.elb",
    "resource_name": "Xby2ELB",
    "overrides": {},
    "req_vpc": true,
    "req_ami": false
},
{
    "module": "pulumi_aws.s3",
    "resource_name": "Bucket",
    "overrides": {
        "resource_name": "the-bucket"
    },
    "req_vpc": false,
    "req_ami": false
}
```

#### Resource Booleans
| Resource | req_vpc | req_ami |
| --- | ----------- | --------- |
| Xby2AMI | false | false |
| Xby2VPC | false | false |
| Xby2SecurityGroup | true | false |
| Xby2EC2 | true | true | 
| Xby2RDS | true | false | 
| Xby2ELB | true | false | 
| Bucket | false | false | 