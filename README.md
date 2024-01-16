# Voting System CLI Project

 This command-line application allows users to register voters, candidates, and cast votes in a simple voting system.
 
### Prerequisites

Make sure you have the following installed on your system:

- Python (version 3.8 or .10)
- Pipenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sheila2024nyambura/voting-system.git

### Usage
# Register voter
pipenv run python cli.py register-voter "Voter Name"

# Register candidate
pipenv run python cli.py register-candidate "Candidate Name"

# Vote
pipenv run python cli.py vote "Voter Name"

# Project Structure
cli.py: Main CLI script.
models.py: Defines SQLAlchemy models for Voters, Candidates, and Votes.
migrations/: Alembic migration scripts.
Pipfile and Pipfile.lock: Dependency management.
voting.db: SQLite database file.

# Licence
This project is licensed under the MIT License.

# Author
Sheila Nyambura


