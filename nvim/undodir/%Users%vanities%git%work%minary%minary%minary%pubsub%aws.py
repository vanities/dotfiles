Vim�UnDo� ���`����십�/[��f6G���W[���L   �   I            logger.warning("could not get queue url {}".format(queue_id))   o                          ]���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]��     �      �   ^    �         ^    �         ]    5�_�                            ����                                                                                                                                                                                                                                                                                                                                       	           V        ]��     �                import json   import logging   import boto35�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �                +from botocore.exceptions import ClientError5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �            �            5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��#     �                $logger = logging.getLogger(__name__)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��$     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]��$     �                 5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                  V        ]��'     �              Efrom coinmine.pubsub.services.pubsub_base import PubSub as PubSubBase5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                  V        ]��)    �              =from .pubsub.services.pubsub_base import PubSub as PubSubBase5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                v       ]��L     �      
      �      	      5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                v       ]��M    �                $logger = logging.getLogger(__name__)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       ]��Q     �            �            5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       ]��Q    �                Cfrom minary.pubsub.services.pubsub_base import PubSub as PubSubBase5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       ]��Z     �            �            5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       ]��\    �                import logging5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             ]���     �   	         5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             ]���     �   
   �      �   
         5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       ]���    �   �   �             class AWSPubSub(PubSubBase):       def configure(self):           try:   V            topic_id = self.key("sns", self.channel_prefix, self.env, self.channel_id)   V            queue_id = self.key("sqs", self.channel_prefix, self.env, self.channel_id)   F            self.psp = PubSubProducer(topic_id, queue_id, self.region)                self.psp.configure()       F            self.psc = PubSubConsumer(self.psp.queue_url, self.region)            except ClientError as e:               logger.error(   P                "Client Error on pubsub uuid={} e={}".format(self.channel_id, e)               )           except Exception as e:               logger.error(   U                "Could not initialize pubsub uuid={} e={}".format(self.channel_id, e)               )           def publish(self, message):           try:   %            self.psp.publish(message)           except Exception as e:               logger.error(   U                "Could not publish to pubsub uuid={} e={}".format(self.channel_id, e)               )           def subscribe(self):           try:                self.psp.subscribe()           except Exception as e:               logger.error(   W                "Could not subscribe to pubsub uuid={} e={}".format(self.channel_id, e)               )           def get_message(self):   %        return self.psc.get_message()       <    def key(self, service, channel_prefix, env, channel_id):   T        return "minary-{}-{}-{}-{}".format(service, channel_prefix, env, channel_id)           def close(self):           pass           def cleanup(self):           self.psp.cleanup()           class PubSubProducer:   3    def __init__(self, topic_id, queue_id, region):            self.topic_id = topic_id            self.queue_id = queue_id           self.region = region               self.topic_arn = None           self.queue_url = None   $        self.subscription_arn = None           def configure(self):   ?        self.sns = boto3.client("sns", region_name=self.region)   ?        self.sqs = boto3.client("sqs", region_name=self.region)   ?        self.sts = boto3.client("sts", region_name=self.region)       :        self.topic_arn = self._create_topic(self.topic_id)   ;        self.queue_url = self._get_queue_url(self.topic_id)   !        # create queue if missing           if not self.queue_url:   >            self.queue_url = self._create_queue(self.topic_id)   <        self.queue_arn = self._get_queue_arn(self.queue_url)   '        self._add_permission_to_queue()       &    def _create_topic(self, topic_id):   <        response = self.sns.create_topic(Name=self.topic_id)   (        topic_arn = response["TopicArn"]   9        logger.info("topic created {}".format(topic_arn))           return topic_arn       '    def _get_queue_url(self, queue_id):           queue_url = None           try:   F            response = self.sqs.get_queue_url(QueueName=self.queue_id)   ,            queue_url = response["QueueUrl"]   ;            logger.info("found queue {}".format(queue_url))               return queue_url           except Exception as e:   N            logger.warning("could not get queue url {}".format(self.queue_id))           return queue_url       &    def _create_queue(self, queue_id):   )        response = self.sqs.create_queue(   $            QueueName=self.queue_id,   P            Attributes={"DelaySeconds": "0", "MessageRetentionPeriod": "86400"},   	        )   (        queue_url = response["QueueUrl"]   9        logger.info("queue created {}".format(queue_url))           return queue_url       (    def _get_queue_arn(self, queue_url):   1        response = self.sqs.get_queue_attributes(   ;            QueueUrl=queue_url, AttributeNames=["QueueArn"]   	        )   6        queue_arn = response["Attributes"]["QueueArn"]   ;        logger.info("found queue arn {}".format(queue_arn))           return queue_arn       '    def _add_permission_to_queue(self):           # get account id   1        response = self.sts.get_caller_identity()   (        account_id = response["Account"]   ;        logger.info("got account id {}".format(account_id))               # set permissions   &        self.sqs.set_queue_attributes(   $            QueueUrl=self.queue_url,               Attributes={   %                "Policy": json.dumps(                       {   0                        "Version": "2008-10-17",   F                        "Id": "arn:aws:sqs:{}:{}:{}/SQSPolicy".format(   B                            self.region, account_id, self.queue_id                           ),   &                        "Statement": [                               {   8                                "Sid": "SNSSendMessage",   2                                "Effect": "Allow",   1                                "Principal": "*",   <                                "Action": "SQS:SendMessage",   ;                                "Resource": self.queue_arn,   .                                "Condition": {   R                                    "ArnEquals": {"aws:SourceArn": self.topic_arn}   "                                },                               }                           ],                       }                   )               },   	        )   1        logger.info("added permissions to queue")           def publish(self, message):   N        self.sns.publish(TopicArn=self.topic_arn, Message=json.dumps(message))           def subscribe(self):   &        response = self.sns.subscribe(   $            TopicArn=self.topic_arn,               Protocol="sqs",   $            Endpoint=self.queue_arn,   '            ReturnSubscriptionArn=True,   	        )   ;        self.subscription_arn = response["SubscriptionArn"]           def cleanup(self):   V        # WARN this is probably not something you want to use in prod, just in testing   6        self.sns.delete_topic(TopicArn=self.topic_arn)   C        self.sns.unsubscribe(SubscriptionArn=self.subscription_arn)   6        self.sqs.delete_queue(QueueUrl=self.queue_url)           class PubSubConsumer:   *    def __init__(self, queue_url, region):   "        self.queue_url = queue_url   :        self.sqs = boto3.client("sqs", region_name=region)           def get_message(self):           message = None           try:   H            response = self.sqs.receive_message(QueueUrl=self.queue_url)   2            message_dict = response["Messages"][0]   :            receipt_handle = message_dict["ReceiptHandle"]   3            body = json.loads(message_dict["Body"])   1            message = json.loads(body["Message"])       0            # Delete received message from queue   $            self.sqs.delete_message(   E                QueueUrl=self.queue_url, ReceiptHandle=receipt_handle               )   K            logger.info("Received and deleted message: {}".format(message))           except Exception as e:   >            logger.warn("Could not receive or delete message")           return message           class PubSubProducer:   "    def __init__(self, env, uuid):   <        self.topic_id = "minary-sns-{}-{}".format(env, uuid)   <        self.queue_id = "minary-sqs-{}-{}".format(env, uuid)   &        self.sns = boto3.client("sns")   &        self.sqs = boto3.client("sqs")           def configure(self):   :        self.topic_arn = self._create_topic(self.topic_id)   :        self.queue_url = self._create_queue(self.topic_id)   <        self.queue_arn = self._get_queue_arn(self.queue_url)       &    def _create_topic(self, topic_id):           try:   @            response = self.sns.create_topic(Name=self.topic_id)   '            response.raise_for_status()   '            return response["TopicArn"]           except Exception as e:   *            logger.error("e={}".format(e))       &    def _create_queue(self, queue_id):           try:   F            response = self.sqs.get_queue_url(QueueName=self.queue_id)   #            # create it if missing!   +            if response.status_code != 200:   1                response = self.sqs.create_queue(   ,                    QueueName=self.queue_id,   X                    Attributes={"DelaySeconds": "0", "MessageRetentionPeriod": "86400"},                   )   +                response.raise_for_status()   '            return response["QueueUrl"]           except Exception as e:   *            logger.error("e={}".format(e))       (    def _get_queue_arn(self, queue_url):           try:   5            response = self.sqs.get_queue_attributes(   ?                QueueUrl=queue_url, AttributeNames=["QueueArn"]               )   '            response.raise_for_status()   5            return response["Attributes"]["QueueArn"]           except Exception as e:   *            logger.error("e={}".format(e))           def publish(self, message):           try:   (            response = self.sns.publish(   D                TopicArn=self.topic_arn, Message=json.dumps(message)               )   '            response.raise_for_status()           except Exception as e:   *            logger.error("e={}".format(e))       "    def subscribe(self, topic_id):           try:   U            # Since we are the queue owner, we won't have to confirm the subscription   *            response = self.sns.subscribe(   P                TopicArn=self.topic_arn, Protocol="sqs", Endpoint=self.queue_arn               )   '            response.raise_for_status()           except Exception as e:   *            logger.error("e={}".format(e))           class PubSubConsumer:   "    def __init__(self, queue_url):   "        self.queue_url = queue_url   &        self.sqs = boto3.client("sqs")           def get_message(self):           try:   H            response = self.sqs.receive_message(QueueUrl=self.queue_url)   '            response.raise_for_status()   9            message = json.loads(response["Messages"][0])   5            receipt_handle = message["ReceiptHandle"]       0            # Delete received message from queue   $            self.sqs.delete_message(   E                QueueUrl=self.queue_url, ReceiptHandle=receipt_handle               )   ?            print("Received and deleted message: %s" % message)                   return message           except Exception as e:   H            logger.error("Could not find AWS SQS queue: e={}".format(e))           return message5�_�                           ����                                                                                                                                                                                                                                                                                                                            �           �          V       ]��g     �         �                  �         �    5�_�                            ����                                                                                                                                                                                                                                                                                                                            �           �          V       ]��j    �       "   �    �       !   �    5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             ]��     �   
   �   �    �   
      �    �   	      �    5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       ]��     �   �   �       �       class AWSPubSub(PubSubBase):       def configure(self):           try:   %            self.topic_id = self.key(   E                "sns", self.channel_prefix, self.env, self.channel_id               )   %            self.queue_id = self.key(   E                "sqs", self.channel_prefix, self.env, self.channel_id               )   P            self.psp = PubSubProducer(self.topic_id, self.queue_id, self.region)                self.psp.configure()       F            self.psc = PubSubConsumer(self.psp.queue_url, self.region)            except ClientError as e:               logger.error(   P                "Client Error on pubsub uuid={} e={}".format(self.channel_id, e)               )               raise e           except Exception as e:               logger.error(   U                "Could not initialize pubsub uuid={} e={}".format(self.channel_id, e)               )               raise e           def publish(self, message):           try:   %            self.psp.publish(message)           except Exception as e:               logger.error(   U                "Could not publish to pubsub uuid={} e={}".format(self.channel_id, e)               )           def subscribe(self):           try:                self.psp.subscribe()           except Exception as e:               logger.error(   W                "Could not subscribe to pubsub uuid={} e={}".format(self.channel_id, e)               )           def get_message(self):   %        return self.psc.get_message()       <    def key(self, service, channel_prefix, env, channel_id):   T        return "minary-{}-{}-{}-{}".format(service, channel_prefix, env, channel_id)           def close(self):           pass           def cleanup(self):           self.psp.cleanup()           class PubSubProducer:   3    def __init__(self, topic_id, queue_id, region):            self.topic_id = topic_id            self.queue_id = queue_id           self.region = region               self.topic_arn = None           self.queue_url = None   $        self.subscription_arn = None           def configure(self):   ?        self.sns = boto3.client("sns", region_name=self.region)   ?        self.sqs = boto3.client("sqs", region_name=self.region)   ?        self.sts = boto3.client("sts", region_name=self.region)       :        self.topic_arn = self._create_topic(self.topic_id)   ;        self.queue_url = self._get_queue_url(self.queue_id)   !        # create queue if missing           if not self.queue_url:   >            self.queue_url = self._create_queue(self.queue_id)   <        self.queue_arn = self._get_queue_arn(self.queue_url)   '        self._add_permission_to_queue()       &    def _create_topic(self, topic_id):   7        response = self.sns.create_topic(Name=topic_id)   (        topic_arn = response["TopicArn"]   9        logger.info("topic created {}".format(topic_arn))           return topic_arn       '    def _get_queue_url(self, queue_id):           queue_url = None           try:   A            response = self.sqs.get_queue_url(QueueName=queue_id)   ,            queue_url = response["QueueUrl"]   ;            logger.info("found queue {}".format(queue_url))               return queue_url           except Exception:   I            logger.warning("could not get queue url {}".format(queue_id))           return queue_url       &    def _create_queue(self, queue_id):   )        response = self.sqs.create_queue(               QueueName=queue_id,   P            Attributes={"DelaySeconds": "0", "MessageRetentionPeriod": "86400"},   	        )   (        queue_url = response["QueueUrl"]   9        logger.info("queue created {}".format(queue_url))           return queue_url       (    def _get_queue_arn(self, queue_url):   1        response = self.sqs.get_queue_attributes(   ;            QueueUrl=queue_url, AttributeNames=["QueueArn"]   	        )   6        queue_arn = response["Attributes"]["QueueArn"]   ;        logger.info("found queue arn {}".format(queue_arn))           return queue_arn       '    def _add_permission_to_queue(self):           # get account id   1        response = self.sts.get_caller_identity()   (        account_id = response["Account"]   ;        logger.info("got account id {}".format(account_id))               # set permissions   &        self.sqs.set_queue_attributes(   $            QueueUrl=self.queue_url,               Attributes={   %                "Policy": json.dumps(                       {   0                        "Version": "2008-10-17",   F                        "Id": "arn:aws:sqs:{}:{}:{}/SQSPolicy".format(   B                            self.region, account_id, self.queue_id                           ),   &                        "Statement": [                               {   8                                "Sid": "SNSSendMessage",   2                                "Effect": "Allow",   1                                "Principal": "*",   <                                "Action": "SQS:SendMessage",   ;                                "Resource": self.queue_arn,   .                                "Condition": {   R                                    "ArnEquals": {"aws:SourceArn": self.topic_arn}   "                                },                               }                           ],                       }                   )               },   	        )   1        logger.info("added permissions to queue")           def publish(self, message):   N        self.sns.publish(TopicArn=self.topic_arn, Message=json.dumps(message))           def subscribe(self):   &        response = self.sns.subscribe(   $            TopicArn=self.topic_arn,               Protocol="sqs",   $            Endpoint=self.queue_arn,   '            ReturnSubscriptionArn=True,   	        )   ;        self.subscription_arn = response["SubscriptionArn"]           def cleanup(self):   V        # WARN this is probably not something you want to use in prod, just in testing   6        self.sns.delete_topic(TopicArn=self.topic_arn)   C        self.sns.unsubscribe(SubscriptionArn=self.subscription_arn)   6        self.sqs.delete_queue(QueueUrl=self.queue_url)           class PubSubConsumer:   *    def __init__(self, queue_url, region):   "        self.queue_url = queue_url   :        self.sqs = boto3.client("sqs", region_name=region)           def get_message(self):           message = None           try:   H            response = self.sqs.receive_message(QueueUrl=self.queue_url)   2            message_dict = response["Messages"][0]   :            receipt_handle = message_dict["ReceiptHandle"]   3            body = json.loads(message_dict["Body"])   1            message = json.loads(body["Message"])       0            # Delete received message from queue   $            self.sqs.delete_message(   E                QueueUrl=self.queue_url, ReceiptHandle=receipt_handle               )   K            logger.info("Received and deleted message: {}".format(message))           except KeyError:               pass           except Exception as e:   M            logger.warn("Could not receive or delete message e={}".format(e))           return message5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �          V       ]��   	 �               �   import json   import boto3   +from botocore.exceptions import ClientError       .from minary.pubsub import PubSub as PubSubBase    from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)               class AWSPubSub(PubSubBase):       def configure(self):           try:   %            self.topic_id = self.key(   !                self.environment,                   "sns",   $                self.channel_prefix,                   self.component,                    self.channel_id,               )   %            self.queue_id = self.key(   !                self.environment,                   "sqs",   $                self.channel_prefix,                   self.component,                    self.channel_id,               )   P            self.psp = PubSubProducer(self.topic_id, self.queue_id, self.region)                self.psp.configure()       F            self.psc = PubSubConsumer(self.psp.queue_url, self.region)            except ClientError as e:               logger.error(   P                "Client Error on pubsub uuid={} e={}".format(self.channel_id, e)               )           except Exception as e:               logger.error(   U                "Could not initialize pubsub uuid={} e={}".format(self.channel_id, e)               )           def publish(self, message):           try:   %            self.psp.publish(message)           except Exception as e:               logger.error(   U                "Could not publish to pubsub uuid={} e={}".format(self.channel_id, e)               )           def subscribe(self):           try:                self.psp.subscribe()           except Exception as e:               logger.error(   W                "Could not subscribe to pubsub uuid={} e={}".format(self.channel_id, e)               )           def get_message(self):   %        return self.psc.get_message()       O    def key(self, environment, service, channel_prefix, component, channel_id):   '        return "{}-{}-{}-{}-{}".format(   G            environment, service, channel_prefix, component, channel_id   	        )           def close(self):           pass           def cleanup(self):           self.psp.cleanup()           class PubSubProducer:   3    def __init__(self, topic_id, queue_id, region):            self.topic_id = topic_id            self.queue_id = queue_id           self.region = region               self.topic_arn = None           self.queue_url = None   $        self.subscription_arn = None           def configure(self):   ?        self.sns = boto3.client("sns", region_name=self.region)   ?        self.sqs = boto3.client("sqs", region_name=self.region)   ?        self.sts = boto3.client("sts", region_name=self.region)       :        self.topic_arn = self._create_topic(self.topic_id)   ;        self.queue_url = self._get_queue_url(self.queue_id)   !        # create queue if missing           if not self.queue_url:   >            self.queue_url = self._create_queue(self.queue_id)   <        self.queue_arn = self._get_queue_arn(self.queue_url)   '        self._add_permission_to_queue()       &    def _create_topic(self, topic_id):   7        response = self.sns.create_topic(Name=topic_id)   (        topic_arn = response["TopicArn"]   9        logger.info("topic created {}".format(topic_arn))           return topic_arn       '    def _get_queue_url(self, queue_id):           queue_url = None           try:   A            response = self.sqs.get_queue_url(QueueName=queue_id)   ,            queue_url = response["QueueUrl"]   ;            logger.info("found queue {}".format(queue_url))               return queue_url           except Exception:   I            logger.warning("could not get queue url {}".format(queue_id))           return queue_url       &    def _create_queue(self, queue_id):   )        response = self.sqs.create_queue(               QueueName=queue_id,   P            Attributes={"DelaySeconds": "0", "MessageRetentionPeriod": "86400"},   	        )   (        queue_url = response["QueueUrl"]   9        logger.info("queue created {}".format(queue_url))           return queue_url       (    def _get_queue_arn(self, queue_url):   1        response = self.sqs.get_queue_attributes(   ;            QueueUrl=queue_url, AttributeNames=["QueueArn"]   	        )   6        queue_arn = response["Attributes"]["QueueArn"]   ;        logger.info("found queue arn {}".format(queue_arn))           return queue_arn       '    def _add_permission_to_queue(self):           # get account id   1        response = self.sts.get_caller_identity()   (        account_id = response["Account"]   ;        logger.info("got account id {}".format(account_id))               # set permissions   &        self.sqs.set_queue_attributes(   $            QueueUrl=self.queue_url,               Attributes={   %                "Policy": json.dumps(                       {   0                        "Version": "2008-10-17",   F                        "Id": "arn:aws:sqs:{}:{}:{}/SQSPolicy".format(   B                            self.region, account_id, self.queue_id                           ),   &                        "Statement": [                               {   8                                "Sid": "SNSSendMessage",   2                                "Effect": "Allow",   1                                "Principal": "*",   <                                "Action": "SQS:SendMessage",   ;                                "Resource": self.queue_arn,   .                                "Condition": {   R                                    "ArnEquals": {"aws:SourceArn": self.topic_arn}   "                                },                               }                           ],                       }                   )               },   	        )   1        logger.info("added permissions to queue")           def publish(self, message):   N        self.sns.publish(TopicArn=self.topic_arn, Message=json.dumps(message))           def subscribe(self):   &        response = self.sns.subscribe(   $            TopicArn=self.topic_arn,               Protocol="sqs",   $            Endpoint=self.queue_arn,   '            ReturnSubscriptionArn=True,   	        )   ;        self.subscription_arn = response["SubscriptionArn"]           def cleanup(self):   V        # WARN this is probably not something you want to use in prod, just in testing   6        self.sns.delete_topic(TopicArn=self.topic_arn)   C        self.sns.unsubscribe(SubscriptionArn=self.subscription_arn)   6        self.sqs.delete_queue(QueueUrl=self.queue_url)           class PubSubConsumer:   *    def __init__(self, queue_url, region):   "        self.queue_url = queue_url   :        self.sqs = boto3.client("sqs", region_name=region)           def get_message(self):           message = None           try:   0            response = self.sqs.receive_message(   ;                QueueUrl=self.queue_url, WaitTimeSeconds=20               )   2            message_dict = response["Messages"][0]   :            receipt_handle = message_dict["ReceiptHandle"]   3            body = json.loads(message_dict["Body"])   1            message = json.loads(body["Message"])       0            # Delete received message from queue   $            self.sqs.delete_message(   E                QueueUrl=self.queue_url, ReceiptHandle=receipt_handle               )   K            logger.info("Received and deleted message: {}".format(message))           except KeyError:               pass           except Exception as e:   M            logger.warn("Could not receive or delete message e={}".format(e))           return message5�_�                    '        ����                                                                                                                                                                                                                                                                                                                            �           �          V       ]��     �   '   )   �                  �   '   )   �    5�_�                    #       ����                                                                                                                                                                                                                                                                                                                            �           �          V       ]��   
 �   #   %   �    �   #   $   �    5�_�                     o       ����                                                                                                                                                                                                                                                                                                                            �           �          V       ]���    �   n   p   �      I            logger.warning("could not get queue url {}".format(queue_id))5��