# Session States

## Session: The Current Conversation Thread

Represents a single, ongoing interaction between a user and your agent system.
Contains the chronological sequence of messages and actions taken by the agent (referred to Events) during that specific interaction.
A Session can also hold temporary data (State) relevant only during this conversation.

## State (session.state): Data Within the Current Conversation

Data stored within a specific Session.
Used to manage information relevant only to the current, active conversation thread (e.g., items in a shopping cart during this chat, user preferences mentioned in this session).

## Memory: Searchable, Cross-Session Information

Represents a store of information that might span multiple past sessions or include external data sources.
It acts as a knowledge base the agent can search to recall information or context beyond the immediate conversation.