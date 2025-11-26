class A2AProtocol:
    """Skeleton message passing structure for agent-to-agent communication."""

    def create_message(self, sender: str, receiver: str, msg_type: str, payload: dict):
        return {
            "sender": sender,
            "receiver": receiver,
            "type": msg_type,
            "payload": payload,
        }
