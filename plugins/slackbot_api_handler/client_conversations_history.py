import logging

logging.basicConfig(level=logging.DEBUG)

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def client_conversations_history(slack_token="",
                                 channel="",
                                 retrieve_messages_from=0
                                 ):
    # WebClient insantiates a client that can call API methods
    # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
    client = WebClient(token=slack_token)
    # Store conversation history
    conversation_history = []
    # ID of the channel you want to send the message to
    channel_id = channel

    try:
        # Call the conversations.history method using the WebClient
        # conversations.history returns the first 100 messages by default
        # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination

        result = client.conversations_history(channel=channel_id, oldest=retrieve_messages_from)

        # Print results
        logging.info("{} messages found in {}".format(len(conversation_history), id))
        return result

    except SlackApiError as e:
        logging.error("Error creating conversation: {}".format(e))
        pass
