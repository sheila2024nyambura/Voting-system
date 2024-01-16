import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Voter, Candidate, Vote

DATABASE_URL = "sqlite:///voting.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('voter_name')
def register_voter(voter_name):
    """Register a new voter."""
    session = SessionLocal()
    voter = Voter(name=voter_name)
    session.add(voter)
    session.commit()
    click.echo(f"Voter {voter_name} registered successfully.")

@cli.command()
@click.argument('candidate_name')
def register_candidate(candidate_name):
    """Register a new candidate."""
    session = SessionLocal()
    candidate = Candidate(name=candidate_name)
    session.add(candidate)
    session.commit()
    click.echo(f"Candidate {candidate_name} registered successfully.")

@cli.command()
@click.argument('voter_name')
@click.argument('candidate_name')
def vote(voter_name, candidate_name):
    """Cast a vote for a candidate."""
    session = SessionLocal()

    voter = session.query(Voter).filter_by(name=voter_name).first()
    candidate = session.query(Candidate).filter_by(name=candidate_name).first()

    if not voter or not candidate:
        click.echo("Invalid voter or candidate.")
        return

    # Check if the voter has already voted
    if session.query(Vote).filter_by(voter_id=voter.id).first():
        click.echo(f"Voter {voter_name} has already voted.")
        return

    vote = Vote(voter=voter, candidate=candidate)
    session.add(vote)
    session.commit()

    click.echo(f"Vote cast by {voter_name} for {candidate_name} successfully.")

if __name__ == '__main__':
    cli()





