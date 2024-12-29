Telegram Auto-Forwarder
  A simple Python script that automatically forwards messages from one Telegram group or channel to another group or multiple groups using a Telegram user account.

Features:
  Real-Time Forwarding: Forwards messages from a source group/channel to one or more target groups/channels.
  Multiple Targets: Supports forwarding to multiple groups or channels simultaneously.
  User Account: Works with a Telegram user account, enabling participation in private groups and channels.
  
Prerequisites:
  1. Python and Libraries
    Install Python (3.8 or later recommended).
    Required Python libraries:
      pyrogram
3. Telegram API Credentials
  Obtain your API ID and API Hash from Telegram's Developer Portal.
4. Group and Channel Access
  Ensure the account running the script:
    Is a member of the source group/channel.
    Has permission to send messages in the target group/channel.

Installation:
  Clone the Repository:
  git clone https://github.com/your-username/telegram-auto-forwarder.git
  cd telegram-auto-forwarder

Set Up the Script:
  Open telegram_forwarder.py.
  Replace placeholders with your credentials and group/channel IDs:
  YOUR_API_ID: Your Telegram API ID.
  YOUR_API_HASH: Your Telegram API Hash.
  source_group_or_channel: The source group/channel username or ID.
  target_group_or_channel_1, target_group_or_channel_2: Target group/channel usernames or IDs.
  
Run the Script:
python telegram_forwarder.py

Usage:
First Run:
  On the first run, you’ll be prompted to log in to your Telegram account.
  Enter your phone number and verification code.
  
Message Forwarding:
  The script will monitor the source group/channel for new messages and forward them to the target groups/channels in real-time.
  
Troubleshooting:
  Ensure the account is a member of both the source and target groups/channels.
  Check permissions:
  Can read messages in the source.
  Can send messages in the target.
  Use print() statements in the script to debug errors.
