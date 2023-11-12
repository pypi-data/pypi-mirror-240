"""
@name: archive_backups.py
@description: This script will archive the backups according to the pre-defined
              retention policy.
@author: Pieter Paulussen
"""
import shutil
import tomllib
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from dateutil.relativedelta import relativedelta
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.columns import Columns
from rich.progress import track

custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
Console = Console(theme=custom_theme, width=250)


class Timeframe:
    def __init__(self, frame: str, count: int, keep: str = "all"):
        self.frame = frame
        self.count = count
        self.keep = keep

    @property
    def start(self):
        return datetime.now() - relativedelta(**{self.frame: self.count})

    @property
    def end(self):
        return datetime.now()

    def __str(self):
        return f"Frame: {self.frame}, Count: {self.count}, Keep: {self.keep}"

    def __repr__(self):
        return self.__str()

    def applies(self, timestamp):
        return self.start < timestamp < self.end


class ArchivePolicy:
    """A strategy defines the retention policy of a backup.

    A retention policy can be defined in multiple ways. Either by specifying the number
    of backups to keep or by specifying the number of days to keep backups.

    The latter can also be combined with the number of backups to keep. For example, if
    you want to keep 3 days of backups regardless of the number of backups, you can
    specify the following:
    [
        {
            "type": "days",
            "count": 3,
        },
        {
            "type": "weeks",
            "count": 1,
        },
        {
            "type": "months",
            "count": 1,
        },
        {
            "type": "years",
            "count": 1,
        },
    ]

    The above list is interpreted as follows:
    - Keep 3 days of backups, regardless of the number of backups
    - Anything older than 3 days, Keep for 1 week, regardless of the number of backups
    - Anything older than 1 week, Keep for 1 month, regardless of the number of backups
    - Anything older than 1 month, Keep for 1 year, regardless of the number of backups

    When a backup moves from one retention policy to another, it is moved to a different
    directory. For example, if a backup is older than 3 days, it will be moved to the
    weekly directory. If a backup is older than 1 week, it will be moved to the monthly
    directory. If a backup is older than 1 month, it will be moved to the yearly
    directory.

    You can also specify the number of backups to keep. For example, if you want to keep
    1 backup for 4 weeks, you can specify the following:
    [
        {
            "type": "weeks",
            "count": 3,
            "keep": 1,
        },
    ]

    Note that the "keep" parameter is optional. If you don't specify it, all backups
    will be kept.

    Also note that the policies are cumulative. If you specify the following:
    [
        {
            "type": "weeks",
            "count": 3,
            "keep": 1,
        },
        {
            "type": "months",
            "count": 1,
            "keep": 1,
        },
    ]

    Then the following will happen:
    - Keep 1 backup for 3 weeks
    - Keep 1 backup for 1 month
    - Anything older than 1 month will be deleted.

    """

    def __init__(self, data=None):
        if data is None or (isinstance(data, list) and len(data) == 0):
            data = [{"type": "days", "count": 1}]
        self._data = data
        self._validate_policy()
        self._timeframes = self._get_timeframes()

    def _validate_policy(self):
        """Validate the policy."""
        if not isinstance(self._data, list):
            raise ValueError(
                f"Invalid retention policy definition. Expected a list, got "
                f"{type(self._data)}"
            )
        for frame in self._data:
            if not isinstance(frame, dict):
                raise ValueError(
                    f"Invalid retention policy item: {frame}. Expected a dictionary, "
                    f"got {type(frame)}"
                )
            if frame["type"] not in ["days", "weeks", "months", "years"]:
                raise ValueError(
                    f"Invalid retention policy. Type {frame['type']} is not "
                    f"supported."
                )
            if frame["count"] < 0:
                raise ValueError(
                    f"Invalid retention policy. Count must be greater or equal to 0."
                )
            if "keep" in frame:
                if frame["keep"] != "all" and frame["keep"] < 0:
                    raise ValueError(
                        f"Invalid retention policy. Keep must be greater than 0."
                    )

    # TODO: apply a check for overlapping timeframes

    def _get_timeframes(self):
        """Return a list of start and end datetime objects for each timeframe."""
        timeframes = []
        for policy in self._data:
            values = {
                "frame": policy["type"],
                "count": policy["count"],
            }
            if "keep" in policy:
                values["keep"] = policy["keep"]

            timeframes.append(Timeframe(**values))

        # Always add a "to remove" timeframe which goes back to very far
        timeframes.append(Timeframe("years", 100, keep="none"))

        return timeframes

    @property
    def timeframes(self):
        """Return a list of start and end datetime objects for each timeframe."""
        for timeframe in self._timeframes:
            yield timeframe


class ArchiveConfig:
    def __init__(self, source=None, destination=None, **kwargs):

        data = self._load_configuration_file()

        source_path = source or data["config"].get("source")
        self.source = Path(source_path) if source_path else Path.cwd()

        destination_path = destination or data["config"].get("destination")
        self.destination = Path(destination_path) if destination_path else self.source / "archive"

        dry_run = data["config"].get("dry_run", True)
        self.dry_run = kwargs.get("dry_run", dry_run)

        verbose = data["config"].get("verbose", False)
        self.verbose = kwargs.get("verbose", verbose)

        prune = data["config"].get("prune", False)
        self.prune = kwargs.get("prune", prune)

        owner = data["config"].get("owner")
        self.owner = kwargs.get("owner", owner)

        group = data["config"].get("group")
        self.group = kwargs.get("group", group)

        if kwargs.get("policies"):
            self.policy = ArchivePolicy(kwargs.get("policies"))
        else:
            policies = data.get("policies", {})
            policy_vals = []
            for frame, values in policies.items():
                if isinstance(values, dict):
                    policy_vals.append(
                        {
                            "type": frame,
                            "count": values["count"],
                            "keep": values["keep"],
                        }
                    )
                elif isinstance(values, list):
                    for value in values:
                        policy_vals.append(
                            {
                                "type": frame,
                                "count": value["count"],
                                "keep": value["keep"],
                            }
                        )
            self.policy = ArchivePolicy(policy_vals)

    def __str__(self):
        return f"ArchiveConfig(source={self.source}, destination={self.destination})"

    def __repr__(self):
        return self.__str__()

    def _load_configuration_file(self):
        """Load the configuration from a TOML file if it exists.

        Acceptable config file locations:
        - /etc/archive_strategy.toml
        - ~/.archive_strategy.toml
        - ./archive_strategy.toml

        """
        data = {}
        for path in [
            Path("/etc/archive_strategy.toml"),
            Path.home() / ".archive_strategy.toml",
            Path.cwd() / "archive_strategy.toml",
        ]:
            if path.exists():
                try:
                    data = tomllib.loads(path.read_text())
                except Exception as e:
                    raise ValueError(f"Invalid TOML file: {path}. Error: {e}")

        if not data.get("config"):
            data["config"] = {}

        return data

    def _show(self):
        headers = [
            "Source", "Destination", "Dry Run", "Verbose", "Prune", "Owner", "Group"
        ]
        values = [
            self.source,
            self.destination,
            self.dry_run,
            self.verbose,
            self.prune,
            self.owner,
            self.group,
        ]
        left = "\n".join(f"[info]{x}:[/info]" for x in headers)
        right = "\n".join(str(x) for x in values)
        columns = Columns([left, right], equal=True)
        Console.print(columns)


class Backup:
    def __init__(self, path, parent):
        self.path = Path(path)
        self.parent = parent
        self.config = parent.config
        self.owner = self.path.owner()
        self.group = self.path.group()
        self.timeframe = None

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def timestamp(self):
        """If the filenames first part contains an int and an underscore, use that
        as the timestamp. Otherwise, use the file's last modified timestamp.
        """
        try:
            first_part = self.name.split("_")[0]
            timestamp = datetime.fromtimestamp(int(first_part))
        except ValueError:
            timestamp = datetime.fromtimestamp(self.path.stat().st_mtime)
        return timestamp

    @property
    def age(self) -> str:
        """Return the age of the backup in human readable format: 1m 2w 2d 3h 5m"""
        age = datetime.now() - self.timestamp
        days = age.days
        hours, remainder = divmod(age.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        weeks, days = divmod(days, 7)
        age = f"{weeks}w {days}d {hours}h {minutes}m"
        return age

    @property
    def week(self):
        return self.timestamp.isocalendar()[1]

    @property
    def size(self):
        """Get the size of the backup file in human readable format: example: 1.2 GB"""
        bytesize = self.path.stat().st_size

        file_size_megabytes = bytesize / (1024 * 1024)
        file_size_gigabytes = bytesize / (1024 * 1024 * 1024)
        if file_size_gigabytes > 1:
            size = f"{file_size_gigabytes:.2f} GB"
        elif file_size_megabytes > 1:
            size = f"{file_size_megabytes:.2f} MB"
        else:
            size = f"{bytesize} bytes"

        return size

    @property
    def to_delete(self) -> bool:
        if not self.timeframe:
            return False
        if self.timeframe.keep == "none":
            return True
        if self.timeframe.keep == "all":
            return False
        if self.timeframe.keep > 0 and len(self.parent.backups) > 1:
            # Check if there are more backups in the same timeframe
            backups = [
                backup
                for backup in self.parent.backups
                if backup.timeframe == self.timeframe
            ]
            # Sort the backups by timestamp (newest first)
            backups = sorted(backups, reverse=True)
            evaluated_backups = set()

            if self.timeframe.frame in ["hours", "days"]:
                if backups.index(self) > self.timeframe.keep - 1:
                    return True
                return False

            if self.timeframe.frame == "weeks":
                weeks = defaultdict(list)

                for backup in backups:
                    weeks[backup.week].append(backup)

                for week, weekly_backups in weeks.items():
                    weekly_backups = sorted(weekly_backups, reverse=True)
                    if self in weekly_backups:
                        if weekly_backups.index(self) > self.timeframe.keep - 1:
                            return True

            if self.timeframe.frame == "months":
                months = defaultdict(list)

                for backup in backups:
                    months[backup.timestamp.month].append(backup)

                for month, monthly_backups in months.items():
                    monthly_backups = sorted(monthly_backups, reverse=True)
                    if self in monthly_backups:
                        if monthly_backups.index(self) > self.timeframe.keep - 1:
                            return True

            if self.timeframe.frame == "years":
                years = defaultdict(list)

                for backup in backups:
                    years[backup.timestamp.year].append(backup)

                for year, yearly_backups in years.items():
                    yearly_backups = sorted(yearly_backups, reverse=True)
                    if self in yearly_backups:
                        if yearly_backups.index(self) > self.timeframe.keep - 1:
                            return True

        return False

    @property
    def to_archive(self) -> bool:
        """If the source directory is not the same as the destination directory,
        the backup file should be moved into the archive."""
        if self.config.source == self.config.destination:
            return False
        elif self.path.parent == self.config.source:
            return True
        else:
            return False

    @property
    def update_owner(self):
        """Update the owner of the backup file, but only if the owner is not the same
        as the owner passed through the archive configuration.
        """
        if self.config.owner is None:
            return False
        elif self.owner != self.config.owner:
            return True
        else:
            return False

    def change_owner(self):
        """Change the owner of the backup file to the owner passed through the archive
        configuration.
        """
        if self.update_owner:
            shutil.chown(self.path, self.config.owner, self.config.group)
            Console.log(f"Changed owner of {self.path.name} to {self.config.owner}")

    def move_to_archive(self):
        """Move the backup to the archive directory."""
        if self.to_archive:
            if not self.config.destination.exists():
                self.config.destination.mkdir(parents=True)
            target_location = self.config.destination / self.name
            self.path = self.path.replace(target_location)

    def apply_policy(self):
        """Check which policy applies to the backup and apply it."""
        for timeframe in self.config.policy.timeframes:
            if timeframe.start < self.timestamp < timeframe.end:
                self.timeframe = timeframe
                break

    def cleanup(self):
        """Cleanup the archive directory."""
        if self.config.prune and self.to_delete:
            self.path.unlink()
            Console.log(f"Deleted {self.path.name}")

    def __repr__(self):
        return f"Backup({self.size}, age={self.age})"

    def __lt__(self, other):
        """
        Compare two Backup objects using the '<' operator.

        :param other: Another Backup object
        :return: True if the first backup is older than the second backup

        """
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        """
        Compare two Backup objects using the '>' operator.

        :param other: Another Backup object
        :return: True if the first backup is newer than the second backup

        """
        return self.timestamp > other.timestamp

    def __eq__(self, other):
        """
        Compare two Backup objects using the '==' operator.

        :param other: Another Backup object
        :return: True if the first backup is equal to the second backup

        """
        return self.path == other.path

    def __hash__(self):
        return hash(self.path)

    def __or__(self, other):
        """
        Concatenate two Backup objects using the '|' operator.

        :param other: Another Backup object
        :return: A dictionary containing the concatenated backups

        """
        return {self, other}

    def __add__(self, other):
        """
        Concatenate two Backup objects using the '+' operator.

        :param other: Another Backup object
        :return: A dictionary containing the concatenated backups

        """
        return {self, other}

    def __iter__(self):
        """
        Return an iterator over the Backup object.

        :return: Iterator over the Backup object

        """
        yield self


class Archiver:
    def __init__(self, config: ArchiveConfig):
        self.config = config
        self.backups = list()
        self._gather_backups()

    def _gather_backups(self):
        """Gather all backups from both source and destination directory."""
        backups = set()
        for backup_elem in self.config.source.rglob("*.gz"):
            backups.add(Backup(backup_elem, self))

        # When the archive directory is not a subdirectory of the source directory,
        # also gather the backups from the archive directory
        for backup_elem in self.config.destination.rglob("*.gz"):
            backups.add(Backup(backup_elem, self))

        # Sort the backups by timestamp (newest first)
        self.backups = sorted(backups, reverse=True)

    def list_backups(
            self,
            full_path: bool = False,
            timestamp: bool = False,
            timeframe: bool = False,
            to_move: bool = False,
            to_prune: bool = False,
    ):
        """Express the list of backups in table format."""
        table = Table(title="Archive")
        table.add_column("File Name")
        table.add_column("Size", justify="right")
        table.add_column("Age", justify="right", style="green")
        if timestamp:
            table.add_column("Timestamp", style="magenta")
        if timeframe:
            table.add_column("Timeframe", style="cyan")
        if to_move:
            table.add_column("Move to Archive", justify="right", style="blue")
        if to_prune:
            table.add_column("Remove", style="red")

        for backup in self.backups:
            row = [
                backup.path.absolute().as_posix() if full_path else backup.path.name,
                backup.size,
                backup.age,
            ]
            if timestamp:
                row.append(backup.timestamp.strftime("%Y-%m-%d %H:%M"))
            if timeframe:
                row.append(str(backup.timeframe) if backup.timeframe else "TBD")
            if to_move:
                row.append("Yes" if backup.to_archive else "No")
            if to_prune:
                row.append("Yes" if backup.to_delete else "No")
            table.add_row(*row)

        Console.print(table)

    def apply_policies_to_backups(self):
        """Apply the retention policies to the backups."""
        for backup in self.backups:
            backup.apply_policy()

    def archive(self):
        """Main method to archive the backups."""
        self._gather_backups()

        for backup in track(self.backups, description="Archiving..."):
            backup.apply_policy()
            backup.move_to_archive()
            backup.change_owner()
            backup.cleanup()
