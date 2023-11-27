import jwt
import json
from datetime import datetime
import secrets
import typer
import string
import random

cli = typer.Typer()


def random_password(length: int) -> str:
    chars = string.ascii_letters + string.digits
    return str("").join(random.choices(chars, k=length))


@cli.command(name="random-password")
def get_random_password(length: int = 64):
    """generate a random password of uppercase letters, lowercase letters, and numbers"""
    if length < 1:
        typer.secho("enter a number greater than 0", fg=typer.colors.RED)
        raise typer.Exit(1)
    print(random_password(length))


def anon_payload(iat: datetime = datetime.utcnow()):
    return {
        "role": "anon",
        "iss": "supabase",
        "iat": int(iat.timestamp()),
        "exp": int(datetime.fromtimestamp(iat.timestamp()).replace(year=iat.year + 10).timestamp())
    }


def service_payload(iat: datetime = datetime.utcnow()):
    return {
        "role": "service_role",
        "iss": "supabase",
        "iat": int(iat.timestamp()),
        "exp": int(datetime.fromtimestamp(iat.timestamp()).replace(year=iat.year + 10).timestamp())
    }


def get_anon(key: str):
    return jwt.encode(payload=anon_payload(), key=key, algorithm="HS256")


@cli.command(name="anon-role")
def anon(key: str):
    """generate an anon role JWT based on a given key"""
    if not key:
        typer.secho("enter a valid key", fg=typer.colors.RED)
        raise typer.Exit(1)
    print(get_anon(key))


def get_service(key: str):
    return jwt.encode(payload=service_payload(), key=key, algorithm="HS256")


@cli.command(name="service-role")
def service(key: str):
    """generate a service role JWT based on a given key"""
    if not key:
        typer.secho("enter a valid key", fg=typer.colors.RED)
        raise typer.Exit(1)
    print(get_service(key))


def _get_key(length: int):
    return secrets.token_urlsafe(length)


@cli.command(name="key")
def get_key(length: int = 64):
    """generate a random key (minimum required by Supabase is 32 characters)"""
    if length < 32:
        typer.secho("Supabase requires a key greater than 32 characters in length", fg=typer.colors.RED)
        raise typer.Exit(1)
    print(_get_key(length))


@cli.command()
def all(length: int = 64):
    """get a full Supabase JWT set (random key, anon role JWT, and service role JWT)"""
    key = _get_key(length)
    service_key = service(key)
    anon_key = anon(key)
    print(json.dumps({
        "service_role_key": service_key,
        "anon_role_key": anon_key,
        "secret": key
    }))


if __name__ == "__main__":
    cli()
