import json

import redis

from utils import byte_to_string, string_to_bytes

redis_host = "localhost"
redis_port = 6379

redis_client = redis.StrictRedis(
    host=redis_host, port=redis_port, decode_responses=True
)


def get_chat_messages() -> list:
    messages = redis_client.get("messages")

    if messages is None:
        return []
    else:
        messages = json.loads(messages)
        for message in messages:
            if message["role"] == "user" and message["images"]:
                message["images"][0] = string_to_bytes(message["images"][0])

    return messages


def update_chat_messages(new_message):
    old_messages = get_chat_messages()
    for message in old_messages:
        if message["role"] == "user" and message["images"]:
            message["images"][0] = byte_to_string(message["images"][0])

    messages = old_messages + [new_message]

    redis_client.set("messages", json.dumps(messages))


def clear_chat_history():
    redis_client.delete("messages")
