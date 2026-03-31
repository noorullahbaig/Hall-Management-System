# Hall Management System

## Overview

Hall Management System is a Python command-line application for managing hall records, bookings, and user accounts. The project uses semicolon-delimited text files for persistence and keeps all workflows inside a single menu-driven script.

## Features

- Administrator login with hall, booking, and user-management menus
- Hall create, view, search, edit, and delete flows
- User registration, login, profile update, and booking management flows
- Booking edit and cancellation support
- Flat-file persistence for halls, users, admins, and booking IDs

## Tech Stack

- Python 3
- Command-line interface
- Text-file storage

## Project Structure

- `Assignment.py` - main application logic and menu navigation
- `hallinfo.txt` - hall master records
- `booking.txt` - booking records
- `bookingid` - booking ID counter
- `users.txt` - user account data
- `adminusers.txt` - administrator account data

## How to Run

From the repository root:

```bash
python3 Assignment.py
```

The application expects the bundled text files to remain in the same directory as `Assignment.py`.
