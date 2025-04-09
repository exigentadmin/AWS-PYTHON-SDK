######################################################################################
# Dale Murdock 
# 2025-03-11
#
# Updates the default outbound queue of a routing profile.
######################################################################################

import boto3

i_id ='string',
rp_id='string',
doq_id='string'

client = boto3.client('connect')

response = client.update_routing_profile_default_outbound_queue(
    InstanceId= i_id,
    RoutingProfileId= rp_id,
    DefaultOutboundQueueId= doq_id
)