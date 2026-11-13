# Screenshot Logger for Digital Forensics
## Overview
This project was developed as part of my MSc Cyber Security at Ravensbourne University London.

The aim of the project is to automate digital evidence collection by capturing screenshots at configurable intervals, recording forensic metadata, generating SHA-256 hashes for integrity verification, and securely storing evidence using Google Drive API integration.

The project was designed to support digital forensic investigations by reducing manual evidence collection while maintaining forensic traceability and chain-of-custody principles.

## Key Features

- Automated screenshot capture
- SHA-256 file hashing
- Metadata logging
- Google Drive cloud upload
- OAuth2 authentication
- Time-stamped evidence collection
- Daily log generation
- Forensic evidence preservation

## Technologies Used
### Programming Language
- Python
### Libraries
- PyAutoGUI
- PyDrive
- Schedule
- Hashlib
- Datetime
- OS
## Cloud Services
- Google Drive API
- OAuth2 Authentication
## Project Architecture
The system follows a simple evidence collection workflow:

1. Capture screenshot
2. Generate timestamp
3. Calculate SHA-256 hash
4. Store forensic metadata
5. Upload evidence to Google Drive
6. Update investigation log

## Current Project Status
## Completed
- Screenshot automation
- Metadata logging
- SHA-256 integrity verification
- Cloud upload functionality
- OAuth2 authentication

## Planned Improvements
- AES encryption
- SQLite evidence database
- Advanced GUI
- OCR support
- SIEM integration
- Microsoft Sentinel integration
- Splunk integration
## Installation
## Clone Repository
git clone https://github.com/prajwolyogi/screenshot-logger-project.git

## Install Dependencies
pip install -r requirements.txt

## Google Drive Setup
This project requires your own Google Cloud credentials.

For security reasons, OAuth credentials and access tokens are not included in this repository.

1. Create a Google Cloud Project.
2. Enable Google Drive API.
3. Create OAuth credentials.
4. Save credentials as:
client_secrets.json
5. Run the application.

## Security Notice
Sensitive files are intentionally excluded from the repository:
- client_secrets.json
- mycreds.txt
- access tokens
- refresh tokens

Users must generate and provide their own credentials.

## Academic Context
This project was developed for the MSc Cyber Security programme at Ravensbourne University London.

Research focus areas:

- Digital Forensics
- Evidence Collection
- Evidence Integrity
- Chain of Custody
- Cloud-Based Forensic Storage
- Secure Authentication

## Future Development Roadmap
### Version 1.1
- Project cleanup
- Installation guide
- Improved logging

### Version 1.2
- AES encryption integration
- Configurable settings

### Version 1.3
- SQLite evidence management

### Version 2.0
- Full GUI
- OCR support
- SIEM integrations

## Author
Prajwol Yogi
MSc Cyber Security Ravensbourne University London