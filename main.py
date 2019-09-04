import boto3

session = boto3.Session(profile_name='default')

client = session.client('ce')

start =  '2019-05-01'
end = '2019-07-17'

response = client.get_cost_and_usage(
    TimePeriod = {
        'Start': start,
        'End': end
    },
    Granularity='MONTHLY',
    Metrics = [
        'UsageQuantity'
    ],
    GroupBy= [{
        'Type': 'DIMENSION',
        'Key': 'SERVICE'
    }]
)

result_by_time = response['ResultsByTime']
services = set()
for results in result_by_time:
    services = services.union(set(map(lambda x : x['Keys'][0], results['Groups'])))

print(services)