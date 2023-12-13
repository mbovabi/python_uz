# Define the questions and answers
import random
questions = {
    1: {"question": "The terraform.tfstate file always matches your currently built infrastructure?",
        "options": {"A": "True", "B": "False"},
        "correct_answer": "B"},
    
    2: {"question": "One remote backend configuration always maps to a single remote workspace?",
        "options": {"A": "True", "B": "False"},
        "correct_answer": "B"},
    
    3: {"question": "How is the Terraform remote backend different than other state backends such as S3, Consul, etc.?",
        "options": {"A": "It can execute Terraform runs on dedicated infrastructure on premises or in Terraform Cloud",
                    "B": "It doesn't show the output of a terraform apply locally",
                    "C": "It is only available to paying customers",
                    "D": "All of the above"},
        "correct_answer": "A"},
4: {"question": "What is the workflow for deploying new infrastructure with Terraform?",
    "options": {"A":"Terraform plan to import the current infrastructure to the state file, make code" ,
                "B":"Write a Terraform configuration, run terraform show to view proposed changes, and terraform apply to create new infrastructure.",
                "C":"Terraform import to import the current infrastructure to the state file, make code changes, and terraform apply to update the infrastructure.",
                "D":"Write a Terraform configuration, run terraform init, run terraform plan to view planned infrastructure changes, and terraform apply to create new infrastructure "},
    "correct_answer": "D"},
    
5: {"question": "A provider configuration block is required in every Terraform configuration.",
    "options": {"A": "True", "B": "False"},
    "correct_answer": "A"},
6: {"question": "You run a local-exec provisioner in a null resource called null_resource.run_script and realize that you need to rerun the script.\nWhich of the following commands would you use first?",
    "options": {"A": "terraform taint null_resource.run_script",
                "B": "terraform apply -target=null_resource.run_script",
                "C": "terraform validate null_resource.run_script",
                "D": "terraform plan -target=null_resource.run_script"},
    "correct_answer": "A"},
7: {"question": "Which provisioner invokes a process on the resource created by Terraform?",
    "options": {"A": "remote-exec",
                "B": "null-exec",
                "C": "local-exec",
                "D": "file"},
    "correct_answer": "A"},
8: {"question": "Which of the following is not true of Terraform providers?",
    "options": {"A": "Providers can be written by individuals",
                "B": "Providers can be maintained by a community of users",
                "C": "Some providers are maintained by HashiCorp",
                "D": "Major cloud vendors and non-cloud vendors can write, maintain, or collaborate on Terraform providers",
                "E": "None of the above"},
    "correct_answer": "E"},
9: {"question": "What command does Terraform require the first time you run it within a configuration directory?",
    "options": {"A": "terraform import",
                "B": "terraform init",
                "C": "terraform plan",
                "D": "terraform workspace"},
    "correct_answer": "B"},
10: {"question": "You have deployed a new webapp with a public IP address on a cloud provider. However, you did not create any outputs for your code.\nWhat is the best method to quickly find the IP address of the resource you deployed?",
     "options": {"A": "Run terraform output ip_address to view the result",
                 "B": "In a new folder, use the terraform_remote_state data source to load in the state file, then write an output for each resource that you find the state file",
                 "C": "Run terraform state list to find the name of the resource, then terraform state show to find the attributes including public IP address",
                 "D": "Run terraform destroy then terraform apply and look for the IP address in stdout"},
     "correct_answer": "C"},
11: {"question": "Which of the following is not a key principle of infrastructure as code?",
     "options": {"A": "Versioned infrastructure",
                 "B": "Golden images",
                 "C": "Idempotence",
                 "D": "Self-describing infrastructure"},
     "correct_answer": "B"},
12: {"question": "Terraform variables and outputs that set the 'description' argument will store that description in the state file.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "B"},
13: {"question": "What is the provider for this fictitious resource?\nresource \"ans_vpc\" \"main\" {\n  name = \"test\"\n}",
     "options": {"A": "vpc",
                 "B": "main",
                 "C": "aws",
                 "D": "test"},
     "correct_answer": "C"},
14: {"question": "If you manually destroy infrastructure, what is the best practice reflecting this change in Terraform?",
     "options": {"A": "Run terraform refresh",
                 "B": "It will happen automatically",
                 "C": "Manually update the state file",
                 "D": "Run terraform import"},
     "correct_answer": "A"},
15: {"question": "What is not processed when running a terraform refresh?",
     "options": {"A": "State file",
                 "B": "Configuration file",
                 "C": "Credentials",
                 "D": "Cloud provider"},
     "correct_answer": "B"},
16: {"question": "What information does the public Terraform Module Registry automatically expose about published modules?",
     "options": {"A": "Required input variables",
                 "B": "Optional input variables and default values",
                 "C": "Outputs",
                 "D": "All of the above",
                 "E": "None of the above"},
     "correct_answer": "D"},
17: {"question": "If a module uses a local value, you can expose that value with a Terraform output.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "A"},
18: {"question": "You should store secret data in the same version control repository as your Terraform configuration.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "B"},
19: {"question": "Which of the following is not a valid string function in Terraform?",
     "options": {"A": "split",
                 "B": "join",
                 "C": "slice",
                 "D": "chomp"},
     "correct_answer": "C"},
20: {"question": "You have provisioned some virtual machines (VMs) on Google Cloud Platform (GCP) using the gcloud command line tool. However, you are standardizing with Terraform and want to manage these VMs using Terraform instead. What are the two things you must do to achieve this? (Choose two.)",
     "options": {"A": "Provision new VMs using Terraform with the same VM names",
                 "B": "Use the terraform import command for the existing VMs",
                 "C": "Write Terraform configuration for the existing VMs",
                 "D": "Run the terraform import-gcp command"},
           "correct_answers": "BC" },
21: {"question": "CertyIQ\nYou have recently started a new job at a retailer as an engineer. As part of this new role, you have been tasked with evaluating multiple outages that occurred during peak shopping time during the holiday season. Your investigation found that the team is manually deploying new compute instances and configuring each compute instance manually. This has led to inconsistent configuration between each compute instance. How would you solve this using infrastructure as code?",
     "options": {"A": "Implement a ticketing workflow that makes engineers submit a ticket before manually provisioning and configuring a resource",
                 "B": "Implement a checklist that engineers can follow when configuring compute instances",
                 "C": "Replace the compute instance type with a larger version to reduce the number of required deployments",
                 "D": "Implement a provisioning pipeline that deploys infrastructure configurations committed to your version control system following code reviews"},
     "correct_answer": "D"},
22: {"question": "terraform init initializes a sample main.tf file in the current directory.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "B"},
23: {"question": "Which two steps are required to provision new infrastructure in the Terraform workflow? (Choose two.)",
     "options": {"A": "Destroy",
                 "B": "Apply",
                 "C": "Import",
                 "D": "Init",
                 "E": "Validate"},
     "correct_answers": ["B", "D"]},
24: {"question": "Why would you use the terraform taint command?",
     "options": {"A": "When you want to force Terraform to destroy a resource on the next apply",
                 "B": "When you want to force Terraform to destroy and recreate a resource on the next apply",
                 "C": "When you want Terraform to ignore a resource on the next apply",
                 "D": "When you want Terraform to destroy all the infrastructure in your workspace"},
     "correct_answer": "B"},
25: {"question": "Terraform requires the Go runtime as a prerequisite for installation.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "B"},
26: {"question": "When should you use the force-unlock command?",
     "options": {"A": "You see a status message that you cannot acquire the lock",
                 "B": "You have a high-priority change",
                 "C": "Automatic unlocking failed",
                 "D": "Your apply failed due to a state lock"},
     "correct_answer": "C"},
27: {"question": 'Terraform can import modules from a number of sources - which of the following is not a valid source?',
     "options": {"A": "FTP server",
                 "B": "GitHub repository",
                 "C": "Local path",
                 "D": "Terraform Module Registry"},
     "correct_answer": "A"},
28: {"question": 'Which of the following is available only in Terraform Enterprise or Cloud workspaces and not in Terraform CLI?',
     "options": {"A": "Secure variable storage",
                 "B": "Support for multiple cloud providers",
                 "C": "Dry runs with terraform plan",
                 "D": "Using the workspace as a data source"},
     "correct_answer": "A"},
29: {"question": "terraform validate validates the syntax of Terraform files.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "A"},
30: {"question": 'You have used Terraform to create an ephemeral development environment in the cloud and are now ready to destroy all the infrastructure described by your Terraform configuration. To be safe, you would like to first see all the infrastructure that will be deleted by Terraform. Which command should you use to show all of the resources that will be deleted? (Choose two.)',
     "options": {"A": "Run terraform plan -destroy",
                 "B": "This is not possible. You can only show resources that will be created.",
                 "C": "Run terraform state rm *",
                 "D": "Run terraform destroy and it will first output all the resources that will be deleted before prompting for approval."},
     "correct_answers": ["A", "D"]},
31: {"question": 'Which of the following is the correct way to pass the value in the variable num_servers into a module with the input servers?',
     "options": {"A": "servers = num_servers",
                 "B": "servers = variable.num_servers",
                 "C": "servers = var(num_servers)",
                 "D": "servers = var.num_servers"},
     "correct_answer": "D"},
32: {"question": "A Terraform provisioner must be nested inside a resource configuration block.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "A"},
33: {"question": "CertyIQ Terraform can run on Windows or Linux, but it requires a Server version of the Windows operating system.",
     "options": {"A": "True",
                 "B": "False"},
     "correct_answer": "B"},
34: {"question": "What does the default 'local' Terraform backend store?",
     "options": {"A": "tfplan files",
                 "B": "Terraform binary",
                 "C": "Provider plugins",
                 "D": "State file"},
     "correct_answer": "D"},
35: {"question": 'You have multiple team members collaborating on infrastructure as code (IaC) using Terraform, and want to apply formatting standards for readability. How can you format Terraform HCL (HashiCorp Configuration Language) code according to standard Terraform style convention?',
     "options": {"A": "Run the terraform fmt command during the code linting phase of your CI/CD process",
                 "B": "Designate one person in each team to review and format everyone's code",
                 "C": "Manually apply two spaces indentation and align equal sign '=' characters in every Terraform file (*.tf)",
                 "D": "Write a shell script to transform Terraform files using tools such as AWK, Python, and sed"},
     "correct_answer": "A"},
36: {"question": 'What value does the Terraform Cloud/Terraform Enterprise private module registry provide over the public Terraform Module Registry?',
     "options": {"A": "The ability to share modules with public Terraform users and members of Terraform Enterprise Organizations",
                 "B": "The ability to tag modules by version or release",
                 "C": "The ability to restrict modules to members of Terraform Cloud or Enterprise organizations",
                 "D": "The ability to share modules publicly with any user of Terraform"},
     "correct_answer": "C"},
37: {"question": "Which task does terraform init not perform?",
     "options": {"A": "Sources all providers present in the configuration and ensures they are downloaded and available locally",
                 "B": "Connects to the backend",
                 "C": "Sources any modules and copies the configuration locally",
                 "D": "Validates all required variables are present"},
     "correct_answer": "D"},
38: {"question": "You have declared a variable called var.list which is a list of objects that all have an attribute id. Which options will produce a list of the IDs? (Choose two.)",
     "options": {"A": "for o in var.list : o => o.id",
                 "B": "var.list[*].id",
                 "C": "[ var.list[*].id ]",
                 "D": "[ for o in var.list : o.id ]"},
     "correct_answer": ["B", "D"]},
39: {"question": "Which argument(s) is (are) required when declaring a Terraform variable?",
     "options": {"A": "type",
                 "B": "default",
                 "C": "description",
                 "D": "All of the above",
                 "E": "None of the above"},
     "correct_answer": "E"},
40: {"question": "When using a module block to reference a module stored on the public Terraform Module Registry such as:\nmodule \"consul\" {\n     source = \"HashiCorp/cansul/aws\"\n}\n\nHow do you specify version 1.0.0?",
     "options": {"A": "Modules stored on the public Terraform Module Registry do not support versioning",
                 "B": "Append ?ref=v1.0.0 argument to the source path",
                 "C": "Add version = \"1.0.0\" attribute to module block",
                 "D": "Nothing - modules stored on the public Terraform Module Registry always default to version 1.0.0"},
     "correct_answer": "C"},
41: {"question": "What features does the hosted service Terraform Cloud provide? (Choose two.)",
     "options": {"A": "Automated infrastructure deployment visualization",
                 "B": "Automatic backups",
                 "C": "Remote state storage",
                 "D": "A web-based user interface (UI)"},
     "correct_answer": ["C", "D"]},
42: {"question": "Where does the Terraform local backend store its state?",
     "options": {"A": "In the /tmp directory",
                 "B": "In the terraform file",
                 "C": "In the terraform.tfstate file",
                 "D": "In the user's terraform.state file"},
     "correct_answer": "C"},
43: {"question": "Which option can not be used to keep secrets out of Terraform configuration files?",
     "options": {"A": "A Terraform provider",
                 "B": "Environment variables",
                 "C": "A -var flag",
                 "D": "secure string"},
     "correct_answer": "D"},
44: {"question": "What is one disadvantage of using dynamic blocks in Terraform?",
     "options": {"A": "They cannot be used to loop through a list of values",
                 "B": "Dynamic blocks can construct repeatable nested blocks",
                 "C": "They make configuration harder to read and understand",
                 "D": "Terraform will run more slowly"},
     "correct_answer": "C"},
45: {"question": "Only the user that generated a plan may apply it. A. True B. False",
     "options": {"A": "True", "B": "False"},
     "correct_answer": "B"},
46: {"question": "Examine the following Terraform configuration, which uses the data source for an AWS AMI. What value should you enter for the ami argument in the AWS instance resource?",
     "options": {"A": "aws_ami.ubuntu",
                 "B": "data.aws_ami.ubuntu",
                 "C": "data.aws_ami.ubuntu.id",
                 "D": "aws_ami.ubuntu.id"},
     "correct_answer": "C"},
47: {"question": "FILL BLANK - You need to specify a dependency manually. What resource meta-parameter can you use to make sure Terraform respects the dependency?Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.",
     "options": {"A":"depends_on"},
     "correct_answer": "depends_on"},
48: {
    "question": "You have never used Terraform before and would like to test it out using a shared team account for a cloud provider. The shared team account already contains 15 virtual machines (VM). You develop a Terraform configuration containing one VM, perform terraform apply, and see that your VM was created successfully. What should you do to delete the newly-created VM with Terraform?",
    "options": {
        "A": "The Terraform state file contains all 16 VMs in the team account. Execute terraform destroy and select the newly-created VM.",
        "B": "The Terraform state file only contains the one new VM. Execute terraform destroy.",
        "C": "Delete the Terraform state file and execute Terraform apply.",
        "D": "Delete the VM using the cloud provider console and terraform apply to apply the changes to the Terraform state file."
    },
    "correct_answer": "B"
},
49: {
    "question": "What is the name assigned by Terraform to reference this resource?",
    "options": {
        "A": "dev",
        "B": "azurerm_resource_group",
        "C": "azurerm",
        "D": "test"
    },
    "correct_answer": "A"
},
50: {
    "question": "Setting the TF_LOG environment variable to DEBUG causes debug messages to be logged into syslog.",
    "options": {"A": "True", 
                "B": "False"},
    "correct_answer": "B"
},

51: {
    "question": "Where in your Terraform configuration do you specify a state backend?",
    "options": {"A": "The terraform block", 
                "B": "The resource block", 
                "C": "The provider block",
                "D": "The datasource block"},
    "correct_answer": "C"
},

52: {
    "question": "In Terraform 0.13 and above, outside of the required_providers block, Terraform configurations always refer to providers by their local names. A. True B. False",
    "options": {"A": "True",
                "B": "False"},
    "correct_answer": "A"
},

53: {
    "question": "What command should you run to display all workspaces for the current configuration?",
    "options": {"A": "terraform workspace", 
                "B": "terraform workspace show", 
                "C": "terraform workspace list", 
                "D": "terraform show workspace"},
    "correct_answer": "C"
},

54: {
    "question": "Terraform providers are always installed from the Internet. A. True B. False",
    "options": {"A": "True", 
                "B": "False"},
    "correct_answer": "A"
},

55: {
    "question": "Which of these is the best practice to protect sensitive values in state files?",
    "options": {"A": "Blockchain",
                "B": "Secure Sockets Layer (SSL)",
                "C": "Enhanced remote backends", 
                "D": "Signed Terraform providers"},
    "correct_answer": "C"
},

56: {
    "question": "When does terraform apply reflect changes in the cloud environment?",
    "options": {"A": "Immediately", 
                "B": "However long it takes the resource provider to fulfill the request", 
                "C": "After updating the state file", 
                "D": "Based on the value provided to the -refresh command line argument", 
                "E": "None of the above"},
    "correct_answer": "A"
},

57: {
    "question": "How would you reference the 'name' value of the second instance of this fictitious resource?",
    "options": {"A": "element(aws_instance.web, ", 
                "B": "aws_instance.web[1].name",
                "C": "aws_instance.web[1]",
                "D": "aws_instance.web[2].name", 
                "E": "aws_instance.web.*.name"},
    "correct_answer": "B"
},

58: {
    "question": "A Terraform provider is not responsible for:",
    "options": {"A": "Understanding API interactions with some service", 
                "B": "Provisioning infrastructure in multiple clouds", 
                "C": "Exposing resources and data sources based on an API", 
                "D": "Managing actions to take based on resource differences"},
    "correct_answer": "D"
},

59: {
    "question": "Terraform provisioners can be added to any resource block. A. True B. False",
    "options": {"A": "True", 
                "B": "False"},
    "correct_answer": "A"
},

60: {
    "question": "What is terraform refresh intended to detect?",
    "options": {"A": "Terraform configuration code changes", 
                "B": "Empty state files", 
                "C": "State file drift", 
                "D": "Corrupt state files"},
    "correct_answer": "C"
},

61: {
    "question": "FILL BLANK - Which flag would you add to terraform plan to save the execution plan to a file?",
    "options": {"A": "-out=FILENAME"},
    "correct_answer": "A"

},

62: {
    "question": "FILL BLANK - What is the name of the default file where Terraform stores the state?",
    "options": {"A": "Terraform.tfstate"},
    "correct_answer": "A"
},

63: {
    "question": "A Terraform local value can reference other Terraform local values. A. True B. False",
    "options": {"A": "True", 
                "B": "False"},
    "correct_answer": "A"
},

64: {
    "question": "Which of the following is not a valid Terraform collection type?",
    "options": {"A": "list", 
                "B": "map",   
                "C": "tree", 
                "D": "set"},
    "correct_answer": "C"
},
65: {
    "question": "When running the command terraform taint against a managed resource you want to force recreation upon, Terraform will immediately destroy and recreate the resource. A. True B. False",
    "options": {"A": "True", 
                "B": "False"},
    "correct_answer": "B"
},

66: {
    "question": "All standard backend types support state storage, locking, and remote operations like plan, apply and destroy. A. True B. False",
    "options": {"A": "True", "B": "False"},
    "correct_answer": "B"
},

67: {
    "question": "How can terraform plan aid in the development process?",
    "options": {"A": "Validates your expectations against the execution plan without permanently modifying state", "B": "Initializes your working directory containing your Terraform configuration files", "C": "Formats your Terraform configuration files", "D": "Reconciles Terraform's state against deployed resources and permanently modifies state using the current status of deployed resources"},
    "correct_answer": "A"
},

68: {
    "question": "You would like to reuse the same Terraform configuration for your development and production environments with a different state file for each. Which command would you use?",
    "options": {"A": "terraform import", "B": "terraform workspace", "C": "terraform state", "D": "terraform init"},
    "correct_answer": "B"
},

69: {
    "question": "What is the name assigned by Terraform to reference this resource?",
    "options": {"A": "compute_instance", "B": "main", "C": "google", "D": "teat"},
    "correct_answer": "B"
},
70: {
    "question": "You're building a CI/CD (continuous integration/ continuous delivery) pipeline and need to inject sensitive variables into your Terraform run. How can you do this safely?",
    "options": {"A": "Pass variables to Terraform with a 'var' flag", "B": "Copy the sensitive variables into your Terraform code", "C": "Store the sensitive variables in a secure_vars.tf file", "D": "Store the sensitive variables as plain text in a source code repository"},
    "correct_answer": "A"
},

71: {
    "question": "Your security team scanned some Terraform workspaces and found secrets stored in plaintext in state files. How can you protect sensitive data stored in Terraform state files?",
    "options": {"A": "Delete the state file every time you run Terraform", "B": "Store the state in an encrypted backend", "C": "Edit your state file to scrub out the sensitive data", "D": "Always store your secrets in a secrets.tfvars file"},
    "correct_answer": "B"
},

72: {
    "question": "In contrast to Terraform Open Source, when working with Terraform Enterprise and Cloud Workspaces, conceptually you could think about them as completely separate working directories. A. True B. False",
    "options": {"A": "True", "B": "False"},
    "correct_answer": "A"
},

73: {
    "question": "You want to know from which paths Terraform is loading providers referenced in your Terraform configuration (*.tf files). You need to enable debug messages to find this out. Which of the following would achieve this?",
    "options": {"A": "Set the environment variable TF_LOG=TRACE", "B": "Set verbose logging for each provider in your Terraform configuration", "C": "Set the environment variable TF_VAR_log=TRACE", "D": "Set the environment variable TF_LOG_PATH"},
    "correct_answer": "A"
},
74: {
    "question": "How is terraform import run?",
    "options": {"A": "As a part of terraform init", "B": "As a part of terraform plan", "C": "As a part of terraform refresh", "D": "By an explicit call"},
    "correct_answer": "D"
},

75: {
    "question": "You have a simple Terraform configuration containing one virtual machine (VM) in a cloud provider. You run terraform apply and the VM is created successfully. What will happen if you delete the VM using the cloud provider console, and run terraform apply again without changing any Terraform code?",
    "options": {"A": "Terraform will remove the VM from the state file", "B": "Terraform will report an error", "C": "Terraform will not make any changes", "D": "Terraform will recreate the VM"},
    "correct_answer": "D"
},

76: {
    "question": "Which of these options is the most secure place to store secrets for connecting to a Terraform remote backend?",
    "options": {"A": "Defined in Environment variables", "B": "Inside the backend block within the Terraform configuration", "C": "Defined in a connection configuration outside of Terraform", "D": "None of the above"},
    "correct_answer": "A"
},
77: {
    "question": "Your DevOps team is currently using the local backend for your Terraform configuration. You would like to move to a remote backend to begin storing the state file in a central location. Which of the following backends would not work?",
    "options": {"A": "Amazon S3", "B": "Artifactory", "C": "Git", "D": "Terraform Cloud"},
    "correct_answer": "C"
},

78: {
    "question": "Which backend does the Terraform CLI use by default?",
    "options": {"A": "Terraform Cloud", "B": "Consul", "C": "Remote", "D": "Local"},
    "correct_answer": "D"
},

79: {
    "question": "When you initialize Terraform, where does it cache modules from the public Terraform Module Registry?",
    "options": {"A": "On disk in the /tmp directory", "B": "In memory", "C": "On disk in the .terraform sub-directory", "D": "They are not cached"},
    "correct_answer": "C"
},

80: {
    "question": "You write a new Terraform configuration and immediately run terraform apply in the CLI using the local backend. Why will the apply fail?",
    "options": {"A": "Terraform needs you to format your code according to best practices first", "B": "Terraform needs to install the necessary plugins first", "C": "The Terraform CLI needs you to log into Terraform cloud first", "D": "Terraform requires you to manually run terraform plan first"},
    "correct_answer": "B"
},

81: {
    "question": "What features stops multiple admins from changing the Terraform state at the same time?",
    "options": {"A": "Version control", "B": "Backend types", "C": "Provider constraints", "D": "State locking"},
    "correct_answer": "D"
},

82: {
    "question": "A fellow developer on your team is asking for some help in refactoring their Terraform code. As part of their application's architecture, they are going to tear down an existing deployment managed by Terraform and deploy new. However, there is a server resource named aws_instance.ubuntu[1] they would like to keep to perform some additional analysis. What command should be used to tell Terraform to no longer manage the resource?",
    "options": {"A": "terraform apply rm aws_instance.ubuntu[1]", "B": "terraform state rm aws_instance.ubuntu[1]", "C": "terraform plan rm aws_instance.ubuntu[1]", "D": "terraform delete aws_instance.ubuntu[1]"},
    "correct_answer": "B"
},

83: {
    "question": "Terraform can only manage resource dependencies if you set them explicitly with the depends_on argument.",
    "options": {"A":"True" , 
                "B" :"False"},
    "correct_answer": "B"
},

86: {
    "question": "You just scaled your VM infrastructure and realized you set the count variable to the wrong value. You correct the value and save your change. What do you do next to make your infrastructure match your configuration?",
    "options": {"A": "Run an apply and confirm the planned changes", "B": "Inspect your Terraform state because you want to change it", "C": "Reinitialize because your configuration has changed", "D": "Inspect all Terraform outputs to make sure they are correct"},
    "correct_answer": "A"
},

87: {
    "question": "Terraform provisioners that require authentication can use the ______ block.",
    "options": {"A": "connection", "B": "credentials", "C": "secrets", "D": "ssh"},
    "correct_answer": "A"
},

88: {
    "question": "Terraform validate reports syntax check errors from which of the following scenarios?",
    "options": {"A": "Code contains tabs indentation instead of spaces", "B": "There is missing value for a variable", "C": "The state files does not match the current infrastructure", "D": "None of the above"},
    "correct_answer": "B"
}
,
89: {
    "question": "Which of the following is allowed as a Terraform variable name?",
    "options": {"A": "count", "B": "name", "C": "source", "D": "version"},
    "correct_answer": "B"
}
,
90: {
    "question": "What type of block is used to construct a collection of nested configuration blocks?",
    "options": {"A": "for_each", "B": "repeated", "C": "nesting", "D": "dynamic"},
    "correct_answer": "D"
},

91: {
    "question": "Module variable assignments are inherited from the parent module and do not need to be explicitly set. True or False?",
    "options" : {"A": "True",
                 "B": "False"},
    "correct_answer": "B"

},

93: {
    "question": "Which of the following is not an action performed by terraform init?",
    "options": {"A": "Create a sample main.tf file", "B": "Initialize a configured backend", "C": "Retrieve the source code for all referenced modules", "D": "Load required provider plugins"},
    "correct_answer": "A"
},

94: {
    "question": "HashiCorp Configuration Language (HCL) supports user-defined functions. True or False?",
    "options": {"B"},
    "correct_answer": "B"

},

95: {
    "question": "How can you trigger a run in a Terraform Cloud workspace that is connected to a Version Control System (VCS) repository?",
    "options": {"A": "Only Terraform Cloud organization owners can set workspace variables on VCS connected workspaces", "B": "Commit a change to the VCS working directory and branch that the Terraform Cloud workspace is connected to", "C": "Only members of a VCS organization can open a pull request against repositories that are connected to Terraform Cloud workspaces", "D": "Only Terraform Cloud organization owners can approve plans in VCS connected workspaces"},
    "correct_answer": "B"
},

96: {
    "question": "Terraform and Terraform providers must use the same major version number in a single configuration.?",
    "options": {"A": "True"
                "B" "False" },
    "correct_answer": "B"
},

97: {
    "question": "Which statement describes a goal of infrastructure as code?",
    "options": {"A": "An abstraction from vendor-specific APIs", "B": "Write once, run anywhere", "C": "A pipeline process to test and deliver software", "D": "The programmatic configuration of resources"},
    "correct_answer": "D"
},

98: {
    "question": "When using Terraform to deploy resources into Azure, which scenarios are true regarding state files? (Choose two.)",
    "options": {"A": "When a change is made to the resources via the Azure Cloud Console, the changes are recorded in a new state file", "B": "When a change is made to the resources via the Azure Cloud Console, Terraform will update the state file to reflect them during the next plan or apply", "C": "When a change is made to the resources via the Azure Cloud Console, the current state file will not be updated", "D": "When a change is made to the resources via the Azure Cloud Console, the changes are recorded in the current state file"},
    "correct_answer": ["B", "C"]
},

99: {
    "question": "You need to deploy resources into two different cloud regions in the same Terraform configuration. To do that, you declare multiple provider configurations as follows: What meta-argument do you need to configure in a resource block to deploy the resource to the `us-west-2` AWS region?",
    "options": {"A": "alias = west", "B": "provider = west", "C": "provider = aws.west", "D": "alias = aws.west"},
    "correct_answer": "C"
},

100: {
    "question": "You have declared an input variable called environment in your parent module. What must you do to pass the value to a child module in the configuration?",
    "options": {"A": "Add node_count = var.node_count", "B": "Declare the variable in a terraform.tfvars file", "C": "Declare a node_count input variable for child module", "D": "Nothing, child modules inherit variables of the parent module"},
    "correct_answer": "A"
},
  101: {
    "question": "If a module declares a variable with a default, that variable must also be defined within the module.",
    "options": {
      "A": "True",
      "B": "False"
    },
    "correct_answer": "B"
  }
,
102: {
    "question": "Which option cannot be used to keep secrets out of Terraform configuration files?",
    "options" : {
      "A": "Environment Variables",
      "B": "Mark the variable as sensitive",
      "C": "A Terraform provider",
      "D": "A -var flag"
    },
    "correct_answer": "C"

    },

    103: {
        "question": "Which of the following arguments are required when declaring a Terraform output?" ,
        "options": {"A": "sensitive", 
                    "B":"description" ,
                    "C": "default", 
                    "D": "value"
        } ,
        "correct_answer": "D"
    },

    104: {
        "question": "Your risk management organization requires that new AWS S3 buckets must be private and encrypted at rest. How can Terraform Enterprise automatically and proactively enforce this security control?",
        "options": {"A" : "With a Sentinel policy, which runs before every apply" ,
                   "B": "By adding variables to each TFE workspace to ensure these settings are always enabled ",
                   "C": "With an S3 module with proper settings for buckets",  
                   "D": "Auditing cloud storage buckets with a vulnerability scanning tool",} ,
        "correct_answer": "A"
    },

    105: {
        "question": "Most Terraform providers interact with ____________.",
        "options": {"A": "API" ,
                   "B" : "VCS Systems ", 
                   "C": "Shell scripts ", 
                   "D": "None of the above" },
        "correct_answer": "A"
    },

    106: {
        "question": "terraform validate validates that your infrastructure matches the Terraform state file.",
        "options": {"A":"True" ,
                    "B":"False"},
        "correct_answer": "B"
    },

    107: {
        "question": "What does terraform import allow you to do?",
        "options": {
            "A": "Import a new Terraform module",
            "B": "Use a state file to import infrastructure to the cloud",
            "C": "Import provisioned infrastructure to your state file",
            "D": "Import an existing state file to a new Terraform workspace"
        },
        "correct_answer": "C"
    },
    108: {
        "question": "FILL BLANK - In the below configuration, how would you reference the module output vpc_id?",
        "options": {"A": "module.vpc.vpc_id"},
        "correct_answer": "A"
    },
    109: {
        "question": "How would you reference the Volume IDs associated with the ebs_block_device blocks in this configuration?",
        "options": {
            "A": "aws_instance.example.ebs_block_device.[*].volume_id",
            "B": "aws_instance.example.ebs_block_device.volume_id",
            "C": "aws_instance.example.ebs_block_device[sda2,sda3].volume_id",
            "D": "aws_instance.example.ebs_block_device.*.volume_id"
        },
        "correct_answer": "D"
    },
    110: {
    "question": "What does state locking accomplish?",
    "options": {
        "A": "Copies the state file from memory to disk",
        "B": "Encrypts any credentials stored within the state file",
        "C": "Blocks Terraform commands from modifying the state file",
        "D": "Prevents accidental deletion of the state file"
    },
    "correct_answer": "C"
},
# Вопрос 111
111: {
    "question": "You just upgraded the version of a provider in an existing Terraform project. What do you need to do to install the new provider?",
    "options": {
        "A": "Run terraform apply -upgrade",
        "B": "Run terraform init -upgrade",
        "C": "Run terraform refresh",
        "D": "Upgrade your version of Terraform"
    },
    "correct_answer": "B"
},
# Вопрос 112
112: {
    "question": "A module can always refer to all variables declared in its parent module.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 113
113: {
    "question": "When you use a remote backend that needs authentication, HashiCorp recommends that you:",
    "options": {
        "A": "Use partial configuration to load the authentication credentials outside of the Terraform code",
        "B": "Push your Terraform configuration to an encrypted git repository",
        "C": "Write the authentication credentials in the Terraform configuration files",
        "D": "Keep the Terraform configuration files in a secret store"
    },
    "correct_answer": "A"
},
# Вопрос 114
114: {
    "question": "You have a simple Terraform configuration containing one virtual machine (VM) in a cloud provider. You run terraform apply and the VM is created successfully. What will happen if you terraform apply again immediately afterwards without changing any Terraform code?",
    "options": {
        "A": "Terraform will terminate and recreate the VM",
        "B": "Terraform will create another duplicate VM",
        "C": "Terraform will apply the VM to the state file",
        "D": "Nothing"
    },
    "correct_answer": "C"
},
# Вопрос 115
115: {
    "question": "A junior admin accidentally deleted some of your cloud instances. What does Terraform do when you run terraform apply?",
    "options": {
        "A": "Build a completely brand new set of infrastructure",
        "B": "Tear down the entire workspace infrastructure and rebuild it",
        "C": "Rebuild only the instances that were deleted",
        "D": "Stop and generate an error message about the missing instances"
    },
    "correct_answer": "C"
},
# Вопрос 116
116: {
    "question": "You have created a main.tr Terraform configuration consisting of an application server, a database, and a load balancer. You ran terraform apply and all resources were created successfully. Now you realize that you do not actually need the load balancer so you run terraform destroy without any flags. What will happen?",
    "options": {
        "A": "Terraform will destroy the application server because it is listed first in the code",
        "B": "Terraform will prompt you to confirm that you want to destroy all the infrastructure",
        "C": "Terraform will destroy the main.tf file",
        "D": "Terraform will prompt you to pick which resource you want to destroy",
        "E": "Terraform will immediately destroy all the infrastructure"
    },
    "correct_answer": "B"
},
# Вопрос 117
117: {
    "question": "Which type of block fetches or computes information for use elsewhere in a Terraform configuration?",
    "options": {
        "A": "provider",
        "B": "resource",
        "C": "local",
        "D": "data"
    },
    "correct_answer": "D"
},
# Вопрос 118
118: {
    "question": "You have just developed a new Terraform configuration for two virtual machines with a cloud provider. You would like to create the infrastructure for the first time. Which Terraform command should you run first?",
    "options": {
        "A": "terraform apply",
        "B": "terraform plan",
        "C": "terraform show",
        "D": "terraform init"
    },
    "correct_answer": "D"
},
# Вопрос 119
119: {
    "question": "All modules published on the official Terraform Module Registry have been verified by HashiCorp.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 120
120: {
    "question": "You have to initialize a Terraform backend before it can be configured.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 121
121: {
    "question": "Which of the following does terraform apply change after you approve the execution plan? (Choose two.)",
    "options": {
        "A": "Cloud infrastructure",
        "B": "The .terraform directory",
        "C": "The execution plan",
        "D": "State file",
        "E": "Terraform code"
    },
    "correct_answer": ["A", "D"]
},
# Вопрос 122
122: {
    "question": "A Terraform backend determines how Terraform loads state and stores updates when you execute ___________.",
    "options": {
        "A": "apply",
        "B": "taint",
        "C": "destroy",
        "D": "All of the above",
        "E": "None of the above"
    },
    "correct_answer": "D"
},

123: {
    "question": "What does Terraform use .terraform.lock.hcl file for?",
    "options": {
        "A": "Tracking provider dependencies",
        "B": "There is no such file",
        "C": "Preventing Terraform runs from occurring",
        "D": "Storing references to workspaces which are locked"
    },
    "correct_answer": "A"
},
# Вопрос 124
124: {
    "question": "You've used Terraform to deploy a virtual machine and a database. You want to replace this virtual machine instance with an identical one without affecting the database. What is the best way to achieve this using Terraform?",
    "options": {
        "A": "Use the terraform state rm command to remove the VM from state file",
        "B": "Use the terraform taint command targeting the VMs then run terraform plan and terraform apply",
        "C": "Use the terraform apply command targeting the VM resources only",
        "D": "Delete the Terraform VM resources from your Terraform code then run terraform plan and terraform apply"
    },
    "correct_answer": "B"
},
# Вопрос 125
125: {
    "question": "How do you specify a module's version when publishing it to the public Terraform Module Registry?",
    "options": {
        "A": "The module's configuration page on the Terraform Module Registry",
        "B": "Terraform Module Registry does not support versioning modules",
        "C": "The release tags in the associated repo",
        "D": "The module's Terraform code"
    },
    "correct_answer": "C"
},
    
# Вопрос 126
126: {
    "question": "Terraform plan updates your state file.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 127
127: {
    "question": "To check if all code in a Terraform configuration with multiple modules is properly formatted without making changes, what command should be run?",
    "options": {
        "A": "terraform fmt -check",
        "B": "terraform fmt -write-false",
        "C": "terraform fmt -list -recursive",
        "D": "terraform fmt -check -recursive"
    },
    "correct_answer": "D"
},
# Вопрос 128
128: {
    "question": "As a member of the operations team, you need to run a script on a virtual machine created by Terraform. Which provisioner is best to use in your Terraform code?",
    "options": {
        "A": "null-resource",
        "B": "local-exec",
        "C": "remote-exec",
        "D": "file"
    },
    "correct_answer": "C"
},

# Вопрос 129
129: {
    "question": "Terraform variable names are saved in the state file.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 130
130: {
    "question": "You are writing a child Terraform module which provisions an AWS instance. You want to make use of the IP address returned in the root configuration. You name the instance resource 'main'. Which of these is the correct way to define the output value using HCL2?",
    "options": {
        "A": "output \"ip_address\" { value = aws_instance.main.private_ip }",
        "B": "output { value = aws_instance.main.private_ip }",
        "C": "output \"ip_address\" { value = module.main.aws_instance.private_ip }",
        "D": "output { value = module.main.aws_instance.private_ip }"
    },
    "correct_answer": "A"
},
# Вопрос 131
131: {
    "question": "How can a ticket-based system slow down infrastructure provisioning and limit the ability to scale? (Choose two.)",
    "options": {
        "A": "A full audit trail of the request and fulfillment process is generated",
        "B": "A request must be submitted for infrastructure changes",
        "C": "As additional resources are required, more tickets are submitted",
        "D": "A catalog of approved resources can be accessed from drop-down lists in a request form"
    },
    "correct_answer": "C"
},
# Вопрос 132
132: {
    "question": "Which of the following statements about Terraform modules is not true?",
    "options": {
        "A": "Modules must be publicly accessible",
        "B": "Modules can be called multiple times",
        "C": "Module is a container for one or more resources",
        "D": "Modules can call other modules"
    },
    "correct_answer": "A"
},
# Вопрос 133
133: {
    "question": "Which Terraform collection type should you use to store key/value pairs?",
    "options": {
        "A": "tuple",
        "B": "set",
        "C": "map",
        "D": "list"
    },
    "correct_answer": "C"
},
# Вопрос 134
134: {
    "question": "You have used Terraform to create an ephemeral development environment in the cloud and are now ready to destroy all the infrastructure described by your Terraform configuration. To be safe, you would like to first see all the infrastructure that will be deleted by Terraform. Which command should you use to show all of the resources that will be deleted? (Choose two.)",
    "options": {
        "A": "Run terraform plan -destroy",
        "B": "Run terraform show -destroy",
        "C": "Run terraform destroy and it will first output all the resources that will be deleted before prompting for approval",
        "D": "Run terraform show -destroy"
    },
    "correct_answer": "AC"
},
# Вопрос 135
135: {
    "question": "When do you need to explicitly execute terraform refresh?",
    "options": {
        "A": "Before every terraform plan",
        "B": "Before every terraform apply",
        "C": "Before every terraform import",
        "D": "None of the above"
    },
    "correct_answer": "D"
},
# Вопрос 136
136: {
    "question": "All Terraform Cloud tiers support team management and governance.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 137
137: {
    "question": "What advantage does an operations team that uses infrastructure as code have?",
    "options": {
        "A": "The ability to delete infrastructure",
        "B": "The ability to update existing infrastructure",
        "C": "The ability to reuse best practice configurations and settings",
        "D": "The ability to autoscale a group of servers"
    },
    "correct_answer": "C"
},
# Вопрос 138
138: {
    "question": "You have modified your Terraform configuration to fix a typo in the Terraform ID of a resource from aws_security_group.http to aws_security_group.http. Which of the following commands would you run to update the ID in state without destroying the resource?",
    "options": {
        "A": "terraform mv aws_security_group.htp aws_security_group.http",
        "B": "terraform apply",
        "C": "terraform refresh"
    },
    "correct_answer": "A"
},
# Вопрос 139
139: {
    "question": "Terraform Cloud is available only as a paid offering from HashiCorp.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 140
140: {
    "question": "Your additional question here",
    "options": {
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D"
    },
    "correct_answer": "A"
},
# Вопрос 141
141: {
    "question": "Terraform Cloud is available only as a paid offering from HashiCorp.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 142
142: {
    "question": "Which of the following is not a way to trigger terraform destroy?",
    "options": {
        "A": "Using the destroy command with auto-approve",
        "B": "Running terraform destroy from the correct directory and then typing 'yes' when prompted in the CLI",
        "C": "Passing --destroy at the end of a plan request",
        "D": "Delete the state file and run terraform apply"
    },
    "correct_answer": "D"
},
# Вопрос 143
143: {
    "question": "Which of the following is not an advantage of using infrastructure as code operations?",
    "options": {
        "A": "Self-service infrastructure deployment",
        "B": "Troubleshoot via a Linux diff command",
        "C": "Public cloud console configuration workflows",
        "D": "Modify a count parameter to scale resources",
        "E": "API driven workflows"
    },
    "correct_answer": "B"
},
# Вопрос 144
144: {
    "question": "You're writing a Terraform configuration that needs to read input from a local file called id_rsa.pub. Which built-in Terraform function can you use to import the file's contents as a string?",
    "options": {
        "A": "fileset('id_rsa.pub')",
        "B": "filebase64('id_rsa.pub')",
        "C": "templatefile('id_rsa.pub')",
        "D": "file('id_rsa.pub')"
    },
    "correct_answer": "A"
},
# Вопрос 145
145: {
    "question": "What does Terraform use providers for? (Choose three.)",
    "options": {
        "A": "Provision resources for on-premises infrastructure services",
        "B": "Simplify API interactions",
        "C": "Provision resources for public cloud infrastructure services",
        "D": "Enforce security and compliance policies",
        "E": "Group a collection of Terraform configuration files that map to a single state file"
    },
    "correct_answer": "ABC"
},
# Вопрос 146
146: {
    "question": "You can reference a resource created with for_each using a Splat (*) expression.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 147
147: {
    "question": "How does Terraform determine dependencies between resources?",
    "options": {
        "A": "Terraform automatically builds a resource graph based on resources, provisioners, special meta-parameters, and the state file, if present.",
        "B": "Terraform requires all dependencies between resources to be specified using the depends_on parameter",
        "C": "Terraform requires resources in a configuration to be listed in the order they will be created to determine dependencies",
        "D": "Terraform requires resource dependencies to be defined as modules and sourced in order"
    },
    "correct_answer": "A"
},
# Вопрос 148
148: {
    "question": "Which parameters does terraform import require? (Choose two.)",
    "options": {
        "A": "Path",
        "B": "Provider",
        "C": "Resource ID",
        "D": "Resource address"
    },
    "correct_answer": "CD"
},
# Вопрос 149
149: {
    "question": "Once a new Terraform backend is configured with a Terraform code block, which command(s) is (are) used to migrate the state file?",
    "options": {
        "A": "terraform apply",
        "B": "terraform push",
        "C": "terraform destroy, then terraform apply",
        "D": "terraform init"
    },
    "correct_answer": "D"
},
# Вопрос 150
150: {
    "question": "What does this code do?",
    "options": {
        "A": "Requires any version of the AWS provider >= 3.0 and < 4.0",
        "B": "Requires any version of the AWS provider >= 3.0",
        "C": "Requires any version of the AWS provider after the 3.0 major release, like 4.1",
        "D": "Requires any version of the AWS provider > 3.0"
    },
    "correct_answer": "A"
},

151: {
    "question": "What does terraform refresh modify?",
    "options": {
        "A": "Your cloud infrastructure",
        "B": "Your state file",
        "C": "Your Terraform plan",
        "D": "Your Terraform configuration"
    },
    "correct_answer": "B"
},
# Вопрос 152
152: {
    "question": "Which of the following is not valid source path for specifying a module?",
    "options": {
        "A": "source = './modulelversion=v1.0.0'",
        "B": "source = 'github.com/hashicorp/example?ref=v1.0.0'",
        "C": "source = './module'",
        "D": "source = 'hashicorp/consul/aws'"
    },
    "correct_answer": "A"
},
# Вопрос 153
153: {
    "question": "Which of the following is true about terraform apply? (Choose two.)",
    "options": {
        "A": "It only operates on infrastructure defined in the current working directory or workspace",
        "B": "You must pass the output of a terraform plan command to it",
        "C": "Depending on provider specification, Terraform may need to destroy and recreate your infrastructure resources",
        "D": "By default, it does not refresh your state file to reflect current infrastructure configuration",
        "E": "You cannot target specific resources for the operation"
    },
    "correct_answer": "AC"
},
# Вопрос 154
154: {
    "question": "Which of the following statements about local modules is incorrect?",
    "options": {
        "A": "Local modules are not cached by terraform init command",
        "B": "Local modules are sourced from a directory on disk",
        "C": "Local modules support versions",
        "D": "All of the above (all statements above are incorrect)",
        "E": "None of the above (all statements above are correct)"
    },
    "correct_answer": "C"
},
# Вопрос 155
155: {
    "question": "Which of the following is true about Terraform's implementation of infrastructure as code? (Choose two.)",
    "options": {
        "A": "It is only compatible with AWS infrastructure management",
        "B": "You cannot reuse infrastructure configuration",
        "C": "You can version your infrastructure configuration",
        "D": "It requires manual configuration of infrastructure resources",
        "E": "It allows you to automate infrastructure provisioning"
    },
    "correct_answer": "CE"
},
# Вопрос 156
156: {
    "question": "You need to write some Terraform code that adds 42 firewall rules to a security group as shown in the example. What can you use to avoid writing 42 different nested ingress config blocks by hand?",
    "options": {
        "A": "A count loop",
        "B": "A for block",
        "C": "A for each block",
        "D": "A dynamic block"
    },
    "correct_answer": "D"
},
# Вопрос 157
157: {
    "question": "Which of the following is the safest way to inject sensitive values into a Terraform Cloud workspace?",
    "options": {
        "A": "Write the value to a file and specify the file with the -var-file flag",
        "B": "Set a value for the variable in the UI and check the 'Sensitive' check box",
        "C": "Edit the state file directly just before running terraform apply",
        "D": "Set the variable value on the command line with the -var flag"
    },
    "correct_answer": "B"
},
# Вопрос 158
158: {
    "question": "terraform apply will fail if you have not run terraform plan first to update the plan output.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 159
159: {
    "question": "How would you reference the attribute 'name' of this fictitious resource in HCL?",
    "options": {
        "A": "resource.kubernetes_namespace.example.name",
        "B": "kubernetes_namespace.test.name",
        "C": "kubernetes_namespace.example.name",
        "D": "data.kubernetes_namespace.name",
        "E": "None of the above"
    },
    "correct_answer": "C"
},
# Вопрос 160
160: {
    "question": "A Terraform output that sets the 'sensitive' argument to true will not store that value in the state file.",
    "options": {
        "A": "True",
        "B": "False"
    },
  "correct_answer": "B"
}
,

 # Вопрос 161
161: {
    "question": "Which are forbidden actions when the Terraform state file is locked? (Choose three.)",
    "options": {
        "A": "terraform destroy",
        "B": "terraform fmt",
        "C": "terraform state list",
        "D": "terraform apply",
        "E": "terraform plan",
        "F": "terraform validate"
    },
    "correct_answer": "ADE"
},
# Вопрос 162
162: {
    "question": "Terraform installs its providers during which phase?",
    "options": {
        "A": "Plan",
        "B": "Init",
        "C": "Refresh",
        "D": "All of the above"
    },
    "correct_answer": "B"
},
# Вопрос 163
163: {
    "question": "When does Sentinel enforce policy logic during a Terraform Enterprise run?",
    "options": {
        "A": "Before the plan phase",
        "B": "During the plan phase",
        "C": "Before the apply phase",
        "D": "After the apply phase"
    },
    "correct_answer": "C"
},
# Вопрос 164
164: {
    "question": "What is the purpose of a Terraform workspace in either open source or enterprise?",
    "options": {
        "A": "Workspaces allow you to manage collections of infrastructure in state files",
        "B": "A logical separation of business units",
        "C": "A method of grouping multiple infrastructure security policies",
        "D": "Provides limited access to a cloud environment"
    },
    "correct_answer": "A"
},
# Вопрос 165
165: {
    "question": "Which is the best way to specify a tag of v1.0.0 when referencing a module stored in Git (for example git::https://example.com/vpc.git)?",
    "options": {
        "A": "Append ?ref=v1.0.0 argument to the source path",
        "B": "Add version = '1.0.0' parameter to module block",
        "C": "Nothing - modules stored on GitHub always default to version 1.0.0",
        "D": "Modules stored on GitHub do not support versioning"
    },
    "correct_answer": "A"
},
# Вопрос 166
166: {
    "question": "Changing the Terraform backend from the default 'local' backend to a different one after doing your first terraform apply is:",
    "options": {
        "A": "Mandatory",
        "B": "Optional",
        "C": "Impossible",
        "D": "Discouraged"
    },
    "correct_answer": "B"
},
# Вопрос 167
167: {
    "question": "You have modified your local Terraform configuration and ran terraform plan to review the changes. Simultaneously, your teammate manually modified the infrastructure component you are working on. Since you already ran terraform plan locally, the execution plan for terraform apply will be the same.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 168
168: {
    "question": "terraform apply is failing with the following error. What next step should you take to determine the root cause of the problem? Error loading state: AccessDenied: Access Denied status code: 403, request id: 288766CE5CCA24A0, host id: FOOBAR",
    "options": {
        "A": "Set TF_LOG=DEBUG",
        "B": "Review syslog for Terraform error messages",
        "C": "Run terraform login to reauthenticate with the provider",
        "D": "Review /var/log/terraform.log for error messages"
    },
    "correct_answer": "A"
},
# Вопрос 169
169: {
    "question": "As a member of an operations team that uses infrastructure as code (IaC) practices, you are tasked with making a change to an infrastructure stack running in a public cloud. Which pattern would follow IaC best practices for making a change?",
    "options": {
        "A": "Clone the repository containing your infrastructure code and then run the code",
        "B": "Use the public cloud console to make the change after a database record has been approved",
        "C": "Make the change programmatically via the public cloud CLI",
        "D": "Make the change via the public cloud API endpoint",
        "E": "Submit a pull request and wait for an approved merge of the proposed changes"
    },
    "correct_answer": "E"
},
# Вопрос 170
170: {
    "question": "What command can you run to generate DOT (Document Template) formatted data to visualize Terraform dependencies?",
    "options": {
        "A": "terraform refresh",
        "B": "terraform show",
        "C": "terraform graph",
        "D": "terraform output"
    },
    "correct_answer": "C"
},

 171: {
    "question": "Which provider authentication method prevents credentials from being stored in the state file?",
    "options": {
        "A": "Using environment variables",
        "B": "Specifying the login credentials in the provider block",
        "C": "Setting credentials as Terraform variables",
        "D": "None of the above"
    },
    "correct_answer": "A"
},
# Вопрос 172
172: {
    "question": "Running terraform fmt without any flags in a directory with Terraform configuration files will check the formatting of those files without changing their contents.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 173
173: {
    "question": "terraform init retrieves the source code for all referenced modules.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "A"
},
# Вопрос 174
174: {
    "question": "You have a Terraform configuration that defines a single virtual machine with no references to it. You have run terraform apply to create the resource, and then removed the resource definition from your Terraform configuration file. What will happen when you run terraform apply in the working directory again?",
    "options": {
        "A": "Nothing",
        "B": "Terraform will destroy the virtual machine",
        "C": "Terraform will error",
        "D": "Terraform will remove the virtual machine from the state file, but the resource will still exist"
    },
    "correct_answer": "B"
},
# Вопрос 175
175: {
    "question": "Which configuration consistency errors does terraform validate report?",
    "options": {
        "A": "A mix of spaces and tabs in configuration files",
        "B": "Differences between local and remote state",
        "C": "Terraform module isn't the latest version",
        "D": "Declaring a resource identifier more than once"
    },
    "correct_answer": "D"
},
# Вопрос 176
176: {
    "question": "In Terraform HCL, an object type of object( name=string, age=number ) would match this value:",
    "options": {
        "A": "John fifty two",
        "B": "John 52"
    },
    "correct_answer": "B"
},
# Вопрос 177
177: {
    "question": "Where can Terraform not load a provider from?",
    "options": {
        "A": "Source code",
        "B": "Plugins directory",
        "C": "Official HashiCorp distribution on releases.hashicorp.com",
        "D": "Provider plugin cache"
    },
    "correct_answer": "A"
},
# Вопрос 178
178: {
    "question": "Which of the following locations can Terraform use as a private source for modules? (Choose two.)",
    "options": {
        "A": "Internally hosted SCM (Source Control Manager) platform",
        "B": "Public Terraform Module Registry",
        "C": "Private repository on GitHub",
        "D": "Public repository on GitHub"
    },
    "correct_answer": "AC"
},
# Вопрос 179
179: {
    "question": "Why should secrets not be hard coded into Terraform code? (Choose two.)",
    "options": {
        "A": "It makes the code less reusable.",
        "B": "Terraform code is typically stored in version control, as well as copied to the systems from which it's run. Any of those may not have robust security mechanisms.",
        "C": "The Terraform code is copied to the target resources to be applied locally and could expose secrets if a target resource is compromised.",
        "D": "All passwords should be rotated on a quarterly basis."
    },
    "correct_answer": "AB"
},
# Вопрос 180
180: {
    "question": "If a Terraform creation-time provisioner fails, what will occur by default?",
    "options": {
        "A": "The resource will not be affected, but the provisioner will need to be applied again",
        "B": "The resource will be destroyed",
        "C": "The resource will be marked as 'tainted'",
        "D": "Nothing, provisioners will not show errors in the command line"
    },
    "correct_answer": "C"
},
# Вопрос 181
181: {
    "question": "When should Terraform configuration files be written when running terraform import on existing infrastructure?",
    "options": {
        "A": "Infrastructure can be imported without corresponding Terraform code",
        "B": "Terraform will generate the corresponding configuration files for you",
        "C": "You should write Terraform configuration files after the next terraform import is executed",
        "D": "Terraform configuration should be written before terraform import is executed"
    },
    "correct_answer": "D"
},
# Вопрос 182
182: {
    "question": "Which command lets you experiment with Terraform's built-in functions?",
    "options": {
        "A": "terraform env",
        "B": "terraform console",
        "C": "terraform test",
        "D": "terraform validate"
    },
    "correct_answer": "B"
},
# Вопрос 183
183: {
    "question": "Why does this backend configuration not follow best practices?",
    "options": {
        "A": "You should not store credentials in Terraform Configuration",
        "B": "You should use the local enhanced storage backend whenever possible",
        "C": "An alias meta-argument should be included in backend blocks whenever possible",
        "D": "The backend configuration should contain multiple credentials so that more than one user can execute terraform plan and terraform apply answer A"
    },
    "correct_answer": "A"
},
# Вопрос 184
184: {
    "question": "Open source Terraform can only import publicly-accessible and open-source modules.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 185
185: {
    "question": "What does terraform destroy do?",
    "options": {
        "A": "Destroy all infrastructure in the Terraform state file",
        "B": "Destroy all Terraform code files in the current directory while leaving the state file intact",
        "C": "Destroy all infrastructure in the configured Terraform provider",
        "D": "Destroy the Terraform state file while leaving infrastructure intact answer A"
    },
    "correct_answer": "A"
},

   186: {
    "question": "While attempting to deploy resources into your cloud provider using Terraform, you begin to see some odd behavior and experience sluggish responses. In order to troubleshoot, you decide to turn on Terraform debugging. Which environment variables must be configured to make Terraform's logging more verbose?",
    "options": {
        "A": "TF_LOG_LEVEL",
        "B": "TF_LOG_FILE",
        "C": "TF_LOG",
        "D": "TP_LOG_PATH answer C"
    },
   "correct_answer": "C" 
   },

# Вопрос 187
187: {
    "question": "If a DevOps team adopts AWS CloudFormation as their standardized method for provisioning public cloud resources, which of the following scenarios poses a challenge for this team?",
    "options": {
        "A": "The team is asked to build a reusable code base that can deploy resources into any AWS region",
        "B": "The team is asked to manage a new application stack built on AWS-native services",
        "C": "The organization decides to expand into Azure and wishes to deploy new infrastructure using their existing codebase",
        "D": "The DevOps team is tasked with automating a manual provisioning process answer C"
    },
    "correct_answer": "C"
},
# Вопрос 188
188: {
    "question": "You cannot install third party plugins using terraform init.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},
# Вопрос 189
189: {
    "question": "Which of the following can you do with terraform plan? (Choose two.)",
    "options": {
        "A": "Save a generated execution plan to apply later",
        "B": "Execute a plan in a different workspace",
        "C": "View the execution plan and check if the changes match your expectations",
        "D": "Schedule Terraform to run at a planned time in the future answer AC"
    },
    "correct_answer": "AC"
},
# Вопрос 190
190: {
    "question": "Which are examples of infrastructure as code? (Choose two.)",
    "options": {
        "A": "Cloned virtual machine images",
        "B": "Change management database records",
        "C": "Versioned configuration files",
        "D": "Docker files answer CD"
    },
    "correct_answer": "CD"
},
# Вопрос 191
191: {
    "question": "FILL BLANK - You need to migrate a workspace to use a remote backend. After updating your configuration, what command do you run to perform the migration?",
    "options": {"A": "terraform init"},
    "correct_answer": "A"

},
# Вопрос 192
192: {
    "question": "When using a module from the public Terraform Module Registry, the following parameters are required attributes in the module block. (Choose two.)",
    "options": {
        "A": "Each of the module’s required inputs",
        "B": "The module’s source address",
        "C": "Terraform Module Registry account token",
        "D": "Each of the module’s dependencies (example: submodules)",
        "E": "The version of the module answer AB"
    },
    "correct_answer": "AB"
},
# Вопрос 193
193: {
    "question": "As a developer, you want to ensure your plugins are up to date with the latest versions. Which Terraform command should you use?",
    "options": {
        "A": "terraform init -upgrade",
        "B": "terraform apply -upgrade",
        "C": "terraform refresh -upgrade",
        "D": "terraform providers -upgrade answer A"
    },
    "correct_answer": "A"
},
# Вопрос 194
194: {
    "question": "You can access state stored with the local backend by using the terraform_remote_state data source.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "A"
},
# Вопрос 195
195: {
    "question": "You have been working in a Cloud provider account that is shared with other team members. You previously used Terraform to create a load balancer that is listening on port 80. After some application changes, you updated the Terraform code to change the port to 443. You run terraform plan and see that the execution plan shows the port changing from 80 to 443 like you intended, and step away to grab some coffee. In the meantime, another team member manually changes the load balancer port to 443 through the Cloud provider console before you get back to your desk. What will happen when you terraform apply upon returning to your desk?",
    "options": {
        "A": "Terraform will fail with an error because the state file is no longer accurate.",
        "B": "Terraform will change the load balancer port to 80, and then change it back to 443.",
        "C": "Terraform will not make any changes to the Load Balancer and will update the state file to reflect any changes made.",
        "D": "Terraform will change the port back to 80 in your code."
    },
    "correct_answer": "C"
},
# Вопрос 196
196: {
    "question": "In a Terraform Cloud workspace linked to a version control repository, speculative plan runs start automatically when you merge or commit changes to version control.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "A"
},

197: {
    "question": "You have some Terraform code and a variable definitions file named dev.auto.tfvars that you tested successfully in the dev environment. You want to deploy the same code in the staging environment with a separate variable definition file and a separate state file. Which two actions should you perform? (Choose two.)",
    "options": {
        "A": "Copy the existing terraform.tfstate file and save it as staging.terraform.tfstate",
        "B": "Write a new staging.auto.tfvars variable definition file and run Terraform with the var-file='staging.auto.tfvars' flag",
        "C": "Create a new Terraform workspace for staging",
        "D": "Create a new Terraform provider for staging",
        "E": "Add new Terraform code (*.tf files) for staging in the same directory"
    },
    "correct_answer": ["B" , "C"]
},

    198: {
    "question": "The ________ determines how Terraform creates, updates, or deletes resources.",
    "options": {
        "A": "Terraform configuration",
        "B": "Terraform core",
        "C": "Terraform provider",
        "D": "Terraform provisioner"
    },
    "correct_answer": "C"
},

199: {
    "question": "Terraform destroy is the only way to remove infrastructure.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},

200: {
    "question": "Which of the following is the correct way to pass the value in the variable num_servers into a module with the input servers in HCL2?",
    "options": {
        "A": "servers - var.num_servers",
        "B": "servers - num_servers",
        "C": "servers - var(num_servers)",
        "D": "$(var.num_servers)"
    },
    "correct_answer": "A"
},

201: {
    "question": "Which of the following commands would you use to access all of the attributes and details of a resource managed by Terraform?",
    "options": {
        "A": "terraform state list",
        "B": "terraform state show",
        "C": "terraform get",
        "D": "terraform state list"
    },
    "correct_answer": "B"
},

202: {
    "question": "How would you be able to reference an attribute from the vsphere_datacenter data source for use with the datacenter_id argument within the vsphere_folder resource in the following configuration?",
    "options": {
        "A": "data.dc.id",
        "B": "data.vsphere_datacenter.dc",
        "C": "vsphere_datacenter.dc.id",
        "D": "data.vsphere_datacenter.dc.id"
    },
    "correct_answer": "D"
},

203: {
    "question": "You decide to move a Terraform state file to Amazon S3 from another location. You write the code below into a file called backend.tf. Which command will migrate your current state file to the new S3 remote backend?",
    "options": {
        "A": "terraform state",
        "B": "terraform init",
        "C": "terraform refresh",
        "D": "terraform push"
    },
    "correct_answer": "B"
},

204: {
    "question": "You want to tag multiple resources with a string that is a combination of a generated random_id and a variable. How should you use the same value in all these resources without repeating the random_id and variable in each resource?",
    "options": {
        "A": "Local values",
        "B": "Data source",
        "C": "Modules",
        "D": "Outputs"
    },
    "correct_answer": "A"
},



   205: {
    "question": "Which of the following is not a benefit of adopting infrastructure as code?",
    "options": {
        "A": "Interpolation",
        "B": "Reusability of code",
        "C": "Versioning",
        "D": "Automation"
    },
    "correct_answer": "A"
},

206: {
    "question": "Module version is required to reference a module on the Terraform Module Registry.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},

207: {
    "question": "While deploying a virtual machine, the first launch user_data script fails due to a race condition with another resource deployed during the same Terraform run. What is the least disruptive method to correct the issue?",
    "options": {
        "A": "Run terraform taint against the virtual machine’s resource name, then terraform apply",
        "B": "Restart the virtual machine from the cloud portal",
        "C": "Run terraform apply again",
        "D": "Run terraform destroy then terraform apply"
    },
    "correct_answer": "A"
},

208: {
    "question": "The public Module Registry is free to use.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "A"
},

209: {
    "question": "Both Terraform Cloud and Terraform Enterprise support policy as code (Sentinel).",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "A"
},

210: {
    "question": "You want to define multiple data disks as nested blocks inside the resource block for a virtual machine. What Terraform feature would help you define the blocks using the values in a variable?",
    "options": {
        "A": "Local values",
        "B": "Collection functions",
        "C": "Dynamic blocks",
        "D": "Count arguments"
    },
    "correct_answer": "C"
},

211: {
    "question": "Which of the following module source paths does not specify a remote module?",
    "options": {
        "A": "source = “./modules/consul”",
        "B": "source = “[email protected]:hashicorp/example.git”",
        "C": "source = “github.com/hashicorp/example”",
        "D": "source = “hashicorp/consul/aws”"
    },
    "correct_answer": "C"
},

212: {
    "question": "You have a list of numbers that represents the number of free CPU cores on each virtual cluster: numcpus = [ 18, 3, 7, 11, 2 ] What Terraform function could you use to select the largest number from the list?",
    "options": {
        "A": "max(numcpus)",
        "B": "ceil(numcpus)",
        "C": "top(numcpus)",
        "D": "high[numcpus]"
    },
    "correct_answer": "A"
},

213: {
    "question": "Variables declared within a module are accessible outside of the module.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},

214: {
    "question": "Which of the following is not a valid Terraform variable type?",
    "options": {
        "A": "list",
        "B": "map",
        "C": "array",
        "D": "string"
    },
    "correct_answer": "C"
},

215: {
    "question": "What is a key benefit of the Terraform state file?",
    "options": {
        "A": "A state file can be used to schedule recurring infrastructure tasks",
        "B": "A state file represents a source of truth for resources provisioned with a public cloud console",
        "C": "A state file represents the desired state expressed by the Terraform code files",
        "D": "A state file represents a source of truth for resources provisioned with Terraform"
    },
    "correct_answer": "D"
},

216: {
    "question": "Which of these statements about Terraform Enterprise workspaces is false?",
    "options": {
        "A": "They can securely store cloud credentials",
        "B": "You must use the CLI to switch between workspaces",
        "C": "Plans and applies can be triggered via version control system integrations",
        "D": "They have role-based access controls"
    },
    "correct_answer": "B"
},

217: {
    "question": "Define the purpose of state in Terraform.",
    "options": {
        "A": "State is used to map real-world resources to your configuration and keep track of metadata",
        "B": "State is a method of codifying the dependencies of related resources",
        "C": "State is used to enforce resource configurations that relate to compliance policies",
        "D": "State is used to store variables and quickly reuse existing code"
    },
    "correct_answer": "A"
},

218: {
    "question": "Which backend does the Terraform CLI use by default?",
    "options": {
        "A": "API",
        "B": "Remote",
        "C": "Terraform Cloud",
        "D": "Local",
        "E": "HTTP"
    },
    "correct_answer": "D"
},

219: {
    "question": "Using the terraform state rm command against a resource will destroy it.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},

220: {
    "question": "Which method for sharing Terraform configurations keeps them confidential within your organization, supports Terraform’s semantic version constraints, and provides a browsable directory?",
    "options": {
        "A": "Generic git repository",
        "B": "Terraform Cloud/Terraform Enterprise private module registry",
        "C": "Public Terraform Module Registry",
        "D": "Subfolder within a workspace"
    },
    "correct_answer": "B"
},

221: {
    "question": "You are writing a child Terraform module that provisions an AWS instance. You want to make use of the IP address returned in the root configuration. You name the instance resource “main”. Which of these is the correct way to define the output value using HCL2?",
    "options": {
        "A": "value = aws_instance_ip_addr",
        "B": "value = ${main.private_ip}",
        "C": "value =${aws_intstance.main.private_ip}",
        "D": "return aws_intsance.main.private_ip"
    },
    "correct_answer": "A"
},

        222: {
        "question": "Which feature is not included in Terraform Cloud’s free tier?",
        "options": {
            "A": "Workspace",
            "B": "Remote state management",
            "C": "Audit logging",
            "D": "Private module registry",
        },
        "correct_answer": "C",    },

223: {
    "question": "Which feature is not included in Terraform Cloud’s free tier?",
    "options": {
        "A": "Workspace",
        "B": "Remote state management",
        "C": "Audit logging",
        "D": "Private module registry"
    },
    "correct_answer": "C"
},

224: {
    "question": "When should you run terraform init?",
    "options": {
        "A": "After you run terraform apply for the first time in a new Terraform project and before you run terraform plan",
        "B": "After you run terraform plan for the first time in a new Terraform project and before you run terraform apply",
        "C": "After you start coding a new Terraform project and before you run terraform plan for the first time",
        "D": "Before you start coding a new Terraform project"
    },
    "correct_answer": "C"
},

225: {
    "question": "Terraform configuration (including any module references) can contain only one Terraform provider type.",
    "options": {
        "A": "True",
        "B": "False"
    },
    "correct_answer": "B"
},

226: {
    "question": "You are making changes to existing Terraform code to add some new infrastructure. When is the best time to run terraform validate?",
    "options": {
        "A": "After you run terraform plan so you can validate that your state file is consistent with your infrastructure",
        "B": "Before you run terraform plan so you can validate your code syntax",
        "C": "Before you run terraform apply so you can validate your infrastructure changes",
        "D": "After you run terraform apply so you can validate that your infrastructure is reflected in your code"
    },
    "correct_answer": "B"
},

227: {
    "question": "How does Terraform manage most dependencies between resources?",
    "options": {
        "A": "By defining dependencies as modules and including them in a particular order",
        "B": "The order that resources appear in Terraform configuration indicates dependencies",
        "C": "Using the depends_on parameter",
        "D": "Terraform will automatically manage most resource dependencies"
    },
    "correct_answer": "D"
},

228: {
    "question": "What does running a terraform plan do?",
    "options": {
        "A": "Imports all of your existing cloud provider resources to the state file",
        "B": "Compares the state file to your Terraform code and determines if any changes need to be made",
        "C": "Imports all of your existing cloud provider resources to your Terraform configuration file",
        "D": "Compares your Terraform code and local state file to the remote state file in a cloud provider and determines if any changes need to be made"
    },
    "correct_answer": "B"
},

    229: {
        "question": "What are some benefits of using Sentinel with Terraform Cloud/Terraform Enterprise? (Choose three.)",
        "options": {
            "A": "Policy-as-code can enforce security best practices",
            "B": "You can restrict specific configurations on resources like 'CIDR=0.0.0.0/0' not allowed",
            "C": "You can enforce a list of approved AWS AMIs",
            "D": "Sentinel Policies can be written in HashiCorp Configuration Language (HCL)",
            "E": "You can check out and check in cloud access keys",
        },
        "correct_answer": ["A","B", "C"],    },

        230: {
        "question": "You want to share Terraform state with your team, store it securely, and provide state locking. How would you do this? (Choose three.)",
        "options": {
            "A": "Using the remote Terraform backend with Terraform Cloud / Terraform Enterprise.",
            "B": "Using the local backend.",
            "C": "Using the s3 terraform backend. The dynamodb_field option is not needed.",
            "D": "Using an s3 terraform backend with an appropriate IAM policy and dynamodb_field option configured.",
            "E": "Using the consul Terraform backend.",
        },
        "correct_answer": ["A","B","E"],    },

        231: {
        "question": "From which of these sources can Terraform import modules?",
        "options": {
            "A": "Local path",
            "B": "GitHub Repository",
            "C": "Terraform Module Registry",
            "D": "All of the above",
        },
        "correct_answer": "D",    },

        232: {
        "question": "How would you output returned values from a child module?",
        "options": {
            "A": "Declare the output in the root configuration",
            "B": "Declare the output in the child module",
            "C": "Declare the output in both the root and child module",
            "D": "None of the above",
        },
        "correct_answer": "B",    },
        233: {
        "question": "You have decided to create a new Terraform workspace to deploy a development environment. What is different about this workspace?",
        "options": {
            "A": "It has its own state file",
            "B": "It pulls in a different terraform.tfvars file",
            "C": "It uses a different branch of code",
            "D": "It uses a different backend",
        },
        "correct_answer": "A",    },

            234: {
        "question": "Any user can publish modules to the public Terraform Module Registry.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },
     235: {
        "question": "Which of these commands makes your code more human readable?",
        "options": {
            "A": "terraform validate",
            "B": "terraform output",
            "C": "terraform plan",
            "D": "terraform fmt",
        },
        "correct_answer": "D",    },
    236: {
        "question": "Infrastructure as Code (IaC) can be stored in a version control system along with application code.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },
        237: {
        "question": "Select the command that doesn’t cause Terraform to refresh its state.",
        "options": {
            "A": "terraform apply",
            "B": "terraform destroy",
            "C": "terraform plan",
            "D": "terraform state list",
        },
        "correct_answer": "D",    },
    238: {
        "question": "Sentinel policy-as-code is available in Terraform Enterprise.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },
        239: {
        "question": "Before you can use Terraform’s remote backend, you must first execute terraform init.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },
       240: {
        "question": "Which two steps are required to provision new infrastructure in the Terraform workflow? (Choose two.)",
        "options": {
            "A": "Plan",
            "B": "Apply",
            "C": "Import",
            "D": "Init",
            "E": "Validate",
        },
        "correct_answer": ["B", "D"],    },

        241: {
        "question": "You are working on some new application features and you want to spin up a copy of your production deployment to perform some quick tests. In order to avoid having to configure a new state backend, what open source Terraform feature would allow you create multiple states but still be associated with your current code?",
        "options": {
            "A": "Terraform data sources",
            "B": "Terraform local values",
            "C": "Terraform modules",
            "D": "Terraform workspaces",
            "E": "None of the above",
        },
        "correct_answer": "D",    },
    242: {
        "question": "Which provisioner invokes a process on the machine running Terraform?",
        "options": {
            "A": "remote-exec",
            "B": "file",
            "C": "local-exec",
            "D": "null-exec",
        },
        "correct_answer": "C",    },
            243: {
        "question": "____________ backends support state locking.",
        "options": {
            "A": "Some",
            "B": "No",
            "C": "Only local",
            "D": "All",
        },
        "correct_answer": "D",    },

    
    244: {
        "question": "Which of the following methods, used to provision resources into a public cloud, demonstrates the concept of infrastructure as code?",
        "options": {
            "A": "curl commands manually run from a terminal",
            "B": "A sequence of REST requests you pass to a public cloud API endpoint",
            "C": "A script that contains a series of public cloud CLI commands",
            "D": "A series of commands you enter into a public cloud console",
        },
        "correct_answer": "C",    },
        245: {
        "question": "Which of the following should you put into the required_providers block?",
        "options": {
            "A": "version >= 3.1",
            "B": 'version = ">= 3.1"',
            "C": "version ~> 3.1",
        },
        "correct_answer": "B",    },

   
    246: {
        "question": "When should you write Terraform configuration files for existing infrastructure that you want to start managing with Terraform?",
        "options": {
            "A": "Before you run terraform import",
            "B": "You can import infrastructure without corresponding Terraform code",
            "C": "Terraform will generate the corresponding configuration files for you",
            "D": "After you run terraform import",
        },
        "correct_answer": "A",    },

    
    247: {
        "question": "Which command should you run to check if all code in a Terraform configuration that references multiple modules is properly formatted without making changes?",
        "options": {
            "A": "terraform fmt -write=false",
            "B": "terraform fmt -list -recursive",
            "C": "terraform fmt -check -recursive",
            "D": "terraform fmt -check",
        },
        "correct_answer": "C",    },

    
    248: {
        "question": "What features stop multiple users from operating on the Terraform state at the same time?",
        "options": {
            "A": "Provider constraints",
            "B": "Remote backends",
            "C": "State locking",
            "D": "Version control",
        },
        "correct_answer": "C",    },

    
    249: {
        "question": "You are creating a reusable Terraform configuration and want to include a billing_dept tag so your Finance team can track team-specific spending on resources. Which of the following billing_dept variable declarations will allow you to do this?",
        "options": {
            "A": "optional = true",
            "B": "type = optional(string)",
            "C": 'default = ""',
            "D": "type = default",
        },
        "correct_answer": "C",    },

    
    250: {
        "question": "Which of these are secure options for storing secrets for connecting to a Terraform remote backend? (Choose two.)",
        "options": {
            "A": "Inside the backend block within the Terraform configuration",
            "B": "Defined in Environment variables",
            "C": "Defined in a connection configuration outside of Terraform",
            "D": "A variable file",
        },
        "correct_answer": ["B", "C"],    },
        251: {
        "question": "You want to define a single input variable to capture configuration values for a server. The values must represent memory as a number, and the server name as a string. Which variable type could you use for this input?",
        "options": {
            "A": "List",
            "B": "Object",
            "C": "Map",
            "D": "Terraform does not support complex input variables of different types",
        },
        "correct_answer": "B",    },

  
    252: {
        "question": "What does Terraform not reference when running a terraform apply -refresh-only?",
        "options": {
            "A": "Credentials",
            "B": "State file",
            "C": "Terraform resource definitions in configuration files",
            "D": "Cloud provider",
        },
        "correct_answer": "C",    },

    
    253: {
        "question": "Multiple team members are collaborating on infrastructure using Terraform and want to format their Terraform code following standard Terraform-style convention. How could they automatically ensure the code satisfies conventions?",
        "options": {
            "A": "Run the terraform fmt command during the code linting phase of your CI/CD process",
            "B": "Manually apply two spaces indentation and align equal sign '=' characters in every Terraform file (*.tf)",
            "C": "Run the terraform validate command prior to executing terraform plan or terraform apply",
        },
        "correct_answer": "A",    },

    254: {
        "question": "When using a remote backend or Terraform Cloud integration, where does Terraform save resource state?",
        "options": {
            "A": "On the disk",
            "B": "In memory",
            "C": "In an environment variable",
            "D": "In the remote backend or Terraform Cloud",
        },
        "correct_answer": "D",    },

    255: {
        "question": "In Terraform HCL, an object type of object( name=string, age=number ) would match this value:",
        "options": {
            "A": '"John\'\' fifty two',
            "B": '"John" 52',
            "C": "John fifty two",
            "D": "John 52",
        },
        "correct_answer": "B",    },

    256: {
        "question": "You add a new resource to an existing Terraform configuration, but do not update the version constraint in the configuration. The existing and new resources use the same provider. The working directory contains a .terraform-lock.hcl file. How will Terraform choose which version of the provider to use?",
        "options": {
            "A": "Terraform will use the latest version of the provider for the new resource and the version recorded in the lock file to manage existing resources",
            "B": "Terraform will use the version recorded in your lock file",
            "C": "Terraform will check your state file to determine the provider version to use",
            "D": "Terraform will use the latest version of the provider available at the time you provision your new resource",
        },
        "correct_answer": "B",    },


    257: {
        "question": "You must use different Terraform commands depending on the cloud provider you use.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    
    258: {
        "question": "Define the purpose of state in Terraform.",
        "options": {
            "A": "State stores variables and lets you quickly reuse existing code",
            "B": "State lets you enforce resource configurations that relate to compliance policies",
            "C": "State codifies the dependencies of related resources",
            "D": "State maps real-world resources to your configuration and keeps track of metadata",
        },
        "correct_answer": "D",    },

    259: {
        "question": "Which of these actions will prevent two Terraform runs from changing the same state file at the same time?",
        "options": {
            "A": "Refresh the state after running Terraform",
            "B": "Delete the state before running Terraform",
            "C": "Configure state locking for your state backend",
            "D": "Run Terraform with parallelism set to 1",
        },
        "correct_answer": "C",    },

    
    260: {
        "question": "While attempting to deploy resources into your cloud provider using Terraform, you begin to see some odd behavior and experience slow responses. In order to troubleshoot you decide to turn on Terraform debugging. Which environment variables must be configured to make Terraform’s logging more verbose?",
        "options": {
            "A": "TF_LOG_PATH",
            "B": "TF_VAR_log_level",
            "C": "TF_LOG",
            "D": "TF_VAR_log_path",
        },
        "correct_answer": "C",    },

    
    261: {
        "question": "The Terraform binary version and provider versions must match each other in a single configuration.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    
    262: {
        "question": "The .terraform.lock.hcl file tracks module versions.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    263: {
        "question": "You can develop a custom provider to manage its resources using Terraform.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },

    
    264: {
        "question": "Which of these is not a benefit of remote state?",
        "options": {
            "A": "Keeping unencrypted sensitive information off disk",
            "B": "Easily share reusable code modules",
            "C": "Working in a team",
            "D": "Delegate output to other teams",
        },
        "correct_answer": "D",    },

    
    265: {
        "question": "When using multiple configurations of the same Terraform provider, what meta-argument must be included in any non-default provider configurations?",
        "options": {
            "A": "depends_on",
            "B": "alias",
            "C": "id",
            "D": "name",
        },
        "correct_answer": "B",    },

    
    266: {
        "question": "A developer accidentally launched a VM (virtual machine) outside of the Terraform workflow and ended up with two servers with the same name. They don’t know which VM Terraform manages but do have a list of all active VM IDs. Which of the following methods could you use to discover which instance Terraform manages?",
        "options": {
            "A": "Run terraform taint on all the VMs to recreate them",
            "B": "Update the code to include outputs for the ID of all VMs, then run terraform plan to view the outputs",
            "C": "Run terraform state list to find the names of all VMs, then run terraform state show for each of them to find which VM ID Terraform manages",
            "D": "Use terraform refresh to find out which IDs are already part of the state",
        },
        "correct_answer": "C",    },

    267: {
        "question": "Which of the following is not considered a safe way to inject sensitive values into a Terraform Cloud workspace?",
        "options": {
            "A": "Edit the state file directly just before running terraform apply",
            "B": "Set the variable value on the command line with the -var flag",
            "C": "Write the value to a file and specify the file with the -var-file flag",
        },
        "correct_answer": "A",    },

    
    268: {
        "question": "If you update the version constraint in your Terraform configuration, Terraform will update your lock file the next time you run terraform init.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    269: {
        "question": "You must initialize your working directory before running terraform validate.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },

    
    270: {
        "question": "If you manually destroy infrastructure, what is the best practice reflecting this change in Terraform?",
        "options": {
            "A": "Manually update the state file",
            "B": "Remove the resource definition from your file and run terraform apply -refresh-only",
            "C": "Run terraform import",
            "D": "It will happen automatically",
        },
        "correct_answer": "B",    },
        271: {
        "question": "You created infrastructure outside of the Terraform workflow that you now want to manage using Terraform. Which command brings the infrastructure into Terraform state?",
        "options": {
            "A": "terraform init",
            "B": "terraform get",
            "C": "terraform refresh",
            "D": "terraform import",
        },
        "correct_answer": "D",    },

    # Question 272
    272: {
        "question": "When using Terraform to deploy resources into Azure, which scenarios are true regarding state files? (Choose two.)",
        "options": {
            "A": "When you change a Terraform-managed resource via the Azure Cloud Console, Terraform updates the state file to reflect the change during the next plan or apply",
            "B": "Changing resources via the Azure Cloud Console records the change in the current state file",
            "C": "When you change a resource via the Azure Cloud Console, Terraform records the changes in a new state file",
            "D": "Changing resources via the Azure Cloud Console does not update the current state file",
        },
        "correct_answer": ["C", "D"],    },

    # Question 273
    273: {
        "question": "Which statement describes a goal of infrastructure as code?",
        "options": {
            "A": "A pipeline process to test and deliver software",
            "B": "Defining a vendor-agnostic API",
            "C": "Write once, run anywhere",
            "D": "The programmatic configuration of resources",
        },
        "correct_answer": "D",    },

    # Question 274
    274: {
        "question": "terraform validate confirms the syntax of Terraform files.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },

    # Question 275
    275: {
        "question": "Which command adds existing resources into Terraform state?",
        "options": {
            "A": "terraform init",
            "B": "terraform plan",
            "C": "terraform refresh",
            "D": "terraform import",
            "E": "All of these",
        },
        "correct_answer": "D",    },

    # Question 276
    276: {
        "question": "It is best practice to store secret data in the same version control repository as your Terraform configuration.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    # Question 277
    277: {
        "question": "Which of the following commands would you use to access all of the attributes and details of a resource managed by Terraform?",
        "options": {
            "A": "terraform state list ‘provider_type.name’",
            "B": "terraform state show ‘provider_type.name’",
            "C": "terraform get ‘provider_type.name’",
            "D": "terraform state list",
        },
        "correct_answer": "B",    },

    # Question 278
    278: {
        "question": "terraform validate confirms that your infrastructure matches the Terraform state file.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    # Question 279
    279: {
        "question": "A senior admin accidentally deleted some of your cloud instances. What does Terraform do when you run terraform apply?",
        "options": {
            "A": "Build a completely brand new set of infrastructure",
            "B": "Tear down the entire workspace infrastructure and rebuild it",
            "C": "Rebuild only the instances that were deleted",
            "D": "Stop and generate an error message about the missing instances",
        },
        "correct_answer": "C",    },

    # Question 280
    280: {
        "question": "terraform init creates an example main.tf file in the current directory.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    # Question 281
    281: {
        "question": "Which argument helps prevent unexpected updates when calling Terraform Registry modules?",
        "options": {
            "A": "count",
            "B": "source",
            "C": "version",
            "D": "lifecycle",
        },
        "correct_answer": "C",    },

    # Question 282
    282: {
        "question": "Setting the TF_LOG environment variable to DEBUG causes debug messages to be logged into stdout.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    # Question 283
    283: {
        "question": "How would you output returned values from a child module in the Terraform CLI output?",
        "options": {
            "A": "Declare the output in the root configuration",
            "B": "Declare the output in the child module",
            "C": "Declare the output in both the root and child module",
            "D": "None of the above",
        },
        "correct_answer": "C",    },
    284: {
        "question": "What is the Terraform resource name of the following resource block?",
        "options": {
            "A": "azurerm_resource_group",
            "B": "azurerm",
            "C": "test",
            "D": "dev",
        },
        "correct_answer": "D",    },

    # Question 285
    285: {
        "question": "When do you need to explicitly execute terraform refresh-only?",
        "options": {
            "A": "Before every terraform plan",
            "B": "Before every terraform apply",
            "C": "Before every terraform import",
            "D": "None of the above",
        },
        "correct_answer": "D",    },

    # Question 286
    286: {
        "question": "How does the Terraform cloud integration differ from other state backends such as S3, Consul, etc.?",
        "options": {
            "A": "It can execute Terraform runs on dedicated infrastructure in Terraform Cloud",
            "B": "It doesn't show the output of a terraform apply locally",
            "C": "It is only available to paying customers",
            "D": "All of the above",
        },
        "correct_answer": "A",    },

    # Question 287
    287: {
        "question": "Which of the following are advantages of using infrastructure as code (IaC) instead of provisioning with a graphical user interface (GUI)? (Choose two.)",
        "options": {
            "A": "Secures your credentials",
            "B": "Lets you version, reuse, and share infrastructure configuration",
            "C": "Provisions the same resources at a lower cost",
            "D": "Reduces the risk of operator error",
            "E": "Prevents manual modifications to your resources",
        },
        "correct_answer": ["B", "D"],    },

    # Question 288
    288: {
        "question": "One cloud configuration always maps to a single remote workspace.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    # Question 289
    289: {
        "question": "Multiple team members are collaborating on infrastructure using Terraform and want to format their Terraform code following standard Terraform-style convention. How could they automatically ensure the code satisfies conventions?",
        "options": {
            "A": "Replace all tabs with spaces",
            "B": "Terraform automatically formats configuration on terraform apply",
            "C": "Run terraform validate prior to executing terraform plan or terraform apply",
            "D": "Use terraform fmt",
        },
        "correct_answer": "D",    },

    # Question 290
    290: {
        "question": "Which backend does the Terraform CLI use by default?",
        "options": {
            "A": "Depends on the cloud provider configured",
            "B": "Remote",
            "C": "Terraform Cloud",
            "D": "Local",
            "E": "HTTP",
        },
        "correct_answer": "D",    },

    # Question 291
    291: {
        "question": "The Terraform CLI will print output values from a child module after running terraform apply.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

    # Question 292
    292: {
        "question": "What does terraform refresh-only modify?",
        "options": {
            "A": "Your cloud infrastructure",
            "B": "Your Terraform plan",
            "C": "Your Terraform configuration",
            "D": "Your state file",
        },
        "correct_answer": "D",    },

    # Question 293
    293: {
        "question": "What does terraform import do?",
        "options": {
            "A": "Imports existing resources into the state file",
            "B": "Imports all infrastructure from a given cloud provider",
            "C": "Imports a new Terraform module",
            "D": "Imports clean copies of tainted resources",
            "E": "None of the above",
        },
        "correct_answer": "A",    },

        294: {
        "question": "Which of the following is the correct way to pass the value in the variable num_servers into a module with the input server?",
        "options": {
            "A": "servers = var(num_servers)",
            "B": "$(var.num_servers)",
            "C": "servers = num_servers",
            "D": "servers = var.num_servers",
        },
        "correct_answer": "D",    },

    # Question 295
    295: {
        "question": "A developer on your team is going to tear down an existing deployment managed by Terraform and deploy a new one. However, there is a server resource named aws_instance.ubuntu[1] they would like to keep. What command should they use to tell Terraform to stop managing that specific resource?",
        "options": {
            "A": "terraform destroy aws_instance.ubuntu[1]",
            "B": "terraform apply rm aws_instance.ubuntu[1]",
            "C": "terraform state rm aws_instance.ubuntu[1]",
            "D": "terraform plan rm aws_instance.ubuntu[1]",
        },
        "correct_answer": "C",    },

    # Question 296
    296: {
        "question": "Before you can use a remote backend, you must first execute terraform init.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "A",    },

    # Question 297
    297: {
        "question": "What does running a terraform plan do?",
        "options": {
            "A": "Compares your Terraform code and local state file to the remote state file in a cloud provider and determines if any changes need to be made",
            "B": "Imports all of your existing cloud provider resources to the state file",
            "C": "Installs all providers and modules referenced by configuration",
            "D": "Compares the state file to your Terraform code and determines if any changes need to be made",
        },
        "correct_answer": "D",    },

    # Question 298
    298: {
        "question": "Which of the following statements about Terraform modules is not true?",
        "options": {
            "A": "Modules must be publicly accessible",
            "B": "You can call the same module multiple times",
            "C": "A module is a container for one or more resources",
            "D": "Modules can call other modules",
        },
        "correct_answer": "A",    },

    # Question 299
    299: {
        "question": "How can a ticket-based system slow down infrastructure provisioning and limit the ability to scale? (Choose two.)",
        "options": {
            "A": "End-users have to request infrastructure changes",
            "B": "Ticket-based systems generate a full audit trail of the request and fulfillment process",
            "C": "Users can access a catalog of approved resources from drop-down lists in a request form",
            "D": "The more resources your organization needs, the more tickets your infrastructure team has to process",
        },
        "correct_answer": ["A", "D"],    },

    # Question 300
    300: {
        "question": "How do you specify a module's version when publishing it to the public Terraform Module Registry?",
        "options": {
            "A": "Configure it in the module's Terraform code",
            "B": "Mention it on the module's configuration page on the Terraform Module Registry",
            "C": "The Terraform Module Registry does not support versioning modules",
            "D": "Tag a release in the associated repo",
        },
        "correct_answer": "D",    },

    # Question 301
    301: {
        "question": "What Terraform command always causes a state file to be updated with changes that might have been made outside of Terraform?",
        "options": {
            "A": "terraform plan -refresh-only",
            "B": "terraform show -json",
            "C": "terraform apply -lock-false",
            "D": "terraform plan -target-state",
        },
        "correct_answer": "A",    },

    # Question 302
    302: {
        "question": "Which command lets you experiment with Terraform expressions?",
        "options": {
            "A": "terraform console",
            "B": "terraform validate",
            "C": "terraform env",
            "D": "terraform test",
        },
        "correct_answer": "A",    },

    # Question 303
    303: {
        "question": "What kind of configuration block will create an infrastructure object with settings specified within the block?",
        "options": {
            "A": "provider",
            "B": "state",
            "C": "data",
            "D": "resource",
        },
        "correct_answer": "D",    },

    # Question 304
    304: {
        "question": "When do changes invoked by terraform apply take effect?",
        "options": {
            "A": "After Terraform has updated the state file",
            "B": "Once the resource provider has fulfilled the request",
            "C": "Immediately",
            "D": "None of the above are correct",
        },
        "correct_answer": "B",    },

    # Question 305
    305: {
        "question": "What is the workflow for deploying new infrastructure with Terraform?",
        "options": {
            "A": "Write Terraform configuration, run 'terraform init' to initialize the working directory or workspace, and run 'terraform apply'",
            "B": "Write Terraform configuration, run 'terraform show' to view proposed changes, and 'terraform apply' to create new infrastructure",
            "C": "Write Terraform configuration, run 'terraform apply' to create infrastructure, use 'terraform validate' to confirm Terraform deployed resources correctly",
            "D": "Write Terraform configuration, run 'terraform plan' to initialize the working directory or workspace, and 'terraform apply' to create the infrastructure",
        },
        "correct_answer": "A",    },

    # Question 306
    306: {
        "question": "Which of these are features of Terraform Cloud? (Choose two.)",
        "options": {
            "A": "Remote state storage",
            "B": "A web-based user interface (UI)",
            "C": "Automatic backups",
            "D": "Automated infrastructure deployment visualization",
        },
        "correct_answer": ["A", "B"],    },

    # Question 307
    307: {
        "question": "Which option can not keep secrets out of Terraform configuration files?",
        "options": {
            "A": "A shared credential file",
            "B": "Mark the variable as sensitive",
            "C": "Environment Variables",
            "D": "A -var flag",
        },
        "correct_answer": "B",    },

    # Question 308
    308: {
        "question": "Which of the following is not true of Terraform providers?",
        "options": {
            "A": "An individual person can write a Terraform Provider",
            "B": "A community of users can maintain a provider",
            "C": "HashiCorp maintains some providers",
            "D": "Cloud providers and infrastructure vendors can write, maintain, or collaborate on Terraform providers",
            "E": "None of the above",
        },
        "correct_answer": "D",    },

    # Question 309
    309: {
        "question": "Which Terraform command checks that your configuration syntax is correct?",
        "options": {
            "A": "terraform fmt",
            "B": "terraform validate",
            "C": "terraform init",
            "D": "terraform show",
        },
        "correct_answer": "B",    },

    # Question 310
    310: {
        "question": "terraform validate uses provider APIs to verify your infrastructure settings.",
        "options": {
            "A": "True",
            "B": "False",
        },
        "correct_answer": "B",    },

}
    # Add more questions following the same format...

# Function to ask a question and check the answer
def present_question(question_data):
    print("\n" + "=" * 50)
    print(question_data["question"])
    print("-" * 50)
    for option, text in question_data["options"].items():
        print(f"{option}. {text}")
    print("=" * 50)
    user_answer = input("Your answer: ")
    return user_answer.upper()

def check_answer(question_data, user_answer):
    correct_answer = question_data["correct_answer"]
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def main():
    question_numbers = list(questions.keys())
    random.shuffle(question_numbers)

    for question_number in question_numbers:
        question_data = questions[question_number]
        user_answer = present_question(question_data)
        check_answer(question_data, user_answer)

if __name__ == "__main__":
    main()