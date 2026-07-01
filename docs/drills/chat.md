# Kata: Chat System

## Prompt

Design a real-time chat system.

## Requirements to clarify

- 1:1, groups, channels?
- Online presence?
- Typing indicators?
- Message history?
- Read receipts?
- Attachments?
- End-to-end encryption?

## Expected concepts

- WebSockets or long polling
- Connection fanout
- Message persistence
- Ordering per conversation
- Push notifications
- Offline delivery
- Idempotent send
- Multi-device sync

## Stretch questions

- How do you order messages across devices?
- What happens if a user reconnects after 24 hours?
- How do you avoid duplicate sends?
- How do you scale presence?
