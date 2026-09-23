---
title: A workspace. A world of capabilities.
description: Bring conversations, files, tools and devices together—with local intelligence and an interface that follows your work.
eyebrow: THE SHADO PLATFORM
---
## Start with a conversation

Ask a question, attach context, choose a role preset and get a streaming response. Keep several conversations available, return to earlier work and archive conversations when you're finished.

A preset brings together a role, model and available capabilities. Give a coding task a different setup from a research or writing task. Enable the tools that are relevant to the work.

{{< feature-grid >}}

## DesktopBridge: an agent with a desktop

Connect a conversation to a supported desktop target: the host desktop, a sandboxed application environment or a remote desktop. Live viewing lets you see the environment your agent is interacting with.

- **Host desktop:** work with supported applications on the connected host.
- **Sandboxed applications:** use configured isolated application environments.
- **Remote desktops:** connect to configured remote targets.

The target, installed software and enabled capabilities determine what the agent can do. Review permissions and supervise consequential actions.

## MobileBridge: mobile devices in the workflow

MobileBridge connects supported Android devices and virtual devices for live screen viewing and agent interaction. It brings mobile applications into the same environment as your other tools.

**MobileBridge and the iPhone app serve different purposes.** MobileBridge provides access to supported target devices. The iPhone app is a companion interface for using your SHADO server.

## An iPhone companion

Connect to your SHADO server from your iPhone. Use conversations, switch presets and access the available tools and settings through a mobile interface.

![SHADO iPhone Simulator in dark mode showing connected applications and tools](/images/iphone.webp)

*Actual dark-mode iPhone Simulator capture. Available services depend on your deployment and configuration.*

{{< downloads >}}

Store listings are coming soon. These buttons are placeholders and do not start a download.

## Arabic voice and meetings

SHADO supports Arabic interaction through chat, speech input, read-aloud and transcription capabilities. Configure the speech engines and voices available in your deployment, including NAMAA and Whisper where installed.

Use transcripts as working material for summaries, follow-up notes and further analysis. Speech quality and processing speed depend on the selected engine, recording quality and available compute.

## Files and connected applications

Work with files and configure integrations such as Nextcloud, email, calendars and cloud storage. Connected services need their own accounts, authorization and configuration.

A self-hosted SHADO server can still connect to an external service. Review the information each integration receives before using it with sensitive work.

## Tools, MCP and skills

Extend the assistant with Python tools, MCP servers and skills. Discovery and installation interfaces help you find capabilities; presets determine which installed capabilities are available to the agent.

- **Python tools:** add a self-contained tool implemented in Python.
- **MCP:** connect supported tool servers and their capabilities.
- **Skills:** add task-specific instructions and resources.
- **Presets:** combine a role, model and selected capabilities for a particular kind of work.

Third-party extensions have their own dependencies, permissions and licenses. Installing an extension is a separate decision from authorizing it for a task.

## Coding and model choice

Use the dashboard or VS Code interface for coding assistance. Configure a coding preset and give it access to the authorized project and tools.

Choose local models or configured cloud providers. Model selection affects output quality, responsiveness, hardware needs and where information is processed. [Explore deployment and data flow](/deployment/).
