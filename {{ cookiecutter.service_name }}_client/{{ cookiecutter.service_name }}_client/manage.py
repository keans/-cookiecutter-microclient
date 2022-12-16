#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests

from .microclient.utils.config import CMD_BASE_URL, CMD_TOKEN, \
    CMD_USER, CMD_PASSWORD
from .microclient.microclient import MicroClient, MicroClientException


@click.group()
@click.option("--url", default=CMD_BASE_URL, show_default=True, required=True)
@click.option("-t", "--token", default=CMD_TOKEN)
@click.pass_context
def cli(ctx, url: str, token: str):
    ctx.ensure_object(dict)

    # store micro client instance in context so that it can be
    # accessed by all other subcommands
    ctx.obj["mc"] = MicroClient(base_url=url, access_token=token)


@cli.group()
@click.pass_context
def {{ cookiecutter.item_name }}s(ctx):
    """
    {{ cookiecutter.item_name }}s commands
    """


@cli.command()
@click.option(
    "-u", "--username", 
    default=CMD_USER,
    show_default=True,
    required=True
)
@click.option(
    "-p", "--password", 
    default=CMD_PASSWORD,
    show_default=True,
    required=True
)
@click.pass_context
def gettoken(ctx, username: str, password: str):
    """
    get OAuth2 bearer token
    """
    try:
        access_token = ctx.obj["mc"].get_token(
            username=username, password=password
        )

    except MicroClientException as e:
        raise click.ClickException(e)

    click.echo(access_token)


@{{ cookiecutter.item_name }}s.command()
@click.pass_context
def list(ctx):
    """
    list all {{ cookiecutter.item_name }}s
    """
    try:
        click.echo(ctx.obj["mc"].get_all())
    except MicroClientException as e:
        raise click.ClickException(e)


@{{ cookiecutter.item_name }}s.command()
@click.option("--id", required=True)
@click.pass_context
def get(ctx, id):
    """
    get {{ cookiecutter.item_name }} by given ID
    """
    try:
        click.echo(ctx.obj["mc"].get(id=id))
    except MicroClientException as e:
        raise click.ClickException(e)


@{{ cookiecutter.item_name }}s.command()
@click.option("--id", required=True)
@click.pass_context
def delete(ctx, id):
    """
    delete {{ cookiecutter.item_name }} by given ID
    """
    try:
        click.echo(ctx.obj["mc"].delete(id=id))
    except MicroClientException as e:
        raise click.ClickException(e)


@{{ cookiecutter.item_name }}s.command()
@click.option("--id", required=True)
@click.option("--name", required=True)
@click.pass_context
def create(ctx, id, name):
    """
    create {{ cookiecutter.item_name }}
    """
    try:
        click.echo(ctx.obj["mc"].create(id=id, name=name))
    except MicroClientException as e:
        raise click.ClickException(e)


@{{ cookiecutter.item_name }}s.command()
@click.option("--id", required=True)
@click.option("--name", required=True)
@click.pass_context
def update(ctx, id, name):
    """
    update {{ cookiecutter.item_name }} by ID
    """
    try:
        click.echo(ctx.obj["mc"].update(id=id, name=name))
    except MicroClientException as e:
        raise click.ClickException(e)


if __name__ == "__main__":
    cli()
