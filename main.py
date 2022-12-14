from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class GnomeSessionExtension(Extension):
    def __init__(self):
        super(GnomeSessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = []
        options = [
                        'ec2', 'ecs', 'rds', 's3', 'elasticbeanstalk', 'elasticache', 'cloudwatch', 'cloudformation', 'vpc', 'iam', 'ecr', 'eks', 'lambda', 'dynamodb',
                        'managementconsole', 'management', 'console',
                        'support', 'ticket', 'helpdesk', 'help',
                        'billing', 'budget', 'costs',
                        'pricingcalculator', 'pricing', 'price', 'prices', 'calculate', 'calculator',
                        'compare', 'instancecomparison', 'comparison',
                        'route53', 'dns', 'sqs', 'sns', 'ses', 'elasticsearch', 'kms', 'cloudfront', 'api', 'gateway',
                        'cloudtrail', 'secret', 'systemsmanager'
                  ]
        my_list = event.query.split(" ")
        if len(my_list) == 1:
            items.append(get_ec2_item())
            items.append(get_ecs_item())
            items.append(get_rds_item())
            items.append(get_s3_item())
            items.append(get_elasticbeanstalk_item())
            items.append(get_elasticache_item())
            items.append(get_cloudwatch_item())
            items.append(get_cloudformation_item())
            items.append(get_vpc_item())
            items.append(get_iam_item())
            items.append(get_ecr_item())
            items.append(get_eks_item())
            items.append(get_lambda_item())
            items.append(get_dynamodb_item())
            items.append(get_managementconsole_item())
            items.append(get_support_item())
            items.append(get_billing_item())
            items.append(get_pricingcalculator())
            items.append(get_compare())
            items.append(get_route53_item())
            items.append(get_sqs_item())
            items.append(get_sns_item())
            items.append(get_ses_item())
            items.append(get_cloudfront_item())
            items.append(get_kms_item())
            items.append(get_elasticsearch_item())
            items.append(get_api_gateway_item())
            items.append(get_secret_item())
            items.append(get_cloudtrail_item())
            items.append(get_systemsmanager_item())
            return RenderResultListAction(items)
        else:
            my_query = my_list[1]
            included = []
            for option in options:
                if my_query in option:
                    if option in ['ec2']:
                        items.append(get_ec2_item())
                    elif option in ['ecs']:
                        items.append(get_ecs_item())
                    elif option in ['rds']:
                        items.append(get_rds_item())
                    elif option in ['s3']:
                        items.append(get_s3_item())
                    elif option in ['elasticbeanstalk']:
                        items.append(get_elasticbeanstalk_item())
                    elif option in ['elasticache']:
                        items.append(get_elasticache_item())
                    elif option in ['cloudwatch']:
                        items.append(get_cloudwatch_item())
                    elif option in ['cloudformation']:
                        items.append(get_cloudformation_item())
                    elif option in ['vpc']:
                        items.append(get_vpc_item())
                    elif option in ['iam']:
                        items.append(get_iam_item())
                    elif option in ['ecr']:
                        items.append(get_ecr_item())
                    elif option in ['eks']:
                        items.append(get_eks_item())
                    elif option in ['lambda']:
                        items.append(get_lambda_item())
                    elif option in ['dynamodb']:
                        items.append(get_dynamodb_item())
                    elif option in ['managementconsole', 'management', 'console'] and 'managementconsole' not in included:
                        items.append(get_managementconsole_item())
                        included.append('managementconsole')
                    elif option in ['support', 'ticket', 'helpdesk', 'help'] and 'support' not in included:
                        items.append(get_support_item())
                        included.append('support')
                    elif option in ['billing', 'budget', 'costs'] and 'billing' not in included:
                        items.append(get_billing_item())
                        included.append('billing')
                    elif option in ['pricingcalculator', 'pricing', 'price', 'prices', 'calculate', 'calculator'] and 'pricingcalculator' not in included:
                        items.append(get_pricingcalculator())
                        included.append('pricingcalculator')
                    elif option in ['compare', 'instancecomparison', 'comparison'] and 'compare' not in included:
                        items.append(get_compare())
                        included.append('compare')
                    elif option in ['route53', 'dns'] and 'route53' not in included:
                        items.append(get_route53_item())
                        included.append('route53')
                    elif option in ['sqs']:
                        items.append(get_sqs_item())
                    elif option in ['sns']:
                        items.append(get_sns_item())
                    elif option in ['ses']:
                        items.append(get_ses_item())
                    elif option in ['cloudfront']:
                        items.append(get_cloudfront_item())
                    elif option in ['kms']:
                        items.append(get_kms_item())
                    elif option in ['elasticsearch']:
                        items.append(get_elasticsearch_item())
                    elif option in ['api', 'gateway']:
                        items.append(get_api_gateway_item())
                    elif option in ['secret']:
                        items.append(get_secret_item())
                    elif option in ['cloudtrail']:
                        items.append(get_cloudtrail_item())
                    elif option in ['systemsmanager']:
                        items.append(get_systemsmanager_item())
            return RenderResultListAction(items)

def get_api_gateway_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS API Gateway',
                               description='AWS API Gateway',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_elasticsearch_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Elasticsearch',
                               description='AWS Elasticsearch Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))
def get_kms_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS KMS',
                               description='AWS Key Management Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))
def get_cloudfront_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Cloudfront',
                               description='AWS CloudFront Manager',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))
def get_ec2_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS EC2',
                               description='AWS Elastic Compute Cloud',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))
def get_ecs_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS ECS',
                               description='EC2 Container Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_rds_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS RDS',
                               description='AWS Relational Database Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_s3_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS S3',
                               description='AWS Simple Storage Service',
                               on_enter=OpenUrlAction("https://s3.console.aws.amazon.com/s3"))

def get_elasticbeanstalk_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS ElasticBeanstalk',
                               description='AWS ElasticBeanstalk Application Environment',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_elasticache_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS ElastiCache',
                               description='AWS ElastiCache (Redis, Memcached, etc.)',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_cloudwatch_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS CloudWatch',
                               description='AWS CloudWatch Metrics and Monitoring',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_cloudformation_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS CloudFormation',
                               description='AWS Cloud Formation Cosole',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_vpc_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS VPC',
                               description='AWS Virtual Private Cloud',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_iam_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS IAM',
                               description='AWS Identity & Access Management',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_ecr_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS ECR',
                               description='AWS Elastic Container Registry',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_eks_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS EKS',
                               description='AWS Kubernetes Management Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_lambda_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Lambda',
                               description='AWS Lambda Serverless Computing',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_dynamodb_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS DynamoDB',
                               description='AWS DynamoDB NoSQL Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_managementconsole_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Management Console',
                               description='Manage all your AWS infrastructure',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_support_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Support Console',
                               description='Access AWS customer and business support ticketing system',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_billing_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Billing Dashboard',
                               description='AWS Billing & Cost Management Center. Manage Billing, Budgets, Cost Explorer and Reports ',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_pricingcalculator():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Pricing Calculator',
                               description='AWS Pricing Calculator',
                               on_enter=OpenUrlAction("https://calculator.s3.amazonaws.com/index.html"))

def get_compare():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Instance Comparision',
                               description='EC2Instances.info Easy Amazon EC2 Instance Comparison',
                               on_enter=OpenUrlAction("https://www.ec2instances.info"))

def get_route53_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Route 53',
                               description='AWS Route 53 Domain & DNS Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_sqs_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Simple Queue Service',
                               description='AWS SQS Managed Message Queues',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_sns_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Simple Notification Service',
                               description='AWS SNS managed message topics for Pub/Sub',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk/v3"))

def get_ses_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Simple Email Service',
                               description='AWS SES Email Sending and Receiving Service',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_secret_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Secrets Manager',
                               description='AWS Secrets Manager',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_cloudtrail_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS CloudTrail',
                               description='AWS CloudTrail',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk"))

def get_systemsmanager_item():
    return ExtensionResultItem(icon='images/icon.png',
                               name='AWS Systems Manager',
                               description='AWS Systems Manager',
                               on_enter=OpenUrlAction("https://www.youtube.com/watch?v=ZAqh1Q2bpCk-manager"))

if __name__ == '__main__':
    GnomeSessionExtension().run()
