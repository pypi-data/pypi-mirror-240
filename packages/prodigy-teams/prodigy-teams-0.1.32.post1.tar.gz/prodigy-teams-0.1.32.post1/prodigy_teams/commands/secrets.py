import builtins

from radicli import Arg
from wasabi import msg

from .. import ty
from ..cli import cli
from ..errors import CLIError, ProdigyTeamsErrors
from ..messages import Messages
from ..prodigy_teams_pam_sdk.models import SecretDetail, SecretSummary
from ..query import resolve_secret, resolve_secret_id
from ..ui import print_info_table, print_table_with_select
from ..util import resolve_remote_path
from ._state import get_auth_state


@cli.subcommand(
    "secrets",
    "list",
    # fmt: off
    select=Arg("--select", help=Messages.select.format(opts=list(SecretSummary.__fields__))),
    as_json=Arg("--json", help=Messages.as_json),
    # fmt: on
)
def list(
    select: ty.List[str] = ["created", "id", "name", "path"], as_json: bool = False
) -> ty.Sequence[SecretSummary]:
    """List all named pointers to secrets on the cluster"""
    client = get_auth_state().client
    res = client.secret.all()
    print_table_with_select(res.items, select=select, as_json=as_json)
    return res.items


@cli.subcommand(
    "secrets",
    "info",
    name_or_id=Arg(help=Messages.name_or_id.format(noun="secret")),
    cluster_id=Arg(help=Messages.cluster_id.format(noun="secret")),
    select=Arg(
        "--select",
        help=Messages.select.format(opts=builtins.list(SecretDetail.__fields__)),
    ),
    as_json=Arg("--json", help=Messages.as_json),
)
def info(
    name_or_id: ty.StrOrUUID,
    cluster_id: ty.Optional[ty.UUID] = None,
    select: ty.Optional[ty.List[str]] = None,
    as_json: bool = False,
) -> SecretDetail:
    """Show info about a secret on the cluster"""
    res = resolve_secret(name_or_id, broker_id=cluster_id)
    print_info_table(res, as_json=as_json, select=select)
    return res


@cli.subcommand(
    "secrets",
    "create",
    name=Arg(help=Messages.name.format(noun="secret")),
    path=Arg(help=Messages.path.format(noun="secret file")),
    exists_ok=Arg("--exists-ok", help=Messages.exists_ok),
)
def create(name: str, path: str, exists_ok: bool = False) -> ty.Optional[ty.UUID]:
    """Create a named pointer to a secret on the cluster"""
    auth = get_auth_state()
    client = auth.client
    broker_id = auth.broker_id
    path = resolve_remote_path(client, path, default_broker=auth.broker_host)
    try:
        res = client.secret.create(name=name, path=path, broker_id=broker_id)
    except ProdigyTeamsErrors.SecretExists:
        if exists_ok:
            msg.info(Messages.T001.format(noun="secret", name=name))
            return None
        raise CLIError(Messages.E002.format(noun="secret", name=name))
    except ProdigyTeamsErrors.SecretInvalid:
        raise CLIError(Messages.E004.format(noun="secret", name=name))
    except ProdigyTeamsErrors.SecretForbiddenCreate:
        raise CLIError(Messages.E003.format(noun="secret", name=name))
    msg.divider("Secret")
    msg.table(res.dict())
    return res.id


@cli.subcommand(
    "secrets",
    "delete",
    name_or_id=Arg(help=Messages.name_or_id.format(noun="secret")),
    cluster_id=Arg(help=Messages.cluster_id.format(noun="secret")),
)
def delete(
    name_or_id: ty.StrOrUUID, cluster_id: ty.Optional[ty.UUID] = None
) -> ty.UUID:
    """Delete a secret by name or ID"""
    secret_id = resolve_secret_id(name_or_id, broker_id=cluster_id)
    auth = get_auth_state()
    try:
        auth.client.secret.delete(id=secret_id)
    except (
        ProdigyTeamsErrors.SecretForbiddenDelete,
        ProdigyTeamsErrors.SecretNotFound,
    ):
        raise CLIError(Messages.E006.format(noun="secret", name=name_or_id))
    else:
        msg.good(Messages.T003.format(noun="secret", name=name_or_id))
    return secret_id
